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
  - target: "[[references/gronhaug2010-branch-and-price-lng-irp]]"
    type: related_to
sources:
  - _papers/barnhart1998branchandprice/barnhart1998branchandprice-extracted.md
  - _papers/barnhart1998branchandprice/barnhart1998branchandprice.md
  - _papers/gronhaug2010branchandprice/gronhaug2010branchandprice-extracted.md
  - _papers/gronhaug2010branchandprice/gronhaug2010branchandprice.md
summary: >-
  Exact optimization paradigm that solves huge integer programs by generating columns on demand inside branch-and-bound while preserving decomposition structure.
provenance:
  extracted: 0.88
  inferred: 0.10
  ambiguous: 0.02
base_confidence: 0.77
lifecycle: draft
lifecycle_changed: 2026-10-22
tier: core
created: 2026-10-22T20:40:00Z
updated: 2026-10-27T06:00:00Z
---

# Branch-and-Price Column Generation

Branch-and-price is an exact method for large integer programs where explicit enumeration of feasible patterns/routes/assignments is impossible.

## Key Ideas

- Start from a restricted master problem with a small column subset.
- Use pricing subproblems to generate only columns with negative reduced cost.
- Embed this inside branch-and-bound to enforce integrality.
- Choose branching rules that keep pricing subproblems valid (often branch on original variables, not generated-column variables).
- Side-constrained pricing needs custom label dominance: in the LNG-IRP branch-and-price of Grønhaug et al. (2010), route labels are comparable only at pickup/destination nodes (discrete tank unloading and duty limits make delivery-node labels incomparable), and berth constraints are relaxed in the subproblem and re-added as cuts when violated. ^[inferred]

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
- [[references/gronhaug2010-branch-and-price-lng-irp]] — time-space pricing with boil-off-coupled inventory in the master

## Open Questions

- Which branching and stabilization variants are most robust across modern benchmark families?
- How should branch-and-price hybrids be combined with matheuristics in large industrial planning pipelines? ^[inferred]

## Sources

- [[_papers/barnhart1998branchandprice/barnhart1998branchandprice-extracted.md]]
- [[_papers/barnhart1998branchandprice/barnhart1998branchandprice.md]]
- [[_papers/gronhaug2010branchandprice/gronhaug2010branchandprice-extracted.md]]
- [[_papers/gronhaug2010branchandprice/gronhaug2010branchandprice.md]]
