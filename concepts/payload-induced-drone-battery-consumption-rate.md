---
title: Payload-induced Drone Battery Consumption Rate (BCR)
category: concepts
tags: [drones, energy-modeling, scheduling, operations-research]
relationships:
  - target: "[[references/torabbeigi2020-payload-bcr-drone-scheduling]]"
    type: derived_from
  - target: "[[concepts/drone-speed-selection-in-routing]]"
    type: related_to
  - target: "[[concepts/min-cost-tsp-with-drone]]"
    type: related_to
  - target: "[[references/tamke2023-vrpd-dss]]"
    type: related_to
  - target: "[[references/fuertes2023-transformer-multi-uav-routing]]"
    type: related_to
  - target: "[[concepts/cooperative-multi-agent-uav-routing]]"
    type: related_to
  - target: "[[concepts/peukert-law-battery-discharge]]"
    type: related_to
  - target: "[[references/raj2020multiple-variable-drone-speed-mfstsp]]"
    type: related_to
  - target: "[[concepts/collective-drone-delivery]]"
    type: related_to
  - target: "[[concepts/drone-energy-consumption-model-taxonomy]]"
    type: related_to
  - target: "[[concepts/multirotor-power-model-components]]"
    type: related_to
  - target: "[[concepts/nonlinear-drone-energy-function-in-routing]]"
    type: related_to
  - target: "[[concepts/uav-payload-bottleneck]]"
    type: related_to
  - target: "[[references/ahmadi-javid2022-drone-delivery-energy-formulation]]"
    type: related_to
  - target: "[[references/cheng2020-drone-routing-energy-function]]"
    type: related_to
  - target: "[[references/dorling2017-drone-delivery-vrp]]"
    type: related_to
  - target: "[[references/liu2017power]]"
    type: related_to
  - target: "[[references/meng2023-multivisit-drone-pickup-delivery]]"
    type: related_to
  - target: "[[references/song2018-persistent-uav-delivery-milp-rhta]]"
    type: related_to
sources:
  - _papers/torabbeigi2020drone/torabbeigi2020drone-extracted.md
  - _papers/torabbeigi2020drone/torabbeigi2020drone.md
  - _papers/fuertes2023solving/fuertes2023solving-extracted.md
  - _papers/fuertes2023solving/fuertes2023solving.md
  - _papers/fuertes2023solving/images/page_4_image_3.jpg
summary: Battery draw grows with payload in drone delivery, and this dependency should be modeled explicitly in feasibility and scheduling decisions.
provenance:
  extracted: 0.82
  inferred: 0.14
  ambiguous: 0.04

base_confidence: 0.77
lifecycle: draft
lifecycle_changed: 2026-10-24
tier: core
created: 2026-10-22T10:00:17Z
updated: 2026-10-30T14:38:55Z
---

# Payload-induced Drone Battery Consumption Rate (BCR)

Payload-induced BCR models battery consumption as a function of carried payload instead of assuming a constant drain rate.

## Key Ideas

- A practical linear approximation is used in the source paper:

\[
\text{BCR} = \alpha \cdot \text{payload} + \beta
\]

- With this model, route feasibility can change materially compared with constant-BCR assumptions.
- Scheduling and fleet-sizing decisions should be recalculated under payload-aware energy constraints.
- Preprocessing rules that remove capacity- or energy-infeasible arcs can significantly reduce optimization search space.
- Fuertes et al. do not model payload-dependent drain (Euclidean distances, zero service time, one shared fleet speed), but battery depletion is the stated motivation for their cooperative reward sharing: $t_{max}$ is set so each UAV reaches roughly half the nodes, and cooperation mitigates lost/UAV-depleted agents because shared regions stay reachable by the rest. Per-agent payload-BCR feasibility is the constraint family such a cooperative fleet planner must enforce. ^[inferred] [[references/fuertes2023-transformer-multi-uav-routing]]

Ignoring payload-sensitive BCR tends to overestimate operational feasibility in heterogeneous-demand settings. ^[inferred]

Extended related pages: [[concepts/cooperative-multi-agent-uav-routing]], [[concepts/transformer-seq2seq-routing-solver]].
Related pages: [[references/torabbeigi2020-payload-bcr-drone-scheduling]], [[concepts/drone-speed-selection-in-routing]], [[concepts/min-cost-tsp-with-drone]], [[references/tamke2023-vrpd-dss]], [[references/poikonen2020-k-mvdrp]].

## Open Questions

- How well does a linear BCR model transfer across drone platforms, weather conditions, and battery age profiles?
- When should nonlinear energy models be preferred over linear BCR for high-stakes planning? ^[inferred]

## Related

- [[references/song2018-persistent-uav-delivery-milp-rhta]] — persistent UAV delivery with payload-weighted flight time, solved by a receding-horizon petal heuristic in under 0.4 s

- [[references/zhang2021-drone-energy-model-comparison]] — regression energy rates (Tseng, Dorling) with payload-weight terms compared against the physical models.
## Sources

- [[_papers/torabbeigi2020drone/torabbeigi2020drone-extracted.md]]
- [[_papers/torabbeigi2020drone/torabbeigi2020drone.md]]
- [[_papers/fuertes2023solving/fuertes2023solving-extracted.md]]
- [[_papers/fuertes2023solving/fuertes2023solving.md]]
- [[_papers/fuertes2023solving/images/page_4_image_3.jpg]]
