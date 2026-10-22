---
title: Adaptive Large Neighborhood Search for Mixed Integer Programming (Hendel, 2022)
category: references
tags: [paper, mip, alns, primal-heuristics]
relationships:
  - target: "[[concepts/adaptive-large-neighborhood-search-for-mip]]"
    type: uses
  - target: "[[concepts/large-neighborhood-search]]"
    type: extends
  - target: "[[concepts/hyper-heuristics]]"
    type: related_to
  - target: "[[references/gendreau2019-handbook-metaheuristics]]"
    type: related_to
sources:
  - _papers/hendel2022adaptive/hendel2022adaptive-extracted.md
  - _papers/hendel2022adaptive/hendel2022adaptive.md
  - _papers/hendel2022adaptive/images/page_0_image_2.jpg
  - _papers/hendel2022adaptive/images/page_19_chart_2.jpg
  - _papers/hendel2022adaptive/images/page_24_chart_2.jpg
  - _papers/hendel2022adaptive/images/page_25_chart_2.jpg
  - _papers/hendel2022adaptive/images/page_27_chart_2.jpg
summary: Proposes ALNS as a general MIP primal heuristic with adaptive subproblem selection and dynamic budgets, improving SCIP primal quality on broad benchmarks.
provenance:
  extracted: 0.90
  inferred: 0.08
  ambiguous: 0.02
base_confidence: 0.67
lifecycle: draft
lifecycle_changed: 2026-10-22
tier: supporting
created: 2026-10-22T10:00:17Z
updated: 2026-10-22T18:14:03Z
---

# Adaptive Large Neighborhood Search for Mixed Integer Programming (Hendel, 2022)

> [!tldr] The paper turns ALNS into a general-purpose MIP primal framework by adaptively choosing among multiple auxiliary subproblems and tuning fixing/node budgets from observed performance.

## Problem & Scope

The work addresses a practical gap: LNS-style ideas were effective in specific MIP settings, but a broadly reusable, solver-integrated adaptive framework was missing.

Target setting is generic MIP primal improvement inside a full branch-and-bound solver (SCIP), not a single problem class.

## Method / Architecture

The framework runs ALNS rounds over a portfolio of auxiliary problems (including RINS, RENS, mutation/crossover-style neighborhoods, local branching, proximity search, zero-objective variants, and DINS).

Each round:
1. selects one auxiliary problem via bandit-style scoring,
2. applies generic (un)fixing policies,
3. solves under controlled node/time effort,
4. computes reward from solution quality and effort,
5. updates selector weights and dynamic limits.

Key adaptive controls include:
- a dynamic fixing-rate target bounded to avoid degenerate neighborhoods,
- a dynamic stall-node limit,
- effort-aware rewards that combine solution success and gap-closing behavior.

## Results

Reported computational evidence includes large-scale simulation plus SCIP integration experiments.

- Simulation and comparison were performed on a broad mixed benchmark pool (MIPLIB + Coral) with 666 instances.
- Adaptive selector calibration favored alpha-UCB among tested selectors.
- In SCIP integration, turning ALNS on yielded about **1% runtime improvement** and **17% primal-integral improvement** on aggregate, with stronger gains on instances where search paths materially diverged.

## Limitations

- Improvements are aggregate and benchmark-dependent; effect size can vary by instance structure and incumbent quality.
- Auxiliary-problem selection and reward shaping add calibration surface that may need retuning across solver versions. ^[inferred]
- Some figure-heavy lines in extracted text are oversized and partially elided by tooling; table-level micro-details may need PDF spot-checks. ^[ambiguous]

## Related

- [[concepts/adaptive-large-neighborhood-search-for-mip]]
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
