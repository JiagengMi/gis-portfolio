# Implemented workflow and release checklist

This replaces the early two-week mobile-inspection plan. The delivered scope is 3D simulation, clearance analysis, and public presentation.

1. Acquire and profile the Calgary public-tree sample; retain source files separately from digitized canopies.
2. Prepare projected canopy polygons, poles, corridors, and straight two-endpoint spans. Match span endpoints to unique poles within 0.1 m; report ambiguity/missing matches rather than picking a distant pole.
3. Populate synthetic heights once; derive base Z and crown depth. Configure Base Height extrusion, convert to multipatch, and test closure. Enclose outputs if needed; restore attributes with OID_ORIG and recalculate Z bounds.
4. Generate parabolic Z polylines, preserving endpoint/midpoint samples. Test one span before generating all 73.
5. Validate Near 3D and Inside 3D against a closed cube: side, above, diagonal, crossing, and fully contained lines.
6. Analyze a canopy copy. Near 3D uses canopy inputs and conductor near-features; Inside 3D uses conductors as targets and canopies as containers, with complex output enabled.
7. Preserve raw distances; write corrected solid clearances and related stable span IDs. Use exact input OBJECTIDs for relationships.
8. Regenerate conductors at 0.25 m; rerun both tools against equivalent canopy geometry. Compare by veg_id. Classify unrounded distances with the documented illustrative rules.
9. Publish result multipatches as a scene layer with associated feature layer; publish the fine conductors as a feature layer. In Pro 3.3 the operator used Map for the standalone line publishing path. Use span_id as display field and enable unique numeric layer IDs. Analyzer checks must pass.
10. Wait for scene-cache completion before adding hosted scene layers. Add results to the **existing** Web Scene, hide/remove obsolete layers from its presentation, set Light Gray Canvas and no real terrain, then apply −1000 m display offsets to both model layers in Scene Viewer.
11. Configure English names/pop-ups, initial viewpoint/slides, source/disclosure text, and public dependency sharing. Save the existing Web Scene rather than creating an unintended replacement item.
12. Update static Experience Builder statistics, status, method, and limitations; save and republish the existing app. Restore/update Web Scene metadata independently if necessary.

## After every release

- Open the existing application URL in an incognito window; no login should be required.
- Verify scene/feature dependencies, cache readiness, class colors, heights, both pop-ups, and Home/default view.
- Check static figures against the frequency table, including zero-clearance cases as a subset of High.
- Check both Web Scene and app metadata; ensure no stale “Not yet calculated” text remains.
- Verify public service permissions are query-only where intended. A pop-up field marked editable is not proof of service editing capability.
- Preserve the existing item IDs and public entry URL. New layer IDs may require reconfiguring app widgets if those widgets directly reference old layer sources.
- Do not overwrite analysis geometry to achieve presentation offsets.

No automatic publishing, geoprocessing rerun, or ArcGIS workspace backup is part of documentation closeout.
