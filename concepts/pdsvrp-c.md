---
title: >-
  PDSVRP-c (Parallel Drone Scheduling Vehicle Routing Problem with Collective Drones)
category: concepts
tags: [vrp, drones, last-mile, operations-research]
relationships:
  - target: "[[concepts/cp-sat-hint-start]]"
    type: related_to
  - target: "[[references/montemanni2024-pdsvrp-collective-drones]]"
    type: derived_from
  - target: "[[references/montemanni2024-parallel-collective-drones]]"
    type: derived_from
  - target: "[[references/montemanni2023-cp-pdsvrp]]"
    type: related_to
  - target: "[[concepts/collective-drone-delivery]]"
    type: related_to
  - target: "[[references/sacramento2019-vrp-d-truck-drone-alns-cost]]"
    type: derived_from
  - target: "[[concepts/k-multi-visit-drone-routing-problem]]"
    type: related_to
    note: "Reciprocal - concepts/k-multi-visit-drone-routing-problem references this page."
    confidence: 0.7
    basis: observed
    since: "2026-10-30T14:38:55Z"
  - target: "[[concepts/min-cost-parallel-drone-scheduling-vrp]]"
    type: related_to
    note: "Reciprocal - concepts/min-cost-parallel-drone-scheduling-vrp references this page."
    confidence: 0.7
    basis: observed
    since: "2026-10-30T14:38:55Z"
  - target: "[[references/nguyen2022-min-cost-pdsvrp]]"
    type: related_to
    note: "Reciprocal - references/nguyen2022-min-cost-pdsvrp references this page."
    confidence: 0.7
    basis: observed
    since: "2026-10-30T14:38:55Z"
  - target: "[[references/poikonen2020-k-mvdrp]]"
    type: related_to
    note: "Reciprocal - references/poikonen2020-k-mvdrp references this page."
    confidence: 0.7
    basis: observed
    since: "2026-10-30T14:38:55Z"
sources:
  - _papers/montemanni2024combining/montemanni2024combining-extracted.md
  - _papers/montemanni2024parallel/montemanni2024parallel-extracted.md
  - _papers/montemanni2024parallel/montemanni2024parallel.md
  - _papers/montemanni2024parallel/images/page_3_image_0.jpg
  - _papers/montemanni2023constraint/montemanni2023constraint-extracted.md
  - _papers/montemanni2023constraint/montemanni2023constraint.md
summary: >-
  PDSVRP-c: multiple trucks plus collaborative drone missions with min-makespan and synchronization; introduced by Montemanni et al. 2024 with CP and MILP models.
provenance:
  extracted: 0.87
  inferred: 0.13
  ambiguous: 0.0
base_confidence: 0.87
lifecycle: draft
lifecycle_changed: 2026-10-25
tier: core
created: 2026-10-22T08:07:13Z
updated: 2026-10-30T14:38:55Z
---

# PDSVRP-c (Parallel Drone Scheduling Vehicle Routing Problem with Collective Drones)

PDSVRP-c is a last-mile optimization problem where several trucks and several drones operate in parallel, and drones may collaborate in groups on a single delivery mission.

It generalizes truck-only min-max VRP and single-drone variants by adding synchronized truck/drone timing and multi-drone assignment decisions.

## Key Ideas

- The graph has depot node 0 and customer nodes; trucks route across the graph while drones perform depot-customer-depot missions.
- Customers split into truck-mandatory set \(\mathcal{C}_T\) and drone-eligible set \(\mathcal{C}_F\).
- For each drone-eligible customer \(j\), bounds \(q_j\) and \(p_j\) define the minimum and maximum number of drones that may serve it.
- Mission duration depends on the number of collaborating drones (precomputed \(\tau_j^k\) values).
- Objective is to minimize overall completion time (makespan), not total distance.
- In practice, good truck tours provide a strong scaffold for assigning drone missions later. ^[inferred]
- The first multi-truck [[concepts/collective-drone-delivery|collective-drone]] variant was introduced by Montemanni, Dell'Amico & Corsini (2024) with two CP models (giant-tour CP2, per-truck CP3) and one MILP.
- A workload-balancing valid inequality, m·α ≥ Σ_{j∈C_F} Σ_k k·τ_j^k z_j^k, strengthens the single-truck CP model and the MILP, yielding first-ever lower bounds on all large PDSTSP-c instances.
- CP2 gives the strongest lower bounds on large instances, CP3 is more consistent with many customers and few trucks, and CP closes all small instances except one.
- Non-collective CP baselines (3-index Circuit models and giant-tour models with time/weight counters, Montemanni & Dell'Amico 2023) produced new best lower bounds on all tested min-time instances and the first lower bounds ever on the min-cost benchmark.

See also [[concepts/cp-sat-hint-start]] for the warm-start strategy, [[references/montemanni2024-pdsvrp-collective-drones]] and [[references/montemanni2024-parallel-collective-drones]] for experiment details, and [[references/montemanni2023-cp-pdsvrp]] for the non-collective CP baselines.

## Open Questions

- How much of the performance gain comes from better lower bounds vs better primal solutions as instance size grows?
- Can decomposition or column-generation hybrids scale better than direct CP-SAT circuit constraints on the largest instances? ^[inferred]


## Related

- [[references/sacramento2019-vrp-d-truck-drone-alns-cost]] — shares drones + vrp tags with this page
## Sources

- [[_papers/montemanni2024combining/montemanni2024combining-extracted.md]]
- [[_papers/montemanni2024parallel/montemanni2024parallel-extracted.md]]
- [[_papers/montemanni2024parallel/montemanni2024parallel.md]]
- [[_papers/montemanni2024parallel/images/page_3_image_0.jpg]]
- [[_papers/montemanni2023constraint/montemanni2023constraint-extracted.md]]
- [[_papers/montemanni2023constraint/montemanni2023constraint.md]]
