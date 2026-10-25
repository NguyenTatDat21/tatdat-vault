---
title: >-
  Exact Multitrip VRPTW Framework
category: concepts
tags: [vehicle-routing, exact-methods, time-windows, branch-and-cut]
relationships:
  - target: "[[references/paradiso2020-esf-multitrip-vrptw]]"
    type: derived_from
  - target: "[[references/poikonen2020-k-mvdrp]]"
    type: related_to
  - target: "[[references/tamke2023-vrpd-dss]]"
    type: related_to
sources:
  - _papers/paradiso2020exact/paradiso2020exact-extracted.md
  - _papers/paradiso2020exact/paradiso2020exact.md
summary: >-
  A structure-based exact framework for capacitated multitrip VRPs with time windows that combines lower bounds and branch-and-cut to scale better than earlier exact approaches.
provenance:
  extracted: 0.81
  inferred: 0.16
  ambiguous: 0.03
base_confidence: 0.67
lifecycle: draft
lifecycle_changed: 2026-10-22
tier: supporting
created: 2026-10-22T09:15:49Z
updated: 2026-10-25T03:40:00Z
---

# Exact Multitrip VRPTW Framework

The ESF pattern solves multitrip VRPs with time windows by modeling route **structures** first, then optimizing over a reduced structure set with strong cuts.

## Key Ideas

- Build an exact formulation around route structures, not only classical trip/journey indexing.
- Use lower bounds early to prune weak structures (`P1` CVRPTW-based and `P2` relaxed-structure based).
- Inject subset-row inequalities and branch-and-cut logic on the reduced model.

![[_papers/paradiso2020exact/images/page_9_image_13.jpg]]
*Figure 1 (paper): "Example of a Support Graph with Six Structures" — structures are the nodes of a support graph; arcs encode time-compatible structure sequencing.*
- Reuse the framework across closely related variants (loading durations, release dates, DRP adaptation) with limited redesign.

This architecture shifts effort from pure monolithic MIP solving toward a decomposition-like pipeline that controls combinatorial growth in larger instances. ^[inferred]

Related pages: [[references/paradiso2020-esf-multitrip-vrptw]], [[references/poikonen2020-k-mvdrp]], [[references/tamke2023-vrpd-dss]], [[references/gendreau2019-handbook-metaheuristics]], [[_papers/boland2017solving/boland2017solving-extracted]].

## Open Questions

- Which structure-generation heuristics preserve exactness while further reducing branch-and-cut runtime on larger release-date sets?
- Can this framework be merged with uncertainty-aware planning layers without losing tractable exact bounds? ^[inferred]

## Sources

- [[_papers/paradiso2020exact/paradiso2020exact-extracted.md]]
- [[_papers/paradiso2020exact/paradiso2020exact.md]]
- [[_papers/paradiso2020exact/images/page_9_image_13.jpg]]
