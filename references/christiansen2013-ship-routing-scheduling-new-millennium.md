---
title: Ship Routing and Scheduling in the New Millennium (Christiansen et al., 2013)
category: references
tags: [maritime, ship-routing-scheduling]
relationships:
  - target: "[[references/christiansen2007-maritime-transportation-operations-research]]"
    type: extends
  - target: "[[references/christiansen2020-liner-shipping-network-design]]"
    type: related_to
  - target: "[[concepts/maritime-inventory-routing-problem]]"
    type: related_to
  - target: "[[concepts/liner-shipping-network-design]]"
    type: related_to
  - target: "[[references/mutlu2016-lng-annual-delivery-program]]"
    type: related_to
  - target: "[[references/papageorgiou2014-mirplib-mirp-instance-library]]"
    type: related_to
  - target: "[[concepts/maritime-routing-under-uncertainty]]"
    type: related_to
  - target: "[[references/christiansen2008-maritime-inventory-routing-problems]]"
    type: related_to
  - target: "[[references/fagerholt2023-maritime-inventory-routing-survey]]"
    type: related_to
  - target: "[[references/ksciuk2023-maritime-uncertainty-review]]"
    type: related_to
sources:
  - _papers/christiansen2013ship/christiansen2013ship-extracted.md
  - _papers/christiansen2013ship/christiansen2013ship.md
summary: "Fourth instalment of the ship routing survey series, covering 2002-2011: four basic models, liner network design and fleet deployment, and evidence that papers and outlets double each decade."
provenance:
  extracted: 0.91
  inferred: 0.07
  ambiguous: 0.02
base_confidence: 0.67
lifecycle: draft
lifecycle_changed: 2026-10-22
tier: core
created: 2026-10-22T23:17:15Z
updated: 2026-10-30T17:41:00Z
---

# Ship Routing and Scheduling in the New Millennium (Christiansen et al., 2013)

> [!tldr] A landmark review of maritime OR in 2002–2011 that formalizes liner network design and fleet deployment, then maps how methods evolved toward decomposition and richer planning scope.

## Problem & Contribution

This invited review is the fourth instalment in the ship routing and scheduling survey series (Ronen 1983, 1993; Christiansen et al. 2004). It covers work published in print and online in 2002–2011, focusing on prescriptive models rather than descriptive ones, and finds over a hundred new refereed papers, with research volume and outlets roughly doubling each decade. Model scope expanded from narrow routing tasks to integrated network, deployment, inventory-routing, LNG, speed and emissions decisions. The review excludes working papers, conference proceedings, theses, technical reports, non-commercial vessels (e.g. naval), and container-line specifics such as berth scheduling, stowage, container management, yard management and cargo allocation.

The paper contributes:
- four basic models in the domain, plus a planning-structure map for the three operating modes — **liner** (fixed route on a published schedule, profit maximization, like a public bus), **industrial** (the operator owns the cargo and controls the ships, minimizing delivery cost, like a private fleet) and **tramp** (ships follow the available cargoes, including optional ones, maximizing profit, like a taxi cab);
- canonical optimization models for liner network design and fleet deployment;
- trend analysis of publication counts, journals and topics;
- explicit research gaps for unresolved practical-scale problems.
- a planning-structure map for liner, tramp, and industrial modes,
- canonical optimization models for liner network design and fleet deployment,
- trend analysis by method class and application area,
- explicit research gaps for unresolved practical-scale problems.

## Core Models (Representative Equations)

### Liner network design objective (simplified review model)

$$
\max \Big(\text{transport revenue} - \sum_{(o,d,i)\in\mathcal W}\sum_{a\in\mathcal A} C_a^C y_a^{(o,d,i)} - \sum_{v\in\mathcal V}\sum_{r\in\mathcal R} C_{vr}^V x_{vr}\Big)
$$

subject to flow conservation, ship-capacity coupling on arcs, demand bounds, and ship-availability constraints (Eq. 1–7 in the paper). A route is defined by three decisions: which ports to visit and in what sequence, how often to visit them, and the size and speed of ships. The graph gives every port a node for each day of the week, with three arc subsets: ship legs between neighbouring ports (1–7 days plus whole weeks), port/ground arcs from day $i$ to $i+1$, and artificial arcs from destination back to origin that close the container flows. The model is a simplified version of Agarwal & Ergun (2008): it selects routes from a given set, whereas they generate new cycles by column generation and solve with Benders decomposition. Published network design models in the decade fall into four categories — single-route/sets of routes without transshipment, hub-and-feeder with each feeder tied to one hub, models classifying some ports as hubs without visit constraints, and multi-route models with no hub/non-hub separation.

### Fleet deployment model (reviewed template)

$$
\min \sum_{v\in\mathcal V}\sum_{r\in\mathcal R}\left(C_{vr}x_{vr}+C_v^I n_{vr}^I\right)+\sum_{v\in\mathcal V}\left(C_v^L d_v-C_v^O n_v^O\right)
$$

with demand satisfaction, frequency, vessel-availability, voyage-time, lay-up and chartering-in/out constraints (Eq. 8–17; $C^I$, $C^O$ chartering costs, $C^L$ daily lay-up cost). Fleet deployment is a tactical problem with a horizon of a shipping season up to six months, the model being inspired by Powell & Perakis (1997) and Gelareh & Meng (2010).

## Key Evidence

| Signal from review | Reported value / implication |
|---|---|
| Fleet growth in 2000–2010 decade | Oil tankers +60%, dry bulk +65%, containership capacity +164%; world fleet 683 → 1,276 million dwt from 1980 to 2010, container share 11 → 169 million dwt (Table 1, UNCTAD 2011, vessels over 100 gross tons) |
| Seaborne trade growth | International seaborne trade rose from 3,704 million tons loaded in 1980 to 8,408 in 2010, about +40% across the 2000s (Table 2) |
| Port-time economics | Container ships spend 15–30% of route time in ports (lower share for longer lines); break-bulk operations used 50–70%, because ships are productive only when sailing |
| Publication outlets (Table 3) | Top-10 outlets mix maritime journals (MPM, MEL), transportation journals (TS, TRE) and general OR journals; EJOR, JORS, TRE, COR and MEL attracted more papers in recent years, OR and NRL fewer |
| Topic trend (Table 4) | Fast growth in the last five years with increased attention to liners, plus specialized topics: sailing speed, MIR, LNG transportation and offshore supply vessel operations; the authors note the liner research gap is closing fast |

## Practical Insights

- Integrated maritime planning is increasingly necessary because network design, deployment, and cargo/inventory decisions interact strongly.
- The review's own trend data — papers and outlets doubling per decade, with growth concentrated in specialized domains — suggests maritime OR succeeds when it matches a model to one operator's real planning horizon (strategic network, tactical deployment, operational routing) rather than to a generic VRP variant.
- Pure monolithic formulations often face scalability limits, motivating decomposition and matheuristic pipelines. ^[inferred]
- Data/model realism grew (e.g., transshipment costs, speed decisions, uncertainty), but unresolved critical problems remained open in 2013.

## Limitations

- As a review, conclusions depend on coverage choices (English refereed outlets, 2002–2011 window, prescriptive models only); working papers, theses, conference proceedings, naval operations and container-line micro-problems are outside the map.
- Reported computational comparisons are not based on a single unified benchmark across all subtopics. MIRPLib [[references/papageorgiou2014-mirplib-mirp-instance-library]] later supplied the public instance set that filled this benchmark gap.
- The four 'basic models' are simplified templates; the paper's own network design model omits transshipment costs and caps each ship type at one weekly departure per route, so real-world costs and schedules are richer than the formulation. ^[inferred]
- Reported computational comparisons are not based on a single unified benchmark across all subtopics.

## Related

- [[references/christiansen2007-maritime-transportation-operations-research]]
- [[references/christiansen2020-liner-shipping-network-design]]
- [[references/mutlu2016-lng-annual-delivery-program]]
- [[concepts/maritime-inventory-routing-problem]]
- [[concepts/liner-shipping-network-design]]
- [[concepts/maritime-routing-under-uncertainty]]
- [[references/christiansen2020-liner-shipping-network-design]]
- [[concepts/maritime-inventory-routing-problem]]
- [[concepts/liner-shipping-network-design]]
- [[concepts/maritime-routing-under-uncertainty]]
- [[references/papageorgiou2014-mirplib-mirp-instance-library]]

## Bibliographic Record

- Citation key: `christiansen2013ship`
- DOI: `10.1016/j.ejor.2012.12.002`
- Canonical URL: <https://www.sciencedirect.com/science/article/pii/S037722171300003X>
- Publication: *European Journal of Operational Research* (2013)
- Authors: Marielle Christiansen; Kjetil Fagerholt; Bjørn Nygreen; David Ronen
- Companion metadata note: [[_papers/christiansen2013ship/christiansen2013ship.md]]

## Sources

- [[_papers/christiansen2013ship/christiansen2013ship-extracted.md]]
- [[_papers/christiansen2013ship/christiansen2013ship.md]]
