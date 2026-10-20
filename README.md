# GIS Portfolio — Jora Mi

Independent geospatial projects using public or synthetic data. No employer or client data is included.

## Featured project: 3D Vegetation Clearance Screening

**[Launch the application](https://experience.arcgis.com/experience/af7532559e924046aec35b94c8e090f1/)** · **[Web Scene](https://ucalgary.maps.arcgis.com/home/webscene/viewer.html?webscene=ec1b41378db342698ce06f8b229e1836)** · **[Case study](projects/01-vegetation-corridor-inspection/)**

A Calgary-based simulation with **241 closed canopy volumes** and **73 conductor spans**. ArcPy conductor modeling, Near 3D surface distances, and Inside 3D containment detection support illustrative screening classes, presented in ArcGIS Online and Experience Builder.

| Class | Clearance rule | Canopies |
|---|---|---:|
| High | <2 m | 67 |
| Medium | ≥2 and <4 m | 62 |
| Low | ≥4 m | 112 |

**52 zero-clearance canopies are included in High.** Refining sampling from 0.5 m to 0.25 m changed clearance by at most **0.000134 m**, with no class changes. This measures numerical sensitivity, not real-world accuracy.

**Stack:** ArcGIS Pro 3.3, ArcPy/Python, file geodatabases, ArcGIS Online, Experience Builder.

## Projects

| # | Project | Status |
|---|---|---|
| 01 | [3D Vegetation Clearance Screening](projects/01-vegetation-corridor-inspection/) | Core analysis and public Web MVP completed |
| 02 | [Wildfire Smoke & PM2.5 Monitoring](projects/02-wildfire-pm25-dashboard/) | Planned |
| 03 | [Stormwater Asset & Flood-Risk Inspection](projects/03-stormwater-inspection/) | Planned |
| 04 | [Urban Planning Site Selection](projects/04-planning-site-selection/) | Planned |

The simulation is not an operational utility system or electrical compliance assessment. Heights, ground reference, infrastructure, and thresholds are synthetic. Mobile inspection, QC workflows, and dashboards remain future extensions.

Local ArcGIS projects, GDBs, caches, and credentials are excluded from Git. Cloning this repository does not recreate the working geodatabase. The `docs/` website remains a future extension; the live ArcGIS application is the current demonstration entry.
