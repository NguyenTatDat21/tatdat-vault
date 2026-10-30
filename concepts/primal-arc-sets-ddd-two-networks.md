---
title: 'Primal Arc Sets in DDD: Two Networks'
summary: Two primal networks in DDD, arcs at least as long as correct travel time
  give feasible solutions, arcs with positive travel time exclude subtours, solution
  sources are set-dependent.
type: concept
tags: ['[dynamic-discretization', primal-heuristics, time-expanded-networks, feasible-solutions, tsp, 'arc-sets]']
provenance:
  extracted: 0.91
  inferred: 0.09
  ambiguous: 0.0
base_confidence: 0.67
created: '2026-10-28T23:10:00+07:00'
updated: 2026-10-30T14:38:55Z
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
  - target: '[[concepts/partially-time-expanded-network-lower-bound]]'
    type: related_to
  - target: '[[concepts/first-in-first-out-property-in-time-dependent-travel]]'
    type: related_to
  - target: '[[concepts/lengthen-arcs-add-node-ddd-refinement]]'
    type: related_to
  - target: '[[concepts/valid-inequalities-subtour-sequence-ddd]]'
    type: related_to
  - target: '[[concepts/duration-objective-depot-discretization]]'
    type: related_to
  - target: '[[concepts/dynamic-discretization-discovery]]'
    type: related_to
  - target: "[[references/vu2020-ddd-td-tsptw-time-expanded-network]]"
    type: related_to

---

> [!tldr] DDD uses two primal networks sharing the lower-bound node set, D̄¹ with arcs at least as long as correct travel time yields always-feasible solutions, D̄² without non-positive arcs has no subtours, the source of the best primal solution is set-dependent.

The lower-bound network has arc set A_T, the two primal networks D̄¹ = (N_T, Ā_T¹) and D̄² = (N_T, Ā_T²) have the same node set N_T. Ā¹ contains arcs ((i, t), (j, t'')) where t'' ≥ t + τ_ij(t), the smallest such t'', so any feasible solution of TD-TSPTW(D̄¹) yields a feasible solution to the original problem. Ā² includes arcs of A_T with t' > t, plus, for every arc in A_T with t' ≤ t, the arc ((i, t), (j, t'')) with the smallest t'' > t, so solutions cannot contain subtours, time points t'' always exist because nodes (j, l_j) are kept.

A candidate solution from the lower-bound network is converted when it has no subtour and no time-window-violating sequence, the conversion prescribes dispatch times as early as possible, with t'_0 = e_{v_0} and t'_{i+1} = max{e, t'_i + τ(t'_i)}, giving makespan value t'_{n+1}. Integer solutions collected by the solver, including non-optimal ones, are tested for conversion. Candidates from D̄¹ are guaranteed to be convertible, candidates from D̄² have no subtour but may have infeasible sequences.

The percentage of instances whose best primal solution came from the lower-bound network, D̄¹, D̄²: Set 1 4.21%, 53.76%, 42.04%, Set w100 23.41%, 39.95%, 36.64%. D̄¹ contributes slightly more often, and for w100 the lower-bound network produces the best solution much more often. With one primal IP enabled, D̄¹ alone: 952 instances 14.01 s, 7.81 iterations, D̄² alone 26.79 s, 5.83 iterations, both 10.94 s, 4.62 iterations, w100 D̄¹ 1.37 s/6.68, D̄² 3.01 s/5.13, both 1.22 s/4.11. Solving both primal IPs is best, D̄¹ is slightly more effective alone, the order matters because D̄¹ is solved first. ^[inferred]

The primal IPs improve primal bounds quickly, so the algorithm can assess solution quality, terminate, and prune arcs from the network, shrinking integer programs at later iterations.

## Related

- [[concepts/partially-time-expanded-network-lower-bound]] - the primal networks share the lower-bound node set.
- [[concepts/first-in-first-out-property-in-time-dependent-travel]] - FIFO guarantees the D̄¹ solutions are feasible and the D̄² network excludes non-positive arcs.
- [[concepts/lengthen-arcs-add-node-ddd-refinement]] - primal solutions enable pruning, the new feasible solution z removes arcs with t + τ_ij(t) ≥ z, resets l_0 = z − 1.
- [[concepts/valid-inequalities-subtour-sequence-ddd]] - the sequence and subtour inequalities, detected in the lower-bound network, apply to primal networks.
- [[concepts/duration-objective-depot-discretization]] - primal networks solved with the duration objective, tour durations enumerated over depot departures.
- [[concepts/dynamic-discretization-discovery]] - primal heuristic pattern in DDD, primal solutions found by solving restricted networks.
- [[concepts/first-in-first-out-property-in-time-dependent-travel]] - FIFO.

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
