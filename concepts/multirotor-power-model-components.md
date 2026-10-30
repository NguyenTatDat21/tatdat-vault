---
title: >-
  Multirotor Power Model Components (Induced, Profile, Parasite)
category: concepts
tags: [power-model, energy-consumption, quadrotor, induced-power, profile-power, parasite-drag, actuator-disk, blade-element, hover-power, steady-state, parameter-identification, uav]
relationships:
  - target: "[[references/liu2017power]]"
    type: derived_from
  - target: "[[concepts/nonlinear-drone-energy-function-in-routing]]"
    type: related_to
  - target: "[[concepts/payload-induced-drone-battery-consumption-rate]]"
    type: related_to
  - target: "[[references/cheng2020-drone-routing-energy-function]]"
    type: related_to
  - target: "[[references/dorling2017-drone-delivery-vrp]]"
    type: related_to
  - target: "[[concepts/peukert-law-battery-discharge]]"
    type: related_to
  - target: "[[concepts/collective-drone-delivery]]"
    type: related_to
  - target: "[[concepts/drone-delivery-energy-and-range-parameters]]"
    type: related_to
  - target: "[[concepts/drone-energy-consumption-model-taxonomy]]"
    type: related_to
  - target: "[[concepts/lift-to-drag-ratio-power-efficiency-sensitivity]]"
    type: related_to
  - target: "[[references/nguyen2023-pdstsp-collective-drones]]"
    type: related_to
  - target: "[[references/wang2019routing]]"
    type: related_to
sources:
  - _papers/liu2017power/liu2017power-extracted.md
  - _papers/liu2017power/liu2017power.md
summary: >-
  Three-component steady-state power model for multi-rotors: induced (actuator disk), profile (blade element), parasite (body drag); convex T^{3/2} hover law; parameters identified from bench flights.
provenance:
  extracted: 0.92
  inferred: 0.00
  ambiguous: 0.08
base_confidence: 0.67
lifecycle: draft
lifecycle_changed: 2026-10-26T00:51:06Z
tier: core
created: 2026-10-26T00:51:06Z
updated: 2026-10-30T14:38:55Z
---

# Multirotor Power Model Components (Induced, Profile, Parasite)

> [!tldr] In the tradition of helicopter power theory, total power of a multi-rotor in steady-state flight decomposes as `P = P_i + P_p + P_par` — induced power (actuator-disk theory), profile power (blade-element theory), parasite power (body drag). The three components account for more than 95% of a typical helicopter's total power.

## The three components

- **Induced power** `P_i(T, V_vert) = k₁ T [ V_vert/2 + √((V_vert/2)² + T/k₂²) ]` from actuator-disk theory with thrust `T`, disk area `A`, air density `ρ`, far-field velocity `V∞`, wake velocity `V₀` (`P_i = TV`, `T = ṁ(V∞ − V₀)`, `V = ½(V∞ + V₀)`, `ṁ = ρAV`).
- **Profile power** from blade-element theory: hover term `(N c c_d ρ R⁴ / 8) Ω³` extended by the advance ratio `μ = V_air cos α / (ΩR)` to `P_p = P_{p,hover}(1 + μ²)`, summarized as `c₂ T^{3/2} + c₃ (V_air cos α)² T^{1/2}`.
- **Parasite power** from body drag: `P_par = ½ C_d ρ A_quad V_air³ = c₄ V_air³`, with lift `L = c₅(V_air cos α)² + c₆ T` and thrust requirement `T = √((mg − L)² + D²)`.

Hovering (`V_vert = 0`) collapses the model to the convex **hover law** `P = (c₁ + c₂)(mg)^{3/2}` — the same `T^{3/2}` payload law used by routing energy models such as [[concepts/nonlinear-drone-energy-function-in-routing]] and [[concepts/payload-induced-drone-battery-consumption-rate]] and by the VRP energy constraints in [[references/cheng2020-drone-routing-energy-function]] and [[references/dorling2017-drone-delivery-vrp]].

## Parameter identification

The decomposition was fitted to an IRIS+ quadrotor via three bench flights at the Richmond Field Station (10 Hz data, EKF-estimated airspeed, voltage×current power, three repeats per test): (1) hover with payloads 14.3–22 N → `c₁ + c₂ = 2.84 (m/kg)^{1/2}`; (2) steady ascend/descend at ±2.5 m/s (180 W up, 164 W hover, 150 W down) → `c₁ + c₂ = 3.11`, ~10% error vs experiment 1; (3) a 345 m cyclic straight line at 5–25 m/s, wind ≈ 2 m/s from the forward/backward ground-speed difference, identifying `c₄ = 0.0296 kg/m`, `c₅ = 0.0279 Ns/m`, with `c₃ ≈ 0` and `c₆ ≈ 0` assumed. Final parameters (Table III of [[references/liu2017power]]): `k₁ = 0.8554`, `k₂ = 0.3051 (kg/m)^{1/2}`, `c₁ = 2.8037`, `c₂ = 0.3177`.

Validation on a separate flight (70 m AGL rectangular loop at 10–20 m/s) gave energy errors of 10.7% on take-off, 2.2% on landing, 16.5% on the loop; the loop under-predicts because acceleration and deceleration add energy the steady-state model omits, and wind at 70 m is significant. `^[ambiguous]`

## Related

- [[references/liu2017power]] — the source paper (ICUAS 2017, DOI 10.1109/ICUAS.2017.7991310)
- [[concepts/nonlinear-drone-energy-function-in-routing]] — routing-level `P(q) = k(W+m+q)^{3/2}`
- [[concepts/payload-induced-drone-battery-consumption-rate]] — payload-aware consumption
- [[references/cheng2020-drone-routing-energy-function]] — energy function inside VRP
- [[references/dorling2017-drone-delivery-vrp]] — drone delivery VRP with energy constraints
- [[concepts/peukert-law-battery-discharge]] — converts power into current-dependent, capacity-shrinking battery demand

## Sources
0

- [[_papers/liu2017power/liu2017power-extracted.md]]
- [[_papers/liu2017power/liu2017power.md]]
