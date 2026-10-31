---
title: "A Comparison of Acceptance Criteria for the ALNS Metaheuristic"
category: references
tags: [alns, simulated-annealing, paper]
sources:
  - "[[_papers/santini2018comparison/santini2018comparison-extracted.md]]"
  - "[[_papers/santini2018comparison/santini2018comparison.md]]"
relationships:
  - target: "[[concepts/simulated-annealing-metropolis-cooling]]"
    type: extends
  - target: "[[concepts/hyper-heuristics]]"
    type: related_to
  - target: "[[references/ropke2006-adaptive-large-neighborhood-search-pdptw]]"
    type: derived_from
  - target: "[[concepts/duration-objective-depot-discretization]]"
    type: related_to
  - target: "[[concepts/alns-destroy-repair-operator-suite]]"
    type: related_to
  - target: "[[references/shaabani2023-multiproduct-mirp-matheuristic]]"
    type: related_to
  - target: "[[concepts/multi-objective-metaheuristic-tuning-validation]]"
    type: related_to
    type: related_to
  - target: "[[concepts/first-in-first-out-property-in-time-dependent-travel]]"
    type: related_to
  - target: "[[concepts/lengthen-arcs-add-node-ddd-refinement]]"
    type: related_to
  - target: "[[references/sacramento2019-vrp-d-truck-drone-alns-cost]]"
    type: related_to
  - target: "[[references/windrasmara2022-alns-multi-drop-fstsp]]"
    type: related_to
summary: "Santini, Ropke, Hvattum (J. Heuristics 2018): 9 ALNS acceptance criteria on CVRP, CMST, QAP. SA, TA and RRT win; HC/RW lose; linear parameter ending at zero saves a tuning dimension."
base_confidence: 0.67
lifecycle: draft
lifecycle_changed: 2026-10-29T17:15:00Z
tier: core
created: 2026-10-27T06:50:00Z
updated: 2026-10-31T19:26:46Z
provenance:
  extracted: 1.00
  inferred: 0.00
  ambiguous: 0.00
---

> [!tldr] Acceptance criteria are not interchangeable
> Across four ALNS settings, the choice of move acceptance criterion moves the average gap to the best known solution by **more than 0.5 percentage points**. Simulated annealing, threshold acceptance and record-to-record travel form the top group; a version of RRT was statistically undominated in three of four test sets.

## Setup

- Criteria compared: Hill Climbing (HC), Random Walk (RW), Late Acceptance Hill Climbing (LAHC), Threshold Acceptance (TA), Simulated Annealing (SA), Great Deluge (GD), Non-Linear Great Deluge (NLGD), Record-to-Record Travel (RRT), plus **Worse Accept (WA)**, introduced in this paper.
- Test bed: capacitated vehicle routing problem (CVRP), capacitated minimum spanning tree (CMST), quadratic assignment problem (QAP), plus a simple LNS for the CVRP. Parameters for each criterion were tuned before comparison.
- ALNS structure: destroy and repair methods chosen by roulette-wheel selection proportional to past scores; the acceptance criterion decides whether the new solution replaces the current one, using internal state that varies during the run (e.g. SA temperature, exponentially decreasing).
ALNS structure: destroy and repair methods chosen by roulette-wheel selection proportional to past scores; the acceptance criterion decides whether the new solution replaces the current one, using internal state that varies during the run (e.g. SA temperature, exponentially decreasing).

$$
\Pr\{\text{accept}\} = e^{(z - h z)/T}, \qquad T = \frac{z(1-h)}{\ln p}, \qquad T_{RRT} = \frac{z(1-h)}{\ln 0.5}
$$

`z` is the objective of the incumbent, `h z` of the candidate; the record-to-record form replaces the temperature by a threshold `T` that falls from `z(1−h)` toward the value matching `p = 0.5` (`_papers/santini2018comparison/santini2018comparison-extracted.md:200, 221, 227`).

Tuning scored each criterion over `M = 20` runs on 6 tuning instances per problem, with `λ = 10` and 150,000 iterations:

$$
A_{\alpha,k} = \frac{1}{\lambda}\sum_{i} v_{\alpha,i,k}, \qquad D_{\alpha,k} = \frac{A_{\alpha,k} - B_k}{A_{\alpha,k}}, \qquad S_\alpha = \frac{1}{K}\sum_k D_{\alpha,k}
$$

(`:457-471`)
## Ranking

- Best: **SA, RRT, TA**. Middle group (better than HC/RW, worse than the top three): **LAHC, GD, NLGD, WA**. Worst: **HC, RW**.

| Problem | Best criterion (aDev / bDev / aTime, pp and s) | Worst |
| --- | --- | --- |
| CMST | Lin. SA 0.399 / 0.108 / 9.367 | HC 2.226, RW 2.824 |
| CVRP (full ALNS) | Lin. RRT (fixed end) 0.391 / 0.112 / 17.871 | RW 2.583 |
| CVRP (simple LNS) | Lin. RRT (fixed end) 0.754 / 0.241 / 11.685 | RW |
| QAP | Lin. WA (fixed end) 0.136 / 0.041 / 43.402 | — |

Table 4, `_papers/santini2018comparison/santini2018comparison-extracted.md:660-700`.
- In three of four test sets a version of RRT was not beaten by any criterion with statistical significance; in the fourth (full ALNS for CVRP) it was beaten only by another version of RRT.
- **Linear** acceptance-parameter functions (start to end value) do as well as the standard exponential versions, and the end value can often be fixed at zero — quality is not lost and the parameter space loses one dimension.
- Recommendations in the paper's own words: use SA, TA, or RRT, preferring RRT if time is short; use a linear acceptance parameter ending at zero. The authors expect the advice to be most useful for problems close to CVRP, CMST, or QAP, and note the ranking may change when the iteration budget is small.

## Search-behaviour regression

Multiple linear regression on run statistics (dependent variable: deviation of the average run from the overall best) ties good performance to: accepting the last move in an early iteration; finding the last improvement of the best solution in an early iteration; avoiding long reject streaks; keeping a long maximum distance between accepted solutions; and having high relative average objective values for rejected solutions. Key coefficients from Table 5, e.g. CMST: "Rel. Avg. Accept. Obj." **+0.002**, "Rel. Avg. Reject. Obj." **−0.002**; CVRP: "Rel. Avg. Accept. Obj." **+0.011**, "Rel. Avg. Reject. Obj." **−0.012**; QAP: "Num. Sol. Accept." **−0.007**.

The authors' forward-looking point: acceptance decisions could be improved by using the distance between current and candidate solution, not only objective value — a concept they note is unexplored in ALNS, with a close relative in skewed variable neighbourhood search.

## Related

- [[concepts/simulated-annealing-metropolis-cooling]] — the SA criterion is one of the top three; its temperature schedule is the tuned parameter.
- [[references/windrasmara2022-alns-multi-drop-fstsp]] — multi-drop FSTSP ALNS applying the Metropolis acceptance criterion in ALNS form.
- [[concepts/hyper-heuristics]] — ALNS is treated as a hyper-heuristic; acceptance criteria have been compared in that framework without definite conclusions.
- [[references/ropke2006-adaptive-large-neighborhood-search-pdptw]] — the original ALNS, whose default criterion was simulated annealing.
- [[references/shaabani2023-multiproduct-mirp-matheuristic]] — Phase 1 of that matheuristic is tuned by a Taguchi L27(3⁶) design, not by ranking acceptance criteria
- [[concepts/alns-destroy-repair-operator-suite]] — the operator side of the same ALNS; this page covers the acceptance side, where the tuned state (temperature/threshold) drives operator weights through the score-based scheme.
- [[concepts/duration-objective-depot-discretization]] — unrelated to this paper; the link was kept from an earlier pass and should be removed if the taxonomy check flags it.

## Sources

- [[_papers/santini2018comparison/santini2018comparison-extracted.md]] — Santini, Ropke & Hvattum, "A comparison of acceptance criteria for the adaptive large neighbourhood search metaheuristic", *Journal of Heuristics*, accepted 2018-05-18, zotero-key UKFLYL2U.
- [[_papers/santini2018comparison/images/page_23_image_1.jpg]] — Fig. 2, "Graph based on the Wilcoxon test for problem CMST ... Bluer and thicker arcs mean that the difference in deviation is greater".
