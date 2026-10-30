---
title: Encodings That Survive Composition and Merging
summary: "An encoding's value survives only specific compositions: tree-convex stays tractable after merging, DNNF simulation stays quasipolynomial, implication chains beat separate encodings."
tags: [encodings, tractability, local-consistency, broken-triangle, pseudo-boolean, microstructure]
provenance:
  extracted: 0.72
  inferred: 0.18
  ambiguous: 0.10
base_confidence: 0.67
tier: core
category: concepts
created: 2026-10-29T15:45:00Z
updated: 2026-10-30T14:38:55Z
sources:
  - _papers/pesant2015principles/pesant2015principles.md
  - _papers/pesant2015principles/pesant2015principles-extracted.md
relationships:
  - target: references/pesant2015-cp2015-proceedings
    type: related_to
  - target: concepts/disjunctive-scheduling-constraint-programming-model
    type: related_to
  - target: concepts/cumulative-volume-lower-bound-cp-search
    type: related_to
  - target: "[[concepts/automated-model-generation]]"
    type: related_to
  - target: "[[concepts/large-neighborhood-search]]"
    type: related_to
  - target: "[[concepts/variable-neighborhood-search]]"
    type: related_to
lifecycle: draft
lifecycle_changed: 2026-10-29T15:45:00Z
---

# Encodings That Survive Composition and Merging

> [!tldr] A tractable encoding is a class closed under the operations the solver performs. CP 2015 gives four closure results: tree-preserving constraints closed under composition and intersection; broken-triangle merges that preserve satisfiability; microstructure width-3 families; and encoding-size bounds for pseudo-Boolean encodings.

## Summary

Propagation adds constraints, so the tractable classes that matter are those closed under composition and intersection. Tree-preserving constraints over tree domains are the closure result behind path-consistency on tree-convex constraints (idx 26, chapter 18, pp. 244-261). Satisfiability-preserving merges on the microstructure collapse value pairs into one value, and the order of merges matters (idx 13, chapter 5, pp. 58-73). Microstructure width is the combinatorial lever (idx 14, chapter 6, pp. 74-88). Encoding size is the same question for SAT: the size of a network is a function of composition, and it grows in a predictable way (idx 23, chapter 15, pp. 200-209; idx 24, chapter 16, pp. 210-225).

## Key ideas

- **Tree-preserving constraints** — the paper's target is tractable classes of tree-convex constraints (extensions of row-convex constraints) closed under the composition and intersection used by path-consistency algorithms; Definitions 1-10 formalise tree, rooted tree, tree of T, k-consistency, tree-convex, consecutive, path-preserving and tree-preserving over finite tree domains `T_x = (D_x, E_x)` (idx 26, chapter 18, pp. 244-261).
- **Tractability restoration** — every chain- or path-preserving constraint network is in essence the disjoint union of several independent CRC constraint networks, which re-establishes tractability for those classes (idx 26, chapter 18, pp. 244-261).
- **Scene labelling stays hard** — the scene labelling problem is NP-complete in general and NP-complete even for trihedral scenes where no four planes share a point; there are 39 possible configurations of two neighbouring nodes in a 2D projective scene (idx 26, chapter 18, pp. 244-261).
- **Broken-triangle merges** — a broken triangle is a pattern of (in)compatibilities between assignments; BT-free value pairs can be BTP-merged, a satisfiability-preserving operation, and the order of BTP-merges matters (idx 13, chapter 5, pp. 58-73).
- **Finding the best merges is hard** — maximizing the number of BTP-merges is NP-hard even with domain bound 3 and in arc-consistent instances, and NP-complete at a single variable (idx 13, chapter 5, pp. 58-73).
- **Microstructure width** — binary CSP with n Boolean variables and domain size 2 has a microstructure graph G(I) with nodes (i, v); the width-3 family, b ≤ 3, and the micro-acyclic tractable micro-Boolean-width classes are polynomial, width 3 included (idx 14, chapter 6, pp. 74-88).
- **Encoding size under composition** — the generalized totalizer is an arc-consistency-preserving extension of the Totalizer with exponential worst case for weights `2^0 … 2^(n-1)` and polynomial size when the largest weight is a polynomial P(n), the number of distinct combinations bounded by `n P(n)` (idx 23, chapter 15, pp. 200-209).
- **Network size formulas** — odd-even (Batcher) and pairwise (Parberry 1992) networks have exactly the same size and depth; the new family needs fewer comparators, the difference growing with k and equal to `n (log n − 4)/2 + log n + 2` at `k = n/2` (idx 24, chapter 16, pp. 210-225).
- **Implication-chain encodings** — exploiting implication chains already present gives encodings smaller than and propagating more strongly than separate encodings, a strict generalization of the MDD encoding (idx 9, chapter 1, pp. 3-11).
- **Simulating compiled forms** — DNNF can be simulated by non-deterministic read-once branching programs of quasi-polynomial size, so the exponential lower bounds for that formalism do not carry over (idx 34, chapter 26, pp. 367-375).
- **Choosing among encodings** — meSAT translates finite linear CSP specifications with several encodings and selects one by kNN, so encoding choice is itself a decision variable of the solver (idx 71, journal-track abstract, p. 741).

## Related

- [[references/pesant2015-cp2015-proceedings]] — the volume these results are drawn from
- [[concepts/disjunctive-scheduling-constraint-programming-model]] — encoding choice dominates scheduling models
- [[concepts/cumulative-volume-lower-bound-cp-search]] — bound computation is a propagation-strength question
- [[concepts/large-neighborhood-search]] — LNS re-solves encodings over neighborhoods

## Sources

- `_papers/pesant2015principles/pesant2015principles-extracted.md` (18,510 lines), chapters 1, 5, 6, 15, 16, 18, 26 and the idx 71 abstract.
