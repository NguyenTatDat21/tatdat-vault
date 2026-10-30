---
title: >-
  Collective Drone Delivery (Coupled Drones as One Vehicle)
category: concepts
aliases: [c-drone, collective UAV, coupled drones, k-unit c-drone]
tags: [drone-delivery, collective-drone, payload-capacity, fleet-size, battery-tradeoff, coverage-area, synchronization, last-mile, faa-regulation]
relationships:
  - target: "[[references/nguyen2023-pdstsp-collective-drones]]"
    type: derived_from
  - target: "[[concepts/peukert-law-battery-discharge]]"
    type: related_to
  - target: "[[concepts/drone-swarm-synchronization]]"
    type: related_to
  - target: "[[concepts/payload-induced-drone-battery-consumption-rate]]"
    type: related_to
  - target: "[[references/montemanni2024-parallel-collective-drones]]"
    type: related_to
  - target: "[[concepts/parallel-drone-scheduling-traveling-salesman-problem]]"
    type: related_to
  - target: "[[concepts/multirotor-power-model-components]]"
    type: related_to
  - target: "[[concepts/hybrid-truck-drone-delivery]]"
    type: related_to
  - target: "[[concepts/pdsvrp-c]]"
    type: related_to
  - target: "[[references/montemanni2023-cp-pdsvrp]]"
    type: related_to
  - target: "[[references/montemanni2024-pdsvrp-collective-drones]]"
    type: related_to
  - target: "[[references/sacramento2019-vrp-d-truck-drone-alns-cost]]"
    type: related_to
  - target: "[[references/wang2019routing]]"
    type: related_to
sources:
  - _papers/nguyen2023parallel/nguyen2023parallel-extracted.md
  - _papers/nguyen2023parallel/nguyen2023parallel.md
summary: >-
  Coupling k depot drones into one c-drone pools payload and range; eligibility splits requests at 0.81/6.91/10.82 kg, gains average 23.47% and need 12+ drones.
provenance:
  extracted: 0.83
  inferred: 0.13
  ambiguous: 0.04
base_confidence: 0.67
lifecycle: draft
lifecycle_changed: 2026-10-26T05:12:09Z
tier: core
created: 2026-10-26T05:12:09Z
updated: 2026-10-30T14:38:55Z
---

# Collective Drone Delivery

> [!tldr] A **collective drone** (c-drone, "collective UAV") is a body formed by coupling $k$ single drones that share power and operating instructions, so payload and range are pooled. Coupling converts a per-drone hard cap into a fleet-level design variable: it lets drones serve parcels a single drone cannot carry, at the cost of a depot synchronization constraint, extra battery weight, and more units on station.

## Mechanism

Paczan et al. (2016) patent the idea. Coupled units share power and operating instructions, which lets them carry "virtually any size, weight or quantity of items"; some units can then **reduce motor rotational speed**, relying on the collective lifting force, which lowers energy consumed during navigation. The larger coupled body produces a bigger radar/object-detection signature, making it more detectable by ground radar and air-traffic controllers — a safety benefit, not a cost.

In scheduling terms a **k-unit c-drone** covers both a single drone ($k=1$) and at least two coupled drones ($k>1$). All $k$ units must be assembled at the depot to complete the coupling process before launch: this is a [[concepts/drone-swarm-synchronization|synchronization constraint]] among drones, and it makes the *order* of services in a drone tour matter, which it does not in the classic [[concepts/parallel-drone-scheduling-traveling-salesman-problem|PDSTSP]]. The payload is evenly distributed, so each unit carries $\bar w = w/k$; in the PDSTSP-c model cruise speeds per $(w,k,\text{distance})$ are pre-computed to minimize flight time subject to the battery constraints, and the coupling time is added only when $k>1$.

## Eligibility: which requests can a c-drone serve?

From the CART classification of 186 184 sampled requests (1000 instances):

| Weight band | Verdict |
|---|---|
| $w < 0.28$ kg | single drone feasible even with the smallest 7.5 Ah battery |
| $0.28 \le w < 0.81$ kg | single drone feasible if $C_{nom}\ge 12$ Ah |
| $0.81 < w < 6.91$ kg | nearly every request is c-drone-eligible |
| $6.91 < w < 10.82$ kg | more than half must go by truck |
| $w > 10.82$ kg | truck-served regardless of distance |

Single-drone range on 12 Ah covers deliveries below 0.81 kg within **12.59 km** and slightly beyond. Feasibility is decided by the battery constraints — maximum discharge current $I_i\le I_{max}$ per flight phase, and the Peukert-corrected demand $C_d\ge\beta C_{nom}$ (see [[concepts/peukert-law-battery-discharge]]); if either fails, that k-unit configuration cannot carry the parcel. ^[inferred]

## Measured benefit

Over 1000 sensitivity samples, replacing the single-drone system with a c-drone system improves makespan by **23.47%** on average; the best leaf reaches **32.33%**, best individuals up to **58.78%**, and even the worst leaf yields **10.33%**. Truck mileage falls by **33.21%** on average, because heavy/distant parcels move from the truck to air.

- **Fleet size $m$ is the most decisive factor** — the root split of the regression tree is on $m$: $m\le 11.5$ → 18.45% average gain, $m>11.5$ → 27.26%; the same ordering recurs deeper in the tree (Nodes 1, 3, 13), and at the third level gain rises from 18.09% to 21.58% as $m$ increases. Recommendation: **at least 12 drones** for a drastic benefit.
- **Battery model matters less and locally.** Aggregate gains at Node 10 ($m>12$): 7.5 Ah → 26.68%, 12 Ah → **29.69%**, 20 Ah → 27.95%, 30 Ah → 25.05%. Beyond 12 Ah the gain falls and the variance grows, because extra battery weight raises the discharge drain and cancels the longer life: a 30-Ah drone weighing 4.64 kg leaves, under the 25 kg cap, at most **6.44 kg** of payload for a 4-unit c-drone and **1.8 kg** for a 5-unit c-drone. **12 Ah is the most consistent choice** on cost/effectiveness.
- **Coverage area $D$ matters at the third level** of the tree: gain rises slightly over $[5.00, 16.18)$ km and declines steadily over $[16.18, 25.00]$ km. Split points 10.5 km and 16.18 km partition Node 5 into gains of 21.48%, 24.66%, 19.63%; the right branch favours 7.14–15 km. Recommendation: a depot coverage area of **7–15 km** for c-drone operations.

## Operating limits (regulatory framing in the source)

Cruise speeds restricted to $[4.00, 28.00]$ m/s; truck 30 km/h average, Manhattan travel; coupling time 1 minute regardless of the number of units; UPS's FAA Part 135 authorisation removes limits on the number of drones and remote operators, Part 135 permits drone + cargo above 25 kg, and Part 107 safety rules cap the **combined weight at 25 kg**, so the largest modelled c-drone has **6 units**. Other constants used: drone frame weight 1.2 kg, 4 propellers, rotor blade radius 0.15 m, Peukert constant 1.1, cruise altitude 100 m, vertical takeoff and landing speed 2 m/s. Table 5 of the source lists "C-drone preparation time | s | 1", which conflicts with the 1-minute coupling time stated in the text. ^[ambiguous]

## Design implications

1. Coupling is a **capacity-expansion** lever, not a routing trick: it widens the set of vehicle-assignment options, and the resulting fleet-assignment flexibility is where the benefit comes from.
2. The benefit is **conditional on fleet size**: with fewer than ~12 drones the synchronization cost eats most of the gain, and the paper reports a floor of 10.33% at Node 2 with 5 units.
3. Battery specification is a **weight-vs-capacity tradeoff**, and the weight penalty is amplified by coupling, since $k$ units each carry their own battery under a shared 25 kg cap. ^[inferred]
4. Depot siting is a **range** parameter: beyond ~16 km coverage the gain decays.
5. Measured against the single-drone system, not against truck-only delivery, and with no operating, energy, noise, or air-traffic cost, so a real deployment comparison needs those costs added. ^[inferred]

## Related

- [[references/nguyen2023-pdstsp-collective-drones]] — the PDSTSP-c model, MILP, RnR heuristic, and all the numbers above
- [[concepts/peukert-law-battery-discharge]] — the feasibility test that determines c-drone eligibility
- [[concepts/drone-swarm-synchronization]] — depot synchronization as a shared constraint family
- [[concepts/payload-induced-drone-battery-consumption-rate]] — payload-dependent consumption, the single-drone version
- [[concepts/multirotor-power-model-components]] — the power model coupling benefits from
- [[references/montemanni2024-parallel-collective-drones]] — collective drones in the PDSVRP setting
- [[concepts/parallel-drone-scheduling-traveling-salesman-problem]] — the problem c-drones are inserted into

## Sources

- [[_papers/nguyen2023parallel/nguyen2023parallel-extracted.md]]
- [[_papers/nguyen2023parallel/nguyen2023parallel.md]]
