---
title: Set Orienteering Problem (SOP)
category: concepts
tags: [orienteering, combinatorial-optimization, routing, profits]
relationships:
  - target: "[[references/archetti2018-set-orienteering-problem]]"
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
  - _papers/lu2024effective/lu2024effective-extracted.md
summary: >-
  SOP maximizes cluster-level profit under route-duration limits, collecting each cluster reward when at least one member node is visited.
provenance:
  extracted: 0.88
  inferred: 0.10
  ambiguous: 0.02
base_confidence: 0.83
lifecycle: draft
lifecycle_changed: 2026-10-22
tier: supporting
created: 2026-10-22T11:22:57Z
updated: 2026-10-22T19:23:44Z
---

# Set Orienteering Problem (SOP)

The Set Orienteering Problem extends classic orienteering by grouping vertices into clusters and attaching profit to clusters rather than individual vertices.

## Key Ideas

- A route starts and ends at the depot.
- Travel time is bounded by a fixed budget `T_max`.
- A cluster contributes profit if at least one of its vertices is visited.
- The objective is to maximize total collected cluster profit within the time budget.
- SOP is NP-hard and quickly becomes intractable for exact methods on large instances.

## Formulation and Search Pattern

Archetti et al. anchor the canonical SOP formulation and pair it with a matheuristic (greedy randomized construction + tabu search + MIPMove) that scales well on large benchmark sets.

High-performing SOP methods often combine:
- population/diversification phases,
- memory-based local refinement (e.g., tabu),
- selective exact subproblem solves for intensification.

This mixed search stack appears to be more robust than single-mode local search in large instances. ^[inferred]

## Related

- [[references/archetti2018-set-orienteering-problem]]
- [[references/lu2024-hybrid-evolutionary-algorithm-sop]]
- [[concepts/tabu-search]]
- [[concepts/hyper-heuristics]]
- [[concepts/large-neighborhood-search]]

## Open Questions

- How sensitive are SOP heuristic gains to cluster structure quality versus route geometry?
- Which hybridization strategy transfers best from SOP to selective GTSP-like variants? ^[inferred]

## Sources

- [[_papers/archetti2018set/archetti2018set-extracted.md]]
- [[_papers/archetti2018set/archetti2018set.md]]
- [[_papers/lu2024effective/lu2024effective-extracted.md]]
