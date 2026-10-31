---
title: >-
  The set team orienteering problem (Nguyen, Martinelli, Pham & Hà, 2025)
category: references
tags: [paper, orienteering, team-orienteering, vehicle-routing, branch-and-price]
relationships:
  - target: "[[references/ropke2006-adaptive-large-neighborhood-search-pdptw]]"
    type: related_to
  - target: "[[concepts/set-team-orienteering-problem-with-time-windows]]"
    type: related_to
  - target: "[[concepts/set-orienteering-problem]]"
    type: extends
  - target: "[[references/archetti2018-set-orienteering-problem]]"
    type: extends
  - target: "[[references/archetti2023-branch-and-cut-sop]]"
    type: related_to
  - target: "[[references/lu2024-hybrid-evolutionary-algorithm-sop]]"
    type: related_to
  - target: "[[references/yu2024-sarl-stoptw]]"
    type: related_to
  - target: "[[concepts/large-neighborhood-search]]"
    type: related_to
  - target: "[[concepts/branch-and-price-column-generation]]"
    type: related_to
  - target: "[[concepts/simulated-annealing-metropolis-cooling]]"
    type: related_to
  - target: "[[references/pham2023-efficient-ga-quadratic-tsp]]"
    type: related_to
  - target: "[[concepts/variable-neighborhood-search]]"
    type: related_to
  - target: "[[references/murray2015flying]]"
    type: related_to
sources:
  - _papers/nguyen2025set/nguyen2025set-extracted.md
  - _papers/nguyen2025set/nguyen2025set.md
  - _papers/nguyen2025set/images/page_9_chart_3.jpg
  - _papers/nguyen2025set/images/page_9_chart_5.jpg
summary: >-
  STOP: vehicle-routing with clusters and cluster-level profits. Branch-and-price proves optimal for STOP up to 783 nodes/157 clusters; LNS 595/612 SOP best-known, 40 new, 61.9% SOP instances optimal.
provenance:
  extracted: 0.87
  inferred: 0.10
  ambiguous: 0.03
base_confidence: 0.67
tier: core
lifecycle: draft
lifecycle_changed: 2026-10-26T04:15:04Z
created: 2026-10-26T04:15:04Z
updated: 2026-10-30T17:41:00Z
---

# The set team orienteering problem (Nguyen, Martinelli, Pham & Hà, 2025)

> [!tldr] STOP: vehicle-routing with clusters and cluster-level profits. Branch-and-price proves optimal for STOP up to 783 nodes/157 clusters; LNS 595/612 SOP best-known, 40 new, 61.9% SOP instances optimal.

*European Journal of Operational Research, 2025. DOI: 10.1016/j.ejor.2024.09.021. Received 14 Sep 2023, accepted 10 Sep 2024, available online 18 Sep 2024.*

## Problem & motivation

The **set team orienteering problem (STOP)**: complete digraph $G=(V,A)$, $V=\{0\}\cup C$, $K$ disjoint clusters partitioning $V\setminus\{0\}$. A cluster $S_k$ yields profit $p_k$ iff at least one of its customers is visited; $m$ homogeneous vehicles, each route within budget $T_{max}$; symmetric costs satisfying the triangle inequality; each cluster served at most once; maximize total collected profit. It generalizes the [[concepts/set-orienteering-problem|set orienteering problem (SOP, $m=1$)]] and is the fundamental variant of [[concepts/set-team-orienteering-problem-with-time-windows|STOPTW]] (time-windowed, Gunawan et al. 2021). Applications: mass distribution across supply-chain clusters (visit one retailer per chain), group-buying delivery, e-commerce multi-address delivery (a customer's home/work/parents' home form one cluster).

Related families: SOP (Archetti et al. 2018, single vehicle, MILP + [[concepts/tabu-search|Tabu]] matheuristic; Pěnička et al. 2019 improved MILP + [[concepts/variable-neighborhood-search|VNS]]; Carrabs et al. 2021 BRKGA; Dontas et al. 2023 Adaptive Memory Matheuristic AMMH; Lu et al. 2024 Hybrid Evolutionary Algorithm HEA, state-of-the-art heuristic; Archetti et al. 2023/2024 branch-and-cut, exact up to 100 customers), CTOP (Yahiaoui et al. 2019, profit only when ALL customers of a cluster are served), COP (Angelelli et al. 2014), GVRP (Bektaş et al. 2011; Hà et al. 2014), VRPRDL (Reyes et al. 2017; B&P by Ozbaygin et al. 2017, BPC Tilk et al. 2021, LNS Dumez et al. 2021, hybrid GA Pham et al. 2022), STOPTW (Gunawan et al. 2021; Yu et al. 2024 SA-RL).

## MILP and master formulation

Variables: $y_k$ (cluster $k$ served), $x_{ij}$ (arc used), $s_i$ (arrival time):

$$\max \sum_{k \in K} p_k y_k$$

$$\sum_{i \in V} x_{ji} - \sum_{i \in V} x_{ji} = 0 \ \forall j \in V \ \text{(flow)}; \quad \sum_{i \notin S_k, j \in S_k} x_{ij} = y_k \ \forall k; \quad x_{ij} = 0 \ \forall i,j \in S_k$$

$$s_j \ge s_i + c_{ij}x_{ij} - T_{max}(1-x_{ij}), \quad s_i + c_{i0}x_{i0} \le T_{max}, \quad \sum_{i \in V} x_{i0} \le m$$

Master set-partitioning over feasible routes $\Omega$: $\max \sum_{r \in \Omega} p_r \lambda_r$ s.t. $\sum_r \lambda_r \le m$, $\sum_r a_{kr}\lambda_r \le 1\ \forall k$, $\lambda$ binary, where $p_r$ is the profit of clusters visited by $r$.

## Branch-and-price

**Pricing**: forward dynamic programming over labels $L(P)=\{\bar c(P), v(P), t(P), \Pi(P)\}$ — reduced cost, last node, route time, collected clusters; start $\{-\gamma, 0, 0, \emptyset\}$; extension adds $p_{H(i)}-\beta_{i}$, time $t+c_{vi}$ (feasible iff $t+c_{vi}+c_{i0} \le T_{max}$ and $H(i)\notin\Pi$); reduced cost of route $r$ is $\bar c_r = \sum_k (p_k-\beta_k)a_{kr} - \gamma$. Dominance rule: label 1 dominates 2 iff $\bar c_1 \ge \bar c_2 \wedge v_1=v_2 \wedge t_1 \le t_2 \wedge \Pi_1 \subseteq \Pi_2$. **Bucket DP**: $\kappa=\min$ arc cost, $\lceil (T_{max}+1)/\kappa \rceil$ buckets per customer, dominance tested only within a bucket. **ng-route relaxation** with memory sets $N_k$ from $\Delta_N=8$ closest clusters; heuristic pricing relaxes dominance to $\bar c_1 \ge \bar c_2 \wedge v_1=v_2$ within a bucket keeping one label per bucket, exact pricing run only when no positive-reduced-cost route is found. Stabilization $\sigma \in [0,1]$ starts at 0.9, decreases by 0.1 per mispricing. **Branching**: on $y_k$ ($\sum_{r \in \Omega_k}\lambda_r = 0$ or $1$) and arc $x_{ij}$; strong branching evaluates the 10 most fractional candidates, score $\max(z_L,z_R) + (1-\alpha)\min(z_L,z_R)$ with $\alpha = 3/4$; artificial variables + Two-Phase Simplex for infeasible reformulations; best-bound node selection. Preprocessing removes nodes with $c_{0i}+c_{i0} > T_{max}$, arcs with $c_{0i}+c_{ij}+c_{j0} > T_{max}$, clusters with no feasible customer, and cluster pairs with no compatible arcs.

## LNS

Solution = $m$ routes, each a permutation of clusters. Route feasibility by DP: $g_v=\min_{u \in S_i}(g_u+c_{uv})$, $h_u=\min_{v \in S_j}(h_v+c_{uv})$, route cost $\bar c_r=\min_{u \in S_i}(g_u+h_u)$; preliminary lower bounds cut 75% of feasibility computations. **5 removal operators** (random, worst-cost, worst-profit, worst profit-over-cost, related removal with $R(i,j)=\varphi_1\cdot\frac{\sum_{u\in S_i,v\in S_j}c_{uv}}{\bar c_{max}|S_i||S_j}+\varphi_2\cdot X(i,j)$, $X$ = position distance within a route), and **9 insertion heuristics** (predetermined-order: random / profit-based / proximity-based $\rho_i$; parallel: cheapest, dynamic profit-over-cost, regret-2, regret-3, dynamic profit regret-2, dynamic profit regret-3, complexity $O(K|V|^2)$). Acceptance = [[concepts/simulated-annealing-metropolis-cooling|simulated annealing]] $p_{(s',s)}=e^{(f_{s'}-f_s)/T}$, $T_0 = -\mu f_{s_0}/\ln(0.5)$, exponential cooling $T \leftarrow \alpha T$; removal count $r$ random in $[4, \max(4,\min(\eta K, 40))]$; stop after 100,000 iterations. Tuned by IRACE over 100,000 experiments. The removal/insertion menu, the roulette-wheel weights and the SA acceptance follow the [[references/ropke2006-adaptive-large-neighborhood-search-pdptw|Ropke–Pisinger ALNS]] template. ^[inferred]

Table 1. General parameters of LNS. ^[ambiguous]

| niter | η | max removal | μ | cooling α |
|---|---|---|---|---|
| 100000 | 0.3 | 40 | 0.11 | 0.99994 |

Table 2. Operators and parameters weights. ^(IRACE-calibrated; removal weights 0.19/0.13/0.38/0.20/0.09, insertion weights: random order 0.29, profit 0.36, proximity 0.12, parallel cheapest 0.07, dynamic profit-over-cost 0.02, regret-2 0.04, regret-3 0.04, dyn-profit regret-2 0.03, dyn-profit regret-3 0.05, parallel total ≤25%; relatedness φ1=0.24, φ2=0.76; priority rp 5/10/4/10.) All 15 operators appear in top-3 configurations; balanced weights win; predetermined-order ratios are lower than parallel insertion, dynamic profit-regret and dynamic profit-over-cost dominate among parallel insertions. ^[ambiguous]

## Instances & setup

SOP benchmark: Fischetti et al. 1997 GTSP Set1/Set2, profits $g_1$=1, $g_2$ ∈ 1–100, $T_{max}=\omega\cdot$ sol_GTSP, $\omega \in \{0.4, 0.6, 0.8\}$, 52–1084 nodes, 11–217 clusters. New STOP instances: 174 from Yu et al. 2024 STOPTW (time windows removed; GTSP via cheapest insertion; $T_{max}=0.6\lceil$ sol_GTSP$/m\rceil$), $m \in \{1,2,3,4\}$, clusters 20–100, nodes 100–300; plus $m=2,3$ over the SOP sets: 612 configurations each of $m=2,3$. LNS runs 10× per instance: 2010 STOP instances, 20,100 LNS runs. [[concepts/branch-and-price-column-generation|B&P]] 6 h (21,600 s) limit, warm-started with the LNS lower bound. C++; B&P on i7-8700K 3.7 GHz 64 GB, LNS on i7-7700HQ 2.8 GHz 32 GB (Passmark 2059; 23% poorer than AMMH, 10% better than HEA).

## SOP results

Table 4. Summary results for all configurations (set, $g_i$, $\omega$) — B&P vs literature on the 612 SOP instances. Gap % vs best-known, time s: ^[ambiguous]

| Set | g | ω | Root gap | Root time | B&P gap | B&P time | #Sol | #Opt | #LSol | #LOpt |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | g1 | 0.4 | 0.97 | 4088.5 | 0.21 | 5256.6 | 45 | 39 | 27 | 27 |
| 1 | g1 | 0.6 | 0.49 | 6546.5 | 0.03 | 7112.8 | 37 | 36 | 15 | 14 |
| 1 | g1 | 0.8 | 0.68 | 8311.2 | 0.03 | 9051.9 | 33 | 32 | 15 | 13 |
| 1 | g2 | 0.4 | 0.86 | 4377.6 | 0.14 | 5617.3 | 43 | 39 | 27 | 27 |
| 1 | g2 | 0.6 | 0.65 | 6535.1 | 0.04 | 7740.1 | 37 | 35 | 15 | 14 |
| 1 | g2 | 0.8 | 0.80 | 8430.7 | 0.07 | 9776.7 | 33 | 31 | 15 | 10 |
| 2 | g1 | 0.4 | 5.30 | 4140.4 | 2.67 | 12700.9 | 44 | 23 | 27 | 21 |
| 2 | g1 | 0.6 | 1.60 | 4295.5 | 0.99 | 13805.0 | 43 | 19 | 15 | 11 |
| 2 | g1 | 0.8 | 0.01 | 3978.8 | 0.01 | 4401.0 | 45 | 44 | 15 | 12 |
| 2 | g2 | 0.4 | 5.65 | 4001.5 | 2.86 | 13761.1 | 44 | 20 | 27 | 20 |
| 2 | g2 | 0.6 | 1.63 | 4311.0 | 0.98 | 14411.4 | 43 | 18 | 15 | 8 |
| 2 | g2 | 0.8 | 0.01 | 4024.4 | 0.01 | 4446.8 | 44 | 43 | 15 | 9 |
| Total/Avg | | | 1.55 | 5253.4 | 0.67 | 9006.8 | 491 | 379 | 228 | 186 |

B&P gives valid bounds on 80.2% of 612 instances (491) and proves optimality on 61.9% (379), versus 8.5%/8.5% (Archetti 2018) and 37.3%/30.4% (Archetti 2024).

Table 5. Summarised comparison results of different metaheuristics on the SOP instances (gap $\bar G$ %, stability $\bar A$ %, best #B, improved #I, optimal #O): ^[ambiguous]

| Method | $\bar G$ | $\bar A$ | #B | #I | #O |
|---|---|---|---|---|---|
| VNS (20 runs) | 0.61 | 1.26 | 456 | — | — |
| BRKGA (10 runs) | 0.49 | 0.96 | 437 | — | — |
| AMMH (5 runs, C#) | 0.02 | — | 544 | — | — |
| LNS (10 runs) | −0.02 | 0.03 | 595 | 40 | 378 |

LNS finds 595/612 best-known solutions (456 VNS, 437 BRKGA, 544 AMMH) including 40 new best-known; reaches 378 of the 379 B&P optima, missing only instance 40d198_s2_40_g2; $\bar A$ ranges −0.03%..0.13% (VNS up to 2.18%, BRKGA 1.61%); LNS's $\bar G$ is better in 8 groups, equal in 2, worse in 2 vs AMMH.

Table 6. LNS vs HEA on the 144 large Set1 instances (≥200 nodes): LNS finds 137 best-known vs HEA 122; better in 17, worse in 7, equal in 120; every group favors LNS; LNS average solution 0.09% above best-known vs HEA 0.21%. ^[ambiguous]

![[_papers/nguyen2025set/images/page_9_chart_3.jpg]]

Fig. 1. Average running time per SOP instance of each method.

![[_papers/nguyen2025set/images/page_9_chart_5.jpg]]

Fig. 2. Growth of running time (logarithmic scale) comparison on SOP instances.

LNS averages 27.94 s per instance — the fastest in every size group; on instances with >1000 nodes it is 67% faster than BRKGA (second fastest).

Table 3. The contribution of each operator, over 20,100 runs on 2010 STOP instances (improve count, ratio %, best count, ratio per 10,000 runs): ^[ambiguous]

| Operator | Improve | Ratio % | Best | Ratio ‱ |
|---|---|---|---|---|
| Profit-based insertion | 50,095,226 | 8.71 | 52,513 | 0.91 |
| Worst profit removal | 49,808,555 | 8.76 | 52,898 | 0.93 |
| Worst profit-over-cost removal | 26,219,243 | 8.76 | 31,898 | 1.07 |
| Random order insertion | 22,402,493 | 4.84 | 19,835 | 0.43 |
| Random removal | 16,597,872 | 5.84 | 19,361 | 0.68 |
| Worst cost removal | 14,136,550 | 7.27 | 17,712 | 0.91 |
| Proximity-based insertion | 12,907,758 | 6.73 | 12,328 | 0.64 |
| Cheapest insertion | 11,523,898 | 10.30 | 21,363 | 1.91 |
| Related removal | 6,139,331 | 4.56 | 7,034 | 0.52 |
| Dynamic profit-over-cost | 4,125,585 | 12.93 | 5,985 | 1.88 |
| Regret-2 insertion | 3,743,791 | 9.36 | 5,735 | 1.43 |
| Dynamic profit regret-2 | 3,721,024 | 12.42 | 5,190 | 1.73 |
| Dynamic profit regret-3 | 2,806,736 | 13.41 | 3,753 | 1.79 |
| Regret-3 insertion | 1,575,040 | 9.41 | 2,201 | 1.31 |

## STOP results

Table 7. Summary results for all configurations (set, $g_i$, $\omega$) of STOP instances — B&P, gaps %, time s: ^[ambiguous]

| m | Set | g | ω | Root gap | Root time | B&P gap | B&P time | #Val | #Opt |
|---|---|---|---|---|---|---|---|---|---|
| 2 | 1 | g1 | 0.4 | 0.21 | 1527.1 | 0.00 | 1643.3 | 48 | 48 |
| 2 | 1 | g1 | 0.6 | 0.45 | 3108.3 | 0.11 | 4790.4 | 46 | 42 |
| 2 | 1 | g1 | 0.8 | 1.00 | 4880.4 | 0.15 | 6362.3 | 41 | 37 |
| 2 | 1 | g2 | 0.4 | 0.18 | 1452.2 | 0.00 | 1967.4 | 48 | 47 |
| 2 | 1 | g2 | 0.6 | 0.47 | 3209.3 | 0.14 | 5181.6 | 46 | 39 |
| 2 | 1 | g2 | 0.8 | 0.95 | 4802.1 | 0.14 | 6976.3 | 41 | 35 |
| 2 | 2 | g1 | 0.4 | 2.61 | 1442.8 | 0.62 | 6142.8 | 48 | 37 |
| 2 | 2 | g1 | 0.6 | 2.10 | 3086.6 | 0.59 | 9605.7 | 45 | 31 |
| 2 | 2 | g1 | 0.8 | 0.94 | 2163.9 | 0.52 | 9623.1 | 48 | 29 |
| 2 | 2 | g2 | 0.4 | 2.47 | 1441.6 | 0.60 | 6101.2 | 48 | 38 |
| 2 | 2 | g2 | 0.6 | 1.99 | 3019.7 | 0.51 | 10755.6 | 45 | 29 |
| 2 | 2 | g2 | 0.8 | 0.87 | 2186.6 | 0.48 | 9231.3 | 48 | 30 |
| 2 | Total | | | 1.19 | 2693.4 | 0.32 | 6531.7 | 552 | 442 |
| 3 | 1 | g1 | 0.4 | 0.13 | 595.2 | 0.02 | 1274.8 | 50 | 48 |
| 3 | 1 | g1 | 0.6 | 0.24 | 1551.9 | 0.02 | 2332.5 | 48 | 47 |
| 3 | 1 | g1 | 0.8 | 0.34 | 2374.0 | 0.05 | 3904.9 | 47 | 43 |
| 3 | 1 | g2 | 0.4 | 0.13 | 598.0 | 0.02 | 1275.6 | 50 | 48 |
| 3 | 1 | g2 | 0.6 | 0.18 | 1531.9 | 0.01 | 2574.5 | 48 | 47 |
| 3 | 1 | g2 | 0.8 | 0.31 | 2261.6 | 0.10 | 4469.4 | 48 | 42 |
| 3 | 2 | g1 | 0.4 | 0.86 | 795.5 | 0.29 | 3523.6 | 50 | 44 |
| 3 | 2 | g1 | 0.6 | 1.55 | 1453.5 | 0.39 | 5761.0 | 48 | 39 |
| 3 | 2 | g1 | 0.8 | 0.78 | 2021.4 | 0.26 | 5586.6 | 48 | 38 |
| 3 | 2 | g2 | 0.4 | 0.81 | 862.5 | 0.30 | 3576.7 | 50 | 43 |
| 3 | 2 | g2 | 0.6 | 1.35 | 1443.2 | 0.34 | 5590.2 | 48 | 38 |
| 3 | 2 | g2 | 0.8 | 0.63 | 2001.7 | 0.23 | 5929.1 | 48 | 38 |
| 3 | Total | | | 0.61 | 1457.5 | 0.17 | 3816.6 | 583 | 515 |

More vehicles make instances easier (smaller gaps, times, more solved) because $T_{max}$ shrinks, shortening routes and easing the pricing DP.

Table 8. Performance of LNS on the STOP instances (gap vs B&P upper bound, time s, #Opt over 51 per group): ^[ambiguous]

| Set | g | ω | m=2 Gap | m=2 GapUB | m=2 Time | m=2 #Opt | m=3 Gap | m=3 GapUB | m=3 Time | m=3 #Opt |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | g1 | 0.4 | 0.01 | 0.00 | 7.47 | 48 | 0.00 | 0.02 | 3.54 | 48 |
| 1 | g1 | 0.6 | 0.03 | 0.11 | 15.23 | 42 | 0.00 | 0.02 | 7.64 | 47 |
| 1 | g1 | 0.8 | 0.04 | 0.14 | 22.25 | 37 | 0.02 | 0.05 | 12.48 | 43 |
| 1 | g2 | 0.4 | 0.01 | 0.00 | 7.28 | 47 | 0.00 | 0.02 | 3.26 | 48 |
| 1 | g2 | 0.6 | 0.05 | 0.14 | 15.46 | 39 | 0.00 | 0.01 | 8.03 | 47 |
| 1 | g2 | 0.8 | 0.04 | 0.14 | 24.43 | 35 | 0.01 | 0.10 | 12.13 | 42 |
| 2 | g1 | 0.4 | 0.05 | 0.61 | 16.19 | 37 | 0.03 | 0.29 | 7.25 | 44 |
| 2 | g1 | 0.6 | 0.06 | 0.58 | 27.13 | 31 | 0.01 | 0.38 | 13.18 | 39 |
| 2 | g1 | 0.8 | 0.01 | 0.51 | 12.66 | 29 | 0.01 | 0.25 | 14.95 | 38 |
| 2 | g2 | 0.4 | 0.04 | 0.59 | 14.14 | 38 | 0.01 | 0.29 | 6.94 | 43 |
| 2 | g2 | 0.6 | 0.05 | 0.50 | 26.29 | 29 | 0.01 | 0.33 | 12.80 | 38 |
| 2 | g2 | 0.8 | 0.02 | 0.47 | 13.09 | 30 | 0.03 | 0.23 | 16.10 | 38 |
| Total | | | 0.04 | 0.32 | 16.80 | 442 | 0.01 | 0.17 | 9.86 | 515 |

[[concepts/large-neighborhood-search|LNS]] reaches optimality in all 957 instances where B&P certifies it (442 for $m=2$, 515 for $m=3$); run-to-run objective variation never exceeds 0.93% ($m=2$) and 1.15% ($m=3$); LNS time falls from 27.94 s (1 vehicle) to 16.80 (2) and 9.86 s (3).

174 new STOP instances (Yu et al. 2024, $m\in\{1,2,3,4\}$, |C| ∈ {100,200,300}): Table 9 — B&P finds valid bounds for all 174 and proves 112 optima; LNS matches all 112. ^[ambiguous] Group $m=1, |C|=200$ is hardest: B&P optimal for 3/29, ~20,000 s; $|C|=100$ solved optimally within 25 s average; remaining groups 20/29 in ~2 h. LNS max average gap 0.23%, max time 11.69 s.

Table 10. LNS vs VNS on the 29 $m=1, |C|=200$ instances ( Solomon c1xx/c2xx; VNS source code from ctu-mrs, iterations raised 2000→5000 to match LNS time). Representative rows (Best / Avg / Time): ^[ambiguous]

| Instance | VNS Best | VNS Avg | VNS Time | LNS Best | LNS Avg | LNS Time | Gap_best % | Gap_avg % |
|---|---|---|---|---|---|---|---|---|
| c101 | 1480 | 1450.0 | 17.06 | 1540 | 1533.0 | 16.20 | −4.05 | −3.58 |
| c102 | 1450 | 1418.0 | 17.26 | 1470 | 1468.0 | 15.17 | −1.38 | −1.24 |
| c103 | 1460 | 1439.0 | 18.33 | 1480 | 1470.0 | 15.47 | −1.37 | −0.68 |
| c104 | 1470 | 1430.0 | 15.18 | 1480 | 1473.0 | 15.43 | −0.68 | −0.20 |
| c105 | 1380 | 1347.0 | 17.22 | 1430 | 1423.0 | 15.68 | −3.62 | −3.12 |

Gap_best ≤ 0 on every instance: LNS beats VNS on 22, ties on 7; mean Gap_avg −1.87%, max 0.23%.

## Conclusions & scope

STOP generalizes several routing-with-profits problems and is the fundamental STOPTW variant. The B&P algorithm closes the gap on STOP instances up to 783 nodes/157 clusters; LNS hits optimal for all of them; on SOP, 61.9% of 612 instances are solved to optimality (first such figure; 30.4% prior best), dual bounds provided for the first time, 40 new best-known solutions out of 612 considered. LNS regret/dynamic-profit-regret insertions were disabled for SOP (single vehicle). New benchmark set with up to 1084 customers and 217 clusters is available for future work.

## Related

- [[concepts/set-team-orienteering-problem-with-time-windows]] — STOP is its fundamental variant.
- [[concepts/set-orienteering-problem]] — SOP, the single-vehicle special case.
- [[references/archetti2018-set-orienteering-problem]] — first SOP definition.
- [[references/archetti2023-branch-and-cut-sop]] — state-of-the-art SOP exact.
- [[references/lu2024-hybrid-evolutionary-algorithm-sop]] — HEA, SOP heuristic benchmark.
- [[references/yu2024-sarl-stoptw]] — SA-RL on STOPTW, source of the new STOP instances.
- [[references/pham2023-efficient-ga-quadratic-tsp]] — co-author Pham; VRPRDL hybrid GA cited.
- [[references/ropke2006-adaptive-large-neighborhood-search-pdptw]] — the ALNS template this page's operator set is calibrated on.

## Sources

- [[_papers/nguyen2025set/nguyen2025set-extracted]]
- [[_papers/nguyen2025set/nguyen2025set]]
- [[_papers/nguyen2025set/images/page_9_chart_3.jpg]]
- [[_papers/nguyen2025set/images/page_9_chart_5.jpg]]