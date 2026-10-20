# Script archive

These files curate the algorithms used interactively in the project session. They were reorganized for documentation; **these exact archived files have not been run against the project GDB**. Syntax and pure-Python helper checks at closeout do not establish an end-to-end ArcPy rerun.

Use the licensed ArcGIS Pro Python environment. Scripts take explicit local paths; no credentials, account names, automatic publishing, or machine-specific paths are embedded. Run only on deliberately prepared local analysis copies. The working `arcgis/` directory is not versioned or backed up by this repository.

## Conductors

```text
python generate_conductors.py --gdb PATH_TO_WORKING_GDB --output conductors_rerun --step 0.25
```

Requires `poles` and `spans` as documented in [data-model.md](../data-model.md). All endpoint candidates within 0.1 m are checked. Output must not exist. The script generates the simplified parabola, includes t=0.5, and checks written endpoints/midpoints. It does not create or randomize source dimensions.

## Final clearance fields

First prepare a new canopy analysis copy and run the tools through Pro:

1. Near 3D: canopy copy → conductor features, no search radius, Location/Delta enabled.
2. Inside 3D: conductor targets → same canopy copy as containers, complex output enabled.

Then:

```text
python finalize_clearance.py --canopies PATH_TO_ANALYSIS_COPY --conductors PATH_TO_CONDUCTORS --relations PATH_TO_INSIDE_TABLE
```

This writes final fields and risk_class to the analysis copy, preserving raw Near fields. It **refuses to overwrite existing final fields**. Existing released results already have these fields: do not point a rerun at them. Relationship IDs must refer to the exact input datasets used in the two tools; copying/rebuilding features afterward may invalidate IDs without an obvious error.

Internal-related spans are all zero-clearance ties. The representative is the first sorted span ID, not a unique physical nearest span. Full internal span IDs are also retained. This archive does not implement exhaustive separated-span tie enumeration or measurement uncertainty.

## Manual stages

Run `python check_repository.py` for syntax, pure-Python classification/correction cases, summary totals, and local Markdown links. This does not run ArcPy or query live services.

Footprint creation, extrusion, enclosure/attribute recovery, known-cube validation, Near/Inside tool execution, sampling comparison, and Online publication are described in [the workflow](../implementation-plan.md). An early unexecuted all-in-one scene builder was removed at closeout because it did not represent the actual completed workflow. There is no claimed one-command project reconstruction.
