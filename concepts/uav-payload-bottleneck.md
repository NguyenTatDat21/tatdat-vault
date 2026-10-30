---
title: >-
  UAV Payload Bottleneck in Truck-Launched Drone Delivery
category: concepts
tags: [UAV, payload, battery, endurance, tradeoff, truck-drone, delivery, bottleneck]
relationships:
  - target: "[[references/wang2019routing]]"
    type: related_to
  - target: "[[concepts/hybrid-truck-drone-delivery]]"
    type: related_to
  - target: "[[concepts/payload-induced-drone-battery-consumption-rate]]"
    type: related_to
  - target: "[[concepts/peukert-law-battery-discharge]]"
    type: related_to
summary: >-
  Truck-launched UAV delivery is gated by payload, not battery: payload, endurance, speed set battery life, and battery weight trades against payload.
provenance:
  extracted: 0.92
  inferred: 0.04
  ambiguous: 0.04
base_confidence: 0.67
tier: core
lifecycle: draft
lifecycle_changed: 2026-10-29
created: 2026-10-29T16:44:00Z
updated: 2026-10-29T16:44:00Z
sources:
  - _papers/wang2019routing/wang2019routing-extracted.md
  - _papers/wang2019routing/images/page_2_image_3.jpg
---

# UAV Payload Bottleneck in Truck-Launched Drone Delivery

> [!tldr] Truck-launched UAV delivery is gated by payload, not battery: a fully loaded drone needs more energy for take-off, and battery weight trades against payload. ^[extracted]

![[_papers/wang2019routing/images/page_2_image_3.jpg]]
*Fig. 2. The illustration of UAV payload bottleneck.* — payload, endurance, battery weight interact; a fully loaded UAV burns more energy for take-off.

Payload, endurance, and speed set the battery life; the battery-weight tradeoff — more battery, less payload — is the key tradeoff for a UAV delivery platform. ^[extracted] The energy per customer-customer arc is `W_ij = (w_d + G_i)·d_ij·P / (370·η·γ·(P−e))`, payload-weighted distance: `w_d` drone weight, `G_i` payload, `P` power demand, `γ` lift-to-weight ratio, `η` engine efficiency, `e` motor efficiency. ^[extracted] Drones are constrained by payload and endurance, flying inside a circle of endurance radius with multi-visit deliveries. ^[extracted]

In the HTDD experiments, truck distance cost rises when UAV max flight distance exceeds 5 km: the payload becomes the bottleneck factor, so the truck carries more work as battery weight tradeoff bites. ^[extracted] HTDD is less sensitive to battery capacity than the baselines. ^[extracted] The paper draws the conclusion from Fig. 2 (a fully loaded UAV needs more energy for take-off) and the endurance sweep results; the 5 km threshold is the sweep point, not a derived constant. `^[ambiguous]` ^[inferred]

## Related

- [[references/wang2019routing]] — the payload-bottleneck paper (Wang et al. 2019, IEEE IoT-J). ^[extracted]
- [[concepts/hybrid-truck-drone-delivery]] — the model where the truck absorbs the payload-bottleneck work. ^[extracted]
- [[concepts/payload-induced-drone-battery-consumption-rate]] — payload as battery-consumption rate in scheduling models. ^[extracted]
- [[concepts/peukert-law-battery-discharge]] — discharge model for endurance-limited UAV battery capacity. ^[extracted]
- [[concepts/nonlinear-drone-energy-function-in-routing]] — energy functions with payload in routing objectives. ^[extracted]
- [[concepts/drone-energy-consumption-model-taxonomy]] — energy-model taxonomy covering the eq. 4 family. ^[extracted]
- [[concepts/multirotor-power-model-components]] — power, lift ratio, efficiency inputs of eq. 4. ^[extracted]

## Sources

- [[_papers/wang2019routing/wang2019routing-extracted]]
- [[_papers/wang2019routing/images/page_2_image_3.jpg]]
