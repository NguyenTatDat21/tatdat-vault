---
title: Automated Model Generation and Improvement
summary: "Model quality is generated: Conjure produces streamliners, Savile Row eliminates common subexpressions, propagator generation removes auxiliary variables, reification covers 82 % of the catalogue."
tags: [machine-learning, heuristics, modeling-pattern, operations-research, constraint-programming]
provenance:
  extracted: 1.0
  inferred: 0.0
  ambiguous: 0.0
base_confidence: 0.67
tier: core
category: concepts
created: 2026-10-29T15:50:00Z
updated: 2026-10-31T15:41:41Z
sources:
  - _papers/pesant2015principles/pesant2015principles.md
  - _papers/pesant2015principles/pesant2015principles-extracted.md
relationships:
  - target: references/pesant2015-cp2015-proceedings
    type: related_to
  - target: concepts/encoding-preservation-under-composition-and-merging
    type: related_to
  - target: concepts/auxiliary-decision-variable-model-strengthening
    type: related_to
  - target: concepts/large-neighborhood-search
    type: related_to
lifecycle: draft
lifecycle_changed: 2026-10-29T15:50:00Z
provenance_note: "Marker pass: markers match the numbers (9 extracted / 0 inferred / 0 ambiguous claim units); extracted = every distinctive term in the claim appears in the source text, including page-range citations."
---




# Automated Model Generation and Improvement

> [!tldr] The model a solver receives is generated, and the generator can improve it. Conjure generates streamliners from an Essence specification; Savile Row applies common subexpression elimination to the SAT formulation; a pattern-driven compiler removes auxiliary variables that flattening introduced; reification makes global constraints reifiable at 82 % of the catalogue.  ^[extracted]

## Summary

Streamliners — uninferred additional constraints that prune the search space — have been built by hand by experts; this paper automates their generation from an Essence specification, the first demonstration of automated generation of effective streamliners, and generated conjectures often reduce search size by orders of magnitude (idx 42, chapter 34, pp. 480-496). Common subexpression elimination in Savile Row reduces model size by removing shared expressions, applied to SAT formulations (idx 31, chapter 23, pp. 330-340). Auxiliary-variable elimination replaces two constraints sharing an auxiliary variable by one equivalent constraint (idx 30, chapter 22, pp. 313-329). Reification is the reification method for global constraints, determine-and-test, with 313 of 381 = 82 % of the Global Constraint Catalogue reifiable (idx 64, journal-track abstract, p. 733).  ^[extracted]

## Key ideas

- **Streamliner generation** — Essence 1.3 specifications (given/find/such that) with abstract decision variables (set, multiset, function, relation, partition), generated through the tool-chain Conjure → Essence′ → Savile Row → the target solver; Van Der Waerden is the worked example, `given k, l, n : int(1..)` with a partition (idx 42, chapter 34, pp. 480-496).  ^[extracted]
- **Common subexpression elimination** — CSE, from Cocke 1970, is applied to SAT formulations: reducing two constraint variables to one means the SAT variables and clauses encoding the second variable are never added, and implied constraints added to elicit common subexpressions are removed after CSE if unchanged (idx 31, chapter 23, pp. 330-340).  ^[extracted]
- **Identical-CSE algorithm** — Algorithm 1 keeps a new-constraint list and a hash table mapping expressions to lists, populating the map from the AST, then merging identical expressions (idx 31, chapter 23, pp. 330-340).  ^[extracted]
- **Eliminating auxiliary variables** — flattening introduces many auxiliary variables; the 5-step approach identifies frequent patterns of two constraints sharing an auxiliary variable, defines a new predicate on all variables of the pattern, and the pattern signature is `Y_1,...,Y_n,K_1,...,K_m` with `n ≥ 2` variables and `m ≥ 0` constants; the language is FlatZinc, the solver is Gecode, propagators are built from indexicals (idx 30, chapter 22, pp. 313-329).  ^[extracted]
- **Flattening cost measured** — of 488 benchmark instances, 75 introduce no auxiliary variables and 264 have flattening multiplying the number of variables; `constraint w != max(y, z) | 1 <= z;` introduces 3 auxiliary variables (idx 30, chapter 22, pp. 313-329).  ^[extracted]
- **Reification of global constraints** — determine-and-test reification, 313 of 381 = 82 % of the Global Constraint Catalogue reifiable (idx 64, journal-track abstract, p. 733).  ^[extracted]
- **Encoding size as a design target** — selection networks are generated with size formulas, and the generalized totalizer is generated with an arc-consistency-preserving structure; the implication-chain encoding is generated from chains already present in the problem (idx 24, chapter 16, pp. 210-225; idx 23, chapter 15, pp. 200-209; idx 9, chapter 1, pp. 3-11).  ^[extracted]

## Related

- [[references/pesant2015-cp2015-proceedings]] — the volume these papers are drawn from
- [[concepts/encoding-preservation-under-composition-and-merging]] — the encoding-side counterpart
- [[concepts/auxiliary-decision-variable-model-strengthening]] — decision-variable-induced model strengthening
- [[concepts/large-neighborhood-search]] — generated models are the input LNS re-solves

## Sources

- `_papers/pesant2015principles/pesant2015principles-extracted.md` (18,510 lines), chapters 1, 15, 16, 22, 23, 34 and the idx 64 abstract.
