---
title: >-
  Hybrid Truck-Drone Delivery (HTDD): trucks plus truck-carried drones plus independent drones
category: concepts
tags: [UAV, truck-drone, delivery, VRP, makespan, time-balancing, multi-visit, hybrid]
relationships:
  - target: "[[references/wang2019routing]]"
    type: related_to
  - target: "[[references/murray2015flying]]"
    type: related_to
  - target: "[[concepts/ellipse-based-flight-segment-geometry]]"
    type: uses
  - target: "[[concepts/uav-payload-bottleneck]]"
    type: uses
  - target: "[[concepts/vehicle-routing-with-synchronization-constraints]]"
    type: related_to
  - target: "[[concepts/k-multi-visit-drone-routing-problem]]"
    type: related_to
  - target: "[[concepts/collective-drone-delivery]]"
    type: related_to
summary: >-
  Three-platform delivery fleet: trucks, drones launched from trucks, independent drones from DCs, time-balanced into one makespan.
provenance:
  extracted: 0.88
  inferred: 0.12
  ambiguous: 0.0
base_confidence: 0.67
tier: core
lifecycle: draft
lifecycle_changed: 2026-10-29
created: 2026-10-29T16:44:00Z
updated: 2026-10-29T16:44:00Z
sources:
  - _papers/wang2019routing/wang2019routing-extracted.md
---

# Hybrid Truck-Drone Delivery (HTDD): trucks plus truck-carried drones plus independent drones

> [!tldr] The three delivery platforms of HTDD: trucks that carry drones, drones launched from a truck at access points, and independent drones dispatched from DCs, all time-balanced into a single fleet makespan. ^[extracted]

HTDD is the triple-platform delivery model formalized by Wang et al. 2019. ^[extracted] Each truck carries multiple drones, and a truck-carried drone flies out to customers and returns on the same arc back to the truck at a rendezvous access point (AP). ^[extracted] The drone is a pure delivery vehicle: it carries a payload, delivers goods, then flies back empty to meet the truck. ^[extracted] The independent drones are dispatched from DCs, inside a circle of radius equal to UAV endurance, and carry multiple deliveries per tour. ^[extracted]

The fleet objective is the makespan `Z = min{max(T_lu, T_vh)}`, truck tour time versus independent-drone time; the time-balancing pass reallocates customers from drones to trucks until truck time exceeds drone time, so the makespan falls as the two sides are balanced. ^[extracted] The truck route is built from the truck-constrained CVRP (T-CVRP), and independent-drone routes from the distance-constrained CVRP. ^[extracted] Truck/UAV rendezvous arcs are synchronization constraints, so the model is in the FSTSP/PDSTSP lineage: the truck is the backbone of the route, drones are the multi-visit platforms. ^[extracted]

The heuristic pipeline is Clarke-Wright plus tabu search for the CVRP, DBSCAN clustering of truck-carried drone customers with `Eps = D_max^su`, ellipse-based flight segment construction, global route construction, and ILS with time-balancing. ^[extracted] Results on 100–500 customers show HTDD beating truck-only, truck-carried, and independent-drone baselines, PDSTSP and KGA. ^[extracted] The model is in the FSTSP/PDSTSP lineage: trucks carry drones, drones as multi-visit platforms, the truck route as the backbone. ^[inferred]

## Related

- [[references/wang2019routing]] — the HTDD paper (Wang, Hu, Du, Zhou, Deng, Hu, IEEE IoT-J 2019). ^[extracted]
- [[references/murray2015flying]] — FSTSP, the single-truck drone-delivery lineage HTDD extends. ^[extracted]
- [[concepts/ellipse-based-flight-segment-geometry]] — the segment geometry HTDD uses for truck-carried drone routes. ^[extracted]
- [[concepts/uav-payload-bottleneck]] — the finding that payload, not battery, is the bottleneck factor. ^[extracted]
- [[concepts/vehicle-routing-with-synchronization-constraints]] — launch-recover arcs as synchronization constraints. ^[extracted]
- [[concepts/k-multi-visit-drone-routing-problem]] — the multi-visit single-truck family. ^[extracted]
- [[concepts/collective-drone-delivery]] — collective drones as the independent platform. ^[extracted]
- [[concepts/parallel-drone-scheduling-traveling-salesman-problem]] — parallel scheduling lineage: truck route plus drone arcs. ^[extracted]

## Sources

- [[_papers/wang2019routing/wang2019routing-extracted]]
