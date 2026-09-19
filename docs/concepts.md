                       CALL OF DUTY
                            │
                  ┌─────────┴─────────┐
                  ▼                   ▼
             BLACK OPS 6           WARZONE
                  │                   │
              Season 03          EXPERIENCE
                  │                   │
                  └──────┬────────────┘
                         ▼
                    APRIL 8 UPDATE
                         │
                      CONTAINS
                         ▼
                       CHANGE
                      /      \
                 AFFECTS    OCCURS_IN
                    ↓           ↓
                   XM4      Multiplayer
                    │
                  TYPE
                    ↓
                  Weapon

                       CHANGE
                         │
                    SUPPORTED_BY
                         ↓
                      EVIDENCE

Later:

PLAYER
   │
PLAYED
   ↓
MATCH
   │
USED
   ↓
XM4

Now the two worlds connect.

And suddenly we can ask:

Players whose first COD experience occurred after the XM4 changes behaved differently. What changed?

Or:

Which content changes preceded changes in new-player retention?

Or:

Which systems are most frequently changed before measurable shifts in player behavior?

Or eventually:

Trace this player outcome backward through the content they experienced, the changes affecting that content, the release containing those changes, and the evidence describing why the change was made.

That's the graph we're actually trying to build.

from the guides

            564 RAW COD GUIDES
                    │
                    ▼
        DETERMINISTIC PREPROCESSOR
                 Python
                    │
                    ▼
        ┌────────────────────────┐
        │ Guide                  │
        │ Title: Nuketown        │
        │ Experience: Multiplayer│
        │                        │
        │ Section: Domination    │
        │ Paragraph: ...         │
        │ Bullets: ...           │
        └────────────────────────┘
                    │
                    ▼
             SEMANTIC LAYER
                  LLM
                    │
                    ▼
        STRUCTURED ASSERTIONS
          /       |        \
         /        |         \
    Concept    Instance   Relationship
                             │
                             ▼
                          Evidence
                    │
                    ▼
          DETERMINISTIC AGGREGATOR
                    │
             deduplicate
             normalize
             count evidence
             identify conflicts
                    │
                    ▼
            ONTOLOGY CANDIDATES
                    │
                    ▼
               Ashish + me
                    │
                    ▼
              ONTOLOGY v0.1