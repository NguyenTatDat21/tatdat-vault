---
title: Branch-and-Price Column Generation
category: concepts
tags: [integer-programming, decomposition, column-generation, exact-methods]
relationships:
  - target: "[[references/barnhart1998-branch-and-price-column-generation]]"
    type: derived_from
  - target: "[[references/archetti2023-branch-and-cut-sop]]"
    type: related_to
  - target: "[[concepts/exact-multitrip-vrptw-framework]]"
    type: related_to
  - target: "[[references/boland2017-continuous-time-service-network-design]]"
    type: related_to
sources:
  - _papers/barnhart1998branchandprice/barnhart1998branchandprice-extracted.md
  - _papers/barnhart1998branchandprice/barnhart1998branchandprice.md
summary: >-
  Exact optimization paradigm that solves huge integer programs by generating columns on demand inside branch-and-bound while preserving decomposition structure.
provenance:
  extracted: 0.88
  inferred: 0.10
  ambiguous: 0.02
base_confidence: 0.67
lifecycle: draft
lifecycle_changed: 2026-10-22
tier: supporting
created: 2026-10-22T20:40:00Z
updated: 2026-10-22T20:40:00Z
---

# Branch-and-Price Column Generation

Branch-and-price is an exact method for large integer programs where explicit enumeration of feasible patterns/routes/assignments is impossible.

## Key Ideas

- Start from a restricted master problem with a small column subset.
- Use pricing subproblems to generate only columns with negative reduced cost.
- Embed this inside branch-and-bound to enforce integrality.
- Choose branching rules that keep pricing subproblems valid (often branch on original variables, not generated-column variables).

## Why It Matters

- Makes exact methods practical on models with huge implicit variable spaces.
- Often yields stronger bounds than compact formulations.
- Supports reusable decomposition templates across routing, scheduling, and assignment families.

## Related

- [[references/barnhart1998-branch-and-price-column-generation]]
- [[references/boland2017-continuous-time-service-network-design]]
- [[references/archetti2023-branch-and-cut-sop]]
- [[concepts/exact-multitrip-vrptw-framework]]
- [[concepts/adaptive-large-neighborhood-search-for-mip]]

## Open Questions

- Which branching and stabilization variants are most robust across modern benchmark families?
- How should branch-and-price hybrids be combined with matheuristics in large industrial planning pipelines? ^[inferred]

## Sources

- [[_papers/barnhart1998branchandprice/barnhart1998branchandprice-extracted.md]]
- [[_papers/barnhart1998branchandprice/barnhart1998branchandprice.md]]
