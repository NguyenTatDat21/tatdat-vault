---
title: >-
  k-Multi-Visit Drone Routing Problem (k-MVDRP)
category: concepts
tags: [vrp, drones, last-mile, operations-research]
relationships:
  - target: "[[references/poikonen2020-k-mvdrp]]"
    type: derived_from
  - target: "[[concepts/pdsvrp-c]]"
    type: related_to
  - target: "[[references/montemanni2024-pdsvrp-collective-drones]]"
    type: related_to
  - target: "[[references/nguyen2022-min-cost-pdsvrp]]"
    type: derived_from
sources:
  - _papers/poikonen2020multivisit/poikonen2020multivisit-extracted.md
  - _papers/poikonen2020multivisit/poikonen2020multivisit.md
summary: >-
  k-MVDRP models a truck with k reusable drones under payload-dependent energy limits and operation-level synchronization, optimized for minimum completion time.
provenance:
  extracted: 0.8
  inferred: 0.17
  ambiguous: 0.03
base_confidence: 0.67
lifecycle: draft
lifecycle_changed: 2026-10-22
tier: core
created: 2026-10-22T08:44:14Z
updated: 2026-10-27T06:00:00Z
---

# k-Multi-Visit Drone Routing Problem (k-MVDRP)

k-MVDRP is a coordinated truck-drone routing model where a truck acts as a mobile depot and up to `k` drones can launch repeatedly, deliver one or more packages, recharge/replace batteries at the truck, and relaunch until all deliveries are complete.

## Key Ideas

- Objective: minimize route completion time (truck + all drones returned to depot).
- Customers have package weights, and drone energy usage is payload-aware through an energy function `e(vi, vj, w)`.
- Launch/landing locations (`V`) are not restricted to customer nodes (`C`), enabling rendezvous-based synchronization.
- An operation starts with truck + drones at one launch location and ends with truck + drones at one retrieval location.
- Each sortie must satisfy energy feasibility, including hover energy when drones wait for the truck (`HOV`).
- The benchmark paper solves large instances with the RTS heuristic (Route → Transform → Shortest Path) rather than full exact optimization.

Compared with [[concepts/pdsvrp-c]], k-MVDRP is a foundational single-truck family with multi-visit drone sorties; PDSVRP-c adds parallel trucks and collective multi-drone service patterns. ^[inferred]

Related pages: [[references/poikonen2020-k-mvdrp]], [[concepts/pdsvrp-c]], [[references/montemanni2024-pdsvrp-collective-drones]], and [[concepts/cp-sat-hint-start]].

## Open Questions

- What assignment rule inside each operation best balances quality and runtime beyond block partitioning?
- Which lower-bound family can jointly capture synchronization wait and battery/range effects tightly enough for stronger guarantees? ^[inferred]


## Related

- [[references/nguyen2022-min-cost-pdsvrp]] — shares drones + vrp tags with this page
- [[references/meng2023-multivisit-drone-pickup-delivery]] — adds pickup-and-delivery customers and load-dependent drone energy to the k-MVDRP family
## Sources

- [[_papers/poikonen2020multivisit/poikonen2020multivisit-extracted.md]]
- [[_papers/poikonen2020multivisit/poikonen2020multivisit.md]]
