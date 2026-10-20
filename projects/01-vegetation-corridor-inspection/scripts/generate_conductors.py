"""Curated session algorithm; exact archived file not ArcPy-rerun at closeout."""
import argparse
import math
import os


def run(gdb, output_name, step):
    import arcpy

    if not math.isfinite(step) or step <= 0:
        raise ValueError('Sampling step must be positive and finite.')
    spans, poles = (os.path.join(gdb, name) for name in ('spans', 'poles'))
    output = os.path.join(gdb, output_name)
    for path in (spans, poles):
        if not arcpy.Exists(path):
            raise ValueError('Missing input: ' + path)
        if arcpy.Describe(path).spatialReference.factoryCode not in (3776, 102187):
            raise ValueError('Expected EPSG:3776 or equivalent: ' + path)
    if arcpy.Exists(output):
        raise ValueError('Output exists; no overwrite: ' + output)
    sr = arcpy.Describe(spans).spatialReference
    pole_data = {}
    with arcpy.da.SearchCursor(poles, ['pole_id', 'SHAPE@XY', 'ground_z_m', 'attach_h_m']) as cursor:
        for pid, xy, ground, attach in cursor:
            pid = (pid or '').strip()
            if not pid or pid in pole_data:
                raise ValueError('Empty/duplicate pole ID: ' + pid)
            if any(v is None or not math.isfinite(v) for v in (*xy, ground, attach)) or attach <= 0:
                raise ValueError('Invalid pole coordinates/heights: ' + pid)
            pole_data[pid] = (*xy, ground + attach)
    fields = ['span_id', 'from_pole_id', 'to_pole_id', 'sag_m', 'sample_step_m', 'SHAPE@']
    prepared, expected, seen_pairs = [], {}, set()
    with arcpy.da.SearchCursor(spans, fields) as cursor:
        for sid, fr, to, sag, _, geom in cursor:
            sid, fr, to = ((value or '').strip() for value in (sid, fr, to))
            if not sid or sid in expected or fr not in pole_data or to not in pole_data or fr == to:
                raise ValueError('Invalid/duplicate span or pole reference: ' + sid)
            pair = tuple(sorted((fr, to)))
            if pair in seen_pairs:
                raise ValueError('Duplicate pole pair: ' + sid)
            seen_pairs.add(pair)
            if sag is None or not math.isfinite(sag) or sag < 0:
                raise ValueError('Invalid sag: ' + sid)
            if geom is None or geom.partCount != 1 or geom.pointCount != 2:
                raise ValueError('Expected a two-vertex single-part span: ' + sid)
            for point, pid in ((geom.firstPoint, fr), (geom.lastPoint, to)):
                candidates = [key for key, xyz in pole_data.items()
                              if math.hypot(point.X-xyz[0], point.Y-xyz[1]) <= 0.1]
                if candidates != [pid]:
                    raise ValueError(f'{sid}: endpoint candidates {candidates}, expected {pid}')
            a, b = pole_data[fr], pole_data[to]
            length = math.dist(a[:2], b[:2])
            if length <= 0:
                raise ValueError('Zero length: ' + sid)
            n = max(2, math.ceil(length / step))
            n += n % 2
            points = []
            for i in range(n + 1):
                t = i / n
                points.append(arcpy.Point((1-t)*a[0]+t*b[0], (1-t)*a[1]+t*b[1],
                                          (1-t)*a[2]+t*b[2]-4*sag*t*(1-t)))
            line = arcpy.Polyline(arcpy.Array(points), sr, True, False)
            prepared.append([sid, fr, to, sag, step, line])
            expected[sid] = (a, b, ((a[0]+b[0])/2, (a[1]+b[1])/2, (a[2]+b[2])/2-sag))
    if len(prepared) != 73:
        raise ValueError(f'Expected 73 spans, found {len(prepared)}; output not created.')
    arcpy.management.CreateFeatureclass(gdb, output_name, 'POLYLINE', has_z='ENABLED',
                                        has_m='DISABLED', spatial_reference=sr)
    for name in fields[:3]:
        arcpy.management.AddField(output, name, 'TEXT', field_length=20)
    for name in fields[3:5]:
        arcpy.management.AddField(output, name, 'DOUBLE')
    with arcpy.da.InsertCursor(output, fields) as cursor:
        for row in prepared:
            cursor.insertRow(row)
    checked = 0
    with arcpy.da.SearchCursor(output, ['span_id', 'SHAPE@']) as cursor:
        for sid, geom in cursor:
            a, b, mid = expected[sid]
            vertices = list(geom.getPart(0))
            midpoint = min(vertices, key=lambda p: math.hypot(p.X-mid[0], p.Y-mid[1]))
            for point, target in ((geom.firstPoint, a), (geom.lastPoint, b), (midpoint, mid)):
                if math.dist((point.X, point.Y, point.Z), target) > 0.01:
                    raise ValueError('Written geometry check failed: ' + sid)
            if any(math.hypot(q.X-p.X, q.Y-p.Y) > step+0.001 for p, q in zip(vertices, vertices[1:])):
                raise ValueError('Written sample spacing check failed: ' + sid)
            checked += 1
    if checked != 73:
        raise ValueError('Written count check failed.')
    print(f'Checked {checked} spans; output: {output}')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--gdb', required=True)
    parser.add_argument('--output', required=True)
    parser.add_argument('--step', type=float, default=0.25)
    args = parser.parse_args()
    run(args.gdb, args.output, args.step)
