---
title: Set Orienteering Problem (SOP)
category: concepts
tags: [orienteering, combinatorial-optimization, routing, profits]
relationships:
  - target: "[[references/archetti2018-set-orienteering-problem]]"
    type: derived_from
  - target: "[[references/archetti2023-branch-and-cut-sop]]"
    type: derived_from
  - target: "[[references/lu2024-hybrid-evolutionary-algorithm-sop]]"
    type: derived_from
  - target: "[[concepts/tabu-search]]"
    type: related_to
  - target: "[[concepts/hyper-heuristics]]"
    type: related_to
sources:
  - _papers/archetti2018set/archetti2018set-extracted.md
  - _papers/archetti2018set/archetti2018set.md
  - _papers/archetti2023new/archetti2023new-extracted.md
  - _papers/archetti2023new/archetti2023new.md
  - _papers/lu2024effective/lu2024effective-extracted.md
summary: >-
  SOP maximizes cluster-level profit under a route-duration budget, with both matheuristic and branch-and-cut exact strategies now defining the practical solution landscape.
provenance:
  extracted: 0.86
  inferred: 0.11
  ambiguous: 0.03
base_confidence: 0.92
lifecycle: draft
lifecycle_changed: 2026-10-22
tier: supporting
created: 2026-10-22T11:22:57Z
updated: 2026-10-22T19:33:55Z
---

# Set Orienteering Problem (SOP)

The Set Orienteering Problem extends classic orienteering by grouping vertices into clusters and attaching profit to clusters rather than individual vertices.

## Key Ideas

- A route starts and ends at the depot.
- Travel time is bounded by a fixed budget `T_max`.
- A cluster contributes profit if at least one of its vertices is visited.
- The objective is to maximize total collected cluster profit within the time budget.
- SOP remains NP-hard and needs hybrid exact/heuristic strategies as instances grow.

## Formulation and Solution Pattern

Recent SOP literature in this vault shows two complementary paths:

- **Matheuristic path (Archetti 2018, Lu 2024):** randomized construction + tabu/local search + exact neighborhood refinement.
- **Exact branch-and-cut path (Archetti 2023):** lower-variable formulation and dedicated valid-inequality separation for stronger exact solving.

Together these works suggest a practical stack: exact methods for medium-size/high-certainty solves, and hybrid metaheuristics for larger or tighter-time scenarios. ^[inferred]

## Related

- [[references/archetti2018-set-orienteering-problem]]
- [[references/archetti2023-branch-and-cut-sop]]
- [[references/lu2024-hybrid-evolutionary-algorithm-sop]]
- [[concepts/tabu-search]]
- [[concepts/hyper-heuristics]]
- [[concepts/large-neighborhood-search]]

## Open Questions

- How sensitive are exact-vs-heuristic breakpoints to route-budget tightness (`T_max`) and cluster geometry?
- Which cut families from exact SOP transfer best to multi-vehicle or stochastic SOP variants? ^[inferred]

## Sources

- [[_papers/archetti2018set/archetti2018set-extracted.md]]
- [[_papers/archetti2018set/archetti2018set.md]]
- [[_papers/archetti2023new/archetti2023new-extracted.md]]
- [[_papers/archetti2023new/archetti2023new.md]]
- [[_papers/lu2024effective/lu2024effective-extracted.md]]
