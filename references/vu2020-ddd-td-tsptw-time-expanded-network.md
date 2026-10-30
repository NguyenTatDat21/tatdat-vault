---
title: 'Vu, Hewitt, Boland, Savelsbergh: Dynamic Discretization Discovery for Solving
  the Time-Dependent Traveling Salesman Problem with Time Windows (Transportation
  Science, 2020)'
summary: DDD-TD-TSPTW solves TD-TSPTW on a partially time-expanded network, outperforms
  TTBF-BC on 1,912 benchmark instances, solves 60-80 locations, and optimizes the
  duration objective.
type: reference
tags: [paper, tsp, time-windows, time-dependent-travel-times, dynamic-discretization, integer-programming, branch-and-cut, computational-study]
provenance:
  extracted: 0.74
  inferred: 0.19
  ambiguous: 0.07
base_confidence: 0.67
created: '2026-10-28T23:10:00+07:00'
updated: 2026-10-30T16:34:49Z
tier: core
category: references
lifecycle: draft
lifecycle_changed: '2026-10-28'
sources:
  - "[[_papers/vu2020dynamic/vu2020dynamic-extracted.md]]"
  - "[[_papers/vu2020dynamic/vu2020dynamic.md]]"
  - "[[_papers/vu2020dynamic/images/page_9_image_3.jpg]]"
  - "[[_papers/vu2020dynamic/images/page_9_image_5.jpg]]"
  - "[[_papers/vu2020dynamic/images/page_12_image_1.jpg]]"
  - "[[_papers/vu2020dynamic/images/page_18_image_1.jpg]]"
  - "[[_papers/vu2020dynamic/images/page_18_image_3.jpg]]"
  - "[[_papers/vu2020dynamic/images/page_22_chart_1.jpg]]"
  - "[[_papers/vu2020dynamic/images/page_23_chart_1.jpg]]"
  - "[[_papers/vu2020dynamic/images/page_27_image_5.jpg]]"
relationships:
  - target: '[[concepts/first-in-first-out-property-in-time-dependent-travel]]'
    type: related_to
  - target: '[[concepts/partially-time-expanded-network-lower-bound]]'
    type: related_to
  - target: '[[concepts/primal-arc-sets-ddd-two-networks]]'
    type: related_to
  - target: '[[concepts/lengthen-arcs-add-node-ddd-refinement]]'
    type: related_to
  - target: '[[concepts/duration-objective-depot-discretization]]'
    type: related_to
  - target: '[[concepts/valid-inequalities-subtour-sequence-ddd]]'
    type: related_to
  - target: '[[concepts/dynamic-discretization-discovery]]'
    type: derived_from

---

> [!tldr] DDD-TD-TSPTW solves TD-TSPTW with FIFO piecewise-linear travel times on a partially time-expanded network, beats the TTBF-BC branch-and-cut on all 1,912 Cordeau/Arigliano instances, solves 60-80 location instances, and covers the duration objective.

## Problem, formulation, objectives

Time-dependent traveling salesman problem with time windows (TD-TSPTW): a vehicle departs the depot, visits each location exactly once within a time window [e_i, l_i], and returns to the depot inside [e_0, l_0]. Travel times are piecewise-linear functions of departure time with a finite number of breakpoints, and the First-In, First-Out property holds, a later departure cannot cause an earlier arrival, so every linear piece has slope at least −1. A feasible solution is a sequence of node-time pairs starting and ending at the depot, with arrivals inside the windows; the makespan objective minimizes the return time t_{n+1}, the duration objective minimizes t_{n+1} − t_0.

The integer program TD-TSPTW(D) is defined on a time-expanded network D = (N, A) with nodes (i, t) for time points T_i including e_i and l_i, and arcs ((i, t), (j, t')) with t' = max{e_j, t + τ_ij(t)} (the arc embeds waiting) and t' ≤ l_j. Constraint 1 requires the vehicle to arrive at each location exactly once inside the window; constraint 2 is flow balance, so the vehicle departs from each node it reaches; constraint 3 defines binary variables. Time windows and time-dependent travel times are embedded directly in the network.

Makespan is modeled by setting c_ij(t) = 0 for all arcs with j not the depot and c_i0(t) = t + τ_i0(t) for return arcs, so costs are incurred only on return, and the cost function is non-negative and non-decreasing in t. The duration objective sets c_0j(t) = −t for arcs leaving the depot, so the cost is non-positive and non-increasing; under FIFO, the only waiting that is ever beneficial is at the depot. ^[inferred]

## The partially time-expanded network and its properties

A partially time-expanded network D_T = (N_T, A_T) is built from a subset of timed nodes. Properties maintained: every window-open and window-close node is in N_T; times in N_T lie within the window; for every node (i, t) in N_T and every arc (i, j) with t + τ_ij(t) ≤ l_j, D_T contains a travel arc (i, j), and every arc in A_T satisfies t' = e_j when t + τ_ij(t) < e_j, or e_j ≤ t' ≤ t + τ_ij(t); arc costs are underestimates, c_ij(t) := min of c_ij(h) for h in [t, l_i] with h + τ_ij(h) ≤ l_j; and Property 5, every arc is as long as possible, strengthening the lower bound by reducing the feasible region. ^[inferred]

Lemma 1: if D_T and the costs satisfy Properties 1-4, the optimal value of TD-TSPTW(D_T) is a lower bound on the optimal value of TD-TSPTW(D). The proof maps every path in D to a path in D_T of equal or smaller cost by induction on the node index, starting from the depot node at time e_0 and using Properties 3 and 4. Lemma 2: for instances with non-decreasing arc costs (the makespan case), if the path corresponding to an optimal solution of TD-TSPTW(D_T) uses arcs that exactly model travel time, then a feasible optimal solution to TD-TSPTW(D) can be derived from it. For the duration objective, all arcs except depot-departing arcs have non-decreasing cost, so adding a node (0, t) for every time at which a feasible tour may start adapts the same proof.

## Algorithm

DDD-TD-TSPTW, implemented in C++ with Gurobi 6.5.0 on a Xeon E5-4610 v2 2.30GHz workstation running Ubuntu 14.04.3, solves single-thread integer programs with MIP gap 1e-4, runs within one hour, and refines D_T iteratively. Preprocessing follows Desrochers, Desrosiers and Solomon, and Montero et al. 2017, using Δ_ij(t) values, the earliest time the vehicle can depart location j after departing i at time t, computed from shortest paths when the triangle inequality fails. Time-window tightening rules push e_k up to the earliest arrival and l_k down to the latest feasible departure; two additional rules, valid when waiting is not beneficial, remove unnecessary departures. Arc pruning uses precedence, j ≺ i, derived from infeasible sequences i → j, from triplets i → j → k, k → i → j, and i → k → j, and precedences are transitively closed.

The initial D_T has node set = {e_i, l_i} for all locations. Each iteration solves TD-TSPTW(D_T), which gives a lower bound that can be computed with an early termination on the IP, then attempts to convert the integer solution to a feasible TD-TSPTW solution. Two primal networks are built at every iteration: D̄¹ with arcs at least as long as correct travel time, whose solutions are always feasible, and D̄², which keeps arcs with t' > t and replaces non-positive arcs with longer ones, guaranteeing no subtours. A candidate solution from D_T can be converted when it has no subtour and no time-window-violating sequence; conversion assigns dispatch times as early as possible. Valid inequalities are added for every detected subtour M and infeasible location sequence M, respectively summing x over M at most |M|−1 and summing x over the sequence at most |M|−2, and, because M is defined by locations, the inequalities apply to every time-expanded network. Lengthening a too-short arc in every iteration guarantees correctness; lengthening arcs opportunistically, adding the nodes needed to continue along the path, is computationally beneficial, and pruning arcs when a new feasible solution z is found, removing arcs with t + τ_ij(t) ≥ z and resetting l_0 = z − 1, then re-running preprocessing, makes the IP smaller. TerFinite: nodes and arcs are never removed, so after a finite number of iterations D_T equals D. ^[ambiguous]

## Computational results

Set 1 has 952 instances (960 reported, 8 missing, as Montero et al. 2017 also found) with 3 travel-time intervals, Set w100 has 960 instances with 73 intervals; n ranges 15, 20, 30, 40; customers sit in three concentric zones, city center, outskirts, residential area, traffic density depends on the origin zone, congestion parameter Δ, and two traffic patterns A, B; day is divided into morning, middle, evening periods, data multiplied by 100 and rounded. Table 1: Set 1 A, TTBF-BC 478/470/31.99 vs DDD 478/478/12.91; Set 1 B, 474/470/20.44 vs 474/474/8.79; w100 A, 108/107/100.13 vs 480/480/1.31; w100 B, 108/107/93.10 vs 480/480/1.14. TTBF-BC time is 3-4 times higher on w100 than Set 1, DDD is faster on w100 than Set 1; the DDD times on w100 include instances TTBF-BC did not solve. TTBF-BC is sensitive to the number of breakpoints, the root gap is larger on w100, so DDD is robust to time-dependent data. ^[inferred]

Dual gap, defined as (LB* − LB_1)/LB*, and primal gap (UB_1 − UB*)/UB_1, are not greatly impacted by instance size, the dual gap is smaller for w100 than Set 1, unlike TTBF-BC's root gap. The correlation coefficient between the average time-window width and DDD solve time on Set 1 is 0.01, so window width is irrelevant. Congestion: Set 1/w100 solve times 7.02/1.11 at Δ = 70, 9.77/1.2 at Δ = 80, 17.04/1.3 at Δ = 90, 9.59/1.28 at Δ = 98, so Δ = 90 is worst, and there is no clear relation between congestion and solve time. Configurations: Base 950/101.19/17.46, Base + VI 948/110.42/15.99, Base + Primal 952/24.68/4.14, Base + VI + Primal 952/10.94/4.62 for Set 1 (solved, time, iterations), and w100 960/3.94/9.97, 960/4.09/9.65, 960/3.18/3.28, 960/1.22/4.11. The valid inequalities barely matter, only 5.08 subtour-based and 14.93 infeasible-sequence inequalities per instance on Set 1, 2.34 and 10.97 on w100; primal IPs dramatically reduce time and iterations, so primal IPs and VI together give the fastest runtimes. ^[inferred]

Network size at termination by configuration for Set 1/w100: 15 locations 62.40/56.73/66.39/37.32 vs 89.34/91.17/99.80/83.56, 20 locations 133.47/127.03/125.52/72.96 vs 146.50/144.61/158.58/124.30, 30 locations 407.33/384.03/312.85/201.27 vs 300.50/298.70/339.35/249.88, 40 locations 998.76/970.51/637.00/437.38 vs 497.08/474.78/460.80/306.87. The best primal solution comes from the lower-bound network, D̄¹, D̄², 4.21%, 53.76%, 42.04% for Set 1, 23.41%, 39.95%, 36.64% for w100, so D̄¹ contributes slightly more often, and for w100 the lower-bound network wins much more often. One primal IP alone: D̄¹ 952/14.01/7.81, D̄² 952/26.79/5.83, both 952/10.94/4.62 for Set 1, D̄¹ 960/1.37/6.68, D̄² 960/3.01/5.13, both 960/1.22/4.11 for w100. Solving both primal IPs is best.

Larger instances: 60, 80, 100 locations, time window width 40, 60, 80, 100, 120, 150, two traffic patterns, four Δ values, 5 instances per class, 240 per size, 720 total, 1 hour, 1% tolerance: 60 locations 239 solved, 54.26 s, 3.78 iterations, 1.56% average gap on unsolved; 80 locations 235, 239.15 s, 4.58 iterations, 2.84%; 100 locations 227, 321.48 s, 4.69 iterations, 11.13%. The iteration count is flat, so the larger integer programs drive time, DDD struggles at 100 locations, solver progress is expected to close the gap. ^[inferred]

## Duration objective

The duration objective adds, before the initial network, a node (0, t) for every possible departure time t = e_0 + ε, e_0 + 2ε, …, ē_0, where ē_0 = min over locations i of max over t with Δ_0i(t) ≤ l_i is the latest feasible depot departure; ε is the depot waiting time unit. Waiting arcs (0, t), (0, t') between consecutive depot times get cost underestimate c_00(t) = 0, and depot-departing arcs get c_0i(t) = −t, so the underestimate is accurate for depot arcs. Lemma 1 is adapted by restricting to paths that correspond to feasible tours, the k = 0 case changes. The primal IPs are solved with the duration objective, a sub-tour-free solution from D_T is evaluated for every depot departure by enumeration and greedy evaluation, and l_0 = z − 1 + t_0 when a feasible solution z is found, followed by re-preprocessing.

Performance: Set 1 makespan 952/10.94/4.62 vs duration 930/143.45/9.77; w100 makespan 960/1.22/4.11 vs duration 955/106.20/9.87. Running two hours solves all instances, the 22 Set 1 and 5 w100 unsolved instances take 3,647.47 and 3,688.40 seconds on average. Network sizes double: initial/final for makespan 53.34/188.80 and 53.50/191.15, for duration 111.88/452.24 and 94.50/438.89. The future work is adding depot nodes dynamically rather than by enumeration.

## Conclusion

The paper states that DDD-TD-TSPTW outperforms the best literature method, is robust to instance parameters including travel-time variability, and that the combination of makespan objective and FIFO property makes travel costs non-decreasing, so the cost underestimate is always accurate; for other objectives, such as minimizing total travel time, additional techniques are needed, and stochastic travel times are a target of study. The authors acknowledge NSF grant CMMI-1435625, the first author was a postdoctoral researcher at Loyola University of Chicago, and the exchange of test instances and ideas is acknowledged from Arigliano et al. 2015 and Montero et al. 2017.

## Figures

![[_papers/vu2020dynamic/images/page_9_image_3.jpg]]
Figure 1(a): Full time-expanded network, D; c_ij(t)

![[_papers/vu2020dynamic/images/page_9_image_5.jpg]]
Figure 1(b): Partially time-expanded network, D_T; c_ij(t)

![[_papers/vu2020dynamic/images/page_12_image_1.jpg]]
Figure 2 Flow chart of DDD-TD-TSPTW

![[_papers/vu2020dynamic/images/page_18_image_1.jpg]]
Figure 3 Refining D_T, τ_u0u1(·) = 1, τ_u1u2(·) = 2 (case a, path (u_0, 1), (u_1, 1), (u_2, 2))

![[_papers/vu2020dynamic/images/page_18_image_3.jpg]]
Figure 3 Refining D_T, τ_u0u1(·) = 1, τ_u1u2(·) = 2 (case b, node (u_1, 2) added, arc ((u_1, 2), (u_2, 4)) created so the vehicle visits the same sequence of locations on arcs that model true travel times)

![[_papers/vu2020dynamic/images/page_22_chart_1.jpg]]
Figure 4 Solve times by number of locations

![[_papers/vu2020dynamic/images/page_23_chart_1.jpg]]
Figure 5 Gaps by number of locations

![[_papers/vu2020dynamic/images/page_27_image_5.jpg]]
Figure 6 Initial N_T

## Sources

Primary source: `_papers/vu2020dynamic/vu2020dynamic-extracted.md` with the Zotero sidecar `_papers/vu2020dynamic/vu2020dynamic.md` (Zotero key CGY2I5XH, journalArticle, publication Transportation Science, date May 1, 2020, year 2020, DOI 10.1287/trsc.2019.0911, creators Duc Minh Vu, Mike Hewitt, Natashia Boland, Martin Savelsbergh). The extracted page header reads "Transportation Science · January 2019" with the postprint citation "Article in Advance", so the sidecar date is taken as authority, the header is the article-in-advance date, not a conflict.^[ambiguous] Figures 1a, 1b, 2, 3a, 3b, 4, 5, 6 are embedded with verbatim captions, author-profile photos and equation crops not embedded in the page are not listed as sources. Tables 1-9 are in the extracted markdown.

## Related

- [[concepts/first-in-first-out-property-in-time-dependent-travel]] - the FIFO property, the slope-at-least-(-1) piecewise-linear travel-time functions, the Δ_ij(t) earliest-departure values, and the Ichoua-Gendreau-Potvin function.
- [[concepts/partially-time-expanded-network-lower-bound]] - Properties 1-5, Lemma 1, Lemma 2, the cost underestimate, Property 5 strengthening.
- [[concepts/primal-arc-sets-ddd-two-networks]] - D̄¹ and D̄², the primal networks that give feasible solutions and no subtours, the best-solution-source table.
- [[concepts/lengthen-arcs-add-node-ddd-refinement]] - Algorithm 2 and Algorithm 3, arc lengthening, opportunistic node addition, pruning with l_0 = z − 1.
- [[concepts/duration-objective-depot-discretization]] - the depot-discretization adaptation, ē_0, waiting arcs, l_0 = z − 1 + t_0, Table 8/9.
- [[concepts/valid-inequalities-subtour-sequence-ddd]] - constraints (7) and (8), location-defined subtour and sequence inequalities valid for every time-expanded network.
- [[concepts/dynamic-discretization-discovery]] - the DDD framework of Boland et al. 2017a applied to service network design, and the TSPTW version of Boland et al. 2017b.
- [[references/gendreau2019-handbook-metaheuristics]] - the metaheuristics handbook volume covering time-dependent routing and neighborhood search.

