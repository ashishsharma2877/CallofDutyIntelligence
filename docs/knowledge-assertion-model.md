# Knowledge Assertion Model v0.1

## Purpose

This document defines the first machine-readable contract for candidate knowledge assertions in CallofDutyIntelligence.

An assertion is the fundamental unit of candidate knowledge:

```text
subject -> predicate -> object
```

Assertions exist independently from any production graph. This contract does not create an ontology, assign final truth, or materialize graph data.

The JSON Schema is implemented at `schemas/knowledge_assertion.schema.json`.

## Source Basis

The examples use the existing Departures guide as their conceptual basis:

- Guide ID: `6afc9b83bbcfa740`
- Source file: `call-of-duty-guides-modern-warfare-iii-multiplayer-map-guide-departures-6afc9b83bb.html`
- Title family: `Modern Warfare III`
- Experience: `Multiplayer`
- Category: `Map`

No additional guides were processed for this contract.

## Assertion Structure

Each assertion contains:

- `assertion_id`: stable identifier for the assertion record.
- `subject`: entity or literal reference with canonical and raw representation where available.
- `predicate`: raw source relationship and proposed canonical predicate.
- `object`: entity or literal reference with canonical and raw representation where available.
- `provenance`: one or more source evidence records.
- `proposal`: proposer, optional AI model information, and extraction timestamp.
- `confidence`: `HIGH`, `MEDIUM`, or `LOW`; confidence is not truth.
- `review_status`: `PENDING`, `APPROVED`, `REJECTED`, or `UNRESOLVED`.
- `related_assertions`: links to other assertions by relation.
- `original_proposal`: preserved initial proposal.
- `review_history`: append-only human review events.
- `explanation`: support for later audit and AI explanation.

## Independent Typing

Subject and object terms intentionally do not contain a `proposed_types` field.

Entity typing is represented through separate assertions using the `IS_A` predicate. Multiple types are therefore allowed naturally:

```text
Departures -> IS_A -> Map
Departures -> IS_A -> Location
```

These assertions are independent and must not be collapsed into one mutually exclusive type.

## Provenance Basis

Each provenance record may use one or more of these basis values:

- `EXPLICIT_SOURCE`: directly stated or explicitly represented by the source.
- `STRUCTURAL_METADATA`: supported by document or DOM structure.
- `AI_INFERENCE`: proposed through AI interpretation.
- `HUMAN_DOMAIN_DECISION`: supplied or decided by a human domain reviewer.

Exact evidence text and source block references should be retained whenever available.

## Proposal and Confidence

`proposal.proposed_by` is one of `AI`, `HUMAN`, or `SYSTEM`. AI proposals may include `model` and `model_version`.

Confidence is a proposal attribute, not a truth label. A high-confidence candidate can still be rejected, and a low-confidence candidate can be approved after review.

## Review Lifecycle

The current assertion status is one of:

- `PENDING`: awaiting review.
- `APPROVED`: eligible for eventual graph materialization.
- `REJECTED`: retained for audit but not graph materialization.
- `UNRESOLVED`: retained because available evidence is insufficient or ambiguous.

`EDITED` is deliberately not a status. Editing is recorded as an `EDITED` action in `review_history`, while the current assertion remains `PENDING`, `APPROVED`, `REJECTED`, or `UNRESOLVED`.

Every review event retains:

- reviewer
- timestamp
- action
- previous value when applicable
- new value when applicable
- optional reviewer comment

The original proposal is never overwritten.

## Related Assertions

`related_assertions` links one assertion to another without merging their identities. Supported relation values are:

- `SUPERSEDE`
- `CONTRADICT`
- `REFINE`
- `ALTERNATIVE_TO`
- `DERIVED_FROM`

These links allow competing, revised, refined, alternative, and derived assertions to remain auditable.

## Graph Eligibility

Only current assertions with `review_status: APPROVED` should eventually be eligible for production graph materialization. Rejected and unresolved assertions remain available for provenance, audit, and explanation. Pending assertions remain candidates awaiting review.

## Example Assertions

The following examples are conceptual contract examples. They use the Departures guide metadata but do not perform new semantic extraction. Exact source block references and evidence text are intentionally left for a later extraction task.

### A. Departures -> IS_A -> Map

Explicitly supported by the guide context.

```json
{
  "assertion_id": "assertion_departures_is_a_map",
  "subject": {"entity_id": "entity_departures", "canonical_name": "Departures", "raw_name": "Departures", "value_type": "entity"},
  "predicate": {"raw": "is a", "canonical": "IS_A"},
  "object": {"entity_id": "entity_map", "canonical_name": "Map", "raw_value": "Map", "value_type": "entity"},
  "provenance": [{"source_document": "data/clean/guides/6afc9b83bbcfa740.json", "guide_id": "6afc9b83bbcfa740", "source_url": "https://callofduty.com/guides/multiplayer-maps/call-of-duty-guides-modern-warfare-iii-multiplayer-map-guide-departures", "source_blocks": [], "evidence_text": null, "basis": ["EXPLICIT_SOURCE"]}],
  "proposal": {"proposed_by": "SYSTEM", "model": null, "model_version": null, "extracted_at": "2026-09-18T00:00:00Z"},
  "confidence": "HIGH",
  "review_status": "PENDING",
  "related_assertions": [],
  "original_proposal": {"subject": "Departures", "predicate": "IS_A", "object": "Map"},
  "review_history": [],
  "explanation": {"why_proposed": "The existing guide metadata identifies Departures as a Multiplayer Map guide.", "why_in_graph": null, "approval_basis": null, "rejection_reason": null}
}
```

### B. Departures -> IS_A -> Location

A human domain-modeling decision. It remains independently valid alongside the Map assertion.

```json
{
  "assertion_id": "assertion_departures_is_a_location",
  "subject": {"entity_id": "entity_departures", "canonical_name": "Departures", "raw_name": "Departures", "value_type": "entity"},
  "predicate": {"raw": "is a", "canonical": "IS_A"},
  "object": {"entity_id": "entity_location", "canonical_name": "Location", "raw_value": "Location", "value_type": "entity"},
  "provenance": [{"source_document": "data/clean/guides/6afc9b83bbcfa740.json", "guide_id": "6afc9b83bbcfa740", "source_url": "https://callofduty.com/guides/multiplayer-maps/call-of-duty-guides-modern-warfare-iii-multiplayer-map-guide-departures", "source_blocks": [], "evidence_text": null, "basis": ["HUMAN_DOMAIN_DECISION"]}],
  "proposal": {"proposed_by": "HUMAN", "model": null, "model_version": null, "extracted_at": "2026-09-18T00:00:00Z"},
  "confidence": "MEDIUM",
  "review_status": "APPROVED",
  "related_assertions": [],
  "original_proposal": null,
  "review_history": [{"reviewer": "domain-reviewer", "timestamp": "2026-09-18T00:00:00Z", "action": "APPROVED", "previous_value": null, "new_value": "Departures IS_A Location", "comment": "Human modeling decision; does not invalidate other types."}],
  "explanation": {"why_proposed": "A human domain modeler proposed Location as an additional type.", "why_in_graph": "Approved by human domain review.", "approval_basis": "HUMAN_DOMAIN_DECISION", "rejection_reason": null}
}
```

### C. Check-In -> IS_A -> Spawn Area

An AI proposal awaiting review because the source is ambiguous about whether Check-In itself is a spawn area or a location associated with a spawn.

```json
{
  "assertion_id": "assertion_check_in_is_a_spawn_area",
  "subject": {"entity_id": "entity_check_in", "canonical_name": "Check-In", "raw_name": "Check-In", "value_type": "entity"},
  "predicate": {"raw": "is a", "canonical": "IS_A"},
  "object": {"entity_id": "entity_spawn_area", "canonical_name": "Spawn Area", "raw_value": "Spawn Area", "value_type": "entity"},
  "provenance": [{"source_document": "data/clean/guides/6afc9b83bbcfa740.json", "guide_id": "6afc9b83bbcfa740", "source_url": "https://callofduty.com/guides/multiplayer-maps/call-of-duty-guides-modern-warfare-iii-multiplayer-map-guide-departures", "source_blocks": [], "evidence_text": null, "basis": ["EXPLICIT_SOURCE", "AI_INFERENCE"]}],
  "proposal": {"proposed_by": "AI", "model": "local-prototype", "model_version": "unspecified", "extracted_at": "2026-09-18T00:00:00Z"},
  "confidence": "LOW",
  "review_status": "PENDING",
  "related_assertions": [],
  "original_proposal": {"subject": "Check-In", "predicate": "IS_A", "object": "Spawn Area"},
  "review_history": [],
  "explanation": {"why_proposed": "The source may associate Check-In with spawning, but does not clearly establish whether Check-In itself is a Spawn Area or a location associated with one.", "why_in_graph": null, "approval_basis": null, "rejection_reason": null}
}
```

### D. Zakhaev International Airport -> IS_A -> Map

Unresolved because the current source does not establish this assertion.

```json
{
  "assertion_id": "assertion_zakhaev_international_airport_is_a_map",
  "subject": {"entity_id": "entity_zakhaev_international_airport", "canonical_name": "Zakhaev International Airport", "raw_name": "Zakhaev International Airport", "value_type": "entity"},
  "predicate": {"raw": "is a", "canonical": "IS_A"},
  "object": {"entity_id": "entity_map", "canonical_name": "Map", "raw_value": "Map", "value_type": "entity"},
  "provenance": [{"source_document": "data/clean/guides/6afc9b83bbcfa740.json", "guide_id": "6afc9b83bbcfa740", "source_url": "https://callofduty.com/guides/multiplayer-maps/call-of-duty-guides-modern-warfare-iii-multiplayer-map-guide-departures", "source_blocks": [], "evidence_text": null, "basis": ["HUMAN_DOMAIN_DECISION"]}],
  "proposal": {"proposed_by": "HUMAN", "model": null, "model_version": null, "extracted_at": "2026-09-18T00:00:00Z"},
  "confidence": "LOW",
  "review_status": "UNRESOLVED",
  "related_assertions": [],
  "original_proposal": null,
  "review_history": [],
  "explanation": {"why_proposed": "The assertion was supplied as a candidate requiring review.", "why_in_graph": null, "approval_basis": null, "rejection_reason": "The current Departures source does not establish this assertion."}
}
```

## Validation Status

The four examples above are intended to be validated against `schemas/knowledge_assertion.schema.json` before use. This document defines the v0.1 contract only; it does not perform extraction or graph materialization.
