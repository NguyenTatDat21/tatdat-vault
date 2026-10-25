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
sources:
  - _papers/christiansen2008maritime/christiansen2008maritime-extracted.md
  - _papers/christiansen2013ship/christiansen2013ship-extracted.md
  - _papers/fagerholt2023maritime/fagerholt2023maritime-extracted.md
  - _papers/fagerholt2023maritime/fagerholt2023maritime.md
  - _papers/halvorsen-weare2013routing/halvorsen-weare2013routing-extracted.md
  - _papers/halvorsen-weare2013routing/halvorsen-weare2013routing.md
summary: >-
  Defines integrated maritime planning where ship routing/scheduling and port inventory dynamics are optimized jointly, plus common extension patterns used in industrial shipping models.
provenance:
  extracted: 0.87
  inferred: 0.11
  ambiguous: 0.02
base_confidence: 1.0
lifecycle: draft
lifecycle_changed: 2026-10-24
tier: supporting
created: 2026-10-22T23:17:15Z
updated: 2026-10-25T10:50:35Z
---

# Maritime Inventory Routing Problem

The **Maritime Inventory Routing Problem (MIRP / ISRP)** integrates vessel routing/scheduling with inventory feasibility at production and consumption ports. Unlike classical VRP, route quality is inseparable from stock trajectories over time.

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

## Sources

- [[_papers/christiansen2008maritime/christiansen2008maritime-extracted.md]]
- [[_papers/christiansen2013ship/christiansen2013ship-extracted.md]]
- [[_papers/fagerholt2023maritime/fagerholt2023maritime-extracted.md]]
- [[_papers/fagerholt2023maritime/fagerholt2023maritime.md]]
- [[_papers/halvorsen-weare2013routing/halvorsen-weare2013routing-extracted.md]]
- [[_papers/halvorsen-weare2013routing/halvorsen-weare2013routing.md]]
- [[_papers/fagerholt2023maritime/images/page_8_image_2.jpg]]
- [[_papers/fagerholt2023maritime/images/page_11_image_2.jpg]]
