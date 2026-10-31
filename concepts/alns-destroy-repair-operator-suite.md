---
title: >-
  ALNS Destroy-Repair Operator Suite (WTD, WDD, BD, LDR-1, LDR-2, HR, AR, RR)
category: concepts
tags: [optimization, heuristics, alns]
summary: The destroy operators RD, WTD, WDD, BD and repair operators RR, AR,
  LDR-1, LDR-2, HR of the multi-drop FSTSP ALNS, with Metropolis acceptance,
  weights, cooling, archive, destroy factor.
provenance:
  extracted: 0.85
  inferred: 0.13
  ambiguous: 0.02
base_confidence: 0.67
tier: core
lifecycle: draft
created: 2026-10-29T17:12:00Z
updated: 2026-10-30T18:52:00Z
sources:
  - _papers/windrasmara2022adaptive/windrasmara2022adaptive.md
relationships:
  - target: "[[references/windrasmara2022-alns-multi-drop-fstsp]]"
    type: extends
  - target: "[[references/ropke2006-adaptive-large-neighborhood-search-pdptw]]"
    type: extends
  - target: "[[references/santini2018-alns-acceptance-criteria]]"
    type: related_to
  - target: "[[concepts/adaptive-large-neighborhood-search-for-mip]]"
    type: related_to
  - target: "[[concepts/large-neighborhood-ship-pair-destroy-repair]]"
    type: related_to
lifecycle_changed: 2026-10-29T17:12:00Z
---

# ALNS Destroy-Repair Operator Suite
^d1
The suite extends the ALNS of Røpke & Pisinger 2006 for the multi-drop FSTSP: destroy operators RD (random removal), WTD (worst truck distance, truck-served nodes), WDD (worst drone distance, reducing drone time to satisfy endurance), BD (block destroy, deleting an interval from `AN`, `AM`, or both); repair operators RR (random), AR (archive repair, Algorithm 3, `rand ≤ 0.33` insert `AM_j`, 0.33–0.67 `AN_j`, else both), LDR-1 (least distance `d_{i−1→i}`, Algorithm 4), LDR-2 (successor variant `d_{i→i+1}`), HR (hill-climbing swap of removed nodes).
^d2
Selection is roulette wheel `Pr(c−)=ω_c−/Σ`, `Pr(c+)=ω_c+/Σ`, weight update `ω_{i+1}− = λ(ω_i−)+(1−λ)(η_i)` with scores by outcomes Ω1–Ω4; acceptance is Metropolis `Pr = exp(−(M'−M)/(BZ×T_c))` with cooling `T_c ← α×T_c`; the elite archive `AR_s` drops its worst member when `M' ≤ M^AR_s`; the destroy factor is `f_c = f_1 − (f_1−f_0)(i_c/I)`, destroyed nodes `ND_c = n(f_c)`; operator removal t-tests ranked BD 25.98 % and LDR-1 22.43 % as most impactful on the Ha dataset.
^d3
The suite is a concrete instance of the ALNS destroy/repair pattern, tuned for truck-drone synchronization.^[inferred]

## Related
- [[references/windrasmara2022-alns-multi-drop-fstsp]] — the paper that instantiated the suite.
- [[references/ropke2006-adaptive-large-neighborhood-search-pdptw]] — canonical ALNS.
- [[references/santini2018-alns-acceptance-criteria]] — acceptance criteria survey.
- [[concepts/adaptive-large-neighborhood-search-for-mip]] — ALNS × MIP pattern.
- [[concepts/large-neighborhood-ship-pair-destroy-repair]] — ship-pair destroy/repair.

## Sources

- `_papers/windrasmara2022adaptive/windrasmara2022adaptive-extracted.md`
