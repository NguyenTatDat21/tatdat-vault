---
title: Four-stage Guillotine-cut Bounded Knapsack
category: concepts
tags: [cutting-and-packing, dynamic-programming, hypergraph, integer-programming]
relationships:
  - target: "[[references/clautiaux2018-hypergraph-guillotine-knapsack]]"
    type: derived_from
  - target: "[[concepts/branch-and-price-column-generation]]"
    type: related_to
  - target: "[[references/barnhart1998-branch-and-price-column-generation]]"
    type: related_to
  - target: "[[concepts/plate-cut-position-guillotine-mip]]"
    type: related_to
  - target: "[[references/furini2016-two-dimensional-guillotine-cutting-ip]]"
    type: related_to
sources:
  - _papers/clautiaux2018combining/clautiaux2018combining-extracted.md
  - _papers/clautiaux2018combining/clautiaux2018combining.md
  - _papers/furini2016modeling/furini2016modeling-extracted.md
  - _papers/furini2016modeling/furini2016modeling.md
summary: >-
  Exact 2D cutting/packing concept where bounded item production and four-stage
  guillotine cuts are solved via DP-derived hypergraph flow with strong pruning.
provenance:
  extracted: 0.86
  inferred: 0.12
  ambiguous: 0.02
base_confidence: 0.77
lifecycle: draft
lifecycle_changed: 2026-10-22
tier: core
created: 2026-10-22T23:45:17Z
updated: 2026-10-27T06:00:00Z
---

# Four-stage Guillotine-cut Bounded Knapsack

This concept models 2D cutting where each cut must be guillotine-compatible and item demand is bounded.

## Core Structure

- **State:** plate dimensions + stage index (+ production counters in bounded variants).
- **Transition:** stage-compatible guillotine cuts or waste decisions.
- **Objective:** maximize packed-item profit under demand caps.
- **Representation:** DP states/transitions can be mapped to a directed acyclic hypergraph and solved as max-cost flow with side constraints.

## Why It Matters

- It turns a combinatorially large cutting-pattern space into a structured optimization pipeline.
- Hypergraph preprocessing + reduced-cost filtering can make exact solving practical on larger industrial instances.
- It illustrates a reusable pattern: derive exact recursion, convert to flow-like master model, then prune aggressively. ^[inferred]
- The same problem space admits a **plate-and-cut-position** MIP (one variable per plate, orientation, and cut position) that covers all feasible guillotine cuts; restricted positions (cuts at item sizes) suffice when a plate fits at most five items — see [[concepts/plate-cut-position-guillotine-mip]]. ^[inferred]

## Related

- [[references/clautiaux2018-hypergraph-guillotine-knapsack]]
- [[concepts/branch-and-price-column-generation]]
- [[references/barnhart1998-branch-and-price-column-generation]]
- [[concepts/plate-cut-position-guillotine-mip]]
- [[references/furini2016-two-dimensional-guillotine-cutting-ip]]

## Open Questions

- How much of the filtering/pruning machinery transfers to non-guillotine or irregular-shape packing variants?
- Which decomposition gives the best practical balance between bound quality and model size in modern solvers? ^[inferred]

## Sources

- [[_papers/clautiaux2018combining/clautiaux2018combining-extracted.md]]
- [[_papers/clautiaux2018combining/clautiaux2018combining.md]]
- [[_papers/furini2016modeling/furini2016modeling-extracted.md]]
- [[_papers/furini2016modeling/images/page_3_image_5.jpg]]
