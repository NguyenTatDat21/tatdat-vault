---
title: Decision Diagrams as Propagation and Bounds
summary: "BDD/MDD propagation, relaxed-BDD linear relaxations, and MDD sequence constraints turn diagram structure into bounds and faster search."
tags: [exact-methods, branch-and-cut, approximation-algorithms]
provenance:
  extracted: 0.5
  inferred: 0.25
  ambiguous: 0.25
base_confidence: 0.67
tier: core
category: concepts
created: 2026-10-29T15:48:00Z
updated: 2026-10-31T15:41:41Z
sources:
  - _papers/pesant2015principles/pesant2015principles.md
  - _papers/pesant2015principles/pesant2015principles-extracted.md
relationships:
  - target: references/pesant2015-cp2015-proceedings
    type: related_to
  - target: concepts/bound-tightening-relaxation-networks
    type: related_to
  - target: concepts/lagrangian-decomposition-propagation
    type: related_to
  - target: concepts/cumulative-volume-lower-bound-cp-search
    type: related_to
  - target: "[[concepts/large-neighborhood-search]]"
    type: related_to
  - target: "[[concepts/variable-neighborhood-search]]"
    type: related_to
lifecycle: draft
lifecycle_changed: 2026-10-29T15:48:00Z
provenance_note: "Marker pass: markers match the numbers (4 extracted / 2 inferred / 2 ambiguous claim units); extracted = every distinctive term in the claim appears in the source text."
---



# Decision Diagrams as Propagation and Bounds

> [!tldr] A decision diagram encodes the feasible assignments of a constraint compactly, so propagation is consistency on the diagram. The same diagram, relaxed, is a linear relaxation: MDD consistency is NP-hard and fixed-parameter tractable in sub-sequence length, and relaxed BDDs give branch-and-bound bounds that are tighter than any previously reported. ^[extracted]

## Summary

MDD consistency on the Sequence constraint is NP-hard, with a fixed-parameter tractability result in the sub-sequence length (idx 65, journal-track abstract, p. 734, JAIR 50:697-722, 2014). The journal-track version applies the same idea to optimization: relaxed BDDs act as linear relaxations inside a branch-and-bound, giving bounds for MAXCUT tighter than previously reported (idx 66, journal-track abstract, p. 735, INFORMS J. Computing 2015). Lagrangian decomposition uses MDD/BDD relaxations as the subproblem structure (idx 11, chapter 3, pp. 30-38), and the implication-chain encodings are a strict generalization of the MDD encoding (idx 9, chapter 1, pp. 3-11). ^[ambiguous]

## Key ideas

- **MDD consistency, complexity** — establishing MDD consistency on the Sequence constraint is NP-hard; the analysis is FPT in the sub-sequence length (idx 65, journal-track abstract, p. 734, JAIR 50:697-722, 2014). ^[extracted]
- **Relaxed BDD as a relaxation** — the branch-and-bound uses relaxed BDDs as linear relaxations, and the reported MAXCUT bounds are tighter than any reported before (idx 66, journal-track abstract, p. 735, INFORMS J. Computing 2015). ^[ambiguous]
- **Simulating compiled forms** — DNNF can be simulated by non-deterministic read-once branching programs of quasi-polynomial size, which shows exponential lower bounds for that formalism do not transfer (idx 34, chapter 26, pp. 367-375). ^[extracted]
- **Diagram encodings** — the implication-chain encoding is no larger than a separate encoding and propagates more strongly, and is a strict generalization of the MDD encoding (idx 9, chapter 1, pp. 3-11). ^[extracted]
- **Dynamic programming with diagrams** — projection and concatenation (Definitions 1 and 2) define bucket elimination, and GPU-based implementations of bucket elimination and dynamic bucket elimination report average speedups of 69.3/34.9/125.1 in the centralized and 44.7/22.3/124.2 in the distributed setting (idx 17, chapter 9, pp. 121-140). ^[inferred]
- **Diagram-based Lagrangian subproblems** — the Lagrangian decomposition of a CP program uses MDD/BDD relaxations on the constraint subproblems, propagating the Lagrangian cost through them (idx 11, chapter 3, pp. 30-38). ^[inferred]

## Related

- [[references/pesant2015-cp2015-proceedings]] — the volume these papers are drawn from
- [[concepts/bound-tightening-relaxation-networks]] — relaxation tightening in interval networks
- [[concepts/lagrangian-decomposition-propagation]] — diagram relaxations inside duality
- [[concepts/cumulative-volume-lower-bound-cp-search]] — bound computation in search

## Sources

- `_papers/pesant2015principles/pesant2015principles-extracted.md` (18,510 lines), chapters 1, 3, 9, 26 and the idx 65, 66 journal-track abstracts.
