---
title: "Branch-and-Price: Column Generation for Solving Huge Integer Programs"
category: references
tags: [integer-programming, column-generation, branch-and-price, decomposition]
relationships:
  - target: "[[concepts/branch-and-price-column-generation]]"
    type: derived_from
  - target: "[[references/archetti2023-branch-and-cut-sop]]"
    type: related_to
  - target: "[[concepts/exact-multitrip-vrptw-framework]]"
    type: related_to
  - target: "[[references/boland2017-continuous-time-service-network-design]]"
    type: related_to
  - target: "[[concepts/four-stage-guillotine-cut-bounded-knapsack]]"
    type: related_to
  - target: "[[references/clautiaux2018-hypergraph-guillotine-knapsack]]"
    type: related_to
  - target: "[[references/furini2016-two-dimensional-guillotine-cutting-ip]]"
    type: related_to
  - target: "[[references/gronhaug2010-branch-and-price-lng-irp]]"
    type: related_to
  - target: "[[references/ogryczak2014-fair-optimization-networks-survey]]"
    type: related_to
sources:
  - _papers/barnhart1998branchandprice/barnhart1998branchandprice-extracted.md
  - _papers/barnhart1998branchandprice/barnhart1998branchandprice.md
summary: >-
  Canonical branch-and-price framework that embeds column generation inside branch-and-bound to solve massive set-partitioning and assignment models with stronger LP bounds.
provenance:
  extracted: 0.90
  inferred: 0.08
  ambiguous: 0.02
base_confidence: 0.67
lifecycle: draft
lifecycle_changed: 2026-10-22
tier: core
created: 2026-10-22T20:40:00Z
updated: 2026-10-30T14:38:55Z
---

# Branch-and-Price: Column Generation for Solving Huge Integer Programs

> [!tldr] Branch-and-price solves huge integer programs by generating variables on demand and branching in a way that preserves pricing structure.

## Problem & Motivation

Large-scale integer programs in scheduling, assignment, and routing often have too many feasible columns to enumerate up front. The paper formalizes a practical way to combine decomposition and exact search so these models remain solvable.

## Bibliographic Record

- Publication: *Operations Research*, Vol. 46, No. 3, pp. 316–334, June 1998
- Authors: Cynthia Barnhart; Ellis L. Johnson; George L. Nemhauser; Martin W. P. Savelsbergh; Pamela H. Vance
- DOI: 10.1287/opre.46.3.316
- Companion metadata note: [[_papers/barnhart1998branchandprice/barnhart1998branchandprice.md]]

## Method / Architecture

Branch-and-price combines:
1. A **restricted master problem** with only a subset of columns,
2. A **pricing subproblem** that finds improving columns,
3. A **branch-and-bound tree** that enforces integrality while keeping pricing tractable.

```mermaid
flowchart LR
  A[Original huge IP] --> B[Dantzig-Wolfe master]
  B --> C[Restricted master LP]
  C --> D[Dual prices]
  D --> E[Pricing subproblem]
  E -->|negative reduced-cost column| C
  C --> F[Branching rule on original variables]
  F --> C
  C --> G[Integer-feasible solution / bound]
```

## Key Equations

$$
\min \sum_{j \in \Omega} c_j \lambda_j
$$

$$
\sum_{j \in \Omega} a_{ij}\lambda_j = 1 \quad \forall i, \qquad \lambda_j \in \{0,1\}
$$

Pricing uses reduced cost from master duals; add column $j$ when:

$$
\bar c_j = c_j - \sum_i \pi_i a_{ij} < 0
$$

## Results

| Setting | Result |
|---|---|
| Generalized assignment and crew scheduling style models | Column generation avoids full-variable enumeration and scales to much larger formulations |
| LP bound quality | Stronger relaxations than many compact formulations |
| Search behavior | Effective only with branching choices that preserve pricing structure |

## Limitations

- Performance depends heavily on subproblem structure and separation/branching engineering.
- Branching directly on generated-column variables can break decomposition and is usually avoided.
- Degeneracy and tailing-off in column generation remain practical pain points. ^[inferred]

## Related

- [[concepts/branch-and-price-column-generation]]
- [[references/boland2017-continuous-time-service-network-design]]
- [[references/archetti2023-branch-and-cut-sop]]
- [[concepts/exact-multitrip-vrptw-framework]]
- [[concepts/adaptive-large-neighborhood-search-for-mip]]

## Sources

- [[_papers/barnhart1998branchandprice/barnhart1998branchandprice-extracted.md]]
- [[_papers/barnhart1998branchandprice/barnhart1998branchandprice.md]]
