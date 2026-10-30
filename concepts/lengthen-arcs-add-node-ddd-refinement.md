---
title: Lengthen-Arcs and Add-Node DDD Refinement
summary: Lengthening too-short arcs with Algorithm 2 and Add-Node keeps Properties
  1-4, guarantees correctness, opportunistic node additions, pruning with l0 = z -
  1.
type: concept
tags: [dynamic-discretization, integer-programming, time-space-network, modeling-pattern]
provenance:
  extracted: 0.9
  inferred: 0.1
  ambiguous: 0.0
base_confidence: 0.57
created: '2026-10-28T23:10:00+07:00'
updated: 2026-10-30T20:00:02Z
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
  - target: "[[references/santini2018-alns-acceptance-criteria]]"
    type: derived_from
  - target: "[[references/silver2018-alphazero-self-play-general-rl]]"
    type: derived_from
  - target: '[[concepts/partially-time-expanded-network-lower-bound]]'
    type: related_to
  - target: '[[concepts/primal-arc-sets-ddd-two-networks]]'
    type: related_to
  - target: '[[concepts/first-in-first-out-property-in-time-dependent-travel]]'
    type: related_to
  - target: '[[concepts/valid-inequalities-subtour-sequence-ddd]]'
    type: related_to
  - target: '[[concepts/duration-objective-depot-discretization]]'
    type: related_to
  - target: '[[concepts/dynamic-discretization-discovery]]'
    type: related_to
  - target: "[[references/vu2020-ddd-td-tsptw-time-expanded-network]]"
    type: related_to
  - target: "[[references/wahal2020-joint-value-profitability-international]]"
    type: related_to

---

> [!tldr] Lengthening too-short arcs by adding nodes, Algorithm 2 walking a solution path with Add-Node, keeps Properties 1-4, guarantees correctness, opportunistically creates nodes needed to continue along the path, and pruning with l_0 = z − 1 shrinks the network.

Algorithm 2 LENGTHEN-ARCS-PATH operates on a path, for each arc in the solution, it considers departure from u_i at t_i, computes t' = max{e_{u_j}, t + τ_{u_{j-1}u_j}(t)} for subsequent locations j, breaks if t' > l_j, calls Add-Node(u_j, t'), and updates t. An arc is lengthened when too short, t_{i+1} < t_i + τ_{u_i u_{i+1}}(t_i), and lengthening keeps the vehicle inside the window, e_{u_{i+1}} ≤ t_i + τ(t_i) ≤ l_{u_{i+1}}. Algorithm 3 ADD-NODE adds (j, t') to N_T if missing, creates arcs (j, t') to (k, t) for each k, choosing the largest t ≤ t' + τ_jk(t'), with cost underestimate, deletes arcs (i, t), (j, t'') with t'' < t' and t + τ_ij(t) ≥ t', and replaces them with ((i, t), (j, t')) with the cost underestimate.

Example: path (u_0, 1), (u_1, 1), (u_2, 2) with τ_{u_0u_1}(·) = 1, τ_{u_1u_2}(·) = 2, arc (u_0, 1), (u_1, 1) is too short, so node (u_1, 2) is added, the path continues to u_2, so node (u_2, 4) and arc (u_1, 2), (u_2, 4) are created, the same location sequence on true-travel-time arcs; sub-path from u_1 at time 1, arc (u_1, 1), (u_2, 2) too short, creates node (u_2, 3) and replaces the arc. Correctness requires lengthening one arc per iteration, opportunistic additions are computationally beneficial because each lengthened arc makes N_T, A_T closer to N, A, strengthening the bound.

Pruning, when a new feasible solution with makespan z is found, removes arcs (i, t), (j, t') with t + τ_ij(t) ≥ z, updates l_0 = z − 1, then repeats preprocessing, the preprocessing may make the partial instance infeasible, in which case the best feasible solution found so far is optimal. Nodes and arcs are never removed, so after finitely many iterations N_T = N, A_T = A, and the algorithm solves the original problem, terminating with a provably optimal solution. ^[inferred]

## Related

- [[concepts/partially-time-expanded-network-lower-bound]] - lengthening preserves Properties 1-4, the lower bound.
- [[concepts/primal-arc-sets-ddd-two-networks]] - primal solutions enable pruning, arcs with t + τ_ij(t) ≥ z removed, l_0 reset.
- [[concepts/first-in-first-out-property-in-time-dependent-travel]] - FIFO ensures the Δ values used by preprocessing remain valid.
- [[concepts/valid-inequalities-subtour-sequence-ddd]] - lengthening removes the current solution, inequalities rule out its location sequence, and all timed copies.
- [[concepts/duration-objective-depot-discretization]] - pruning uses l_0 = z − 1, the duration case uses l_0 = z − 1 + t_0.
- [[concepts/dynamic-discretization-discovery]] - the DDD pattern, refine network, solve, convert, lengthen.
- [[concepts/first-in-first-out-property-in-time-dependent-travel]] - FIFO.
- [[references/santini2018-alns-acceptance-criteria]] — shares   + , + - tags with this page
- [[references/silver2018-alphazero-self-play-general-rl]] — shares   + , + - tags with this page

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
