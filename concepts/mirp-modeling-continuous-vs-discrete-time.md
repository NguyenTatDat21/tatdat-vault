---
title: >-
  Continuous vs Discrete Time in Maritime Inventory Routing Models
category: concepts
tags: [maritime, mixed-integer-programming]
relationships:
  - target: "[[references/fagerholt2023-maritime-inventory-routing-survey]]"
    type: derived_from
  - target: "[[concepts/maritime-inventory-routing-problem]]"
    type: extends
  - target: "[[concepts/annual-lng-delivery-program]]"
    type: related_to
  - target: "[[references/boland2017-continuous-time-service-network-design]]"
    type: related_to
  - target: "[[concepts/time-space-network-ship-flow-model]]"
    type: extends
  - target: "[[references/goel2012-large-neighborhood-search-lng-inventory-routing]]"
    type: related_to
  - target: "[[references/goel2015-constraint-programming-lng-ship-scheduling]]"
    type: related_to
  - target: "[[references/papageorgiou2014-mirplib-mirp-instance-library]]"
    type: related_to
  - target: "[[concepts/cumulative-volume-lower-bound-cp-search]]"
    type: related_to
  - target: "[[concepts/disjunctive-scheduling-constraint-programming-model]]"
    type: related_to
sources:
  - _papers/fagerholt2023maritime/fagerholt2023maritime-extracted.md
  - _papers/fagerholt2023maritime/fagerholt2023maritime.md
  - _papers/goel2012large/goel2012large-extracted.md
  - _papers/goel2012large/goel2012large.md
  - _papers/goel2015constraint/goel2015constraint-extracted.md
  - _papers/goel2015constraint/goel2015constraint.md
  - _papers/fagerholt2023maritime/images/page_8_image_2.jpg
  - _papers/fagerholt2023maritime/images/page_11_image_2.jpg
summary: >-
  The MIRP modeling fork: a discrete time-expanded port-time node grid versus a continuous-time
  port-visit node grid, with the trade-offs that decide which one a study should use.
provenance:
  extracted: 0.85
  inferred: 0.12
  ambiguous: 0.03
base_confidence: 0.87
lifecycle: draft
lifecycle_changed: 2026-10-24
tier: core
created: 2026-10-24T00:32:00Z
updated: 2026-10-30T17:41:00Z
---

# Continuous vs Discrete Time in Maritime Inventory Routing Models

Every MIRP model must place inventory decisions on a timeline, and the timeline choice is the single biggest structural decision in the literature — it drives instance size, which constraints are expressible, and which solution methods are usable.

## Core Structure

- **Discrete time** — a node is a **(port, time) pair** in a grid of time periods; variables are flow on arcs between port-time nodes. Time periods are decision epochs, so inventory bounds must hold at every period.
- **Continuous time** — a node is a **(port, visit number) pair**; ship positions and port-visit times are continuous variables, so the time axis itself is the decision.
- **Shared core constraint** (inventory balance, discrete form):

$$
$$ s_{it} = s_{i,t-1} + J_i D_{it} - \sum_{v \in \mathcal{V}} J_i q_{itv} \quad (i,t) \in \mathcal{N}, $$
$$

- **Census** (53 papers, 2013–2023): 30 use discrete time, 27 continuous, 4 both. Discrete-time instances dominate public benchmarks; continuous-time instances are not public. The dominant public discrete-time benchmark is MIRPLib [[references/papageorgiou2014-mirplib-mirp-instance-library]].

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

Variants beyond the fork: **location-event** and **vessel-event** continuous models; an event-point model for ports with multiple berths; hybrid discrete/continuous models; nonlinear speed, fuel-consumption, and tide models; path-flow models with set-partitioning structure; fixed-charge network-flow models with lot-sizing valid inequalities; constraint programming with interval/sequence variables and cumul functions — the Goel et al. LNG port-visit model is the clearest CP instantiation (see [[concepts/cumulative-volume-lower-bound-cp-search]]).

![[_papers/fagerholt2023maritime/images/page_8_image_2.jpg]]
*Fig. 1 (paper): "Time-expanded (or time-space) network for an individual vessel first available at port i in time period 1 and at port j in time period 2." The vessel waits two periods at port 1, travels to port j (three periods), waits, then exits; port operations are handled via constraints, not by the network.*

![[_papers/fagerholt2023maritime/images/page_11_image_2.jpg]]
*Fig. 2 (paper): "An instance and solution for a continuous-time model for MIRP." Nodes are (port, visit-number) pairs; production and consumption rates are constants over the horizon, one berth per port, visit cap set by a parameter.*

## Why It Matters

- Instance size is the binding constraint: discrete-time models routinely outgrow solvers, which is why 19/53 MIRP papers fall back on default MIP solvers, 14 use matheuristics, 9 use metaheuristics, and rolling horizon appears in 5.
- The discrete-time approximation is not harmless: inventory bounds are only checked at period boundaries, so a "feasible" plan can violate bounds between periods. ^[inferred]
- Fixed-charge network-flow reformulations tighten LP relaxations via lot-sizing cuts, yet the literature has no proof that they yield better primal solutions on large instances — the model that is "stronger" on paper is not necessarily better in practice.
- Constraint programming was ~4–10× faster than MILP on average in one comparison, showing that the modeling paradigm, not just the solver, drives performance.
- The Goel et al. LNG case quantifies the fork on instance P14: the discrete time-space MIP has 232,856 binary variables and 79,425 constraints, while the continuous CP port-visit model (CP2) has 15,375 variables and 22,089 constraints (203.1 MB vs 1.9 GB for the discrete-visit CP1); CP2 reaches its first feasible solution (63,352) in 4 s vs MIP-Heur's 70,474 in 18 s, and solves 4.55x faster on average than the MIP heuristic (up to 10.5x with the iterative search) [[references/goel2015-constraint-programming-lng-ship-scheduling]].
- Horizon length is a trap: optimal MIRP decisions depend on the horizon $T$, so a planning system cannot claim "steady state" without stating the horizon. ^[inferred]

## Related

- [[references/fagerholt2023-maritime-inventory-routing-survey]]
- [[concepts/maritime-inventory-routing-problem]]
- [[concepts/annual-lng-delivery-program]]
- [[references/christiansen2013-ship-routing-scheduling-new-millennium]]
- [[references/boland2017-continuous-time-service-network-design]]
- [[concepts/time-space-network-ship-flow-model]]
- [[concepts/cumulative-volume-lower-bound-cp-search]]
- [[references/goel2012-large-neighborhood-search-lng-inventory-routing]]
- [[references/goel2015-constraint-programming-lng-ship-scheduling]]
- [[concepts/branch-and-price-column-generation]]
- [[references/papageorgiou2014-mirplib-mirp-instance-library]]

## Open Questions

- Are continuous-time models genuinely better for steady-state studies? No published benchmark supports the claim — continuous-time instances are not public.
- Will fixed-charge models be shown to beat discrete-time models on the primal side, not just the LP relaxation?
- Can a standardized, open-source simulation framework settle model comparisons for stochastic dynamic MIRP, as the survey calls for?

## Sources

- [[_papers/fagerholt2023maritime/fagerholt2023maritime-extracted.md]]
- [[_papers/fagerholt2023maritime/fagerholt2023maritime.md]]
- [[_papers/fagerholt2023maritime/images/page_8_image_2.jpg]]
- [[_papers/fagerholt2023maritime/images/page_11_image_2.jpg]]
- [[_papers/goel2012large/goel2012large-extracted.md]]
- [[_papers/goel2012large/goel2012large.md]]
- [[_papers/goel2015constraint/goel2015constraint-extracted.md]]
- [[_papers/goel2015constraint/goel2015constraint.md]]
