---
title: >-
  A Power Consumption Model for Multi-Rotor Small Unmanned Aircraft Systems (Liu, Sengupta & Kurzhanskiy, 2017)
category: references
tags: [paper, energy-modeling, uav]
relationships:
  - target: "[[concepts/multirotor-power-model-components]]"
    type: related_to
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
  - target: "[[references/raj2020multiple-variable-drone-speed-mfstsp]]"
    type: related_to
  - target: "[[references/zhang2021-drone-energy-model-comparison]]"
    type: related_to
sources:
  - _papers/liu2017power/liu2017power-extracted.md
  - _papers/liu2017power/liu2017power.md
  - _papers/liu2017power/images/page_1_image_7.jpg
  - _papers/liu2017power/images/page_3_chart_11.jpg
  - _papers/liu2017power/images/page_4_image_8.jpg
  - _papers/liu2017power/images/page_4_chart_10.jpg
  - _papers/liu2017power/images/page_4_chart_11.jpg
  - _papers/liu2017power/images/page_4_chart_13.jpg
  - _papers/liu2017power/images/page_5_chart_9.jpg
summary: >-
  Multi-rotor power model: induced, profile, parasite components from helicopter theory; parameters identified by hover, ascend/descend, cruise tests; 2-17% validation error.
provenance:
  extracted: 0.94
  inferred: 0.06
  ambiguous: 0.00
base_confidence: 0.67
lifecycle: draft
lifecycle_changed: 2026-10-26
tier: core
created: 2026-10-26T00:51:06Z
updated: 2026-10-30T17:41:00Z
---

# A Power Consumption Model for Multi-Rotor Small Unmanned Aircraft Systems (Liu, Sengupta & Kurzhanskiy, 2017)

> [!tldr] The paper derives a three-component power model for multi-rotor UAVs from helicopter theory (induced, profile, parasite), identifies its parameters through three bench flights of an IRIS+ quadrotor, and validates it in a full rectangular-loop flight with 2.2%–16.5% energy errors.

## Problem & Motivation

Published at the 2017 International Conference on Unmanned Aircraft Systems (ICUAS, DOI 10.1109/ICUAS.2017.7991310) by the CAL Unmanned Laboratory, UC Berkeley. Energy models are needed to plan UAS missions: the authors build a theoretical power model for a multi-rotor in **steady-state flight** (vehicle in force equilibrium), with parameters estimated from experiments, in the tradition of helicopter power theory (Johnson, Leishman) — the three power components account for more than 95% of a typical helicopter's total power. Wind effects and acceleration are left as future work; the flight-path template is vertical take-off, horizontal straight segments, vertical landing.

![[_papers/liu2017power/images/page_1_image_7.jpg]]
*Fig. 1: Control volume (CV) of the air mass of interest.*

## Method / Architecture

Power is decomposed as

$$
P = P_i + P_p + P_{par}
$$

- **Induced power** from actuator-disk theory: with thrust `T`, disk area `A`, air density `ρ`, far-field velocity `V∞`, wake velocity `V₀`, equations `P_i = TV`, `T = ṁ(V∞ − V₀)`, `V = ½(V∞ + V₀)`, `ṁ = ρAV` give

$$
P_i(T, V_{vert}) = k_1 T \left[ \frac{V_{vert}}{2} + \sqrt{\left(\frac{V_{vert}}{2}\right)^2 + \frac{T}{k_2^2}} \right]
$$

- **Profile power** from blade-element theory: hover term `P_{p,hover,i} = (N c c_d ρ R^4 / 8) Ω_i³`, extended by the advance ratio `μ_i = V_air cos α_i / (Ω_i R)` to `P_{p,i} = P_{p,hover,i}(1 + μ_i²)`, summarized as `P_p(T, V_air) = c₂ T^{3/2} + c₃ (V_air cos α)² T^{1/2}`.
- **Parasite power** from body drag: `P_par = ½ C_d ρ A_quad V_air³ = c₄ V_air³`, with lift `L = c₅(V_air cos α)² + c₆ T` and thrust requirement `T = √((mg − L)² + D²)`.
- Hovering (`V_vert = 0`): `P_{i,hover} = (k₁/k₂) T^{3/2} = c₁ T^{3/2}` — the same convex `T^{3/2}` payload law used in routing energy models. `c₃ ≈ 0` and `c₆ ≈ 0` are assumed to make the parameter identification tractable. `V_air = ‖V_ground − V_wind‖`.

Parameter identification used three IRIS+ quadrotor experiments at the Richmond Field Station (10 Hz data, EKF-estimated airspeed, onboard voltage×current power, three repeats per test):

1. **Hover with payloads** (total weight 14.3–22 N): fit `P = (c₁ + c₂)(mg)^{3/2}` → `c₁ + c₂ = 2.84 (m/kg)^{1/2}`.
2. **Steady-state ascend/descend** at `V_vert = ±2.5 m/s`, no payload: measured mean power 180 W (ascend, stdev 6.3), 164 W (hover, stdev 1.7), 150 W (descend, stdev 4.9); four equations in four unknowns → `c₁ + c₂ = 3.11`, about 10% error vs Experiment 1.
3. **Cyclic straight line** (345 m back-and-forth, 20 s hovers at waypoints, desired speeds 5–25 m/s): wind estimated ≈ 2 m/s from the forward/backward ground-speed difference; power is essentially flat for airspeed < 10 m/s, and the lift-induced power/thrust dip at 5–10 m/s appears; lift measured 2.5 N at 10 m/s airspeed. Fit identifies `c₄`, `c₅`. ^[inferred]

![[_papers/liu2017power/images/page_3_chart_11.jpg]]
*Fig. 6: Least square fit of IRIS+ hovering with different payloads.*

![[_papers/liu2017power/images/page_4_image_8.jpg]]
![[_papers/liu2017power/images/page_4_chart_10.jpg]]
![[_papers/liu2017power/images/page_4_chart_11.jpg]]
![[_papers/liu2017power/images/page_4_chart_13.jpg]]
*Fig. 8: Experiment 3 setup and result.* — (a) cyclic straight line mission. (b) time history plot for 25m/s test to estimate wind speed. (c) power consumption plot of tests at different airspeeds.

## Key Equations

Identified parameters (Table III): `k₁ = 0.8554`, `k₂ = 0.3051 (kg/m)^{1/2}`, `c₁ = k₁/k₂ = 2.8037 (m/kg)^{1/2}`, `c₂ = 0.3177 (m/kg)^{1/2}`, `c₃ ≈ 0`, `c₄ = 0.0296 kg/m`, `c₅ = 0.0279 Ns/m`, `c₆ ≈ 0`.

Model summary (Eq. 14) in full:

$$
P(T, V_{vert}, V_{air}) = k_1 T\left[\frac{V_{vert}}{2} + \sqrt{\frac{V_{vert}^2}{4} + \frac{T}{k_2^2}}\right] + c_2 T^{3/2} + c_4 V_{air}^3
$$

with `T = √((mg − (c₅ V_air cos α)²)² + (c₄ V_air²)²)` under `c₆ = 0`.

## Results

Validation on a separate flight (ascend to 70 m AGL, rectangular loop at 10–20 m/s, land; wind neglected, airspeed ≈ ground speed), measured vs model energy (Table IV):

| Phase | Measured (J) | Model (J) | Diff (%) |
| --- | --- | --- | --- |
| Take off | 4.43e3 | 3.95e3 | 10.7 |
| Landing | 5.07e3 | 5.18e3 | 2.2 |
| Loop | 1.47e4 | 1.23e4 | 16.5 |

![[_papers/liu2017power/images/page_5_chart_9.jpg]]
*Fig. 9: The validation experiment is a rectangular loop at 70m AGL. The waypoints are shown as red squares, and the actual path in blue is overlaid with the desired path in black.*

The loop under-predicts because acceleration and deceleration add real energy the steady-state model omits, and wind at 70 m altitude is significant; actual ground speed never reaches the desired 25 m/s because of parasite drag.

## Limitations

Steady-state only (no acceleration phases), no wind modeling, single quadrotor airframe; parameters are airframe-specific. The paper notes wind estimation as future work. Funding: UARC at NASA Ames (Contract UCSCMCA-14-020) and NSF CNS-1136141. ^[inferred]

## Related

- [[concepts/multirotor-power-model-components]] — the reusable three-component decomposition
- [[concepts/nonlinear-drone-energy-function-in-routing]] — routing-level use of `P(q) = k(W+m+q)^{3/2}`, matching the hover law here
- [[concepts/payload-induced-drone-battery-consumption-rate]] — payload-aware consumption
- [[references/cheng2020-drone-routing-energy-function]] — energy function inside VRP
- [[references/dorling2017-drone-delivery-vrp]] — drone delivery VRP with energy constraints

## Sources

- [[_papers/liu2017power/liu2017power-extracted.md]]
- [[_papers/liu2017power/liu2017power.md]]
- [[_papers/liu2017power/images/page_1_image_7.jpg]]
- [[_papers/liu2017power/images/page_3_chart_11.jpg]]
- [[_papers/liu2017power/images/page_4_image_8.jpg]]
- [[_papers/liu2017power/images/page_4_chart_10.jpg]]
- [[_papers/liu2017power/images/page_4_chart_11.jpg]]
- [[_papers/liu2017power/images/page_4_chart_13.jpg]]
- [[_papers/liu2017power/images/page_5_chart_9.jpg]]
