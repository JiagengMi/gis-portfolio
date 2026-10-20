# Source register

| Source | Actual role | Notes |
|---|---|---|
| [City of Calgary Public Trees](https://data.calgary.ca/Environment/Public-Trees/tfs4-3wwa) | Acquired/profiled public point inventory and study-area context | 618-record sample downloaded 2026-09-28; Socrata ID tfs4-3wwa; original XY WGS84; wam_id was unique in the sample |
| Imagery used in ArcGIS Pro | Manual tracing of 241 canopy footprints | Footprints are imagery-digitized, not City inventory polygons or LiDAR reconstruction. Per-canopy source-tree IDs were not populated. Do not claim a one-to-one inventory linkage. Record the imagery provider/vintage from item attribution before redistributing source imagery; no exact vintage is asserted here. |
| Manually digitized corridors, poles, spans | Simulation infrastructure | 75 pole locations, 73 final spans; not verified real utility assets |
| Synthetic heights and parameters | Model dimensions | Ground=1000 m; tree heights 6/9/12/15; crown bases 2/3/4; attachments=12; sag=1; final sampling=0.25 m |
| Esri Light Gray Canvas | Current web presentation basemap | Subject to service/provider attribution and terms; no basemap tiles are redistributed here |
| World Imagery | Earlier/contextual presentation | Third-party attribution belongs to the respective providers; not the source of measured ground elevation |
| Calgary Tree Canopy 2022 | Early candidate only | Not claimed as used in the final geometry workflow |

## Existing curated source files

- `data/source/calgary-public-trees-study-area.geojson`
- `data/source/calgary-public-trees-study-area.csv`

Original sample query:

```text
within_box(point,51.080,-114.140,51.070,-114.125)
```

See [data-profile.md](data-profile.md) for the downloaded inventory profile. Inventory licence/redistribution requirements and imagery terms must be checked at their source before additional redistribution. No employer or client data is used; working GDBs, imagery caches, and ArcGIS project files are excluded from Git.
