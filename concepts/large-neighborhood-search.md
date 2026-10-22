---
title: >-
  Large Neighborhood Search (LNS)
category: concepts
tags: [metaheuristics, lns, alns, routing]
relationships:
  - target: "[[concepts/variable-neighborhood-search]]"
    type: related_to
  - target: "[[concepts/hyper-heuristics]]"
    type: related_to
  - target: "[[concepts/tabu-search]]"
    type: related_to
  - target: "[[references/gendreau2019-handbook-metaheuristics]]"
    type: derived_from
sources:
  - _papers/gendreau2019handbook/gendreau2019handbook-extracted.md
summary: >-
  LNS improves solutions by repeatedly destroying and repairing large parts of a solution; ALNS adapts operator choice based on observed performance.
provenance:
  extracted: 0.79
  inferred: 0.18
  ambiguous: 0.03
base_confidence: 0.57
lifecycle: draft
lifecycle_changed: 2026-10-22
tier: supporting
created: 2026-10-22T08:35:02Z
updated: 2026-10-22T08:35:02Z
---

# Large Neighborhood Search (LNS)

LNS is a destroy-and-repair metaheuristic: remove a substantial part of a current solution, then rebuild it with a repair heuristic and keep improvements under an acceptance policy.

## Key Ideas

- Large neighborhoods can offer better-quality moves per iteration than small local neighborhoods.
- Explicit neighborhood enumeration is often intractable, so LNS explores neighborhoods implicitly via destroy/repair operators.
- **ALNS** (Adaptive LNS) learns operator usefulness and shifts selection probabilities over time.
- LNS sits within the broader very-large-scale neighborhood (VLSN) family.
- In routing, LNS-style methods are attractive when exact neighborhood scans are too expensive.

LNS and ALNS can also be viewed as low-level heuristic families that a higher-level hyper-heuristic can orchestrate. ^[inferred]

Related pages: [[concepts/variable-neighborhood-search]], [[concepts/hyper-heuristics]], [[concepts/tabu-search]], [[references/gendreau2019-handbook-metaheuristics]], and [[references/montemanni2024-pdsvrp-collective-drones]].

## Open Questions

- Which destroy/repair operator portfolios transfer cleanly from CVRP to collaborative truck-drone variants?
- How aggressively should ALNS adaptation respond to short-term operator performance volatility? ^[inferred]

## Sources

- [[_papers/gendreau2019handbook/gendreau2019handbook-extracted.md]]
