---
title: First-In, First-Out Property in Time-Dependent Travel
summary: First-In, First-Out property for time-dependent travel, piecewise-linear
  travel-time functions with slope at least -1, and the Ichoua-Gendreau-Potvin interval-constant
  model.
type: concept
tags: '[time-dependent-travel, fifo-property, travel-time-functions, piecewise-linear,
  routing, preprocessing]'
provenance:
  base: 0.0
  extracted: 0.9
  inferred: 0.1
  ambiguous: 0.0
base_confidence: 0.67
created: '2026-10-28T23:10:00+07:00'
updated: '2026-10-28T23:10:00+07:00'
tier: supporting
lifecycle: draft
lifecycle_changed: '2026-10-28'
sources:
- '  - "[[_papers/vu2020dynamic/vu2020dynamic-extracted.md]]"'
- '  - "[[_papers/vu2020dynamic/vu2020dynamic.md]]"'
- '  - "[[_papers/vu2020dynamic/images/page_9_image_3.jpg]]"'
- '  - "[[_papers/vu2020dynamic/images/page_9_image_5.jpg]]"'
- '  - "[[_papers/vu2020dynamic/images/page_12_image_1.jpg]]"'
- '  - "[[_papers/vu2020dynamic/images/page_18_image_1.jpg]]"'
- '  - "[[_papers/vu2020dynamic/images/page_18_image_3.jpg]]"'
- '  - "[[_papers/vu2020dynamic/images/page_22_chart_1.jpg]]"'
- '  - "[[_papers/vu2020dynamic/images/page_23_chart_1.jpg]]"'
- '  - "[[_papers/vu2020dynamic/images/page_27_image_5.jpg]]"'
relationships:
  - target: "[[references/santini2018-alns-acceptance-criteria]]"
    type: derived_from
  - target: "[[references/wahal2020-joint-value-profitability-international]]"
    type: derived_from
  - target: '[[concepts/partially-time-expanded-network-lower-bound]]'
    type: related_to
  - target: '[[concepts/lengthen-arcs-add-node-ddd-refinement]]'
    type: uses
  - target: '[[concepts/duration-objective-depot-discretization]]'
    type: uses
  - target: '[[concepts/dynamic-discretization-discovery]]'
    type: related_to
  - target: '[[concepts/valid-inequalities-subtour-sequence-ddd]]'
    type: related_to
---

> [!tldr] The First-In, First-Out property for time-dependent travel: a later departure cannot produce an earlier arrival, piecewise-linear travel-time functions have slope at least minus 1, and FIFO makes waiting at non-depot locations unnecessary.

The FIFO property is assumed on arcs, for all arcs (i, j) and times t ≤ t', t + τ_ij(t) ≤ t' + τ_ij(t'). A piecewise-linear travel-time function satisfies FIFO exactly when all linear pieces have slope at least −1, so a later departure cannot lead to an earlier arrival, the arrival time is non-decreasing in departure time.

Ichoua, Gendreau and Potvin (2003) propose a travel-time function that enforces FIFO, assuming travel speeds are constant within a time interval and change from one interval to the next, this is the travel model used for time-dependent TSP variants. Ghiani and Guerriero (2014) study properties of this function and propose generalizations. The FIFO assumption is standard in the time-dependent routing literature; studies of the time-dependent TSP that do not enforce FIFO include Picard and Queyranne 1978, Lucena 1990, Fischetti et al. 1993, Gouveia and Voz 1995, Albiach et al. 2008, Stecco et al. 2008, Méndez-Díaz et al. 2011, Bront et al. 2014, Abeledo et al. 2013, and Melgarejo et al. 2015.

For makespan and duration objectives, FIFO implies it is never advantageous to wait at a location other than at the depot in the duration case, so an optimal solution only waits when arriving before a time window opens. Δ_ij(t), the earliest time the vehicle can depart location j after departing i at time t, equals max{e_j, t + τ_ij(t)} when travel times satisfy the triangle inequality, and otherwise is computed by solving shortest path problems, where the FIFO property is what makes the Δ values valid. Preprocessing rules push e_k up to min over i of Δ_ik(e_i) capped by l_k, and push l_k down to max over i of Δ_ki(t) ≤ l_i, and when waiting is not beneficial also push e_k with max over t of Δ_ki(t) ≤ e_i and l_k with Δ_ik(l_i). Infeasible sequences, i → j with Δ_ij(e_i) > l_j, define precedence j ≺ i, arc (i, j) is eliminated, triplets i → j → k, k → i → j, i → k → j give more precedences, precedences are transitively closed, arcs (i, 0) and (0, j) are removed for precedences, and arcs (i, k) for chains of precedences. ^[inferred]

FIFO is the structural condition that makes time-expanded-network formulations handle time-dependent travel times naturally, a later-dispatch arc simply updates the appropriate arc in the network, so the number of travel-time breakpoints does not make the method more expensive.

## Related

- [[concepts/partially-time-expanded-network-lower-bound]] - the FIFO property underpins the lower-bound proof, arc lengthening, and primal networks.
- [[concepts/lengthen-arcs-add-node-ddd-refinement]] - FIFO enables the lengthen-arc procedure, the Δ values, and pruning.
- [[concepts/duration-objective-depot-discretization]] - FIFO makes depot waiting the only beneficial waiting, the basis of the duration adaptation.
- [[concepts/dynamic-discretization-discovery]] - the DDD framework assumes time-expanded networks built from FIFO-consistent travel times.
- [[concepts/valid-inequalities-subtour-sequence-ddd]] - FIFO guarantees infeasible location sequences under true travel times, so sequence inequalities are location-based.
- [[concepts/first-in-first-out-property-in-time-dependent-travel]] - the same family, the FIFO property, the slope-at-least-(-1) piecewise-linear travel time functions, the Ichoua-Gendreau-Potvin function, the triangle inequality, the preprocessing rules, the infeasible sequences, the precedence, transitive closure, arc removal, the shortest path Δ values.
- [[references/santini2018-alns-acceptance-criteria]] — shares   + , + - tags with this page
- [[references/wahal2020-joint-value-profitability-international]] — shares   + , + - tags with this page

