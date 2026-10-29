---title: "Auxiliary Decision Variables in Scheduling Model Strengthening"
category: concepts
tags: [constraint-programming, mixed-integer-programming, scheduling, modeling-pattern, formulation-strength]
relationships:
  - target: "[[concepts/disjunctive-scheduling-constraint-programming-model]]"
    type: derived_from
  - target: "[[references/ku2016-mixed-integer-programming-job-shop]]"
    type: related_to
  - target: "[[references/isik2023-constraint-programming-hybrid-flow-shop]]"
    type: related_to
  - target: "[[references/jimenez-piqueras2023-constraint-programming-premarshalling]]"
    type: related_to
  - target: "[[references/halvorsen-weare2013-lng-routing-berth-inventory]]"
    type: derived_from
  - target: "[[references/vilim2015-failure-directed-search-cp-scheduling]]"
    type: derived_from

  - target: "[[concepts/lagrangian-decomposition-propagation]]"
    type: related_to
  - target: "[[concepts/automated-model-generation]]"
    type: related_to
  - target: "[[concepts/bound-tightening-relaxation-networks]]"
    type: related_to

sources:
  - _papers/ku2016mixed/ku2016mixed-extracted.md
  - _papers/ku2016mixed/ku2016mixed.md
  - _papers/isik2023constraint/isik2023constraint-extracted.md
  - _papers/isik2023constraint/isik2023constraint.md
  - _papers/jimenez-piqueras2023constraint/jimenez-piqueras2023constraint-extracted.md
  - _papers/jimenez-piqueras2023constraint/jimenez-piqueras2023constraint.md
summary: >-
  Scheduling evidence that adding auxiliary decision variables changes solver performance in ways model size cannot predict, and that strengthening strategies do not transfer between CP and MIP.
provenance:
  extracted: 0.75
  inferred: 0.25
  ambiguous: 0.00
base_confidence: 0.87
lifecycle: draft
lifecycle_changed: 2026-10-25
tier: supporting
created: 2026-10-25T11:47:49Z
updated: 2026-10-27T06:00:00Z
---

# Auxiliary Decision Variables in Scheduling Model Strengthening

> [!tldr] Across three scheduling papers, solver performance is driven by auxiliary decision variables and their constraint structure, not by model size: Liao's surplus variables flip the SCIP ranking, CP premarshalling models improve by adding variable groups, and CP objective-as-decision-expression saves time and memory.

## Key Ideas

- **Surplus variables change the solver's view.** Liao's disjunctive JSP model adds surplus variables q to the Manne big-M model; in CPLEX it is 2.5× slower, in SCIP presolving eliminates q and turns Liao into Manne, making it faster — perturbing Manne's constraint order reproduces the same gain. Model size predicted the wrong winner. ^[extracted, ku2016]
- **Adding variable groups strengthens CP.** The premarshalling CP series CP2 (priorities) → CP3 (+occupancy δ) → CP4 (+move origin z) → CP5 (+blocking w) each solves more instances faster (BZ avg time 87.0 s → 2.8 s); δ and z "are not needed to describe the problem" yet each step gains 7-13% solved instances. ^[extracted, jimenez]
- **Objective as decision expression.** Defining the makespan C_max as a CP decision expression (endOf) reduces variables and improves solution time and memory in HFSP CP models. ^[extracted, isik]
- **Redundant constraints help propagation.** A redundant Cumulative \le |M_s| constraint is added to HFSP CP models to strengthen propagation. ^[extracted, isik]
- **Strategies do not cross paradigms.** Transplanting CP-finding strategies into an IP solver, and IP strategies into CP, loses performance (52% fewer instances; 16-46× slower) — each paradigm needs its own strengthening logic. ^[extracted, jimenez]
- Indicator constraints (CPLEX IF/OR) performed worse than the big-M disjunction with a well bounded V for JSP. ^[extracted, ku]

## Pattern

$$\text{model quality} \neq f(\text{variables, constraints});\quad \text{model quality} = f(\text{structure}, \text{solver presolve/search})$$

Choose models empirically against the target solver, not by counting variables: auxiliary variables are cheap to add and can be decisive; presolve and propagation interplay is what makes one formulation beat another. ^[inferred]

## Related
- [[concepts/bound-tightening-relaxation-networks]] — shares constraint-programming + scheduling tags with this page
- [[concepts/automated-model-generation]] — shares constraint-programming + scheduling tags with this page
- [[concepts/lagrangian-decomposition-propagation]] — shares constraint-programming + scheduling tags with this page

- [[concepts/disjunctive-scheduling-constraint-programming-model]]
- [[references/ku2016-mixed-integer-programming-job-shop]]
- [[references/isik2023-constraint-programming-hybrid-flow-shop]]
- [[references/jimenez-piqueras2023-constraint-programming-premarshalling]]
- [[references/halvorsen-weare2013-lng-routing-berth-inventory]] — shares mixed-integer-programming + scheduling tags with this page
- [[references/vilim2015-failure-directed-search-cp-scheduling]] — shares constraint-programming + scheduling tags with this page

## Sources

- [[_papers/ku2016mixed/ku2016mixed-extracted.md]]
- [[_papers/ku2016mixed/ku2016mixed.md]]
- [[_papers/isik2023constraint/isik2023constraint-extracted.md]]
- [[_papers/isik2023constraint/isik2023constraint.md]]
- [[_papers/jimenez-piqueras2023constraint/jimenez-piqueras2023constraint-extracted.md]]
- [[_papers/jimenez-piqueras2023constraint/jimenez-piqueras2023constraint.md]]
