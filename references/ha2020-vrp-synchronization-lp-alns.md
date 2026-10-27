---
title: >-
  A New CP Model and LP-based ALNS for VRP with Synchronization Constraints
category: references
tags: [paper, vrp, synchronization, constraint-programming, alns, linear-programming, time-windows]
relationships:
  - target: "[[references/ropke2006-adaptive-large-neighborhood-search-pdptw]]"
    type: uses
  - target: "[[concepts/vehicle-routing-with-synchronization-constraints]]"
    type: uses
  - target: "[[concepts/large-neighborhood-search]]"
    type: uses
  - target: "[[concepts/adaptive-large-neighborhood-search-for-mip]]"
    type: related_to
  - target: "[[references/hojabri2018-vrp-synchronization-alns-cp]]"
    type: derived_from
  - target: "[[references/paradiso2020-esf-multitrip-vrptw]]"
    type: related_to
sources:
  - _papers/ha2020new/ha2020new-extracted.md
  - _papers/ha2020new/ha2020new.md
  - _papers/ha2020new/images/page_6_image_2.jpg
  - _papers/ha2020new/images/page_6_image_4.jpg
  - _papers/ha2020new/images/page_9_chart_7.jpg
summary: >-
  First MIP and CP model for VRP-SC; lp-ALNS uses LP insertion feasibility, beats cp-ALNS on all classes, finds 620 new best-known solutions, improves four VRPTWSyn bests.
provenance:
  extracted: 0.88
  inferred: 0.10
  ambiguous: 0.02
base_confidence: 0.67
lifecycle: draft
lifecycle_changed: 2026-10-25T19:48:00Z
tier: core
created: 2026-10-25T19:48:00Z
updated: 2026-10-26T12:26:00Z
---

# A New CP Model and LP-based ALNS for VRP with Synchronization Constraints

> [!tldr] Hà, Nguyen, Nguyen, Pham, Do & Rousseau (2020, *Comput. Oper. Res.*, DOI 10.1016/j.cor.2020.105085) give the **first MIP** and a new **CP model** for VRP with synchronization constraints, plus **lp-ALNS** — an ALNS whose insertion feasibility checks are linear programs — dominating all prior heuristics and improving four VRPTWSyn best-known solutions.

## Problem & Novelty

VRPSC: regular vehicles $K_r$ (capacity $Q$) visit regular customers, special vehicles $K_s$ visit special customers $V_s$; every special customer also needs a regular-service visit by its mirror vertex $m_i$; start times must synchronize:

$$
y_{m_i}-\alpha_i \le y_i \le y_{m_i}+\beta_i
$$

with time windows $[o_i,u_i]$ on regular vertices (service start), service times $h_i^l$, travel times/costs $t_{ij}^l,c_{ij}^l$. Motivated by a real ISP deployment in Vietnam where a delay of at most 15 minutes is allowed. First exact models for VRPSC (prior work: Hojabri & Rousseau 2018 ALNS+CP only). ^[inferred]

![[_papers/ha2020new/images/page_6_image_2.jpg]]
*Fig. 1. Computing waiting times due to time window and synchronization constraints.* (Waiting time due to time window = 30; waiting time due to synchronization constraint = 45 — labels quoted from the figure, shown with its companion image page_6_image_4.jpg.)

![[_papers/ha2020new/images/page_6_image_4.jpg]]
*Fig. 1. Computing waiting times due to time window and synchronization constraints.*

## Method / Pipeline

1. **MIP**: coverage, depot start/end, flow, capacity constraints (2)–(6); sequencing $y_i+(h_i+t_{ij})x_{ij}-M(1-x_{ij})\le y_j$ with $M=u_{v_0^e}$ (7); time windows (8); sync (9)–(10).
2. **CP model** in IBM ILOG CP Optimizer: one interval $Itv_i^l$ per vertex/vehicle, optional alternatives $ItvAlt_{ik}^l$ for mirror pairs, sequences per vehicle, `noOverlap` with travel-time transition matrix $T_l$, `startOf` for time windows and sync, `presenceOf` for capacity, `typeOfNext` for arc costs; objective $\min\sum_k Cost_k^l$ (22).
3. **lp-ALNS**: removal operators random / related / worst, relatedness — the operator menu and SA acceptance follow [[references/ropke2006-adaptive-large-neighborhood-search-pdptw|Ropke & Pisinger 2006]]. ^[inferred]

$$
R_{ij}=\lambda_1\frac{|\tau_i-\tau_j|}{\max Time}+\lambda_2\frac{d_{ij}}{\max Dis}+\lambda_3\frac{|q_i-q_j|}{\max Dem}+\lambda_4|type_i-type_j|,\quad \lambda=(4,2,1,4)
$$

with cheapest insertion (23) $IC_j^r=c_{ij}+c_{j(i+1)}-c_{i(i+1)}$, regret-$k$ ranking, and **LP-based feasibility**: model (F1) maximizes the delay $\delta_a$ on arc $a$ under time-window, sync, and route-arc constraints; an insertion is accepted iff $t_{(j-1)i}+t_{ij}-t_{(j-1)j}+waitTime_i+h_i^r\le\delta_a$ (33) and $arrivalTime_i\le u_i$ (34). Model (F2) is a single LP maximizing $\sum_a\varpi_a\delta_a$ (objective coefficients flipped to probe each arc); saved earliest/latest arrival values give $O(1)$ sync-violation checks $lb_i-ub_{m_i}>\beta_i$ or $ub_i-lb_{m_i}<-\alpha_i$ (38)–(41), with a final LP (F3) check when all $O(1)$ checks pass.

## Key Equations

The sync constraint pair (9)–(10) and the LP feasibility arc-delay model (F1):

$$
\max\ \delta_a \quad \text{s.t. time windows (27), sync (28), route-arc inequalities (29)--(30)}
$$

Cheapest insertion cost (23) with the special-customer averaged-cost rule (24) keeping special insertions competitive, and regret-$k$ $RV_i=\sum_{j=1}^{k}\big(f_{i,r_{ij}}-f_{i,r_{i1}}\big)$ (25), $k\in\{2,3\}$.

## Setup & Headline Results

Instances from Hojabri 2018: $|V|\in\{25,50,100,200\}$, Solomon + Homberger-Gehring R/C/RC classes 1/2, special customers {5%, 25%, 50%}, $\alpha=0$, $\beta=10$; solvers IBM OPL 12.8.0, C++ + CPLEX 12.8.0, 2.10 GHz Intel E5-2683; ALNS 25,000 iterations, simulated-annealing acceptance, Pisinger–Ropke 2007 settings unchanged, $nb_{rm}\in[4,\min(40,0.4|V|)]$.

| Comparison | Outcome |
|---|---|
| CP model vs cp-ALNS (25 customers, 5 min) | CP better on 56 of 60 classes; best on class-1 (short routes), never proves optimality in 3 h |
| lp-ALNS vs cp-ALNS | 128 better / 7 worse at 25 customers; dominates all classes; avg improvement −4.59% (R1 25-cust sync 7), −7.91% (50-cust R1 50), −11.05% (200 R2 sync 10), −14.99% (200 R2 sync 50), −16.75% (200 R1 sync 100) |
| lp-ALNS vs MIP | 67 better, 93 equal, 8 worse; gaps never positive; MIP solved 63/168 small instances optimally (avg 3,585–9,314 s, gaps 3.24–35.09%) |
| New best-known solutions | 620 of 681 instances |
| VRPTWSyn (Bredström–Rönnqvist home-care, 20/50/80 customers, ~10% synced) | avg gaps +41.07 vs BR08, +0.07 vs ADM16, +0.09 vs PD18, −0.13 vs LTX19, −0.01 vs BKS; 4 new best-known (6A, 8A, 9A, 10A); ~10 h per 80-customer instance |
| Speedups | O(1) checks: 20× on 50-cust/25-sync; F2 model saves ≥30% runtime (model construction is the bottleneck) |

![[_papers/ha2020new/images/page_9_chart_7.jpg]]
*Fig. 3. Number of new best-known solutions found by lp-ALNS.*

## Ablations & Limitations

- MIP closes only 63/168 small instances in the time limit — exact solving remains impractical beyond 25 customers.
- CP wins on 25-customer instances because 25,000 iterations are excessive there; on larger classes the ALNS repair is what wins. ^[inferred]
- LP-based insertion replaces the CP-based reinsertion of Hojabri & Rousseau: the paper attributes most of the quality jump to LP feasibility precision at arc-delay level. ^[inferred]
- C101/C105/C106 (25 customers, 2 sync) removed from experiments because published results were inexact. ^[extracted]

## Bibliographic Record

- Publication: *Computers & Operations Research*, Vol. 124, article 105085, December 2020
- Authors: Minh Hoàng Hà; Tat Dat Nguyen; Thinh Nguyen Duy; Hoang Giang Pham; Thuy Do; Louis-Martin Rousseau
- DOI: 10.1016/j.cor.2020.105085
- Companion metadata note: [[_papers/ha2020new/ha2020new.md]]

## Related

- [[concepts/vehicle-routing-with-synchronization-constraints]]
- [[concepts/large-neighborhood-search]]
- [[concepts/adaptive-large-neighborhood-search-for-mip]]
- [[references/hojabri2018-vrp-synchronization-alns-cp]] — the cp-ALNS baseline this paper builds on and outperforms
- [[references/paradiso2020-esf-multitrip-vrptw]]
- [[references/ropke2006-adaptive-large-neighborhood-search-pdptw]] — the ALNS scheme whose operator menu and acceptance settings this paper adopts.

## Sources

- [[_papers/ha2020new/ha2020new-extracted.md]]
- [[_papers/ha2020new/ha2020new.md]]
- [[_papers/ha2020new/images/page_6_image_2.jpg]]
- [[_papers/ha2020new/images/page_6_image_4.jpg]]
- [[_papers/ha2020new/images/page_9_chart_7.jpg]]