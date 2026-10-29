---
title: >-
  The flying sidekick traveling salesman problem: Optimization of drone-assisted parcel delivery (Murray & Chu, 2015)
category: references
tags: [paper, fstsp, pdstsp, drone-routing, truck-drone-synchronization, milp, tsp, heuristic, pms, makespan, uav-endurance, uav-speed, last-mile-delivery, parcel-delivery, trc, optimization, drone-swarm-synchronization]
relationships:
  - target: "[[concepts/multiple-flying-sidekicks-traveling-salesman-problem]]"
    type: related_to
  - target: "[[concepts/parallel-drone-scheduling-traveling-salesman-problem]]"
    type: related_to
  - target: "[[concepts/vehicle-routing-with-synchronization-constraints]]"
    type: related_to
  - target: "[[concepts/drone-speed-selection-in-routing]]"
    type: related_to
  - target: "[[references/murray2020-multiple-flying-sidekicks-tsp]]"
    type: extends
  - target: "[[references/dorling2017-drone-delivery-vrp]]"
    type: related_to
  - target: "[[references/ha2020-vrp-synchronization-lp-alns]]"
    type: related_to
  - target: "[[references/dinh2021-haco-pdstsp]]"
    type: related_to
  - target: "[[references/dellamico2020-matheuristics-pdstsp]]"
    type: related_to
  - target: "[[references/cheng2020-drone-routing-energy-function]]"
    type: related_to
  - target: "[[references/torabbeigi2020-payload-bcr-drone-scheduling]]"
    type: related_to
  - target: "[[references/montemanni2023-cp-pdsvrp]]"
    type: related_to
  - target: "[[references/nguyen2022-min-cost-pdsvrp]]"
    type: related_to
sources:
  - _papers/murray2015flying/murray2015flying-extracted.md
  - _papers/murray2015flying/murray2015flying.md
  - _papers/murray2015flying/images/page_2_image_2.jpg
  - _papers/murray2015flying/images/page_2_image_4.jpg
  - _papers/murray2015flying/images/page_2_image_6.jpg
  - _papers/murray2015flying/images/page_2_image_8.jpg
  - _papers/murray2015flying/images/page_3_image_2.jpg
  - _papers/murray2015flying/images/page_3_image_4.jpg
  - _papers/murray2015flying/images/page_3_table_6.jpg
  - _papers/murray2015flying/images/page_9_image_3.jpg
  - _papers/murray2015flying/images/page_14_chart_2.jpg
  - _papers/murray2015flying/images/page_15_chart_8.jpg
  - _papers/murray2015flying/images/page_16_chart_8.jpg
  - _papers/murray2015flying/images/page_16_chart_10.jpg
  - _papers/murray2015flying/images/page_17_chart_2.jpg
  - _papers/murray2015flying/images/page_17_chart_4.jpg
  - _papers/murray2015flying/images/page_17_image_8.jpg
  - _papers/murray2015flying/images/page_17_image_10.jpg
  - _papers/murray2015flying/images/page_16_table_4.jpg
  - _papers/murray2015flying/images/page_18_image_2.jpg
  - _papers/murray2015flying/images/page_18_image_4.jpg
  - _papers/murray2015flying/images/page_18_image_6.jpg
  - _papers/murray2015flying/images/page_19_image_7.jpg
  - _papers/murray2015flying/images/page_19_image_9.jpg
  - _papers/murray2015flying/images/page_19_image_11.jpg
summary: >-
  FSTSP: truck+UAV tandem with 3-node sortie triples, 32-constraint MILP, route-and-re-assign heuristic; PDSTSP: depot-launched UAV fleet. Gaps 0.12–10.68% on 720 instances.
provenance:
  extracted: 0.88
  inferred: 0.09
  ambiguous: 0.03
base_confidence: 0.87
tier: core
lifecycle: draft
lifecycle_changed: 2026-10-29T17:15:00Z
created: 2026-10-26T04:15:04Z
updated: 2026-10-27T06:00:00Z
---

# The flying sidekick traveling salesman problem (Murray & Chu, 2015)

*Transportation Research Part C: Emerging Technologies, 2015. DOI: 10.1016/j.trc.2015.03.005.*

## Problem & motivation

Murray & Chu introduce two new [[concepts/vehicle-routing-with-synchronization-constraints|vehicle-routing problems]] motivated by drone-assisted last-mile parcel delivery (Amazon Prime Air announced 2013, range 10 miles, payload 5 lb — covering 86% of Amazon's deliveries; Deutsche Post DHL's Parcelcopter; Teal Group forecast cumulative worldwide UAV spending above $89 billion over the next decade; FAA limits: 400 ft ceiling, line-of-sight, GPS accuracy ~10 m).

**FSTSP**: one truck and one UAV depart a single depot exactly once and must both return. Each of $c$ customers is served exactly once, by truck or UAV. UAV-ineligible customers (parcel weight over UAV payload, signature required, no safe landing site) go to the truck. In tandem, the UAV rides the truck (conserving battery), is launched from a node, delivers to exactly one customer, and rendezvous back with the truck. Objective: minimize the time to serve all customers and return both vehicles to the depot, i.e. $\min t_{c+1}$.

![[_papers/murray2015flying/images/page_2_image_2.jpg]]

(a) The traditional approach, where a delivery truck visits all customers.

![[_papers/murray2015flying/images/page_2_image_4.jpg]]

(b) UAVs deliver to all eligible customers within the UAV's flight range; the delivery truck serves customers with large parcels or those outside of flight range.

![[_papers/murray2015flying/images/page_2_image_6.jpg]]

(c) Optimized assignment of customers to either a UAV or a traditional delivery truck.

![[_papers/murray2015flying/images/page_2_image_8.jpg]]

(d) A comparison of delivery schedules for the three systems depicted above.

Fig. 2. Customer deliveries are made by either a traditional delivery truck or via UAV. Customers 2 and 9 (circular nodes) are ineligible to be served via UAV (e.g., due to parcel weight restrictions).

**PDSTSP** (parallel drone scheduling TSP): depot near customers, one truck plus a fleet $V$ of identical UAVs that operate from the depot with no synchronization; each UAV round trip is launch at depot, one delivery, return within endurance. Objective: minimize the latest vehicle return time $z$ (a makespan).

![[_papers/murray2015flying/images/page_3_image_2.jpg]]

(a) An optimal truck delivery sequence, without the aid of a UAV.

![[_papers/murray2015flying/images/page_3_image_4.jpg]]

(b) The UAV is launched from a delivery truck, delivering parcels to two eligible customers.

![[_papers/murray2015flying/images/page_3_table_6.jpg]]

(c) A comparison of delivery schedules for the two scenarios depicted above.

Fig. 3. In cases where the distribution center (depot) is not conducive to direct UAV deliveries, a truck/UAV tandem may reduce delivery times. Customers 2 and 9, depicted by circular nodes above, are ineligible to be served via UAV.

Positioned in Drexl's (2012) taxonomy as vehicle "movement synchronization en route"; related to VRPTT (Drexl 2007), the truck-and-trailer routing problem (Chao 2002; Villegas et al. 2013 EJOR 230(2):231–244), and Lin (2011, Comp. Oper. Res. 38(11):1596–1609) pickup-delivery with vans and scooters, with FSTSP differing in that the UAV can separate and reconnect multiple times.

## FSTSP formulation

Notation: $C' \subseteq C$ = UAV-eligible customers; $N=\{0,\dots,c+1\}$, $N_0=\{0,\dots,c\}$, $N_+=\{1,\dots,c+1\}$; truck travel times $\tau_{ij}$, UAV times $\tau'_{ij}$, $\tau_{0,c+1}=0$; service times $s_L$ (launch: battery swap + parcel load) and $s_R$ (recovery). A UAV sortie is a 3-node tuple $\langle i,j,k\rangle \in P$: launch $i \in N_0$, delivery $j \in C'$, rendezvous $k \in N_+$ (a truck-serviced customer, or the ending depot $c+1$, which retires the UAV), with $t'_k - (t'_i - \tau'_{ij}) \le e$ (endurance). Decision variables: binary $x_{ij}$ (truck arc), $y_{ijk}$ (sortie), arrival times $t_j$, $t'_j$ ($t_0=t'_0=0$), truck visit order $p_{ij} \in \{0,1\}$, positions $1 \le u_i \le c+2$.

Assumptions (§3.1): one customer per sortie; truck may visit several customers while the UAV is airborne; the UAV cannot land mid-route to wait; launch from $i$ cannot return to the truck at $i$; rendezvous only at truck-serviced nodes; no customer revisits, no non-customer nodes.

Objective and core constraints (1)–(32), condensed:

$$\min t_{c+1}$$

$$\sum_{i \in N_0} x_{ij} + \sum_{i \in N_0} \sum_{k \in N_+} y_{ijk} = 1 \quad \forall j \in C$$

$$\sum_{j \in C} y_{0jk} \le 1,\ \sum_{i \in N_0} y_{ijk} \le 1 \quad (\text{UAV launch and rendezvous used at most once})$$

$$t'_k = t_k, \quad t'_i = t_i \quad (\text{synchronization at launch and rendezvous})$$

$$t'_k \ge t'_i + \tau'_{ij} + \tau'_{jk} + s_L + s_R - M(1 - y_{ijk})$$

$$t_k \ge t_i + \tau_{ij} + s_L + s_R - M(1 - y_{ijk}) \quad (\text{truck time includes service at } i, k)$$

$$t_k \ge t_i + \tau_{ij} x_{ij}, \quad u_i - u_j + (c+2) x_{ij} \le c+2 \quad (\text{truck flow, subtour elimination})$$

Worked example of constraint (18): truck reaches $k$ at 9, UAV at 11, $s_R = 1$ ⇒ $t_k = t'_k = 12$ (truck waits for UAV recovery). Big-M is set from a nearest-neighbor truck route upper bound. NP-hard: MILP solvers "may require several hours to solve … for seemingly simple 10-customer problems." ^[inferred]

## Route and re-assign heuristic (Algorithms 1–5)

Algorithm 1: solve the TSP over all customers (truck route, times $t$); loop over each $j \in C'$ computing savings, then cost of serving $j$ by truck re-insertion (`calcCostTruck`) or UAV (`calcCostUAV`); `performUpdate` implements the maximum-savings move; stop when no positive savings remain. ^[inferred]

- **Savings (Alg. 2)**: removing $j$ from between truck nodes $i,k$ saves $\tau_{i,j} + \tau_{j,k} - \tau_{i,k}$; if $j$ lies inside a UAV-paired subroute $[a..b]$, savings are capped by $t'_{[b]} - (t_{[a]} + \tau'_{a,j'} + \tau'_{j',b} + s_R)$ — the UAV must fly the replacement sortie within the existing round-trip window. ^[inferred]
- **Truck re-insertion (Alg. 3)**: insert $j$ between $i,k$; cost $= \tau_{i,j} + \tau_{j,k} - \tau_{i,k}$; net $=$ savings $-$ cost; feasibility $t_{[b]} - t_{[a]} + \mathrm{cost} \le e$.
- **UAV assignment (Alg. 4)**: for node pairs $i \prec k$ in a non-UAV subroute with $\tau'_{i,j} + \tau'_{j,k} \le e$: cost $= \max\{0,\ \max\{(t'_{[k]}-t_{[i]}) + s_L + s_R,\ \tau'_{i,j}+\tau'_{j,k}+s_L+s_R\} - (t'_{[k]}-t_{[i]})\}$ — i.e. the extra time the truck must spend waiting for the UAV.

Fig. 4 worked example (7 nodes, $C'=\{6,2,5,4\}$, route $\{0,3,6,2,5,1,4,7\}$): removing 5 splits the route into subroutes $\{0,3,6,2\}$, $\{2,1,4,7\}$; assigning 4 to the UAV leaves three subroutes and $C'=\{6\}$.

![[_papers/murray2015flying/images/page_9_image_3.jpg]]

(b) UAV-eligible customer 5 has been removed from the truck's route and is assigned to the UAV. The UAV is launched from the depot (node 0) and is recovered by the truck at node 2. There are now two truck subroutes, {0, 3, 6, 2} and {2, 1, 4, 7}; Cprime = {6, 4}.

(c) Customer 4 is assigned to the UAV. There are now three truck subroutes, and Cprime = {6}.

Fig. 4. A notional example to demonstrate the FSTSP heuristic. Nodes 0 and 7 represent the depot. Customers in C<sup>0</sup>(UAV-eligible) are shown in boxed nodes, while the remaining circular nodes represent UAV-ineligible customers. ^[ambiguous] — the extractor rendered Fig. 4a as garbled ASCII ("①→③→⑥→2→→①→4→⑦"), so only subfigure (b)'s image survives.

## PDSTSP formulation & heuristic

Structure: the truck route is a TSP over the truck-served subset; assigning depot-range customers $C'' \subseteq C'$ ($\tau'_{0,i} + \tau'_{i,c+1} \le e$) to $V$ UAVs is parallel identical machine scheduling (PMS) minimizing makespan, jobs = customers with processing time = UAV round-trip flight time. The partition choice couples two NP-hard subproblems; PMS literature: Min & Cheng (1999) GA, Xu & Nagi (2013) exact column generation. Heuristic (Algorithms 6–7): start with all $C''$ on UAVs, solve PMS (binary IP or LPT — sort descending, assign longest to the first available UAV, Pinedo 2012 ch. 5) and TSP; iteratively move the customer with greatest net savings out of the makespan-determining partition; fall back to pairwise swaps between partitions; stop when nothing improves. ^[inferred]

## Numerical experiments

Computing: HP 8100 Elite, quad-core Intel i7-860, 4 GB RAM, Ubuntu 14.04; Gurobi 5.6.0; Python 2.7.5.

**§5.1 FSTSP** — 72 problems, 10 customers, 8-mile square region; depot at center-of-gravity, average x with y=0, or SW corner; 80–90% UAV-eligible; endurance 20 or 40 min; UAV 15/25/35 mph Euclidean, truck 25 mph Manhattan; $s_L = s_R = 1$ min. The underlying TSP is solved by IP (Appendix A), Clarke–Wright savings, nearest neighbor, or sweep (depot focal point, initial angle 0 rad, clockwise).

Table 1. Details of heuristic performance on small FSTSP instances (reconstructed label — the extracted caption body is garbled: only the table image `page_14_table_9.jpg` survives, caption text not recovered; gaps/runtimes verified verbatim against the in-table HTML rows). ^[ambiguous]

| TSP approach | Gap avg | Gap min | Gap max | RT avg | RT min | RT max |
|---|---|---|---|---|---|---|
| IP | -1.16 | -21.73 | 11.59 | 5.026 | 0.380 | 31.540 |
| Savings | 0.33 | -17.33 | 14.07 | 0.004 | 0.001 | 0.006 |
| Nearest neighbor | 2.91 | -12.45 | 19.26 | 0.004 | 0.001 | 0.006 |
| Sweep | 8.33 | -15.70 | 30.93 | 0.004 | 0.001 | 0.006 |
| FSTSP formulation | — | — | — | 1800.000 | 1800.000 | 1800.000 |

The 30-min limit was hit on all 72 problems (none provably optimal); negative gaps mean the heuristic beat the truncated Gurobi run. Sweep's 8.33% average ≈ 4.8 min extra delivery time, max 30.93% ≈ 18 min.

![[_papers/murray2015flying/images/page_14_chart_2.jpg]]

Fig. 5. A comparison of the FSTSP heuristic’s effectiveness using various solution approaches for the underlying TSP.

**§5.2 PDSTSP** — 10 or 20 customers, 80–90% eligible, truck & UAV 25 mph, endurance 30 min; 20/40/60/80% of customers in depot range; 3 depot positions; 10 repeats → 240 unique problems (120 × 10-customer, 120 × 20-customer); with 1/2/3 UAVs → 720 test instances. Gurobi (3-min limit) solved all 10-customer problems to optimality and terminated at the limit on 87 of 360 20-customer instances.

Table 2 Details of heuristic performance on small PDSTSP instances.

| TSP | PMS | 10c gap avg | 10c gap max | 10c RT avg | 10c RT max | 20c gap avg | 20c gap max | 20c RT avg | 20c RT max |
|---|---|---|---|---|---|---|---|---|---|
| IP | IP | 0.12 | 10.13 | 2.4856 | 29.97 | 0.22 | 5.53 | 495.272 | 21510.61 |
| IP | LPT | 0.12 | 10.13 | 2.3093 | 28.85 | 0.31 | 18.00 | 498.057 | 21521.31 |
| Savings | IP | 1.57 | 20.68 | 0.2373 | 8.26 | 3.79 | 18.83 | 3.721 | 80.68 |
| Savings | LPT | 1.58 | 20.68 | 0.0003 | 0.01 | 3.90 | 18.83 | 0.008 | 0.07 |
| Nearest | IP | 5.46 | 37.17 | 0.2335 | 8.26 | 10.63 | 34.21 | 3.137 | 65.83 |
| Nearest | LPT | 5.46 | 37.17 | 0.0003 | 0.01 | 10.68 | 34.21 | 0.002 | 0.02 |
| PDSTSP formulation |  | — | — | 0.3194 | 2.02 | — | — | 77.775 | 180.00 |

IP/IP's 0.12% average gap = 0.09 min over optimal (10c); 0.22% = 0.24 min (20c); nearest neighbor ≈ 6.8 min extra (10c) and ≈ 16.7 min (20c).

![[_papers/murray2015flying/images/page_15_chart_8.jpg]]

Fig. 6. Solution quality for variants of the PDSTSP heuristic on combined 10- and 20-customer problems. The gap is based on the best solution obtained by Gurobi within the time limit.

**§5.3 Speed vs endurance** (see [[concepts/drone-speed-selection-in-routing]]) — 90 unique problems, 25/50/75 customers, 9 speed/endurance combinations from 20 mph & 20 min to 40 mph & 40 min, truck 25 mph, savings+LPT. Faster UAVs dominate longer endurance: a 13.33-mile flight range at 40 mph × 20 min outperforms 20 mph × 40 min; the jump from 30 to 40 mph at 20 min endurance is dramatic. Low speeds cap the number of eligible customers the UAV can serve. FSTSP benefits less than PDSTSP because its tight synchronization limits exploitation; relaxing rendezvous restrictions may yield more savings. ^[inferred]

![[_papers/murray2015flying/images/page_16_chart_8.jpg]]

(a) One available UAV

![[_papers/murray2015flying/images/page_16_chart_10.jpg]]

(b) Three available UAVs

Fig. 7. Impacts of speed and endurance for the PDSTSP. Numbers above each speed/endurance pair represent groupings of equivalent total flight distances.

![[_papers/murray2015flying/images/page_17_chart_2.jpg]]

(a) Improvement over TSP solution

![[_papers/murray2015flying/images/page_17_chart_4.jpg]]

(b) Percentage of eligible customers visited by UAV

Fig. 8. Impacts of speed and endurance for the FSTSP. Numbers above each speed/endurance pair represent groupings of equivalent total flight distances.

**§5.4 Depot placement** — identical customer sets with depot moved. Fig. 9 (6 of 9 in range): PDSTSP makespan ≪ FSTSP; the optimal PDSTSP assigns only 4 of 6 eligible customers to the UAV (naive full assignment is suboptimal); FSTSP's 2-customer UAV assignment still beats truck-only TSP. Fig. 10 (4 in range): PDSTSP assigns 4, FSTSP 2; smaller gap. Fig. 11 (2 in range): FSTSP, assigning only 1 customer, beats PDSTSP's 2, because rectilinear truck travel passes near customers 3 and 5. Depot proximity governs which model applies; a priori model choice is hard.

![[_papers/murray2015flying/images/page_17_image_8.jpg]]

(a) Optimal PDSTSP solution

![[_papers/murray2015flying/images/page_17_image_10.jpg]]

(b) Optimal FSTSP solution

![[_papers/murray2015flying/images/page_16_table_4.jpg]]

(c) A comparison of delivery schedules for the two systems depicted above. The “Truck Only" schedule represents an optimal TSP solution for a single truck serving all customers.

Fig. 9. Six customers are within the UAV’s flight radius from a centrally-located depot. Customers 2 and 9 (circular nodes) are ineligible to be served via UAV (e.g., due to parcel weight restrictions).

![[_papers/murray2015flying/images/page_18_image_2.jpg]]

(a) Optimal PDSTSP solution

![[_papers/murray2015flying/images/page_18_image_4.jpg]]

(b) Optimal FSTSP solution

![[_papers/murray2015flying/images/page_18_image_6.jpg]]

(c) A comparison of delivery schedules for the two systems depicted above. The “Truck Only" schedule represents an optimal TSP solution for a single truck serving all customers.

Fig. 10. Four customers are within the UAV’s flight radius from a slightly offset depot. Customers 2 and 9 (circular nodes) are ineligible to be served via UAV (e.g., due to parcel weight restrictions).

![[_papers/murray2015flying/images/page_19_image_7.jpg]]

(a) Optimal PDSTSP solution

![[_papers/murray2015flying/images/page_19_image_9.jpg]]

(b) Optimal FSTSP solution

![[_papers/murray2015flying/images/page_19_image_11.jpg]]

(c) A comparison of delivery schedules for the two systems depicted above. The "Truck Only' schedule represents an optimal TSP solution for a single truck serving all customers.

Fig. 11. Only two customers are within the UAV flight radius from a remotely-located depot. Customers 2 and 9 (circular nodes) are ineligible to be served via UAV (e.g., due to parcel weight restrictions).

## Limitations & future work

MILP solves only small instances optimally. Authors propose relaxing launch/return at the same location, rendezvous at non-customer locations, multiple UAVs and trucks, integrating FSTSP+PDSTSP, local search on Algorithm 6 lines 29–34, simulated annealing/tabu search, lower bounds via constraint relaxation, and a cost-based objective. Acknowledgements: Eddie Robison Rivera, EIC Yafeng Yin, two reviewers. The FSTSP defined here is the single-sidekick base for [[concepts/multiple-flying-sidekicks-traveling-salesman-problem]] (Murray 2020); the PDSTSP seeds [[concepts/parallel-drone-scheduling-traveling-salesman-problem]] (solved later by Ants/HACO, ALNS matheuristics, CP). ^[inferred]

## Related

- [[references/murray2020-multiple-flying-sidekicks-tsp]] — multiple flying sidekicks, the follow-up generalization by Murray.
- [[references/windrasmara2022-alns-multi-drop-fstsp]] — multi-drop ALNS heuristic on the FSTSP, building on the single-drop FSTSP lineage.
- [[references/dorling2017-drone-delivery-vrp]] — VRPD, the closest contemporary depot-launch model.
- [[references/ha2020-vrp-synchronization-lp-alns]] — CP/LP-ALNS for VRP with synchronization constraints.
- [[references/dinh2021-haco-pdstsp]], [[references/dellamico2020-matheuristics-pdstsp]], [[references/montemanni2023-cp-pdsvrp]], [[references/nguyen2022-min-cost-pdsvrp]] — PDS-line descendants.
- [[references/cheng2020-drone-routing-energy-function]], [[references/torabbeigi2020-payload-bcr-drone-scheduling]] — energy/payload-aware descendants.
- [[concepts/hybrid-truck-drone-delivery]], [[concepts/ellipse-based-flight-segment-geometry]] — HTDD triple-platform FSTSP extension: trucks as mobile launch stations, a third delivery platform, time-balanced truck+drone makespan by Wang et al. 2019. ^[extracted]

## Sources

- [[_papers/murray2015flying/murray2015flying-extracted]]
- [[_papers/murray2015flying/murray2015flying]]
- [[_papers/murray2015flying/images/page_2_image_2.jpg]], [[_papers/murray2015flying/images/page_2_image_4.jpg]], [[_papers/murray2015flying/images/page_2_image_6.jpg]], [[_papers/murray2015flying/images/page_2_image_8.jpg]]
- [[_papers/murray2015flying/images/page_3_image_2.jpg]], [[_papers/murray2015flying/images/page_3_image_4.jpg]], [[_papers/murray2015flying/images/page_3_table_6.jpg]]
- [[_papers/murray2015flying/images/page_9_image_3.jpg]]
- [[_papers/murray2015flying/images/page_14_chart_2.jpg]], [[_papers/murray2015flying/images/page_15_chart_8.jpg]]
- [[_papers/murray2015flying/images/page_16_chart_8.jpg]], [[_papers/murray2015flying/images/page_16_chart_10.jpg]], [[_papers/murray2015flying/images/page_16_table_4.jpg]]
- [[_papers/murray2015flying/images/page_17_chart_2.jpg]], [[_papers/murray2015flying/images/page_17_chart_4.jpg]], [[_papers/murray2015flying/images/page_17_image_8.jpg]], [[_papers/murray2015flying/images/page_17_image_10.jpg]]
- [[_papers/murray2015flying/images/page_18_image_2.jpg]], [[_papers/murray2015flying/images/page_18_image_4.jpg]], [[_papers/murray2015flying/images/page_18_image_6.jpg]]
- [[_papers/murray2015flying/images/page_19_image_7.jpg]], [[_papers/murray2015flying/images/page_19_image_9.jpg]], [[_papers/murray2015flying/images/page_19_image_11.jpg]]
