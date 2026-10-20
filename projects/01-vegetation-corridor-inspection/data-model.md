# Implemented data model

English field names are retained in the GDB; readable English aliases are used in pop-ups. Working coordinates are EPSG:3776 (ArcGIS may report equivalent 102187), metres.

| Dataset | Geometry | Role / fields |
|---|---|---|
| vegetation_canopy | 2D polygon | `veg_id`, `ground_z_m`, `tree_h_m`, `crown_base_m`, `crown_base_z`, `crown_depth_m`, footprint/height source fields |
| poles | 2D point | `pole_id`, `ground_z_m`, `attach_h_m`; actual field `pole_z_m=14` represents synthetic above-ground pole height |
| spans | 2D polyline | `span_id`, `from_pole_id`, `to_pole_id`, `sag_m`, `sample_step_m` |
| vegetation_3d_closed | Closed multipatch | Enclosed canopy geometry, restored business attributes, `IsClosed` |
| conductors_3d | Z-enabled polyline | 73 original nominal 0.5 m curves; stable span IDs |
| conductors_3d_025m | Z-enabled polyline | 73 regenerated 0.25 m curves; endpoints/midpoints checked |
| vegetation_clearance | Multipatch | 0.5 m analysis baseline; raw Near and final clearance fields |
| vegetation_clearance_025m | Multipatch | Final 0.25 m analysis and `risk_class` |
| conductor_canopy_inside_025m | Nonspatial table | `Target_ID` = fine conductor OBJECTID; `Contain_ID` = final canopy OBJECTID; `Status` |
| clearance_risk_counts | Nonspatial table | Frequency by `risk_class` |

The coarse relationship table has the same logical role; its actual name/location must be checked in the current project. A table lookup initially failed because the assumed path did not match its saved location.

## Final result fields

| Field | Type | Meaning |
|---|---|---|
| veg_id | Text | Stable canopy identifier |
| NEAR_FID | Integer | Nearest conductor OBJECTID in the exact Near 3D input |
| NEAR_DIST3 | Double | Raw 3D surface distance; not independently a solid clearance |
| clearance_m | Double | Internal relationship → 0; otherwise valid NEAR_DIST3 |
| nearest_span_id | Text | Closest span or deterministic representative of tied internal spans |
| inside_span_ids | Text | All internal-related span IDs, separated by semicolons |
| inside_count | Integer | Number of distinct internal-related spans |
| distance_method | Text | Inside3D / Near3D / Unknown |
| risk_class | Text | High / Medium / Low / Unknown |

Never join a regenerated table using assumed row order. After Enclose Multipatch, restore attributes from the **immediate input** via `OID_ORIG`, not a different source's OBJECTID. Recompute Z_MIN/Z_MAX on the enclosed geometry rather than copying old bounds.

## Context and deferred schema

17 corridors, 17 inspection zones, a 9 m corridor buffer, and an empty vegetation observations layer were present in the initial audit. Their existence does not prove that every zone parameter or geometry was verified. The public release does not implement observation forms, attachments, QC status transitions, mobile collection, or a dashboard.
