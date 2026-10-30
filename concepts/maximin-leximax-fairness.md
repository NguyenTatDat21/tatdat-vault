---
title: Maximin and leximax fairness criteria
summary: "Maximin, leximax, McLoone fairness criteria, Rawls difference principle, equality cost, leximax lexicographic sequence, McLoone median lower half, bandwidth."
tags: fairness, maximin, Rawlsian
provenance:
  extracted: 0.8
  inferred: 0.15
  ambiguous: 0.05
base_confidence: 0.67
tier: core
category: concepts
created: 2026-10-29T17:37:00Z
updated: 2026-10-29T17:37:00Z
sources:
- _papers/xinyingchen2023guide/xinyingchen2023guide-extracted.md
relationships:
  - target: references/xinyingchen2023guide
    type: related_to
  - target: concepts/leximax-leximin-fairness-principles
    type: related_to
  - target: concepts/sequential-leximax-threshold-models
    type: related_to
  - target: concepts/utility-fairness-thresholds
    type: related_to
  - target: concepts/alpha-fairness-proportional-fairness
    type: related_to
lifecycle: draft
lifecycle_changed: 2026-10-29T17:37:00Z
---

> [!tldr] Maximin and leximax fairness criteria.

## Key claims
- Rawls difference principle, social-contract original position, maximin W(u)=min_i{u_i} linearizable, institutions and primary goods Freeman 2003, Richardson & Weithman 1999, bandwidth allocation Luss 1999, Ogryczak & Śliwiński 2002, Ogryczak et al. 2008, reviewer assignment Stelmakh et al. 2018, ridesharing Nanda et al. 2020, medical appointment scheduling Samorini et al. 2021, ML Rawlsian Hashimoto 2018, Heidari 2019, Shah 2021. ^[inferred]
- Maximin equality cost: budget Σx_i≤B, u_i=a_i x_i, maximin equalizes utilities, u_0=B/Σ(1/a_i), expensive welfare of individual k, upper bound d_k reduces everyone to a_k d_k, unused resources B−d_k a_k Σ(1/a_i); leximax lexicographic sequence removes leftover resources, avoids high equality cost. ^[inferred]
- McLoone index `W(u)=1/(|I(u)|ũ) Σ_{i∈I(u)} u_i`, ũ median, I(u)={i|u_i≤ũ}, 1 if none below median, 0 long lower tail, educational equality/public policy. ^[inferred]

## Related
- [[_papers/xinyingchen2023guide/xinyingchen2023guide-extracted]] — source.
- [[concepts/leximax-leximin-fairness-principles]] — leximax/leximin, Pigou-Dalton axioms, OWA limits.
- [[concepts/sequential-leximax-threshold-models]] — leximax threshold, sequential SWFs, kidney exchange.
- [[concepts/alpha-fairness-proportional-fairness]] — alpha continuum utilitarian↔maximin.