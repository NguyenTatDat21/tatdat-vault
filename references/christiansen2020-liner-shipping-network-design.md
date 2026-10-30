---
title: Liner Shipping Network Design Survey (Christiansen et al., 2020)
category: references
tags: [maritime, survey]
relationships:
  - target: "[[concepts/liner-shipping-network-design]]"
    type: related_to
  - target: "[[references/christiansen2013-ship-routing-scheduling-new-millennium]]"
    type: extends
  - target: "[[concepts/maritime-routing-under-uncertainty]]"
    type: related_to
  - target: "[[references/ksciuk2023-maritime-uncertainty-review]]"
    type: related_to
sources:
  - _papers/christiansen2020liner/christiansen2020liner-extracted.md
  - _papers/christiansen2020liner/christiansen2020liner.md
summary: >-
  A comprehensive LSNDP survey that formalizes service design, fleet deployment, and commodity flow integration, and compares four main algorithm families against LINER-LIB benchmarks.
provenance:
  extracted: 0.9
  inferred: 0.08
  ambiguous: 0.02
base_confidence: 0.67
lifecycle: draft
lifecycle_changed: 2026-10-22
tier: core
created: 2026-10-22T23:17:15Z
updated: 2026-10-30T17:41:00Z
---

# Liner Shipping Network Design Survey (Christiansen et al., 2020)

> [!tldr] This survey consolidates modern liner shipping network design by defining a common modeling core and comparing integrated MIP, two-stage, subset-of-services, and backbone-flow algorithm paradigms.

## Problem & Contribution

The paper studies the **Liner Shipping Network Design Problem (LSNDP)**: design weekly services, assign vessels, and route multi-commodity demand under capacity and transit constraints while balancing revenue and operating costs.

Major contribution:
- unified notation and service-flow formulations,
- structured taxonomy of algorithm families,
- benchmark-oriented comparison through LINER-LIB,
- practical discussion of constraints that matter in industrial deployments.

## Core Formulation (Service-based LSNDP)

A representative service-based model is:

$$
\min \sum_{s\in S} c_s y_s + \sum_{k\in K}\sum_{(i,j)\in A} c_{ij}^k \sum_{s\in S} x_{ij}^{ks}
$$

subject to:

$$
\sum_{s\in S}\sum_{j:(i,j)\in A} x_{ij}^{ks} - \sum_{s\in S}\sum_{j:(j,i)\in A} x_{ji}^{ks} = \xi_i^k \quad \forall i\in N, k\in K
$$

$$
\sum_{k\in K} x_{ij}^{ks} \le u_{ij}^{s} y_s \quad \forall s\in S,(i,j)\in A
$$

$$
\sum_{s\in S} m_v^s y_s \le m_v \quad \forall v\in V
$$

where service selection (`y_s`) and flow variables (`x_{ij}^{ks}`) couple design and cargo routing.

## Method Taxonomy

The survey groups LSNDP methods into four families:
1. **Integrated MIP formulations** (joint design + flow in one model),
2. **Two-stage methods** (design then flow, often with feedback loops),
3. **Subset-of-services methods** (select from candidate services),
4. **Backbone-flow methods** (flow-first to induce high-load backbone links, then service design).

This framing clarifies why fully integrated exact approaches struggle at large scale, while decomposition/heuristics dominate practical deployments.

## Benchmark Context (LINER-LIB)

The paper highlights LINER-LIB as a shared benchmark suite with instances from small single-hub to world-scale multi-hub settings (up to 197 ports and 9,630 OD pairs), enabling reproducible algorithm comparisons.

## Practical Insights

- Transit-time constraints, transshipment costs, demand rejection, and speed optimization are not optional details; they materially alter both model difficulty and solution quality.
- Service shape flexibility (simple, butterfly, pendulum, complex) changes both tractability and realism.
- Industrial utility often depends on balancing optimization quality with planner-acceptable network stability. ^[inferred]

## Limitations

- As a survey, model comparison depends on heterogeneous assumptions and reporting conventions across papers.
- Several algorithm classes are assessed through benchmark proxies rather than fully harmonized industrial data pipelines.

## Related

- [[concepts/liner-shipping-network-design]]
- [[references/christiansen2013-ship-routing-scheduling-new-millennium]]
- [[references/christiansen2007-maritime-transportation-operations-research]]
- [[concepts/maritime-routing-under-uncertainty]]
- [[references/boland2017-continuous-time-service-network-design]]

## Bibliographic Record

- Citation key: `christiansen2020liner`
- DOI: `10.1016/j.ejor.2019.09.057`
- Canonical URL: <https://doi.org/10.1016/j.ejor.2019.09.057>
- Publication: *European Journal of Operational Research* (2020)
- Authors: Marielle Christiansen; Erik Orm Hellsten; David Pisinger; David Sacramento; Charlotte Vilhelmsen
- Companion metadata note: [[_papers/christiansen2020liner/christiansen2020liner.md]]

## Sources

- [[_papers/christiansen2020liner/christiansen2020liner-extracted.md]]
- [[_papers/christiansen2020liner/christiansen2020liner.md]]
