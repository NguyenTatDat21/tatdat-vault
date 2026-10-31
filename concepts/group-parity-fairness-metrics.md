---
title: Group parity fairness metrics in machine learning
summary: "Group parity fairness metrics in ML decisions: demographic parity, equalized odds, accuracy parity, predictive rate parity, W(δ)=1−|B(δ)|, pairwise incompatible."
tags: [fairness, machine-learning]
provenance:
  extracted: 0.85
  inferred: 0.15
  ambiguous: 0
base_confidence: 0.67
tier: supporting
category: concepts
created: 2026-10-29T17:37:00Z
updated: 2026-10-30T18:52:00Z
sources:
- _papers/xinyingchen2023guide/xinyingchen2023guide.md
relationships:
  - target: references/xinyingchen2023guide
    type: related_to
  - target: concepts/inequality-measures-fairness-formulations
    type: related_to
  - target: concepts/welfare-social-function-fairness-formulations
    type: related_to
lifecycle: draft
lifecycle_changed: 2026-10-29T17:37:00Z
---

> [!tldr] Group parity fairness metrics in machine learning.

## Key claims
- W(δ)=1−|B(δ)| with a_i=1 selection, N protected, N' rest, δ decisions; demographic parity `B(δ)= (1/|N|)Σδ_i − (1/|N'|)Σδ_i`, 0≤W≤1, complete parity W=1, Dwork et al. 2012, critiques. ^[inferred]
- Equalized odds eq. 6 equality of opportunity `Σa_iδ_i/Σa_i (N) − Σa_iδ_i/Σa_i (N')`, qualified rates among qualified, unqualified false positive rate; accuracy parity eq. 8 ` (1/|N|)Σ(a_iδ_i+(1−a_i)(1−δ_i)) − (1/|N'|)Σ…`. ^[inferred]
- Predictive rate parity eq. 9 `B(δ)=Σa_iδ_i(N)/Σδ_i(N) − Σa_iδ_i(N')/Σδ_i(N')`, risk-assessment recidivism Dieterich 2016, Chouldechova 2017, child maltreatment screening Chouldechova et al. 2018; no consensus, pairwise incompatible, first three easy linear, predictive rate parity extremely difficult. ^[inferred]

## Related
- [[_papers/xinyingchen2023guide/xinyingchen2023guide-extracted]] — source.
- [[concepts/inequality-measures-fairness-formulations]] — inequality metrics compare with group parity.
- [[concepts/welfare-social-function-fairness-formulations]] — group parity as constraints/objectives.

## Sources

- `_papers/xinyingchen2023guide/xinyingchen2023guide-extracted.md`
