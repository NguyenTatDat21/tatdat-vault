---
title: "Drone Energy Consumption Model Taxonomy"
category: concepts
tags:
  - drone-energy-models
  - energy-consumption
  - taxonomy
  - unmanned-air-vehicle
  - route-optimization
aliases:
  - drone Epm model classes
  - three thrust assumptions
sources:
  - "[[_papers/zhang2021energy/zhang2021energy-extracted.md]]"
relationships:
  - target: "[[references/zhang2021-drone-energy-model-comparison]]"
    type: derived_from
  - target: "[[concepts/multirotor-power-model-components]]"
    type: uses
  - target: "[[concepts/lift-to-drag-ratio-power-efficiency-sensitivity]]"
    type: related_to
  - target: "[[concepts/payload-induced-drone-battery-consumption-rate]]"
    type: related_to
summary: "Drone energy models split by thrust assumption (lift-to-drag, thrust=weight, thrust=weight+drag+lift), by travel components covered, and by adjustments for wind, avionics, and empty return; spread spans 16 to over 400 J/m."
base_confidence: 0.67
lifecycle: draft
lifecycle_changed: 2026-10-27
tier: supporting
created: 2026-10-27T09:20:00Z
updated: 2026-10-27T09:20:00Z
provenance:
  extracted: 0.91
  inferred: 0.09
  ambiguous: 0.00
---

> [!tldr] Three questions locate any drone energy model
> A drone energy model is located by three answers: which thrust assumption it uses, which travel components it integrates, and which adjustments it makes. Published steady-level-flight values span under 20 J/m to over 400 J/m, and **only half of the 12 key models include hovering and vertical travel**.

## The three thrust assumptions

- (i) **lift-to-drag stream**: thrust equals drag and lift equals weight, so `T = W / r` with `r = L/D`; models: D'Andrea 2014, Figliozzi 2017, Lohn 2017, Xu 2017, Troudi 2018.
- (ii) **thrust = weight stream**: as for a hovering helicopter; models: Dorling 2017, Jeong 2019.
- (iii) **thrust = weight + drag + lift stream**: models: Liu 2017, Stolaroff 2018, Kirchstein 2020.
- The assumption encodes whether the drone is treated as a fixed-wing aircraft or a helicopter, and it drives the power equation. `^[inferred]` Streams (i) and (ii) are the extremes: the fixed-wing view credits aerodynamic lift, the helicopter view charges the full weight; stream (iii) is the compromise for a multirotor producing both lift and forward thrust at the same time.
- Energy per metre is obtained by dividing power by ground speed, `Epm = P / ((1 − φ)v_a)`, where `φ` is the headwind ratio, so ground speed `v = (1 − φ)v_a`.

## The five fundamental models

- **LD** (D'Andrea 2014): `Epm = Σ m_k g / (r η)` — power grows linearly with airspeed, so energy per metre is flat.
- **RH** (Dorling 2017, hovering): `Epm = (Σ m_k g)^{3/2} / (η v_a √(2nρς))` — `P = (Σ m_k g)^{3/2} / √(2nρς)`; `Epm` decreases with airspeed, so longer flights are more efficient per metre.
- **R2** (Stolaroff 2018): `Epm = T(v_a sin α + v_i)/(v_a η)` with `T = Σ m_k g + ½ρΣ C_{D_k}A_k v_a²`, `v_i = T/(½ρv_a²S_wing)` — convex in airspeed.
- **R3** (Kirchstein 2020): `Epm = 1/η(κTw/v_a + ½ρΣC_{D_k}A_k v_a² + κ₂(Σm_k g)^{1.5}/v_a + κ₃(Σm_k g)^{0.5}v_a)` — adds a third profile-power term.
- **LR** (Tseng 2017): `Epm = −2.595 + (0.197 m₂ + 251.7)/v_a` — a nonlinear regression on horizontal/vertical speed, acceleration, payload, and wind (9 coefficients), valid for small payloads below 5 m/s; the Matrice 100 form is `Epm = −1.526 + (0.220 m₂ + 433.9)/v_a`.
- The convex models R2/R3 have an interior optimum speed; LD and LR do not have a convex shape in the tested range, so they never find an optimum. `^[inferred]` The convexity difference is the most consequential structural property: only the models that include parasite and profile power can answer the question "at what speed should this drone fly".

## Range formula

- `R = m₂ · s_batt · γ / ((Epm_loaded + Epm_unloaded) · f)` — battery mass × specific energy × depth of discharge, divided by the round-trip energy rate scaled by the safety factor.
- Safety factors in the literature: Figliozzi flies 70% of max distance; Stolaroff f = 1.2 (83.3%); Troudi f = 1.25 (80%).
- Manufacturer data cannot replace a model: `BatteryEnergy(J) = Capacity(mAh) × Voltage(V) × 3.6`, and `FlightDistance = FlightSpeed × FlightTime` is unreliable because manufacturers report maxima — hover time × max speed gives about 2× the reported flight distance, cruise time × cruise speed 13–40% less.
- Table A1 (7 commercial drones): Mavic Spark 0.30 kg, 16 min at 5.56 m/s, max hover 15 min, 13.9 m/s, 9 km, 60,739 J, **6.7 J/m**; Mavic Air 0.43 kg, 21 min at 6.94, 20 min, 19.0, 10 km, 98,753 J, 9.9; Mavic Pro 0.73 kg, 27 min at 6.94, 24 min, 18.1, 13 km, 157,183 J, 12.1; Mavic 2 Pro 0.91 kg, 31 min at 6.94, 29 min, 20.0, 18 km, 213,444 J, 11.9; Phantom 4 Pro V2.0 1.38 kg, 30 min at 5.56, 28 min, 20.0, 14 km, 321,206 J, 22.9; 3DR-Solo 1.8 kg, 20 min, 25.0, 8 km, 277,056 J, 34.6; MD4-3000 11.0 kg, 45 min, 20.25, 36 km, 2,797,200 J, 77.7 J/m.

## Adjustments the models add

- Avionics: D'Andrea +20% power (P_avio = 100 J/s on a 6 kg drone at 47.2 J/m), Kirchstein +3.38% (131.5 → 135.9 J/m).
- Wind: 30 km/h headwind **+261%** (D'Andrea, 47.2 → 141.6 J/m); 45 km/h **+129%** (Kirchstein, 216.4 → 300.6); Kirchstein's full flight profile with 10 km/h wind **+70.1%** (127.2 → 216.4).
- Empty return: Figliozzi averages the loaded and unloaded rates, `Epm = ½(gΣm_k/(r(v)ηη_r) + gΣm_{k≤2}/(r(v)ηη_r))`.
- Adverse weather +50% (Figliozzi, 77.8 → 116.7); an advanced future drone −50% (38.9); Xu's larger drone with 9.2 kg payload +213% (168.0 → 525.0); Xu's advanced design −82.7% (168.0 → 29.0).
- Delivery mechanism: a drone carried by another vehicle uses little energy; landing, tether-lowering, parachute drops and truck-coordination hovering use substantially more.

## Field calibration

- Dorling's hovering equation predicted **4.5–5× less** power than measured hovering with 0.5–1.5 kg payloads.
- Liu's model underestimated ascent by 10.7%, horizontal flight by 16.3%, descent by −2.2%, total by 11.4%; ascending/descending used 39% of a short loop's energy versus 4.5% of a 10 km trip; Liu's calibrated constants `κ₁ = 0.8554`, `c₂ = 0.3177 (m/kg)^{1/2}`.
- Stolaroff fitted η from 1073 measured flight segments in winds up to 7 m/s (η = 0.7).
- Dorling's regression `P = β₁(m₂ + m₃) + β₀` with β₁ = 46.7 J/s-kg, β₀ = 26.9 J/s (ArduCopter Hexa-B, n = 6, ς = 0.2 m², m₁ = 1.5 kg); energy rate `Epm = (217(m₂+m₃)+185)/v_a` at 14.8 V, `(171(m₂+m₃)+187)/v_a` at 11.1 V.

## Consequences for routing models

- Published steady-level rates: Liu 17.3, Dorling hover 15.7, Stolaroff quad 47.4, D'Andrea 39.2, Tseng T1 47.7–67.4, Tseng T2 85.3–107.3, Dorling regression 48.9–85.1, Figliozzi 77.8, Kirchstein 127.2, Xu 168.0, Stolaroff octocopter 436.7 J/m.
- Micro drones (payload ≤ 1 kg, ≤ 6 m/s) span 15.7–107.3 J/m, a factor of six.
- Fixed rates used in routing: 46.1 J/m (Amazon 2013, Ferrandez), 223.7 J/m (DJI Matrice 600 Pro, Moore), 22–223 J/m (Goodchild & Toy), where the drone-versus-truck emissions benefit depends on which rate is chosen.
- Murray & Raj (2020) found that using Liu's model, a payload-linear regression, and fixed distance limits produces very different routes, several infeasible, and that non-steady energy must be included.
- The authors' conclusion: all models can agree with appropriate parameters, calibration matters, and calibration requires measurement. `^[inferred]` The practical reading is that a routing model should carry the energy assumptions explicitly — the rate, the profile coverage, the wind term, the safety factor — because each of those choices changes which routes are feasible.

## Related

- [[references/zhang2021-drone-energy-model-comparison]] — the 12-model comparison and common-setting evaluation.
- [[concepts/multirotor-power-model-components]] — the three-component power structure behind R3.
- [[concepts/lift-to-drag-ratio-power-efficiency-sensitivity]] — the parameter that reconciles model classes.
- [[concepts/payload-induced-drone-battery-consumption-rate]] — regression rates used inside routing models.

## Sources

- [[_papers/zhang2021energy/zhang2021energy-extracted.md]] — Zhang, Campbell, Sweeney II, Hupman, *Transportation Research Part D: Transport and Environment*, 2021-01-01, DOI 10.1016/j.trd.2020.102668; zotero-key AAI27WZU.
