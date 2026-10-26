---
title: >-
  Maritime Inventory Routing: Recent Trends and Future Directions (Fagerholt et al., 2023)
category: references
tags: [paper, maritime, inventory-routing, survey, mixed-integer-programming, modeling-choices]
relationships:
  - target: "[[concepts/mirp-modeling-continuous-vs-discrete-time]]"
    type: uses
  - target: "[[concepts/maritime-inventory-routing-problem]]"
    type: derived_from
  - target: "[[references/ksciuk2023-maritime-uncertainty-review]]"
    type: related_to
  - target: "[[references/christiansen2013-ship-routing-scheduling-new-millennium]]"
    type: related_to
  - target: "[[concepts/annual-lng-delivery-program]]"
    type: related_to
  - target: "[[concepts/variable-neighborhood-search]]"
    type: related_to
  - target: "[[concepts/large-neighborhood-search]]"
    type: related_to
  - target: "[[references/papageorgiou2014-mirplib-mirp-instance-library]]"
    type: related_to
  - target: "[[references/rakke2011rolling-rolling-horizon-lng-adp]]"
    type: related_to
  - target: "[[concepts/swarm-intelligence-pso-aco]]"
    type: related_to
sources:
  - _papers/fagerholt2023maritime/fagerholt2023maritime-extracted.md
  - _papers/fagerholt2023maritime/fagerholt2023maritime.md
summary: "Decade survey of 53 MIRP papers: what makes maritime IRP unlike land IRP, discrete vs continuous time trade-offs, solution-method census, benchmarks, directions."
provenance:
  extracted: 0.86
  inferred: 0.11
  ambiguous: 0.03
base_confidence: 0.67
lifecycle: draft
lifecycle_changed: 2026-10-24
tier: supporting
created: 2026-10-24T00:32:00Z
updated: 2026-10-26T10:43:50Z
---

# Maritime Inventory Routing: Recent Trends and Future Directions (Fagerholt et al., 2023)

Rakke et al.'s rolling horizon heuristic for the LNG ADP [[references/rakke2011rolling-rolling-horizon-lng-adp]] is one of the rolling-horizon applications this survey traces.

> [!tldr] A survey of 53 peer-reviewed MIRP papers published 2013–2023 that (1) contrasts maritime IRP with land IRP, (2) compares discrete-time and continuous-time MILP modeling, (3) tabulates variants and solution methods, and (4) names concrete future directions — new fuels, integrated supply chains, machine-learning-enhanced optimization, carbon regulation, and standardized instances.

## Scope & Framing

MIRP is defined (Christiansen et al. 2013) as planning in which one actor manages inventory at one or both ends of maritime legs **and** plans vessel routing/scheduling. The paper updates two earlier surveys: Papageorgiou et al. (2014, through mid-2013) and Andersson et al. (2010).

What distinguishes MIRP from land VRP/IRP:

- **Multiple production sites**, not one depot;
- **Open-ended routes** — no return-to-depot, no closed tours;
- **Long voyages and long horizons** (days, not hours);
- **Heterogeneous fleets** — even identical vessels differ by start location and start time;
- **Evaporative cargo** (LNG, ammonia) that can be consumed as fuel, so the cargo is partly the fuel;
- **Objective is usually transport cost only** — for vertically integrated producers, inventory holding cost is sunk.

Most MIRP work is application-driven, and papers rarely describe the underlying problem structure, so complexity comparisons across papers are hard. ^[inferred]

## Modeling: Discrete vs Continuous Time

The core inventory balance is:

$$
S_{i,t} = S_{i,t-1} + \text{arrival/production}_{i,t} - \text{consumption/shipment}_{i,t}, \qquad S^{\min}_i \le S_{i,t} \le S^{\max}_i
$$

The modeling choice is what a node means:

| | Discrete time | Continuous time |
|---|---|---|
| Node | (port, time period) pair | (port, visit number) pair |
| Pros | time-dependent parameters easy; modification easy; finite speed options via arcs; reference grid simplifies constraints; fits rolling horizon | no time approximation; smaller instances for steady-state |
| Cons | time approximation; very large MILPs; inventory bounds enforced only at period boundaries | hard with time-dependent parameters; multiple berths need special handling; awkward in rolling horizon |

Counts in the survey: 30 of 53 papers use discrete time, 27 continuous, 4 use both. Guidance: choose continuous time when the problem is steady-state, has one berth per port, and warrants a bespoke model; choose discrete time otherwise.

![[_papers/fagerholt2023maritime/images/page_8_image_2.jpg]]
*Fig. 1 (paper): "Time-expanded (or time-space) network for an individual vessel first available at port i in time period 1 and at port j in time period 2." Travel arcs encode voyage duration (three periods in the example), and the network does not depict port operations — these are handled via constraints.*

![[_papers/fagerholt2023maritime/images/page_11_image_2.jpg]]
*Fig. 2 (paper): "An instance and solution for a continuous-time model for MIRP." Nodes are (port, visit-number) pairs with a port-visit cap set by a parameter, one berth per port, production/consumption rates constant over the horizon.*

## Alternative Formulations Seen

- **Location-event and vessel-event** continuous-time models (Agra et al. 2022).
- **Event-point model** for multiple berths per port (Jiang & Grossmann 2015).
- **Hybrid discrete/continuous** models (Agra et al. 2013b).
- **Nonlinear speed / fuel / tide models** (De et al. 2016, 2017; Radan et al. 2022).
- **Path-flow / set-partitioning** (Desrochers et al. 1992 pattern): Bredström et al. 2015 with multiproduct and route-dependent cargo capacities; Stålhane et al. 2014 with branch-and-price plus path generation; Andersson et al. 2016 "duties" (one production visit plus up to two consumption visits); Rakke et al. 2015 delivery patterns via branch-price-and-cut.
- **Fixed-charge network flow** view (Agra et al. 2013a): yields lot-sizing valid inequalities and tighter LP relaxations, with three conceptual sublevels per (port, time) node — arrival, operations/departure, inventory. It requires assuming a visit implies an operation and that waiting occurs only before operations, and has not been shown to give better primal solutions on large instances.
- **Constraint programming** (Goel et al. 2015, the only CP use surveyed): interval and sequence variables with cumul functions — 4–10× faster on average than MILP.

Multi-product variants (survey Table 3) track demand style (ratable / demand / tracking), split loads, split deliveries, and product separation (dedicated compartments vs none vs stowage rules).

## Solution-Method Census (53 papers)

| Family | Count | Notes |
|---|---|---|
| Default MIP solver | 19 | dominant choice |
| Branch-and-cut | 2 | Andersson et al. 2016, 2017 |
| Branch-and-price / branch-price-and-cut | 3 | Stålhane 2014, Xin 2021, Rakke 2015 |
| Benders-like decomposition | 4 | |
| Constraint programming | 1 | Goel et al. 2015 |
| Rolling horizon | 5 | |
| Other matheuristics | 14 | largest heuristic family |
| Non-model heuristics / metaheuristics | 9 | [[concepts/variable-neighborhood-search|VNS]], GRASP, [[concepts/swarm-intelligence-pso-aco|PSO]], GA |

Benchmarks: **MIRPLIB** ([[references/papageorgiou2014-mirplib-mirp-instance-library]] mirplib.scl.gatech.edu, published 2012) — 5 MIRPLIB instances appear in MIPLIB's Collection Set, and a subset was used in the NeurIPS 2021 ML for Combinatorial Optimization competition (Gasse et al. 2022). MIRPLIB is mostly discrete-time; continuous-time instances are not public. Hemmati et al. 2016 multiproduct short-sea instances and Rodrigues et al. 2019 uncertainty variants (7 base instances × 3 initial inventories) are at home.himolde.no/hvattum/benchmarks/.

## Future Directions Named

1. **New cargoes**: hydrogen, ammonia, liquefied CO$_2$ — including dual-use backhaul (cargo in, fuel out).
2. **Holistic supply chains** mixing maritime and land IRP in one model.
3. **Machine learning**: offline learning to strengthen models, RL / approximate dynamic programming online (Papageorgiou et al. 2015 was the first RL use in MIRP).
4. **Compute**: parallel CPU/GPU, quantum computing (Harwood et al. 2021 assessed IRP formulations from a quantum-computing perspective after recasting them as VRPTW); Munguía et al. 2019's parallel alternating criteria search, a [[concepts/large-neighborhood-search|LNS]]-based primal heuristic, ran on a 96-core cluster.
5. **Speed optimization and emissions** (Eide et al. 2020; Norstad et al. 2011); IMO carbon-intensity regulation targets −40% by 2030 and −70% by 2050 vs 2008.
6. **Standardized instances plus an open-source simulation framework** for open-ended, dynamic, stochastic MIRP — uncertainty modeling is described as being in its infancy.
7. A **finer MIRP taxonomy**: load-then-unload route structure, route length / number of port calls, product separation, speed, uncertainty, time-varying parameters, hard vs soft inventory constraints, fleet homogeneity and chartering, short-sea vs deep-sea.

## Limitations

- Single product is the dominant assumption; multi-product coverage is thin.
- No public continuous-time benchmark set, so continuous-vs-discrete comparisons are not reproducible. ^[inferred]
- Because papers describe applications more than problem structure, there is no clean complexity map across the literature. ^[inferred]
- Coverage ends at papers published through 2023 and inherits the search limits of that window.
- End-of-horizon assumptions are flagged as a trap: optimal voyages at the end of the horizon depend on horizon length T, so modelers must state them explicitly.

## Related

- [[concepts/mirp-modeling-continuous-vs-discrete-time]]
- [[concepts/maritime-inventory-routing-problem]]
- [[references/ksciuk2023-maritime-uncertainty-review]]
- [[references/dossantos2024-multiobjective-maritime-cargo-routing]]
- [[references/christiansen2013-ship-routing-scheduling-new-millennium]]
- [[concepts/annual-lng-delivery-program]]

- [[references/papageorgiou2014-mirplib-mirp-instance-library]]
## Bibliographic Record

- Citation key: fagerholt2023maritime
- DOI: 10.1111/itor.13313
- Canonical URL: <https://onlinelibrary.wiley.com/doi/abs/10.1111/itor.13313>
- Publication: *International Transactions in Operational Research* (2023)
- Authors: Kjetil Fagerholt; Lars Magnus Hvattum; Dimitri J. Papageorgiou; Sebastián Urrutia
- Companion metadata note: [[_papers/fagerholt2023maritime/fagerholt2023maritime.md]]

## Sources

- [[_papers/fagerholt2023maritime/fagerholt2023maritime-extracted.md]]
- [[_papers/fagerholt2023maritime/fagerholt2023maritime.md]]
- [[_papers/fagerholt2023maritime/images/page_8_image_2.jpg]]
- [[_papers/fagerholt2023maritime/images/page_11_image_2.jpg]]
