---
title: >-
  Drone Routing Problem with Swarm Synchronization (Li, Wang & Zhan, 2024)
category: references
tags: [paper, drone-routing, vrptw, swarm-synchronization, milp, alns, split-delivery, multi-trip, detour-insertion, time-windows, rotary-wing-drone, vehicle-routing, optimization, ejor]
relationships:
  - target: "[[references/ropke2006-adaptive-large-neighborhood-search-pdptw]]"
    type: related_to
  - target: "[[concepts/drone-swarm-synchronization]]"
    type: related_to
  - target: "[[concepts/large-neighborhood-search]]"
    type: related_to
  - target: "[[concepts/vehicle-routing-with-synchronization-constraints]]"
    type: related_to
  - target: "[[concepts/simulated-annealing-metropolis-cooling]]"
    type: related_to
  - target: "[[references/ha2020-vrp-synchronization-lp-alns]]"
    type: related_to
  - target: "[[concepts/exact-multitrip-vrptw-framework]]"
    type: related_to
  - target: "[[concepts/nonlinear-drone-energy-function-in-routing]]"
    type: related_to
  - target: "[[concepts/adaptive-large-neighborhood-search-for-mip]]"
    type: related_to
  - target: "[[references/wang2019routing]]"
    type: related_to
sources:
  - _papers/li2024drone/li2024drone-extracted.md
  - _papers/li2024drone/li2024drone.md
  - _papers/li2024drone/images/page_3_image_8.jpg
  - _papers/li2024drone/images/page_5_image_31.jpg
  - _papers/li2024drone/images/page_11_chart_7.jpg
  - _papers/li2024drone/images/page_15_chart_2.jpg
  - _papers/li2024drone/images/page_15_chart_4.jpg
  - _papers/li2024drone/images/page_15_chart_6.jpg
summary: >-
  DRP-SS: a VRPTW variant with drone swarms that couple and decouple at nodes, multi trips, split delivery; MILP plus ALNS with detour and multi-trip operators.
provenance:
  extracted: 0.85
  inferred: 0.12
  ambiguous: 0.03
base_confidence: 0.77
lifecycle: draft
lifecycle_changed: 2026-10-29
tier: core
created: 2026-10-26T00:51:06Z
updated: 2026-10-30T14:38:55Z
---

# Drone Routing Problem with Swarm Synchronization (Li, Wang & Zhan, 2024)

> [!tldr] The paper defines the Drone Routing Problem with Swarm Synchronization (DRP-SS): a VRPTW variant in which rotary-wing drones (RWDs) dynamically couple and decouple at network nodes, serve over-capacity customers as swarms with simultaneous arrival, run multiple trips, and allow split delivery; a MILP and an ALNS with detour and multi-trip operators quantify what swarms buy — lower variable cost at higher computational burden.

## Problem & Motivation

Published in European Journal of Operational Research (2024, DOI 10.1016/j.ejor.2023.10.015), the paper models a fleet of homogeneous rotary-wing drones operating from a single depot with time windows. Key rules:

- Each customer is visited by a single RWD at most once; demands larger than the drone capacity `Q` must be **split** across multiple RWDs.
- Customers whose full demand arrives from several drones require a **swarm**: the members serving that customer must arrive **simultaneously** (constraint 23).
- Swarms form and break **dynamically at nodes** (coupling/decoupling), not at the depot only; swarm members leave a shared node at equal times (constraints 24–26).
- A drone can fly to a customer **without delivering** (detour) purely to join a swarm; no time window is imposed at a detour node.
- Each RWD can perform multiple trips per departure; a preparation time `τ` is required between consecutive trips.

The paper's Table 1 literature comparison argues DRP-SS is the only surveyed variant that combines coupling/decoupling, split delivery, multi trips and time windows. Assumptions: 2D network, no third-dimension launch/retrieval modeling, waiting time ignored, energy consumed only on flying arcs and servicing.

![[_papers/li2024drone/images/page_3_image_8.jpg]]
*Fig. 1. Illustrative example of the DRP-SS. (LRL: less than RWD-load; RL: full RWD-load).* — depot 0 plus 10 customers, `Q = 1`, service 5 min, preparation 10 min, three RWDs; customers 1–4 exceed the capacity and need swarms; sync arcs include (0,1),(0,4) for u1,u2 and (0,2),(4,6),(6,0) for u1,u2,u3.

![[_papers/li2024drone/images/page_5_image_31.jpg]]
*Fig. 2. DRP-SS route examples.* — u1 one trip 0-2-1-7-3-0; u2 two trips 0-4-5-0 and 0-3-0; u3 one trip 0-4-6-0; the swarm u1+u2 is formed at customer 3 via u1's detour, the swarm u2+u3 is formed at the depot and decoupled at customer 4.

## Method / Architecture

**MILP formulation.** Decision variables `x_uij` (flying arc), `y_u` (RWD in use), `f_ui` (service), `r_uij` (parcel flow), `w_uij` (trip successor), `z` (swarm identification), arrival/departure times `t^a_ui`, `t^d_ui`. Constraints cover degree balance, demand split (`Σ_u p_ui = q_i`, `p_ui ≤ Q f_ui`), parcel flow conservation, flying-time budget `g_uij ≤ L^T x_uij` per departure, successive-trip linking with preparation time `t^d_ui + τ + (d_i0 + d_0j)/v − M(1 − w_uij) ≤ t^a_uj`, time continuity, time windows enforced only when a parcel is delivered, simultaneous swarm service, and at most `|U|` RWDs in one swarm. `M = max{|C|, l_0 + L^T}`.

**ALNS heuristic.** An initial-solution heuristic orders customers by ascending window end and enumerates feasible insertion positions. Customer-insertion operators: new-route insertion (NRI), customer-route insertion (CRI), new-trip insertion before/after a route (BTI/FTI), residual-demand insertion (MI), and detour insertion (DI, applied with probability α, applied to interacting swarm routes or to form a new swarm). Arrival times are adjusted route-wide after insertion; in extreme cases every route is touched. Destroy operators: random removal, worst removal, Shaw removal (similarity by arrival-time difference, distance, and drone-index differences inside swarms), longest-route removal, visits-in-long-routes removal. Removal count starts at 50% of customers and shrinks 5% every 2000 iterations down to a 5% floor. Repair operators: greedy (with two random-selection variants), regret-2, regret-3, and local-regret variants, with BTI/FTI/MI/DI applied after most repairs. Operator weights adapt by `P_m ← (1−β1)P_m + β1·π_m/ω_m`; acceptance is simulated annealing `e^{−(c(S)−c(S′))/T}`, `T ← β2·T`. Tuned parameters: α = 10%, σ1 = 5, σ2 = 1, σ3 = 0, β1 = 0.05, β2 = 0.99975, max 10 000 iterations, stop after 2000 non-improving iterations; α and β1 were the sensitive parameters in one-factor-at-a-time tuning. The weight rule, score constants σ1=5, σ2=1, σ3=0, cooling β2=0.99975 and SA acceptance are the [[references/ropke2006-adaptive-large-neighborhood-search-pdptw|Ropke–Pisinger ALNS]] scheme with renamed symbols. ^[inferred]

## Key Equations

Per-arc variable cost for one RWD inside a swarm of size `N_uij + 1`:

$$
c^{\text{swarm}}_{ij} = \left(b - a \cdot N_{uij}\right) \cdot c_{ij}
$$

with `b = 1` the solo per-distance cost and `a = 0.05` the swarm discount per co-member; a swarm flying an arc pays less per drone the more members it has. Full objective:

$$
\min \; \lambda \sum_{u \in U} y_u + \sum_{u \in U} \sum_{(i,j) \in V^2} \left( b \cdot x_{uij} - a \cdot \sum_{u_1 \in U} z_{uu1ij} \right) \cdot c_{ij}
$$

The set-partitioning reformulation used to attack exactness keeps the RWD dimension (group routes with swarms), which makes column generation impractical: the subproblem must be solved dozens to hundreds of times, and one label extension in a labeling scheme can generate up to `3 · (C_n^0 + C_n^1 + … + C_n^{⌊n/2⌋})` new labels.

## Results

- **Instance set**: 71 small-scale and 116 large-scale instances built from Solomon VRPTW benchmarks; `Q = 100`, `λ = 1000`, `a = 0.05`, `b = 1`, `v = 1`, Euclidean costs; C types use `L^T = 500`/`τ = 90`/`s_i = 90`, R/RC types `L^T = 200`/`τ = 10`/`s_i = 10`; large instances carry `L^T = 1000` (C) or 200 (R/RC), with P1/P2/P3 variants adding 10/20/30 customers of extra demand.
- **Small scale**: CPLEX proves optima for C-type up to 12 customers, R-type up to 6, RC up to 5, and runs out of time (14 400 s) on 26 instances; the ALNS solves all 71 small instances in under 5 s (average 0.89 s), reaches all 43 known optima, and reports Gap2 = 0.00% in 25 of the 28 cases where CPLEX had no proven optimum. It beats the CPLEX upper bound on C101-f-12 (3224.60 vs 3226.04) and C108-r-12 (2512.60 vs 3397.35).
- **VRPTW benchmark check** (objective = distance, DRP-SS operators removed): optimal for 24/29 instances of the -10X sets and 13/27 of -20X, average gap 0.11%, outperforming HGSADC and bALNS averages.
- **Large scale** (ALNS averages): objective 16,005.20 at 605.86 s (O), 20,751.57 at 1744.49 s (P1), 25,912.78 at 3143.51 s (P2), 29,983.42 at 6211.39 s (P3); more over-capacity customers mean more swarm arcs (N^F 11 → 39) and more RWDs per swarm arc (2.6 → 3.2).
- **Detour ablation (ALNS-E, no detour operator)**: Gap5 = 1.63%/2.32%/2.25%/2.55% for O/P1/P2/P3 on every instance — detours genuinely save cost.
- **Swarm ablation (ALNS-W, truck mode)**: 3.42–3.92% worse than ALNS, 1.11–1.77% worse than ALNS-E; swarms pay, and removing swarm synchronization removes most of the computational burden.
- **Multi-trip ablation (ALNS-T)**: gaps 19.88%–67.14%; multi-trip operators cut RWD utilization by 2–20, savings mostly from fixed cost `λ`.
- **Detour prevention (DRP-SS-L)**: adding `Σ_u Σ_j x_uij ≤ ⌈q_i/Q⌉` lets CPLEX close every C-type instance up to 12 customers in under 2600 s, average 122.61 s; permitting detours lowers variable cost in 25 instances at the price of longer times.

![[_papers/li2024drone/images/page_11_chart_7.jpg]]
*Fig. 11. Computational results of ALNS parameter tuning.*

![[_papers/li2024drone/images/page_15_chart_2.jpg]]
![[_papers/li2024drone/images/page_15_chart_4.jpg]]
![[_papers/li2024drone/images/page_15_chart_6.jpg]]
*Fig. 12. Boxplots (a) Instance characteristics and costs; (b) Instance characteristics and N^F; (c) Instance characteristics and computation time.* — C-type costs are lowest, RC highest; RC instances take the longest.

## Limitations

Swarm synchronization plus time continuity is the computational bottleneck: detours save cost but lengthen computation. The model ignores 3D flight dynamics, swarm speed and energy consumption; future work targets those plus continuous split delivery. Grant: NSFC 71972007. The large-scale instance list writes "CM4" where CMT4 is meant. `^[ambiguous]`

## Related

- [[concepts/drone-swarm-synchronization]] — the reusable mechanism this paper introduced
- [[concepts/large-neighborhood-search]] — ALNS shell, adaptive weights, SA acceptance
- [[concepts/vehicle-routing-with-synchronization-constraints]] — classical synchronization vs swarm synchronization
- [[references/ha2020-vrp-synchronization-lp-alns]] — VRPMS ALNS baseline in the paper's Table 1
- [[concepts/simulated-annealing-metropolis-cooling]] — acceptance inside the ALNS
- [[concepts/exact-multitrip-vrptw-framework]] — multi-trip VRPTW lineage
- [[references/ropke2006-adaptive-large-neighborhood-search-pdptw]] — source of the ALNS weight, score and cooling constants this page reuses.
- [[concepts/nonlinear-drone-energy-function-in-routing]] — shares drone-routing + optimization tags with this page
- [[references/wang2019routing]] — Wang et al. 2019 formalize HTDD triple platforms, treating internal capability as UAV payload and endurance and external capability as truck-launched access points. ^[extracted]

## Sources

- [[_papers/li2024drone/li2024drone-extracted.md]]
- [[_papers/li2024drone/li2024drone.md]]
- [[_papers/li2024drone/images/page_3_image_8.jpg]]
- [[_papers/li2024drone/images/page_5_image_31.jpg]]
- [[_papers/li2024drone/images/page_11_chart_7.jpg]]
- [[_papers/li2024drone/images/page_15_chart_2.jpg]]
- [[_papers/li2024drone/images/page_15_chart_4.jpg]]
- [[_papers/li2024drone/images/page_15_chart_6.jpg]]