---
title: "Sacramento, Pisinger, Ropke: An adaptive large neighborhood search metaheuristic for the vehicle routing problem with drones (Transportation Research Part C, 2019)"
summary: "VRP-D: homogeneous truck fleet with one drone per truck, 31-constraint MIP minimizes cost, ALNS with 2 destroy and 4 repair methods beats truck-only by 20-30%."
type: reference
tags: [paper, vrp, drones, alns, truck-drone-cooperation, cost-minimization, mip, metaheuristic, endurance-utilization, sensitivity-analysis]
provenance:
  extracted: 0.97
  inferred: 0.02
  ambiguous: 0.01
base_confidence: 0.67
created: 2026-10-28T14:56:00Z
updated: 2026-10-30T19:12:06Z
tier: core
category: references
lifecycle: source
lifecycle_changed: 2026-10-29T17:15:00Z
sources:
  - "[[_papers/sacramento2019adaptive/sacramento2019adaptive-extracted.md]]"
  - "[[_papers/sacramento2019adaptive/sacramento2019adaptive.md]]"
  - "[[_papers/sacramento2019adaptive/images/page_2_image_4.jpg]]"
  - "[[_papers/sacramento2019adaptive/images/page_7_image_3.jpg]]"
  - "[[_papers/sacramento2019adaptive/images/page_14_image_1.jpg]]"
  - "[[_papers/sacramento2019adaptive/images/page_14_image_2.jpg]]"
  - "[[_papers/sacramento2019adaptive/images/page_14_image_6.jpg]]"
  - "[[_papers/sacramento2019adaptive/images/page_14_image_8.jpg]]"
  - "[[_papers/sacramento2019adaptive/images/page_19_image_2.jpg]]"
  - "[[_papers/sacramento2019adaptive/images/page_23_image_0.jpg]]"
  - "[[_papers/sacramento2019adaptive/images/page_30_chart_1.jpg]]"
  - "[[_papers/sacramento2019adaptive/images/page_31_chart_0.jpg]]"
  - "[[_papers/sacramento2019adaptive/images/page_31_image_4.jpg]]"
  - "[[_papers/sacramento2019adaptive/images/page_32_image_0.jpg]]"
  - "[[_papers/sacramento2019adaptive/images/page_45_image_2.jpg]]"
  - "[[_papers/sacramento2019adaptive/images/page_46_chart_2.jpg]]"
  - "[[_papers/sacramento2019adaptive/images/page_47_chart_2.jpg]]"
relationships:
  - target: "[[references/murray2015flying]]"
    type: related_to
  - target: "[[concepts/large-neighborhood-search]]"
    type: related_to
  - target: "[[concepts/simulated-annealing-metropolis-cooling]]"
    type: related_to
  - target: "[[references/santini2018-alns-acceptance-criteria]]"
    type: related_to
  - target: "[[references/ropke2006-adaptive-large-neighborhood-search-pdptw]]"
    type: related_to
  - target: "[[concepts/min-cost-tsp-with-drone]]"
    type: related_to
  - target: "[[concepts/collective-drone-delivery]]"
    type: related_to
  - target: "[[concepts/adaptive-large-neighborhood-search-for-mip]]"
    type: related_to
  - target: "[[concepts/bilevel-vrpd-task-assignment-routing]]"
    type: related_to
  - target: "[[concepts/k-multi-visit-drone-routing-problem]]"
    type: related_to
  - target: "[[concepts/min-cost-parallel-drone-scheduling-vrp]]"
    type: related_to
  - target: "[[concepts/pdsvrp-c]]"
    type: related_to
  - target: "[[concepts/vehicle-routing-with-synchronization-constraints]]"
    type: related_to
  - target: "[[references/windrasmara2022-alns-multi-drop-fstsp]]"
    type: related_to

---

> [!tldr] Truck + one drone per truck, cost minimization, ALNS with 4 repair methods, 20-30% savings against the truck-only case, endurance beyond 15 minutes hardly matters, speed is not a determining factor, payload is the lever with the clearest gains.

## Problem and formulation

The paper formulates the Vehicle Routing Problem with Drones (VRP-D): a homogeneous fleet of driver-operated trucks, each equipped with a single UAV, is based at one depot, every customer is served exactly once by truck or by the drone coordinated with its truck, drone delivery is one customer per sortie because of payload limits, and the objective is the total operation cost. The drone is transported by the truck when not flying, is launched and recovered at customer locations multiple times along the route, and has launch time SL and recovery time SR. Trucks have a capacity and a maximum route duration T_max of 8 hours. The MIP extends Murray and Chu's Flying Sidekick formulation with a truck index on every variable, uses 27 binary variables and 31 constraints, and excludes depot-to-depot drone flights so the truck and drone never depart the depot together. The big-M value is the number of nodes, the worst case of one truck visiting all customers.^[inferred] The objective is cost, not completion time, so driver cost is neglected because it is paid by fixed contract; drone-arc costs are symmetric and load-independent because real data are unavailable.^[inferred]

Constraints 2, 7-8, 9, 10-11, 20-23, 24, 27 enforce single visits, truck subtour elimination, capacity, one launch and one recovery per node, time synchronization of truck and drone at launch and recovery, battery endurance, and the rule that no new launch occurs while a drone is in the air. Figures 3-6 visualize the four prohibited moves the formulation excludes: the truck cannot wait for the drone at the launch customer, the drone cannot start and end at the depot alone, new launches cannot occur before recovery, and a launch cannot occur inside an in-flight sortie.

## Parameter set (Table 1)

Launch time 1 minute and recovery time 1 minute from Murray and Chu, truck speed 35 mph, drone speed 50 mph, endurance 30 minutes, truck capacity with drones 1300 kg, truck capacity without drones 1400 kg, drone capacity 5 kg, fuel price 1.13 euros per liter, fuel consumption 0.07 liters per km, miles converter 1.61 km per mile, drone factor cost 10% (Workhorse electricity cost of 2 cents per mile corresponds to 10-15% of truck cost), maximum route duration 8 hours. Distances are Euclidean, travel time is distance divided by constant speed, truck cost is fuel price times consumption times converter times distance, drone cost is alpha times truck cost.

## ALNS design

The ALNS follows Ropke and Pisinger 2006: destroy and repair methods selected by roulette wheel, weights updated with reaction factor 0.9 and scores 33 for a new global best, 9 for an accepted better solution, 13 for an accepted worse solution, 0 for a rejected one. Acceptance is simulated-annealing style, exp((f(s)-f(s'))/T), with a temperature decreasing linearly to zero over the elapsed CPU time, following Santini et al. 2018; parameters are initial temperature factor 0.004 times the initial solution value (10% higher for small instances), destruction degree 0.15, noImpvMax 1000.

Destroy methods have fixed equal probability, adaptivity is reserved to the repair side: random destroy removes customers, and removing a launch or recovery customer removes its drone customers; cluster destroy removes customers around a random seed, each step choosing randomly among the two closest customers to the seed in the partial solution, with the same cascade. The number removed is min(max(random 1-3, delta times customers), 40).

Repair methods: greedy truck-first sortie-second (best insertion for truck visits, then FindSortie), nearby-area truck-first sortie-second (random insertion within a 5-mile area, sortie chosen randomly among those within 10% of the cost before removal, a weaker version beneficial for small instances), closest insertion (insert only in the route containing the nearest customer, leftovers repaired by the first method), heavy insertion (customers above drone capacity first, then close insertion). FindSortie scans route pairs with launch position i before recovery position k, checks that launch, recovery, flight and service fit in the endurance, and keeps the cheapest sortie under the cost threshold.

The initial solution is built in three phases: nearest-neighbor truck routes with capacity and time checks, relocation local search, then drone insertion via FindSortie repeated until no saving remains; a string-relocation neighborhood cleans crosses that single relocation cannot fix, using strings that must not start or end inside an active sortie. Java implementation, CPLEX 12.7, Huawei XH620 server.

## Results: small instances (Table 3) and 112 instances (Table 4)

36 small instances with 6, 10, 12 customers in 5x5, 10x10, 20x20 grids. The ALNS reaches the CPLEX optimum in every one of 10 runs at 5 minutes CPU limit: mean equals the optimum, standard deviation zero, gap zero. CPLEX time grows steeply: 0.926 s for 06.05.1, 7479 s for 06.10.1, 62131 s for 12.05.2, 3723 s for 12.20.1, 1335 s for 12.20.4. The prose claims nearly 17 hours for instance 12.05.1, Table 3 gives 1161.880 s for 12.05.1 and 62131.170 s for 12.05.2; the 17-hour figure matches the 12.05.2 row.^[ambiguous] The truck-only benchmark comes from Pisinger and Ropke 2007 with drone material removed and capacity 1400 kg. Savings over the truck-only case sit in the 20-30% range, sometimes above, the initial solution is improved by 15-25%, small instances vary most because one or two heavy customers placed far from the depot can kill the saving. Savings range from 17.40% (10.5.1) to 58.37% (6.10.3), from 15.79% (50.10.1) to 32.48% (50.10.4), from 21.27% (200.30.2) to 26.95% (200.40.1). The objective estimates fuel cost only, driver wages are not included.

Average drone usage: the number of customers served by drones grows linearly with customer count, reaching about 50% of potential drone customers; a route with n_t truck visits launches at most n_t+1 drones, so an n-customer instance admits at most 2n/3 sorties with n/3 trucks. Endurance use decreases with instance size, and no more than 60% of the battery time is consumed between launch and recovery. The 12.10.4 instance reaches 47.88% saving, 20.20.3 31.21%, 100.10.1 32.66%, 150.20.2 31.24%, 200.40.1 26.95% with 172 customers, 200.40.2 22.56% with 178.

## Sensitivity: cost, endurance, speed, payload

Scenarios 100, 150, 200, 250 customers on the 30x30 grid probe four drone parameters. Drone-arc cost: savings shrink as cost rises, become negligible at 50% of truck cost, and sorties fall; for a fixed cost the saving against customer count has a bell-like shape, because customers spread in a large area make sorties hard, mid-density makes them easy, saturation reduces the saving per customer; the 5-minute limit also degrades quality for larger instances.

Endurance: 5 minutes gives negative savings because launch, recovery and service take 3 minutes leaving 2 minutes of flight, the instances turn into truck-only VRP and the VRP-D heuristic loses to the truck-only heuristic; endurance beyond 15 minutes barely moves the objective, because heavy customers force truck visits, launch and recovery customers must differ, and long sorties are expensive. Average sorties at 30 minutes are 45.008, 67.320, 86.896, 108.056 for the four scenarios, endurance utilization 38.20%, 33.19%, 29.97%, 28.41%; 60 minutes leaves the objective nearly unchanged.

Speed: savings grow monotonically, above 20% even at 25 mph, sorties stay stable, endurance utilization drops from 57.93% at 25 mph to 31.81% at 75 mph, so speed is not a determining factor. The 25 mph curve lacks the bell shape, likely from only 25 samples.

Payload: raising capacity from 1 kg to 5 kg covers 34.80% to 86.72% of customers, at 20 kg 90.16% and unlimited 100%, so savings rise clearly; 2 kg versus 20 kg in one instance gives 12.660 versus 10.511, with 56% of customers below 2 kg and 88% below 20 kg, a 32% increase in potential drone customers.

## Clustered instances and appendix C

10 clustered instances 150.30.c.01-10, 30x30 grid, 1 to 5 focal points, customers normal-distributed around the focal point with 2-mile standard deviation, behave like uniform instances with lower standard deviation; clusters split the problem into subproblems, and routes combine clusters when focal points are close. Savings span 22.16% (4 focal points) to 40.62% (2 focal points, 10.3291 cost), the best and worst columns. The average number of routes does not match the number of focal points, and the paper suggests cluster-specialized repair methods. Appendix C runs 375 instances in 15 scenarios of 25: the bell-like shape recurs per grid size, the 50-customer 30x30 case averages a higher saving than the 100-customer case, halving endurance to 15 minutes drops the saving significantly, especially for few customers in large grids, and variance decreases.

The conclusion states that endurance must be significantly reduced below 30 minutes to affect solutions, speed is not a determining factor, benefits stay above 20% below truck speed, payload increase reduces fuel cost more easily and creates more potential drone customers, avoiding dispatching a truck to remote customers. Future work: the dynamic case, Dantzig-Wolfe decomposition, and allowing the truck to wait at the launch location as in Agatz et al. 2015, enabling multiple launches from the same location.

## Figures

![[_papers/sacramento2019adaptive/images/page_2_image_4.jpg]]
Figure 1: Example of a delivery drone. Photo by Sam Churchill.

![[_papers/sacramento2019adaptive/images/page_7_image_3.jpg]]
Figure 2: Example of a VRP-D solution. The solid lines indicate the route of the trucks, while the dashed lines indicate the trips of the drones. Filled circle nodes represent customers that, due to a heavy delivery, can only be visited by the truck and emptied circle nodes represent customers that can be visited by either the truck or the drone. Triangle nodes corresponds to drone visits in the solution.

![[_papers/sacramento2019adaptive/images/page_14_image_1.jpg]]
Figure 3: Prohibited move of the UAV for the launch and recovery operation.

![[_papers/sacramento2019adaptive/images/page_14_image_2.jpg]]
Figure 4: Prohibited move of the independently operation of the UAV.

![[_papers/sacramento2019adaptive/images/page_14_image_6.jpg]]
Figure 5: Prohibited move of new launches.

![[_papers/sacramento2019adaptive/images/page_14_image_8.jpg]]
Figure 6: Prohibited move of new launches within a sortie.

![[_papers/sacramento2019adaptive/images/page_19_image_2.jpg]]
Figure 7: Example of the String Relocation algorithm in the same route (top) and in another route (bottom). On the left, there is the initial solution after the first three steps and on the right, there is the initial solution improved after the string relocation algorithm.

![[_papers/sacramento2019adaptive/images/page_23_image_0.jpg]]
Figure 8: Example of Greedy truck-first and sortie-second repair method in the algorithm. The solid lines indicate the route of the trucks, while the dashed lines indicate the trips of the drones. Filled circle nodes represent customers that can only be visited by the truck and circle nodes represent customers that can be visited by either the truck or the drone. Triangle nodes corresponds to drone visits in the solution.

![[_papers/sacramento2019adaptive/images/page_30_chart_1.jpg]]
Figure 10: Average saving of the best known solution with respect to the initial solution and to the truck-only case per instance.

![[_papers/sacramento2019adaptive/images/page_31_chart_0.jpg]]
Figure 11: Average number of sorties and average sortie endurance utilization per instance.

![[_papers/sacramento2019adaptive/images/page_31_image_4.jpg]]
Figure 12: Best known solution for the VRP-D and VRP for an instance with 20 customers. The solid lines indicate the route of the trucks, while the dashed lines indicate the trips of the drones.

![[_papers/sacramento2019adaptive/images/page_32_image_0.jpg]]
Figure 13: Best known solution for the VRP-D and VRP for an instance with 100 customers. The solid lines indicate the route of the trucks, while the dashed lines indicate the trips of the drones.

![[_papers/sacramento2019adaptive/images/page_45_image_2.jpg]]
Figure 19: Instance 150.30.c.10, where customers are located between three clusters around the distribution center. The solid lines indicate the route of the trucks, while the dashed lines indicate the trips of the drones.

![[_papers/sacramento2019adaptive/images/page_46_chart_2.jpg]]
Figure 20: Distribution of the saving obtained by serving the customers using a mixed truck/drone approach compared to using a truck-only approach (SVRP) for different scenarios. The average saving for each scenario is marked with a cross.

![[_papers/sacramento2019adaptive/images/page_47_chart_2.jpg]]
Figure 21: Distribution of the saving obtained by serving the customers using a mixed truck/drone approach compared to using a truck-only approach (SVRP) for different scenarios, when considering 15 minutes of total endurance time. The average saving for each scenario is marked with a cross.

## Sources

Primary source: `_papers/sacramento2019adaptive/sacramento2019adaptive-extracted.md` with the Zotero sidecar `_papers/sacramento2019adaptive/sacramento2019adaptive.md` (Zotero key XP2IP9T4, journalArticle, title "An adaptive large neighborhood search metaheuristic for the vehicle routing problem with drones", publication Transportation Research Part C: Emerging Technologies, date 2019-05-01, DOI 10.1016/j.trc.2019.02.018). Figures 1, 2, 3, 4, 5, 6, 7, 8, 10, 11, 12, 13, 19, 20, 21 are embedded with verbatim captions; equation, table and chart crops not embedded in the page are not listed as sources. Instances are public at Zenodo, DOI 10.5281/zenodo.2572764.

## Related

- [[references/murray2015flying]] - the Flying Sidekick TSP this VRP-D MIP extends, with time minimization, single truck and single drone, and the PDSTSP fleet variant.
- [[references/windrasmara2022-alns-multi-drop-fstsp]] — multi-drop FSTSP ALNS; uses Sacramento's drone-cost ≈ 10 % of truck for its managerial cost model.
- [[concepts/large-neighborhood-search]] - Shaw's LNS and the ALNS framework of Ropke & Pisinger 2006 that supplies the destroy/repair, roulette-wheel weight update and score scheme.
- [[concepts/simulated-annealing-metropolis-cooling]] - the acceptance criterion the ALNS borrows; here the temperature is time-linear, ending at zero.
- [[references/santini2018-alns-acceptance-criteria]] - the source of the linear temperature schedule, the criterion that wins among nine ALNS acceptance criteria on CVRP, CMST and QAP.
- [[references/ropke2006-adaptive-large-neighborhood-search-pdptw]] - the ALNS template whose adaptive weights, scores and reaction factor are taken from Ropke & Pisinger 2006.
- [[concepts/min-cost-tsp-with-drone]] - the cost-minimizing TSP-D of Ha et al. 2018, the closest cost-objective sibling to this truck-fleet model.
- [[concepts/collective-drone-delivery]] - collective, synchronization-free drone delivery is the PDSTSP-style line the paper reviews as fleet-scale work.
- [[concepts/payload-induced-drone-battery-consumption-rate]] - the payload-energy trade the VRP-D paper predicts as future work, with a factor for load affecting speed and endurance.
- [[references/ha2018-min-cost-tsp-d]] - Ha et al. 2018, the cost-minimizing TSP-D.
