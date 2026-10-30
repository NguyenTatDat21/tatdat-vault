---
title: Maritime Inventory Routing Problem
category: concepts
tags: [maritime, inventory-routing, ship-routing-scheduling, logistics]
relationships:
  - target: "[[references/christiansen2008-maritime-inventory-routing-problems]]"
    type: derived_from
  - target: "[[references/christiansen2013-ship-routing-scheduling-new-millennium]]"
    type: related_to
  - target: "[[concepts/annual-lng-delivery-program]]"
    type: related_to
  - target: "[[concepts/maritime-routing-under-uncertainty]]"
    type: related_to
  - target: "[[concepts/mirp-modeling-continuous-vs-discrete-time]]"
    type: related_to
  - target: "[[references/deshpande2023-lng-adp-inventory-berth]]"
    type: related_to
  - target: "[[references/halvorsen-weare2013-lng-routing-berth-inventory]]"
    type: related_to
  - target: "[[references/gronhaug2009-supply-chain-optimization-lng]]"
    type: related_to
  - target: "[[references/gronhaug2010-branch-and-price-lng-irp]]"
    type: related_to
  - target: "[[references/papageorgiou2014-mirplib-mirp-instance-library]]"
    type: related_to
  - target: "[[references/rakke2011rolling-rolling-horizon-lng-adp]]"
    type: uses
  - target: "[[concepts/multi-objective-maritime-cargo-routing-scheduling]]"
    type: related_to
  - target: "[[concepts/time-space-network-ship-flow-model]]"
    type: related_to
  - target: "[[references/al-haidous2016-optimal-lng-deliveries]]"
    type: related_to
  - target: "[[references/christiansen2007-maritime-transportation-operations-research]]"
    type: related_to
  - target: "[[references/dossantos2024-multiobjective-maritime-cargo-routing]]"
    type: related_to
  - target: "[[references/fagerholt2023-maritime-inventory-routing-survey]]"
    type: related_to
  - target: "[[references/goel2012-large-neighborhood-search-lng-inventory-routing]]"
    type: related_to
  - target: "[[references/goel2015-constraint-programming-lng-ship-scheduling]]"
    type: related_to
  - target: "[[references/haug2023-adp-speed-optimization-ports]]"
    type: related_to
  - target: "[[references/ksciuk2023-maritime-uncertainty-review]]"
    type: related_to
  - target: "[[references/mutlu2016-lng-annual-delivery-program]]"
    type: related_to
  - target: "[[references/shaabani2023-multiproduct-mirp-matheuristic]]"
    type: related_to
  - target: "[[references/stalhane2012-construction-improvement-lng-adp]]"
    type: related_to
  - target: "[[references/zhao2025-lns-hgs-inventory-routing]]"
    type: related_to
sources:
  - _papers/christiansen2008maritime/christiansen2008maritime-extracted.md
  - _papers/christiansen2013ship/christiansen2013ship-extracted.md
  - _papers/fagerholt2023maritime/fagerholt2023maritime-extracted.md
  - _papers/fagerholt2023maritime/fagerholt2023maritime.md
  - _papers/halvorsen-weare2013routing/halvorsen-weare2013routing-extracted.md
  - _papers/halvorsen-weare2013routing/halvorsen-weare2013routing.md
  - _papers/gronhaug2009supply/gronhaug2009supply-extracted.md
  - _papers/gronhaug2009supply/gronhaug2009supply.md
  - _papers/gronhaug2010branchandprice/gronhaug2010branchandprice-extracted.md
  - _papers/gronhaug2010branchandprice/gronhaug2010branchandprice.md
summary: >-
  Defines integrated maritime planning where ship routing/scheduling and port inventory dynamics are optimized jointly, plus common extension patterns used in industrial shipping models.
provenance:
  extracted: 0.85
  inferred: 0.13
  ambiguous: 0.02
base_confidence: 1.0
lifecycle: draft
lifecycle_changed: 2026-10-24
tier: core
created: 2026-10-22T23:17:15Z
updated: 2026-10-30T14:38:55Z
---

# Maritime Inventory Routing Problem

The **Maritime Inventory Routing Problem (MIRP / ISRP)** integrates vessel routing/scheduling with inventory feasibility at production and consumption ports. Unlike classical VRP, route quality is inseparable from stock trajectories over time.

Rakke et al.'s LNG ADP model ([[references/rakke2011rolling-rolling-horizon-lng-adp]]) is a maritime inventory routing instance solved by a rolling horizon heuristic.

The first public instance library for this problem is MIRPLib [[references/papageorgiou2014-mirplib-mirp-instance-library]], which standardizes discrete-time benchmarks.
## Core Structure

Typical MIRP formulations couple:
- ship movement and visit sequencing,
- loading/unloading quantity decisions,
- inventory balance over time at ports,
- inventory lower/upper safety constraints,
- vessel capacity and timing constraints.

A generic inventory balance form is:

$$
S_{i,t}=S_{i,t-1}+\text{production/arrival}_{i,t}-\text{consumption/shipment}_{i,t}
$$

with bounds:

$$
S_{\min,i}\le S_{i,t} \le S_{\max,i}
$$

## Why It Matters

- It captures stockout/overflow risks directly rather than treating routing and inventory as separate planning layers.
- It supports industrial cases such as LNG and bulk shipping where shipment timing and port stock are tightly coupled.
- It exposes trade-offs between routing cost, service timing, and inventory risk.

## Common Extension Axes

From the reviewed maritime literature, MIRP variants frequently add:
- one-sided inventory constraints,
- variable production/consumption rates,
- multi-product and compartment constraints,
- spot charters and contract heterogeneity,
- weather/speed uncertainty and rolling-horizon replanning.
- the discrete-time vs continuous-time modeling fork, which the 2013–2023 survey splits 30/27 papers, with 4 using both ([[concepts/mirp-modeling-continuous-vs-discrete-time]]),
- fixed-charge network-flow reformulations with lot-sizing valid inequalities, and constraint-programming models that ran ~4–10× faster than MILP on average,
- evaporative cargo (LNG, ammonia) that can be used as ship fuel, adding a second use dimension to the delivery decision.
- decomposition by coupling constraints: Halvorsen-Weare & Fagerholt remove only the berth and inventory constraints to split an annual LNG program into per-subproblem routing models plus a feasibility scheduling MILP; heuristic routing reached 360-day instances the monolithic model cannot solve within 10,000 s, with heuristic routing costs matching exact routing for most instances ([[references/halvorsen-weare2013-lng-routing-berth-inventory]]);

## Open Questions

- Which decomposition patterns are most robust for very large MIRP instances with uncertainty? ^[inferred]
- How should digital-twin and real-time AIS/port data be incorporated without destabilizing optimization cycles? ^[inferred]

## LNG-IRP Extensions

- Grønhaug & Christiansen (2009) coined **LNG-IRP** for a real liquefaction–fleet–regasification planning problem, adding boil-off, discrete full-tank unloading, variable production/sales, and berth limits to the MIRP template; see [[references/gronhaug2009-supply-chain-optimization-lng]]. ^[inferred]
- Grønhaug et al. (2010) show the inventory constraints must stay in the branch-and-price master because boil-off couples route duration to delivered quantities — the Christiansen (1999) maritime decomposition does not apply; 16/27 instances closed in 10 h, 2–25× faster than a priori path enumeration; see [[references/gronhaug2010-branch-and-price-lng-irp]]. ^[inferred]

## Related

- [[references/christiansen2008-maritime-inventory-routing-problems]]
- [[references/christiansen2013-ship-routing-scheduling-new-millennium]]
- [[references/mutlu2016-lng-annual-delivery-program]]
- [[references/deshpande2023-lng-adp-inventory-berth]]
- [[concepts/annual-lng-delivery-program]]
- [[concepts/maritime-routing-under-uncertainty]]
- [[concepts/mirp-modeling-continuous-vs-discrete-time]]
- [[references/fagerholt2023-maritime-inventory-routing-survey]]
- [[references/halvorsen-weare2013-lng-routing-berth-inventory]]
- [[references/gronhaug2009-supply-chain-optimization-lng]]
- [[references/shaabani2023-multiproduct-mirp-matheuristic]] — two-phase matheuristic for the multi-product version, 60-day horizon
- [[references/zhao2025-lns-hgs-inventory-routing]] — whole-horizon DP reinsertion for the land IRP; 365 new best solutions on 1,040 benchmarks
- [[references/stalhane2012-construction-improvement-lng-adp]] — construction + local search + reduced MIP on 20 real LNG instances with berth and storage limits
- [[references/papageorgiou2014-mirplib-mirp-instance-library]]
- [[references/gronhaug2010-branch-and-price-lng-irp]]

## Sources

- [[_papers/christiansen2008maritime/christiansen2008maritime-extracted.md]]
- [[_papers/christiansen2013ship/christiansen2013ship-extracted.md]]
- [[_papers/fagerholt2023maritime/fagerholt2023maritime-extracted.md]]
- [[_papers/fagerholt2023maritime/fagerholt2023maritime.md]]
- [[_papers/halvorsen-weare2013routing/halvorsen-weare2013routing-extracted.md]]
- [[_papers/halvorsen-weare2013routing/halvorsen-weare2013routing.md]]
- [[_papers/fagerholt2023maritime/images/page_8_image_2.jpg]]
- [[_papers/fagerholt2023maritime/images/page_11_image_2.jpg]]
- [[_papers/gronhaug2009supply/gronhaug2009supply-extracted.md]]
- [[_papers/gronhaug2009supply/gronhaug2009supply.md]]
- [[_papers/gronhaug2010branchandprice/gronhaug2010branchandprice-extracted.md]]
- [[_papers/gronhaug2010branchandprice/gronhaug2010branchandprice.md]]
