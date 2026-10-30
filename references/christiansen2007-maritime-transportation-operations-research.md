---
title: Maritime Transportation OR Models Across Planning Levels (Christiansen et al., 2007)
category: references
tags: [maritime, ship-routing-scheduling]
relationships:
  - target: "[[references/christiansen2013-ship-routing-scheduling-new-millennium]]"
    type: related_to
  - target: "[[concepts/maritime-inventory-routing-problem]]"
    type: related_to
  - target: "[[concepts/liner-shipping-network-design]]"
    type: related_to
sources:
  - _papers/christiansen2007chapter/christiansen2007chapter-extracted.md
  - _papers/christiansen2007chapter/christiansen2007chapter.md
summary: >-
  Surveys maritime transportation OR models across strategic, tactical, and operational horizons, with canonical formulations for fleet sizing, liner network design, and ship routing/scheduling.
provenance:
  extracted: 0.88
  inferred: 0.1
  ambiguous: 0.02
base_confidence: 0.67
lifecycle: draft
lifecycle_changed: 2026-10-22
tier: supporting
created: 2026-10-22T23:17:15Z
updated: 2026-10-30T17:41:00Z
---

# Maritime Transportation OR Models Across Planning Levels (Christiansen et al., 2007)

> [!tldr] A foundational OR chapter that organizes maritime planning by horizon (strategic/tactical/operational) and operation mode (liner/tramp/industrial), then maps each to optimization models.

## Problem & Contribution

The chapter consolidates maritime decision problems into a structured planning framework and emphasizes why maritime operations need specialized OR models (high capital intensity, uncertain operations, and cross-jurisdiction logistics).

It contributes a unifying view across:
- planning levels: strategic, tactical, operational,
- operation modes: liner, tramp, industrial,
- model families: fleet size/mix, network design, routing/scheduling, and contract evaluation.

## Method / Modeling Frame

The chapter repeatedly uses integer-programming formulations for fleet and routing decisions. A representative strategic fleet size/mix model is expressed as:

$$
\min \sum_{v\in\mathcal{V}}\sum_{r\in\mathcal{R}_v} C^{V}_{vr}u_{vr} + \sum_{v\in\mathcal{V}} C^{F}_{v}s_v
$$

subject to route-service coverage and planning-horizon feasibility:

$$
\sum_{v\in\mathcal{V}}\sum_{r\in\mathcal{R}_v} A_{ir}u_{vr} \ge D_i \quad \forall i
$$

$$
\sum_{r\in\mathcal{R}_v} T^{V}_{vr}u_{vr} \le T \quad \forall v
$$

The chapter also details arc-flow formulations for industrial/tramp scheduling and route-design models for liner services.

## Selected Evidence

| Signal | Value / takeaway |
|---|---|
| Estimated share of international trade by sea | ~65% to 85% |
| Growth in container fleet capacity (1980–2003, cited in chapter) | ~727% |
| Planning insight | Tactical routing/scheduling is strongly coupled with strategic fleet and network choices |

## Limitations

- As a handbook chapter, breadth is prioritized over controlled head-to-head computational benchmarking across all model families.
- Several formulations are presented as canonical templates and require case-specific calibration for modern fuel/emissions constraints. ^[inferred]

## Related

- [[references/christiansen2013-ship-routing-scheduling-new-millennium]]
- [[references/christiansen2020-liner-shipping-network-design]]
- [[concepts/maritime-inventory-routing-problem]]
- [[concepts/liner-shipping-network-design]]
- [[concepts/maritime-routing-under-uncertainty]]

## Bibliographic Record

- Citation key: `christiansen2007chapter`
- DOI: `10.1016/S0927-0507(06)14004-9`
- Canonical URL: <https://www.sciencedirect.com/science/article/pii/S0927050706140049>
- Publication: *Handbooks in Operations Research and Management Science* (2007)
- Authors: Marielle Christiansen; Kjetil Fagerholt; Bjørn Nygreen; David Ronen; Cynthia Barnhart; Gilbert Laporte
- Companion metadata note: [[_papers/christiansen2007chapter/christiansen2007chapter.md]]

## Sources

- [[_papers/christiansen2007chapter/christiansen2007chapter-extracted.md]]
- [[_papers/christiansen2007chapter/christiansen2007chapter.md]]
