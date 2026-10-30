---
title: >-
  Delivery by Drones with Arbitrary Energy Consumption Models: A New Formulation Approach
category: references
tags: [drones, routing, energy-modeling, mixed-integer-programming]
relationships:
  - target: "[[concepts/nonlinear-drone-energy-function-in-routing]]"
    type: extends
  - target: "[[concepts/payload-induced-drone-battery-consumption-rate]]"
    type: uses
  - target: "[[references/cheng2020-drone-routing-energy-function]]"
    type: related_to
  - target: "[[references/dorling2017-drone-delivery-vrp]]"
    type: related_to
  - target: "[[concepts/drone-speed-selection-in-routing]]"
    type: uses
sources:
  - _papers/ahmadi-javid2022delivery/ahmadi-javid2022delivery-extracted.md
  - _papers/ahmadi-javid2022delivery/ahmadi-javid2022delivery.md
summary: >-
  Arc-based multi-trip drone-delivery formulation with arbitrary energy models, preserving nonlinear realism while substantially accelerating exact optimization on benchmarks.
provenance:
  extracted: 0.88
  inferred: 0.10
  ambiguous: 0.02
base_confidence: 0.67
lifecycle: draft
lifecycle_changed: 2026-10-22
tier: core
created: 2026-10-22T19:23:44Z
updated: 2026-10-30T14:39:22Z
---

# Delivery by Drones with Arbitrary Energy Consumption Models: A New Formulation Approach

> [!tldr] Reformulates [[references/dorling2017-drone-delivery-vrp|multi-trip drone delivery]] so general energy models can be used directly, with major runtime gains on benchmark instances.

## Problem & Motivation

The paper targets drone-delivery planning where each drone may execute multiple trips from a central depot to serve customers. Prior exact models typically needed restrictive approximations of battery usage, which limited realism and scalability.

## Method / Architecture

The model uses arc-based routing decisions and explicitly couples routing with an energy-consumption term that can represent general functions of payload and flight time.

```mermaid
flowchart LR
  A[Customers, depot, time windows] --> B[Arc-routing variables x_a]
  B --> C[Travel-cost term]
  B --> D[Energy term ed_a]
  D --> E[General energy model F_a(w_a, t_a)]
  E --> F[Linear-relaxation-friendly formulation]
  F --> G[Exact or bounded-gap schedules]
```

Mermaid structure is reconstructed from the formulation narrative, not transcribed from a figure. ^[inferred]

## Key Equations

$$
\min \sum_{a \in A_O} c_a x_a + \delta \sum_{a \in A_O} ed_a x_a
$$

$$
ed_a = F_a(w_a, t_a) \qquad a \in A_O
$$

$$
F_a(w_a, t_a) = t_a\,\alpha\,(\beta + w_a)^{3/2}
$$

## Results

| Setting | Prior best | This paper |
|---|---|---|
| 255 benchmark instances (up to 50 customers) | Branch-and-cut baseline | ~20× faster on average |
| 15 instances with 50 customers | None solved to optimality previously | 15/15 solved optimally |
| New larger instances (up to 150 customers) | Limited precedent | Small optimality gaps within a few hours |

## Limitations

- Reported computational gains are tied to the tested benchmark family and selected energy function.
- The paper presents extensions (hovering/time-window handling, payload-dependent flight time), but cross-dataset external validity is still an open empirical question. ^[inferred]

## Related

- [[concepts/nonlinear-drone-energy-function-in-routing]]
- [[concepts/payload-induced-drone-battery-consumption-rate]]
- [[references/cheng2020-drone-routing-energy-function]]
- [[references/nguyen2022-min-cost-pdsvrp]]
- [[references/dorling2017-drone-delivery-vrp]]
- [[concepts/drone-speed-selection-in-routing]] — shares drones + routing tags with this page

## Sources

- [[_papers/ahmadi-javid2022delivery/ahmadi-javid2022delivery-extracted.md]]
- [[_papers/ahmadi-javid2022delivery/ahmadi-javid2022delivery.md]]
