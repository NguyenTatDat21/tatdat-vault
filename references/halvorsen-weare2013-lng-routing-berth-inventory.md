---
title: "Routing and Scheduling in a Liquefied Natural Gas Shipping Problem with Inventory and Berth Constraints"
category: references
tags: [paper, maritime, lng, inventory-routing, berth-constraints, decomposition, mixed-integer-programming]
relationships:
  - target: "[[concepts/maritime-inventory-routing-problem]]"
    type: implements
  - target: "[[concepts/annual-lng-delivery-program]]"
    type: related_to
  - target: "[[references/fagerholt2023-maritime-inventory-routing-survey]]"
    type: related_to
sources:
  - _papers/halvorsen-weare2013routing/halvorsen-weare2013routing-extracted.md
  - _papers/halvorsen-weare2013routing/halvorsen-weare2013routing.md
  - _papers/halvorsen-weare2013routing/images/page_4_chart_2.jpg
  - _papers/halvorsen-weare2013routing/images/page_5_image_3.jpg
  - _papers/halvorsen-weare2013routing/images/page_9_image_3.jpg
  - _papers/halvorsen-weare2013routing/images/page_10_image_3.jpg
  - _papers/halvorsen-weare2013routing/images/page_17_chart_2.jpg
  - _papers/halvorsen-weare2013routing/images/page_17_chart_4.jpg
summary: >-
  Decomposes annual LNG delivery planning into subproblem routing models and a feasibility
  scheduling MILP coupled only by berth and inventory constraints; heuristic routing scales to
  360-day horizons.
provenance:
  extracted: 0.94
  inferred: 0.06
  ambiguous: 0.00
base_confidence: 0.67
lifecycle: draft
lifecycle_changed: 2026-10-25
tier: supporting
created: 2026-10-25T10:50:35Z
updated: 2026-10-25T10:50:35Z
---

# Routing and Scheduling in a Liquefied Natural Gas Shipping Problem with Inventory and Berth Constraints

> [!tldr] Halvorsen-Weare & Fagerholt split an annual LNG delivery program into per-subproblem routing models and a feasibility scheduling MILP, coupled only by berth and inventory constraints, and show heuristic routing scales the approach to 360-day horizons the monolithic model cannot reach.

## Problem & Contribution

- The world's largest LNG producer plans its annual delivery program (ADP) with a fixed heterogeneous fleet, contract volume bounds, daily berth capacity at loading terminals, and inventory limits at production and regasification ports.
- Vessel activity chains are contract-tied, so the fleet separates into independent subproblems; spot cargoes are served by non-fleet vessels, so they affect only berth utilization and inventory, not profit (line 79).
- Each cargo is a full shipload whose volume depends on the vessel; deliveries have an inner time window (target dates, quadratic step penalty $C_{PEN}=t_{VIOL}^{2}\cdot\alpha$, eq. 33, lines 361-363) and a hard outer window (line 53).
- Contributions: a full MIP (objective 1, constraints 2-13), a decomposition exploiting that only berth and inventory constraints couple subproblems, a multi-start local-search routing heuristic, and a feasibility scheduling MILP tested on 12 real-life instances.

## Method

Objective (1), lines 140-143, routing cost plus inner-window penalties:

$$
\min \sum_{v,i,j} C_{vij}\,x_{vij} \;+\; \sum_{v,n,t} C_{PEN}\,y_{vnt}
$$

with $C_{PEN}=t_{VIOL}^{2}\cdot\alpha$ (eq. 33, lines 361-363). The full model enforces cargo coverage, origin/flow conservation, destination, sequencing, berth capacity $\sum x + z_t \le B$ (8), contract volume bounds (9), the inventory balance

$$
s_t = s_{t-1} + P_t - \textstyle\sum_v Q_v\,x_{vnt} - Q_s\,z_t \tag{10}
$$

with safety bounds $S_{MN}\le s_t\le S_{MX}$ (11).

![[_papers/halvorsen-weare2013routing/images/page_4_chart_2.jpg]]
"Fig. 1 Example of penalty cost function for inner time window violations"

![[_papers/halvorsen-weare2013routing/images/page_5_image_3.jpg]]
"Fig. 2 Illustration of the simple network structure"

![[_papers/halvorsen-weare2013routing/images/page_9_image_3.jpg]]
"Fig. 3 Example with four vessels, four cargoes, eight time periods"

Decomposition (Fig. 4): constraints (8), (10), (11) are the only constraints connecting subproblems; removing them yields a routing subproblem per contract-tied segment (eq. 16-24) that forbids inner-window violations, followed by a feasibility scheduling MILP (eq. 25-32) minimizing penalty costs, where an objective value of 0 certifies no inner-window violations (line 309).

![[_papers/halvorsen-weare2013routing/images/page_10_image_3.jpg]]
"Fig. 4 Decomposition scheme"

Heuristic routing: multi-start local search with biased-random insertion (RANDOM_P = 15, up to 100 starting solutions) and inter-route moves only — Reassign, 2-interchange, 3-interchange — because time windows fix intra-route sequence (lines 251-260).

## Results

12 instances = 3 real-life problems × horizons 30/90/180/360 days; all use inner window width 7 days and outer window 21 days (line 333). Total CPU seconds per pairing (Table 3, line 365):

| Instance (horizon) | Full model | Exact routing + FP | Heuristic routing + FP |
|---|---|---|---|
| 1 (30 d) | 0.1 | 0.0 | 1.2 |
| 2 (90 d) | 28.0 | 0.7 | 70.3 |
| 3 (180 d) | — | 200.7 | 161.8 |
| 4 (360 d) | — | — | 1450.5 |
| 5 (30 d) | 0.1 | 1.7 | 0.5 |
| 6 (90 d) | 251.5 | 0.7 | 13.3 |
| 7 (180 d) | — | 43.4 | >10,000 |
| 8 (360 d) | — | — | 483.7 |
| 9 (30 d) | 0.4 | 0.2 | 0.5 |
| 10 (90 d) | 349.9 | 1.4 | 3.3 |
| 11 (180 d) | — | >10,000 | 80.9 |
| 12 (360 d) | — | — | 158.0 |

- The full model found integer solutions within the 10,000 s cap only for instances 1, 2, 5, 6, 9, 10 (Table 3, line 365).
- Only the heuristic routing + feasibility pairing found integer solutions for instances 4, 8, 12 (line 365).
- Routing costs are equal across the three methods for most instances; instance 5's heuristic objective is 0.48% above the exact/full one (line 355).
- Feasibility pairing gaps at the cap: instance 7 heuristic up to 7.5%, instance 11 exact 63.6% (line 357), caused by artificial penalty costs.
- Inner-window violations: the full model produced none; instance 7 exact 10 cargoes/22 days vs heuristic 12/26, instance 11 exact 3/5 vs heuristic 4/7 (lines 359-361); the heuristic-vs-exact violation spread is accidental, with no cost incentive behind it (line 361).

![[_papers/halvorsen-weare2013routing/images/page_17_chart_2.jpg]]
"Fig. 5 Inventory levels of LNG for problem instance 5"

![[_papers/halvorsen-weare2013routing/images/page_17_chart_4.jpg]]
"Fig. 6 Berth capacity utilization for problem instance 9"

## Limitations

- The two phases exchange no information: a suboptimal routing can admit a better schedule, so routing must be regenerated when scheduling is infeasible.
- Plans are not robust to unforeseen events such as weather delays; robust planning is named as future work.
- Uniform window widths (7/21 days in all instances) are unrealistic in real planning; customers range from rigid to flexible and plans require replanning cycles (line 391).
- Regasification-side inventory detail and spot-cargo economics are excluded, so the model optimizes producer-side logistics only. ^[inferred]

## Related

- [[concepts/maritime-inventory-routing-problem]]
- [[concepts/annual-lng-delivery-program]]
- [[references/fagerholt2023-maritime-inventory-routing-survey]]

## Bibliographic Record

- Citation key: `halvorsen-weare2013routing`
- DOI: 10.1007/s10479-010-0794-y
- URL: https://doi.org/10.1007/s10479-010-0794-y
- Publication: journalArticle, Annals of Operations Research, 2013-03-01 (published online 21 October 2010)
- Authors: Elin E. Halvorsen-Weare, Kjetil Fagerholt
- Companion metadata: [[../_papers/halvorsen-weare2013routing/halvorsen-weare2013routing.md|halvorsen-weare2013routing metadata]]

## Sources

- [[_papers/halvorsen-weare2013routing/halvorsen-weare2013routing-extracted.md]]
- [[_papers/halvorsen-weare2013routing/halvorsen-weare2013routing.md]]
- [[_papers/halvorsen-weare2013routing/images/page_4_chart_2.jpg]]
- [[_papers/halvorsen-weare2013routing/images/page_5_image_3.jpg]]
- [[_papers/halvorsen-weare2013routing/images/page_9_image_3.jpg]]
- [[_papers/halvorsen-weare2013routing/images/page_10_image_3.jpg]]
- [[_papers/halvorsen-weare2013routing/images/page_17_chart_2.jpg]]
- [[_papers/halvorsen-weare2013routing/images/page_17_chart_4.jpg]]
