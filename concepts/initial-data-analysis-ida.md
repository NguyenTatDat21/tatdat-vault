---
title: "Initial data analysis (IDA): Chatfield's five-stage model and the data-scrutiny sequence"
summary: "Chatfield ch5-6: five stages, two phases, four IDA steps, sample-size thresholds, DATA = FIT + RESIDUAL."
tags: [operations-research]
provenance:
  extracted: 0.92
  inferred: 0.05
  ambiguous: 0.03
base_confidence: 0.67
tier: core
category: concepts
created: 2026-10-30T09:28:40Z
updated: 2026-10-31T02:05:00Z
sources:
  - _papers/chatfieldProblemSolvingStatisticians1995/chatfieldProblemSolvingStatisticians1995.md
  - _papers/chatfieldProblemSolvingStatisticians1995/chatfieldProblemSolvingStatisticians1995-extracted.md
relationships:
  - target: "[[references/chatfield1995-problem-solving-statisticians-guide]]"
    type: related_to
  - target: "[[concepts/statistical-investigation-lifecycle]]"
    type: related_to
  - target: "[[concepts/six-guidelines-anaesthetic-case-statistical-problem-solving]]"
    type: related_to
  - target: "[[concepts/definitive-analysis-procedure-choice]]"
    type: related_to
  - target: "[[concepts/data-collection-designs-and-pitfalls]]"
    type: related_to
  - target: "[[concepts/effective-statistician-eight-principles]]"
    type: related_to
lifecycle: draft
lifecycle_changed: 2026-10-30T09:28:40Z
---

> [!tldr] Five stages, the first of which is the whole art of IDA, and four steps that can take as little as half an hour.^[extracted]

## Summary

Chapter 5 sets out Chatfield's procedure, in his view "not too far removed from my ideal, if I had one". It is aimed at statistical inference, the aim in much of the book, and is not a model for descriptive statistics, where the main aim is to summarize and present the data. The **five stages** are: look at the data; formulate a sensible model; fit the model; check the fit of the model; utilize/present the model. All stages are important and none is easy, and they form "an iterative process with, hopefully, feedback from each stage to earlier stages".^[extracted]

The **two phases** split the five stages: a preliminary analysis (stage 1 — processing, quality checking, modifying, summarizing, looking for important features, assessing the effects of removing outliers, deciding which features are likely to be important in the final model) followed by a definitive analysis (stages 2–4, model formulation, fitting, checking). Chatfield's own terminology is deliberately neutral: "I shall adopt the neutral title 'initial examination of data' (abbreviated as IDA) in order to encompass this activity". The chapter 6 title "Initial data analysis: the key to statistical problem solving" makes IDA the key, and the chapter's key messages are "the importance of good data collection and good data scrutiny and presentation as a prelude to proper statistical inference" and "the dangers of drawing over-optimistic conclusions from statistical analyses".^[extracted]

The procedure applies to almost all the data types that occur in practice, and has been successfully applied to large data sets; a full, rigorous and thorough analysis takes much longer than half an hour.^[extracted]

## Key ideas

- **Stage 1, the details.** Look at the data using all the simple graphical methods in chapter 6, plus simple summary statistics and correlations, simple analysis of means, comparisons of sub-group means, and significance tests of simple comparisons, all designed to look for simple features in the data.^[extracted]
- **The IDA sequence, chapter 6.** (1) Plot each variable graphically, one by one, with simple graphs (histograms, time plots, boxplots). (2) Calculate summary statistics — mean, sd, median, quartiles, total, mode, skewness, kurtosis, number missing, number zero — for each variable, plus derived statistics such as ratios, log transforms, sums of squares, interactions. (3) Calculate correlations between all pairs of quantitative variables, as correlation coefficients and scatterplots, plus cross-classified statistics for categorical variables; look for extreme values, outliers, trends, clusters, gaps, anomalies, anomalies in the summary statistics, correlation, missing values, zero values.^[extracted]
- **The four steps of IDA.** (1) Plot each variable graphically, one by one, using simple graphs, looking for anomalies, missing values, outliers, zero values, patterns, trends, clusters, gaps, unusual features; (2) find the important features, i.e. look for unusual features and outliers, try to explain anomalies, investigate outliers and patterns, look at all variables, look for sub-groups, cross-classify, look for relationships, look for unusual values, look at the structure; (3) look for simple statistical relationships, i.e. look at all variables, look for patterns, look for relationships, look for trends, look for clusters, look for gaps, look for unusual features; (4) calculate summary statistics, look at sub-groups, look at the structure, look at the relationship, look for the model.^[extracted]
- **The four steps of the definitive analysis.** (1) Choose the model; (2) fit the model; (3) check the fit; (4) utilize/present the model.^[extracted]
- **Chapter 6, the data-scrutiny sequence.** Data scrutiny (sections 6.2–6.4) and the four IDA steps (section 6.5) are "the main topic of this chapter, and the main topic of this book"; it begins with the four data-collection methods from chapter 4, the four data types, and the four data-analysis methods, and the four steps "can take as little as a half-hour".^[extracted]
- **Thresholds for trusting the sample.** Sample sizes below about 10 quantitative measurements or about 30 categorical observations are "very unreliable"; they should be treated as pilot samples and the results reported as indicative, not as a basis for firm conclusions.^[extracted]
- **Scale levels.** Qualitative, binary, ordinal, and quantitative, with the "interval" and "ratio" sub-types of quantitative. The distinction between interval and ratio is largely irrelevant in practice; a qualitative variable with a natural ordering is best treated as ordinal; a count with a large number of possible values is best treated as quantitative, and the parametric/non-parametric division is a matter of judgment.^[extracted]
- **Data scrutiny, three sections.** Checking data quality (the first step, checking against the data-collection protocol and the design), looking at the structure (cross-classification, looking for the pattern in the data, checking for anomalies, and looking for outliers), and data presentation (the first graphical display, looking at the data, looking for anomalies, looking for patterns).^[extracted]
- **Exploration before inference, the model-building list.** The chapter 5 list of methods for model-building excludes "best fit"; data mining, "the automatic extraction of models" (Lovell, 1983), is listed, and the overfitting/underfitting compromise is recognized, citing Cox & Snell (1981, chapter 4) and Gilchrist (1984); it excludes any method for designing experiments, which is chapter 4's subject.^[extracted]
- **DATA = FIT + RESIDUAL.** The aphorism "DATA = FIT + RESIDUAL" (the chapter 7 summary, echoing Anscombe), and, from chapter 9, the "equivalent aphorism DATA = SIGNAL + NOISE". "The key to good statistical methods is to understand the data"; chapter 11's aphorism is "Spend effort on the data, not on the analysis."^[extracted]
- **Exploratory versus confirmatory.** The exploratory approach is "largly synonymous with IDA", as the term is used in this book (chapter 6, section 6.1); the term data analysis is used in preference to exploratory data analysis.^[extracted]
- **The procedure's own summary.** The five stages, the four steps, and the four data-collection methods, and the key messages: do not trust data you did not collect yourself; get involved at the start; the two phases; the four data types; the four data-analysis methods; "the key to good statistical methods is to understand the data".^[extracted]
- **The practical sequence.** Chatfield gives a practical ordering: data collection, IDA, the definitive analysis, the presentation, and the report, with the presentation "an important part of the whole process"; the report structure from chapter 8, section 8.1.^[extracted]

## Key numbers

| Item | Value |
| --- | --- |
| Five stages | look, formulate, fit, check, utilize/present |
| IDA steps | 4, can take as little as half an hour |
| Unreliable sample sizes | below ~10 quantitative measurements, below ~30 categorical observations |
| Data types | qualitative, binary, ordinal, quantitative (interval, ratio) |
| Data-analysis methods | 4 (descriptive, probabilistic, inferential, predictive) |
| Data-collection methods | 4 (experiments, sample surveys, observational studies, specialist investigations) |
| Aphorisms | DATA = FIT + RESIDUAL; DATA = SIGNAL + NOISE |

## Related

- [[six-guidelines-anaesthetic-case-statistical-problem-solving]] — Rule 4 gives IDA as step 1.
- [[definitive-analysis-procedure-choice]] — stages 2–4, procedure class, and the checks on the procedure.
- [[chatfield1995-problem-solving-statisticians-guide]] — chapter 5 (23–36) and chapter 6 (37–74).

## Sources

- `_papers/chatfieldProblemSolvingStatisticians1995/chatfieldProblemSolvingStatisticians1995.md`
- `_papers/chatfieldProblemSolvingStatisticians1995/chatfieldProblemSolvingStatisticians1995-extracted.md`
