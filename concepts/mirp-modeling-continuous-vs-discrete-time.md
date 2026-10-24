---
title: >-
  Continuous vs Discrete Time in Maritime Inventory Routing Models
category: concepts
tags: [maritime-routing, modeling-choices, discrete-time, continuous-time, mixed-integer-programming]
relationships:
  - target: "[[references/fagerholt2023-maritime-inventory-routing-survey]]"
    type: derived_from
  - target: "[[concepts/maritime-inventory-routing-problem]]"
    type: extends
  - target: "[[concepts/annual-lng-delivery-program]]"
    type: related_to
  - target: "[[references/boland2017-continuous-time-service-network-design]]"
    type: related_to
sources:
  - _papers/fagerholt2023maritime/fagerholt2023maritime-extracted.md
  - _papers/fagerholt2023maritime/fagerholt2023maritime.md
summary: >-
  The MIRP modeling fork: a discrete time-expanded port-time node grid versus a continuous-time
  port-visit node grid, with the trade-offs that decide which one a study should use.
provenance:
  extracted: 0.85
  inferred: 0.12
  ambiguous: 0.03
base_confidence: 0.67
lifecycle: draft
lifecycle_changed: 2026-10-24
tier: supporting
created: 2026-10-24T00:32:00Z
updated: 2026-10-24T00:32:00Z
---

# Continuous vs Discrete Time in Maritime Inventory Routing Models

Every MIRP model must place inventory decisions on a timeline, and the timeline choice is the single biggest structural decision in the literature — it drives instance size, which constraints are expressible, and which solution methods are usable.

## Core Structure

- **Discrete time** — a node is a **(port, time) pair** in a grid of time periods; variables are flow on arcs between port-time nodes. Time periods are decision epochs, so inventory bounds must hold at every period.
- **Continuous time** — a node is a **(port, visit number) pair**; ship positions and port-visit times are continuous variables, so the time axis itself is the decision.
- **Shared core constraint** (inventory balance, discrete form):

$$
\sum_{(h,v)\in E(i,j,t)} x_{ijv,t,h} = q_{ijt},\qquad inv_{j,t+1} = inv_{j,t} - q_{ijt} + \sum_{(h,v)\in E(j,k,t)} x_{jkv,t,h}
$$

- **Census** (53 papers, 2013–2023): 30 use discrete time, 27 continuous, 4 both. Discrete-time instances dominate public benchmarks; continuous-time instances are not public.

| Dimension | Discrete time | Continuous time |
|---|---|---|
| Time-dependent parameters (tide, demand, production) | easy | hard |
| Speed / sailing-time options | finite set via arcs | continuous function of speed |
| Instance size | large MILPs | compact, good for steady state |
| Time realism | approximation (period boundaries) | exact event times |
| Multi-berth ports | natural | special handling needed |
| Rolling horizon | fits well | awkward |
| Inventory bound enforced | only at period boundaries | at every port visit |

**Guidance**: continuous time when the study is steady-state, ports have one berth, and the model is bespoke; discrete time otherwise.

Variants beyond the fork: **location-event** and **vessel-event** continuous models; an event-point model for ports with multiple berths; hybrid discrete/continuous models; nonlinear speed, fuel-consumption, and tide models; path-flow models with set-partitioning structure; fixed-charge network-flow models with lot-sizing valid inequalities; constraint programming with interval/sequence variables and cumul functions.

![[_papers/fagerholt2023maritime/images/page_8_image_2.jpg]]
*Fig. 1 (paper): time-expanded network — one node per (port, period), sailing arcs and inventory arcs, source and sink nodes.*

![[_papers/fagerholt2023maritime/images/page_11_image_2.jpg]]
*Fig. 2 (paper): continuous-time network — one node per (port, visit-number), sailing time is a variable on the arc.*

## Why It Matters

- Instance size is the binding constraint: discrete-time models routinely outgrow solvers, which is why 19/53 MIRP papers fall back on default MIP solvers, 14 use matheuristics, 9 use metaheuristics, and rolling horizon appears in 5.
- The discrete-time approximation is not harmless: inventory bounds are only checked at period boundaries, so a "feasible" plan can violate bounds between periods. ^[inferred]
- Fixed-charge network-flow reformulations tighten LP relaxations via lot-sizing cuts, yet the literature has no proof that they yield better primal solutions on large instances — the model that is "stronger" on paper is not necessarily better in practice.
- Constraint programming was ~4–10× faster than MILP on average in one comparison, showing that the modeling paradigm, not just the solver, drives performance.
- Horizon length is a trap: optimal MIRP decisions depend on the horizon $T$, so a planning system cannot claim "steady state" without stating the horizon. ^[inferred]

## Related

- [[references/fagerholt2023-maritime-inventory-routing-survey]]
- [[concepts/maritime-inventory-routing-problem]]
- [[concepts/annual-lng-delivery-program]]
- [[references/christiansen2013-ship-routing-scheduling-new-millennium]]
- [[references/boland2017-continuous-time-service-network-design]]
- [[concepts/branch-and-price-column-generation]]

## Open Questions

- Are continuous-time models genuinely better for steady-state studies? No published benchmark supports the claim — continuous-time instances are not public.
- Will fixed-charge models be shown to beat discrete-time models on the primal side, not just the LP relaxation?
- Can a standardized, open-source simulation framework settle model comparisons for stochastic dynamic MIRP, as the survey calls for?

## Sources

- [[_papers/fagerholt2023maritime/fagerholt2023maritime-extracted.md]]
- [[_papers/fagerholt2023maritime/fagerholt2023maritime.md]]
- [[_papers/fagerholt2023maritime/images/page_8_image_2.jpg]]
- [[_papers/fagerholt2023maritime/images/page_11_image_2.jpg]]
