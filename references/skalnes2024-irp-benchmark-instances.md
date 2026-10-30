---
title: "Skålnes, Ben Ahmed, Hvattum, Stålhane: New benchmark instances for the inventory routing problem (European Journal of Operational Research, 2024)"
summary: "IRP benchmark paper: 270 real-world-like instances A-P-N-Q-T, sine demand trajectories, MATILDA instance space, B&C and matheuristic bounds, clustered instances cross phase transition."
type: reference
tags: [paper, benchmark-instances, inventory-routing, vendor-managed-inventory, matheuristic, branch-and-cut, instance-space-analysis, matilda, phase-transition, instance-generation]
provenance:
  extracted: 0.94
  inferred: 0.03
  ambiguous: 0.03
base_confidence: 0.67
created: 2026-10-28T15:40:00Z
updated: 2026-10-30T14:39:22Z
tier: supporting
category: references
lifecycle: draft
lifecycle_changed: "2026-10-28"
sources:
  - "[[_papers/skalnes2024new/skalnes2024new-extracted.md]]"
  - "[[_papers/skalnes2024new/skalnes2024new.md]]"
  - "[[_papers/skalnes2024new/images/page_3_chart_2.jpg]]"
  - "[[_papers/skalnes2024new/images/page_4_chart_2.jpg]]"
  - "[[_papers/skalnes2024new/images/page_8_chart_2.jpg]]"
  - "[[_papers/skalnes2024new/images/page_9_chart_2.jpg]]"
  - "[[_papers/skalnes2024new/images/page_9_chart_19.jpg]]"
  - "[[_papers/skalnes2024new/images/page_9_chart_21.jpg]]"
  - "[[_papers/skalnes2024new/images/page_12_chart_2.jpg]]"
  - "[[_papers/skalnes2024new/images/page_13_chart_2.jpg]]"
  - "[[_papers/skalnes2024new/images/page_14_chart_4.jpg]]"
  - "[[_papers/skalnes2024new/images/page_14_chart_6.jpg]]"
  - "[[_papers/skalnes2024new/images/page_15_chart_2.jpg]]"
  - "[[_papers/skalnes2024new/images/page_15_chart_4.jpg]]"
relationships:
  - target: "[[references/pisinger2019-large-neighborhood-search]]"
    type: related_to
  - target: "[[concepts/large-neighborhood-search]]"
    type: related_to

---

> [!tldr] 270 new IRP instances built to break the pattern that made the Archetti benchmarks easy for tailored methods; the new set is harder for B&C and matheuristics, clustered instances cross a phase transition, route lengths stay short because fleets scale with customers.

## Why new instances are needed

The existing IRP benchmarks have features that methods can exploit. Avella, Boccia and Wolsey (2015) showed that inventory capacities in the Archetti benchmarks are integer multiples, specifically two and three, of customer demands, which makes specialized valid inequalities data-dependent; abundant vehicle capacity lets optimal delivery dates be computed easily, so the IRP collapses to a capacitated VRP per period, or TSPs per period and vehicle with visits fixed a priori. For the 212 three-period instances solved to optimality by the B&C method, on average 5.3%, 94%, and 7.3% of customers are visited in the first, second and third period. Heuristics such as the matheuristic of Archetti et al. 2017 and Solyalı & Süral 2022 exploit this. Long planning horizons lose difficulty when demands are stationary because repeating distribution patterns can be identified. The new set avoids overfitting by using non-stationary demands, real-life vehicle fleets, higher inventory-capacity variance, an explicit depot capacity bound, random/clustered/mixed node positions, depot-minimal inventory costs, and distances rounded to satisfy the triangle inequality.

The instance-space analysis using the MATILDA platform shows the new instances fill regions the original set does not cover, and existing solution methods struggle: the new set is both diverse and complex, so new methods are needed.

## Instance generation

Instances are pallet-transport based, generic for road transport, with three real vehicle types: small truck 8 EUR-pallets, truck 18, trailer truck 38, a homogeneous fleet scaled to customers and demand; a EUR-pallet is 1200 × 800 × 144 mm and carries 1500 kg safe load. The vehicle capacity is the most constrained feature in practice, so the fleet comes first.

Demand is built from a sine trajectory per customer: mean = B_i K_i sin(θ_i t + φ_i) + K_i, coefficients drawn from uniform distributions; the realized demand in each period is drawn from a uniform distribution centered on the trajectory with symmetric support a from the interval 0,1, rounded to the nearest integer; a = 0.2 with trajectory mean 10 gives demands between 8 and 12. Depot production is constant, S_t = ceil(sum of all demands / periods).

Inventory capacity per customer comes from a minimum visiting frequency F drawn uniformly from [1, |T|]: I_i = ceil(max(max_t D_it, sum D_it / F)); F = 1 sets capacity equal to total demand over the horizon, F = |T| sets it equal to the maximum demand. Depot capacity is drawn uniformly from [max(S_t, max_i sum_t D_it), sum of all demand], initial customer inventory from [0, min(D_i1 + D_i2, L_i)], initial depot inventory from [sum of first-period customer demand, min(S_1 + S_2, L_0)]. Inventory costs assume economies of scale at the depot: customer marginal cost per unit per period is drawn uniformly from [0.0, 0.3], based on the multi-case study of Azzi et al. 2014.^[inferred]

Nodes sit on a 500 × 500 grid, depot coordinates uniform. Random positioning draws coordinates uniformly. Clustered positioning draws a center uniformly, then an angle uniform and a radius r from an exponentially decaying distribution p(x | λ) = λ e^{-λ r}; λ = 50 is the tested value reflecting a city or town. Random-clustered positioning puts 50% of customers randomly, the rest clustered. Urban grid units mean 0.1 km per unit, rural 0.5 km; C_ij urban = floor(0.1 E_ij + 1), rural = floor(0.5 E_ij + 1), Euclidean distance E_ij, rounding plus one keeps the triangle inequality valid, which matters because many algorithms work well only when it holds. Transport cost is 1 euro per km, under the reported freight rates of 1.52 euros/km (van der Meulen et al. 2020) and 1.58 euros/km (Ti&Upply 2020) for trailer trucks, within the 0.80-3.16 euros/km route range.

The name format is A-P-N-Q-T: area (rural/urban), positioning (R/C/RC), customers (10, 25, 50, 100, 200), vehicle capacity (8/18/38), periods (6/9/12); varying attributes one at a time yields 270 instances. Some new rural random 6-period 10-25 customer instances overlap the original attributes, with fleets scaled up. The instances and best-known solutions are public at the AXIOM project web page.

## Feasibility inspection heuristic

The feasibility heuristic checks whether a fleet can cover the demands; stock-outs σ_it = max(D_it − I_it, 0) drive the loop. If vehicles can be added, K grows by k̄ = min(K_max − K, ceil(sum σ / (Q × periods))); when K cannot grow, demands are reduced by d̄ = sum σ / periods per period per customer; each change regenerates an IRP solution, iterated until no stock-outs. The construction heuristic uses urgent customers (inventory below demand) delivered with the stock-out quantity on the most residual vehicle, then non-urgent customers added with quantity min(residual capacity, capacity headroom, supplier stock), routes built by the Lin-Kernighan heuristic.^[inferred]

## Model and solution methods

The MILP is the aggregated form of Skålnes et al. 2022: objective min transport + inventory, inventory balance for depot and customers, limits between lower and upper inventory, delivered quantity bounded by K δ_0t, max-level policy q_it ≤ L_i − s_i(t−1), delivery only when visited via min(L_i − I_it, Q) δ_it, degree constraints, flow balance, subtour and capacitated subtour elimination, domain constraints. The B&C solves the linear relaxation of constraints 7-15 and 18-21, adds subtour constraints dynamically, separates capacity inequalities of Desaulniers et al. 2016, the simple disjoint route inequalities of Avella et al. 2018, and Coelho & Laporte 2014 valid inequalities, omitting h-DR inequalities because h = 8 separation is too expensive for 100-200 customer instances; capacity and DR inequalities are separated exactly only in the root node; the customer schedule formulation is not used because enumeration is too slow for 9 and 12 periods, suited only to six periods or less.

The matheuristic is the reimplementation of Archetti et al. 2017: construction from a relaxation keeping δ integrality, Lin-Kernighan for routes, a fail-safe construction, tabu search with five moves (add visit, remove visit, move visit to another day, swap two visits, move to a different route) allowing capacity and supplier stock-out violations with recovery, an improvement phase fixing variables to zero and re-solving the MILP. C++, Gurobi 9.5 default settings, single thread, Lenovo NextScale with dual Intel E5-2670v3 2.3GHz, 64 GB RAM; B&C time limit 7,200 seconds, matheuristic 1,800 seconds for 25 customers and below, 2,400 for the rest.

## Instance space analysis

13 features are defined: customers, periods, vehicles, demand standard deviation, inventory capacity standard deviation, edge cost standard deviation, inventory-to-edge cost ratio, demand-to-inventory ratio, demand-to-vehicle-capacity ratio, inventory-to-vehicle ratio, depot-customer inventory cost ratio, demand-to-initial-inventory ratio, initial-inventory-to-capacity ratio. MATILDA auto-selects the 10 least overlapping features correlated with the gap criterion gap = (UB − LB)/UB, then projects to z1, z2 coordinates. New instances (red) and original instances (blue) lie in distinct areas of the projected space, so the new set complements the original. Feature plots show: demand standard deviation much larger for new instances; edge cost standard deviation varies more, reflecting the three location structures; inventory-to-edge ratio extremes similar, with smoother gradient for new instances; inventory capacity standard deviation and customer counts distributed similarly; the demand-to-inventory ratio of original instances takes three to four distinct levels, matching the two-and-three multiples structure, while new instances show continuous transition; new instances have lower demand-to-initial-inventory ratio, so fewer customers can be served in the first period from initial inventory, and a lower initial-inventory-to-capacity ratio, so customers start emptier. New instances with few vehicles sit on the left of the space, many vehicles on the right.

## Performance across all instances

The reimplementation's upper bounds are slightly worse on average than Archetti et al. 2017: Table 3 gives average differences by customers and vehicles, 0.00 at 5, -0.03/-0.27 at 10, -1.56 at 15, 0.39 at 20, 0.68 at 25, 3.70 at 30, overall 0.49%, with the worst subset at 30 customers with 4 and 5 vehicles; better gaps than the original implementation occur on the smallest instances.^[inferred] The gap definition used later is (UB − LB)/LB, where LB is the B&C bound.

Feasible-solution counts (Table 4): constructive heuristic finds feasible solutions on all 270 instances, matheuristic finds 108 (all 10- and 25-customer instances, zero at 50, 100, 200), B&C finds 133: 18 of 50 (5 R, 3 C, 10 RC), 7 of 100 (3 R, 4 RC), zero at 200. B&C proves optimality on 13 of 270 instances, all 10-customer: 6 random, 1 clustered, 6 random-clustered; the matheuristic finds one optimal solution in a random-clustered instance. Average gaps (Table 5): constructive 49.9 (R), 52.8 (C), 53.9 (RC), 52.2 (10 customers), 52.9 (25), 60.3 (50), 88.4 (100), 142.5 (200); matheuristic 1.53 (10), 12.87 (25), n/a above; B&C 0.75 (10), 2.33 (25), 30.65 (50), 276.1 (100), n/a (200). The B&C 100-customer average of 276.1% mixes a few feasible solutions that are far worse than the constructive heuristic, so the 50-100 customer rows are hard to read.^[ambiguous]

Clustered instances have smaller average gaps than random and mixed for both matheuristic and B&C, explained by cost drivers being the arcs between clusters: once the inter-cluster arcs are fixed, the lower bound is strong, the sequence within a cluster barely affects cost. B&C struggles to find feasible solutions for clustered instances and finds the most in random-clustered ones, which the paper reads as crossing a phase transition threshold, as defined by Gent & Walsh 1996, with TSP evidence from Zhang 2004 on distinct distance values and van Hemert & Urquhart 2004 plus Smith-Miles et al. 2010 on cluster-to-node ratios. Eighteen new instances share customers, vehicles and periods with at least one original instance, 40 original instances share with new ones; the matheuristic on 12 new 10-customer instances with vehicles 2, 4, 5 and 6 periods gets gaps 23% better than 30 comparable original instances, spending 83.6% more time on average; the six new 25-customer instances get gaps 12.3% worse than 10 original instances in roughly the same time; B&C performs similarly.^[inferred] So the seven other features do not make the new instances easier.

## Drivers of difficulty

Gaps per periods (Table 6): matheuristic 10-customer 0.90/1.47/2.22 for 6/9/12 periods, 25-customer 9.46/12.49/16.66; B&C 10-customer 0.52/0.66/1.08, 25-customer 2.01/1.82/3.15, 50-customer 19.16/39.90/44.94, 100-customer 276.3/334.8/40.8. Ignoring the seven feasible 100-customer instances, the averages for 6, 9, 12 periods become 4.84%, 5.96% and 6.40%, confirming periods increase difficulty. Periods move the gap much less than customers do, because more customers bring larger fleets. Ten-customer times (Table 7): matheuristic hits its 1,800-second limit on 6, 9, 12 periods for truck 18, at 1,339 seconds for trailer trucks with 6 periods; B&C is fastest on small trucks (1,498 seconds for 6 periods), 5,265 for 12 periods, truck and trailer trucks reach the 7,200 limit, all averaged 3,706/6,006/6,555.^[inferred]

Gaps per vehicle capacity (Table 8): matheuristic at 10 customers 0.52 (Q=8), 1.53 (18), 2.54 (38); at 25 customers 9.17/13.79/15.65; B&C at 10 customers 0.11/0.39/1.76, 25 customers 0.68/2.47/3.83, 50 customers 27.45/50.30/24.72, 100 customers 42.23/587.8. The matheuristic is fastest on trailer trucks yet gets best solutions on small trucks; the B&C gets best gaps on small trucks, solution quality drops as capacity rises, plausibly because a large capacity makes the linear relaxation weaker under the delivery constraint: a large Q needs less arc flow, so the bound is worse. Route length as number of customers in a route (Fig. 6 box plot): small truck Q=8 routes are direct routes visiting only one customer in more than 75% of routes; truck Q=18 has more than 50% one-customer routes plus a significant share with several visits; trailer truck Q=38 has less than 25% one-customer routes and more than half with three or more visits; Fig. 7 shows the original instances have much longer routes, so the new instances represent a different business segment, increasing customers by expanding the fleet, not vehicle capacity.^[inferred]

## Conclusion

The paper states that commodity flow formulations scale well with many vehicles and periods, so the new instances favor them; branch-cut-and-price is favored when routes have few visits; valid inequalities and branching decisions on the new set are open research; heuristic work needs more complex neighborhoods and instance-specific information such as clustering by location or consumption rate, as Cao & Glover 2010 suggest. Instances can be extended to multiple depots, multiple and perishable products, time windows, heterogeneous fleets; for variants where customer inventory costs are zero, set the depot inventory holding cost equal to the first customer's in the instance files.

## Figures

![[_papers/skalnes2024new/images/page_3_chart_2.jpg]]
Fig. 1. Illustration of a customer demand distribution.

![[_papers/skalnes2024new/images/page_4_chart_2.jpg]]
Fig. 2. An example of random, clustered, and random-clustered node positioning.

![[_papers/skalnes2024new/images/page_8_chart_2.jpg]]
Fig. 3. Distribution of instances across the 2D projection of the instance space.

![[_papers/skalnes2024new/images/page_9_chart_2.jpg]]
Fig. 4a. Average standard deviation of demands across the 2D instance space.

![[_papers/skalnes2024new/images/page_9_chart_19.jpg]]
Fig. 5a. Highlighting the percentage of good algorithms.

![[_papers/skalnes2024new/images/page_9_chart_21.jpg]]
Fig. 5b. The normalized gap obtained by the B&C method.

![[_papers/skalnes2024new/images/page_12_chart_2.jpg]]
Fig. 6. Overview of the route length on a subset of the new instances.

![[_papers/skalnes2024new/images/page_13_chart_2.jpg]]
Fig. 7. Overview of the route lengths on a subset of the original instances.

![[_papers/skalnes2024new/images/page_14_chart_4.jpg]]
Fig. A.1. Highlighting each instance where the B&C method obtained a gap lower than or equal to 5%.

![[_papers/skalnes2024new/images/page_14_chart_6.jpg]]
Fig. A.2. Highlighting each instance where the matheruistic obtained a gap lower than or equal to 5%.

![[_papers/skalnes2024new/images/page_15_chart_2.jpg]]
Fig. A.3. The normalized gap obtained by the matheuristic.

![[_papers/skalnes2024new/images/page_15_chart_4.jpg]]
Fig. A.4. Footprint analysis. Recommendation of which algorithm to use on a given subset of the instances.

## Sources

Primary source: `_papers/skalnes2024new/skalnes2024new-extracted.md` with the Zotero sidecar `_papers/skalnes2024new/skalnes2024new.md` (Zotero key H263I4LI, journalArticle, title "New benchmark instances for the inventory routing problem", publication European Journal of Operational Research, date 2024-03-16, DOI 10.1016/j.ejor.2023.08.010, creators Jørgen Skålnes, Mohamed Ben Ahmed, Lars Magnus Hvattum, Magnus Stålhane). The extracted header line calls the journal "Production, Manufacturing, Transportation and Logistics"; the sidecar DOI and publication point to EJOR, so the header line is treated as an OCR artifact.^[ambiguous] Figures 1, 2, 3, 4a, 5a, 5b, 6, 7, A.1, A.2, A.3, A.4 are embedded with verbatim captions; chart, table and equation crops not embedded in the page are not listed as sources. Tables 1-8 and B.1-B.4 with instance codes and bounds are in the extracted markdown; instances and best-known solutions are at the AXIOM project web page.

## Related

- [[references/pisinger2019-large-neighborhood-search]] - the LNS chapter covering Shaw's original LNS and ALNS, the framework the new IRP matheuristic line is compared against in structure.
- [[concepts/large-neighborhood-search]] - the destroy/repair neighborhood family that the matheuristic's five visit moves extend, with tabu search and MILP phases.
- [[concepts/phase-transition-instance-generation]] - the phase-transition threshold explanation the clustered IRP instances cross, with TSP cluster-ratio evidence.
- [[concepts/benchmark-instance-design]] - instance generation for benchmark sets, the family the new IRP set belongs to, with vehicle routing, liner shipping, tramp shipping, maritime inventory routing, Solomon R/RC positioning.
- [[concepts/branch-and-cut]] - the B&C method family this paper runs, with dynamic subtour separation, capacity and disjoint route inequalities, h-DR omission, 7,200-second limit.
