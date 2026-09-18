# Content Calendar Data Model

This document describes the evolving data model for the Call of Duty
content calendar.

The model should be derived from the source data rather than forcing
Call of Duty's release history into a predetermined graph ontology.

## Initial Release Event

Potential fields:

- event_date
- title
- release_name
- release_type
- season
- content_type
- content_name
- change_type
- description
- source_url
- source_title
- retrieved_at

## Principles

### Preserve provenance

Every extracted fact should be traceable to its original source.

### Preserve raw data

Raw source data should remain separate from normalized data.

### Do not prematurely design the graph

The content calendar will inform which concepts should eventually become:

- entities
- relationships
- attributes
- events

### Separate facts from interpretation

Source facts should be preserved independently from classifications,
summaries, or conclusions generated later by AI.