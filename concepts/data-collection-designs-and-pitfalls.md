---
title: "Collecting data: designs, sample size, and the pitfalls Chatfield's six examples teach"
summary: "Chatfield ch4: active intervention, blocking, Puerto Rico surname sample, pseudo-replication, the stroke design."
tags: [data-collection, experimental-design, sample-survey, randomization, confounding, pseudo-replication, clinical-trials, sample-size, chatfield]
provenance:
  extracted: 0.90
  inferred: 0.08
  ambiguous: 0.02
base_confidence: 0.67
tier: supporting
category: concepts
created: 2026-11-05T14:24:00Z
updated: 2026-11-05T14:24:00Z
sources:
  - _papers/chatfieldProblemSolvingStatisticians1995/chatfieldProblemSolvingStatisticians1995.md
  - _papers/chatfieldProblemSolvingStatisticians1995/chatfieldProblemSolvingStatisticians1995-extracted.md
relationships:
  - target: "[[chatfield1995-problem-solving-statisticians-guide]]"
    type: related_to
  - target: "[[six-guidelines-anaesthetic-case-statistical-problem-solving]]"
    type: related_to
  - target: "[[initial-data-analysis-ida]]"
    type: related_to
lifecycle: draft
lifecycle_changed: 2026-11-05T14:24:00Z
---

> [!tldr] "Data collection is as much a part of statistics as data analysis" and "do not trust any data that you did not collect yourself" — the two closing key messages of chapter 4.^[extracted]

## Summary

Chatfield distinguishes data collected in designed experiments (including clinical trials), sample surveys, pure observational studies, and more specialist investigations such as controlled prospective and retrospective studies. Whatever the method, the investigator must formulate objectives, decide which variables to measure and to what accuracy, and specify the procedure for collecting data, including sample size, the method of randomization, and how the data are recorded.^[extracted]

The distinction in spirit is the point: "Experiments require active intervention by the investigator, for example in deciding how to allocate treatments to experimental units. A clear interpretation of any differences which arise should then be possible. In contrast, as the name suggests, the investigator is generally more passive in observational studies and simply observes what is going on." Sample surveys draw a representative sample from a well-defined population, usually by randomization or by quota sampling, and are "essentially observational in character", so they share the same drawback, namely that it may be dangerous to interpret interesting-looking effects, particularly as regards cause and effect. Properly constructed observational studies can be useful pointers for later studies, "but they can sometimes be worthless or even positively misleading."^[extracted]

## Key ideas

- **Objectives drive the design.** The designs needed to pick out important variables (screening designs such as fractional factorials) are quite different from those modelling a response surface over a wide area or choosing values of explanatory variables to maximize a response. Some analysts want to maximize a mean response; for others, reducing variability is the prime interest. In surveys, required precision may be critical.^[extracted]
- **The parallels and the cautions.** "The distinctions between the different types of data collection are not always clear-cut and there are many parallels between the basic concepts of design and survey sampling (e.g. compare blocking and stratification)."^[extracted]
- **Management is neglected.** "Generally speaking, insufficient attention is given to the management of studies. Factors such as the order in which observations are taken, the effect of time of day, and the use of different observers can have substantial unforeseen effects." Some plans can be specified exactly in advance; others sensibly become iterative (Box, 1994) as exploration proceeds, and a variable thought unimportant at the start may become key.^[extracted]
- **Example 4.1, an observational study.** Data on seven treatments for child ear infections, from all 400+ children attending a local hospital over six months. Large differences in reinfection rates are a useful indication that some treatments are better. But doctors allocated the treatment they liked best, so results need caution: "Some doctors always used the same treatment and then the effect of the treatment is confounded with (i.e. cannot be distinguished from) the effect of the doctor. Good results may indicate a good doctor, not a good treatment." Other doctors gave particular treatments to the worst-affected patients. Only a proper clinical trial with random allocation can settle it; "historical data like these are better than nothing, and observational studies can be a useful cost-effective preliminary to a proper experiment."^[extracted]
- **Retrospective versus prospective.** In controlled retrospective trials a response is observed on carefully selected individuals and their history is examined to assess which variables determine the condition of interest; it is "generally safer, but takes much longer" to use a controlled prospective trial in which individuals are chosen by the investigator and followed through time. The general term longitudinal data describes data collected on the same units on several occasions over time (Plewis, 1985).^[extracted]
- **Sample-size guidance.** A sample size of about 20 is "usually a working minimum" for measured variables; binary success/failure variables need much larger samples — spotting a 10 % increase in the proportion of patients responding to a new treatment with 80 % power requires several hundred.^[extracted] The standard formulae (significance usually 5 %, power 80-90 %) are available for prespecified changes in a mean or proportion, "and in my experience these formulae are often used after the data have been collected in order to try and explain why a result was not significant!"^[extracted]
- **Large is not better.** "Many people think 'the larger the better', not realizing that a large, but poorly administered, and hence messy, sample may actually contain less information than a smaller, but carefully controlled, sample."^[extracted] Over-ambitious example: a study comparing several methods of treating elderly stroke patients, with four types of hospital, four types of specialty, five types of ward, and year variation, all with a maximum of 240 patients — a size that sounds large but gives very small numbers in each cross-classified category.^[extracted]
- **The anecdotal reality of fieldwork.** "Try selecting a 'random' live pig from a crowded pigsty and weighing it on a balance! Or try getting a quota sample to answer questions on some sensitive political topic. Refusal to cooperate and deliberate lies become a real problem." One interviewer confessed that the only way to get people to answer was to stand next to a photo booth in a railway station, giving a biased sample even when quotas were satisfied.^[extracted]
- **Knowing the limitations helps the analysis.** A pregnant woman's routine check at hospital: kept waiting three hours, found to have abnormally high blood pressure, admitted; subsequent tests showed she was quite normal and that the stress of waiting had induced the abnormally high reading.^[extracted]
- **Non-sampling errors.** For sample surveys, non-sampling errors such as non-response are "at least as important as sampling errors". The literature's optimal sampling schemes minimize variance subject to a cost constraint but ignore the multipurpose, multivariate nature of most surveys and disregard non-sampling errors. The adjective *proximum* has been suggested for a design that aspires to approximate optimality while taking account of robustness, administrative convenience and cost.^[extracted]
- **The two survey failings.** Selecting an unrepresentative sample (judgement or convenience sample, or an inadequate frame) and asking silly questions (careful questionnaire design, not too many questions, fair, concise and clear wording; a pilot survey is vital). The other main sources of non-sampling error are non-response and measurement errors, including interviewer bias, recording errors, and respondents giving incorrect information deliberately or unwittingly.^[extracted]
- **Example 4.2, unrepresentative samples.** Puerto Rico: the US government based its grant aid on the total of the first 100 hurricane-claim applications multiplied by 100, where small claims arrive first because they need less preparation. A company's "random" sample of clients was everyone whose surname began with V, on the mistaken assumption that alphabetical order is random, which effectively excluded all Scottish and Welsh surnames. A 1-in-20 systematic sample of 20,000+ customers missed a part of Britain because one of the separate data tapes was missed in producing the sample.^[extracted]
- **Randomization is the most common failing.** It is needed to eliminate nuisance factors and applies both to the allocation of experimental units and to the order in which observations are taken. In regression experiments, recording observations sequentially in the same order as increasing explanatory values confounds the time effect with the explanatory effect. If randomization is left to a client it is often carried out incorrectly, so the protocol should spell out exactly how to do it.^[extracted]
- **Example 4.3, faulty designs.** A forestry experiment on sloping land in Africa whose design "had been designed in Rome"; the field plan should have been resolved on the spot. A field worker read the plan from the wrong end on the second occasion, so treatment combinations differed from plan. A fungicide factorial on planks of wood (treated/untreated, side/ends, Mississippi/Wisconsin, month) found a large treatment effect in Wisconsin but not Mississippi, because in Mississippi the treated planks had been stacked on top of the untreated ones, so rain carried the fungicide down.^[extracted]
- **Example 4.4, a suspect recording procedure.** A composite factorial experiment on the conductivity of copper sulphate solution (CuSO4 concentration, H2SO4 concentration, temperature) explained only about 10 % of the variation, against an expected almost perfect fit. Observing the technician revealed the probe touching the side or bottom of the beaker, insufficient immersion depth, and readings taken before the digital readout settled (about 15 seconds for diffusion through the membrane). Two fixes — clamp the probe to a fixed depth, read after 30 seconds — and a one-hour repeat gave R² = 0.99. Chatfield's point: the recommendations are technological in appearance, and he takes a wider view of the statistician's responsibilities as including good scientific method in general, citing G.E.P. Box's exhortation to "strive to earn the title of first class scientist".^[extracted]
- **Example 4.5, pseudo-replication.** Eight net-bags of leaves placed at the same location at 1 m depth and retrieved after one month gives eight replicates in name only: "you have no information about how decomposition varies from one spot to another at 1 m depth. The observations are not independent and no generalization is possible." The problem is harder to spot comparing eight bags at one location and depth with eight at another location and depth. Put another way, what is the treatment? (Hurlbert, 1984, for the term.)^[extracted]
- **Example 4.6, official statistics.** A prominent British politician (Healey, 1980) appointed "railway checker" at a large station during the Second World War counted servicemen boarding and leaving — as a convalescent with eight platforms in blackout conditions he made up all the figures, then asked ticket collectors for numbers, which were also invented. The moral: a sensible balance between effort collecting data and analysing them, and care in specifying exactly what is worth recording and how. Chatfield adds (writing in 1994) the explosion of data collection by UK hospital managers, so that nurses and doctors spend a high proportion of time completing poorly designed forms, much of the information of dubious quality and some never used.^[extracted]
- **Clinical trials and perversity.** Andersen (1990) devotes a book to flawed experiments. Two types of people are involved in drug trials on humans, doctors and patients, "and both groups can act perversely in such a way as to ruin the design": a doctor may ignore the protocol and allocate the treatment he believes is best, a patient may not take the drug as directed.^[extracted]
- **Screening versus single-treatment design.** An agricultural research station may screen as many as 10,000 new products a year, of which about 1,000 go to secondary and 100 to tertiary testing, after which statutory tests for efficacy, toxicology, and environmental soundness remain, and the number launched is in single figures or even zero.^[extracted]
- **The summary checklists.** For sample surveys: the sample is representative and of suitable size; questions are fair, clear, concise, tested in a pilot; non-sampling errors such as interviewer bias, non-response and measurement error are reduced; data are coded and processed accurately. For experimental designs: randomization is used properly; it is possible to find estimates of all effects of interest, including important interactions, and give them a unique interpretation, which was not possible in Examples 4.1 and 4.5.^[extracted]
- **The contribution of being involved early.** A statistician involved at the start, who advises on data collection and knows the background and objectives, makes a much more satisfying contribution than one called in later. When data are collected haphazardly, the analyst asked to analyse them should closely scrutinise the data-collection procedure, which determines whether it is worth spending much effort on the analysis.^[extracted]

## Key numbers

| Item | Value |
| --- | --- |
| Ear-infection study (Example 4.1) | 400+ children, 7 treatments, six months |
| Stroke-study design (4.2 sample-size discussion) | 240 patients max, 4 hospital types, 4 specialties, 5 ward types, year variation |
| Working minimum for measured variables | about 20 observations |
| 10 % increase in response proportion, 80 % power | several hundred patients |
| Conductivity experiment after fixes | R² = 0.99, experiment repeated in under one hour |
| Agricultural screening | 10,000 screened, ~1,000 secondary, 100 tertiary, launches in single figures |
| Significance / power convention | 5 % significance, 80-90 % power |

## Related

- [[chatfield1995-problem-solving-statisticians-guide]] — the book's structure.
- [[six-guidelines-anaesthetic-case-statistical-problem-solving]] — Rule 2, find out how the data were collected.
- [[initial-data-analysis-ida]] — data scrutiny as the first part of IDA.
