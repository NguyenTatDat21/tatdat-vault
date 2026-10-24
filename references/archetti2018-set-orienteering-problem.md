---
title: >-
  The Set Orienteering Problem
category: references
tags: [orienteering, routing, matheuristic, mixed-integer-programming]
relationships:
  - target: "[[concepts/set-orienteering-problem]]"
    type: derived_from
  - target: "[[references/lu2024-hybrid-evolutionary-algorithm-sop]]"
    type: related_to
  - target: "[[concepts/tabu-search]]"
    type: uses
sources:
  - _papers/archetti2018set/archetti2018set-extracted.md
  - _papers/archetti2018set/archetti2018set.md
summary: >-
  Foundational SOP formulation and matheuristic for maximizing cluster profit under route-duration limits, with strong solution quality on large benchmark instances.
provenance:
  extracted: 0.90
  inferred: 0.08
  ambiguous: 0.02
base_confidence: 0.67
lifecycle: draft
lifecycle_changed: 2026-10-22
tier: supporting
created: 2026-10-22T19:23:44Z
updated: 2026-10-22T19:23:44Z
---

# The Set Orienteering Problem

> [!tldr] Defines SOP as cluster-profit routing with a time budget and proposes a robust matheuristic that scales to large benchmarks.

## Problem & Motivation

SOP generalizes the Orienteering Problem by assigning profit to clusters instead of individual customers. Profit is collected if at least one node of a cluster is visited, under a route-duration limit.

## Method / Architecture
## Bibliographic Record

- Publication: *European Journal of Operational Research*, 2018 (issue: May 2018; volume/pages not recorded in the Zotero metadata)
- Authors: Claudia Archetti; Francesco Carrabs; Raffaele Cerulli
- DOI: 10.1016/j.ejor.2017.11.009
- Companion metadata note: [[_papers/archetti2018set/archetti2018set.md]]


The paper combines:
- an exact MIP formulation for SOP,
- a greedy randomized construction,
- a greedy construction heuristic,
- a MIP-based neighborhood move (MIPMove) inside a matheuristic loop.

```mermaid
flowchart LR
  A[Clustered customers + profits] --> B[SOP MIP model]
  B --> C[Greedy initialization]
  C --> D[Tabu search refinement]
  D --> E[MIPMove neighborhood optimization]
  E --> F[Best feasible route under T_max]
```

Flow is reconstructed from the algorithm description. ^[inferred]

## Key Equations

$$
\max \sum_{g \in \mathcal{P}} p_g z_g
$$

$$
\sum_{(i,j)\in\delta^{+}(i)} x_{ij} = y_i \qquad i \in V
$$

$$
\sum_{(i,j)\in A} c_{ij}x_{ij} \leq T_{\max}
$$

## Results

| Setting | Result |
|---|---|
| Benchmark family | Instances derived from GTSP benchmarks |
| Largest size noted | Up to 1084 vertices |
| Performance takeaway | Matheuristic produced robust, high-quality solutions with short compute times |

## Limitations

- Focus is single-vehicle SOP; multi-vehicle and richer operational constraints need extensions.
- Performance claims emphasize benchmark behavior; sensitivity to cluster-generation quality is not exhaustively isolated. ^[inferred]

## Related

- [[concepts/set-orienteering-problem]]
- [[references/lu2024-hybrid-evolutionary-algorithm-sop]]
- [[concepts/tabu-search]]
- [[concepts/hyper-heuristics]]

## Sources

- [[_papers/archetti2018set/archetti2018set-extracted.md]]
- [[_papers/archetti2018set/archetti2018set.md]]
