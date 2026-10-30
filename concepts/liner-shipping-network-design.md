---
title: Liner Shipping Network Design
category: concepts
tags: [maritime]
relationships:
  - target: "[[references/christiansen2020-liner-shipping-network-design]]"
    type: derived_from
  - target: "[[references/christiansen2013-ship-routing-scheduling-new-millennium]]"
    type: extends
  - target: "[[references/boland2017-continuous-time-service-network-design]]"
    type: related_to
  - target: "[[references/christiansen2007-maritime-transportation-operations-research]]"
    type: related_to
sources:
  - _papers/christiansen2020liner/christiansen2020liner-extracted.md
  - _papers/christiansen2013ship/christiansen2013ship-extracted.md
summary: >-
  The optimization problem of constructing cyclic liner services, assigning vessel capacity, and routing commodity demand under transit, transshipment, and cost constraints.
provenance:
  extracted: 0.87
  inferred: 0.11
  ambiguous: 0.02
base_confidence: 0.77
lifecycle: draft
lifecycle_changed: 2026-10-22
tier: core
created: 2026-10-22T23:17:15Z
updated: 2026-10-30T17:41:00Z
---

# Liner Shipping Network Design

**Liner Shipping Network Design (LSNDP)** chooses which cyclic services to operate, which vessels to assign, and how to route OD demand through the resulting maritime network while balancing revenue, service quality, and operating cost.

## Canonical Decision Layers

1. **Service design**: choose service shapes (simple, butterfly, pendulum, complex) and visited ports.
2. **Fleet deployment**: allocate vessel classes and frequencies to selected services.
3. **Cargo flow**: route multi-commodity demand with capacity and transit-time constraints.
4. **Operational knobs**: speed, transshipment handling, demand rejection penalties.

## Generic Mathematical Structure

Service-based formulations typically minimize service and flow costs:

$$
\min \sum_{s\in S} c_s y_s + \sum_{k\in K}\sum_{(i,j)\in A} c_{ij}^k \sum_{s\in S} x_{ij}^{ks}
$$

subject to flow conservation, service-capacity coupling, and vessel-availability constraints.

## Main Algorithm Families

- **Integrated MIP**: unified exact model (high fidelity, limited scale).
- **Two-stage design→flow**: often with feedback loops and decomposition.
- **Subset-of-services**: select a network from planner-generated candidate services.
- **Backbone-flow**: flow-first strategy to induce high-load links before service construction.

## Why This Concept Matters

- It is a central abstraction connecting strategic maritime planning and tactical deployment.
- It links naturally to service network design methods used in other transport domains. ^[inferred]
- Benchmark suites (e.g., LINER-LIB) make cross-paper comparisons possible but still leave model-assumption heterogeneity.

## Related

- [[references/christiansen2020-liner-shipping-network-design]]
- [[references/christiansen2013-ship-routing-scheduling-new-millennium]]
- [[references/christiansen2007-maritime-transportation-operations-research]]
- [[references/boland2017-continuous-time-service-network-design]]
- [[concepts/maritime-routing-under-uncertainty]]

## Sources

- [[_papers/christiansen2020liner/christiansen2020liner-extracted.md]]
- [[_papers/christiansen2013ship/christiansen2013ship-extracted.md]]
