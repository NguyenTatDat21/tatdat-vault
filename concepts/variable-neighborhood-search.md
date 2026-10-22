---
title: >-
  Variable Neighborhood Search (VNS)
category: concepts
tags: [metaheuristics, local-search, neighborhood-search]
relationships:
  - target: "[[concepts/tabu-search]]"
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
  VNS systematically changes neighborhood structures during search; key variants include VND, RVNS, and BVNS with shake-and-descent cycles.
provenance:
  extracted: 0.8
  inferred: 0.17
  ambiguous: 0.03
base_confidence: 0.57
lifecycle: draft
lifecycle_changed: 2026-10-22
tier: supporting
created: 2026-10-22T08:35:02Z
updated: 2026-10-22T08:35:02Z
---

# Variable Neighborhood Search (VNS)

VNS is built on a simple principle: improve robustness by not relying on a single neighborhood. The search intentionally changes neighborhoods over time, both during perturbation and local descent.

## Key Ideas

- A local optimum in one neighborhood may be improvable in another neighborhood.
- A global optimum is a local optimum under all neighborhoods.
- Many useful local minima are close, so controlled neighborhood changes can move search between them.
- **VND** applies deterministic neighborhood descent.
- **RVNS** applies random neighborhood exploration, often useful for very large instances.
- **BVNS** combines shaking plus local search and a neighborhood-change policy.

In practice, small `k_max` values (often 2 or 3) are frequently effective for BVNS in many problem families.

Related pages: [[concepts/tabu-search]], [[concepts/large-neighborhood-search]], [[concepts/parallel-metaheuristics-cooperative-search]], [[references/gendreau2019-handbook-metaheuristics]], and [[concepts/pdsvrp-c]].

## Open Questions

- Which neighborhood ordering is most robust for mixed truck/drone routing objectives?
- Can adaptive neighborhood-change policies outperform fixed `k_max` strategies under strict time budgets? ^[inferred]

## Sources

- [[_papers/gendreau2019handbook/gendreau2019handbook-extracted.md]]
