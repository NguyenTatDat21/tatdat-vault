---
title: >-
  Parallel Metaheuristics and Cooperative Search
category: concepts
tags: [metaheuristics, optimization]
relationships:
  - target: "[[concepts/tabu-search]]"
    type: related_to
  - target: "[[concepts/variable-neighborhood-search]]"
    type: related_to
  - target: "[[concepts/large-neighborhood-search]]"
    type: related_to
  - target: "[[references/gendreau2019-handbook-metaheuristics]]"
    type: derived_from
  - target: "[[concepts/search-combinators-meta-search]]"
    type: related_to
  - target: "[[concepts/hyper-heuristics]]"
    type: related_to
  - target: "[[concepts/metaheuristic-hybridization]]"
    type: related_to
  - target: "[[concepts/multi-objective-metaheuristic-tuning-validation]]"
    type: related_to
  - target: "[[concepts/swarm-intelligence-pso-aco]]"
    type: related_to
sources:
  - _papers/gendreau2019handbook/gendreau2019handbook-extracted.md
summary: >-
  Parallel metaheuristics run multiple search processes; cooperative variants exchange information to improve robustness and solution quality over independent runs.
provenance:
  extracted: 0.77
  inferred: 0.2
  ambiguous: 0.03
base_confidence: 0.67
lifecycle: draft
lifecycle_changed: 2026-10-22
tier: core
created: 2026-10-22T08:35:02Z
updated: 2026-10-30T17:41:00Z
---

# Parallel Metaheuristics and Cooperative Search

Parallel metaheuristics use multiple concurrent search trajectories. The chapter emphasizes two goals: solve larger/harder instances faster and improve reliability of final solutions.

## Key Ideas

- Independent multi-search gives speedup but often leaves quality gains on the table.
- Cooperative search exchanges search information (incumbents, elite components, memory structures) between processes.
- Effective design depends on communication policy (what, when, and how much to exchange).
- The chapter classifies designs by control cardinality, communication/control structure, and process differentiation.
- Asynchronous exchange often helps reduce idle time and preserves throughput on heterogeneous workloads. ^[inferred]

A practical warning is to preserve diversity: too-frequent or too-strong sharing can make all workers converge to similar regions too early.

Related pages: [[concepts/tabu-search]], [[concepts/variable-neighborhood-search]], [[concepts/large-neighborhood-search]], [[concepts/hyper-heuristics]], and [[references/gendreau2019-handbook-metaheuristics]].

## Open Questions

- Which cooperation policy works best for mixed move spaces that combine routing arcs and drone-assignment decisions?
- How should communication frequency adapt to search-stage signals (early exploration vs late intensification)? ^[inferred]

## Sources

- [[_papers/gendreau2019handbook/gendreau2019handbook-extracted.md]]

## Related

- [[concepts/search-combinators-meta-search]] — shares search + metaheuristic tags with this page
