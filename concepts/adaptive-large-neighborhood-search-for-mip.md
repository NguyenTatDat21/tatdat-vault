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
base_confidence: 0.77
lifecycle: draft
lifecycle_changed: 2026-10-22
tier: core
created: 2026-10-22T10:00:17Z
updated: 2026-10-27T06:00:00Z
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

## Sources

- [[_papers/hendel2022adaptive/hendel2022adaptive-extracted.md]]
- [[_papers/hendel2022adaptive/hendel2022adaptive.md]]
- [[_papers/ha2020new/ha2020new-extracted.md]]
- [[_papers/ha2020new/ha2020new.md]]
