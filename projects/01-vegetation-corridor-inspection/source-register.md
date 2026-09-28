# Source register

| Source | Intended use | Status | Attribution / notes |
|---|---|---|---|
| City of Calgary Public Trees | Real vegetation asset locations and selected descriptive attributes | Downloaded 2026-09-28 | 618 features from Socrata dataset `tfs4-3wwa`; City of Calgary Open Data; query extent: north 51.080, west -114.140, south 51.070, east -114.125 |
| City of Calgary Tree Canopy 2022 | Optional contextual vegetation polygon layer | Candidate | Derived from orthophotos and LiDAR; quality controlled by the City; use only if it improves the map |
| Synthetic corridor polylines | Demonstration infrastructure | Planned | Created solely for this portfolio project; not real utility infrastructure |
| Synthetic inspection zones | Assignment and reporting workflow | Planned | Created solely for this portfolio project |
| Synthetic or field-test observations | Form, QC, and dashboard testing | Planned | Explicitly label each record through `data_origin` |

## Data minimization decision

Use a small Calgary study area and a limited number of records. The purpose is to demonstrate workflow design, not to reproduce a citywide asset database. This keeps the application responsive, reduces ArcGIS Online storage consumption, and makes testing auditable.

## Local source files

- `data/source/calgary-public-trees-study-area.geojson`
- `data/source/calgary-public-trees-study-area.csv`

API query predicate:

```text
within_box(point,51.080,-114.140,51.070,-114.125)
```

