---
title: >-
  Drone Swarm Synchronization
category: concepts
tags: [swarm-synchronization, vrptw, split-delivery, simultaneous-arrival, coupling, decoupling, detour, multi-trip, rotary-wing-drone, drone-routing, synchronization, alns]
relationships:
  - target: "[[references/li2024drone]]"
    type: derived_from
  - target: "[[concepts/vehicle-routing-with-synchronization-constraints]]"
    type: related_to
  - target: "[[references/ha2020-vrp-synchronization-lp-alns]]"
    type: related_to
  - target: "[[concepts/exact-multitrip-vrptw-framework]]"
    type: related_to
  - target: "[[concepts/large-neighborhood-search]]"
    type: related_to
  - target: "[[concepts/simulated-annealing-metropolis-cooling]]"
    type: related_to
  - target: "[[concepts/collective-drone-delivery]]"
    type: related_to
  - target: "[[references/hojabri2018-vrp-synchronization-alns-cp]]"
    type: derived_from
sources:
  - _papers/li2024drone/li2024drone-extracted.md
  - _papers/li2024drone/li2024drone.md
summary: >-
  Swarm synchronization: drones couple and decouple at nodes, serve over-capacity customers with simultaneous arrival, split delivery, detours, multi trips; defined by DRP-SS (Li, Wang & Zhan 2024).
provenance:
  extracted: 0.93
  inferred: 0.07
  ambiguous: 0.00
base_confidence: 0.67
lifecycle: draft
lifecycle_changed: 2026-10-26T00:51:06Z
tier: core
created: 2026-10-26T00:51:06Z
updated: 2026-10-27T06:00:00Z
---

# Drone Swarm Synchronization

> [!tldr] Rotary-wing drones (RWDs) dynamically couple and decouple into swarms **at network nodes** (not only at the depot); a customer whose demand exceeds drone capacity `Q` is served by **split delivery**, and a customer served fully by several drones requires a **swarm** whose members arrive **simultaneously**. The mechanism was formalized as the Drone Routing Problem with Swarm Synchronization (DRP-SS) by Li, Wang & Zhan (2024, EJOR, DOI 10.1016/j.ejor.2023.10.015).

## Rules

- Customers over capacity `Q` are split across multiple RWDs (`Σ_u p_ui = q_i`, `p_ui ≤ Q f_ui`).
- Swarm members serving a customer must arrive simultaneously; swarms form and break at nodes, members leave a shared node at equal times.
- A drone may fly to a customer **without delivering** (detour) purely to join a swarm; no time window is imposed at a detour node.
- Each RWD can run multiple trips; a preparation time `τ` separates consecutive trips.
- A swarm flying an arc pays less per member: `c^swarm_ij = (b − a·N_uij)·c_ij` with `b = 1`, `a = 0.05`.
- DRP-SS is, in the paper's Table 1, the only surveyed variant combining coupling/decoupling, split delivery, multi trips, and time windows; [[concepts/vehicle-routing-with-synchronization-constraints]] is the classical predecessor, with the VRPMS ALNS baseline of [[references/ha2020-vrp-synchronization-lp-alns]] as comparison.

## What swarms buy

Solved by a MILP plus an ALNS with detour and multi-trip operators (see [[concepts/large-neighborhood-search]] and [[concepts/simulated-annealing-metropolis-cooling]]), on 71 small and 116 large Solomon-derived instances: detours save 1.63%–2.55% (no-detour ablation), swarms save 3.42%–3.92% over truck mode, multi trips save 19.88%–67.14%; more over-capacity customers mean more swarm arcs (11 → 39) and 2.6 → 3.2 drones per swarm arc. CPLEX closes every C-type instance up to 12 customers in under 2600 s when detours are prevented (`Σ_u Σ_j x_uij ≤ ⌈q_i/Q⌉`). The gain comes with higher computational burden: swarm synchronization plus time continuity is the bottleneck. Multi-trip structure connects to the multi-trip VRPTW exact framework lineage in [[concepts/exact-multitrip-vrptw-framework]].

## Related

- [[references/li2024drone]] — the source paper defining DRP-SS
- [[concepts/vehicle-routing-with-synchronization-constraints]] — classical synchronization
- [[references/ha2020-vrp-synchronization-lp-alns]] — VRPMS ALNS baseline
- [[concepts/exact-multitrip-vrptw-framework]] — multi-trip VRPTW lineage
- [[concepts/large-neighborhood-search]] — the ALNS shell
- [[concepts/simulated-annealing-metropolis-cooling]] — acceptance in the ALNS
- [[concepts/collective-drone-delivery]] — c-drones couple at the depot, so the order of services in a drone tour matters ^[inferred]
- [[references/hojabri2018-vrp-synchronization-alns-cp]] — shares alns + synchronization tags with this page

## Sources

- [[_papers/li2024drone/li2024drone-extracted.md]]
- [[_papers/li2024drone/li2024drone.md]]
