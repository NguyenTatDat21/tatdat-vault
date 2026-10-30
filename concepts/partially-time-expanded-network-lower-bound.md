---
title: Partially Time-Expanded Network Lower Bound
summary: Partially time-expanded network, window endpoints, arcs that underestimate
  travel time, cost underestimates, longest arcs, lower bound by Lemma 1, optimality
  by Lemma 2.
type: concept
tags: [time-expanded-networks, lower-bounds, dynamic-discretization, integer-programming, relaxation, properties-lemmas]
provenance:
  extracted: 0.91
  inferred: 0.09
  ambiguous: 0.0
base_confidence: 0.57
created: '2026-10-28T23:10:00+07:00'
updated: 2026-10-30T19:12:06Z
tier: core
category: concepts
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
  - target: '[[concepts/first-in-first-out-property-in-time-dependent-travel]]'
    type: related_to
  - target: '[[concepts/primal-arc-sets-ddd-two-networks]]'
    type: related_to
  - target: '[[concepts/lengthen-arcs-add-node-ddd-refinement]]'
    type: related_to
  - target: '[[concepts/valid-inequalities-subtour-sequence-ddd]]'
    type: related_to
  - target: '[[concepts/duration-objective-depot-discretization]]'
    type: related_to
  - target: '[[concepts/dynamic-discretization-discovery]]'
    type: derived_from
  - target: "[[references/vu2020-ddd-td-tsptw-time-expanded-network]]"
    type: related_to

---

> [!tldr] A partially time-expanded network is a sparse subset of timed nodes and arcs that keeps window endpoints, includes every travel arc that can start at a represented time, underestimates costs, and keeps arcs as long as possible, giving a lower bound that strengthens as arcs are lengthened.

Property 1 requires the window-open and window-close nodes (i, e_i), (i, l_i) in N_T. Property 2 restricts N_T to times inside each location's window. Property 3 requires, for every (i, t) in N_T and arc (i, j) with t + τ_ij(t) ≤ l_j, a travel arc in A_T, and every arc in A_T must satisfy either t + τ_ij(t) < e_j with t' = e_j, or e_j ≤ t' ≤ t + τ_ij(t), so arcs under-estimate travel time; an arc is too short if t' < max{e_j, t + τ_ij(t)}, and the choice of arc implies a dispatch at time at least t. Property 4 defines the arc cost as the cost underestimate, c_ij(t) = min of c_ij(h) for h between t and l_i with h + τ_ij(h) ≤ l_j, the cheapest dispatch at time h ≥ t, so costs under-estimate how travel is represented in D. Property 5 states every arc is as long as possible, there is no node (j, t'') in N_T with t' < t'' ≤ t + τ_ij(t); Property 5 strengthens the bound, reducing the feasible region.

Lemma 1, lower bound: Properties 1-4 imply TD-TSPTW(D_T) gives a lower bound, proof maps any path p in D to p' in D_T with t'_k ≤ t_k, arcs in A_T, and underestimated costs, induction starting at the depot node at e_0. Lemma 2, optimality: with arc costs non-decreasing in t, and a path p' that corresponds to an optimal solution of the partial problem with t'_i = max{e_{u_i}, t'_{i-1} + τ(…)} for every node, a feasible optimal solution of TD-TSPTW(D) can be derived from p'. For the duration objective, costs are non-decreasing on all arcs leaving the depot, so adding a node (0, t) for every feasible departure time adapts the proof.

A feasible solution for TD-TSPTW(D_T) induces a depot-to-depot path plus disjoint cycles (subtours), every location appears exactly once in a cycle or in the path. Sparse discretization can yield subtours, and a path may violate time windows under true travel times. A solution to TD-TSPTW(D_T) gives a valid lower bound without solving the integer program to optimality, any lower bound on the partial IP value is a valid bound on the original.

The DDD algorithm starts with N_T = {e_i, l_i} and refines by lengthening arcs, preserving Properties 1-4; the primal networks D̄¹, D̄² share the node set N_T. ^[inferred]

## Related

- [[concepts/first-in-first-out-property-in-time-dependent-travel]] - the FIFO property is the condition that makes Properties 3 and 4 valid, Lemma 1, and the lengthen-arc procedure.
- [[concepts/primal-arc-sets-ddd-two-networks]] - the primal networks built on the same node set, with arcs at least as long as correct travel time, and arcs with positive travel time.
- [[concepts/lengthen-arcs-add-node-ddd-refinement]] - the lengthening that preserves the properties.
- [[concepts/valid-inequalities-subtour-sequence-ddd]] - the subtour and sequence inequalities, location-defined, applied to every time-expanded network.
- [[concepts/duration-objective-depot-discretization]] - the depot-node set for the duration objective, the lower-bound lemma adapted to feasible tours.
- [[concepts/dynamic-discretization-discovery]] - the DDD framework in service network design, the lower-bound-then-refine pattern.
- [[concepts/first-in-first-out-property-in-time-dependent-travel]] - the FIFO family.

## Sources

- `- "[[_papers/vu2020dynamic/vu2020dynamic-extracted.md]]"`
- `- "[[_papers/vu2020dynamic/vu2020dynamic.md]]"`
- `- "[[_papers/vu2020dynamic/images/page_9_image_3.jpg]]"`
- `- "[[_papers/vu2020dynamic/images/page_9_image_5.jpg]]"`
- `- "[[_papers/vu2020dynamic/images/page_12_image_1.jpg]]"`
- `- "[[_papers/vu2020dynamic/images/page_18_image_1.jpg]]"`
- `- "[[_papers/vu2020dynamic/images/page_18_image_3.jpg]]"`
- `- "[[_papers/vu2020dynamic/images/page_22_chart_1.jpg]]"`
- `- "[[_papers/vu2020dynamic/images/page_23_chart_1.jpg]]"`
- `- "[[_papers/vu2020dynamic/images/page_27_image_5.jpg]]"`
