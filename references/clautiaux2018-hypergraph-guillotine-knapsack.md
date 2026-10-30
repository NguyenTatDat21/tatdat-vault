---
title: >-
  Combining Dynamic Programming and Lagrangian Filtering for Four-stage 2D
  Guillotine Bounded Knapsack (Clautiaux et al., 2018)
category: references
tags: [paper, cutting-and-packing, dynamic-programming, integer-programming]
relationships:
  - target: "[[concepts/four-stage-guillotine-cut-bounded-knapsack]]"
    type: uses
  - target: "[[concepts/branch-and-price-column-generation]]"
    type: related_to
  - target: "[[references/barnhart1998-branch-and-price-column-generation]]"
    type: related_to
  - target: "[[concepts/bin-packing-based-cutting-stock-ilp]]"
    type: related_to
    note: "Reciprocal - concepts/bin-packing-based-cutting-stock-ilp references this page."
    confidence: 0.7
    basis: observed
    since: "2026-10-30T14:38:55Z"
  - target: "[[concepts/plate-cut-position-guillotine-mip]]"
    type: related_to
    note: "Reciprocal - concepts/plate-cut-position-guillotine-mip references this page."
    confidence: 0.7
    basis: observed
    since: "2026-10-30T14:38:55Z"
  - target: "[[references/furini2016-two-dimensional-guillotine-cutting-ip]]"
    type: related_to
    note: "Reciprocal - references/furini2016-two-dimensional-guillotine-cutting-ip references this page."
    confidence: 0.7
    basis: observed
    since: "2026-10-30T14:38:55Z"
  - target: "[[references/hadjsalem2023-2d-variable-sized-cutting-stock-textile]]"
    type: related_to
    note: "Reciprocal - references/hadjsalem2023-2d-variable-sized-cutting-stock-textile references this page."
    confidence: 0.7
    basis: observed
    since: "2026-10-30T14:38:55Z"
sources:
  - _papers/clautiaux2018combining/clautiaux2018combining-extracted.md
  - _papers/clautiaux2018combining/clautiaux2018combining.md
  - _papers/furini2016modeling/furini2016modeling-extracted.md
summary: >-
  Exact hypergraph-flow and dynamic-programming framework for four-stage
  guillotine bounded knapsack, accelerated by preprocessing and Lagrangian
  filtering.
provenance:
  extracted: 0.85
  inferred: 0.13
  ambiguous: 0.02
base_confidence: 0.77
lifecycle: draft
lifecycle_changed: 2026-10-22
tier: core
created: 2026-10-22T23:45:17Z
updated: 2026-10-30T14:38:55Z
---

# Combining Dynamic Programming and Lagrangian Filtering for Four-stage 2D Guillotine Bounded Knapsack (Clautiaux et al., 2018)

> [!tldr] The paper builds an exact four-stage guillotine-cut bounded-knapsack solver by combining a DP-derived hypergraph flow model, preprocessing reductions, and Lagrangian filtering to prune non-promising hyperarcs.

## Problem & Contribution

The work targets a bounded two-dimensional guillotine-cut knapsack setting where item demand is capped and cuts are restricted to a four-stage pattern.

Main contribution:
- represent feasible cutting patterns as flow in a directed acyclic hypergraph derived from DP recurrences,
- enforce bounded production with side constraints in an ILP flow model,
- accelerate exact solving with hypergraph preprocessing and reduced-cost filtering.

## Method / Architecture

The core objective remains profit maximization under cutting and demand feasibility:

$$
\max \sum_i p_i y_i
$$

with `y_i` induced by hypergraph flow and bounded by item-demand constraints.

Pipeline used in the paper:
1. DP recursion over stage-indexed plate states.
2. Hypergraph conversion of DP states and transitions.
3. Flow-based ILP with demand side constraints.
4. Preprocessing (symmetry reduction, plate-size reduction, state contraction).
5. Lagrangian filtering to remove hyperarcs that cannot appear in improving solutions.

## Results

- The paper reports substantial runtime gains from filtering and preprocessing versus direct MIP solving.
- Iterative labeling variants (with/without strong dominance) are competitive with or better than baseline MIP on larger bounded instances.
- Reported comparisons indicate the approach is competitive with then-best exact literature methods on several benchmark families.

## Limitations

- Gains depend strongly on bound quality and multiplier quality in Lagrangian filtering.
- Performance varies by instance family; some classes remain easier for alternative exact procedures. ^[ambiguous]
- The method is specialized to guillotine-cut structure and does not directly transfer to unrestricted 2D packing.
- The four-stage pattern is a modeling restriction; a plate-and-cut-position MIP over all feasible guillotine cuts covers strictly more patterns, at the cost of a pseudo-polynomial variable count — see [[references/furini2016-two-dimensional-guillotine-cutting-ip]]. ^[inferred]

## Related

- [[concepts/four-stage-guillotine-cut-bounded-knapsack]]
- [[concepts/branch-and-price-column-generation]]
- [[references/barnhart1998-branch-and-price-column-generation]]
- [[references/furini2016-two-dimensional-guillotine-cutting-ip]]
- [[concepts/plate-cut-position-guillotine-mip]]

## Bibliographic Record

- Citation key: `clautiaux2018combining`
- DOI: `10.1016/j.disopt.2018.02.003`
- Canonical URL: <https://doi.org/10.1016/j.disopt.2018.02.003>
- Publication: *Discrete Optimization* (2018)
- Authors: François Clautiaux; Ruslan Sadykov; François Vanderbeck; Quentin Viaud
- Companion metadata note: [[_papers/clautiaux2018combining/clautiaux2018combining.md]]

## Sources

- [[_papers/clautiaux2018combining/clautiaux2018combining-extracted.md]]
- [[_papers/clautiaux2018combining/clautiaux2018combining.md]]
- [[_papers/furini2016modeling/furini2016modeling-extracted.md]]
