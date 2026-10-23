---
title: >-
  Uncertainty in Maritime Ship Routing and Scheduling: Literature Review (Ksciuk et al., 2023)
category: references
tags: [paper, maritime, uncertainty, routing]
relationships:
  - target: "[[concepts/maritime-routing-under-uncertainty]]"
    type: uses
  - target: "[[_papers/fagerholt2023maritime/fagerholt2023maritime-extracted]]"
    type: related_to
  - target: "[[_papers/christiansen2013ship/christiansen2013ship-extracted]]"
    type: related_to
  - target: "[[references/christiansen2013-ship-routing-scheduling-new-millennium]]"
    type: related_to
  - target: "[[references/christiansen2020-liner-shipping-network-design]]"
    type: related_to
  - target: "[[concepts/maritime-inventory-routing-problem]]"
    type: related_to
sources:
  - _papers/ksciuk2023uncertainty/ksciuk2023uncertainty-extracted.md
  - _papers/ksciuk2023uncertainty/ksciuk2023uncertainty.md
  - _papers/ksciuk2023uncertainty/images/page_0_image_9.jpg
  - _papers/ksciuk2023uncertainty/images/page_2_image_2.jpg
  - _papers/ksciuk2023uncertainty/images/page_2_image_4.jpg
summary: >-
  Surveys uncertainty modeling in maritime routing/scheduling across strategic, tactical, and operational decisions, highlighting a major gap between academic methods and industry adoption.
provenance:
  extracted: 0.84
  inferred: 0.13
  ambiguous: 0.03
base_confidence: 0.67
lifecycle: draft
lifecycle_changed: 2026-10-22
tier: supporting
created: 2026-10-22T09:12:13Z
updated: 2026-10-22T23:32:21Z
---

# Uncertainty in Maritime Ship Routing and Scheduling: Literature Review (Ksciuk et al., 2023)

> [!tldr] The review organizes maritime uncertainty research by planning level and shows that advanced stochastic/robust models are still weakly adopted in industry practice.

## Scope & Framing

The paper reviews uncertainty-aware optimization in maritime transportation, covering liner, tramp, and industrial shipping contexts.

It analyzes strategic, tactical, and operational decisions and emphasizes how uncertainty sources differ by planning horizon.

## Taxonomy of Uncertainty and Decisions

The review groups decisions into three planning levels:
- **Strategic:** fleet composition/renewal, long-horizon network structure;
- **Tactical:** vessel scheduling, [[concepts/maritime-inventory-routing-problem|maritime inventory routing]], deployment, bunker planning;
- **Operational:** weather routing, empty container repositioning, day-to-day disruption response.

Uncertainty dimensions repeatedly discussed include demand variation, travel/port time variability, fuel-price volatility, and disruption effects.

## Industry-Practice Gap

A central conclusion is the gap between optimization advances and practical deployment.

Reported reasons include:
- limited/fragmented data quality for uncertainty modeling;
- integration and implementation risk in existing planning stacks;
- difficulty of evaluating ROI for richer stochastic models;
- complexity of scenario generation and model maintenance.

The paper highlights buffering and decomposition-style planning as common practical mitigations when full stochastic optimization is not deployed.

## Future Directions

The review calls out recurring research needs:
- uncertainty-aware planning for decarbonization transitions (new fuels/technologies);
- integrated disruption-aware optimization across planning levels;
- improved statistical/ML scenario generation coupled with optimization;
- methods that remain usable under industrial data and runtime constraints.

Some recommendations imply a shift toward hybrid decision pipelines (forecasting + robust optimization + rolling-horizon control), though exact operational designs remain open. ^[inferred]

## Related

- [[concepts/maritime-routing-under-uncertainty]]
- [[references/christiansen2013-ship-routing-scheduling-new-millennium]]
- [[references/christiansen2020-liner-shipping-network-design]]
- [[_papers/fagerholt2023maritime/fagerholt2023maritime-extracted]]
- [[_papers/christiansen2013ship/christiansen2013ship-extracted]]
- [[_papers/gronhaug2010branchandprice/gronhaug2010branchandprice-extracted]]

## Bibliographic Record

- Citation key: `ksciuk2023uncertainty`
- DOI: `10.1016/j.ejor.2022.08.006`
- Canonical URL: <https://www.sciencedirect.com/science/article/pii/S0377221722007032>
- Publication: *European Journal of Operational Research* (2023)
- Authors: Tomasz Ksciuk; Franziska Kuhlemann; Kevin Tierney; Achim Koberstein
- Companion metadata note: [[_papers/ksciuk2023uncertainty/ksciuk2023uncertainty.md]]

## Sources

- [[_papers/ksciuk2023uncertainty/ksciuk2023uncertainty-extracted.md]]
- [[_papers/ksciuk2023uncertainty/ksciuk2023uncertainty.md]]
- [[_papers/ksciuk2023uncertainty/images/page_0_image_9.jpg]]
- [[_papers/ksciuk2023uncertainty/images/page_2_image_2.jpg]]
- [[_papers/ksciuk2023uncertainty/images/page_2_image_4.jpg]]
