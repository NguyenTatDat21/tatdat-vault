---title: >-
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
  - target: "[[concepts/large-neighborhood-ship-pair-destroy-repair]]"
    type: related_to
  - target: "[[references/goel2012-large-neighborhood-search-lng-inventory-routing]]"
    type: related_to
  - target: "[[references/gendreau2019-handbook-metaheuristics]]"
    type: derived_from

  - target: "[[concepts/decision-diagrams-optimization]]"
    type: related_to
  - target: "[[concepts/encoding-preservation-under-composition-and-merging]]"
    type: related_to
  - target: "[[concepts/search-combinators-meta-search]]"
    type: related_to

sources:
  - _papers/gendreau2019handbook/gendreau2019handbook-extracted.md
  - _papers/gendreau2019handbook/gendreau2019handbook.md
  - _papers/goel2012large/goel2012large-extracted.md
  - _papers/goel2012large/goel2012large.md
summary: >-
  VNS systematically changes neighborhood structures during search; key variants include VND, RVNS, and BVNS with shake-and-descent cycles.
provenance:
  extracted: 0.82
  inferred: 0.15
  ambiguous: 0.03
base_confidence: 0.77
lifecycle: draft
lifecycle_changed: 2026-10-24
tier: core
created: 2026-10-22T08:35:02Z
updated: 2026-10-27T06:00:00Z
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

## Schemes, Extensions, and an Industrial Instance

- **GVNS** (generalized VNS) and **VNDS** (variable neighborhood decomposition search): VNDS is a two-level VNS based on a problem decomposition, solving a sequence of reduced problems generated from linear-programming relaxations with variables fixed by VNDS rules, producing sequences of upper and lower bounds.
- Neighborhood-change rule: if $f(x')<f(x)$, set $x\leftarrow x'$ and return $k$ to the initial neighborhood; otherwise move $k$ to the next neighborhood. Nested neighborhoods are induced by a metric or quasi-metric on the solution space.
- Extensions recorded in the handbook: **Formulation Space Search** / variable formulation search, where a neighborhood change is a change of formulation; VNS for automatic programming and AI; AutoGraphiX graph-theory discovery with more than 1500 conjectures, more than half proved automatically compared with about 400 by human efforts.
- Exact/hybrid uses: VNS for large-scale location by primal-dual methods, VNS combined with **local branching** for MILP solution generation, VNS decomposition plus exact solvers for very large MILP, VNS for continuous nonlinear programs, VNS for MINLP with branch-and-bound and local branching.
- Industrial instance: Goel et al. (2012) run a two-ship VNS neighborhood on a time-space MIP — fix all ships except a pair, re-solve for the pair, terminate after $C(|V|,2)$ non-improving iterations — with geometric-mean speed-up 13.60–15.72 over CPLEX's first feasible solution. See [[concepts/large-neighborhood-ship-pair-destroy-repair]].

Related pages: [[concepts/tabu-search]], [[concepts/large-neighborhood-search]], [[concepts/large-neighborhood-ship-pair-destroy-repair]], [[concepts/parallel-metaheuristics-cooperative-search]], [[references/gendreau2019-handbook-metaheuristics]], [[references/goel2012-large-neighborhood-search-lng-inventory-routing]], and [[concepts/pdsvrp-c]].

## Open Questions

- Which neighborhood ordering is most robust for mixed truck/drone routing objectives?
- Can adaptive neighborhood-change policies outperform fixed `k_max` strategies under strict time budgets? ^[inferred]

## Sources

- [[_papers/gendreau2019handbook/gendreau2019handbook-extracted.md]]
- [[_papers/gendreau2019handbook/gendreau2019handbook.md]]
- [[_papers/goel2012large/goel2012large-extracted.md]]
- [[_papers/goel2012large/goel2012large.md]]

## Related
- [[concepts/search-combinators-meta-search]] — shares search + metaheuristic tags with this page
- [[concepts/encoding-preservation-under-composition-and-merging]] — shares search + metaheuristic tags with this page

- [[concepts/decision-diagrams-optimization]] — shares search + metaheuristic tags with this page
