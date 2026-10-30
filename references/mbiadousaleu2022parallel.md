---
title: >-
  The parallel drone scheduling problem with multiple drones and vehicles (Mbiadou Saleu, Deroussi, Feillet, Grangeon & Quilliot, 2022)
category: references
tags: [paper, drone-routing, pdstsp, pdsmtsp, multi-vehicle-fleet, iterated-local-search, dynamic-programming, label-setting, branch-and-cut, makespan-objective, cvrplib, manhattan-distance, metaheuristic-hybridization, city-logistics, giant-tour, split-decoding, milp, heuristics, optimization, ejor]
relationships:
  - target: "[[concepts/parallel-drone-scheduling-traveling-salesman-problem]]"
    type: extends
  - target: "[[references/lourenco2019iterated]]"
    type: uses
  - target: "[[references/dellamico2020-matheuristics-pdstsp]]"
    type: related_to
  - target: "[[references/ha2018-min-cost-tsp-d]]"
    type: related_to
  - target: "[[references/dinh2021-haco-pdstsp]]"
    type: related_to
  - target: "[[references/montemanni2023-cp-pdsvrp]]"
    type: related_to
  - target: "[[references/nguyen2022-min-cost-pdsvrp]]"
    type: related_to
  - target: "[[references/murray2020-multiple-flying-sidekicks-tsp]]"
    type: related_to
  - target: "[[concepts/min-cost-parallel-drone-scheduling-vrp]]"
    type: related_to
  - target: "[[concepts/metaheuristic-hybridization]]"
    type: uses
  - target: "[[concepts/branch-and-price-column-generation]]"
    type: related_to
  - target: "[[concepts/iterated-local-search]]"
    type: related_to
  - target: "[[concepts/nonlinear-drone-energy-function-in-routing]]"
    type: related_to
sources:
  - _papers/mbiadousaleu2022parallel/mbiadousaleu2022parallel-extracted.md
  - _papers/mbiadousaleu2022parallel/mbiadousaleu2022parallel.md
  - _papers/mbiadousaleu2022parallel/images/page_2_image_0.jpg
  - _papers/mbiadousaleu2022parallel/images/page_2_image_2.jpg
  - _papers/mbiadousaleu2022parallel/images/page_2_image_4.jpg
  - _papers/mbiadousaleu2022parallel/images/page_2_image_6.jpg
  - _papers/mbiadousaleu2022parallel/images/page_2_image_8.jpg
  - _papers/mbiadousaleu2022parallel/images/page_5_image_0.jpg
  - _papers/mbiadousaleu2022parallel/images/page_10_image_0.jpg
  - _papers/mbiadousaleu2022parallel/images/page_10_image_1.jpg
  - _papers/mbiadousaleu2022parallel/images/page_10_image_2.jpg
  - _papers/mbiadousaleu2022parallel/images/page_10_image_3.jpg
  - _papers/mbiadousaleu2022parallel/images/page_10_image_7.jpg
  - _papers/mbiadousaleu2022parallel/images/page_10_image_8.jpg
  - _papers/mbiadousaleu2022parallel/images/page_10_image_9.jpg
  - _papers/mbiadousaleu2022parallel/images/page_10_image_11.jpg
  - _papers/mbiadousaleu2022parallel/images/page_10_image_14.jpg
  - _papers/mbiadousaleu2022parallel/images/page_10_image_15.jpg
  - _papers/mbiadousaleu2022parallel/images/page_10_image_16.jpg
  - _papers/mbiadousaleu2022parallel/images/page_10_image_18.jpg
  - _papers/mbiadousaleu2022parallel/images/page_11_image_0.jpg
  - _papers/mbiadousaleu2022parallel/images/page_12_image_3.jpg
  - _papers/mbiadousaleu2022parallel/images/page_15_image_0.jpg
summary: >-
  PDSMTSP: K trucks, M drones in parallel, completion-time objective. Branch-and-cut fails in 3 h; ILS with dynamic-programming split of a giant tour beats B&C on 13 CVRPLIB instances, n = 50-199.
provenance:
  extracted: 0.89
  inferred: 0.09
  ambiguous: 0.02
base_confidence: 0.67
lifecycle: draft
lifecycle_changed: 2026-10-26T00:51:06Z
tier: core
created: 2026-10-26T00:51:06Z
updated: 2026-10-30T14:39:22Z
---

# The parallel drone scheduling problem with multiple drones and vehicles (Mbiadou Saleu, Deroussi, Feillet, Grangeon & Quilliot, 2022)

> [!tldr] European Journal of Operational Research 2022 (DOI 10.1016/j.ejor.2021.08.014) formalizes the PDSMTSP: K vehicles and M drones leave the depot at time 0, drones fly single round trips from the depot, there is no synchronization, and the objective is the completion time. A branch-and-cut "largely fails" within 3 hours; the paper's hybrid ILS + dynamic-programming split of a giant tour beats it on every shared instance, tested on 20 CVRPLIB instances with n = 50–199.

## Problem & Motivation

Drone parcel delivery became a real industrial program in 2013–2017: Amazon Prime Air announced a 30-minute drone delivery in December 2013, Google Wing tested in Australia in August 2014, DHL Parcelcopter delivered medications to the North Sea island Juist in September 2014, and UPS tested HorseFly launched from the roof of a delivery truck in February 2017.

![[_papers/mbiadousaleu2022parallel/images/page_2_image_0.jpg]]
*Fig. 1. Amazon Prime Air*

![[_papers/mbiadousaleu2022parallel/images/page_2_image_2.jpg]]
*Fig. 2. Google Wing*

![[_papers/mbiadousaleu2022parallel/images/page_2_image_4.jpg]]
*Fig. 3. DHL Parcelcopter*

![[_papers/mbiadousaleu2022parallel/images/page_2_image_6.jpg]]
*Fig. 4. UPS HorseFly*

Three delivery paradigms exist: truck-only, truck-drone in tandem, and truck-drone in parallel. Murray & Chu (2015) introduced both the FSTSP (drone takes off and lands on the truck, tandem) and the PDSTSP (drone flies from the depot, parallel). The parallel variant was then studied for a single vehicle: [[references/lourenco2019iterated]] describes the ILS framework the present heuristic builds on; Saleu et al. (2018, Networks 72, 459–474) gave the iterative two-step heuristic; [[references/dellamico2020-matheuristics-pdstsp]] a matheuristic; Ulmer & Thomas adaptive dynamic programming; Ham (2018) drop & pickup with constraint programming. Table 1 of the paper shows the gap this work fills: **the extension of PDSTSP to several trucks had never been studied**. ^[inferred]

![[_papers/mbiadousaleu2022parallel/images/page_2_image_8.jpg]]
*Fig. 5. Illustration of FSTSP and PDSTSP vs truck-only delivery* ^[inferred]

**PDSMTSP.** A complete directed graph `G = (N ∪ {0}, A)` of n customers plus depot 0; K vehicles and M drones; a subset `N_d ⊆ N` of drone-eligible customers (payload and battery restrictions). A vehicle tour costs `Σ t_ij` over its arcs; a drone flies a single round trip from the depot serving one customer, with time `t̂_i` covering take-off, flight, service and landing. All vehicles and drones leave the depot at time 0 and must be back; the objective minimizes the completion time `T` (max of all resources' durations). The authors call this objective "somehow academic": practical costs are vehicle usage, energy, number of drones.

![[_papers/mbiadousaleu2022parallel/images/page_5_image_0.jpg]]
*Fig. 6. A set of 10 customers served by 2 vehicles and 2 drones.* — the paper's solution vector is `((1,10,9), (5,6,7,8,4), (3), (2))`: vehicle 1 takes customers 1,10,9, vehicle 2 takes 5,6,7,8,4, customers 3 and 2 go to drones.

## Method / Architecture

**MILP.** Variables `x_ijk` (arc (i,j) in vehicle k's tour), `w_ij` (arc used by any vehicle), `z_i` (customer served by a vehicle), `y_im` (customer i assigned to drone m), `T ≥ 0`. Constraints (2)–(15): makespan per vehicle and per drone, `z_i = 1` for non-drone-eligible customers, `Σ_m y_im = 1 − z_i`, arc aggregation, in-degree = `z_i`, at most one departure from the depot per vehicle, flow conservation, and subtour elimination `Σ_{j∈S, l∉S} w_jl ≥ z_i` for every nonempty `S ⊆ N`, `i ∈ S` (exponential).

**Branch-and-cut.** IBM CPLEX 12.6 with Lazy Constraint Callbacks (on integer incumbents: circuit detection in the `w_ij > 0` graph, and circuits not connected to the depot) and User Cut Callbacks (on fractional solutions: auxiliary graph with arc capacities `w_ij`, Ford–Fulkerson max flow from depot to i; flow < `z_i` proves i unreachable and yields a SEC). The LP relaxation is weak, so the approach is restricted to small instances. ^[inferred]

**Hybrid metaheuristic HM (Algorithm 1), read as an Iterated Local Search** [[concepts/iterated-local-search]] [[references/lourenco2019iterated]]: start from a nearest-neighbor giant TSP tour τ visiting all customers in vehicle 1; repeat: `split(τ)` → `reoptimizeTSP` each vehicle subsequence with Lin–Kernighan (Helsgaun implementation) → `optimizePMS` long-processing-time assignment of drone customers → `improveSol` local search → accept only improvements. The giant tour is then rebuilt by concatenating the first X vehicle tours of the best solution in random order, inserting the drone customers randomly, then 2-opt. Ties in completion time are broken by the smaller sum of vehicle and drone durations. Three novelties over the single-vehicle heuristic of Saleu et al. (2018): ad hoc local-search moves, a modified split with new labels and bounds for several vehicles, and the ILS framework with a learning component. Decoding time is the bottleneck of the method. ^[inferred]

**Local search moves** (restricted to the resource with maximal completion time; the moved customer goes to the target resource with minimal completion time; first improvement): transfer vehicle→drone and drone→vehicle (neighborhood `O(n × M)`), exchange drone-veh (`O(n × |N_d|)`), relocate vehicle→vehicle, exchange veh-veh, cross (exchange of two sequences crossing two edges); every neighbor is evaluated in `O(1)`.

![[_papers/mbiadousaleu2022parallel/images/page_10_image_0.jpg]]
![[_papers/mbiadousaleu2022parallel/images/page_10_image_1.jpg]]
![[_papers/mbiadousaleu2022parallel/images/page_10_image_2.jpg]]
![[_papers/mbiadousaleu2022parallel/images/page_10_image_3.jpg]]
*(a) transfer from a vehicle to a drone*

![[_papers/mbiadousaleu2022parallel/images/page_10_image_7.jpg]]
![[_papers/mbiadousaleu2022parallel/images/page_10_image_8.jpg]]
![[_papers/mbiadousaleu2022parallel/images/page_10_image_9.jpg]]
![[_papers/mbiadousaleu2022parallel/images/page_10_image_11.jpg]]
*(b) transfer from a drone to a vehicle*

![[_papers/mbiadousaleu2022parallel/images/page_10_image_14.jpg]]
![[_papers/mbiadousaleu2022parallel/images/page_10_image_15.jpg]]
![[_papers/mbiadousaleu2022parallel/images/page_10_image_16.jpg]]
![[_papers/mbiadousaleu2022parallel/images/page_10_image_18.jpg]]
*(c) exchange move drone-veh*

*Fig. 7. Local search operators between a vehicle and a drone (left-hand side: before the move; right-hand side: after the move)*

![[_papers/mbiadousaleu2022parallel/images/page_11_image_0.jpg]]
*Fig. 8. Local search operators between two vehicles (left-hand side: before the move; right-hand side: after the move)*

**split(τ).** The decomposition respects the giant-tour order (vehicle sequences are subsequences, vehicle order follows τ order). Acyclic digraph `G^τ`, nodes `{0, 1.., n, n+1}` where n+1 is a depot copy; arc `(i, j)` exists iff every customer strictly between i and j in τ is drone-eligible. Each arc carries cost vector `(c¹_ij = t_ij, c²_ij = (1/M) · Σ t̂_μ over the in-between customers` — an optimistic aggregation of the drone fleet). The problem is a multi-criteria shortest path solved by dynamic programming with labels `L = (n^veh, c^preVeh, c^curVeh, c^drone, pred)` extended by two rules (extend the current vehicle tour, or close it and open a new one), and a 4-condition dominance rule.

![[_papers/mbiadousaleu2022parallel/images/page_12_image_3.jpg]]
*Fig. 9. Graph $G^{\tau}$ for the instance of tables 2(a) and 2(b), with $\tau = (1,2,3,4,5)$.*

![[_papers/mbiadousaleu2022parallel/images/page_15_image_0.jpg]]
*Fig. 10. Values $SP(i)$ for the graph of Figure 9 ($M = 1$).*

**Bounding.** UB1 = best incumbent. UB2: compute `χ(n+1, 1)` and `χ(n+1, K)` (min cost of serving the sequence with k vehicles, ignoring drones), set the "vehicle acceleration coefficient" `α = χ(n+1,1) / χ(n+1,K)`, run a single-vehicle split on costs `t_ij/α` keeping only the best label per node, re-decompose into K tours, assign the rest to drones by LPT. UB3: `α = K`. Lower bound `LB^tot` uses the shortest path `SP(i)` with arc costs `c¹ + M·c²`; pruning rule R1 (label whose completion parts already reach UB) and R2 (LB^tot ≥ UB).

**Figure 11** — *Fig. 11. Illustration of the split procedure on the graph of Figure 9, without or with the bounding mechanisms ($K = 2$, $M = 1$). The last element of the definition of a label (pred) has not been represented for the sake of simplicity*: the worked example gives UB = 27, `τ₁ = (0,1,2,0)`, `τ₂ = (0,4,5,0)`, customer 3 to the drone, solution cost 27, and `L(6) = ∅` once bounds are applied. No image is present for Figure 11 in the extracted markdown, and the paper's body text refers to it as "Figure ??". `^[ambiguous]`

**Label cap.** At most `K × T_max` labels per node (grouped by `n^veh`, sorted by `c^preVeh + c^curVeh + c^drone`). On CMT5, `T_max = 60` gives 7,177,526 labels on average, 17.96% average gap vs the B&C upper bound, 7.20 s; `T_max = 10` gives 32,592 labels, 11.96% gap, 0.05 s — `T_max = 60` was chosen as the quality/time trade-off.

## Key Equations

Makespan constraints of the MILP (one per vehicle, one per drone):

$$
T \ge \sum_{(i,j)\in A} t_{ij}\, x_{ijk} \quad \forall k,
\qquad
T \ge \sum_{i\in N_d} \hat{t}_i\, y_{im} \quad \forall m
$$

Subtour elimination constraint (10):

$$
\sum_{j \in S,\, l \notin S} w_{jl} \ge z_i \quad \forall\, \emptyset \ne S \subseteq N,\; i \in S
$$

Decomposition recursion (16), used by upper bound 2:

$$
\chi(i,k) = \min_{j <_\tau i} \max\big(\chi(j,k-1),\; t_{0,\mathrm{succ}(j)} + \mathrm{time}_\tau(\mathrm{succ}(j), i) + t_{i0}\big)
$$

Combined lower bound used for pruning:

$$
LB^{tot}(i, L) = \frac{c^{curVeh}(L) + M \cdot c^{drone}(L) + SP(i)}{K - n^{veh}(L) + 1 + M}
$$

## Results

**Instances & environment.** 20 CVRPLIB instances with the depot near the barycenter, n = 50–199, `K = ⌈fleet/2⌉`, `M = ⌊fleet/2⌋` — CMT1–CMT5 (50/75/100/150/199, fleets (3,2),(5,5),(4,4),(6,6),(9,8)), E-n51-k5, E-n76-k8, E-n101-k8, M-n151-k12, M-n200-k16, P-n51-k10 … P-n101-k4, X-n110-k13, X-n115-k10, X-n139-k10. All customers drone-eligible; vehicles use Manhattan distance, drones Euclidean. C++ heuristic on an Intel i5-6200U, 8 GB RAM, 1000 s limit; CPLEX 12.6 on a 16-core Xeon E5-2670, 62.5 GB, 3 h limit.

**Branch-and-cut largely fails** in 3 h: no proven optimum, gaps `Gap1` between 22.79% and 97.20% on the 13 instances it closed. The heuristics beat every B&C upper bound:

| Instance | B&C C.T. | Gap1 | Heuristic best |
|---|---|---|---|
| CMT1 (50,3,2) | 188 | 22.79% | 166 (HM(LL)) |
| CMT2 (75,5,5) | 3630.86 | 97.20% | 130.23 |
| CMT3 (100,4,4) | 4537.11 | 96.45% | 184 |
| E-n76-k8 (75,4,4) | 2975.51 | 95.73% | 154 |
| P-n51-k10 (50,5,5) | 230 | 64.74% | 111.07 |
| P-n76-k5 (75,3,2) | 280 | 35.26% | 200 |
| P-n101-k4 (100,2,2) | 4725.47 | 93.20% | 342 (HMb) |

B&C lower bounds are weak: CMT1 LB 145.86 vs heuristic 166; P-n101-k4 LB 321.74 vs 342.69 — the best heuristics are "at worst of reasonable quality".

**Table 5 highlights.** HM/HMb behave alike; the multi-start variant MS never finds a best solution (learning via the giant-tour rebuild pays off). Best completion times: CMT1 166, CMT2 130.23, CMT3 184, CMT4 150 (HMb), CMT5 138 (HM), M-n200-k16 144, X-n110-k13 1864, X-n115-k10 2258, X-n139-k10 2492 (HMb(LL)) vs 2928.64 for unrestricted HM — limiting labels buys robustness on decoding-stalled instances.

**Execution details.** Dominance + bounding prune >95% of labels (99.29% on CMT5); on n > 60, 70–90% of the 1000 s is spent in `split(τ)`, 1–4% in local search. The drone-aggregation gap gD stays under 5% for almost all instances (CMT5 HM 4.60, X-n110-k13 HM 5.68, X-n139-k10 HM(LL) 7.73).

**Additional experiments (Table 9).** With the depot moved to a corner, completion time rises and drone assignments drop (CMT1: 232 vs 168, 5 drone customers vs 8). Truck-only runs (0% drone-eligible) lower the completion time by 20–25% on most instances (CMT1 212, CMT2 168, P-n101-k4 420 vs 342.69 with drones) — except X-n139-k10, 2844 vs the best drone run 2492, consistent with HM's failure on that instance.

## Limitations

First PDSMTSP paper, so no literature comparison was possible; the authors' own branch-and-cut gave no competitive basis. The decoding combinatorial explosion stalls X-n139-k10 (unrestricted HM spends one iteration, 77,374,287 labels, 3056 s in `split(τ)`). Absolute completion times on synthetic CVRPLIB instances are hard to interpret for logistics value. The model is weakly constrained (mostly partition/permutation constraints), which makes constraint programming propagation difficult. Future work: an exact framework (branch-and-price, see [[concepts/branch-and-price-column-generation]]), controlling `split(τ)` combinatorics, CP formulations, time windows, real-time traffic, drone recharging, fleet sizing. Funding: ANR "Investissements d'Avenir", IMobS3 LabEx ANR-10-LABX-0016, IDEX-ISITE CAP 20-25 ANR-16-IDEX-0001, ERDF AURA region, Auvergne-Rhône-Alpes region. ^[inferred]

## Related

- [[concepts/parallel-drone-scheduling-traveling-salesman-problem]] — PDSTSP: this paper extends it from 1 vehicle to K vehicles (type: extends)
- [[references/lourenco2019iterated]] — the ILS framework the hybrid metaheuristic instantiates (type: uses)
- [[concepts/metaheuristic-hybridization]] — DP decoding + LK reoptimization + local search in one ILS shell (type: uses)
- [[references/dellamico2020-matheuristics-pdstsp]] — matheuristic for single-vehicle PDSTSP, same problem family
- [[references/ha2018-min-cost-tsp-d]] — min-cost TSPD (single truck), parallel-variant lineage
- [[references/dinh2021-haco-pdstsp]] — ACO matheuristic for PDSTSP
- [[references/montemanni2023-cp-pdsvrp]] — constraint programming for the parallel drone scheduling VRP, the CP perspective the authors propose here
- [[references/nguyen2022-min-cost-pdsvrp]] — min-cost PDSVRP line of work
- [[references/murray2020-multiple-flying-sidekicks-tsp]] — multi-drone tandem FSTSP, the parallel's counterpart
- [[concepts/min-cost-parallel-drone-scheduling-vrp]] — min-cost parallel scheduling variant of the same family
- [[concepts/branch-and-price-column-generation]] — the exact approach suggested as a perspective ^[inferred]

## Sources

- [[_papers/mbiadousaleu2022parallel/mbiadousaleu2022parallel-extracted.md]]
- [[_papers/mbiadousaleu2022parallel/mbiadousaleu2022parallel.md]]
- [[_papers/mbiadousaleu2022parallel/images/page_2_image_0.jpg]]
- [[_papers/mbiadousaleu2022parallel/images/page_2_image_2.jpg]]
- [[_papers/mbiadousaleu2022parallel/images/page_2_image_4.jpg]]
- [[_papers/mbiadousaleu2022parallel/images/page_2_image_6.jpg]]
- [[_papers/mbiadousaleu2022parallel/images/page_2_image_8.jpg]]
- [[_papers/mbiadousaleu2022parallel/images/page_5_image_0.jpg]]
- [[_papers/mbiadousaleu2022parallel/images/page_10_image_0.jpg]]
- [[_papers/mbiadousaleu2022parallel/images/page_10_image_1.jpg]]
- [[_papers/mbiadousaleu2022parallel/images/page_10_image_2.jpg]]
- [[_papers/mbiadousaleu2022parallel/images/page_10_image_3.jpg]]
- [[_papers/mbiadousaleu2022parallel/images/page_10_image_7.jpg]]
- [[_papers/mbiadousaleu2022parallel/images/page_10_image_8.jpg]]
- [[_papers/mbiadousaleu2022parallel/images/page_10_image_9.jpg]]
- [[_papers/mbiadousaleu2022parallel/images/page_10_image_11.jpg]]
- [[_papers/mbiadousaleu2022parallel/images/page_10_image_14.jpg]]
- [[_papers/mbiadousaleu2022parallel/images/page_10_image_15.jpg]]
- [[_papers/mbiadousaleu2022parallel/images/page_10_image_16.jpg]]
- [[_papers/mbiadousaleu2022parallel/images/page_10_image_18.jpg]]
- [[_papers/mbiadousaleu2022parallel/images/page_11_image_0.jpg]]
- [[_papers/mbiadousaleu2022parallel/images/page_12_image_3.jpg]]
- [[_papers/mbiadousaleu2022parallel/images/page_15_image_0.jpg]]
