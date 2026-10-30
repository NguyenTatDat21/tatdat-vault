---
title: Solving the TSPTW with Dynamic Discretization Discovery
category: references
tags: [tsptw, dynamic-discretization, exact-algorithms, time-expanded-networks]
relationships:
  - target: "[[concepts/dynamic-discretization-discovery]]"
    type: derived_from
  - target: "[[references/boland2017-continuous-time-service-network-design]]"
    type: extends
  - target: "[[references/archetti2023-branch-and-cut-sop]]"
    type: related_to
  - target: "[[concepts/large-neighborhood-ship-pair-destroy-repair]]"
    type: related_to
sources:
  - _papers/boland2017solving/boland2017solving-extracted.md
  - _papers/boland2017solving/boland2017solving.md
summary: >-
  Presents Dynamic Discretization Discovery for TSPTW, iteratively refining only needed departure times and solving many benchmark instances to optimality with much smaller networks.
provenance:
  extracted: 0.9
  inferred: 0.08
  ambiguous: 0.02
base_confidence: 0.67
lifecycle: draft
lifecycle_changed: 2026-10-22
tier: supporting
created: 2026-10-22T21:08:00Z
updated: 2026-10-30T14:38:55Z
---

# Solving the TSPTW with Dynamic Discretization Discovery

> [!tldr] DDD solves the TSP with time windows by repeatedly solving a compact partially time-expanded model and refining only where timing infeasibility appears.

## Problem & Motivation

A full discretization of time windows can make TSPTW models too large, but coarse discretization can miss optimal paths. The paper targets exact solution quality while controlling model size through adaptive time-point generation.

## Method / Architecture
## Bibliographic Record

- Publication: Conference paper, Springer, 2017-06 (LNCS series; exact volume not recorded in the Zotero metadata)
- Authors: Natashia Boland; Mike Hewitt; Martin Savelsbergh; Vu Duc Minh
- DOI: 10.1007/978-3-319-59776-8_21
- Implementation: C++ with Gurobi 6.5.0 (single thread), Intel Xeon E5-4610 v2 2.30 GHz, Ubuntu 14.04.3
- Companion metadata note: [[_papers/boland2017solving/boland2017solving.md]]


Dynamic Discretization Discovery alternates between optimization and targeted time expansion:

1. Build an initial small partially time-expanded network.
2. Solve a mixed-integer model over this network.
3. Detect arcs that need additional departure-time resolution.
4. Apply `LENGTHEN-ARC` and add only necessary time points.
5. Repeat until no violating arc remains.

## Key Equations

Time-expanded objective:

$$
\min \sum_{a \in \mathcal{A}} c_a\, x_a
$$

Flow conservation over expanded nodes:

$$
\sum_{a \in \delta^-((i,t))} x_a - \sum_{a \in \delta^+((i,t))} x_a = 0 \quad \forall (i,t) \in \mathcal{N},\ i \neq 0
$$

Each customer visited once:

$$
\sum_{a = ((i,t),(j,t')) \in \mathcal{A}} x_a = 1 \quad \forall i \in N, \qquad x_a \in \{0,1\} \ \forall a \in \mathcal{A}
$$

## Results

| Benchmark view | Result |
|---|---|
| Overall solve quality | 313/337 instances solved to target quality |
| Competitiveness | 329 instances at or better than then-best known values |
| New bests | 41 improved best-known solutions in SU class |
| Model size | Large reductions versus fully expanded networks on hard classes |

## Limitations

- Most evidence is from standard benchmark families; transfer to other temporal-routing structures may require tuning. ^[inferred]
- Benefits depend on refinement trigger design and solver behavior on each class.

## Related

- [[concepts/dynamic-discretization-discovery]]
- [[references/boland2017-continuous-time-service-network-design]]
- [[references/archetti2023-branch-and-cut-sop]]
- [[concepts/set-orienteering-problem]]

## Sources

- [[_papers/boland2017solving/boland2017solving-extracted.md]]
- [[_papers/boland2017solving/boland2017solving.md]]
