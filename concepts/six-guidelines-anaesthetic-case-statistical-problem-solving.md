---
title: "Chatfield's six guidelines for statistical problem solving, with the anaesthetic case"
summary: "The Preface six Rules: define the problem, data collection, objectives, IDA, procedure class, presentation."
tags: [operations-research]
provenance:
  extracted: 0.90
  inferred: 0.08
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
  - target: "[[references/chatfield1995-problem-solving-statisticians-guide]]"
    type: related_to
  - target: "[[concepts/data-collection-designs-and-pitfalls]]"
    type: related_to
  - target: "[[concepts/initial-data-analysis-ida]]"
    type: related_to
  - target: "[[concepts/definitive-analysis-procedure-choice]]"
    type: related_to
  - target: "[[concepts/effective-statistician-eight-principles]]"
    type: related_to
  - target: "[[concepts/problem-formulation-objectives-type-iii-error]]"
    type: related_to
lifecycle: draft
lifecycle_changed: 2026-10-30T09:28:40Z
---

> [!tldr] A doctor's telephone call is the whole Prelude: 31 variables measured on 80 surgical patients, four anaesthetic groups, and the question "How should the data be analysed?". Chatfield answers with six general rules, the first of which is to understand what is being measured and why before touching the data.^[extracted]

## Summary

The Prelude is Chatfield's argument that textbook examples are "over-simplified and rather artificial" and that a real problem arrives as a messy data set. The six rules are the book's operating procedure, amplified in Part One, while Part Two gives the worked exercises that illustrate them.^[extracted]

The six rules are: **Rule 1** "Do not attempt to analyse the data until you understand what is being measured and why. Find out whether there is any prior information about likely effects"; **Rule 2** "Find out how the data were collected"; **Rule 3** "Look at the structure of the data"; **Rule 4** "The data then need to be carefully examined in an exploratory way, before attempting a more sophisticated analysis"; **Rule 5** "Use your common sense at all times"; **Rule 6** "Report the results in a clear, self-explanatory way".^[extracted]

## Key ideas

- **The setting.** A doctor at a local hospital has data comparing the effects of four anaesthetic drugs and wants help. The statistician is assured "it won't take long (of course it does! but statisticians must be willing to respond to genuine requests for help)".^[extracted] The data are 31 variables for each of 80 patients undergoing surgery for conditions such as appendicitis.^[extracted]
- **The symbol key (Rule 1 output).** A question mark denotes a missing observation; a slash denotes NO or NONE (no vapour inhaled by patient 3); the group code A, B, C, D denotes the anaesthetic administered; T1 is time in minutes from reversal of anaesthetic till the eyes open, T2 time to first breath, T3 time till discharge from the operating theatre; overall condition after the operation is rated 1 (very good) to 4 (awful).^[extracted]
- **Prior information matters.** "The doctor was unaware of any previous experiments to compare the four anaesthetics and wanted the data analysed as a 'one-off' sample. It seems unlikely that the prior information was so meagre and this point may be worth pursuing if the results are inconclusive."^[extracted]
- **Randomization determines what is justifiable.** If patients were not allocated randomly to the four groups, "a simple descriptive analysis may be all that can be justified" (Rule 2).^[extracted]
- **Variable elimination.** 20 patients in each of the four groups is enough for a comparison; the number of variables is high, so they should not all be considered at once, and variables should be eliminated in consultation with the doctor. "T1 and T2 were usually identical and are essentially measuring the same thing. One of them should be excluded."^[extracted]
- **The three variable categories.** Demographic variables (age) describe each patient; controlled variables (type of vapour) are under the control of hospital staff; response variables (condition) measure how the patient responds to the operation. Variables are also classified by measurement type: continuous, discrete, qualitative, binary. "The ensuing analysis depends critically on the data structure."^[extracted]
- **The exploratory order (Rule 4).** First the demographic variables: are the groups reasonably comparable? Significance tests should be avoided here because there are several variables and the overall comparison is what is of interest. Second the controlled variables (same surgeon and anaesthetist? different strategies in different groups?). Third the response variables, examined one at a time, with a one-way ANOVA as a helpful first pass. The instruction is to avoid over-concern with significance and the size of P-values at this stage.^[extracted]
- **The criterion for judging differences.** With several variables, different operations, and doubts about randomization, "it is more important to see if any differences between groups are of practical importance and to see if this fits in with any prior knowledge."^[extracted]
- **The four-phase brief summary** ("How to tackle statistical problems", p. xiii): Understanding the problem (What are the objectives? What background information is available? Can you formulate the problem in statistical terms? Ask Questions); Collecting the data (Have the data already been collected? If so, how? If not, should an experimental design, sample survey, observational study, or what, be used? How will randomization be involved?); Analysing the data (process the data, check quality, carry out an IDA, ask whether the conclusions are then obvious, and whether the formal method was specified beforehand); Presenting the results (Are the conclusions what you expected? Plan the structure of your report carefully. Revise it several times. Ask a friend to read it before you hand it over).^[extracted]
- The "Analysing the data" phase checklist extends to: have you tackled a similar problem before, can you restate or solve part of the problem, is there prior information about a sensible model, would the analysis be easier with transformations, try more than one analysis if unsure (with or without an outlier, parametric or non-parametric) and check whether the results are qualitatively different; ask for help; check any fitted model with a residual analysis and by replicating the results where possible.^[extracted]

## Table P.1 (the printed extract)

| Row | 3 | 5 | 14 | 27 | 42 |
| --- | --- | --- | --- | --- | --- |
| Group | A | B | D | A | C |
| Sex | M | F | F | F | F |
| Age | 38 | 38 | 42 | 41 | 54 |
| Operation | RIH | Mastectomy | TAH | Laparotomy | Appendix |
| Premed time | ? | ? | 116 | 90 | 59 |
| Vapour | / | / | / | HAL | / |
| T1 | 3 | 4 | 3 | 10 | 1 |
| T2 | 3 | 4 | 3 | 10 | 1 |
| T3 | 48 | ? | 110 | 108 | 38 |
| Antiemetic | ? | 200 | 25 | 60 | / |
| Condition | 2 | 2 | 1 | 3 | 1 |

Values as printed in Table P.1 (line 237).^[extracted]

## Related

- [[chatfield1995-problem-solving-statisticians-guide]] — the book, its structure and its Preface.
- [[data-collection-designs-and-pitfalls]] — Rule 2 in chapter 4.
- [[initial-data-analysis-ida]] — Rule 4 as the IDA of chapters 5-6.

## Sources

- `_papers/chatfieldProblemSolvingStatisticians1995/chatfieldProblemSolvingStatisticians1995.md`
- `_papers/chatfieldProblemSolvingStatisticians1995/chatfieldProblemSolvingStatisticians1995-extracted.md`
