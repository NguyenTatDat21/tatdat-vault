---
title: "Mixed Integer Programming for the Job Shop Scheduling Problem"
category: references
tags: [mixed-integer-programming, constraint-programming, scheduling, job-shop, benchmarking, disjunctive-models]
relationships:
  - target: "[[concepts/disjunctive-scheduling-constraint-programming-model]]"
    type: related_to
  - target: "[[references/goel2015-constraint-programming-lng-ship-scheduling]]"
    type: related_to
  - target: "[[references/furini2016-two-dimensional-guillotine-cutting-ip]]"
    type: related_to
  - target: "[[references/pesant2015-cp2015-proceedings]]"
    type: related_to
  - target: "[[concepts/auxiliary-decision-variable-model-strengthening]]"
    type: related_to
    note: "Reciprocal - concepts/auxiliary-decision-variable-model-strengthening references this page."
    confidence: 0.7
    basis: observed
    since: "2026-10-30T14:38:55Z"
  - target: "[[references/isik2023-constraint-programming-hybrid-flow-shop]]"
    type: related_to
    note: "Reciprocal - references/isik2023-constraint-programming-hybrid-flow-shop references this page."
    confidence: 0.7
    basis: observed
    since: "2026-10-30T14:38:55Z"
  - target: "[[references/jimenez-piqueras2023-constraint-programming-premarshalling]]"
    type: related_to
    note: "Reciprocal - references/jimenez-piqueras2023-constraint-programming-premarshalling references this page."
    confidence: 0.7
    basis: observed
    since: "2026-10-30T14:38:55Z"
sources:
  - _papers/ku2016mixed/ku2016mixed-extracted.md
  - _papers/ku2016mixed/ku2016mixed.md
  - _papers/ku2016mixed/images/page_3_image_0.jpg
  - _papers/ku2016mixed/images/page_9_chart_0.jpg
  - _papers/ku2016mixed/images/page_9_chart_2.jpg
  - _papers/ku2016mixed/images/page_11_chart_0.jpg
  - _papers/ku2016mixed/images/page_11_chart_2.jpg
  - _papers/ku2016mixed/images/page_15_chart_0.jpg
  - _papers/ku2016mixed/images/page_15_chart_2.jpg
summary: >-
  Benchmarking four classic JSP MIP models in CPLEX, GUROBI, SCIP and against CP: Manne's disjunctive model wins in CPLEX/GUROBI, CP dominates large instances.
provenance:
  extracted: 0.87
  inferred: 0.10
  ambiguous: 0.03
base_confidence: 0.67
lifecycle: draft
lifecycle_changed: 2026-10-25
tier: core
created: 2026-10-25T11:47:49Z
updated: 2026-10-30T14:38:55Z
---

# Mixed Integer Programming for the Job Shop Scheduling Problem

> [!tldr] Ku and Beck benchmark four classic MIP models for the classical job shop (minimum makespan) in three modern solvers: the Manne disjunctive model performs best in CPLEX/GUROBI, SCIP flips the ranking, and constraint programming is the strongest for large instances.

## Problem & Contribution

- Four MIP models: Manne's disjunctive big-M model, Liao's disjunctive variant (surplus variables q), the time-indexed Kondili model, and the rank-based Wagner model, benchmarked with modern solvers and 64-bit machines — none had been tested this way.
- Instance classes: {3×3 … 20×20}, 10 each, generated with the Taillard generator, processing times U[1,20]; plus Taillard ta01-ta20; 3600 s limit; CPLEX 12.6.2, GUROBI 6.0.4, SCIP 3.1.1, IBM ILOG CP Optimizer.
- Finding: judging models by model size is error-prone; modern MIP proves optimality for moderate-size JSP quickly.

## Method

The Manne model uses start times x_ij and binary precede variables z_ijk with a big-M bound V = Σ p_ij; Liao adds surplus variables via $$V z_{ijk} + (x_{ij} - x_{ik}) - p_{ik} = q_{ijk}, \quad q_{ijk} \le V - p_{ij} - p_{ik}$$ making the disjunction an equality; the time-indexed model uses binaries x_ijt (size ∝ |J||M||H|, pseudo-polynomial); the rank-based model uses binaries x_ijk for position with implied start times. Model sizes: disjunctive |J|²|M| binaries, rank-based |J|²|M| binaries with |J|³|M| constraints.

![[_papers/ku2016mixed/images/page_3_image_0.jpg]]
*"Figure 1: Job Shop Scheduling Problem. Three jobs J1, J2, and J3 are to be scheduled on three machines M1, M2 and M3. The graph on the top represents the precedence constraints. The Gantt Chart on the bottom displays a feasible schedule which satisfies the precedence constraints." (verbatim).*

## Results

CPLEX geometric-mean solve times (seconds, # optimal of 10):

| Model | 10×10 | 12×12 | 15×15 | 20×15 |
|---|---|---|---|---|
| Manne | 3.19, 10 Opt | 99.43, 10 Opt | 1568.89, 5 Opt | none |
| Liao | 7.62 | 386.58, 8 | 3463.38, 1 | none |
| Rank-based | fails from 8×8 | — | — | — |
| Time-indexed | fits up to 5×5 in 8 GB | beats rank-based below 8×8 | 8 GB memory failure | — |

- GUROBI results are consistent with CPLEX (Manne best, slightly faster on the other three at small sizes). SCIP reverses: Liao beats Manne up to 12×12 because SCIP presolving eliminates the q variables, transforming Liao into Manne — perturbing Manne's constraint order reproduces the Liao-like gain.
- Indicator constraints (CPLEX IF/OR) perform worse than the big-M Manne model; multi-threading ≈3× faster; parameter tuning adds ≈1.5× (≈4.5× total on 12×12), MRE ≈30% for non-solvable instances; the tuning tool finds no change for Taillard instances.

MIP (Manne, multi-thread + tuning) vs CP Optimizer (geometric mean, # Opt/10):

| Size | MIP | CP |
|---|---|---|
| 12×12 | 33.19, 10/10 | 3.58, 10/10 |
| 15×15 | 1568.89, 7/10 | 39.57, 10/10 |
| 20×15 | none | 1037.81, 6/10 |

- Mean relative error vs the exact iSTS-SGS: MIP 2.3% on random 20×20, 6.2% on ta11-ta20; CP 0.6% and 0.5%.

![[_papers/ku2016mixed/images/page_9_chart_0.jpg]] ![[_papers/ku2016mixed/images/page_9_chart_2.jpg]]
*"Figure 5: MRE Performance Over Time for the Disjunctive MIP Models using CPLEX." (verbatim; subfigures "(a) 15 × 15 problems", "(b) ta01 - ta10")*

![[_papers/ku2016mixed/images/page_11_chart_0.jpg]] ![[_papers/ku2016mixed/images/page_11_chart_2.jpg]]
*"Figure 6: MRE Performance Over Time for the Disjunctive MIP Models using SCIP." (verbatim; subfigures "(a) 15 × 15 problems", "(b) ta01 - ta10")*

![[_papers/ku2016mixed/images/page_15_chart_0.jpg]] ![[_papers/ku2016mixed/images/page_15_chart_2.jpg]]
*"Figure 7: MRE Performance Over Time of the MIP Models, CP Model and iSTS-SGS. Note that for the ta11 - ta20 problems, the tuning tool does not find parameter settings different from the default. Therefore we do not plot the curve for multi+tune." (verbatim; subfigures "(a) 20 × 20 problems", "(b) ta11 - ta20")*

## Limitations

- 3600 s cap and one 8 GB machine: the time-indexed model does not fit at 15×15, and CP thread non-determinism worsens CP by ≈1.6× (single-thread CP is used in the comparison).
- Off-the-shelf CP, not the state-of-the-art CP, already beats MIP on large JSP; the results argue for solver-empirical model choice over model-size analysis. ^[inferred]

## Related
- [[references/pesant2015-cp2015-proceedings]] — shares constraint-programming + scheduling tags with this page

- [[concepts/disjunctive-scheduling-constraint-programming-model]]
- [[concepts/auxiliary-decision-variable-model-strengthening]]
- [[references/goel2015-constraint-programming-lng-ship-scheduling]]

## Bibliographic Record

- Citation key: ku2016mixed — Ku, Wen-Yang; Beck, J. Christopher, "Mixed integer programming for the job shop scheduling problem", Computers & Operations Research, 2016-09.
- DOI: 10.1016/j.cor.2016.04.006. Canonical URL: https://doi.org/10.1016/j.cor.2016.04.006 (S0305054816300764).
- Companion metadata: [[_papers/ku2016mixed/ku2016mixed.md|ku2016mixed metadata]]

## Sources

- [[_papers/ku2016mixed/ku2016mixed-extracted.md]]
- [[_papers/ku2016mixed/ku2016mixed.md]]
- [[_papers/ku2016mixed/images/page_3_image_0.jpg]]
- [[_papers/ku2016mixed/images/page_9_chart_0.jpg]]
- [[_papers/ku2016mixed/images/page_9_chart_2.jpg]]
- [[_papers/ku2016mixed/images/page_11_chart_0.jpg]]
- [[_papers/ku2016mixed/images/page_11_chart_2.jpg]]
- [[_papers/ku2016mixed/images/page_15_chart_0.jpg]]
- [[_papers/ku2016mixed/images/page_15_chart_2.jpg]]
