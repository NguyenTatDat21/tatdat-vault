---
title: Problem Solving — A Statistician's Guide (2nd ed.)
category: references
tags: [statistics, methodology, problem-formulation, data-analysis-practice]
relationships:
  - target: "[[concepts/statistical-investigation-lifecycle]]"
    type: derived_from
  - target: "[[references/bertsimas2020-predictive-to-prescriptive-analytics]]"
    type: related_to
  - target: "[[references/chen2010-shrinkage-mmse-covariance-estimation]]"
    type: related_to
sources:
  - _papers/chatfieldProblemSolvingStatisticians1995/chatfieldProblemSolvingStatisticians1995-extracted.md
  - _papers/chatfieldProblemSolvingStatisticians1995/chatfieldProblemSolvingStatisticians1995.md
summary: >-
  Practical statistics handbook emphasizing end-to-end problem solving: framing questions, collecting and exploring data, choosing robust analyses, and communicating results.
provenance:
  extracted: 0.87
  inferred: 0.11
  ambiguous: 0.02
base_confidence: 0.67
lifecycle: draft
lifecycle_changed: 2026-10-22
tier: supporting
created: 2026-10-22T21:12:00Z
updated: 2026-10-24T18:36:02Z
---

# Problem Solving — A Statistician's Guide (2nd ed.)

> [!tldr] Statistics is treated as a decision process, not a recipe: define the real question, inspect data early, pick methods that match assumptions, and communicate uncertainty clearly.

## Problem & Motivation

Many analyses fail not because formulas are wrong, but because the original problem is poorly framed or data quality is misunderstood. The book addresses this by structuring statistical work as a complete lifecycle from question to action.

## Framework

Core workflow distilled from the text:

The book's chapter on the stages of a statistical investigation lists seven steps (the text notes the list "is not sacrosanct"):

1. Understand and formulate the problem in statistical terms, clarifying the objectives and searching the literature.
2. Plan the investigation and collect the data, balancing collection and analysis effort (the data-collection method is crucial).
3. Assess the structure and quality of the collected data (processing, errors, outliers, missing values).
4. Carry out an initial examination — summary statistics, graphs, tables; descriptive analysis may suffice.
5. Select and perform appropriate analyses, checking fitted models via residual analysis and refining as needed.
6. Compare the findings with previous results, acquiring further data where needed.
7. Interpret and communicate the results, with extra care over graphs, tables, and output.

The book opens this chapter with the quote: "An approximate answer to the right question is worth a great deal more than a precise answer to the wrong question."

## Main Contributions

- Emphasizes practical judgment over automatic procedure selection.
- Integrates exploratory analysis and model criticism as first-class steps.
- Highlights communication and interpretation as part of statistical validity, not post-processing.

## Limitations

- As a methodology text, evidence is principle-driven and example-based rather than benchmark-comparative.
- Some software-era details are dated; conceptual workflow remains reusable. ^[inferred]

## Related

- [[concepts/statistical-investigation-lifecycle]]
- [[references/bertsimas2020-predictive-to-prescriptive-analytics]]
- [[references/chen2010-shrinkage-mmse-covariance-estimation]]
- [[concepts/predictive-to-prescriptive-analytics]]

## Open Questions

- Which parts of this lifecycle should be mandatory in modern ML/AI deployment reviews?
- How can organizations measure whether teams actually follow this full workflow? ^[inferred]

## Sources

- [[_papers/chatfieldProblemSolvingStatisticians1995/chatfieldProblemSolvingStatisticians1995-extracted.md]]
- [[_papers/chatfieldProblemSolvingStatisticians1995/chatfieldProblemSolvingStatisticians1995.md]]
