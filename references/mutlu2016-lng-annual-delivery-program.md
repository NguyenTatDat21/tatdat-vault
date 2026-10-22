---
title: >-
  Annual LNG Delivery Program for Upstream Supply Chain (Mutlu et al., 2016)
category: references
tags: [paper, maritime, lng, inventory-routing]
relationships:
  - target: "[[concepts/annual-lng-delivery-program]]"
    type: uses
  - target: "[[concepts/maritime-routing-under-uncertainty]]"
    type: related_to
  - target: "[[references/ksciuk2023-maritime-uncertainty-review]]"
    type: related_to
sources:
  - _papers/mutlu2016comprehensive/mutlu2016comprehensive-extracted.md
  - _papers/mutlu2016comprehensive/mutlu2016comprehensive.md
  - _papers/mutlu2016comprehensive/images/page_8_chart_5.jpg
  - _papers/mutlu2016comprehensive/images/page_9_chart_2.jpg
  - _papers/mutlu2016comprehensive/images/page_9_chart_4.jpg
summary: >-
  Formulates a realistic LNG annual delivery planning problem and shows a vessel-routing heuristic (VRH) beats long-run CPLEX baselines, with notable split-delivery savings.
provenance:
  extracted: 0.87
  inferred: 0.10
  ambiguous: 0.03
base_confidence: 0.67
lifecycle: draft
lifecycle_changed: 2026-10-22
tier: supporting
created: 2026-10-22T09:52:03Z
updated: 2026-10-22T18:14:03Z
---

# Annual LNG Delivery Program for Upstream Supply Chain (Mutlu et al., 2016)

> [!tldr] The paper integrates production, inventory, fleet scheduling, and contract structure into LNG annual delivery planning, then shows a practical heuristic stack (VRH/MVRH) outperforms long-run exact baselines.

## Problem & Scope

The paper targets tactical annual delivery planning (ADP) for LNG suppliers with practical constraints, including:
- heterogeneous vessel fleet,
- maintenance and berth constraints,
- contract over/under-delivery penalties,
- inventory-production coupling,
- and optional split-delivery policies.

The objective is cost-efficient annual plans under realistic contractual and operational structures.

## Method / Architecture

Two solution layers are combined:

1. **MIP baseline (EM):** exact model solved with CPLEX under long fixed runtime;
2. **Heuristic stack:** Vessel Routing Heuristic (VRH) and reranking-based extensions, then reduced-master refinement.

Operationally, VRH explores contract orderings and fast route construction, while reduced-master optimization improves candidate plans.

## Results

From the reported computational study on 18 benchmark instances:

- EM/CPLEX required very long runtimes and first feasible solutions appeared only after long execution windows.
- VRH generated feasible plans quickly (seconds-level for single permutations) and completed broader search within hours.
- VRH outperformed EM on all listed instances in objective quality.
- Reported **average improvement by VRH over EM: 20.1%**.
- Allowing split delivery provided additional savings with **average 4.2%** reduction vs no-split variants.
- Sensitivity analysis on storage-to-production ratio (`ρ^I`) reported cost savings that can reach around **40%** when storage capacity is substantially increased.

## Limitations

- Results are based on constructed benchmark classes; transferability to every market/network design is not guaranteed.
- High combinatorial complexity remains; heuristic quality depends on reranking and parameter choices.
- Some extraction lines are oversized due embedded figures, so figure-level visual interpretation should be verified from PDF when needed. ^[ambiguous]

## Related

- [[concepts/annual-lng-delivery-program]]
- [[concepts/maritime-routing-under-uncertainty]]
- [[references/ksciuk2023-maritime-uncertainty-review]]
- [[_papers/andersson2017creating/andersson2017creating-extracted]]
- [[_papers/al-haidous2016optimal/al-haidous2016optimal-extracted]]
- [[_papers/goel2015constraint/goel2015constraint-extracted]]
- [[_papers/fagerholt2023maritime/fagerholt2023maritime-extracted]]

## Bibliographic Record

- Citation key: `mutlu2016comprehensive`
- DOI: `10.1016/j.ejor.2015.10.031`
- Canonical URL: <https://www.sciencedirect.com/science/article/pii/S0377221715009571>
- Publication: *European Journal of Operational Research* (2016)
- Authors: Fatih Mutlu; Mohamed K. Msakni; Hakan Yildiz; Erkut Sönmez; Shaligram Pokharel
- Companion metadata note: [[_papers/mutlu2016comprehensive/mutlu2016comprehensive.md]]

## Sources

- [[_papers/mutlu2016comprehensive/mutlu2016comprehensive-extracted.md]]
- [[_papers/mutlu2016comprehensive/mutlu2016comprehensive.md]]
- [[_papers/mutlu2016comprehensive/images/page_8_chart_5.jpg]]
- [[_papers/mutlu2016comprehensive/images/page_9_chart_2.jpg]]
- [[_papers/mutlu2016comprehensive/images/page_9_chart_4.jpg]]
