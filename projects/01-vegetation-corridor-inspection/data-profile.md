# Public Trees sample profile

Profile date: 2026-09-28

## Scope

- Source: City of Calgary Open Data, Public Trees (`tfs4-3wwa`)
- Bounding box: north 51.080, west -114.140, south 51.070, east -114.125
- Formats retained: GeoJSON and CSV
- Feature count: 618
- Geometry count: 618

## Initial quality checks

| Check | Result |
|---|---:|
| Records | 618 |
| GeoJSON features | 618 |
| Missing point geometry | 0 |
| Unique `wam_id` values | 618 |
| Missing `wam_id` values | 0 |
| Unique `tree_asset_cd` values | 17 |
| Unique common-name values | 64 |
| DBH range among populated values | 2–125 cm |

## Modelling decisions

- Use `wam_id`, not `tree_asset_cd`, as the source identifier in the portfolio workflow because `wam_id` is unique across this downloaded sample.
- Preserve the raw source files unchanged.
- Create processed layers separately and retain only fields required for the demonstration.
- Do not interpret the source tree-condition field as corridor risk. Corridor risk will be synthetic or derived under a documented portfolio rule.
- Do not publish appraised-value fields because they are unnecessary for the inspection use case.

## Fields likely to retain

- `wam_id`
- `common_name`
- `genus`
- `species`
- `dbh_cm`
- `mature_size`
- `tree_condition_rating_perc`
- `comm_code`
- `location_detail`
- `modified_dt`
- point geometry

