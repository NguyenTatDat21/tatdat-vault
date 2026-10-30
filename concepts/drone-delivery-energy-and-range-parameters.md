---
title: >-
  Drone Delivery Energy and Range Parameters: weight, payload, power, lift ratio, efficiency
category: concepts
tags: [uav, energy-modeling]
relationships:
  - target: "[[references/wang2019routing]]"
    type: related_to
  - target: "[[concepts/nonlinear-drone-energy-function-in-routing]]"
    type: related_to
  - target: "[[concepts/multirotor-power-model-components]]"
    type: related_to
  - target: "[[concepts/lift-to-drag-ratio-power-efficiency-sensitivity]]"
    type: related_to
summary: >-
  Single-product payload energy per arc: drone weight plus payload times distance, scaled by power demand, lift-to-weight ratio, and engine/motor efficiency.
provenance:
  extracted: 0.88
  inferred: 0.12
  ambiguous: 0.0
base_confidence: 0.67
tier: supporting
lifecycle: draft
lifecycle_changed: 2026-10-29
created: 2026-10-29T16:44:00Z
updated: 2026-10-30T17:41:00Z
sources:
  - _papers/wang2019routing/wang2019routing-extracted.md
---

# Drone Delivery Energy and Range Parameters: weight, payload, power, lift ratio, efficiency

> [!tldr] The eq. 4 family from the truck-launched UAV literature: energy per arc is payload-weighted distance `W_ij = (w_d + G_i)·d_ij·P / (370·η·γ·(P−e))` with drone weight, payload, power demand, lift-to-weight ratio, engine and motor efficiency. ^[extracted]

The energy per customer-customer arc is `W_ij = (w_d + G_i)·d_ij·P / (370·η·γ·(P−e))` (eq. 4): `w_d` drone weight, `G_i` payload, `d_ij` distance, `P` power demand, `γ` lift-to-weight ratio, `η` engine efficiency, `e` motor efficiency. ^[extracted] Payload, endurance, and speed set the battery life; payload, speed, endurance, and weight are key parameters in UAV routing. ^[extracted] The energy model uses the payload-weighted-distance form, so the energy objective is weight-weighted, not flight-count based. ^[extracted]

Energy and range enter the truck-carried UAV segment model as endurance `D_max^su` and payload `M_max^su` constraints: segment/loop length bounded by endurance, payload sums bounded by payload capacity. ^[extracted] The battery-weight tradeoff — more battery, less payload — is the key tradeoff for a UAV delivery platform. ^[extracted] The model's form is a single-product payload-weighted distance function, as in the eq. 4 literature. ^[inferred]

## Related

- [[references/wang2019routing]] — the eq. 4 energy model, UAV truck-launched delivery. ^[extracted]
- [[concepts/nonlinear-drone-energy-function-in-routing]] — payload-weighted nonlinear energy functions. ^[extracted]
- [[concepts/multirotor-power-model-components]] — power-model components feeding P, γ, η, e. ^[extracted]
- [[concepts/lift-to-drag-ratio-power-efficiency-sensitivity]] — lift-ratio and efficiency sensitivity. ^[extracted]
- [[concepts/drone-energy-consumption-model-taxonomy]] — taxonomy of energy-consumption models. ^[extracted]
- [[concepts/payload-induced-drone-battery-consumption-rate]] — payload-induced battery-consumption rate. ^[extracted]
- [[concepts/peukert-law-battery-discharge]] — battery discharge models for endurance. ^[extracted]

## Sources

- [[_papers/wang2019routing/wang2019routing-extracted]]
