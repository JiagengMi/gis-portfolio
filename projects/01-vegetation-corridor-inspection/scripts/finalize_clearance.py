"""Curated session algorithm; prepare exact Near/Inside inputs before running."""
import argparse
from collections import Counter
import math


def classify(distance):
    if distance is None or not math.isfinite(distance) or distance < 0:
        return 'Unknown'
    return 'High' if distance < 2 else ('Medium' if distance < 4 else 'Low')


def resolve(near_distance, near_span, inside_spans):
    ids = sorted(set(inside_spans))
    if ids:
        return (0.0, ids[0], '; '.join(ids), len(ids), 'Inside3D', 'High')
    if near_span and classify(near_distance) != 'Unknown':
        return (near_distance, near_span, None, 0, 'Near3D', classify(near_distance))
    return (None, None, None, 0, 'Unknown', 'Unknown')


def run(canopies, conductors, relations):
    import arcpy

    output_fields = [('clearance_m', 'DOUBLE', None), ('nearest_span_id', 'TEXT', 20),
                     ('inside_span_ids', 'TEXT', 2000), ('inside_count', 'LONG', None),
                     ('distance_method', 'TEXT', 30), ('risk_class', 'TEXT', 10)]
    for path in (canopies, conductors, relations):
        if not arcpy.Exists(path):
            raise ValueError('Missing input: ' + path)
    existing = {f.name.lower() for f in arcpy.ListFields(canopies)}
    if any(name.lower() in existing for name, _, _ in output_fields):
        raise ValueError('Final fields already exist; use a deliberately prepared analysis copy.')
    spans, seen = {}, set()
    with arcpy.da.SearchCursor(conductors, ['OID@', 'span_id']) as cursor:
        for oid, sid in cursor:
            if not sid or sid in seen:
                raise ValueError('Empty/duplicate span ID.')
            spans[oid] = sid
            seen.add(sid)
    rows, veg_ids, canopy_ids = [], set(), set()
    with arcpy.da.SearchCursor(canopies, ['OID@', 'veg_id', 'NEAR_FID', 'NEAR_DIST3']) as cursor:
        for row in cursor:
            oid, vid, _, _ = row
            if not vid or vid in veg_ids:
                raise ValueError('Empty/duplicate veg_id.')
            veg_ids.add(vid)
            canopy_ids.add(oid)
            rows.append(row)
    if len(rows) != 241 or len(spans) != 73:
        raise ValueError('Expected 241 canopies and 73 spans.')
    inside = {}
    with arcpy.da.SearchCursor(relations, ['Target_ID', 'Contain_ID', 'Status']) as cursor:
        for target, container, status in cursor:
            if target not in spans or container not in canopy_ids:
                raise ValueError('Unmatched relationship IDs; verify exact tool inputs.')
            if status not in ('Inside', 'Partially Inside'):
                raise ValueError('Unexpected Inside 3D status: ' + str(status))
            inside.setdefault(container, set()).add(spans[target])
    prepared = {}
    for oid, _, near_id, distance in rows:
        values = resolve(distance, spans.get(near_id), inside.get(oid, set()))
        if values[2] and len(values[2]) > 2000:
            raise ValueError('Inside span list exceeds field width.')
        prepared[oid] = values
    for name, kind, length in output_fields:
        if length:
            arcpy.management.AddField(canopies, name, kind, field_length=length)
        else:
            arcpy.management.AddField(canopies, name, kind)
    fields = ['OID@'] + [name for name, _, _ in output_fields]
    with arcpy.da.UpdateCursor(canopies, fields) as cursor:
        for row in cursor:
            row[1:] = prepared[row[0]]
            cursor.updateRow(row)
    counts, checked = Counter(), 0
    with arcpy.da.SearchCursor(canopies, fields) as cursor:
        for row in cursor:
            expected = prepared[row[0]]
            if expected[0] is None:
                if row[1] is not None:
                    raise ValueError('Unexpected stored distance.')
            elif row[1] is None or abs(row[1]-expected[0]) > 1e-6:
                raise ValueError('Stored distance check failed.')
            if tuple(row[2:]) != expected[1:]:
                raise ValueError('Stored attributes check failed.')
            counts[row[-1]] += 1
            checked += 1
    if checked != 241:
        raise ValueError('Stored count check failed.')
    print('Verified canopy results:', checked, dict(counts))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ('canopies', 'conductors', 'relations'):
        parser.add_argument('--' + name, required=True)
    args = parser.parse_args()
    run(args.canopies, args.conductors, args.relations)
