---
title: "Green vehicle routing problem: A state-of-the-art review"
category: references
tags: [green-logistics, vehicle-routing, systematic-review, sustainability]
relationships:
  - target: "[[concepts/green-vehicle-routing-problem-taxonomy]]"
    type: derived_from
  - target: "[[concepts/vehicle-routing-with-synchronization-constraints]]"
    type: related_to
  - target: "[[concepts/hyper-heuristics]]"
    type: related_to
  - target: "[[concepts/multi-objective-metaheuristic-tuning-validation]]"
    type: related_to
    note: "Reciprocal - concepts/multi-objective-metaheuristic-tuning-validation references this page."
    confidence: 0.7
    basis: observed
    since: "2026-10-30T14:38:55Z"
  - target: "[[references/ganjia2026-multiobjective-sustainable-supply-chain-scheduling]]"
    type: related_to
    note: "Reciprocal - references/ganjia2026-multiobjective-sustainable-supply-chain-scheduling references this page."
    confidence: 0.7
    basis: observed
    since: "2026-10-30T14:38:55Z"
sources:
  - _papers/asghari2021green/asghari2021green-extracted.md
  - _papers/asghari2021green/asghari2021green.md
summary: >-
  Systematic review of Green-VRP literature (2000–2020) that organizes ICEV, AFV, and HEV streams into a unified taxonomy of models, objectives, and methods.
provenance:
  extracted: 0.90
  inferred: 0.08
  ambiguous: 0.02
base_confidence: 0.67
lifecycle: draft
lifecycle_changed: 2026-10-22
tier: core
created: 2026-10-22T19:33:55Z
updated: 2026-10-30T14:39:22Z
---

# Green vehicle routing problem: A state-of-the-art review

> [!tldr] Consolidates Green-VRP variants into a practical map of vehicle technologies, objective functions, uncertainty settings, and solution strategies.

## Problem & Motivation

Green-VRP studies were spread across multiple sub-communities (combustion, alternative-fuel, and hybrid fleets), making it hard to compare assumptions and methods. This review provides one structured synthesis.

## Method / Architecture

The review builds a taxonomy over problem variants, objective sets, operating scenarios, and optimization methods.

```mermaid
flowchart TD
  A[Green-VRP literature] --> B[Vehicle stream: ICEV / AFV / HEV]
  B --> C[Modeling assumptions]
  C --> D[Objectives and constraints]
  D --> E[Method class: exact / heuristic / metaheuristic]
  E --> F[Research gaps and future directions]
```

## Key Quantitative Anchors

| Anchor | Value |
|---|---|
| Review window | 2000–2020 |
| Papers analyzed | 313 |
| Main streams | ICEV, AFV, HEV |
| Output | Taxonomy + analytical tables + gap map |

## Results

| Theme | Takeaway |
|---|---|
| Coverage | Presents a broad and structured synthesis across major Green-VRP variants |
| Modeling | Highlights how energy/fuel assumptions change constraints and objectives |
| Methods | Contrasts exact, heuristic, and metaheuristic usage across streams |
| Future work | Identifies gaps where variant integration is still limited |

## Limitations

- As a review paper, it does not benchmark a new algorithmic solver directly.
- The taxonomy reflects evidence available through 2020; later growth areas may shift priorities. ^[inferred]

## Related

- [[concepts/green-vehicle-routing-problem-taxonomy]]
- [[concepts/vehicle-routing-with-synchronization-constraints]]
- [[concepts/hyper-heuristics]]
- [[concepts/large-neighborhood-search]]

## Sources

- [[_papers/asghari2021green/asghari2021green-extracted.md]]
- [[_papers/asghari2021green/asghari2021green.md]]
