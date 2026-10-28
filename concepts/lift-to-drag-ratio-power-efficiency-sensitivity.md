---
title: "Lift-to-Drag Ratio and Power Transfer Efficiency Sensitivity"
category: concepts
tags:
  - lift-to-drag-ratio
  - power-efficiency
  - drone-energy-models
  - parameter-sensitivity
  - calibration
  - route-optimization
aliases:
  - L over D in drone energy models
  - r and eta calibration
sources:
  - "[[_papers/zhang2021energy/zhang2021energy-extracted.md]]"
relationships:
  - target: "[[concepts/drone-energy-consumption-model-taxonomy]]"
    type: extends
  - target: "[[references/zhang2021-drone-energy-model-comparison]]"
    type: derived_from
  - target: "[[concepts/multirotor-power-model-components]]"
    type: related_to
summary: "Lift-to-drag ratio r and power transfer efficiency η are the two calibration knobs that reconcile drone energy models: setting r to 0.8–1.4 brings the lift-to-drag model in line with the component models, changing range by 49–160%."
base_confidence: 0.67
lifecycle: draft
lifecycle_changed: 2026-10-27
tier: supporting
created: 2026-10-27T09:25:00Z
updated: 2026-10-27T09:25:00Z
provenance:
  extracted: 0.80
  inferred: 0.20
  ambiguous: 0.00
---

> [!tldr] Two numbers decide whether two energy models can ever agree
> The lift-to-drag ratio `r = L/D` and the power transfer efficiency `η` (battery to propeller) are the parameters that make the thrust=drag models and the component models agree, and both are usually taken as constants. In a single common setting, adjusting `r` from 3 to 0.8–1.4 (small drone) or 0.7–1.4 (large drone) brings the lift-to-drag model's energy per metre down to the minima of the two- and three-component models, and the choice of model moves range by 49% to 160%.

## The parameters

- `r = L/D`, a dimensionless aerodynamic ratio, used as `T = W / r`. Measured values used in the literature: D'Andrea `r = 3` (constant, no speed dependence), Kirchstein `r = 3` fitted, Figliozzi `r = 2.4` implied by an 77.8 J/m rate for a 10.1 kg + 5 kg MD4-3000 at `η·η_r = 0.9 × 0.73 = 0.66`.
- `η` (battery-to-propeller efficiency) measured by Stolaroff from 1073 flight segments (η = 0.7); Kirchstein uses η = 0.73 with charging efficiency `η_c = 0.9`; D'Andrea's example uses η = 0.5; Figliozzi uses the combined 0.66.
- Related constants: specific energy `s_batt` = 540,000 J/kg, depth of discharge `γ` = 0.5, safety factor `f` = 1.2, air density ρ = 1.225 kg/m³, gravity g = 9.807.

## The convexity structure

- Induced power falls as `1/v_a`, parasite power grows as `v_a²`, profile power grows as `v_a`, so power is convex in airspeed with an interior optimum. `^[inferred]` Convexity is what the component models capture and the lift-to-drag and hovering models do not: a model that only scales weight by `r` produces a flat energy-per-metre curve, so it cannot answer the speed question at all.
- With a fixed `r`, the lift-to-drag model gives no optimal speed; in the common setting the minimum of the LD energy curve is simply the maximum tested speed.
- Kirchstein notes that a model including profile power requires a lower efficiency than a model excluding it, so R2 and R3 cannot share the same η. `^[inferred]` The parameters are not independent of the model structure: calibrating one model's η and transferring it to another model silently mis-scales the power.

## Numbers from the common setting

- Small drone (quad, 2.57 kg, 0.5 kg payload): LD 10.8 J/m at 12.5 m/s, range 10.4 km; RH 36.8 at 6 m/s, 3.1 km; R2 28.2 at 10 m/s, 4.0 km; R3 37.8 at 11 m/s, 3.0 km.
- Large drone (octocopter, 24 kg, 7 kg payload): LD 95.7 J/m, 11.8 km; RH 404.8 J/m, 2.8 km; R2 211.6 J/m at 13 m/s, 5.3 km; R3 415.8 J/m at 16 m/s, 2.7 km.
- R3 vs R2 at the optimal speed: +34% energy per metre and −25% range (small); +96% and −49% (large).
- LD vs R2 for the small drone: −62% energy per metre, +160% range.
- Setting `r` to 0.8–1.2 (small) or 0.7–1.4 (large) brings LD's energy per metre to the R2/R3 minima. `^[inferred]` Reconciliation by `r` alone means the model classes are not competing descriptions of physics — they are the same linear-in-weight law with different hidden parameters, and the honest parameter value is the one measured, not the one assumed.
- Range-versus-speed curves: LD flat, RH and LR increasing linearly, R2 and R3 following the convex shape, peaking near 4 km and 3 km for the small drone, 5.7 km and 2.9 km for the large.
- Payload effect: energy per metre rises roughly linearly, 20–40% from 0 to 7 kg; large-drone energy per metre is 6–10× the small-drone value in the same 0–0.5 kg band, so flying a large drone with a light payload is energy-inefficient.
- Range at increasing payload: LD 10.5–11.6 km (small) and 12.1–14.2 km (large), LR 2.0–2.4 km, RH and R3 3.0–3.5 km, R2 at 39–48% of LD.

## Consequences

- The same drone, the same battery, the same safety factor, and four models give ranges from 2.7 km to 11.8 km. `^[inferred]` For routing, the practical consequence is a different number of depots, a different set of reachable customers, and a different make-or-buy decision between drone and ground vehicle.
- The authors state the ranges are upper bounds because the common setting excludes hovering, takeoff and landing, vertical flight, avionics and wind, and report that actual range is lower.
- Wind is the largest single adjustment measured: a 30 km/h headwind triples the energy per metre (+261%), 45 km/h adds 129%; Kirchstein's complete flight profile with 10 km/h wind adds 70.1%. `^[inferred]` Because wind enters multiplicatively while `r` and `η` enter as constants, a wind term matters more than the choice between models.

## Related

- [[concepts/drone-energy-consumption-model-taxonomy]] — the model classes these parameters reconcile.
- [[references/zhang2021-drone-energy-model-comparison]] — the common-setting comparison producing the numbers above.
- [[concepts/multirotor-power-model-components]] — the three power components that make the energy curve convex.

## Limitations

- The parameters are measured on commercial off-the-shelf drones, not delivery-specific designs.
- `r` is treated as a constant in the models evaluated; a more sophisticated treatment would make it speed-dependent, as Stolaroff's η treatment is not.
- The parameter ranges (0.8–1.4) come from matching energy minima, not from measurements, so they are reconciling values, not validated ones.

## Sources

- [[_papers/zhang2021energy/zhang2021energy-extracted.md]] — Zhang, Campbell, Sweeney II, Hupman, *Transportation Research Part D: Transport and Environment*, 2021-01-01, DOI 10.1016/j.trd.2020.102668; zotero-key AAI27WZU.
