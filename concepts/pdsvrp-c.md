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
sources: [_papers/montemanni2024combining/montemanni2024combining-extracted.md]
summary: >-
  PDSVRP-c extends truck-and-drone routing to multiple trucks plus collaborative drone missions, with a min-makespan objective and synchronization constraints.
provenance:
  extracted: 0.72
  inferred: 0.24
  ambiguous: 0.04
base_confidence: 0.67
lifecycle: draft
lifecycle_changed: 2026-10-22
tier: supporting
created: 2026-10-22T08:07:13Z
updated: 2026-10-22T08:07:13Z
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

See also [[concepts/cp-sat-hint-start]] for the warm-start strategy and [[references/montemanni2024-pdsvrp-collective-drones]] for the experiment details.

## Open Questions

- How much of the performance gain comes from better lower bounds vs better primal solutions as instance size grows?
- Can decomposition or column-generation hybrids scale better than direct CP-SAT circuit constraints on the largest instances? ^[inferred]

## Sources

- [[_papers/montemanni2024combining/montemanni2024combining-extracted.md]]
