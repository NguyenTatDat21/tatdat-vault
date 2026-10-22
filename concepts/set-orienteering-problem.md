---
title: Set Orienteering Problem (SOP)
category: concepts
tags: [orienteering, combinatorial-optimization, routing, profits]
relationships:
  - target: "[[references/lu2024-hybrid-evolutionary-algorithm-sop]]"
    type: derived_from
  - target: "[[concepts/tabu-search]]"
    type: related_to
  - target: "[[concepts/hyper-heuristics]]"
    type: related_to
sources:
  - _papers/lu2024effective/lu2024effective-extracted.md
summary: SOP selects a profit-maximizing tour over clustered customers under a travel-time budget, collecting cluster profit when at least one member is visited.
provenance:
  extracted: 0.86
  inferred: 0.12
  ambiguous: 0.02
base_confidence: 0.57
lifecycle: draft
lifecycle_changed: 2026-10-22
tier: supporting
created: 2026-10-22T11:22:57Z
updated: 2026-10-22T11:22:57Z
---

# Set Orienteering Problem (SOP)

The Set Orienteering Problem extends classic orienteering by grouping vertices into clusters and attaching profit to clusters rather than individual vertices.

## Key Ideas

- A route starts and ends at the depot.
- Travel time is bounded by a fixed budget `T_max`.
- A cluster contributes profit if at least one of its vertices is visited.
- The objective is to maximize total collected cluster profit within the time budget.
- SOP is NP-hard and quickly becomes intractable for exact methods on large instances.

## Algorithmic Patterns (from Lu et al.)

High-performing SOP heuristics can combine:

- population-based search (diversification),
- tabu-guided local refinement (intensification),
- occasional infeasible-space exploration before repair.

This combination is reported to improve robustness over single-mode local search in large benchmark sets. ^[inferred]

Related pages: [[references/lu2024-hybrid-evolutionary-algorithm-sop]], [[concepts/tabu-search]], [[concepts/hyper-heuristics]], [[concepts/large-neighborhood-search]].

## Open Questions

- How sensitive are SOP heuristic gains to cluster structure quality versus route geometry?
- Which hybridization strategy transfers best from SOP to selective GTSP-like variants? ^[inferred]

## Sources

- [[_papers/lu2024effective/lu2024effective-extracted.md]]
