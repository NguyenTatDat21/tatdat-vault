---
title: >-
  Annual LNG Delivery Program (ADP)
category: concepts
tags: [maritime, lng, inventory-routing, tactical-planning]
relationships:
  - target: "[[references/mutlu2016-lng-annual-delivery-program]]"
    type: derived_from
  - target: "[[references/al-haidous2016-optimal-lng-deliveries]]"
    type: extends
  - target: "[[references/andersson2017-creating-annual-lng-delivery-programs]]"
    type: extends
  - target: "[[concepts/maritime-routing-under-uncertainty]]"
    type: related_to
  - target: "[[concepts/maritime-inventory-routing-problem]]"
    type: extends
  - target: "[[references/christiansen2008-maritime-inventory-routing-problems]]"
    type: derived_from
  - target: "[[references/deshpande2023-lng-adp-inventory-berth]]"
    type: extends
  - target: "[[references/haug2023-adp-speed-optimization-ports]]"
    type: extends
  - target: "[[references/goel2012-large-neighborhood-search-lng-inventory-routing]]"
    type: related_to
  - target: "[[references/goel2015-constraint-programming-lng-ship-scheduling]]"
    type: related_to
  - target: "[[concepts/mirp-modeling-continuous-vs-discrete-time]]"
    type: related_to
  - target: "[[references/rakke2011rolling-rolling-horizon-lng-adp]]"
    type: implements
sources:
  - _papers/mutlu2016comprehensive/mutlu2016comprehensive-extracted.md
  - _papers/mutlu2016comprehensive/mutlu2016comprehensive.md
  - _papers/al-haidous2016optimal/al-haidous2016optimal-extracted.md
  - _papers/al-haidous2016optimal/al-haidous2016optimal.md
  - _papers/andersson2017creating/andersson2017creating-extracted.md
  - _papers/andersson2017creating/andersson2017creating.md
  - _papers/goel2012large/goel2012large-extracted.md
  - _papers/goel2012large/goel2012large.md
  - _papers/goel2015constraint/goel2015constraint-extracted.md
  - _papers/goel2015constraint/goel2015constraint.md
  - _papers/haug2023planning/haug2023planning-extracted.md
  - _papers/haug2023planning/haug2023planning.md
summary: >-
  Tactical LNG planning problem that coordinates inventory, vessel schedules, contract obligations, and optional spot-market actions over annual horizons.
provenance:
  extracted: 0.86
  inferred: 0.11
  ambiguous: 0.03
base_confidence: 1.0
lifecycle: draft
lifecycle_changed: 2026-10-24
tier: supporting
created: 2026-10-22T09:52:03Z
updated: 2026-10-26T10:43:50Z
---

# Annual LNG Delivery Program (ADP)

Annual Delivery Program (ADP) is a tactical planning problem for LNG suppliers that couples maritime routing with production, storage, and contract satisfaction decisions.

The rolling horizon heuristic of [[references/rakke2011rolling-rolling-horizon-lng-adp|Rakke et al. (2011)]] builds an ADP by solving one-month central windows with two-month forecasting windows.

## Key Ideas

- Planning horizon is long (roughly one year), with periodic shipment decisions.
- Decisions must respect vessel availability, maintenance windows, berth capacity, and customer contract terms.
- Inventory-production balance at loading terminals is tightly coupled to [[concepts/maritime-inventory-routing-problem|inventory-routing]] feasibility.
- Al-Haidous et al. formulate ADP with a compact arc-flow MIP that minimizes required fleet size while preserving operational detail.
- Andersson et al. extend the annual LNG setup with explicit spot-market economics and branch-and-cut valid inequalities that tighten the model.
- The annual program sits on the MIRP time fork: the day-grid arc-flow MIP is the discrete-time side, the CP port-visit model the continuous-time side — solving the same instances, CP2 with CPOptimizer is 4.55x faster on average than the MIP heuristic (up to 10.5x with the iterative search), and CP2 needs 15,375 variables on the largest instance vs 232,856 binaries in the MIP — see [[concepts/mirp-modeling-continuous-vs-discrete-time]]. ^[inferred]
- Goel et al. (2015) cover the same program as a **disjunctive scheduling CP model**: CPOptimizer interval variables per cargo/ship visit, `SequenceVar` + `NoOverlap` per ship route, inventory profiles as cumul functions, plus a cumulative-volume lower bound (Theorem 1) that forces loadings/discharges at regular intervals and bounds per-terminal losses by the incumbent loss vector — 15,375 variables (no binaries) vs 232,856 binaries in the MIP, 4.55x (10.5x with the iterative search) faster than the MIP heuristic, better solutions on most large instances [[references/goel2015-constraint-programming-lng-ship-scheduling]].
- Goel et al. (2012) cast the annual horizon as a **daily time-space network**: nodes are (terminal, time period), per-ship arcs for source/sink, waiting (no berth), and travel (loading/unloading immediately followed by travel), inventory balances Eq. 5 (production: $I_{l,t}=I_{l,t-1}+p_{l,t}-\sum c_{v,l}x_a-o_{l,t}$) and Eq. 6 (regas: $I_{r,t}=I_{r,t-1}-d_{r,t}+\sum c_{v,r}x_a+s_{r,t}$) with lost-production/stockout slack, berth caps $\sum x_a\le b_j$ per terminal-period, and an objective penalizing weighted lost production, regas stockouts, and unmet demand with monotonically decreasing time weights [[references/goel2012-large-neighborhood-search-lng-inventory-routing]].
- Haug et al. add vessel speed optimization and multiple loading ports to the ADP MIP, keeping optimality gaps below 1% within an hour for 180-day single-loading-port real-life instances, and propose embedding the model in a rolling-horizon heuristic for 365-day planning [[references/haug2023-adp-speed-optimization-ports]].

ADP is a load-bearing bridge between strategic network design and short-horizon operational replanning in LNG supply chains. ^[inferred]

## Related

- [[references/mutlu2016-lng-annual-delivery-program]]
- [[references/al-haidous2016-optimal-lng-deliveries]]
- [[references/andersson2017-creating-annual-lng-delivery-programs]]
- [[references/deshpande2023-lng-adp-inventory-berth]]
- [[concepts/maritime-routing-under-uncertainty]]
- [[references/christiansen2008-maritime-inventory-routing-problems]]
- [[references/ksciuk2023-maritime-uncertainty-review]]
- [[concepts/mirp-modeling-continuous-vs-discrete-time]]
- [[references/goel2012-large-neighborhood-search-lng-inventory-routing]]
- [[references/goel2015-constraint-programming-lng-ship-scheduling]]
- [[references/haug2023-adp-speed-optimization-ports]]

## Open Questions

- Which uncertainty structures (demand, weather, spot-market price) should be integrated directly into annual ADP optimization?
- How should ADP plans be re-optimized in rolling horizons without destabilizing contractual commitments? ^[inferred]

## Sources

- [[_papers/mutlu2016comprehensive/mutlu2016comprehensive-extracted.md]]
- [[_papers/mutlu2016comprehensive/mutlu2016comprehensive.md]]
- [[_papers/al-haidous2016optimal/al-haidous2016optimal-extracted.md]]
- [[_papers/al-haidous2016optimal/al-haidous2016optimal.md]]
- [[_papers/andersson2017creating/andersson2017creating-extracted.md]]
- [[_papers/andersson2017creating/andersson2017creating.md]]
- [[_papers/goel2012large/goel2012large-extracted.md]]
- [[_papers/goel2012large/goel2012large.md]]
- [[_papers/goel2015constraint/goel2015constraint-extracted.md]]
- [[_papers/goel2015constraint/goel2015constraint.md]]
- [[_papers/haug2023planning/haug2023planning-extracted.md]]
- [[_papers/haug2023planning/haug2023planning.md]]
