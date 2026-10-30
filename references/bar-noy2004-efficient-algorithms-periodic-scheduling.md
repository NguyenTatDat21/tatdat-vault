---
title: Efficient algorithms for periodic scheduling
category: references
tags: [periodic-scheduling, fairness, approximation-algorithms, networking]
relationships:
  - target: "[[concepts/periodic-scheduling-under-capacity-constraints]]"
    type: derived_from
  - target: "[[references/bar-noy2002-minimizing-periodic-scheduling-costs]]"
    type: extends
  - target: "[[concepts/set-team-orienteering-problem-with-time-windows]]"
    type: related_to
  - target: "[[references/richards1996-scheduling-to-maximize-customer-satisfaction]]"
    type: related_to
  - target: "[[references/ogryczak2014-fair-optimization-networks-survey]]"
    type: related_to
    note: "Reciprocal - references/ogryczak2014-fair-optimization-networks-survey references this page."
    confidence: 0.7
    basis: observed
    since: "2026-10-30T14:38:55Z"
sources:
  - _papers/bar-noy2004efficient/bar-noy2004efficient-extracted.md
  - _papers/bar-noy2004efficient/bar-noy2004efficient.md
summary: >-
  Studies perfectly periodic scheduling under fairness objectives, proving NP-hardness and combining optimal exponential methods with practical tree-scheduling heuristics.
provenance:
  extracted: 0.90
  inferred: 0.08
  ambiguous: 0.02
base_confidence: 0.67
lifecycle: draft
lifecycle_changed: 2026-10-22
tier: core
created: 2026-10-22T19:33:55Z
updated: 2026-10-30T14:38:55Z
---

# Efficient algorithms for periodic scheduling

> [!tldr] Formalizes perfectly periodic scheduling quality by MAX and AVE criteria, then designs exact and heuristic tree-based algorithms under NP-hardness.

## Problem & Motivation

Given requested service frequencies, build perfectly periodic schedules where each client is served at exact regular intervals while keeping mismatch between requested and allocated frequency small.

## Method / Architecture

The paper uses tree scheduling (hierarchical round-robin) and analyzes both exact optimization and efficient heuristics for two objective families.

```mermaid
flowchart LR
  A[Requested frequencies] --> B[Scheduling tree design]
  B --> C[MAX objective]
  B --> D[AVE objective]
  C --> E[Exact exponential algorithm]
  D --> F[Exact exponential algorithm]
  B --> G[Polynomial heuristics]
```

## Key Equations

$$
\text{ratio}_i = \frac{a_i}{b_i}
$$

$$
\text{MAX} = \max_i \left\{ \frac{a_i}{b_i} \right\} \ \text{(unweighted)}, \qquad
\text{AVE} = \sum_i a_i \cdot \frac{a_i}{b_i} = \sum_i \frac{a_i^2}{b_i} \ \text{(weighted by requested share)}
$$

## Results

| Result type | Reported finding |
|---|---|
| Complexity | Optimal perfectly periodic schedule is NP-hard |
| Exact methods | Exponential-time optimum algorithms for MAX and AVE |
| Practical methods | Tree-based heuristics run efficiently and perform strongly in simulations |
| Empirical note | Some heuristics can outperform prior non-perfectly-periodic baselines |

## Limitations

- Perfect periodicity may be too restrictive for bursty or nonstationary demand settings. ^[inferred]
- Evaluation focuses on studied traffic/request models and may not transfer unchanged to all workloads. ^[inferred]

## Related

- [[concepts/periodic-scheduling-under-capacity-constraints]]
- [[references/bar-noy2002-minimizing-periodic-scheduling-costs]]
- [[references/richards1996-scheduling-to-maximize-customer-satisfaction]] — periodic weekly assignment with per-slot minimum and maximum capacity, solved exactly as a capacitated transportation problem.
- [[concepts/set-team-orienteering-problem-with-time-windows]]

## Bibliographic Record

- Citation key: bar-noy2004efficient
- DOI: `10.1016/j.comnet.2003.12.017`
- Canonical URL: <https://www.sciencedirect.com/science/article/pii/S1389128604000052>
- Publication: *Computer Networks*, 2004-06-05
- Authors: Amotz Bar-Noy; Vladimir Dreizin; Boaz Patt-Shamir
- Companion metadata note: [[_papers/bar-noy2004efficient/bar-noy2004efficient.md]]

## Sources

- [[_papers/bar-noy2004efficient/bar-noy2004efficient-extracted.md]]
- [[_papers/bar-noy2004efficient/bar-noy2004efficient.md]]
