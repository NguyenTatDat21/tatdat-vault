---
title: Periodic Scheduling Under Capacity Constraints
category: concepts
tags: [periodic-scheduling, operations-research, approximation-algorithms, fairness]
relationships:
  - target: "[[references/bar-noy2002-minimizing-periodic-scheduling-costs]]"
    type: derived_from
  - target: "[[references/bar-noy2004-efficient-algorithms-periodic-scheduling]]"
    type: derived_from
  - target: "[[concepts/set-orienteering-problem]]"
    type: related_to
  - target: "[[concepts/set-team-orienteering-problem-with-time-windows]]"
    type: related_to
  - target: "[[concepts/leximax-leximin-fairness-principles]]"
    type: related_to
sources:
  - _papers/bar-noy2002minimizing/bar-noy2002minimizing-extracted.md
  - _papers/bar-noy2002minimizing/bar-noy2002minimizing.md
  - _papers/bar-noy2004efficient/bar-noy2004efficient-extracted.md
  - _papers/bar-noy2004efficient/bar-noy2004efficient.md
summary: >-
  Family of periodic service-allocation models with per-slot capacity limits, balancing fairness or cost via exact tree constructions and approximation guarantees.
provenance:
  extracted: 0.84
  inferred: 0.13
  ambiguous: 0.03
base_confidence: 0.83
lifecycle: draft
lifecycle_changed: 2026-10-22
tier: supporting
created: 2026-10-22T19:33:55Z
updated: 2026-10-22T19:33:55Z
---

# Periodic Scheduling Under Capacity Constraints

Periodic scheduling asks how to assign recurring service slots when only limited service capacity is available at each time step.

## Key Ideas

- Demand is represented as desired service frequencies across items/clients.
- Capacity constraints limit how many services can be assigned per slot.
- Objective functions typically trade service quality ([[concepts/leximax-leximin-fairness-principles|fairness]] or delay) against operational/service cost.
- Perfect periodicity (exact regular spacing) improves predictability but increases combinatorial difficulty.

## Canonical Algorithmic Patterns

- **Relax-and-round:** solve nonlinear/continuous relaxations, then construct feasible periodic schedules.
- **Tree scheduling:** build hierarchical round-robin structures to approximate requested frequencies.
- **Bounded approximations:** use structural insights (e.g., sequence constructions) to provide worst-case guarantees.

## Related

- [[references/bar-noy2002-minimizing-periodic-scheduling-costs]]
- [[references/bar-noy2004-efficient-algorithms-periodic-scheduling]]
- [[concepts/set-orienteering-problem]]
- [[concepts/set-team-orienteering-problem-with-time-windows]]

## Open Questions

- When does strict periodicity outperform adaptive non-periodic scheduling in real workloads?
- Which approximation strategies remain robust under nonstationary demand and multi-resource constraints? ^[inferred]

## Sources

- [[_papers/bar-noy2002minimizing/bar-noy2002minimizing-extracted.md]]
- [[_papers/bar-noy2002minimizing/bar-noy2002minimizing.md]]
- [[_papers/bar-noy2004efficient/bar-noy2004efficient-extracted.md]]
- [[_papers/bar-noy2004efficient/bar-noy2004efficient.md]]
