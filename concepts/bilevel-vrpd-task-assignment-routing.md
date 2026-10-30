---
title: >-
  Bi-level VRPD Task Assignment and Routing
category: concepts
tags: [vrp, drones, decomposition]
relationships:
  - target: "[[references/yang2022-vrpd-bilevel-heuristic]]"
    type: derived_from
  - target: "[[concepts/large-neighborhood-search]]"
    type: extends
  - target: "[[concepts/k-multi-visit-drone-routing-problem]]"
    type: related_to
  - target: "[[references/dorling2017-drone-delivery-vrp]]"
    type: related_to
  - target: "[[references/montemanni2024-pdsvrp-collective-drones]]"
    type: derived_from
  - target: "[[references/nguyen2022-min-cost-pdsvrp]]"
    type: derived_from
  - target: "[[references/sacramento2019-vrp-d-truck-drone-alns-cost]]"
    type: derived_from
  - target: "[[concepts/cooperative-multi-agent-uav-routing]]"
    type: related_to
  - target: "[[concepts/min-cost-parallel-drone-scheduling-vrp]]"
    type: related_to
sources:
  - _papers/yang2022solving/yang2022solving-extracted.md
  - _papers/yang2022solving/yang2022solving.md
summary: >-
  A two-level optimization pattern that separates customer-to-mode assignment from route/schedule construction in VRPD, coupling global assignment search with ALNS route refinement.
provenance:
  extracted: 0.87
  inferred: 0.10
  ambiguous: 0.03
base_confidence: 0.67
lifecycle: draft
lifecycle_changed: 2026-10-22
tier: core
created: 2026-10-22T09:52:03Z
updated: 2026-10-30T17:41:00Z
---

# Bi-level VRPD Task Assignment and Routing

Bi-level VRPD decomposition separates **who serves each customer** from **how vehicles are routed and scheduled**.

## Key Ideas

- **Upper level:** search assignment vectors that map UAV-eligible customers to truck or drone service; the published instantiation encodes the assignment as a bit string with one bit per UAV-serviceable customer.
- **Lower level:** given an assignment, rebuild truck routes and drone station schedules to evaluate total objective; the truck-routing step uses random removal, worst removal and regret-insertion moves inside a simulated-annealing acceptance rule.
- This decomposition reduces combinatorial coupling compared with a monolithic neighborhood over assignment + routing at once. ^[inferred]
- In the Yang et al. instantiation, BSO drives assignment exploration while ALNS-SA improves route quality.

A generic abstraction is:

$$
\min_{a \in A} F\big(a, R(a)\big)
$$

where `a` is assignment and `R(a)` is lower-level route/schedule optimization.

Compared with plain [[concepts/large-neighborhood-search]], this pattern adds an explicit assignment layer and can improve exploration over heterogeneous service-mode choices. ^[inferred]

Related pages: [[references/yang2022-vrpd-bilevel-heuristic]], [[concepts/large-neighborhood-search]], [[concepts/k-multi-visit-drone-routing-problem]], [[references/poikonen2020-k-mvdrp]].

## Open Questions

- Which assignment encodings best preserve useful route structure during crossover/mutation?
- When does bi-level separation outperform single-level ALNS on larger, noisier urban instances? ^[inferred]


## Related

- [[references/montemanni2024-pdsvrp-collective-drones]] — shares drones + vrp tags with this page
- [[references/nguyen2022-min-cost-pdsvrp]] — shares drones + vrp tags with this page
- [[references/sacramento2019-vrp-d-truck-drone-alns-cost]] — shares drones + vrp tags with this page
## Sources

- [[_papers/yang2022solving/yang2022solving-extracted.md]]
- [[_papers/yang2022solving/yang2022solving.md]]
