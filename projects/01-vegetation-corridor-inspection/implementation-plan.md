# Two-week implementation plan

The schedule is task-based rather than calendar-bound. Stop after each checkpoint and save a local backup.

## Week 1 — MVP

### Day 1: Scope and workspace

- Confirm the project statement and portfolio disclosure.
- Create an ArcGIS Pro project and file geodatabase.
- Create folders for source data, processed data, exports, screenshots, and documentation.
- Record the ArcGIS Online username/organization used for publishing, but never store credentials.

Checkpoint: empty ArcGIS Pro project and documented folder structure.

### Day 2: Acquire and inspect open data

- Download a manageable subset of Calgary Public Trees.
- Record source URL, access date, licence, attribution, spatial reference, and relevant fields.
- Inspect geometry, null values, duplicates, and identifier stability.
- Select a small study area; do not publish the entire city inventory unless justified.

Checkpoint: source data register and a clean study-area tree layer.

### Day 3: Create synthetic operational data

- Draw two or three demonstration corridors in the study area.
- Buffer or otherwise delineate a small inspection area.
- Create inspection zones.
- Select or copy a subset of nearby trees into the observation workflow.
- Populate `data_origin` so open and synthetic records cannot be confused.

Checkpoint: corridors, zones, and observations are visually coherent and explicitly labelled.

### Day 4: Build and validate the geodatabase

- Create fields, aliases, coded-value domains, and defaults.
- Enable attachments on the observation layer.
- Check coordinate system, geometry, required identifiers, and domain compliance.
- Create a simple data-quality checklist and record the results.

Checkpoint: publishable geodatabase with no duplicate project IDs or invalid geometry.

### Day 5: Publish the source layers

- Publish corridors, zones, and observations as hosted feature layers.
- Complete item title, summary, description, tags, attribution, and limitations.
- Test query and editing behaviour in Map Viewer.
- Export a local backup after the first successful publish.

Checkpoint: hosted source layers work in ArcGIS Online.

### Day 6: Configure the internal web map

- Apply clear, colour-blind-conscious symbology.
- Configure scale visibility, labels, field aliases, and popups.
- Configure the observation form with required fields and conditional visibility.
- Test at least five valid records and three invalid or incomplete cases.

Checkpoint: the form supports a complete inspection record and catches intended errors.

### Day 7: Mobile workflow

- Open the map in Field Maps or connect a Survey123 form.
- Test creating a point, editing a status, and adding an attachment.
- If safe and convenient, collect two or three clearly labelled field-test records; otherwise use synthetic test points.
- Document what worked and what required adjustment.

Checkpoint: one end-to-end record appears correctly in the hosted layer.

## Week 2 — Public product and interview pack

### Day 8: QC workflow

- Configure QC status, reviewer notes, and rework behaviour.
- Create filters for Pending, Passed, and Rework.
- Test the transition from New to Inspected to Closed.

### Day 9: Safe public view

- Create a read-only hosted feature layer view.
- Remove or hide unnecessary personal and editing fields.
- Disable editing and verify public users cannot change records.
- Create a separate public web map from the view.

### Day 10: Dashboard

- Add indicators for total observations, high risk, pending QC, and closed records.
- Add category charts for risk and workflow status.
- Add selectors for zone, status, and risk.
- Verify that filters update both map and indicators.

### Day 11: Experience Builder

- Build Overview, Interactive Map, Dashboard, Workflow, Data & Limitations, and About sections.
- Add the portfolio disclosure and data attribution prominently.
- Design desktop and mobile layouts.

### Day 12: Functional and access testing

- Test every public URL in an incognito window.
- Check all layer dependencies and sharing levels.
- Test forms, popups, filters, mobile layout, and read-only restrictions.
- Record results in a test table rather than claiming unmeasured performance.

### Day 13: Interview pack

- Create a one-page case study.
- Create a simple system architecture graphic.
- Record a two-minute walkthrough.
- Write a postmortem covering trade-offs, limitations, and next improvements.

### Day 14: Release

- Save local exports and screenshots.
- Publish the case study and demo link.
- Verify attribution and links one final time.
- Only now draft factual CV bullets based on the completed implementation and measured test results.

