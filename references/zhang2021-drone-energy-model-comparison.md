---
title: "Zhang 2021 – Energy Consumption Models for Delivery Drones: A Comparison and Assessment"
category: references
tags: [energy-modeling, uav, paper]
aliases:
  - Zhang Campbell Sweeney Hupman 2021
  - drone Epm comparison
sources:
  - "[[_papers/zhang2021energy/zhang2021energy-extracted.md]]"
  - "[[_papers/zhang2021energy/zhang2021energy.md]]"
  - "[[_papers/zhang2021energy/images/page_11_chart_2.jpg]]"
  - "[[_papers/zhang2021energy/images/page_14_chart_2.jpg]]"
  - "[[_papers/zhang2021energy/images/page_16_chart_2.jpg]]"
  - "[[_papers/zhang2021energy/images/page_16_chart_5.jpg]]"
relationships:
  - target: "[[concepts/drone-energy-consumption-model-taxonomy]]"
    type: related_to
  - target: "[[concepts/lift-to-drag-ratio-power-efficiency-sensitivity]]"
    type: related_to
  - target: "[[references/liu2017power]]"
    type: derived_from
summary: "Zhang et al. (TR-D 2021) unify notation for 12 drone energy models; Epm spans 16 to 400 J/m, factor 3-5 spread on one drone, so model choice changes range and emissions."
base_confidence: 0.67
lifecycle: draft
lifecycle_changed: 2026-10-27
tier: supporting
created: 2026-10-27T08:15:00Z
updated: 2026-10-30T17:41:00Z
provenance:
  extracted: 0.92
  inferred: 0.08
  ambiguous: 0.00
---

> [!tldr] Twelve published models, one drone, Epm from 16 to over 400 J/m
> Zhang, Campbell, Sweeney & Hupman (Transportation Research Part D, 2021) classify drone energy consumption models by thrust assumption, travel components covered and adjustments, restate them in a unified notation, then evaluate five fundamental models on two prototypical drones with identical parameters. Steady-level-flight energy per metre spans under 20 J/m to over 400 J/m in the literature, and on the common drone the models differ by a factor of 3–5, which is enough to change route, fleet and emissions conclusions.

## Why this matters

- Drone energy requirements determine range, endurance, cost and emissions, yet many optimization models use energy only indirectly as a fixed flight-time or flight-distance limit (Murray & Chu 2015; Chiang et al. 2019; Kitchacharoenchai et al. 2020), while others embed an explicit model (Kirchstein 2020; Murray & Raj 2020; Poikonen & Golden 2020; Stolaroff et al. 2018; Figliozzi 2017; Dorling et al. 2017).
- Fixed rates in the literature are wildly inconsistent: Ferrandez et al. (2016) use 46.1 J/m (2013 Amazon drone, 5 lb at 70 km/hr), Moore (2019) uses 223.7 J/m (DJI Matrice 600 Pro field tests by the U.S. Department of Energy 2019, 2020), Goodchild & Toy (2018) test 22–223 J/m (10–100 Wh/mile) and find that drone emissions benefits relative to trucks depend strongly on the rate.
- Trucks and cars have fuel-consumption standards from decades of research (Barth et al. 2005); drones do not, and drone operations are more sensitive to energy capacity than ground vehicles (Cheng et al. 2020).

## Factor map

- Four factor categories: **drone design** (weight, size, rotor count/size, battery weight and capacity, power transfer efficiency, max speed and payload, lift-to-drag ratio, delivery mechanism, avionics), **environment** (air density, gravity, wind, weather, ambient temperature, operating regulations), **drone dynamics** (speed, motion type, acceleration, angle of attack, altitude, riding on trucks or public transit), **delivery operations** (payload weight/size, empty returns, fleet size and mix, deliveries per trip, delivery mode, service region).
- Five interrelated aspects: payload weight, battery weight, airframe weight, airspeed, range. The three weights (+) increase the energy rate; airspeed has a (+/−) effect because power is approximately convex in airspeed (induced, parasite and profile drag competing); the energy rate plus battery weight/capacity determines range. `^[inferred]` The battery trade-off is the crux: a heavier battery raises the energy rate, lowering range, while adding capacity, raising it.
- Drones carried on other vehicles expend little or no energy; landing, tether-lowering and parachute drops use different amounts; paired truck-drone or multi-drone coordination can force substantial hovering.

## Three thrust assumptions define three literature streams

- (i) thrust equals drag and lift equals weight, so `T = W / r` with `r = L/D`; (ii) thrust equals weight, as for a hovering helicopter; (iii) thrust equals the sum of weight, drag and lift. The assumption encodes whether the model treats the drone as a fixed-wing aircraft or a helicopter.

## Table 1: 12 key models scored by features

- D'Andrea (2014): `T = W/r`, horizontal, wind, avionics, theoretical. Figliozzi (2017): `T = W/r`, horizontal, empty return, theoretical. Dorling et al. (2017): `T = W`, horizontal + hover + vertical, regression, field tests. Tseng et al. (2017a/b): horizontal + hover + vertical, wind, avionics, regression, field tests. Liu et al. (2017): `T = W + D + L`, all three components, wind, theoretical, field tests. Lohn (2017) and Xu (2017): `T = W/r`, all components, wind, avionics, empty return, theoretical. Stolaroff et al. (2018): `T = W + D + L`, horizontal, wind, theoretical, field tests. Troudi et al. (2018): `T = W/r`, horizontal, avionics, theoretical. Jeong et al. (2019): `T = W`, horizontal, wind, theoretical, field tests. Kirchstein (2020): `T = W + D + L`, all components, wind, avionics, empty return, theoretical.
- All 12 models include horizontal travel; **only half include hovering and vertical travel**; only 2 of 12 include none of the wind/avionics/empty-return adjustments; 10 papers give theoretical models, 3 give regression, 5 include field tests.
- Murray & Raj (2020) is the only reference using multiple energy models in one study (Liu et al.'s model, a simple regression linear in payload, and fixed distance/time limits) and finds that different models produce very different routes, several energy-infeasible, and that energy outside steady level flight (launch, retrieval, delivery, truck-coordination hovering) must be included.

## Unified notation and the five fundamental models

- Notation: air density `ρ`, gravity `g`, induced speed `v_i`, airspeed `v_a`, headwind ratio `φ` so ground speed `v = (1 − φ)v_a`, one-way distance `d`, lift-to-drag ratio `r`, power transfer efficiency `η` (battery to propeller), charging efficiency `η_c`, component index k = body/battery/payload, drag coefficients `C_{D_k}`, projected areas `A_k`, masses `m_k`, depth of discharge `γ`, specific energy `s_batt`, safety factor `f`, maximum one-way range `R`, power `P`, avionics power `P_avio`, rotors `n`, blades `N`, blade chord `c`, blade drag `c_d`, rotor disc area `ς`, angle of attack `α`, energy per metre `Epm`.
- `R = m_2 · s_batt · γ / ((Epm_loaded + Epm_unloaded) · f)` — the range formula used for every model in the common setting.
- Table 5 gives five models: **LD** (D'Andrea, `Epm = Σ m_k g / (r η)`), **RH** (Dorling hovering, `Epm = (Σ m_k g)^{3/2} / (η v_a √(2 n ρ ς))`), **R2** (Stolaroff two-component), **R3** (Kirchstein three-component with profile power), **LR** (Tseng regression `Epm = −2.595 + (0.197 m_2 + 251.7)/v_a` for small payloads below 5 m/s).
- Equations 1–23 restate every published model in this notation, including D'Andrea's `P = (Σ m_k) g v_a / (r η) + P_avio` (eq. 2, the 370 constant in eq. 1 converts km/h), Figliozzi's empty-return average `Epm = ½(gΣm_k/(r(v)ηη_r) + gΣm_{k≤2}/(r(v)ηη_r))` (eq. 5), Kirchstein's four-term Epm with lifting-power markup κ and downwash coefficient w (eq. 21), and Liu's thrust `T = √((Σ m_k g − c_5(v_a cos α)²)² + (½ρΣ C_{D_k}A_k v_a²)²)` (eq. 18).

![[_papers/zhang2021energy/images/page_11_chart_2.jpg]]
*Fig. 3. Epm results from baseline models in Tables 3a and 3b.*

## Literature Epm values, one point per model

- Micro drones with payload ≤ 1 kg and airspeed ≤ 6 m/s cluster at 15.7–107.3 J/m; payloads 1.15–2.5 kg at 12–23 m/s give 39.2–168.0 J/m; the heaviest drone (Stolaroff octocopter, 7 kg payload) gives **436.7 J/m**, more than 5× the next-largest.
- Table 3b values: Liu 17.3 J/m (takeoff 1.46 kg, battery 204 KJ, 637 KJ/kg), Stolaroff quad 47.4, Dorling hovering 15.7, Dorling regression 48.9–85.1, Tseng T1 47.7–67.4, Tseng T2 85.3–107.3, D'Andrea 39.2, Figliozzi 77.8, Kirchstein 127.2, Stolaroff octocopter 436.7, Xu 168.0 J/m.
- Field-test calibration matters: Dorling's hovering equation predicted **4.5–5× less** power than the measured hovering with 0.5–1.5 kg payloads; Liu's model underestimated ascent by 10.7%, horizontal flight by 16.3%, overestimated descent by 2.2%, total by 11.4%; ascending/descending consumed 39% of a short loop's energy vs 4.5% of a 10 km trip.
- Adjustments (Table 4): avionics +20% (D'Andrea) and +3.4% (Kirchstein); 30 km/h wind +261%; 45 km/h wind +129%; Kirchstein's complete flight profile with 10 km/h wind +70%; Figliozzi's adverse weather +50% and a future advanced drone −50%; Xu's larger drone with 9.2 kg payload +213% and an advanced design −82.7%.
- `^[inferred]` Steady-level-flight Epm therefore systematically understates a real trip; the profile phases and wind dominate the totals, which is why route models that use a single fixed J/m figure carry unquantified risk.

![[_papers/zhang2021energy/images/page_14_chart_2.jpg]]
*Fig. 4. Energy consumption rate versus airspeed for small and large drones.*

## Common-setting results

- Common parameters (Table 6): ρ = 1.225 kg/m³, g = 9.807, φ = 0, empty return on, `s_batt` = 540,000 J/kg, η = 0.7, f = 1.2, γ = 0.5. Small drone: quadcopter, 4 blades of chord 0.0157 m, `c_l` 0.271, `c_d` 0.012, 4 rotors of disc area 0.0507 m², body 1.07 kg, battery 1 kg, payload 0.5 kg, areas 0.0599/0.0037/0.0135 m², drag coefficients 1.49/1/2.2, r = 3, no avionics, κ = 1, κ₂ 0.790, κ₃ 0.0042, parasite factors 0.075 loaded and 0.057 unloaded. Large drone: octocopter, 3 blades of chord 0.1 m, `c_l` 0.4, `c_d` 0.075, 8 rotors of 0.027 m², body 7 kg, battery 10 kg, payload 7 kg, areas 0.224/0.015/0.0929, κ₂ 0.683, κ₃ 0.0868, parasite factors 0.339/0.214; its battery carries 10× the energy of the small drone.
- Epm-minimising speed and range (Table 7): small drone LD 10.8 J/m at 12.5 m/s and 10.4 km, RH 36.8 at 6 m/s and 3.1 km, R2 28.2 at 10 m/s and 4.0 km, R3 37.8 at 11 m/s and 3.0 km. Large drone: LD 95.7 J/m and 11.8 km, RH 404.8 J/m and 2.8 km, R2 211.6 J/m at 13 m/s and 5.3 km, R3 415.8 J/m at 16 m/s and 2.7 km.
- At the optimal speed R3 estimates 34% higher Epm and 25% shorter range than R2 for the small drone, and 96% higher Epm with 49% shorter range for the large drone; LD gives 62% lower Epm and 160% longer range than R2 for the small drone.
- Adjusting r to 0.8–1.2 (small) or 0.7–1.4 (large) would bring LD in line with the energy-minimising values of R2 and R3. `^[inferred]` Model choice and parameter choice are inseparable: the r value alone reconciles the classes.
- Range vs airspeed: LD is flat, RH and LR increase linearly, R2 and R3 follow the convex Epm shape, maxing near 4 km and 3 km (small) and 5.7 km and 2.9 km (large). Payload increases Epm roughly linearly, by 20–40% from 0 to 7 kg; large-drone Epm is 6–10× the small-drone Epm in the same 0–0.5 kg payload band, so flying a large drone with a small payload is energy-inefficient.
- Range falls with payload for every model: LD 10.5–11.6 km (small) and 12.1–14.2 km (large), LR 2.0–2.4 km, RH and R3 3.0–3.5 km, R2 39–48% of LD.

![[_papers/zhang2021energy/images/page_16_chart_2.jpg]]
*Fig. 6. Energy consumption rate versus payload for small and large drones.*

![[_papers/zhang2021energy/images/page_16_chart_5.jpg]]
*Fig. 7. Maximum range versus payload for small and large drones.*

## Manufacturer data cannot substitute

- `Epm = BatteryEnergy / FlightDistance` (eq. A1) and `BatteryEnergy (J) = Capacity (mAh) × Voltage (V) × 3.6` (eq. A2), but flight distance is not reported consistently; `FlightDistance = FlightSpeed × FlightTime` (eq. A3) is unreliable because manufacturers report maxima.
- Table A1 (7 drones): Mavic Spark 0.30 kg, 16 min at 5.56 m/s, max hover 15 min, max speed 13.9 m/s, max distance 9 km, 60,739 J, Epm 6.7 J/m; Mavic Air 0.43 kg, 21 min at 6.94, 20 min hover, 19.0 m/s, 10 km, 98,753 J, 9.9; Mavic Pro 0.73 kg, 27 min at 6.94, 24 min, 18.1, 13 km, 157,183 J, 12.1; Mavic 2 Pro 0.91 kg, 31 min at 6.94, 29 min, 20.0, 18 km, 213,444 J, 11.9; Phantom 4 Pro V2.0 1.38 kg, 30 min at 5.56, 28 min, 20.0, 14 km, 321,206 J, 22.9; 3DR-Solo 1.8 kg, 20 min, 25.0 m/s, 8 km, 277,056 J, 34.6; MD4-3000 11.0 kg, 45 min, 20.25 m/s, 36 km, 2,797,200 J, 77.7.
- Hover-time × max speed gives distances about 2× the reported flight distance; time × speed at the stated cruise speed gives 13–40% less than the reported distance.
- Safety factors used in practice: Figliozzi flies 70% of max distance, Stolaroff f = 1.2 (83.3%), Troudi f = 1.25 (80%).

## Conclusions

- The authors' goal is not to pick a preferred model: all models examined can agree with appropriate parameters, and the calibration is what matters, which needs flight measurement. `^[inferred]` The paper is best read as a warning that energy-model choice propagates into route feasibility, fleet size, depot count and emissions policy.
- Field experiments are needed to establish standards analogous to vehicle fuel-efficiency labels, ideally in partnerships between government agencies (U.S. Department of Energy, EPA), universities and industry; avionics and wind need particular attention, and research should identify when a parsimonious model is accurate enough.
- Linking energy models to route optimization and strategic delivery system design is named as the key open research area, with airspeed and wind given more weight than in ground delivery models.

## Related

- [[concepts/drone-energy-consumption-model-taxonomy]] — the classification this paper proposes.
- [[concepts/lift-to-drag-ratio-power-efficiency-sensitivity]] — the parameter mechanism behind the spread.
- [[concepts/multirotor-power-model-components]] — the three-component structure behind R3.
- [[concepts/payload-induced-drone-battery-consumption-rate]] — regression energy rates used in routing models.
- [[references/dorling2017-drone-delivery-vrp]] — hovering model and field tests scored in Table 1.
- [[references/liu2017power]] — the three-component model with profile power.

## Limitations

- The scope is battery-powered aerial drones only.
- The common setting excludes hovering, takeoff/landing, vertical flight, avionics and wind, so the reported ranges are upper bounds; the authors say actual range is lower.
- Many published parameter values come from commercial off-the-shelf drones, not delivery-specific designs.
- The LD model as evaluated has no speed-dependent lift-to-drag ratio, which the authors note a more sophisticated version would use.

## Sources

- [[_papers/zhang2021energy/zhang2021energy-extracted.md]] — Zhang, Campbell, Sweeney II, Hupman, *Transportation Research Part D: Transport and Environment*, 2021-01-01, DOI 10.1016/j.trd.2020.102668; zotero-key AAI27WZU.
