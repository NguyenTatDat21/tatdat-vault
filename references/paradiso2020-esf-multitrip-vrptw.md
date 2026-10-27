---
title: >-
  Exact Solution Framework for Multitrip VRP with Time Windows (Paradiso et al., 2020)
category: references
tags: [paper, exact-methods, vehicle-routing, time-windows]
relationships:
  - target: "[[concepts/exact-multitrip-vrptw-framework]]"
    type: uses
  - target: "[[references/poikonen2020-k-mvdrp]]"
    type: related_to
  - target: "[[references/tamke2023-vrpd-dss]]"
    type: related_to
sources:
  - _papers/paradiso2020exact/paradiso2020exact-extracted.md
  - _papers/paradiso2020exact/paradiso2020exact.md
  - _papers/paradiso2020exact/images/page_1_image_2.jpg
  - _papers/paradiso2020exact/images/page_9_image_13.jpg
summary: >-
  Proposes a structure-based exact framework (ESF) for multitrip VRP with time windows, combining strong lower bounds and branch-and-cut to solve larger instances than prior exact methods.
provenance:
  extracted: 0.88
  inferred: 0.08
  ambiguous: 0.04
base_confidence: 0.67
lifecycle: draft
lifecycle_changed: 2026-10-22
tier: core
created: 2026-10-22T09:12:13Z
updated: 2026-10-27T06:00:00Z
---

# Exact Solution Framework for Multitrip VRP with Time Windows (Paradiso et al., 2020)

> [!tldr] The paper introduces a structure-based exact solution framework (ESF) for CMTVRPTW variants and reports major gains in solved instances and runtime versus prior tailored exact methods.

## Problem & Motivation

The work studies capacitated multitrip VRP with time windows (CMTVRPTW) and four variants (loading times, limited trip duration, release dates, and drone-routing adaptation).

Prior exact methods could struggle even at ~25 customers; the paper targets stronger scalability and a unifying exact framework. ^[inferred]

## Method / Architecture

The ESF is built around a **structure-based formulation** (instead of trip- or journey-indexed formulations only), plus two lower bounds:

![[_papers/paradiso2020exact/images/page_1_image_2.jpg]]
*(Title-page figure; no caption in the PDF text layer.)*
- CVRPTW-based lower bound (`P1`),
- relaxed structure-feasibility lower bound (`P2`) with subset-row inequalities.

A reduced structure set is then passed to branch-and-cut (with embedded branch-and-price style separation logic where needed).

![[_papers/paradiso2020exact/images/page_9_image_13.jpg]]
*Figure 1 (paper): "Example of a Support Graph 𝐺̃ = (𝑉̃, 𝐴̃) with Six Structures" — the support graph whose arcs connect structures s₁, s₂ with e_{s₁} + d_{s₁} ≤ ℓ_{s₂}, used to formulate the separation problem of the structure feasibility constraints.*

Core point: the framework is reusable across problem variants by specializing one step, rather than redesigning a full exact method per variant.

## Results

Reported outcomes include:
- CMTVRPTW: 60/81 solved (all 25-customer, most 40-customer, partial 50-customer), average ~11 minutes on solved instances.
- CMTVRPTW-LD: 162/162 solved, average ~16.8 seconds.
- DRP benchmarks: all Type A (85/85) and Type B (54/54) solved, with low average times.
- Literature comparisons: ESF solves more instances and is often faster than Hern14/Hern16/Cheng18 baselines.

The paper identifies structure enumeration as the practical bottleneck for the hardest classes (especially larger release-date variants).

## Limitations

- Exact scalability still degrades on hardest 50-customer and release-date-heavy groups. ^[inferred]
- Some section labels/tables in extracted text show OCR/format artifacts, so a few tabular details should be cross-checked against the PDF appendix. ^[ambiguous]

## Related

- [[concepts/exact-multitrip-vrptw-framework]]
- [[references/poikonen2020-k-mvdrp]]
- [[references/tamke2023-vrpd-dss]]
- [[references/gendreau2019-handbook-metaheuristics]]
- [[_papers/boland2017solving/boland2017solving-extracted]]
- [[_papers/ha2020new/ha2020new-extracted]]

## Bibliographic Record

- Citation key: `paradiso2020exact`
- DOI: `10.1287/opre.2019.1874`
- Canonical URL: <https://pubsonline.informs.org/doi/abs/10.1287/opre.2019.1874>
- Publication: *Operations Research* (2020)
- Authors: Rosario Paradiso; Roberto Roberti; Demetrio Laganá; Wout Dullaert
- Companion metadata note: [[_papers/paradiso2020exact/paradiso2020exact.md]]

## Sources

- [[_papers/paradiso2020exact/paradiso2020exact-extracted.md]]
- [[_papers/paradiso2020exact/paradiso2020exact.md]]
- [[_papers/paradiso2020exact/images/page_1_image_2.jpg]]
- [[_papers/paradiso2020exact/images/page_9_image_13.jpg]]
