# Validation record

Source: operator-run Pro console/table screenshots in the project session. Recorded 2026-10-20; no closeout geoprocessing rerun.

## Known geometry

A closed 10 × 10 × 10 m cube spans Z=1000–1010. Is Closed 3D returned Yes.

| Case | Expected solid clearance (m) | Near 3D (m) | Inside 3D |
|---|---:|---:|---|
| Side_3m | 3 | 3 | No relationship |
| Above_5m | 5 | 5 | No relationship |
| Diagonal | √34 ≈ 5.830952 | 5.830952 | No relationship |
| Crossing | 0 | 0 | Partially Inside |
| Fully_inside | 0 | 4 | Inside |

The contained case explains the correction step. The combined method matches all five expected clearances. These tests are not exhaustive coverage of tangencies, degenerate geometry, or multipatch topology.

## Project geometry

- 241 closed canopy results, with business attributes restored using the immediate input's OBJECTID.
- 73 spans after endpoint snapping and ID checks. S-062 needed manual endpoint corrections before batch generation passed.
- S-001: P-001 → P-002; endpoints Z=1012 m; midpoint Z=1011 m; 97 original vertices.
- Both batches passed endpoint/midpoint checks; the refined batch also checked planar sampling intervals.
- 21 internal relationships affect 16 distinct canopies. Final zero clearance affects 52 canopies, including other contact/intersection cases.

## Sampling sensitivity

Curves were regenerated from the same parabola at 0.25 m, rather than densifying straight segments. Both Near 3D and Inside 3D were rerun and results compared by veg_id.

| Metric | Result |
|---|---:|
| Canopies compared | 241 |
| Maximum absolute clearance difference | 0.000134 m |
| Mean difference, rounded console output | 0.000021 m |
| Screening class changes | 0 |
| Internal canopy sets identical | Yes: 16 each |
| Zero-clearance canopy sets identical | Yes: 52 each |

Largest reported change: V-004, about 5.588227 → 5.588093 m. Rounded values are for reporting, not threshold calculations. The 0.134 mm maximum difference does **not** establish physical measurement accuracy.

## Classification

Unrounded clearance: High <2 m; Medium ≥2 and <4 m; Low ≥4 m; missing/invalid results Unknown. Final frequency output: **67 + 62 + 112 + 0 = 241**. All **52** zero-clearance cases are included in High.

## Public release

Initial release: operator incognito access passed. Revised layer addition, pop-ups, flat basemap/offsets, and app republishing were operator-completed.

Anonymous REST checks at closeout independently confirmed:

- Web Scene and Web Experience access: public; scene description and terms present.
- Final visible canopy and conductor services and feature counts: 241 / 73.
- Hosted classification counts: High 67, Medium 62, Low 112; zero clearance 52.
- Visible conductor sampling field min=max=0.25 m; anonymous service capabilities: Query.
- Both final visible layers have scene elevation offsets of −1000 m; old layers are hidden.

See [the API audit record](results/public-release-audit.json). A complete final browser/mobile visual audit and a comprehensive editing-permission audit across all dependencies were not performed. Repeat the [release checklist](implementation-plan.md) after changes.
