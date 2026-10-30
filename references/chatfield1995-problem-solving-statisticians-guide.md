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
  - target: "[[concepts/six-guidelines-anaesthetic-case-statistical-problem-solving]]"
    type: related_to
  - target: "[[concepts/problem-formulation-objectives-type-iii-error]]"
    type: related_to
  - target: "[[concepts/data-collection-designs-and-pitfalls]]"
    type: related_to
  - target: "[[concepts/initial-data-analysis-ida]]"
    type: related_to
  - target: "[[concepts/definitive-analysis-procedure-choice]]"
    type: related_to
  - target: "[[concepts/effective-statistician-eight-principles]]"
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
tier: core
created: 2026-10-22T21:12:00Z
updated: 2026-10-30T14:08:41Z
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

## Verified anatomy (page-by-page, from the extracted text)

- **Bibliographic:** Chapman & Hall, 1995; print ISBN 978-0-4126-0630-4, e-book ISBN 978-1-1358-3079-1, DOI 10.1201/9781315135440, 348 pages, series "Chocolate"; electronic ISBN 0-412-58380-2 is in the front-matter PDF page 4.^[extracted]
- **Structure (TOC page numbers as authority):** Preface vii, Prelude ix, chapter 1 The rules of the game p. 1, chapter 2 Formulation p. 7, chapter 3 p. 9, chapter 4 p. 13, chapter 5 p. 23, chapter 6 p. 37, chapter 7 p. 75, chapter 8 p. 93, chapter 9 p. 101, chapter 10 p. 105, chapter 11 p. 111, chapter 12 Numeracy p. 115, Summary p. 121, A Descriptive statistics p. 127, B Exploring data p. 137, C Exercises p. 163, D Answers p. 173, E Further reading p. 189, F Author p. 207, G Books p. 215, H Software p. 231, Appendix A p. 237, B p. 293, C Some useful addresses p. 305, References p. 311, Author index p. 319, Subject index p. 321.^[extracted]
- **Appendix A has fifteen sections**, A.1 to A.15, with the introduction stating the appendix "is an aide-mémoire … not intended for use as a 'cookbook'".^[extracted]
- **Exercises:** section B has 15 exercises, section C has 34 (C.1 to C.14, plus 20 real-data exercises from sources listed in section D), 49 in total; A.4.3 lists 20 further reading exercises, A.5.3 lists 29.^[extracted]
- **Preface, verbatim:** "Problem solving is a complex process which is something of an acquired knack. This makes it tricky to teach. The situation is not helped by those textbooks which adopt a 'cookbook' approach and give the false impression that statistical techniques can be performed 'parrot-fashion'." The Preface names the six Rules (Rule 6, presentation), the book's emphases (problem formulation, data collection, initial data analysis, model formulation, communication, numeracy, and "the ability to think in a statistically aware way"), the target reader ("undergraduates of all types … research students … those whose work involves the collection, analysis and interpretation of data"), and the second-edition additions (new exercises E.5, E.6, G.5(b), rewrites, and the emphasis on communication and numeracy). The book is "based on a course I have given for several years at Bath University to final-year statistics undergraduates … examined by continuous assessment", and Chatfield admits the book "will not please all the people all the time. It is often said that ten statisticians will ten different ways." Chatfield also acknowledges Cox, Draper, Ehrenberg, Hand, Hinkley, Johnston, Mead, Silverman, Williams, "Particular thanks … to Jim Hodges for Example 4.3(3)", and the Taylor & Francis e-Library, ISBN 0-412-58380-2, 2003.^[extracted]
- **The six Rules:** see [[six-guidelines-anaesthetic-case-statistical-problem-solving]].^[extracted]
- **The five stages:** see [[initial-data-analysis-ida]] and [[definitive-analysis-procedure-choice]].^[extracted]
- **The eight principles:** see [[effective-statistician-eight-principles]].^[extracted]
- **Related in this vault:** [[concepts/statistical-investigation-lifecycle]], [[concepts/automated-model-generation]] (the model-formulation step in a different domain), [[references/bertsimas2020-predictive-to-prescriptive-analytics]], [[references/chen2010-shrinkage-mmse-covariance-estimation]].
