# Data model

Use English field names in the geodatabase and human-readable aliases in ArcGIS Online. Final types may be adjusted after testing the source data.

## 1. Corridors (polyline)

Synthetic linear infrastructure used only to demonstrate the workflow.

| Field | Type | Required | Domain / example |
|---|---|---:|---|
| corridor_id | Text (20) | Yes | COR-001 |
| corridor_name | Text (80) | Yes | Demonstration Corridor A |
| asset_type | Text (30) | Yes | Distribution / Transmission / Other |
| priority | Short integer | Yes | 1 / 2 / 3 |
| active | Short integer | Yes | 1 = Yes, 0 = No |
| data_origin | Text (20) | Yes | Synthetic |
| notes | Text (255) | No | Free text |

## 2. Inspection Zones (polygon)

Work areas used for assignment and progress reporting.

| Field | Type | Required | Domain / example |
|---|---|---:|---|
| zone_id | Text (20) | Yes | ZONE-001 |
| zone_name | Text (80) | Yes | Northwest Demo Zone |
| corridor_id | Text (20) | Yes | COR-001 |
| assigned_to | Text (80) | No | Demo Inspector |
| target_date | Date | No | Date only |
| zone_status | Text (20) | Yes | Not Started / In Progress / Complete |
| data_origin | Text (20) | Yes | Synthetic |

## 3. Vegetation Observations (point)

Operational inspection layer. Enable attachments for demonstration photos.

| Field | Type | Required | Domain / example |
|---|---|---:|---|
| observation_id | Text (30) | Yes | OBS-0001 |
| corridor_id | Text (20) | Yes | COR-001 |
| zone_id | Text (20) | Yes | ZONE-001 |
| source_tree_id | Text (50) | No | Calgary Open Data `wam_id` (unique in downloaded sample) |
| vegetation_type | Text (30) | Yes | Tree / Shrub / Other |
| proximity_class | Text (20) | Yes | Near / Moderate / Clear |
| risk_level | Text (10) | Yes | Low / Medium / High |
| workflow_status | Text (20) | Yes | New / Inspected / Action Needed / Closed |
| observed_date | Date | Yes | Inspection date |
| inspector_name | Text (80) | Yes | Portfolio test user |
| recommended_action | Text (30) | No | Monitor / Review / Trim / Remove / None |
| qc_status | Text (20) | Yes | Pending / Passed / Rework |
| qc_notes | Text (500) | No | Reviewer comments |
| data_origin | Text (20) | Yes | Open Data / Synthetic / Field Test |

## Form behaviour

- Default `workflow_status` to `New` and `qc_status` to `Pending`.
- Require risk level, vegetation type, observation date, and location.
- Show `recommended_action` when risk is Medium or High.
- Show `qc_notes` when QC status is Rework.
- Keep source IDs visible to analysts but hide nonessential technical fields from the public popup.

## Sharing model

- Source hosted feature layers: private or organization-only; editing enabled only where required.
- Internal web map: organization-only.
- Public hosted view: read-only, limited fields, no unnecessary personal names.
- Dashboard and Experience Builder: public only after dependency and anonymous-access tests pass.

