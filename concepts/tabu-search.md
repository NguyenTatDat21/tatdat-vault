---
title: >-
  Tabu Search
category: concepts
tags: [metaheuristics, local-search, operations-research]
relationships:
  - target: "[[concepts/variable-neighborhood-search]]"
    type: related_to
  - target: "[[concepts/large-neighborhood-search]]"
    type: related_to
  - target: "[[concepts/parallel-metaheuristics-cooperative-search]]"
    type: related_to
  - target: "[[references/gendreau2019-handbook-metaheuristics]]"
    type: derived_from
sources:
  - _papers/gendreau2019handbook/gendreau2019handbook-extracted.md
summary: >-
  Tabu Search is a memory-augmented local search method that allows non-improving moves while using tabu tenure and aspiration to escape local optima.
provenance:
  extracted: 0.78
  inferred: 0.19
  ambiguous: 0.03
base_confidence: 0.67
lifecycle: draft
lifecycle_changed: 2026-10-22
tier: core
created: 2026-10-22T08:35:02Z
updated: 2026-10-27T06:00:00Z
---

# Tabu Search

Tabu Search extends local search with adaptive memory. Instead of accepting only improving moves, it can accept non-improving moves while forbidding recently reversed decisions through tabu status.

## Key Ideas

- Define a neighborhood around the current solution and iterate by selecting the best admissible move.
- Keep short-term memory (tabu list/tenure) to avoid cycling.
- Use aspiration criteria to override tabu status when a move yields a globally best-so-far solution.
- Intensification and diversification are explicit control modes that change search behavior over time.
- Candidate-list strategies reduce per-iteration cost when full neighborhoods are too large.

For routing, the chapter uses CVRP as a concrete frame for describing feasible moves and memory design.

See also [[concepts/variable-neighborhood-search]], [[concepts/large-neighborhood-search]], [[references/gendreau2019-handbook-metaheuristics]], and [[references/montemanni2024-pdsvrp-collective-drones]].

## Open Questions

- How should tabu tenure scale with instance size in truck-drone variants where assignment and routing moves interact?
- Which aspiration rules are most stable when objective values are noisy or multi-criteria? ^[inferred]

## Sources

- [[_papers/gendreau2019handbook/gendreau2019handbook-extracted.md]]
