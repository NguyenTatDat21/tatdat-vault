---
title: Adaptive Large Neighborhood Search for Mixed Integer Programming (Hendel, 2022)
category: references
tags: [paper, mip, alns, primal-heuristics, bandit, scip]
relationships:
  - target: "[[concepts/adaptive-large-neighborhood-search-for-mip]]"
    type: uses
  - target: "[[references/yang2022-vrpd-bilevel-heuristic]]"
    type: related_to
  - target: "[[concepts/large-neighborhood-search]]"
    type: extends
  - target: "[[concepts/hyper-heuristics]]"
    type: related_to
  - target: "[[references/gendreau2019-handbook-metaheuristics]]"
    type: related_to
  - target: "[[concepts/branch-and-cut]]"
    type: related_to
  - target: "[[concepts/disjunctive-scheduling-constraint-programming-model]]"
    type: related_to
  - target: "[[concepts/large-neighborhood-ship-pair-destroy-repair]]"
    type: related_to
  - target: "[[references/dorling2017-drone-delivery-vrp]]"
    type: related_to
  - target: "[[references/goel2015-constraint-programming-lng-ship-scheduling]]"
    type: related_to
  - target: "[[references/ropke2006-adaptive-large-neighborhood-search-pdptw]]"
    type: related_to
sources:
  - _papers/hendel2022adaptive/hendel2022adaptive-extracted.md
  - _papers/hendel2022adaptive/hendel2022adaptive.md
  - _papers/hendel2022adaptive/images/page_0_image_2.jpg
  - _papers/hendel2022adaptive/images/page_17_image_2.jpg
  - _papers/hendel2022adaptive/images/page_19_chart_2.jpg
  - _papers/hendel2022adaptive/images/page_24_chart_2.jpg
  - _papers/hendel2022adaptive/images/page_25_chart_2.jpg
  - _papers/hendel2022adaptive/images/page_27_chart_2.jpg
summary: >-
  Integrates ALNS operator adaptation, partial fixing, and local-neighborhood bound tightening into a general MIP solver, and quantifies the extra speedup ALNS gives SCIP over the last eight years.
provenance:
  extracted: 0.92
  inferred: 0.07
  ambiguous: 0.01
base_confidence: 0.67
lifecycle: draft
lifecycle_changed: 2026-10-22
tier: core
summary: "Adaptive LNS for mixed integer programs: bandit-selected destroy and repair operators that improve primal heuristics inside SCIP."
created: 2026-10-22T10:00:17Z
updated: 2026-10-30T14:38:55Z
---

# Adaptive Large Neighborhood Search for Mixed Integer Programming (Hendel, 2022)

> [!tldr] The paper turns ALNS into a general-purpose MIP primal framework by adaptively choosing among multiple auxiliary subproblems and tuning fixing/node budgets from observed performance.

## Problem & Scope

The work addresses a practical gap: LNS-style ideas were effective in specific MIP settings, but a broadly reusable, solver-integrated adaptive framework was missing.

Target setting is generic MIP primal improvement inside a full branch-and-bound solver (SCIP), not a single problem class.

## Method / Architecture

The framework runs ALNS rounds over a portfolio of eight auxiliary problems: RENS, RINS, Crossover, Mutation, Local Branching, Proximity, Zero Objective and DINS. Two of the most successful in the experiments, DINS and Local Branching, had previously been inactive in SCIP and are activated within ALNS by default from SCIP 5.0.

Each round:
1. selects one auxiliary problem with a multi-armed bandit strategy — α-UCB, γ-UCB or EXP3 — where α-UCB uses $\alpha = 0.0016$ in the SCIP experiments and tests one previously unseen action per round during the first eight rounds,
2. applies generic (un)fixing policies,
3. solves under controlled node/time effort,
4. computes reward from solution quality and effort (reward parameters $\eta_1 = 0.5$ baseline, $\eta_2 = 0.8$ control),
5. updates selector weights and dynamic limits.

Key adaptive controls include:
- a dynamic fixing-rate target bounded to avoid degenerate neighborhoods (initial 0.9 for every auxiliary problem, adjusted dynamically in [0.3, 0.9]),
- a dynamic stall-node limit (50 nodes, $\kappa_0 = 500$ nodes at a found solution, $\kappa_1 = 0.5$ share of main-search nodes, with a lower budget threshold of 0.1),
- effort-aware rewards that combine solution success and gap-closing behavior.

## Results

Reported computational evidence includes large-scale simulation plus SCIP integration experiments.

- Calibration and auxiliary-problem comparison used the union of MIPLIB 3.0, 2003, 2010 and Coral — 666 instances — on SCIP 5.0 with CPLEX 12.7.1, single-threaded, with a 5 h time limit; fixing-rate targets {0.1, …, 0.9} in steps of 0.2 with ±0.1 tolerance and a fixed stall limit of 50 nodes.
- Adaptive selector calibration: α-UCB was the best performing of the three tested bandit strategies, and α-UCB also gives the simplest explanation of why an auxiliary problem was chosen. A larger α makes weaker actions more frequent.
- In SCIP 7.0.2 (ALNS on by default), ALNS on versus off achieved a 1% speedup and a 17% primal-integral improvement overall on 720 test instances with a 1 h limit and three random seeds; on the 195 instances where the solving process differed, time improved by 6% and primal integral by 37%, on the 155 Equal instances ALNS off was 2% better in both, and on the harder bracket [100, 3600] time improved 5% and primal integral 20%.

![[_papers/hendel2022adaptive/images/page_24_chart_2.jpg]]

*Fig. 3 (paper): Solution rates (left) and average rewards (right) at different fixing rates*

## Limitations

- Improvements are aggregate and benchmark-dependent: ALNS solved four records fewer than ALNS off in the aggregate groups, with 16 records exclusively solved by one setting across 14 instances, which the paper attributes to performance variability rather than systematic deterioration.
- The released version needed modifications for SCIP 7.0.2: fractionality-based fixing for RENS (the only neighborhood without a reference solution), multiple ALNS calls inside the root node, local reduced costs and pseudo-costs for generic fixing, a lower node-budget threshold of 0.1, and a cap on ALNS calls per incumbent equal to the number of active neighborhoods.
- Auxiliary-problem selection and reward shaping add calibration surface that may need retuning across solver versions. ^[inferred]
- Neighborhoods are not universally applicable: Local Branching and Proximity need binary variables, Zero Objective needs a nonzero objective, so the comparison focused on instances where all eight neighborhoods are valid. ^[extracted]
- Auxiliary-problem selection and reward shaping add calibration surface that may need retuning across solver versions. ^[inferred]
- The reward diagram, bandit illustration and several tables are rendered as images in the extracted markdown; parameter values were read from Table 2 ($\delta$ = 0.01, $k$ = 2, $d_{max} = 0.2 \cdot n_b$, $|X^{DINS}|$ = 5). ^[extracted]

## Related

- [[concepts/adaptive-large-neighborhood-search-for-mip]]
- [[concepts/large-neighborhood-search]]
- [[concepts/hyper-heuristics]]
- [[references/gendreau2019-handbook-metaheuristics]]
- [[references/yang2022-vrpd-bilevel-heuristic]]
- [[_papers/hendel2022adaptive/hendel2022adaptive-extracted]]
- [[concepts/large-neighborhood-search]]
- [[concepts/hyper-heuristics]]
- [[references/gendreau2019-handbook-metaheuristics]]
- [[_papers/hendel2022adaptive/hendel2022adaptive-extracted]]

## Bibliographic Record

- Citation key: `hendel2022adaptive`
- DOI: `10.1007/s12532-021-00209-7`
- Canonical URL: <https://doi.org/10.1007/s12532-021-00209-7>
- Publication: *Mathematical Programming Computation* (2022)
- Authors: Gregor Hendel
- Companion metadata note: [[_papers/hendel2022adaptive/hendel2022adaptive.md]]

## Sources

- [[_papers/hendel2022adaptive/hendel2022adaptive-extracted.md]]
- [[_papers/hendel2022adaptive/hendel2022adaptive.md]]
- [[_papers/hendel2022adaptive/images/page_0_image_2.jpg]]
- [[_papers/hendel2022adaptive/images/page_19_chart_2.jpg]]
- [[_papers/hendel2022adaptive/images/page_24_chart_2.jpg]]
- [[_papers/hendel2022adaptive/images/page_25_chart_2.jpg]]
- [[_papers/hendel2022adaptive/images/page_27_chart_2.jpg]]
