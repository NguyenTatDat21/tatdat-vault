---
title: 'Constraint Programming Models for the Parallel Drone Scheduling Vehicle Routing Problem'
category: references
tags: [vehicle-routing, drones, constraint-programming, cp-sat, lower-bounds, optimization]
relationships:
  - target: "[[references/nguyen2022-min-cost-pdsvrp]]"
    type: derived_from
  - target: "[[concepts/min-cost-parallel-drone-scheduling-vrp]]"
    type: implements
  - target: "[[concepts/pdsvrp-c]]"
    type: related_to
  - target: "[[references/montemanni2024-parallel-collective-drones]]"
    type: related_to
  - target: "[[concepts/collective-drone-delivery]]"
    type: related_to
sources:
  - _papers/montemanni2023constraint/montemanni2023constraint-extracted.md
  - _papers/montemanni2023constraint/montemanni2023constraint.md
  - _papers/montemanni2023constraint/images/page_3_image_2.jpg
  - _papers/montemanni2023constraint/images/page_3_image_3.jpg
summary: >-
  Two CP-SAT models per variant for min-time and min-cost PDSVRP: new best lower bounds on all tested instances, first bounds for min-cost benchmarks, several instances closed.
provenance:
  extracted: 0.82
  inferred: 0.13
  ambiguous: 0.05
base_confidence: 0.37
lifecycle: draft
lifecycle_changed: 2026-10-25
tier: supporting
created: 2026-10-25T10:55:07Z
updated: 2026-10-25T10:55:07Z
---

# Constraint Programming Models for the Parallel Drone Scheduling Vehicle Routing Problem

> [!tldr] Two constraint-programming models per PDSVRP variant — a 3-index per-truck model and a giant-tour 2-index model with time/weight counters — for the min-time (MT-PDSVRP) and min-cost (MC-PDSVRP) versions. Solved with CP-SAT, they produce new best lower bounds on every tested instance, the first lower bounds ever for the min-cost benchmarks, and close several instances for the first time.

## Problem & Contribution

- MT-PDSVRP (Parallel Drone Scheduling Multiple TSP, Mbiadou Saleu et al., EJOR 2022): fleet of homogeneous trucks (one route each) plus drones operating back-and-forth depot trips, one parcel per trip; drone-eligible set C^D ⊆ C limited by parcel weight, distance, terrain; objective is the makespan α, the time the last vehicle is back at the depot.
- MC-PDSVRP (Nguyen et al., EJOR 2022, min-cost PDSVRP): adds truck edge costs, drone mission costs, parcel weights w_i, truck capacity Q^T, and per-vehicle working-time caps τ^T, τ^D for load balancing; objective is total operational cost.
- Contribution: four CP models (MT-3IDX, MT-2IDX, MC-3IDX, MC-2IDX) exploiting Circuit / MultipleCircuit statements and cumulative counters, benchmarked against published branch-and-cut, branch-and-price, matheuristic and ruin&recreate results.
- ![[_papers/montemanni2023constraint/images/page_3_image_2.jpg]]
  ![[_papers/montemanni2023constraint/images/page_3_image_3.jpg]]
  "Figure 1: An example of an instance is provided on the left; we assume that two trucks and two drones are available (travel times are omitted for the sake of simplicity). A solution of the MT-PDSVRP is provided on the right. The black and blue arcs represent the tour of the two truck. The first visits nodes 2 and 3 before going back to the depot, the second visits nodes 6 and 7 and goes back to the depot. The dashed red arcs depict the missions of the first drone (that serves nodes 1 and 8), while the dashed green arcs depict the missions of the second drone (that serves nodes 4 and 5)."

## Method

MT-3IDX: per-truck binary arc variables z_kij with Circuit constraints (self-loop z_kii = 1 when truck k skips customer i), drone assignment x_di, and

$$\min\ \alpha\ \text{ s.t.}\ \alpha\ge\sum_{ij}t^T_{ij}z_{kij}\ \forall k,\qquad \alpha\ge\sum_i t^U_i x_{di}\ \forall d,\qquad \sum_d x_{di}+\sum_k \neg z_{kii}=1\ \forall i\in C^D$$

MT-2IDX: giant-tour y_ij with MultipleCircuit, Σ_j y_0j ≤ |T|, and time counters γ_0 = 0, y_ij ⇒ γ_j = γ_i + t^T_ij, y_i0 ⇒ α ≥ γ_i + t^T_i0 — fewer variables, more complex constraints.
^[inferred] The counter-with-implication pattern is the CP-specific mechanism that turns a single giant tour into per-truck makespan accounting.

MC models add objective Σ truck costs + Σ drone mission costs, working-time limits, and capacity: MC-3IDX uses Σ_j w_j z_kij ≤ Q^T; MC-2IDX uses weight counters β_0 = 0, y_ij ⇒ β_j = β_i + w_j, β_i ≤ Q^T.
^[inferred] The same counter mechanism carries capacity, which is what makes the giant-tour formulation work under capacity constraints.

## Results

Setup: Python 3.9, CP-SAT (Google OR-Tools 9.5.2237), i7-12700F 12 cores 32 GB; time limits 10800 s (CVRPLIB MT), 3600 s (TSPLIB MT), 1800 s (MC).

| Setting | Finding | Evidence (lines) |
|---|---|---|
| 20 CVRPLIB MT-PDSVRP instances (50–199 customers) | new improved lower bounds for all instances; 2 new best-known heuristic solutions; MT-3IDX tighter, MT-2IDX the only viable model on X-n139-k10 (LB 1118.67 vs HM 2492.00) | line 409 |
| TSPLIB MT-PDSVRP, 2 trucks (Raj et al. branch-and-price) | MT-3IDX gives all state-of-the-art LBs and best heuristics; five instances closed for the first time, e.g. att48 2T2D 16940.18*, eil101 2T2D 293.00* vs MH 305.40 | lines ~290–350 |
| TSPLIB MT-PDSVRP, 3 trucks | MT-3IDX degrades with more trucks, proves att48 3T2D 13452.00*; MT-2IDX finds two new best heuristics — indicated for more trucks | lines ~290–350 |
| MC-PDSVRP 30/50 customers | CP gives the first lower bounds ever; several closed, e.g. 30-r-1-c LB=UB=58.30*, 30-c-1-c 39.98*, 50-r-0-c 161.13* with LB 131.27 (MC-2IDX) | Tables 4–5 |
| MC-PDSVRP 100/200/400 customers | first LBs ever produced (e.g. 400-r-1-c LB 487.76 vs RR UB 578.77); MC-2IDX scales well for bounds, MC-3IDX often yields no bound | line 445 |

- Model preference reverses between variants: MT-3IDX wins on min-time, MC-2IDX wins on min-cost, attributed to the different objective and instance characteristics.

## Limitations

- Preprint (arXiv 2023), not peer-reviewed at time of publication.
- CP heuristic upper bounds do not consistently match the nine hybrid metaheuristics on the min-time benchmark; MC-2IDX often produces strong lower bounds with no feasible solution found within the time limit on large instances.
- Bounds quality degrades for very large instances (LB 0.00 for MT-2IDX on gr229; MC-3IDX unable to bound 400-customer instances).

## Related

- [[references/nguyen2022-min-cost-pdsvrp]] — the min-cost PDSVRP whose instances and model this paper adopts
- [[concepts/min-cost-parallel-drone-scheduling-vrp]] — the concept this paper's MC models formalize in CP
- [[concepts/pdsvrp-c]] — collective-drones variant built on these CP baselines
- [[references/montemanni2024-parallel-collective-drones]] — follow-up with collective drones, citing this preprint
- [[concepts/collective-drone-delivery]] — the collective-drones concept these CP baselines feed
- [[concepts/collective-drone-delivery]] — the collective-drones concept these CP baselines feed

## Bibliographic Record

- Citation key: `montemanni2023constraint`
- DOI: 10.48550/arXiv.2307.02980
- Canonical URL: http://arxiv.org/abs/2307.02980
- Publication: arXiv preprint, July 6, 2023 (submitted for publication)
- Authors: Roberto Montemanni, Mauro Dell'Amico
- Metadata companion: [[../_papers/montemanni2023constraint/montemanni2023constraint.md|montemanni2023constraint metadata]]

## Sources

- [[_papers/montemanni2023constraint/montemanni2023constraint-extracted.md]]
- [[_papers/montemanni2023constraint/montemanni2023constraint.md]]
- [[_papers/montemanni2023constraint/images/page_3_image_2.jpg]]
- [[_papers/montemanni2023constraint/images/page_3_image_3.jpg]]
