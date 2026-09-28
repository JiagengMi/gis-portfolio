# Vegetation Corridor Inspection System

Status: Planning

## Project statement

An independent ArcGIS Online portfolio project that demonstrates how a GIS analyst can publish, collect, review, and communicate vegetation observations near simulated linear infrastructure.

This is not an operational utility system. It uses City of Calgary open data and clearly labelled synthetic corridor, inspection, and risk data. It does not use employer, client, or confidential data.

## Business question

How can a small GIS team identify vegetation near a simulated corridor, collect standardized inspection observations, perform quality control, and provide a safe read-only operational overview?

## Intended users

- Field inspector: creates and updates observations, adds notes and photos.
- GIS analyst: validates geometry and attributes, completes QC, assigns follow-up status.
- Manager or portfolio viewer: explores a read-only map and dashboard.

## Planned ArcGIS architecture

```text
Calgary open tree data + synthetic corridor data
                    |
                 ArcGIS Pro
                    |
        Hosted feature layers (editable source)
                    |
       +------------+-------------+
       |                          |
Field Maps / Survey123      Hosted view (read-only)
       |                          |
Internal operations map     Dashboard + Experience Builder
```

## MVP deliverables

- Hosted feature layers for corridors, inspection zones, and vegetation observations.
- An internal editing web map with a controlled inspection form.
- A read-only hosted feature layer view for public presentation.
- A dashboard with risk, status, QC, and completion indicators.
- An Experience Builder application suitable for a two-minute demonstration.
- A one-page case study, test results, architecture diagram, and postmortem.

## Success criteria

- Anonymous users can open the public application without signing in.
- Public users cannot edit the source data.
- Required inspection fields cannot be omitted through the configured form.
- Risk, workflow status, and QC status use controlled values rather than unrestricted text.
- Dashboard filters update the map and indicators consistently.
- Every published item includes a description, data source, limitations, attribution, and update date.

## Portfolio disclosure

Suggested label for every public page:

> Independent portfolio project using City of Calgary open data and synthetic infrastructure/inspection records. Created to demonstrate ArcGIS Online workflow design; not affiliated with or used by a utility operator.

