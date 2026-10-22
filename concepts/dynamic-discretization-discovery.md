---
title: Dynamic Discretization Discovery
category: concepts
tags: [exact-optimization, time-expanded-network, adaptive-discretization, routing]
relationships:
  - target: "[[references/boland2017-dynamic-discretization-tsptw]]"
    type: derived_from
  - target: "[[references/boland2017-continuous-time-service-network-design]]"
    type: extends
  - target: "[[concepts/branch-and-price-column-generation]]"
    type: related_to
sources:
  - _papers/boland2017solving/boland2017solving-extracted.md
  - _papers/boland2017solving/boland2017solving.md
  - _papers/boland2017continuoustime/boland2017continuoustime-extracted.md
  - _papers/boland2017continuoustime/boland2017continuoustime.md
summary: >-
  Exact optimization strategy that starts with coarse time discretization and iteratively adds only the time points needed to recover continuous-time feasibility and optimality.
provenance:
  extracted: 0.88
  inferred: 0.1
  ambiguous: 0.02
base_confidence: 0.83
lifecycle: draft
lifecycle_changed: 2026-10-22
tier: supporting
created: 2026-10-22T21:16:00Z
updated: 2026-10-22T21:16:00Z
---

# Dynamic Discretization Discovery

Dynamic Discretization Discovery (DDD) is an exact method for time-dependent network optimization that avoids full time expansion.

## Key Ideas

- Build a small partially time-expanded network.
- Solve the current MIP exactly on that network.
- Detect where timing resolution is insufficient.
- Add only targeted time points/arcs and repeat.
- Stop when no timing infeasibility remains; current solution is then exact for the continuous-time model.

## Why It Matters

- Controls combinatorial growth from naive minute-level discretization.
- Preserves exact-solution guarantees unlike purely heuristic coarsening.
- Transfers across multiple routing/service-network formulations with time windows. ^[inferred]

## Related

- [[references/boland2017-dynamic-discretization-tsptw]]
- [[references/boland2017-continuous-time-service-network-design]]
- [[concepts/branch-and-price-column-generation]]
- [[concepts/set-orienteering-problem]]

## Open Questions

- Which refinement triggers give best runtime-quality trade-offs across problem families?
- Can DDD be combined with stronger cuts or decomposition layers without losing practical speedups? ^[inferred]

## Sources

- [[_papers/boland2017solving/boland2017solving-extracted.md]]
- [[_papers/boland2017solving/boland2017solving.md]]
- [[_papers/boland2017continuoustime/boland2017continuoustime-extracted.md]]
- [[_papers/boland2017continuoustime/boland2017continuoustime.md]]
