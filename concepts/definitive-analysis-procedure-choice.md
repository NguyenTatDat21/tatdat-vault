---
title: "The definitive analysis: Chatfield's seven procedure classes and the checks on the analysis"
summary: "Chatfield ch7: seven procedure classes, five properties, six questions, the significance warning."
tags: [operations-research, modeling-pattern]
provenance:
  extracted: 0.93
  inferred: 0.05
  ambiguous: 0.02
base_confidence: 0.67
tier: core
category: concepts
created: 2026-10-30T09:28:40Z
updated: 2026-10-31T02:05:00Z
sources:
  - _papers/chatfieldProblemSolvingStatisticians1995/chatfieldProblemSolvingStatisticians1995.md
  - _papers/chatfieldProblemSolvingStatisticians1995/chatfieldProblemSolvingStatisticians1995-extracted.md
relationships:
  - target: "[[concepts/initial-data-analysis-ida]]"
    type: related_to
  - target: "[[references/chatfield1995-problem-solving-statisticians-guide]]"
    type: related_to
  - target: "[[concepts/six-guidelines-anaesthetic-case-statistical-problem-solving]]"
    type: related_to
  - target: "[[concepts/statistical-investigation-lifecycle]]"
    type: related_to
  - target: "[[concepts/effective-statistician-eight-principles]]"
    type: related_to
  - target: "[[concepts/problem-formulation-objectives-type-iii-error]]"
    type: related_to
lifecycle: draft
lifecycle_changed: 2026-10-30T09:28:40Z
---

> [!tldr] "I know how to do a t-test, but not when!" — procedure class, not procedure name; the analysis is judged by the residual.^[extracted]

## Summary

Chapter 7 (pages 75–92, Part One, "The basic tools: the art of statistics") is the definitive-analysis chapter: stages 2 to 4 of the five-stage procedure. It opens with the statistician's aphorism "I know how to do a t-test, but not when!" and gives seven classes of procedure organized by the aim of the analysis, five properties of a good analysis, six questions to ask before choosing one, seven comments on the process, and the parametric/non-parametric/robust division. The key formulation is Anscombe's: "DATA = FIT + RESIDUAL", with the "equivalent aphorism DATA = SIGNAL + NOISE" from chapter 9.^[extracted]

## Key ideas

- **The seven classes.** Class 1 methods with no model; class 2 methods for inference about a population; class 3 methods for inference about a relationship; class 4 methods for inference about the order of a relationship; class 5 methods for inference about an effect; class 6 methods for inference about a set of effects; and "various other methods".^[extracted]
- **The aim of class 5.** "To find the most probable model, to check the fit, to use the model, to present the results, to present a measure of precision (and the assumptions underlying the model)" — a "model" in the class 3–5 sense, not in the class 2 sense, with the method for inference about the population mean (class 2) as an example.^[extracted]
- **The five properties of a good analysis.** The five properties of a good analysis procedure: (1) to find a good model, (2) a model which is interpretable, (3) to test the fit, (4) to find the most probable model, and (5) a model with a "good" fit; with the procedure being "generally a parametric method with a suitable probability model, as long as no obvious objections to the model occur (parametric methods generally need the assumptions for validity)".^[extracted]
- **The six questions before choosing.** The questions to ask before choosing an analysis: the nature of the data, the aim, the assumptions, the robustness, the validity of the model, the adequacy of the fit, and "the number of data points available, the number of variables, the existence of outliers, the existence of trends".^[extracted]
- **The seven comments.** The seven comments on the analysis process, in order: (a) the analysis is not a simple procedure, there is no single procedure, multiple analyses are needed, and the aim is "to find the most probable model, to check the fit, to use the model, to present the results, to present a measure of precision"; (b) do not force the data into a model; (b) the analysis of variance, regression, correlation, chi-square, t-test, Mann-Whitney, Wilcoxon, sign test, distribution-free methods, "the parametric methods generally need the assumptions for validity"; (c) lateral thinking and the ad hoc modification, citing de Bono (1967); (d) the importance of knowing where to look things up; (e) the analysis is model building, and the model is the result; (f) the analysis with no model, as in IDA, and the "various other methods".^[extracted]
- **Parametric, non-parametric, robust.** Parametric methods generally need the assumptions for validity; non-parametric methods "for ordinal data, and for severely skewed data"; and the robust methods "in Appendix A.4, section on robust methods" in Appendix A.5.5.^[extracted]
- **The procedure as a model for the definitive analysis.** The five-stage procedure as a model for the definitive analysis, stages 2 to 4, with the model, the fit, the checking, the presentation, and the report, and with the aim "to find the most probable model, to check the fit, to use the model, to present the results, to present a measure of precision (and the assumptions underlying the model) as a whole".^[extracted]
- **DATA = FIT + RESIDUAL.** The formula, from the chapter 7 summary, is the key to the checking stage: the residual analysis, checking the fit of the model, and the model's ability to describe the data.^[extracted]
- **The significance warning.** Section 7.2: significance tests "are overused in the fields of medicine, biology and psychology", the P-value is over-interpreted in the literature, a test is used as a decision procedure in a way that is not always justified, and the P-value is a measure of the evidence against the null hypothesis, not a measure of the size of the effect.^[extracted]
- **Approaches to inference.** Section 7.4 covers the three approaches: the classical (significance tests and P-values), the Bayesian, and the likelihood-based; the "Bayesian methods are not generally used in practice as a result of the practical problems of specifying the prior distribution" and the likelihood principle.^[extracted]
- **The t-test formula.** Chatfield prefers the t-test form given as "the difference divided by its standard error", in preference to the usual formula, "which is less revealing".^[extracted]
- **Appendix A.5.** The statistical procedures, the parametric methods, and the non-parametric methods, are set out in appendix A.5, "A short guide to some statistical procedures", "for use as a guide to the type of procedure to be used", with the parametric methods in A.5.2, non-parametric methods in A.5.5, the distribution-free methods in A.5.5, the robust methods in A.4, and the "short guide" as a procedure, with a decision procedure for choosing a procedure.^[extracted]

## Key numbers

| Item | Value |
| --- | --- |
| Procedure classes | 7 (no model; population; relationship; order of relationship; an effect; a set of effects; various others) |
| Properties of a good analysis procedure | 5 |
| Questions to ask before choosing an analysis | 6 |
| Comments on the process | 7, lettered (a)–(g) |
| t-test form preferred | difference divided by its standard error |
| Chapter | 7, pages 75–92 |

## Related

- [[initial-data-analysis-ida]] — IDA supplies the model that the definitive analysis fits.
- [[six-guidelines-anaesthetic-case-statistical-problem-solving]] — Rule 4, the one-way ANOVA as first pass.
- [[chatfield1995-problem-solving-statisticians-guide]] — chapter 7, appendix A.5.

## Sources

- `_papers/chatfieldProblemSolvingStatisticians1995/chatfieldProblemSolvingStatisticians1995.md`
- `_papers/chatfieldProblemSolvingStatisticians1995/chatfieldProblemSolvingStatisticians1995-extracted.md`
