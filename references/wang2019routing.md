---
title: >-
  Path Planning for Triple Ecosystems in Diverse Environments (Wang, Hu, Du, Zhou, Deng, Hu, IEEE IoT-J 2019)
category: references
tags: [paper, uav, truck-drone, delivery, vrp, makespan, time-balancing, ellipse, flight-segment, dbscan, tabu-search, ils, clarke-wright, tsp, cvrp, energy-model, heuristics]
relationships:
  - target: "[[references/murray2015flying]]"
    type: related_to
  - target: "[[references/nguyen2023-pdstsp-collective-drones]]"
    type: related_to
  - target: "[[references/li2024drone]]"
    type: related_to
  - target: "[[references/lourenco2019iterated]]"
    type: uses
  - target: "[[concepts/hybrid-truck-drone-delivery]]"
    type: uses
  - target: "[[concepts/ellipse-based-flight-segment-geometry]]"
    type: uses
  - target: "[[concepts/uav-payload-bottleneck]]"
    type: uses
  - target: "[[concepts/drone-delivery-energy-and-range-parameters]]"
    type: uses
  - target: "[[concepts/vehicle-routing-with-synchronization-constraints]]"
    type: uses
  - target: "[[concepts/iterated-local-search]]"
    type: uses
  - target: "[[concepts/k-multi-visit-drone-routing-problem]]"
    type: uses
  - target: "[[concepts/tabu-search]]"
    type: uses
  - target: "[[concepts/lift-to-drag-ratio-power-efficiency-sensitivity]]"
    type: uses
  - target: "[[concepts/nonlinear-drone-energy-function-in-routing]]"
    type: uses
  - target: "[[concepts/collective-drone-delivery]]"
    type: uses
  - target: "[[concepts/min-cost-tsp-with-drone]]"
    type: uses
  - target: "[[concepts/parallel-drone-scheduling-traveling-salesman-problem]]"
    type: uses
  - target: "[[concepts/multirotor-power-model-components]]"
    type: uses
  - target: "[[concepts/metaheuristic-hybridization]]"
    type: uses
  - target: "[[concepts/drone-energy-consumption-model-taxonomy]]"
    type: uses
sources:
  - _papers/wang2019routing/wang2019routing.md
  - _papers/wang2019routing/wang2019routing-extracted.md
  - _papers/wang2019routing/images/page_1_image_3.jpg
  - _papers/wang2019routing/images/page_2_image_3.jpg
  - _papers/wang2019routing/images/page_3_image_8.jpg
  - _papers/wang2019routing/images/page_4_image_18.jpg
  - _papers/wang2019routing/images/page_6_image_3.jpg
  - _papers/wang2019routing/images/page_6_image_10.jpg
  - _papers/wang2019routing/images/page_6_image_12.jpg
  - _papers/wang2019routing/images/page_7_image_8.jpg
  - _papers/wang2019routing/images/page_7_image_10.jpg
  - _papers/wang2019routing/images/page_7_image_12.jpg
  - _papers/wang2019routing/images/page_8_image_3.jpg
  - _papers/wang2019routing/images/page_8_image_5.jpg
  - _papers/wang2019routing/images/page_9_image_3.jpg
  - _papers/wang2019routing/images/page_9_image_12.jpg
  - _papers/wang2019routing/images/page_10_chart_3.jpg
  - _papers/wang2019routing/images/page_10_chart_6.jpg
  - _papers/wang2019routing/images/page_10_chart_8.jpg
  - _papers/wang2019routing/images/page_11_chart_3.jpg
  - _papers/wang2019routing/images/page_11_chart_6.jpg
  - _papers/wang2019routing/images/page_11_chart_8.jpg
  - _papers/wang2019routing/images/page_12_chart_3.jpg
  - _papers/wang2019routing/images/page_12_chart_5.jpg
  - _papers/wang2019routing/images/page_12_chart_7.jpg
summary: >-
  HTDD: trucks launch drones on-line plus independent drones as third platform; ellipse flight segments, tabu+DBSCAN, global route time-balancing; beats PDSTSP and KGA, payload is bottleneck.
provenance:
  extracted: 0.89
  inferred: 0.10
  ambiguous: 0.01
base_confidence: 0.77
tier: core
lifecycle: source
lifecycle_changed: 2026-10-29T16:52:00Z
created: 2026-10-29T16:40:00Z
updated: 2026-10-30T14:08:41Z
---

# Path Planning for Triple Ecosystems in Diverse Environments (Wang, Hu, Du, Zhou, Deng, Hu, IEEE IoT-J 2019)

> [!tldr] This paper closes the gap between truck-only and drone-only delivery by embedding drones inside trucks: truck-carried routes are built from ellipse-based flight segments, and trucks plus independent drones are time-balanced into one fleet makespan. The three-step heuristic (CVRP tabu, DBSCAN clustering, global construction with ILS) beats PDSTSP and KGA on 100–500-customer instances, and payload, not battery, is the bottleneck factor. ^[extracted]

Published in IEEE Internet of Things Journal (December 2019), DOI 10.1109/JIOT.2019.2939397. The six authors are Desheng Wang, Peng Hu, Jingxuan Du, Pan Zhou, Tianping Deng and Menglan Hu (HUST, Wuhan; Pan Zhou is the corresponding author). The extracted sidecar renders the paper's name as "Path Planning for Triple Ecosystems in Diverse Environments" and the body renders it as "HTDD: Path Planning for Triple Ecosystems"; the sidecar title is used here verbatim. `^[ambiguous]`

![[_papers/wang2019routing/images/page_1_image_3.jpg]]
*Fig. 1. Illustration of the HTDD.*

*Fig. 1. Illustration of the HTDD.* — an urban area with 50 customers: a truck tour, drones launched from trucks at APs, independent drones from DCs, and two types of drones.

The problem is the Hybrid Truck-Drone Delivery Problem (HTDD) with three delivery platforms: trucks, drones that are carried and launched by trucks, and independent drones dispatched from DCs. Trucks act as moving launch stations: each truck carries multiple drones, a truck-carried drone flies out to customers and returns on the same arc back to the truck at a rendezvous Access Point (AP); a drone carries a payload to deliver goods, so the truck route is the backbone of the solution. Drones are assumed to fly in straight lines, the classic UAV assumption. ^[extracted] Each customer has a delivery demand, and a truck is capped by capacity $C_v$ and drone endurance $C_d$ (battery/charging).

The objective is the fleet makespan: the route cost is $Z = \min\{\max(T_{lu}, T_{vh})\}$ (eq. 14), where $T_{vh}$ is the truck tour time and $T_{lu}$ the independent-drone time; the truck-tour model with drones on it is the truck-constrained CVRP (T-CVRP), so the work reduces to balancing truck time against drone time, exactly the FSTSP/HTDD lineage. ^[extracted]

![[_papers/wang2019routing/images/page_2_image_3.jpg]]
*Fig. 2. The illustration of UAV payload bottleneck. The UAV payload is the main bottleneck factor for UAV delivery and a fully loaded UAV needs more energy for taking off.*

*Fig. 2. The illustration of UAV payload bottleneck.* — payload, endurance and battery weight interact: a fully loaded drone burns more energy for take-off, so battery weight trades against payload.

![[_papers/wang2019routing/images/page_3_image_8.jpg]]
*Fig. 3. UAVs are constrained by the payload and endurance. The UAVs are flying inside the circle, and the circle radius is equal to the UAV endurance.*

*Fig. 3. UAVs are constrained by the payload and endurance* — drones fly inside a circle of endurance radius, one drone serves multiple customers (multi-visit), drones can be carried by the truck, and independent drones come from DCs.

Energy is single-product payload energy: $W_{ij} = (w_d + G_i)\cdot d_{ij}\cdot P / (370\cdot\eta\cdot\gamma\cdot(P-e))$ (eq. 4) with $w_d$ the drone weight, $G_i$ payload, $P$ power demand, $\gamma$ lift-to-weight ratio, $\eta$ engine efficiency, $e$ motor efficiency. Payload, endurance, and speed set the battery life; the battery-weight tradeoff — more battery, less payload — is the key tradeoff for a UAV delivery platform. ^[extracted]

![[_papers/wang2019routing/images/page_4_image_18.jpg]]
*Fig. 4. UAV truck launching, truck-carried UAV, and the ellipse for the UAV segment.*

*Fig. 4. UAV truck launching, truck-carried UAV, and the ellipse for the UAV segment.* — the segment ellipse: two Access Points on the truck route as foci, customers on the arc, launch-recover arcs $d_{QA}$, $d_{QB}$, flight arc $d_{AB}$.

Truck-cardred drone segments are built from ellipse geometry: $d_{QA} + d_{QB} = D_{max}^{su}$ (eq. 19), $d_{AB} = \alpha\cdot D_{max}^{su}$ (eq. 20), $1 \geq \beta > \alpha > 0$; the segment length is $\beta\cdot D_{max}^{su}$, so the ellipse's major/minor axes grow as $\beta$ increases. Radius adaptation: one unvisited customer inside expands the ellipse, multiple unvisited customers inside expand the ellipse, multiple customers inside the ellipse split the segment. ^[extracted]

![[_papers/wang2019routing/images/page_6_image_3.jpg]]
*Fig. 6. The illustration of the segment radius adaptation.*

*Fig. 6. The illustration of the segment radius adaptation.* — segment radius adaptation: single customer, single customer, and multiple customers inside the ellipse.

![[_papers/wang2019routing/images/page_6_image_10.jpg]]
*Fig. 6. The illustration of UAV customers redistribution.*

*Fig. 6. The illustration of UAV customers redistribution.* — customer redistribution: customers that enter the truck route are redistributed, customers that exit the truck route are redistributed.

![[_papers/wang2019routing/images/page_6_image_12.jpg]]
*Fig. 6. The illustration of customer redistribution for segment.*

*Fig. 6. The illustration of customer redistribution for segment.* — customer redistribution inside a segment: customer 1 and 2, customer 3 and 4, customer 5 and 6, segment node is the insertion location for min-cost.

![[_papers/wang2019routing/images/page_7_image_8.jpg]]
*Fig. 7. The illustration of segment route construction.*

![[_papers/wang2019routing/images/page_7_image_10.jpg]]
*Fig. 7. The illustration of UAV-exclusion for segment.*

![[_papers/wang2019routing/images/page_7_image_12.jpg]]
*Fig. 7. The illustration of the segment node abstraction.*

![[_papers/wang2019routing/images/page_8_image_3.jpg]]
*Fig. 8. The illustration of the route construction.*

![[_papers/wang2019routing/images/page_8_image_5.jpg]]
*Fig. 8. The illustration of the global route construction.*

![[_papers/wang2019routing/images/page_9_image_3.jpg]]
*Fig. 9. The illustration of time balancing.*

![[_papers/wang2019routing/images/page_9_image_12.jpg]]
*Fig. 9. The illustration of step 3.*

![[_papers/wang2019routing/images/page_10_chart_3.jpg]]
*Fig. 10. The illustration of time balancing.*

![[_papers/wang2019routing/images/page_10_chart_6.jpg]]
*Fig. 10. The illustration of step 1.*

![[_papers/wang2019routing/images/page_10_chart_8.jpg]]
*Fig. 10. The illustration of step 2.*

![[_papers/wang2019routing/images/page_11_chart_3.jpg]]
*Fig. 11. The illustration of step 3.*

![[_papers/wang2019routing/images/page_11_chart_6.jpg]]
*Fig. 11. The illustration of the global route construction.*

![[_papers/wang2019routing/images/page_11_chart_8.jpg]]
*Fig. 11. The illustration of the segment node abstraction.*

![[_papers/wang2019routing/images/page_12_chart_3.jpg]]
*Fig. 12. The illustration of the segment reroute.*

![[_papers/wang2019routing/images/page_12_chart_5.jpg]]
*Fig. 12. The illustration of the global route construction.*

![[_papers/wang2019routing/images/page_12_chart_7.jpg]]
*Fig. 12. The illustration of time balancing.*

## Algorithm

HTDD is solved by a 3-step pipeline: a truck route from the CVRP, clusters of truck-carried drone customers, global routes for independent drones, and a time-balancing pass that shifts customers between trucks and drones to cut the makespan. Step 1 builds the initial truck route by solving the CVRP with Clarke-Wright savings plus a tabu search that uses inter-route interpolation, inter-route exchange, inter-route 2-opt*, and intra-route 2-opt. ^[extracted]

![[_papers/wang2019routing/images/page_6_image_3.jpg]]
*Fig. 6. The illustration of the segment radius adaptation.*

![[_papers/wang2019routing/images/page_6_image_10.jpg]]
*Fig. 6. The illustration of UAV customers redistribution.*

![[_papers/wang2019routing/images/page_6_image_12.jpg]]
*Fig. 6. The illustration of customer redistribution for segment.*

![[_papers/wang2019routing/images/page_7_image_8.jpg]]
*Fig. 7. The illustration of segment route construction.*

![[_papers/wang2019routing/images/page_7_image_10.jpg]]
*Fig. 7. The illustration of UAV-exclusion for segment.*

![[_papers/wang2019routing/images/page_7_image_12.jpg]]
*Fig. 7. The illustration of the segment node abstraction.*

![[_papers/wang2019routing/images/page_8_image_3.jpg]]
*Fig. 8. The illustration of the route construction.*

![[_papers/wang2019routing/images/page_8_image_5.jpg]]
*Fig. 8. The illustration of the global route construction.*

![[_papers/wang2019routing/images/page_9_image_3.jpg]]
*Fig. 9. The illustration of time balancing.*

![[_papers/wang2019routing/images/page_9_image_12.jpg]]
*Fig. 9. The illustration of step 3.*

![[_papers/wang2019routing/images/page_10_chart_3.jpg]]
*Fig. 10. The illustration of time balancing.*

![[_papers/wang2019routing/images/page_10_chart_6.jpg]]
*Fig. 10. The illustration of step 1.*

![[_papers/wang2019routing/images/page_10_chart_8.jpg]]
*Fig. 10. The illustration of step 2.*

![[_papers/wang2019routing/images/page_11_chart_3.jpg]]
*Fig. 11. The illustration of step 3.*

![[_papers/wang2019routing/images/page_11_chart_6.jpg]]
*Fig. 11. The illustration of the global route construction.*

![[_papers/wang2019routing/images/page_11_chart_8.jpg]]
*Fig. 11. The illustration of the segment node abstraction.*

![[_papers/wang2019routing/images/page_12_chart_3.jpg]]
*Fig. 12. The illustration of the segment reroute.*

![[_papers/wang2019routing/images/page_12_chart_5.jpg]]
*Fig. 12. The illustration of the global route construction.*

![[_papers/wang2019routing/images/page_12_chart_7.jpg]]
*Fig. 12. The illustration of time balancing.*


## Experiment & results

The evaluation is a Java simulator with 50 iterations per instance, a drone weighing 2 kg with 3 kg payload, max flight distance 7 km, truck operating cost 0.484 per km, customers 100–500, truck capacity 100–1000 (tested at 300 customers), and UAV endurance sweeps. Baselines are truck-only delivery, truck-launched drone delivery, and independent drone delivery, matching the PDST/FSTSP and KGA baselines. ^[extracted] The reported axes are total time, truck distance, and UAV distance, matching the figures' (a) time cost, (b) distance cost of the trucks, (c) distance cost of drones. ^[extracted]

HTDD beats all baselines: lower total time, shorter truck distance, shorter UAV distance. ^[extracted] Truck distance cost rises when UAV max flight distance exceeds 5 km — the payload bottleneck takes over: more payload means battery weight tradeoff, so the truck carries more work. ^[extracted] HTDD is less sensitive to battery capacity than the baselines. ^[extracted] The time-balancing pass reallocates customers from drones to trucks until truck time exceeds drone time, so the makespan is pulled down by balancing $T_{lu}$ against $T_{vh}$. ^[extracted]

*Fig. 15(a) Time cost.*
*Fig. 15(b) Distance cost of the trucks.*
*Fig. 15(c) Distance cost of drones.*
*Fig. 16(a) Time cost.*
*Fig. 16(b) Distance cost of the trucks.*
*Fig. 16(c) Distance cost of drones.*
*Fig. 17(a) Time cost.*
*Fig. 17(b) Distance cost of the trucks.*
*Fig. 17(c) Distance cost of drones.*

- [[concepts/drone-delivery-energy-and-range-parameters]] — the energy model of this paper, eq. 4. ^[extracted]
- [[concepts/uav-payload-bottleneck]] — the paper's finding that payload, not battery, gates truck-launched UAV delivery. ^[extracted]
- [[concepts/ellipse-based-flight-segment-geometry]] — the ellipse segment geometry, eq. 19-20, used to build truck-carried UAV routes. ^[extracted]
- [[concepts/hybrid-truck-drone-delivery]] — the HTDD model, three delivery platforms in one fleet. ^[extracted]
- [[concepts/vehicle-routing-with-synchronization-constraints]] — truck/UAV rendezvous at APs, the launch-recover arc constraint. ^[extracted]
- [[concepts/drone-energy-consumption-model-taxonomy]] — the eq. 4 payload-weighted energy model used for the DCVRP routing independent drones from DCs. ^[extracted]
- [[concepts/k-multi-visit-drone-routing-problem]] — the multi-visit UAV setting, drones carry multiple deliveries inside one endurance circle. ^[extracted]
- [[concepts/lift-to-drag-ratio-power-efficiency-sensitivity]] — the lift-ratio and efficiency coefficients of eq. 4. ^[extracted]
- [[concepts/nonlinear-drone-energy-function-in-routing]] — payload-weighted distance as the energy function. ^[extracted]
- [[concepts/collective-drone-delivery]] — fleet of many drones cooperating to deliver, the PDSTSP setting. ^[extracted]
- [[concepts/min-cost-tsp-with-drone]] — segment loops modeled as TSP paths, greedy UAV-exclusion loop. ^[extracted]
- [[concepts/parallel-drone-scheduling-traveling-salesman-problem]] — parallel drone scheduling TSP lineage: truck route plus drone arcs. ^[extracted]
- [[concepts/multirotor-power-model-components]] — the power demand P, lift ratio γ, efficiency η/e inputs of eq. 4. ^[extracted]
- [[concepts/metaheuristic-hybridization]] — Clarke-Wright + tabu + DBSCAN + ILS combined in one pipeline. ^[extracted]
- [[references/murray2015flying]] — the FSTSP baseline (PDSTSP, Murray & Chu) HTDD compares against. ^[extracted]
- [[references/nguyen2023-pdstsp-collective-drones]] — the collective-drone PDSTSP lineage this paper is built on. ^[extracted]
- [[references/li2024drone]] — the internal/external capability survey framing reused by this paper. ^[extracted]
- [[references/lourenco2019iterated]] — ILS framework for the ILS pass used inside the heuristic. ^[extracted]
- [[concepts/tabu-search]] — tabu moves used for the tabu-search steps, and the ILS with tabu acceptance. ^[extracted]
- [[concepts/iterated-local-search]] — ILS inter-route insertion, swap, 2-opt*, segment-node abstraction reroute, acceptance by max(T_lu,T_v) improvement. ^[extracted]

## Sources

- `_papers/wang2019routing/wang2019routing.md`
- `_papers/wang2019routing/wang2019routing-extracted.md`
