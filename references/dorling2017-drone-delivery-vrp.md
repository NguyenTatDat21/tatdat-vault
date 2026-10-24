---
title: Vehicle Routing Problems for Drone Delivery (Dorling et al., 2017)
category: references
tags: [VRP, drone-delivery, multirotor-energy-model, battery-weight, simulated-annealing, Dantzig-Wolfe]
relationships:
  - target: "[[concepts/payload-induced-drone-battery-consumption-rate]]"
    type: uses
  - target: "[[concepts/nonlinear-drone-energy-function-in-routing]]"
    type: related_to
  - target: "[[references/cheng2020-drone-routing-energy-function]]"
    type: related_to
  - target: "[[concepts/exact-multitrip-vrptw-framework]]"
    type: related_to
sources:
  - _papers/dorling2017vehicle/dorling2017vehicle-extracted.md
  - _papers/dorling2017vehicle/dorling2017vehicle.md
summary: >-
  Defines multi-trip drone-delivery VRPs with battery/payload-aware energy,
  derives a practical linear power model, and combines MILP and simulated
  annealing for cost/time objectives.
provenance:
  extracted: 0.88
  inferred: 0.09
  ambiguous: 0.03
base_confidence: 0.67
lifecycle: draft
lifecycle_changed: 2026-10-22
tier: supporting
created: 2026-10-22T23:45:17Z
updated: 2026-10-22T23:45:17Z
---

# Vehicle Routing Problems for Drone Delivery (Dorling et al., 2017)

> [!tldr] This paper formulates drone-only multi-trip delivery VRPs that explicitly model payload/battery effects on energy, then solves minimum-cost and minimum-time variants with MILP and simulated annealing.

## Problem & Contribution

The paper argues classical VRPs miss key drone-delivery realities:
- multiple depot returns and vehicle reuse,
- payload- and battery-dependent energy draw,
- tight coupling between route choice, battery size, and feasibility.

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

- Hover, straight flight and altitude-change power measurements on the same airframe are close: 15.6/19.9 W/kg with 311 W hover, 15.3/19.8 W/kg with 304 W straight flight, 14.7/20.3 W/kg with 297 W altitude change (Table I).

## Optimization Pattern

- MILP captures routing, reuse, timing, energy, capacity, and budget constraints.
| Measured power | Hover 15.6 W/kg with 311 W, straight flight 15.3 W/kg with 304 W, altitude change 14.7 W/kg with 297 W — power is nearly equal in hover and level flight (Table I) |
| Hardware | 3D Robotics ArduCopter Hexa-B hexacopter, six 850 RPM/V motors, 10×4.6 APC slow-fly propellers, Arduino flight controller running firmware 3.0.1 of the APM 2.5 autopilot, u-blox LEA-6 GPS with 4 mm ceramic patch antenna, 4-cell 14.8 V LiPo battery |

## Results

| Small MILP and SA comparison | SA is near-optimal for up to 8 locations; MT-DDP: MILP 5.40–9.63 min with runtimes from 0.97 s to 116.98 s, SA 5.48–9.83 min in 0.24–0.31 s; MC-DDP: MILP 0.99–1.22 k$ with runtimes from 9.47 s to 1,116.87 s, SA 1.00–1.26 k$ in 0.19–0.24 s |
| Larger SA runs | MT-DDP: 12.19–104.75 min with $\mu = 0.99$ vs 13.28–117.82 min with $\mu = 0.9$; MC-DDP: 13.52–65.57 k$ vs 13.99–75.13 k$ |
| Simulation parameters | Drone cost $F = $500$, carrying capacity $Q = 3$ kg including battery and payload, $\alpha = 0.217$ kW/kg, $\beta = 0.185$ kW, speed $v = 6$ m/s, service time $\tau = 60$ s per location, energy density $\xi = 650$ kJ/kg, energy price $\varepsilon = $0.1$ per kJ |

## Limitations

| Cooling schedule | Raising $\mu$ from 0.9 to 0.99 improves MT-DDP time and MC-DDP cost by up to 15% for about 10× runtime (18.45 → 181.41 s, 57.11 → 497.65 s); 0.99 → 0.999 gives at most 5% for another 10×, so the paper uses $\mu = 0.99$; standard deviations are largest when the number of locations is high and $\mu$ is low |
| Reuse and battery optimization | In the min-cost time-limited case, drone reuse passes the about $113,000 limit reached without reuse; optimizing battery weight per route improves cost by 13% over a fixed 0.3 kg battery, improves delivery time by about 22% over a fixed 0.25 kg, and gives a 15% cost gain at $b = 0.3$ kg vs 0.5 kg and an 80% time gain at $b = 0.25$ kg vs 0.45 kg (500 locations, 1 km²) |

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
