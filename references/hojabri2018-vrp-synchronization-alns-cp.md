---
title: ALNS + Constraint Programming for VRP with Synchronization (Hojabri et al., 2018)
category: references
tags: [paper, vrp, synchronization, alns]
relationships:
  - target: "[[concepts/vehicle-routing-with-synchronization-constraints]]"
    type: uses
  - target: "[[concepts/large-neighborhood-search]]"
    type: uses
  - target: "[[concepts/exact-multitrip-vrptw-framework]]"
    type: related_to
  - target: "[[references/paradiso2020-esf-multitrip-vrptw]]"
    type: related_to
  - target: "[[concepts/drone-swarm-synchronization]]"
    type: related_to
    note: "Reciprocal - concepts/drone-swarm-synchronization references this page."
    confidence: 0.7
    basis: observed
    since: "2026-10-30T14:38:55Z"
  - target: "[[references/ha2020-vrp-synchronization-lp-alns]]"
    type: related_to
    note: "Reciprocal - references/ha2020-vrp-synchronization-lp-alns references this page."
    confidence: 0.7
    basis: observed
    since: "2026-10-30T14:38:55Z"
sources:
  - _papers/hojabri2018large/hojabri2018large-extracted.md
  - _papers/hojabri2018large/hojabri2018large.md
  - _papers/hojabri2018large/images/page_0_image_8.jpg
  - _papers/hojabri2018large/images/page_2_image_2.jpg
summary: Presents an ALNS framework with CP-based reinsertion for VRP synchronization constraints, showing robust improvements on benchmark sets.
provenance:
  extracted: 0.88
  inferred: 0.09
  ambiguous: 0.03
base_confidence: 0.67
lifecycle: draft
lifecycle_changed: 2026-10-22
tier: core
created: 2026-10-22T10:00:17Z
updated: 2026-10-30T14:39:22Z
---

# ALNS + Constraint Programming for VRP with Synchronization (Hojabri et al., 2018)

> [!tldr] The paper combines ALNS destruction operators with CP-based reinsertion to handle synchronization-heavy VRP variants where regular and special routes must be time-coordinated.

## Problem & Scope

The studied problem (VRPMS) extends VRPTW with synchronization constraints between two route sets (regular and special vehicles).

A special service at customer \(i\) must start within a relative window around regular-service time \(t\):

\[
t - \delta \le t'_i \le t + \gamma
\]

Objective: minimize total travel distance while satisfying both standard VRPTW constraints and synchronization rules.

## Method / Architecture

The solution architecture is an ALNS metaheuristic with CP-assisted repair:

- destroy operators remove structured parts of a solution,
- CP-based reinsertion rebuilds feasible synchronized routes,
- adaptive operator scoring updates selection probabilities by segment performance,
- acceptance and neighborhood-size controls prevent search stagnation.

From the tested operator set, **route removal** and **historical node-pair removal** were retained as strongest contributors.

## Results

- Experiments were built from Solomon and Homberger-Gehring instances across sizes 25/50/100/200 and varying special-customer ratios.
- ALNS consistently improved initial solutions.
- Synchronization constraints introduced a measurable but bounded quality gap relative to corresponding VRPTW best-known references.
- Reported behavior suggests even a small number of synchronization constraints can alter route structure significantly.

## Limitations

- Absolute performance gaps vary by instance class and synchronization density.
- Detailed numeric table cells are partly difficult to recover from extracted markdown where oversized figure/table lines were truncated by tooling. ^[ambiguous]
- The objective focuses on distance; other operational criteria (e.g., service robustness) are not the primary target. ^[inferred]

## Related

- [[concepts/vehicle-routing-with-synchronization-constraints]]
- [[concepts/large-neighborhood-search]]
- [[concepts/exact-multitrip-vrptw-framework]]
- [[references/paradiso2020-esf-multitrip-vrptw]]
- [[references/gendreau2019-handbook-metaheuristics]]
- [[_papers/hojabri2018large/hojabri2018large-extracted]]

## Bibliographic Record

- Citation key: `hojabri2018large`
- DOI: `10.1016/j.cor.2017.11.011`
- Canonical URL: <https://www.sciencedirect.com/science/article/pii/S0305054817302885>
- Publication: *Computers & Operations Research* (2018)
- Authors: Hossein Hojabri; Michel Gendreau; Jean-Yves Potvin; Louis-Martin Rousseau
- Companion metadata note: [[_papers/hojabri2018large/hojabri2018large.md]]

## Sources

- [[_papers/hojabri2018large/hojabri2018large-extracted.md]]
- [[_papers/hojabri2018large/hojabri2018large.md]]
- [[_papers/hojabri2018large/images/page_0_image_8.jpg]]
- [[_papers/hojabri2018large/images/page_2_image_2.jpg]]
