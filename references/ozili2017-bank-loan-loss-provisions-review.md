---
title: "Bank Loan Loss Provisions Research: A Review"
category: references
tags: [risk-modeling, accruals]
relationships:
  - target: "[[references/beatty2014-financial-accounting-in-banking]]"
    type: related_to
  - target: "[[references/pincus2007-accrual-anomaly-international-evidence]]"
    type: related_to
sources:
  - _papers/ozili2017bank/ozili2017bank-extracted.md
  - _papers/ozili2017bank/ozili2017bank.md
  - _papers/ozili2017bank/images/page_4_table_4.jpg
summary: >-
  Post-2000 review of bank loan loss provisioning: LLP discretion links to income smoothing, capital management, signalling and procyclicality across Basel regimes and country contexts.
provenance:
  extracted: 0.81
  inferred: 0.04
  ambiguous: 0.15
base_confidence: 0.67
lifecycle: draft
lifecycle_changed: 2026-10-26T09:12:06Z
tier: supporting
created: 2026-10-26T09:12:06Z
updated: 2026-10-30T17:41:00Z
---

# Bank Loan Loss Provisions Research: A Review

> [!tldr] The successor to Wall & Koch (2000): bank loan loss provisions are the most debated accounting number in bank reporting after 2008, and the core problem is that managerial discretion in LLP estimates is exploited for income smoothing, capital management, signalling and tax objectives, so regulators must limit that discretion.

## Problem & Motivation

Banks set aside loan loss provisions (LLPs) as a cushion to absorb expected losses on the loan portfolio. LLP attracts regulator and standard-setter attention for six reasons: large loan books make banks vulnerable to default-driven provisioning needs (Laeven & Majnoni, 2003); LLP is procyclical and worsened bank capital erosion at the 2008 crisis peak; LLP is a significant discretionary accrual managers exploit for opportunistic reporting (Wahlen, 1994); LLP is a micro-prudential surveillance tool; LLP signals the informativeness of bank accruals; LLP is the most debated accounting number in bank financial reporting after profitability and derivatives since 2008. The review complements Wall & Koch (2000); JEL classification G21, G28, E32, E44. Its empirical sibling, the accounting-in-banking synthesis [[references/beatty2014-financial-accounting-in-banking]], covers the same discretion and regulation streams from the financial-reporting side. The review states what it deliberately does not cover: Islamic banks (provisioning rules identical to conventional banks), dynamic provisioning (single-country bias: Spain, Chile, Peru, Uruguay), and discretionary LLP versus stock returns. Sidecar issue date is 2017-09, matching the accepted manuscript; the extracted text records receipt 25 January 2017, revision 22 May 2017, acceptance 26 May 2017, online 1 June 2017.

## Basel regimes and LLP treatment (Table 1)

| Item | Basel I | Basel II | Basel III |
| --- | --- | --- | --- |
| Dates | 1988; amendments 1995 (netting) and 1996 (market risk), implemented 1998 | Proposed 1999, revised 2001 & 2003, published 2004, implemented 2007, amended 2011 (Basel 2.5) | First published 2009, final 2010; through-the-cycle provisioning expected fully introduced June 2018 |
| LLP treatment | Reserves count as 1.25% of risk-weighted assets in Tier 2 capital; national regulators may exceed the 1.25% limit | IRB: expected losses fully covered by LLPs; EL > provisions deducted 50% from Tier 1 and 50% from Tier 2; EL < provisions recognised in Tier 2 up to 0.6% of risk-weighted assets; standardised approach reserves capped at 1.25% of risk-weighted assets | Expected through-the-cycle system: specific provisions on newly-originated loans from individual borrower characteristics; significant managerial discretion |
| Capital adequacy | 8% of risk-weighted assets; ≥ 50% (i.e. 4%) Tier 1; 2% common equity | 8% of risk-weighted assets under Pillar 1 (IRB, standardised, AMA); Pillars 2–3 supervision and market discipline | Tier 1 equity ≥ 4.5%, total Tier 1 6%; Tier 1/Tier 2 requirements as in Basel I/II; six regulations: capital definition, capital conservation buffer, countercyclical buffer, leverage ratio, liquidity ratio, countercyclical credit risk |
| Weaknesses | Fixed risk weights by borrower category; no default-correlation model; backward-looking, procyclical | Loose capital definition, insufficient credit-risk capital, no robust liquidity solution | Not yet fully implemented at time of writing |

Table 1: Basel regulation, LLP treatment and capital adequacy under Basel Accord.

![[_papers/ozili2017bank/images/page_4_table_4.jpg]]
Crop "page_4_table_4" from PDF page 4; the extracted markdown labels this table only as "Table 1", so the crop-to-table mapping is inferred from page order ^[ambiguous].

Basel I was criticised because fixed risk weights ignore borrower creditworthiness changes over the loan life, banks understate LLP when capital is low, and banks cut lending in bad times to conserve capital, transmitting extra procyclicality (Ahmed et al., 1999; Borio et al., 2001, pp. 1-57; Cavallo & Majnoni, 2002, pp. 319-342; Jackson et al., 1999; Bikker & Metzemakers, 2005). Basel II Pillar 1 design principle: bank capital covers unexpected losses, LLPs cover expected losses (Majnoni et al., 2004). Basel III improves on Basel II by requiring through-the-cycle specific provisions at loan origination, improving underlying data quality and PD/EL estimation.

## Three hypothesis streams

1. **Capital management hypothesis**: because general LLPs enter regulatory capital ratios, managers inflate LLPs when capital is adequate and deflate them toward the minimum (Ahmed et al., 1999; Moyer, 1990; Scholes et al., 1990). Kilic et al. (2012) and Bonin & Kosak (2013) offer the inverse view: absent minimum requirements, banks treat LLP as capital — overstating LLP when equity is low, understating when equity is sufficient. Evidence tests the negative relation between discretionary LLP and pre-LLP Tier 1/equity capital. Ahmed et al. (1999) examined 113 US banks, 1986-1995, and found banks manage minimum regulatory capital via LLP; overall evidence is mixed (Collins et al., 1995; Leventis et al., 2011; Curcio & Hasan, 2015).
2. **Signalling hypothesis**: abnormal LLPs signal loan-portfolio quality or future earnings; supported via positive relation between discretionary LLP and one-year-ahead earnings (Wahlen, 1994; Kanagaretnam et al., 2003, 2005; Eng & Nabar, 2007, for Hong Kong, Malaysia, Singapore 1993-2000: abnormal LLPs positively related to stock returns and future cash flows, investors bid prices up). Ahmed et al. (1999) found no support.
3. **Income smoothing hypothesis**: managers move LLPs to keep reported earnings stable (Greenawalt & Sinkey, 1988; Wahlen, 1994), the "saving for a rainy day" reading (Skala, 2015): high-earnings years bank provisions into reserves, low-earnings years draw them down. Tests relate discretionary LLP to pre-provision, pre-tax earnings.

## Procyclicality and the dynamic provisioning experiment

- Borio et al. (2001, pp. 1-57) find a strong negative LLP-business-cycle relation for 10 OECD countries; Beatty & Liao (2009) show banks delay LLPs until recession, reinforcing the current state; Agenor & Zilberman (2015) show backward-looking provisioning is procyclical because provisions are triggered by past-due payments; Olszak et al. (2016) find LLPs of large, public, commercial and consolidated-reporting banks are more procyclical, while stringent capital standards and better investor protection weaken procyclicality.
- Dynamic provisioning (higher LLPs in good times, lower in downturns): Spain compelled adoption in 2000; adopted in Spain, Peru, Columbia, Chile; Peru implemented its countercyclical provision rule in 2008. Post-adoption Spanish studies (De Lis et al., 2001; Perez et al., 2008; Saurina, 2009; Fillat & Montoriol-Garriga, 2010; Jiménez et al., 2012) show provisioning driven more by credit risk than smoothing or capital management. Chan-Lau (2012) for Chile: dynamic provisions enhance solvency but do not cut LLP procyclicality. Wezel (2010) for Uruguay: provisions stock accumulated since 2001 fully absorbs medium-sized shocks.
- Criticisms: research biased to Spain, Chile, Peru, Uruguay; buffer sustainability depends on crisis severity and lag; cycle transitions are hard to detect — "business cycle developments are hard to foresee, given their erratic duration and amplitude" (Bikker & Metzemakers, 2005, p. 144); dynamic provisions permit income/profit smoothing against financial transparency (FASB-IASB, 2009); open design questions: rule-based vs discretionary buffers, GDP vs credit supply vs loan-to-value as the trigger variable, and developed vs emerging country treatment.

## Cross-country evidence (samples and findings as reported)

| Country/region | Study | Sample | Finding |
| --- | --- | --- | --- |
| Netherlands | Norden & Stoian (2013) | 85 banks, 1998-2012 | LLP lowers earnings volatility; LLP rises when earnings are high, falls when regulatory capital ratios are low |
| Italy | Caporale et al. (2015) | 400 banks, 2001-2012 | Provisioning driven by non-discretionary components, especially 2008-2012; no income smoothing |
| Spain | Perez et al. (2008); Anandarajan et al. (2003) | Spanish banks; Basel I adoption 1992 | Dynamic system: smoothing yes, capital management no; post-1992 capital rules removed the constraint on earnings smoothing |
| China | Wu et al. (2015); Curcio et al. (2014) | 102 banks, 2006-2011 | Banks with more foreign strategic investors smooth earnings via LLP; smoothing yes, capital management no; listed banks smooth less than unlisted |
| Nigeria | Ozili (2015) | Listed banks, 2004-2013 | Smoothing and capital management during voluntary IFRS adoption; weak signalling evidence |
| UK | Pain (2003) | Major UK banks panel | Real GDP growth, real interest rates, lagged aggregate lending growth drive LLP |
| Philippines | Floro (2010) | Philippine banks | Capital management via LLP; fewer LLP in expansion, higher in downturn |
| Vietnam | Bryce et al. (2015) | Vietnamese banks | No evidence of LLP-based smoothing |
| Turkey | Acar & Ipci (2015) | 28 commercial banks, 2005-2011 | Income smoothing, reduced during 2007-2009; LLP signals future prospects |
| Hong Kong | Abdul Adzis et al. (2016) | HK banks | Smoothing reduced after IAS 39 adoption |
| US | El Sood (2012) | 878 banks, 2001-2009 | LLP accelerated to smooth earnings when hitting regulatory capital minimum, in non-recession, when more profitable; smoothing upward during the crisis |
| US | Balboa et al. (2013) | 15,268 banks, 1996-2011 | Smoothing when pre-provision earnings positive and substantial; non-linear LLP-earnings relation via dynamic panel |
| US | Kilic et al. (2012) | US banks, SFAS 133 | LLP smoothing increased after derivatives smoothing was blocked by disclosure rules |
| MENA | Elnahass et al. (2014), 2006-2011; Othman & Mersni (2014); Taktak et al. (2010); Farook et al. (2014); Quttainah et al. (2013); Soedarmono et al. (2017) | Islamic vs conventional banks | LLP value-relevant in both sectors; Islamic-bank discretionary component valued lower; Islamic banks use LLP for earnings and capital management; Islamic banks have lower LLP; less earnings management, no Shariah-Board difference; Islamic LLP procyclical, capital management offsets it. Taktak et al. (2010) is reported as smoothing in §3.2.3 and as no evidence of smoothing in §5.2.2 ^[ambiguous] |
| Africa | Ozili (2017a); Amidu & Kuipo (2015) | African banks | Smoothing confirmed; listed banks smooth more; Big-4 auditor does not reduce smoothing; LLP procyclical |
| Europe | Leventis et al. (2011) | 91 listed IFRS banks | Smoothing by early and late adopters, reduced after IFRS adoption |
| Europe | Curcio & Hasan (2015) | Euro / non-Euro credit institutions, 1996-2006 | Non-Euro Area smooth earnings; Euro Area evidence not found |
| Europe | Skala (2015); Bouvatier et al. (2014); Ozili (2017b); Bonin & Kosak (2013); Curcio et al. (2017) | Central Europe; EU banks; 11 emerging European countries; EBA stress tests | Rainy-day smoothing at high earnings; concentrated-ownership banks smooth; LLP driven by credit risk and smoothing; emerging Europe smooths; smoothing only for the 2011 EBA exercise |
| Australia/Asia | Anandarajan et al. (2007); Cummings & Durrani (2016); Eng & Nabar (2007); Packer & Zhu (2012) | Australian public banks; two regimes; 3 Asian countries 1993-2000; 240 banks from 12 countries 2000-2009 | Aggressive post-Basel smoothing; regulatory forward-looking vs accounting incurred-loss regimes; abnormal LLP signals cash flows; smoothing plus countercyclical provisioning, notably India |
| International | Cavallo & Majnoni (2002) | 1176 banks 1988-1999, 804 G10 + 372 non-G10 | Smoothing among G10 banks, not non-G10 |
| International | Fonseca & Gonzalez (2008); Kar (2015); Bushman & Williams (2012) | 41 countries; 1294 MFIs, 103 countries, 1996-2013; 27 countries | Income smoothing confirmed; MFIs smooth and are procyclical; forward-looking provisioning exploited to smooth earnings |

## Ethics and factors behind income smoothing

Income smoothing via LLP violates no rule outright — it arises from discretion permitted by both accounting and prudential regimes — so the verdict turns on motive. Ethical motives: rainy-day saving, job protection (DeFond & Park, 1997), reducing owner-manager information asymmetry, stability via smoothing earnings volatility, improving bondholder/supervisor risk perception. Unethical motives: bonus extraction (Healy, 1985), reducing earnings informativeness, increasing reporting opacity, lowering earnings quality, avoiding shareholder interference/tax, fixed dividend payout management.

Eight drivers: (1) capital markets prefer lower earnings-variability and return volatility; (2) avoiding scrutiny of excessive profits by regulators and politicians (Burgstahler & Dichev, 1997); (3) regulatory arbitrage; (4) accounting regime — Ashraf et al. (2014) examined 7343 banks from 118 countries, 1999-2010, and found rule-based regimes show higher smoothing than principles-based; (5) corruption via non-transparent reporting; (6) competition — smoothing lowers cost of capital by reducing information asymmetry (Francis et al., 2004), competitive firms smooth more (Marciukaityte & Park, 2009); (7) transient events — smoothing in the 1990 US boom (Liu & Ryan, 2006); (8) national culture — banks in high-individualism, high power-distance, low uncertainty-avoidance societies report smoother earnings via LLP, and high risk-taking cultures suffered larger crisis losses (Kanagaretnam et al., 2011).

Six constraints: (1) strict disclosure rules (income smoothing fell after IFRS adoption; Balla & Rose (2015) found the 1998 SEC constraint weakened LLP-earnings links for publicly-held banks, not private ones; IAS 39 reduced Hong Kong smoothing); (2) religiosity — negatively related to earnings smoothing (Kanagaretnam et al., 2015); (3) audit quality — Big-4 auditors reduce smoothing (Kanagaretnam et al., 2010; DeAngelo, 1981), contradicting the African result ^[ambiguous]; (4) investor protection — smoothing falls with stronger protection, minority-shareholder protection matters, legal enforcement quality does not (Fonseca & Gonzalez, 2008; Shen & Chih, 2005); (5) ownership structure — concentrated ownership associates with low earnings informativeness (Fan & Wong, 2002, 977 companies, 7 East Asian economies), dispersed-ownership industrial firms manage earnings less (Leuz et al., 2003), while for EU banks Gebhardt & Novotny-Farkas (2011) report smoothing pronounced among widely-held listed banks whereas Bouvatier et al. (2014) report smoothing reduced among dispersed-ownership banks ^[ambiguous]; (6) strong banking supervision reduces smoothing.

## Methodology

Baseline model: `Discretionary Provisions = f(non-discretionary provisions, bank-specific factors, institutional factors, country/regional factors)`; the regression form follows the research objective. Econometric practice: pooled/panel, fixed/random effects, static/dynamic panels, system and difference GMM. Data sources: Bankscope (now discontinued), Fitch, Compustat, bank financial statements, confidential databases, regulator data, Datastream, Thomson One Banker, World Bank. LLP proxies show low construct-validity problems relative to general accruals research (DeFond, 2010; Dechow et al., 2010). Control variables: real GDP growth, minority shareholder rights, religiosity, legal systems, banking supervision, inflation, disclosure regulation, monetary policy rate, political economy. The open methodological issue is the deflator — total assets, beginning total assets, beginning total loans, gross/average loans all appear, with no consensus; the paper recommends normalising LLP and total assets with natural logarithms to handle bank-size skew. Cross-country comparability is limited because LLP is a function of unobservable accounting systems, assumptions and managerial choices.

## Challenges

- **Two conflicting provisioning models**: IFRS incurred-loss (lower LLP) versus Basel expected-credit-loss (higher LLP); managers can choose the model to shift earnings. IFRS 9 expected-credit-loss model was slated for 2018, recognising 12-month expected credit losses in stage 1 and lifetime expected losses in stage 2 after significant increases in credit risk (Gaston & Song, 2014, p. 11). Forward-looking provisioning gives managers a licence for speculative provisioning (Bushman & Williams, 2012).
- **Paucity of critical studies**: LLP research is result-driven; few studies challenge proxies and assumptions.
- **Qualitative methods are rare**: among the first 50 peer-reviewed LLP articles sampled at random from Google Scholar, 2012-2016, at least one qualitative study existed (Balasubramanyan et al., 2013, using the Senior Loan Officer Opinion Survey).
- **Political cost argument**: banks may smooth to avoid scrutiny of excessive profits or losses; political cost and income smoothing explanations are not mutually exclusive.

## Future directions

Sensitivity of abnormal LLP changes in equity response to specific versus general provisions; persistence of abnormal LLP around CEO exit; country-specific interventions inducing LLP procyclicality in emerging markets (government loan guarantees); dynamic vs transparent LLP balance (dual "IFRS provisions + regulatory provisions" reporting vs full replacement of incurred loss with expected credit loss); Basel III effects on provisioning discretion; LLP behaviour of systemic versus non-systemic institutions (large SIFIs' LLPs are more procyclical, Olszak et al., 2016); overlapping motivations (signalling and smoothing can only be pursued one at a time); supervision design for dynamic provisioning; regional blocs as stabilisers (OPEC, OECD, NAFTA, G8, Eurozone, EU, BRIC, ASEAN, G20, Latin American and Caribbean).

## Conclusion

Four survey findings: LLP studies have moved from narrow country studies to macro, accounting, cultural, prudential and institutional interactions; the LLP-business-cycle link for micro-prudential policy depends on the regulatory treatment of LLP, and granting banks discretion over LLP build-up and release can produce countercyclical effects regulators want; a sufficient-versus-transparent LLP compromise is achievable between standard setters and regulators; banks across countries use LLP discretion in ways that do not reflect their true financial condition. Provisioning models are only as good as their assumptions and inputs, so the standing recommendation is to limit managerial discretion — regulators must watch how much discretion lending institutions have over reported provision estimates.

## Limitations

Self-declared scope exclusions: Islamic bank provisioning, dynamic provisioning depth, and LLP-stock-return links. As a secondary review, every reported sample size and finding is the review's reading of the cited studies, not original estimation. The paper itself reports contradictory characterisations of Taktak et al. (2010) and of the ownership-structure literature, flagged above. ^[inferred]

## Related

- [[references/beatty2014-financial-accounting-in-banking]] — companion empirical review of bank accounting discretion and regulation (related_to)
- [[references/pincus2007-accrual-anomaly-international-evidence]] — cross-country accrual-quality evidence, the international analogue of the LLP cross-country studies (related_to)

## Sources

- `_papers/ozili2017bank/ozili2017bank-extracted.md` — full-text extraction, 571 lines
- `_papers/ozili2017bank/ozili2017bank.md` — Zotero sidecar (title, authors, journal, DOI 10.1016/j.bir.2017.05.001)
- `_papers/ozili2017bank/images/page_4_table_4.jpg` — table crop from PDF page 4, embedded above
