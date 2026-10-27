---
title: Combining Heuristics and Constraint Programming for the Parallel Drone Scheduling Vehicle Routing Problem with Collective Drones (Montemanni et al., 2024)
category: references
tags:
  - paper
  - vrp
  - drones
  - constraint-programming
relationships:
  - target: "[[concepts/pdsvrp-c]]"
    type: uses
  - target: "[[concepts/cp-sat-hint-start]]"
    type: implements
  - target: "[[concepts/collective-drone-delivery]]"
    type: related_to
sources:
  - _papers/montemanni2024combining/montemanni2024combining-extracted.md
  - _papers/montemanni2024combining/montemanni2024combining.md
  - _papers/montemanni2024combining/images/page_52_image_8.jpg
  - _papers/montemanni2024combining/images/page_53_image_3.jpg
  - _papers/montemanni2024combining/images/page_54_image_2.jpg
  - _papers/montemanni2024combining/images/page_54_image_5.jpg
  - _papers/montemanni2024combining/images/page_102_image_3.jpg
  - _papers/montemanni2024combining/images/page_105_table_3.jpg
  - _papers/montemanni2024combining/images/page_105_table_5.jpg
  - _papers/montemanni2024combining/images/page_111_image_10.jpg
  - _papers/montemanni2024combining/images/page_112_image_10.jpg
  - _papers/montemanni2024combining/images/page_112_image_12.jpg
  - _papers/montemanni2024combining/images/page_112_image_13.jpg
  - _papers/montemanni2024combining/images/page_112_image_16.jpg
  - _papers/montemanni2024combining/images/page_112_image_2.jpg
  - _papers/montemanni2024combining/images/page_112_image_4.jpg
  - _papers/montemanni2024combining/images/page_112_image_5.jpg
  - _papers/montemanni2024combining/images/page_112_image_8.jpg
  - _papers/montemanni2024combining/images/page_112_table_23.jpg
  - _papers/montemanni2024combining/images/page_113_equation_8.jpg
  - _papers/montemanni2024combining/images/page_113_table_11.jpg
  - _papers/montemanni2024combining/images/page_119_equation_4.jpg
  - _papers/montemanni2024combining/images/page_121_table_4.jpg
  - _papers/montemanni2024combining/images/page_122_table_3.jpg
  - _papers/montemanni2024combining/images/page_128_chart_6.jpg
  - _papers/montemanni2024combining/images/page_129_chart_2.jpg
summary: "Deep-dive notes on Montemanni et al. (2024): CP-SAT models for PDSVRP-c and why truck-only VRP hint-start improves bounds and solution quality."
provenance:
  extracted: 0.8
  inferred: 0.18
  ambiguous: 0.02
base_confidence: 0.67
lifecycle: draft
lifecycle_changed: 2026-10-22
tier: core
created: 2026-10-22T08:07:13Z
updated: 2026-10-22T19:01:44Z
---

# Combining Heuristics and Constraint Programming for the Parallel Drone Scheduling Vehicle Routing Problem with Collective Drones

> [!tldr] The paper shows that seeding CP-SAT with a truck-only min-max VRP solution improves bounds and heuristic outcomes for PDSVRP-c, with collaborative drones yielding about 10% average time savings versus truck-only routing.

## Bibliographic Record

- Citation key: `montemanni2024combining`
- DOI: `10.1007/978-3-031-62912-9_13`
- URL: <https://link.springer.com/10.1007/978-3-031-62912-9_13>
- Publication record: *Metaheuristics* (2024)
- Zotero creators listed in the source note: Roberto Montemanni, Mauro Dell’Amico, Andrea Corsini, Marc Sevaux, Alexandru-Liviu Olteanu, Eduardo G. Pardo, Angelo Sifaleras, Salma Makboul
- Companion metadata note: [[_papers/montemanni2024combining/montemanni2024combining.md]]
## Problem & Motivation

The paper studies last-mile delivery where multiple trucks and multiple drones cooperate in parallel. Some customers can be served by one truck tour, some by drone missions, and some by coordinated (collective) drone groups.

Without drones, the problem collapses to a min-max vehicle routing problem. The authors test whether this simpler truck-only solution can be used as a strong starting hint for harder CP models.

## Method / Architecture

Two CP-SAT models from prior work are reused:
- **M2**: giant-tour style truck variables plus drone assignment/synchronization variables.
- **M3**: truck-indexed routing variables and per-truck circuit constraints.

Hint-start strategy:
1. Solve a truck-only min-max VRP heuristic first.
2. Inject that solution as partial variable hints in CP-SAT.
3. Let CP-SAT reassign suitable customers to drones and refine schedules.

```mermaid
flowchart LR
  A[Truck-only min-max VRP solution] --> B[Hint-start values passed to CP-SAT]
  B --> C[M2 and M3 CP-SAT models]
  C --> D[Reassign customers to collaborative drone missions]
  D --> E[Improved lower/upper bounds within the same time budget]
```
*Hint-start flow reconstructed from the text. ^[inferred]*

## Key Equations

Core objective (both models):

$$
\min \alpha
$$

where \(\alpha\) is the makespan and must dominate truck and drone completion times.

A useful reading of the objective is:

$$
\alpha \geq \max\{T_{\text{truck}}, T_{\text{drone}}\}
$$

(Conceptual restatement for interpretation. ^[inferred])

## Results

Implementation and setup reported in the paper:
- Python 3.11.2 + Google OR-Tools CP-SAT 9.6
- Intel i7-12700F, 32 GB RAM
- 1-hour limit per instance
- Benchmarks with 50–200 customers, 5–10 drones, and 2–5 trucks

Headline table slices (average row shown in the paper):

| Setting | Truck-only VRP UB | Best hint-start bound reported | Practical reading |
|---|---:|---|---|
| 2 trucks | 131.5 | [68.6, 117.2] | Better LB and better UB than truck-only baseline |
| 3 trucks | 99.7 | [51.1, 92.7] | Same pattern; hint-start improves final quality |

The paper concludes that hint-start is beneficial for both lower bounds and heuristic solutions, and that collaborative drones provide around 10% average time savings versus truck-only routing.

## Limitations

- The authors still report scalability pressure for large instances, especially tied to CP-SAT `Circuit` / `MultipleCircuit` behavior on larger VRP-like structures.
- Gains depend on how informative the initial truck-only hint is. ^[inferred]

## Related

- [[concepts/pdsvrp-c]]
- [[concepts/cp-sat-hint-start]]
- [[_papers/montemanni2024parallel/montemanni2024parallel-extracted]]
- [[_papers/nguyen2023parallel/nguyen2023parallel-extracted]]
- [[_papers/montemanni2023constraint/montemanni2023constraint-extracted]]
- [[concepts/collective-drone-delivery]] — collective drones are the defining feature of PDSVRP-c
- [[concepts/collective-drone-delivery]] — the c-drone mechanism that PDSVRP-c's collective missions rely on

## Sources

- [[_papers/montemanni2024combining/montemanni2024combining-extracted.md]]
- [[_papers/montemanni2024combining/montemanni2024combining.md]]
- [[_papers/montemanni2024combining/images/page_52_image_8.jpg]]
- [[_papers/montemanni2024combining/images/page_53_image_3.jpg]]
- [[_papers/montemanni2024combining/images/page_54_image_2.jpg]]
- [[_papers/montemanni2024combining/images/page_54_image_5.jpg]]
- [[_papers/montemanni2024combining/images/page_102_image_3.jpg]]
- [[_papers/montemanni2024combining/images/page_105_table_3.jpg]]
- [[_papers/montemanni2024combining/images/page_105_table_5.jpg]]
- [[_papers/montemanni2024combining/images/page_111_image_10.jpg]]
- [[_papers/montemanni2024combining/images/page_112_image_10.jpg]]
- [[_papers/montemanni2024combining/images/page_112_image_12.jpg]]
- [[_papers/montemanni2024combining/images/page_112_image_13.jpg]]
- [[_papers/montemanni2024combining/images/page_112_image_16.jpg]]
- [[_papers/montemanni2024combining/images/page_112_image_2.jpg]]
- [[_papers/montemanni2024combining/images/page_112_image_4.jpg]]
- [[_papers/montemanni2024combining/images/page_112_image_5.jpg]]
- [[_papers/montemanni2024combining/images/page_112_image_8.jpg]]
- [[_papers/montemanni2024combining/images/page_112_table_23.jpg]]
- [[_papers/montemanni2024combining/images/page_113_equation_8.jpg]]
- [[_papers/montemanni2024combining/images/page_113_table_11.jpg]]
- [[_papers/montemanni2024combining/images/page_119_equation_4.jpg]]
- [[_papers/montemanni2024combining/images/page_121_table_4.jpg]]
- [[_papers/montemanni2024combining/images/page_122_table_3.jpg]]
- [[_papers/montemanni2024combining/images/page_128_chart_6.jpg]]
- [[_papers/montemanni2024combining/images/page_129_chart_2.jpg]]
