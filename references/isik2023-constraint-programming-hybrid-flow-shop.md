---
title: "Constraint Programming Models for Hybrid Flow Shop Scheduling"
category: references
tags: [constraint-programming, mixed-integer-programming, scheduling, makespan]
relationships:
  - target: "[[concepts/disjunctive-scheduling-constraint-programming-model]]"
    type: related_to
  - target: "[[references/ku2016-mixed-integer-programming-job-shop]]"
    type: related_to
  - target: "[[references/goel2015-constraint-programming-lng-ship-scheduling]]"
    type: related_to
  - target: "[[references/pesant2015-cp2015-proceedings]]"
    type: related_to
  - target: "[[concepts/auxiliary-decision-variable-model-strengthening]]"
    type: related_to
  - target: "[[concepts/failure-directed-search]]"
    type: related_to
sources:
  - _papers/isik2023constraint/isik2023constraint-extracted.md
  - _papers/isik2023constraint/isik2023constraint.md
  - _papers/isik2023constraint/images/page_6_image_8.jpg
  - _papers/isik2023constraint/images/page_7_image_2.jpg
  - _papers/isik2023constraint/images/page_21_chart_4.jpg
  - _papers/isik2023constraint/images/page_21_chart_5.jpg
  - _papers/isik2023constraint/images/page_21_chart_6.jpg
  - _papers/isik2023constraint/images/page_21_chart_7.jpg
summary: >-
  First CP models for blocked and SDST hybrid flow shops with unrelated machines and eligibility; CP beats two new MILP models on all instance sizes.
provenance:
  extracted: 0.89
  inferred: 0.06
  ambiguous: 0.05
base_confidence: 0.67
lifecycle: draft
lifecycle_changed: 2026-10-25
tier: core
created: 2026-10-25T11:47:49Z
updated: 2026-10-30T17:41:00Z
---

# Constraint Programming Models for Hybrid Flow Shop Scheduling

> [!tldr] Işık, Topaloglu Yildiz and Şatır Akpunar build the first constraint programming models for hybrid flow shops with unrelated machines, machine eligibility, blocking, sequence-dependent setup times and their combinations; CP beats two new MILP models at every instance size.

## Problem & Contribution

- HFSP with unrelated parallel machines per stage and job-machine eligibility sets E_{j,m}, minimizing makespan; variants HFSP-NW (no-wait), HFSP-B (blocking), HFSP-SDST, HFSP-SDST-NW, HFSP-SDST-B.
- First CP models for HFSP-B, HFSP-SDST-NW and HFSP-SDST-B with unrelated machines and eligibility; two new time-indexed MILP models for HFSP-SDST-NW and HFSP-SDST-B; CP and MILP compared for HFSP and HFSP-SDST against Meng et al. 2020 models.
- 90 new larger instances (20/30/40 jobs, 2-4 stages); optimality confirmed for 20 benchmark instances whose optimal values were previously unconfirmed in all HFSP variants.

## Method

CP (IBM CP Optimizer, OPL 12.10, 600 s): mandatory interval X_{j,s} per job-stage, optional intervals Y_{j,s,m} with \text{alternative}(X_{j,s}, \{Y_{j,s,m}\}_{m \in E_{j,m}}), per-stage machine interval sequences Stg_{s,m} with noOverlap(Stg, setup matrix St_{s,m,j,j'}), endBeforeStart for idle stages, endAtStart for no-wait, blocking expressed through startOfNext on sequences, and redundant Cumulative \le |M_s| constraints. The makespan C_max is defined as a decision expression (endOf), which reduces variables and improves solution time. Default CP search settings; tree-search and VVO strategies did not improve results.

![[_papers/isik2023constraint/images/page_6_image_8.jpg]]
*"Fig. 1 Flow chart of a general algorithm for CP (Kanet et al. 2004)" (verbatim).*

![[_papers/isik2023constraint/images/page_7_image_2.jpg]]
*"Fig. 2 Visual representation of interval and interval sequence variables" (verbatim).*

MILP: binary assignment X_{j,m}, position Y_{j,m,t}, start times B_{j,s}, precedence binaries Y_{j,j',s}, big-M constraints; no-wait as equality B_{j,s} + P = B_{j,s+1}; blocking via pair constraints. Gap formula: $$Gap\% = \frac{Obj - \max(LB_{CP}, LB_{MILP})}{\max(LB_{CP}, LB_{MILP})} \times 100$$ hardware i5-7200U 2.5 GHz, 8 GB.

## Results

Mean optimality gap on 90 new instances (CP vs MILP, %):

| Variant | CP gap | MILP gap | CP optima | MILP optima |
|---|---|---|---|---|
| HFSP | 0.00 | 10.07 | 90 | 0 |
| HFSP-NW | 5.77 | 21.63 | 26 | 2 |
| HFSP-B | 17.32 | 29.49 | 13 | 1 |
| HFSP-SDST | 34.01 | 59.85 | 9 | 0 |
| HFSP-SDST-NW | 60.57 | 90.09 | 1 | 0 |
| HFSP-SDST-B | 56.45 | 86.11 | 0 | 0 |

- New instances, HFSP: CP mean objective 690.6, first solution 6.2 s, total 14.2 s; MILP objective 774.2, 594.1 s.
- Benchmark: CP optimal on 13 of 16 HFSP instances vs MILP 7; RealCase2 (50 jobs): CP 1901, MILP infeasible, iterated greedy heuristic 1948 in 215 s.
- HFSP-SDST-NW: CP guarantees an optimum in 12 benchmark instances vs MILP 4 confirmed. ^[ambiguous]

![[_papers/isik2023constraint/images/page_21_chart_4.jpg]] ![[_papers/isik2023constraint/images/page_21_chart_5.jpg]] ![[_papers/isik2023constraint/images/page_21_chart_6.jpg]] ![[_papers/isik2023constraint/images/page_21_chart_7.jpg]]
*"Fig. 3 The variation of the optimality gap value of MILP and CP models" (verbatim; red = MILP, blue = CP).*

## Limitations

- On the hardest variant (HFSP-SDST-B) CP found no optimum on the 90 new instances and hit infeasibility on RealCase2; gaps grow with every added constraint layer.
- CP time limit 600 s; unconfirmed optima may be gaps, not proofs. ^[inferred]
- The paper suggests CP models for batching, preemption, stage-skipping, and matheuristics as future work.

## Related
- [[references/pesant2015-cp2015-proceedings]] — shares constraint-programming + scheduling tags with this page

- [[concepts/disjunctive-scheduling-constraint-programming-model]]
- [[concepts/auxiliary-decision-variable-model-strengthening]]
- [[references/ku2016-mixed-integer-programming-job-shop]]

## Bibliographic Record

- Citation key: isik2023constraint — Işık, Eyüp Ensar; Topaloglu Yildiz, Seyda; Şatır Akpunar, Özge, "Constraint programming models for hybrid flow shop scheduling problems with multiple resource constraints", Soft Computing, 2023-12-01.
- DOI: 10.1007/s00500-023-09086-9. Canonical URL: https://doi.org/10.1007/s00500-023-09086-9
- Data/models: dx.doi.org/10.17632/n4g8cfjg87.1 (Mendeley Data).
- Companion metadata: [[_papers/isik2023constraint/isik2023constraint.md|isik2023constraint metadata]]

## Sources

- [[_papers/isik2023constraint/isik2023constraint-extracted.md]]
- [[_papers/isik2023constraint/isik2023constraint.md]]
- [[_papers/isik2023constraint/images/page_6_image_8.jpg]]
- [[_papers/isik2023constraint/images/page_7_image_2.jpg]]
- [[_papers/isik2023constraint/images/page_21_chart_4.jpg]]
- [[_papers/isik2023constraint/images/page_21_chart_5.jpg]]
- [[_papers/isik2023constraint/images/page_21_chart_6.jpg]]
- [[_papers/isik2023constraint/images/page_21_chart_7.jpg]]
