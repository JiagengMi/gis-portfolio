# Retrospective

The early inspection concept evolved into a focused 3D screening demonstration. Field collection, QC forms, and dashboards were deferred rather than presented as finished.

1. **Visual solidity is not geometric closure.** Extrusions looked complete but failed closure checks. Enclose Multipatch fixed closure but dropped attributes, requiring an explicit provenance join.
2. **Surface distance is not solid clearance.** A fully contained line had positive surface distance; Inside 3D supplied the missing relationship.
3. **Presentation and analysis elevations differ.** A common online display offset solved synthetic-ground/basemap mismatch without altering analytical Z.
4. **Upload is not cache readiness.** The missing-root-node message required checking cache status. Pro's unsupported elevation-setting error required removing cartographic offset for publishing.
5. **Stable IDs and checks prevent silent errors.** Endpoint candidate checks caught S-062 snapping problems. Tool relationship IDs refer to exact datasets; comparisons use veg_id.
6. **Precision is not accuracy.** Sampling refinement supports numerical stability, while all synthetic/geometry simplifications remain sources of model uncertainty.

Further work may cover tangencies and degeneracies, source geometry uncertainty, nearest-span ties, accessible symbology and mobile layouts, and real inspection workflows. Operational safety would require surveyed data, correct vertical references, and engineering conductor models.
