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
  - target: "[[concepts/iterated-local-search]]"
    type: related_to
    note: "Reciprocal - concepts/iterated-local-search references this page."
    confidence: 0.7
    basis: observed
    since: "2026-10-30T14:38:55Z"
  - target: "[[concepts/multi-objective-metaheuristic-tuning-validation]]"
    type: related_to
    note: "Reciprocal - concepts/multi-objective-metaheuristic-tuning-validation references this page."
    confidence: 0.7
    basis: observed
    since: "2026-10-30T14:38:55Z"
  - target: "[[concepts/set-orienteering-problem]]"
    type: related_to
    note: "Reciprocal - concepts/set-orienteering-problem references this page."
    confidence: 0.7
    basis: observed
    since: "2026-10-30T14:38:55Z"
  - target: "[[concepts/set-team-orienteering-problem-with-time-windows]]"
    type: related_to
    note: "Reciprocal - concepts/set-team-orienteering-problem-with-time-windows references this page."
    confidence: 0.7
    basis: observed
    since: "2026-10-30T14:38:55Z"
  - target: "[[references/archetti2018-set-orienteering-problem]]"
    type: related_to
    note: "Reciprocal - references/archetti2018-set-orienteering-problem references this page."
    confidence: 0.7
    basis: observed
    since: "2026-10-30T14:38:55Z"
  - target: "[[references/lourenco2019iterated]]"
    type: related_to
    note: "Reciprocal - references/lourenco2019iterated references this page."
    confidence: 0.7
    basis: observed
    since: "2026-10-30T14:38:55Z"
  - target: "[[references/lu2024-hybrid-evolutionary-algorithm-sop]]"
    type: related_to
    note: "Reciprocal - references/lu2024-hybrid-evolutionary-algorithm-sop references this page."
    confidence: 0.7
    basis: observed
    since: "2026-10-30T14:38:55Z"
  - target: "[[references/wang2019routing]]"
    type: related_to
    note: "Reciprocal - references/wang2019routing references this page."
    confidence: 0.7
    basis: observed
    since: "2026-10-30T14:38:55Z"
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
updated: 2026-10-30T14:38:55Z
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
