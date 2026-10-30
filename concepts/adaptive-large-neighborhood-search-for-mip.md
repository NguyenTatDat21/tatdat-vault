---
title: Adaptive Large Neighborhood Search for MIP (ALNS-MIP)
category: concepts
tags: [mip, alns, primal-heuristics, optimization]
relationships:
  - target: "[[references/hendel2022-adaptive-lns-for-mip]]"
    type: derived_from
  - target: "[[concepts/large-neighborhood-search]]"
    type: extends
  - target: "[[concepts/hyper-heuristics]]"
    type: related_to
  - target: "[[concepts/variable-neighborhood-search]]"
    type: related_to
  - target: "[[references/gendreau2019-handbook-metaheuristics]]"
    type: related_to
  - target: "[[references/ha2020-vrp-synchronization-lp-alns]]"
    type: related_to
  - target: "[[references/li2024drone]]"
    type: derived_from
  - target: "[[references/sacramento2019-vrp-d-truck-drone-alns-cost]]"
    type: derived_from
  - target: "[[concepts/alns-destroy-repair-operator-suite]]"
    type: related_to
    note: "Reciprocal - concepts/alns-destroy-repair-operator-suite references this page."
    confidence: 0.7
    basis: observed
    since: "2026-10-30T14:38:55Z"
  - target: "[[concepts/cumulative-volume-lower-bound-cp-search]]"
    type: related_to
    note: "Reciprocal - concepts/cumulative-volume-lower-bound-cp-search references this page."
    confidence: 0.7
    basis: observed
    since: "2026-10-30T14:38:55Z"
  - target: "[[concepts/fuzzy-weighted-max-min-scalarization]]"
    type: related_to
    note: "Reciprocal - concepts/fuzzy-weighted-max-min-scalarization references this page."
    confidence: 0.7
    basis: observed
    since: "2026-10-30T14:38:55Z"
  - target: "[[concepts/large-neighborhood-ship-pair-destroy-repair]]"
    type: related_to
    note: "Reciprocal - concepts/large-neighborhood-ship-pair-destroy-repair references this page."
    confidence: 0.7
    basis: observed
    since: "2026-10-30T14:38:55Z"
  - target: "[[concepts/metaheuristic-hybridization]]"
    type: related_to
    note: "Reciprocal - concepts/metaheuristic-hybridization references this page."
    confidence: 0.7
    basis: observed
    since: "2026-10-30T14:38:55Z"
  - target: "[[concepts/simulated-annealing-metropolis-cooling]]"
    type: related_to
    note: "Reciprocal - concepts/simulated-annealing-metropolis-cooling references this page."
    confidence: 0.7
    basis: observed
    since: "2026-10-30T14:38:55Z"
  - target: "[[references/hartman2023-leximin-approximation]]"
    type: related_to
    note: "Reciprocal - references/hartman2023-leximin-approximation references this page."
    confidence: 0.7
    basis: observed
    since: "2026-10-30T14:38:55Z"
  - target: "[[references/pisinger2019-large-neighborhood-search]]"
    type: related_to
    note: "Reciprocal - references/pisinger2019-large-neighborhood-search references this page."
    confidence: 0.7
    basis: observed
    since: "2026-10-30T14:38:55Z"
  - target: "[[references/ropke2006-adaptive-large-neighborhood-search-pdptw]]"
    type: related_to
    note: "Reciprocal - references/ropke2006-adaptive-large-neighborhood-search-pdptw references this page."
    confidence: 0.7
    basis: observed
    since: "2026-10-30T14:38:55Z"
  - target: "[[references/windrasmara2022-alns-multi-drop-fstsp]]"
    type: related_to
    note: "Reciprocal - references/windrasmara2022-alns-multi-drop-fstsp references this page."
    confidence: 0.7
    basis: observed
    since: "2026-10-30T14:38:55Z"
  - target: "[[references/zhao2025-lns-hgs-inventory-routing]]"
    type: related_to
    note: "Reciprocal - references/zhao2025-lns-hgs-inventory-routing references this page."
    confidence: 0.7
    basis: observed
    since: "2026-10-30T14:38:55Z"
sources:
  - _papers/hendel2022adaptive/hendel2022adaptive-extracted.md
  - _papers/hendel2022adaptive/hendel2022adaptive.md
  - _papers/ha2020new/ha2020new-extracted.md
  - _papers/ha2020new/ha2020new.md
summary: ALNS-MIP adaptively chooses and budgets MIP neighborhood subproblems to improve incumbents within branch-and-bound.
provenance:
  extracted: 0.88
  inferred: 0.10
  ambiguous: 0.02
base_confidence: 0.87
lifecycle: draft
lifecycle_changed: 2026-10-29T17:15:00Z
tier: core
created: 2026-10-22T10:00:17Z
updated: 2026-10-30T14:38:55Z
---

# Adaptive Large Neighborhood Search for MIP (ALNS-MIP)

ALNS-MIP is a primal-heuristic design pattern that frames MIP improvement as repeated selection and solution of auxiliary subproblems with adaptive control.

## Key Ideas

- Maintain a portfolio of neighborhood subproblem types rather than one fixed heuristic; the published instantiation runs the framework around eight well-known LNS heuristics as a primal heuristic in SCIP.
- Select the next subproblem using reward-driven adaptation (multi-armed-bandit-style policy).
- Control fixing rates and local effort dynamically to avoid repeatedly solving either too-easy or too-hard neighborhoods.
- Use effort-aware rewards that combine "found better incumbent" and "closed meaningful primal-dual gap" signals: a solution reward for reaching a new incumbent, a closed-gap reward for the objective improvement toward the dual bound, and an effort term that approximates the run time spent and compensates for different target fixing rates, blended by two convex-combination parameters. ^[inferred]

Compared with static heuristic scheduling, ALNS-MIP offers a principled way to spend primal search budget where it is most productive in the current search state. ^[inferred]

Related pages: [[references/hendel2022-adaptive-lns-for-mip]], [[concepts/large-neighborhood-search]], [[concepts/hyper-heuristics]], [[concepts/variable-neighborhood-search]], [[references/gendreau2019-handbook-metaheuristics]], [[references/ha2020-vrp-synchronization-lp-alns]].

## Open Questions

- How stable are selector and reward hyperparameters across solver versions and new benchmark families?
- What is the best way to co-budget ALNS with other primal heuristics in large-scale production MIP pipelines? ^[inferred]

## Related

- [[references/zhao2025-lns-hgs-inventory-routing]] — the authors name adaptive LNS as a natural host for their whole-horizon DP repair operator
- [[references/windrasmara2022-alns-multi-drop-fstsp]] — multi-drop FSTSP solved with an ALNS MIP-style set-partitioning formulation.
- [[references/li2024drone]] — shares alns + optimization tags with this page
- [[references/sacramento2019-vrp-d-truck-drone-alns-cost]] — shares alns + mip tags with this page

## Sources

- [[_papers/hendel2022adaptive/hendel2022adaptive-extracted.md]]
- [[_papers/hendel2022adaptive/hendel2022adaptive.md]]
- [[_papers/ha2020new/ha2020new-extracted.md]]
- [[_papers/ha2020new/ha2020new.md]]
