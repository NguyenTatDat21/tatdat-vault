---
title: "Constraint Programming Models for Container Pre-Marshalling"
category: references
tags: [constraint-programming, container-premarshalling, yard-scheduling, maritime-terminals, model-strengthening]
relationships:
  - target: "[[concepts/disjunctive-scheduling-constraint-programming-model]]"
    type: related_to
  - target: "[[references/ku2016-mixed-integer-programming-job-shop]]"
    type: related_to
  - target: "[[references/furini2016-two-dimensional-guillotine-cutting-ip]]"
    type: related_to
sources:
  - _papers/jimenez-piqueras2023constraint/jimenez-piqueras2023constraint-extracted.md
  - _papers/jimenez-piqueras2023constraint/jimenez-piqueras2023constraint.md
  - _papers/jimenez-piqueras2023constraint/images/page_3_image_2.jpg
summary: >-
  A five-model CP series for container premarshalling: each added decision-variable group cuts solve time, and the best model beats the state-of-the-art IP on all datasets.
provenance:
  extracted: 0.85
  inferred: 0.10
  ambiguous: 0.05
base_confidence: 0.67
lifecycle: draft
lifecycle_changed: 2026-10-25
tier: supporting
created: 2026-10-25T11:47:49Z
updated: 2026-10-25T11:47:49Z
---

# Constraint Programming Models for Container Pre-Marshalling

> [!tldr] Jiménez-Piqueras, Parreño-Torres, Álvarez-Valdés and Ruiz build five CP feasibility models for the container premarshalling problem; each new group of decision variables improves the model, and the final model beats the state-of-the-art integer program IPS6 on all four datasets.

## Problem & Contribution

- Container premarshalling (CPMP): reorder a bay of stacks (positions s, tiers t, priority groups p, input layout f_{s,t}) with minimum crane moves ⟨s′,s″⟩ so that no container with a later retrieval lies below one with an earlier retrieval, without moving any container out of the bay. NP-hard.
- Prior CP was only Rendl & Prandtstetter 2013 (ad-hoc heuristic); state-of-the-art exact method is the IPS6 integer program (Parreño-Torres et al. 2019); best heuristics use deep-learning-assisted tree search.
- Key finding: CP model construction logic differs radically from MILP — adding new groups of decision variables at each model improves performance, a pattern opposite to normal MILP strengthening.

## Method

Pure feasibility CP models solved iteratively: start at the lower bound k̄, increase by 1 until feasible, exactly one crane move per stage; optimality is guaranteed by construction.
- CP2: integer priority variables x_{s,t}^k per stage (Eq. 2 multiplicity invariance, ordered final layout, slot stability, one movement per stage, move rules, transitive-move avoidance).
- CP3 adds binary occupancy δ_{s,t}^k; CP4 adds binary move-origin z_{s,t}^k (z is not needed to describe the problem, δ does not help describe it either, yet both improve performance), linking x, y, δ, z via constraints 21-27 including symmetry cuts.
- CP5 adds blocking-container variables w_{s,t}^k (constraints 28-33; constraint 33 discards infeasible stages early).
Solvers: CPLEX 20.1.0 / CP Optimizer, 4 vCPU VMs, 3600 s; datasets BZ (960 instances), ZJY (100), EMM (417), CV (399, hardest).

![[_papers/jimenez-piqueras2023constraint/images/page_3_image_2.jpg]]
*"Fig. 1. Example of an optimal solution for the problem. Blocking containers are shaded and the container moved at each stage is indicated with a thick border." (verbatim).* The example bay's optimal solution uses 4 movements {⟨3,1⟩, ⟨2,1⟩, ⟨3,2⟩, ⟨4,3⟩} across five bay configurations.

## Results

Instances solved optimally / average time (s), per dataset:

| Dataset | CP2 | CP3 | CP4 | CP5 | IPS6 |
|---|---|---|---|---|---|
| BZ (960) | 790 / 87.0 | 808 / 28.2 | 878 / 4.8 | 906 / 2.8 | 900 |
| ZJY (100) | 26 / 721.6 | 42 / 263.4 | 68 / 9.7 | 93 / 5.6 | 82 |
| EMM (417) | 313 / 116.6 | 320 / 39.1 | 344 / 6.7 | 362 / 5.8 | 360 |
| CV (399) | 102 / 330.3 | 145 / 54.5 | 205 / 7.5 | 281 / 4.3 | 162 |

- Each variable group adds a step: CP3 +7.5% solved on average, CP4 +13.2%, CP5 +13% more; CP2 needs >75× the time of CP5 on ZJY/CV and >20× on BZ/EMM.
- CP5 beats IPS6 on every dataset: +30 percentage points on CV, 12× and 22× faster on EMM and CV.
- Cross-paradigm transfer fails: running the CP5 improvement strategy inside an IP solves 52% fewer ZJY instances than CP5 alone; the IPS6 strategy inside CP loses 6-33% and is 16-46× slower.
- The iterative algorithm (increase k̄ from the lower bound) is drastically better than the objective-function (minimize k̄) variant.

## Limitations

- EMM counts 417 instances while the source dataset has 445; the paper does not explain the reduction. ^[ambiguous]
- Feasibility-only models: no objective function variant was competitive; datasets are synthetic bay layouts.
- The cross-paradigm asymmetry implies heuristic-design knowledge does not transfer between CP and MILP, so model-strengthening must be validated in the target solver. ^[inferred]

## Related

- [[concepts/disjunctive-scheduling-constraint-programming-model]]
- [[concepts/auxiliary-decision-variable-model-strengthening]]
- [[references/ku2016-mixed-integer-programming-job-shop]]

## Bibliographic Record

- Citation key: jimenez-piqueras2023constraint — Jiménez-Piqueras, Celia; Parreño-Torres, Consuelo; Ruiz, Rubén; Álvarez-Valdés, Ramón, "Constraint programming models for the container premarshalling problem in yard terminals", European Journal of Operational Research, 2023-04-16.
- DOI: 10.1016/j.ejor.2022.07.042. Canonical URL: https://doi.org/10.1016/j.ejor.2022.07.042 (open access, CC BY-NC-ND).
- Funding: PRE2019-087706, RTI2018-094940-B-I00 (Spanish projects).
- Companion metadata: [[_papers/jimenez-piqueras2023constraint/jimenez-piqueras2023constraint.md|jimenez-piqueras2023constraint metadata]]

## Sources

- [[_papers/jimenez-piqueras2023constraint/jimenez-piqueras2023constraint-extracted.md]]
- [[_papers/jimenez-piqueras2023constraint/jimenez-piqueras2023constraint.md]]
- [[_papers/jimenez-piqueras2023constraint/images/page_3_image_2.jpg]]
