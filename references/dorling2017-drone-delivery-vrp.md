---
title: Vehicle Routing Problems for Drone Delivery (Dorling et al., 2017)
category: references
tags: [vrp, drone-delivery, multirotor-energy-model, battery-weight, simulated-annealing, dantzig-wolfe]
relationships:
  - target: "[[concepts/payload-induced-drone-battery-consumption-rate]]"
    type: uses
  - target: "[[concepts/nonlinear-drone-energy-function-in-routing]]"
    type: related_to
  - target: "[[references/cheng2020-drone-routing-energy-function]]"
    type: related_to
  - target: "[[concepts/exact-multitrip-vrptw-framework]]"
    type: related_to
  - target: "[[references/mutlu2016-lng-annual-delivery-program]]"
    type: related_to
  - target: "[[references/yang2022-vrpd-bilevel-heuristic]]"
    type: related_to
  - target: "[[references/hendel2022-adaptive-lns-for-mip]]"
    type: related_to
  - target: "[[concepts/bilevel-vrpd-task-assignment-routing]]"
    type: related_to
  - target: "[[concepts/multirotor-power-model-components]]"
    type: related_to
  - target: "[[references/ahmadi-javid2022-drone-delivery-energy-formulation]]"
    type: related_to
  - target: "[[references/liu2017power]]"
    type: related_to
  - target: "[[references/murray2015flying]]"
    type: related_to
  - target: "[[references/torabbeigi2020-payload-bcr-drone-scheduling]]"
    type: related_to
sources:
  - _papers/dorling2017vehicle/dorling2017vehicle-extracted.md
  - _papers/dorling2017vehicle/dorling2017vehicle.md
  - _papers/dorling2017vehicle/images/page_3_chart_1.jpg
  - _papers/dorling2017vehicle/images/page_3_chart_10.jpg
  - _papers/dorling2017vehicle/images/page_10_image_10.jpg
  - _papers/dorling2017vehicle/images/page_10_chart_12.jpg
  - _papers/dorling2017vehicle/images/page_11_chart_1.jpg
  - _papers/dorling2017vehicle/images/page_13_chart_12.jpg
  - _papers/dorling2017vehicle/images/page_13_chart_14.jpg
summary: "Adds a measured linear multirotor power model, battery weight as payload, drone reuse, and per-route battery optimization to VRP, with two Dantzig-Wolfe MILP variants and simulated annealing."
provenance:
  extracted: 0.91
  inferred: 0.09
  ambiguous: 0.00
base_confidence: 0.67
lifecycle: draft
lifecycle_changed: 2026-10-22
tier: core
created: 2026-10-22T23:45:17Z
updated: 2026-10-30T14:38:55Z
---

# Vehicle Routing Problems for Drone Delivery (Dorling et al., 2017)

> [!tldr] This paper formulates drone-only multi-trip delivery VRPs that explicitly model payload/battery effects on energy, then solves minimum-cost and minimum-time variants with MILP and simulated annealing.

## Problem & Contribution

The paper argues classical VRPs miss key drone-delivery realities:
- multiple depot returns and vehicle reuse,
- payload- and battery-dependent energy draw,
- tight coupling between route choice, battery size, and feasibility.

![[_papers/dorling2017vehicle/images/page_3_chart_10.jpg]]

*Fig. 2 (paper): An example showing two drones flying three different routes.*

It introduces two variants:
- **MC-DDP** (minimum cost),
- **MT-DDP** (minimum overall delivery time).

## Energy Model

A practical linear approximation for multirotor power is used:

$$
p(m)=\alpha m + \beta
$$

where `m` is battery+payload mass, `\alpha` is marginal power-per-kg, and `\beta` is baseline hover power.

The paper reports fitted values (hexacopter setting) around:
- $\alpha \approx 46.7$ W/kg
- $\beta \approx 26.9$ W
- The linear fit over $0 \le m \le 3$ kg has mean percent error 3.1% and largest difference 6.3 W; widening $m$ to 0–10 kg raises mean percent error to 12.8% and the largest difference to about 51 W, so the approximation should not be extrapolated to heavier payloads. ^[inferred]

![[_papers/dorling2017vehicle/images/page_3_chart_1.jpg]]

*Fig. 1 (paper): The linear approximation (3) fitted to the power consumption model (2), assuming n = 6 rotors, a fluid density of ρ = 1.204 kg/m³, a rotor disc area of ς = 0.2 m², and a frame weight W = 1.5 kg*

- Hover, straight flight and altitude-change power measurements on the same airframe are close: 15.6/19.9 W/kg with 311 W hover, 15.3/19.8 W/kg with 304 W straight flight, 14.7/20.3 W/kg with 297 W altitude change (Table I).

![[_papers/dorling2017vehicle/images/page_10_image_10.jpg]]

*(a) The hexacopter path during the straight flight manoeuvre. Map data and image © 2015 Google.*

![[_papers/dorling2017vehicle/images/page_10_chart_12.jpg]]

*(b) Hexacopter altitude while performing altitude changes.*

*Fig. 4 (paper): Hexacopter manoeuvre information.*

![[_papers/dorling2017vehicle/images/page_11_chart_1.jpg]]

*Fig. 5 (paper): Hexacopter energy consumption for various battery and payload weights m, with corresponding energy consumption model values.*

The linear fit over $0 \le m \le 3$ kg has mean percent error 3.1% and largest difference 6.3 W; widening $m$ to 0–10 kg raises mean percent error to 12.8% and the largest difference to about 51 W.

## Optimization Pattern

- MILP captures routing, reuse, timing, energy, capacity, and budget constraints. ^[inferred]
- SA explores string-based solutions `s = [0 r1 0 r2 0 … rR 0]`, where `0` is the depot and neighbouring zeros mark empty routes, using swap, relocate, and 2-opt moves with Metropolis acceptance (initial temperature Υ₀ = 1, final Υ′ = 0.001, cooling μ = 0.9, Λ = 1000 rounds per cooling phase).
- Per-route battery weight is found by binary search on the route cost function, and discrete battery sizes turn the choice into a minimum knapsack problem.

## Results

| Item | Finding |
| --- | --- |
| Small MILP and SA comparison | SA is near-optimal for up to 8 locations; MT-DDP: MILP 5.40–9.63 min with runtimes from 0.97 s to 116.98 s, SA 5.48–9.83 min in 0.24–0.31 s; MC-DDP: MILP 0.99–1.22 k$ with runtimes from 9.47 s to 1,116.87 s, SA 1.00–1.26 k$ in 0.19–0.24 s |
| Hardware | 3D Robotics ArduCopter Hexa-B hexacopter, six 850 RPM/V motors, 10×4.6 APC slow-fly propellers, Arduino flight controller running firmware 3.0.1 of the APM 2.5 autopilot, u-blox LEA-6 GPS with 4 mm ceramic patch antenna, 4-cell 14.8 V LiPo battery |
| Simulation parameters | Drone cost F = \$500, carrying capacity Q = 3 kg including battery and payload, α = 0.217 kW/kg, β = 0.185 kW, speed v = 6 m/s, service time τ = 60 s per location, energy density ξ = 650 kJ/kg, energy price ε = \$0.1 per kJ |
| Larger SA runs | MT-DDP: 12.19–104.75 min with μ = 0.99 vs 13.28–117.82 min with μ = 0.9; MC-DDP: 13.52–65.57 k$ vs 13.99–75.13 k$ |
| Cooling schedule | Raising μ from 0.9 to 0.99 improves MT-DDP time and MC-DDP cost by up to 15% for about 10× runtime (18.45 → 181.41 s, 57.11 → 497.65 s); 0.99 → 0.999 adds at most 5% for another 10×, so the paper uses μ = 0.99; standard deviations are largest when location counts are high and μ is low |
| Reuse and battery optimization | Drone reuse passes the about \$113,000 cost limit reached without reuse at 500 nodes; optimizing battery weight per route improves cost by 13% over a fixed 0.3 kg battery and delivery time by about 22% over a fixed 0.25 kg, and a 15% cost gain at b = 0.3 kg vs 0.5 kg and an 80% time gain at b = 0.25 kg vs 0.45 kg (500 locations, 1 km²) |

![[_papers/dorling2017vehicle/images/page_13_chart_12.jpg]]

*Fig. 9 (paper): Costs found by the MC-DDP when every drone’s battery weighs b kg, with a time limit of 30 minutes on a 1 km² field with 500 nodes.*

![[_papers/dorling2017vehicle/images/page_13_chart_14.jpg]]

*Fig. 10 (paper): Delivery times found by the MT-DDP when every drone’s battery weighs b kg, with a budget of \$10,000 on a 1 km² field with 500 nodes.*

## Limitations
- The linear power model is fitted over 0–3 kg: mean percent error 3.1% and largest difference 6.3 W. Widening the fit to 0–10 kg raises mean percent error to 12.8% and the largest difference to about 51 W, so the approximation should not be extrapolated to heavier payloads.
- Weather, wind, battery aging, and maintenance costs are ignored, batteries are assumed purchased fully charged, recharging is handled by the depot, and multiple depots are not modelled. ^[extracted]
- Hover power is an upper bound on flight power because translational lift reduces required power, so energy estimates are conservative. ^[extracted]
- Battery-reuse experiments for the time-minimizing variant were not reported for budgets below $35,000 because the solver found no solutions. ^[extracted] ^[inferred]
- Per-route battery optimization can be less effective for small areas and low node counts. ^[extracted]

## Related

- [[concepts/payload-induced-drone-battery-consumption-rate]]
- [[concepts/nonlinear-drone-energy-function-in-routing]]
- [[references/cheng2020-drone-routing-energy-function]]
- [[concepts/exact-multitrip-vrptw-framework]]
- [[references/tamke2023-vrpd-dss]]

## Bibliographic Record

- Citation key: `dorling2017vehicle`
- DOI: `10.1109/TSMC.2016.2582745`
- Canonical URL: <https://doi.org/10.1109/TSMC.2016.2582745>
- Publication: *IEEE Transactions on Systems, Man, and Cybernetics: Systems* (2017)
- Authors: Kevin Dorling; Jeremy Heinrichs; Geoff G. Messier; Sébastien Magierowski
- Companion metadata note: [[_papers/dorling2017vehicle/dorling2017vehicle.md]]

## Sources

- [[_papers/dorling2017vehicle/dorling2017vehicle-extracted.md]]
- [[_papers/dorling2017vehicle/dorling2017vehicle.md]]
