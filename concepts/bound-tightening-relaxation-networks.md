---
title: Bound Tightening in Relaxation Networks
summary: "Convex relaxations tighten bounds where CP bound consistency leaves them loose: relaxation networks, Lagrangian bounds and diagram relaxations drive the pruning."
tags: [bound-consistency, convex-relaxation, power-network, cumulative, interval-propagation]
provenance:
  extracted: 0.72
  inferred: 0.18
  ambiguous: 0.10
base_confidence: 0.67
tier: core
category: concepts
created: 2026-10-29T15:47:00Z
updated: 2026-10-30T14:38:55Z
sources:
  - _papers/pesant2015principles/pesant2015principles.md
  - _papers/pesant2015principles/pesant2015principles-extracted.md
relationships:
  - target: references/pesant2015-cp2015-proceedings
    type: related_to
  - target: concepts/lagrangian-decomposition-propagation
    type: related_to
  - target: concepts/cumulative-volume-lower-bound-cp-search
    type: related_to
  - target: concepts/disjunctive-scheduling-constraint-programming-model
    type: related_to
  - target: "[[concepts/auxiliary-decision-variable-model-strengthening]]"
    type: related_to
    note: "Reciprocal - concepts/auxiliary-decision-variable-model-strengthening references this page."
    confidence: 0.7
    basis: observed
    since: "2026-10-30T14:38:55Z"
  - target: "[[concepts/decision-diagrams-optimization]]"
    type: related_to
    note: "Reciprocal - concepts/decision-diagrams-optimization references this page."
    confidence: 0.7
    basis: observed
    since: "2026-10-30T14:38:55Z"
  - target: "[[concepts/large-neighborhood-search]]"
    type: related_to
    note: "Reciprocal - concepts/large-neighborhood-search references this page."
    confidence: 0.7
    basis: observed
    since: "2026-10-30T14:38:55Z"
lifecycle: draft
lifecycle_changed: 2026-10-29T15:47:00Z
---

# Bound Tightening in Relaxation Networks

> [!tldr] Bound tightening is CP's contribution to convex relaxation: a relaxation network over interval domains, a minimal-network fixpoint, and bound-consistency filtering. The same interval-shrinking view gives the time-table rules for cumulative resources.

## Summary

A convex relaxation of the non-convex AC power flow model is written as a constraint network on intervals — the CCN triple (X, I, C) of variables, interval domains, and constraints — and bound tightening runs minCCRN and bcCCRN fixpoint algorithms on it, with Proposition 1 stating soundness, MINCCN ⊆ bcCCRN (idx 12, chapter 4, pp. 39-57). On the CP side the interval-shrinking rules for cumulative resources are Eq. (2) `(t < C) ⇒ t < s_i` for start times, with end times updated symmetrically, and the mandatory-profile rectangle ⟨a_j, b_j, h_j⟩ (idx 19, chapter 11, pp. 149-158).

## Key ideas

- **Relaxation as a CP network** — convex relaxation networks (CCRN) are handled with CP concepts, minimal network and bound consistency, tightening variable bounds so the relaxation becomes smaller (idx 12, chapter 4, pp. 39-57).
- **QC-N and QC-B close the gap** — the two tightening schemes significantly reduce QC optimality gaps; QC-N closes the AC-OPF gap below 1 % in 90 % of cases and closes 10 open test cases, and almost always outperforms SDP (idx 12, chapter 4, pp. 39-57).
- **Soundness of tightening** — minCCRN/bcCCRN are fixpoint algorithms, and Proposition 1 states MINCCN ⊆ bcCCRN, so the tightened network remains sound (idx 12, chapter 4, pp. 39-57).
- **Time-table rules** — for a single cumulative resource with capacity C and tasks with `s_i + d_i = e_i`, the start-time rule is Eq. (2) `(t < C) ⇒ t < s_i`, with end times updated symmetrically, using rectangles ⟨a_j, b_j, h_j⟩ in the mandatory profile (idx 19, chapter 11, pp. 149-158).
- **Left-conflict test in linear time** — Proposition 1: `j* = argmax{h_j | ⟨a_j,b_j,h_j⟩ ∈ TT_Ω ∧ [a_j,b_j[ ∩ [s̲_i, min(e̲_i, s̄_i)[ ≠ ∅}`, and j* is in left-conflict iff `h_{j*} + c_i > C`, otherwise task i has no left conflict; the RMQ-based algorithm achieves this with a linear-time scan (idx 19, chapter 11, pp. 149-158).
- **Profile built only from mandatory parts** — the scalable algorithm restricts the profile to tasks that have a mandatory part, set Ω_u = {i | s̲_i < s̄_i} (idx 19, chapter 11, pp. 149-158).
- **Bound-consistent temporal global constraint** — the ExistAllen(T, R, I) propagator is bound-consistent, linear O(n+m) versus O(n×m) for the natural algorithm, and works for any of the 2^13 relation combinations without tuning (idx 16, chapter 8, pp. 105-120).
- **Transition-time lower bounds** — extended Θ-tree and Θ-Λ-tree integrate transition-time lower bounds while overload checking, detectable precedences, not-first/not-last and edge-finding stay at O(n log n) (idx 15, chapter 7, pp. 89-104).

## Related

- [[references/pesant2015-cp2015-proceedings]] — the volume these papers are drawn from
- [[concepts/lagrangian-decomposition-propagation]] — the dual-side bound mechanism
- [[concepts/cumulative-volume-lower-bound-cp-search]] — cumulative bounds in CP search
- [[concepts/disjunctive-scheduling-constraint-programming-model]] — unary and cumulative resource models

## Sources

- `_papers/pesant2015principles/pesant2015principles-extracted.md` (18,510 lines), chapters 4, 7, 8, 11.
