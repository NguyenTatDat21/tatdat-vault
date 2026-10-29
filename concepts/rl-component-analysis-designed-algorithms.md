---
title: RL Component Analysis of Designed Algorithms
summary: The best learned search algorithms are analysed by counting which operators and heuristics the policy calls, a post-hoc check that the learned policy does not collapse onto one component.
tags: [reinforcement-learning, component-analysis, hyper-heuristics, automated-algorithm-design, policy-analysis]
provenance:
  extracted_paper_extracted_md: 0.85
  extracted_paper_sidecar: 0.05
  author_synthesis: 0.10
base_confidence: 0.67
tier: supporting
created: 2026-10-29T18:10:00Z
updated: 2026-10-29T18:10:00Z
lifecycle: draft
lifecycle_changed: 2026-10-29
sources:
- _papers/yi2023automated/yi2023automated-extracted.md
- references/ganjia2026-multiobjective-sustainable-supply-chain-scheduling.md
relationships:
- target: '[[references/yi2023-ace-gsf-automated-design-cvrptw]]'
  type: related_to
- target: '[[references/yang2022-vrpd-bilevel-heuristic]]'
  type: related_to
- target: '[[references/ganjia2026-multiobjective-sustainable-supply-chain-scheduling]]'
  type: related_to
- target: '[[concepts/actor-critic-entropy-automated-algorithm-design]]'
  type: part_of
- "references/ganjia2026-multiobjective-sustainable-supply-chain-scheduling"
---

# RL Component Analysis of Designed Algorithms

## The method
- The best individuals found by ACE are analysed by counting the operators and heuristics called during search, in three categories: `op` (operators), `se` (selection for evolution), `sr` (selection for replacement). ^[extracted, p. 24]  #component-analysis
- Every component is called at least once in every designed algorithm. ^[extracted, p. 25]  #component-analysis
- `h8` is called the most frequently. ^[extracted, p. 25]  #component-analysis
- Ganjia et al. (2026) count `op` in Table 24, `se` in Table 25, `sr` in Table 26. ^[extracted, p. 24]  #q-learning
## What the counts show
- ACE analysis excludes C101/C102/C201/C202, because ACE always found the best-known solutions on them in preliminary experiments.
- Yang & Ha (2022) analyse their evolved operators in the `op` component table, in a bilevel design that fixes the operators and heuristics. ^[synthesized, Q007]  #op
- Ganjia et al. (2026) count `op` in Table 24, `se` in Table 25, `sr` in Table 26 on three VRPTW instance sets. ^[synthesized, Q007]  #q-learning
- Chen & Hooker (2023) `references/xinyingchen2023guide` treat component choice as a design question in their ML track. ^[synthesized, Q007]  #policy-analysis
- The `sr` action space in ACE is small (h7/h8 only), so the policy learns little about `sr`, i.e. `sr` choices have small impact on the training curves. ^[synthesized, Q007]  #action-space

## Related pages
- [[references/yi2023-ace-gsf-automated-design-cvrptw]] — the ACE component counts.
- [[references/ganjia2026-multiobjective-sustainable-supply-chain-scheduling]] — the q-learning component counts.
- [[references/yang2022-vrpd-bilevel-heuristic]] — the evolved-operator analysis.
