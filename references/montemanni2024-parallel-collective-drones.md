---
title: 'Parallel Drone Scheduling Vehicle Routing Problems with Collective Drones'
category: references
tags: [vehicle-routing, drones, cooperative-drones, constraint-programming, cp-sat, milp, valid-inequalities]
relationships:
  - target: "[[references/montemanni2023-cp-pdsvrp]]"
    type: extends
  - target: "[[concepts/parallel-drone-scheduling-traveling-salesman-problem]]"
    type: extends
  - target: "[[concepts/pdsvrp-c]]"
    type: related_to
  - target: "[[references/montemanni2024-pdsvrp-collective-drones]]"
    type: related_to
  - target: "[[concepts/collective-drone-delivery]]"
    type: related_to
  - target: "[[concepts/cp-sat-hint-start]]"
    type: related_to
  - target: "[[references/nguyen2023-pdstsp-collective-drones]]"
    type: related_to
sources:
  - _papers/montemanni2024parallel/montemanni2024parallel-extracted.md
  - _papers/montemanni2024parallel/montemanni2024parallel.md
  - _papers/montemanni2024parallel/images/page_3_image_0.jpg
  - _papers/montemanni2024parallel/images/page_15_chart_3.jpg
summary: >-
  First CP/MILP treatment of PDSVRP with collective drones: a workload-balancing valid inequality plus CP1-CP3 models give first-ever lower bounds on all PDSTSP-c and PDSVRP-c instances.
provenance:
  extracted: 0.8
  inferred: 0.15
  ambiguous: 0.05
base_confidence: 0.67
lifecycle: draft
lifecycle_changed: 2026-10-25
tier: core
created: 2026-10-25T10:55:07Z
updated: 2026-10-30T14:38:55Z
---

# Parallel Drone Scheduling Vehicle Routing Problems with Collective Drones

> [!tldr] [[concepts/collective-drone-delivery|Collective drones]] connect in flight to share a delivery: the connected drone carries more and flies faster. This paper adds a valid inequality to a CP model for the single-truck PDSTSP-c, then introduces PDSVRP-c (multiple trucks + collective drones) with two CP models and a MILP, producing first-ever lower bounds on every tested instance.

## Problem & Contribution

- PDSVRP: trucks (one route each, depot start/end) serve customers in parallel with drones, one parcel per drone mission. Collective drones allow drones to connect for one mission: the connected drone's maximum payload increases and the group flies at higher speed (a real configuration in the military/commercial literature, e.g. Paczan et al. 2016 patent).
- PDSTSP-c (single truck, Nguyen & Hà 2023): truck route covers some customers, drones cover the rest in collective missions of k ∈ {1,2,3} drones. New here: a valid inequality strengthening the CP model, plus the first multi-truck version PDSVRP-c, with two CP models and one MILP.
- ![[_papers/montemanni2024parallel/images/page_3_image_0.jpg]]
  "Figure 1: Example of solution of a PDSVRP-C with three trucks and five drones, including three clusters of two drones (drones 1 and 3; 2 and 4; 5)."
- ![[_papers/montemanni2024parallel/images/page_15_chart_3.jpg]]
  "Figure 2: The optimality gap in percentage for the MILP +(16) and CP1+(16) on small PDSTSP-c instances."

## Method

CP1 (PDSTSP-c baseline, CP-SAT): per-vehicle binary arc variables z_ijsk (truck k ∈ S) and x_ijd (drone d), aggregated arc counters y_ij, mission flow f_ij ∈ [0, m]:

$$\sum_j y_{ij}=\sum_j y_{ji}=1\ \forall i\in C,\qquad \sum_j z_{0jsk}=1\ \forall k\in S,\qquad m\,y_{ij}\ge\sum_{d}x_{ijd},\qquad T_j+M(1-y_{ij})\ge T_i+\sum_k \tau_j^k z_j^k$$

with Circuit constraints per vehicle, y_i0 ⇒ α ≥ T_i + t_i0^T, and the time counters T_j enforcing truck–drone synchronization. τ_j^k is the mission time when drone d launches at truck node i in a cluster of k drones.

The new valid inequality (16), balancing workload between truck and drones:

$$m\,\alpha\ \ge\ \sum_{j\in C_F}\sum_{k\in\mathbb{K}} k\,\tau_j^k\,z_j^k$$

where C_F is the set of customers served by drones; the RHS is the maximal total drone mission time, the LHS an upper bound on it. The paper notes it exposes mission times to the objective α (tightening the LP relaxation and propagating time variables) while failing to capture the waiting enforced by synchronization.
^[inferred] It is a workload-balance (max-makespan) bound, and is also what the collective speed/payload model feeds.

CP2 uses giant-tour counters T̄_j with per-node service times τ_j = Σ_k τ_j^k z_j^k under MultipleCircuit (effective when many tours are present); CP3 is the PDSVRP-c model with per-truck arc variables w_ij^k, a w_00^k unused-truck flag, and the coverage requirement that each customer is served by exactly one truck. The MILP has binary w_ij^k, u_j^k (cluster size at node j), truck time variables T_j with big-M synchronization, and exponential subtour-elimination inequalities generated dynamically as lazy constraints (O(|E|) scan per integer solution).

## Results

Setup: Python 3.11.2, CP-SAT (OR-Tools 9.6), Gurobi 10.0; PDSTSP-c instances from Nguyen & Hà (15–200 customers, m ∈ [3,6] small / [5,10] large), PDSVRP-c adds s trucks ∈ [2,3] small / [2,5] large; every table note lists a 3600 sec time limit for both Gurobi and CP-SAT; tables report [LB, UB], time to best heuristic, time to prove optimality.

| Scope | Finding | Evidence (lines) |
|---|---|---|
| Small PDSTSP-c | CP1+(16) closes all instances except three (20-c-c, 21-c-c, 26-r-c); e.g. 15-r-e [92, 92] in 0.84 s vs MILP 12.15 s | lines 610–625 |
| Inequality (16) | "very effective in improving performances of both CP1 and MILP" | line 625 |
| Large PDSTSP-c | valid lower bounds for all 30 instances for the first time; 10/30 bounds equal the best known solution, proving it optimal, e.g. 82-c-e [64, 64], 185-c-c [96, 96], 76-c-c [52, 52] | lines 639–653 |
| PDSVRP-c small | CP3 superior, closes all instances but one; MILP degrades with size (26-r-c closed by MILP [56, 56] in 180.88 s, not by CP) | lines 655–671 |
| PDSVRP-c large | CP2 beats CP3 on lower bounds; CP3 more consistent with many customers + few trucks (CP2 sometimes finds no feasible solution, e.g. 154-c-c CP2 LB 35, CP3 LB 8/UB 72) | lines 671, 677–714 |

- CP upper bounds are not competitive with the ruin&recreate metaheuristics, so CP is positioned as the bounds/reference tool; the paper flags scaling issues on large instances and room for tailored heuristics.
- Collective-speed model: optimal drone mission times for each cluster size are pre-calculated on literature instances (provided by Nguyen & Hà), so speed/payload trade-offs enter τ_j^k, not the model structure. ^[inferred]

## Limitations

- Running times are not comparable with metaheuristics: ruin&recreate reports best-of-30-runs, CP runs single 3600 s runs.
- Preprint version (the published COR 2024 article is the peer-reviewed record).
- The collective-drone configuration is modeled by pre-computed per-cluster mission times, not by an energy/geometry model of the connection itself. ^[inferred]
- Upper bounds lag dedicated heuristics; CP value here is bounds, heuristic solution quality, and modeling flexibility.

## Related

- [[references/montemanni2023-cp-pdsvrp]] — non-collective CP baselines this work extends
- [[concepts/pdsvrp-c]] — the problem introduced by this paper
- [[concepts/parallel-drone-scheduling-traveling-salesman-problem]] — single-truck family PDSTSP-c extends
- [[references/montemanni2024-pdsvrp-collective-drones]] — companion record of the same paper already in the vault

## Bibliographic Record

- Citation key: `montemanni2024parallel`
- DOI: 10.1016/j.cor.2023.106514
- Canonical URL: https://www.sciencedirect.com/science/article/pii/S0305054823003787
- Publication: Computers & Operations Research, March 2024
- Authors: Roberto Montemanni, Mauro Dell'Amico, Andrea Corsini
- Metadata companion: [[_papers/montemanni2024parallel/montemanni2024parallel.md|montemanni2024parallel metadata]]

## Sources

- [[_papers/montemanni2024parallel/montemanni2024parallel-extracted.md]]
- [[_papers/montemanni2024parallel/montemanni2024parallel.md]]
- [[_papers/montemanni2024parallel/images/page_3_image_0.jpg]]
- [[_papers/montemanni2024parallel/images/page_15_chart_3.jpg]]
