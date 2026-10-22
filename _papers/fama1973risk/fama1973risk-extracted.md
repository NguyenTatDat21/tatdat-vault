Eugene F. Fama; James D. MacBeth

The Journal of Political Economy, Vol. 81, No. 3 (May - Jun., 1973), 607-636.

Stable URL:

http://links.jstor.org/sici?sici=0022-3808%28197305%2F06%2981%3A3%3C607%3ARRAEET%3E2.0.CO%3B2-J

The Journal of Political Economy is currently published by The University of Chicago Press.

Your use of the JSTOR archive indicates your acceptance of JSTOR's Terms and Conditions of Use, available at http://www.jstor.org/about/terms.html. JSTOR's Terms and Conditions of Use provides, in part, that unless you have obtained prior permission, you may not download an entire issue of a journal or multiple copies of articles, and you may use content in the JSTOR archive only for your personal, non-commercial use.

Please contact the publisher regarding any further use of this work. Publisher contact information may be obtained at http://www.jstor.org/journals/ucpress.html.

Each copy of any part of a JSTOR transmission must contain the same copyright notice that appears on the screen or printed page of such transmission.

# Risk, Return, and Equilibrium: Empirical Tests

Eugene F. Fama and James D. MacBeth

University of Chicago

This paper tests the relationship between average return and risk for New York Stock Exchange common stocks. The theoretical basis of the tests is the “two-parameter” portfolio model and models of market equilibrium derived from the two-parameter portfolio model. We cannot reject the hypothesis of these models that the pricing of common stocks reflects the attempts of risk-averse investors to hold portfolios that are “efficient” in terms of expected value and dispersion of return. Moreover, the observed “fair game” properties of the coefficients and residuals of the risk-return regressions are consistent with an “efficient capital market”—that is, a market where prices of securities fully reflect available information.

## I. Theoretical Background

In the two-parameter portfolio model of Tobin (1958), Markowitz (1959), and Fama (1965b), the capital market is assumed to be perfect in the sense that investors are price takers and there are neither transactions costs nor information costs. Distributions of one-period percentage returns on all assets and portfolios are assumed to be normal or to conform to some other two-parameter member of the symmetric stable class. Investors are assumed to be risk averse and to behave as if they choose among portfolios on the basis of maximum expected utility. A perfect capital market, investor risk aversion, and two-parameter return distributions imply the important “efficient set theorem”: The optimal portfolio for any investor must be efficient in the sense that no other portfolio with the same or higher expected return has lower dispersion of return. $^{1}$

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">Received August 24, 1971. Final version received for publication September 2, 1972. Research supported by a grant from the National Science Foundation. The comments of Professors F. Black, L. Fisher, N. Gonedes, M. Jensen, M. Miller, R. Officer, H. Roberts, R. Roll, and M. Scholes are gratefully acknowledged. A special note of thanks is due to Black, Jensen, and Officer.</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$^{1}$  Although the choice of dispersion parameter is arbitrary, the standard deviation</span></small>

In the portfolio model the investor looks at individual assets only in terms of their contributions to the expected value and dispersion, or risk, of his portfolio return. With normal return distributions the risk of portfolio p is measured by the standard deviation,  $\sigma(\widetilde{R}_{p})$ , of its return,  $\widetilde{R}_{p}$ , and the risk of an asset for an investor who holds p is the contribution of the asset to  $\sigma(\widetilde{R}_{p})$ . If  $x_{ip}$  is the proportion of portfolio funds invested in asset i,  $\sigma_{ij} = \text{cov}(\widetilde{R}_{i}, \widetilde{R}_{j})$  is the covariance between the returns on assets i and j, and N is the number of assets, then

$$
\sigma (\tilde {R} _ {p}) = \sum_ {i = 1} ^ {N} x _ {i p} \left[ \frac {\sum_ {j = 1} ^ {N} x _ {j p} \sigma_ {i j}}{\sigma (\tilde {R} _ {p})} \right] = \sum_ {i = 1} ^ {N} x _ {i p} \frac {\operatorname{cov} \left(\tilde {R} _ {i} , \tilde {R} _ {p}\right)}{\sigma (\tilde {R} _ {p})}.
$$

Thus, the contribution of asset $i$ to $\sigma(\widetilde{R}_p)$—that is, the risk of asset $i$ in the portfolio $p$—is proportional to

$$
\sum_ {j = 1} ^ {N} x _ {j p} \sigma_ {i j} / \sigma (\tilde {R} _ {p}) = \mathrm{cov} (\tilde {R} _ {i}, \tilde {R} _ {p}) / \sigma (\tilde {R} _ {p}).
$$

Note that since the weights $x_{jp}$ vary from portfolio to portfolio, the risk of an asset is different for different portfolios.

For an individual investor the relationship between the risk of an asset and its expected return is implied by the fact that the investor's optimal portfolio is efficient. Thus, if he chooses the portfolio $m$, the fact that $m$ is efficient means that the weights $x_{im}, i = 1, 2, \ldots, N$, maximize expected portfolio return

$$
E (\widetilde {R} _ {m}) = \sum_ {i = 1} ^ {N} x _ {i m} E (\widetilde {R} _ {i}),
$$

subject to the constraints

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">is common when return distributions are assumed to be normal, whereas an interfractile range is usually suggested when returns are generated from some other symmetric stable distribution.</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">It is well known that the mean-standard deviation version of the two-parameter portfolio model can be derived from the assumption that investors have quadratic utility functions. But the problems with this approach are also well known. In any case, the empirical evidence of Fama (1965a), Blume (1970), Roll (1970), K. Miller (1971), and Officer (1971) provides support for the “distribution” approach to the model. For a discussion of the issues and a detailed treatment of the two-parameter model, see Fama and Miller (1972, chaps. 6–8).</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">We also concentrate on the special case of the two-parameter model obtained with the assumption of normally distributed returns. As shown in Fama (1971) or Fama and Miller (1972, chap. 7), the important testable implications of the general symmetric stable model are the same as those of the normal model.</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$^{2}$  Tildes ( $\sim$ ) are used to denote random variables. And the one-period percentage return is most often referred to just as the return.</span></small>

$$
\sigma (\widetilde {R} _ {p}) = \sigma (\widetilde {R} _ {m}) \quad \text {and} \quad \sum_ {i = 1} ^ {N} x _ {i m} = 1.
$$

Lagrangian methods can then be used to show that the weights $x_{jm}$ must be chosen in such a way that for any asset $i$ in $m$

$$
\left| E (\widetilde {R} _ {i}) - E (\widetilde {R} _ {m}) = S _ {m} \left[ \frac {\sum_ {j = 1} ^ {N} x _ {j m} \sigma_ {i j}}{\sigma (\widetilde {R} _ {m})} - \sigma (\widetilde {R} _ {m}) \right], \right.\tag{1}
$$

where  $S_{m}$  is the rate of change of  $E(\widetilde{R}_{p})$  with respect to a change in  $\sigma(\widetilde{R}_{p})$  at the point on the efficient set corresponding to portfolio m. If there are nonnegativity constraints on the weights (that is, if short selling is prohibited), then (1) only holds for assets i such that  $x_{im} > 0$ .

Although equation (1) is just a condition on the weights  $x_{jm}$  that is required for portfolio efficiency, it can be interpreted as the relationship between the risk of asset i in portfolio m and the expected return on the asset. The equation says that the difference between the expected return on the asset and the expected return on the portfolio is proportional to the difference between the risk of the asset and the risk of the portfolio. The proportionality factor is  $S_{m}$ , the slope of the efficient set at the point corresponding to the portfolio m. And the risk of the asset is its contribution to total portfolio risk,  $\sigma(\widetilde{R}_{m})$ .

## II. Testable Implications

Suppose now that we posit a market of risk-averse investors who make portfolio decisions period by period according to the two-parameter model.$^{3}$ We are concerned with determining what this implies for observable properties of security and portfolio returns. We consider two categories of implications. First, there are conditions on expected returns that are implied by the fact that in a two-parameter world investors hold efficient portfolios. Second, there are conditions on the behavior of returns through time that are implied by the assumption of the two-parameter model that the capital market is perfect or frictionless in the sense that there are neither transactions costs nor information costs.

## A. Expected Returns

The implications of the two-parameter model for expected returns derive from the efficiency condition or expected return-risk relationship of equation (1). First, it is convenient to rewrite (1) as

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$^{3}$  A multiperiod version of the two-parameter model is in Fama (1970a) or Fama and Miller (1972, chap. 8).</span></small>

$$
E (\widetilde {R} _ {i}) = [ E (\widetilde {R} _ {m}) - S _ {m} \sigma (\widetilde {R} _ {m}) ] + S _ {m} \sigma (\widetilde {R} _ {m}) \beta_ {i},\tag{2}
$$

where

$$
\beta_ {i} \equiv \frac {\operatorname{cov} \left(\tilde {R} _ {i} , \tilde {R} _ {m}\right)}{\sigma^ {2} \left(\tilde {R} _ {m}\right)} = \frac {\sum_ {j = 1} ^ {N} x _ {j m} \sigma_ {i j}}{\sigma^ {2} \left(\tilde {R} _ {m}\right)} = \frac {\operatorname{cov} \left(\tilde {R} _ {i} , \tilde {R} _ {m}\right) / \sigma \left(\tilde {R} _ {m}\right)}{\sigma \left(\tilde {R} _ {m}\right)}.\tag{3}
$$

The parameter  $\beta_{i}$  can be interpreted as the risk of asset i in the portfolio m, measured relative to  $\sigma(\widetilde{R}_{m})$ , the total risk of m. The intercept in (2),

$$
E (\tilde {R} _ {0}) \equiv E (\tilde {R} _ {m}) - S _ {m} \sigma (\tilde {R} _ {m}),\tag{4}
$$

is the expected return on a security whose return is uncorrelated with $\widetilde{R}_m$ — that is, a zero-$\beta$ security. Since $\beta = 0$ implies that a security contributes nothing to $\sigma (\widetilde{R}_m)$, it is appropriate to say that it is riskless in this portfolio. It is well to note from (3), however, that since $x_{im}\sigma_{ii} = x_{im}$ $\sigma^2 (\widetilde{R}_i)$ is just one of the $N$ terms in $\beta_{i},\beta_{i} = 0$ does not imply that security $i$ has zero variance of return.

From (4), it follows that

$$
S _ {m} = \frac {E (\widetilde {R} _ {m}) - E (\widetilde {R} _ {0})}{\sigma (\widetilde {R} _ {m})},\tag{5}
$$

so that (2) can be rewritten

$$
E (\tilde {K} _ {i}) = E (\tilde {K} _ {0}) + [ E (\tilde {K} _ {m}) - E (\tilde {K} _ {0}) ] \beta_ {i}.\tag{6}
$$

In words, the expected return on security $i$ is $E(\widetilde{R}_0)$, the expected return on a security that is riskless in the portfolio $m$, plus a risk premium that is $\beta_i$ times the difference between $E(\widetilde{R}_m)$ and $E(\widetilde{R}_0)$.

Equation (6) has three testable implications: (C1) The relationship between the expected return on a security and its risk in any efficient portfolio $m$ is linear. (C2) $\beta_{i}$ is a complete measure of the risk of security $i$ in the efficient portfolio $m$; no other measure of the risk of $i$ appears in (6). (C3) In a market of risk-averse investors, higher risk should be associated with higher expected return; that is, $E(\widetilde{R}_m) - E(\widetilde{R}_0) > 0$.

The importance of condition C3 is obvious. The importance of C1 and C2 should become clear as the discussion proceeds. At this point suffice it to say that if C1 and C2 do not hold, market returns do not reflect the attempts of investors to hold efficient portfolios: Some assets are systematically underpriced or overpriced relative to what is implied by the expected return-risk or efficiency equation (6).

## B. Market Equilibrium and the Efficiency of the Market Portfolio

To test conditions C1–C3 we must identify some efficient portfolio m. This in turn requires specification of the characteristic of market equilibrium when investors make portfolio decisions according to the two-parameter model.

Assume again that the capital market is perfect. In addition, suppose that from the information available without cost all investors derive the same and correct assessment of the distribution of the future value of any asset or portfolio—an assumption usually called “homogeneous expectations.” Finally, assume that short selling of all assets is allowed. Then Black (1972) has shown that in a market equilibrium, the so-called market portfolio, defined by the weights

$$
x _ {i m} \equiv \frac {\text {total market value of all units of asset} i}{\text {total market value of all assets}},
$$

is always efficient.

Since it contains all assets in positive amounts, the market portfolio is a convenient reference point for testing the expected return-risk conditions C1–C3 of the two-parameter model. And the homogeneous-expectations assumption implies a correspondence between ex ante assessments of return distributions and distributions of ex post returns that is also required for meaningful tests of these three hypotheses.

## C. A Stochastic Model for Returns

Equation (6) is in terms of expected returns. But its implications must be tested with data on period-by-period security and portfolio returns. We wish to choose a model of period-by-period returns that allows us to use observed average returns to test the expected-return conditions C1–C3, but one that is nevertheless as general as possible. We suggest the following stochastic generalization of (6):

$$
\widetilde {R} _ {i t} = \widetilde {\gamma} _ {0 t} + \widetilde {\gamma} _ {1 t} \beta_ {i} + \widetilde {\gamma} _ {2 t} \beta_ {i} ^ {2} + \widetilde {\gamma} _ {3 t} s _ {i} + \widetilde {\eta} _ {i t}.\tag{7}
$$

The subscript $t$ refers to period $t$, so that $\widetilde{R}_{it}$ is the one-period percentage return on security $i$ from $t - 1$ to $t$. Equation (7) allows $\widetilde{\gamma}_{0t}$ and $\widetilde{\gamma}_{1t}$ to vary stochastically from period to period. The hypothesis of condition C3 is that the expected value of the risk premium $\widetilde{\gamma}_{1t}$, which is the slope $[E(\widetilde{R}_{mt}) - E(\widetilde{R}_{0t})]$ in (6), is positive—that is, $E(\widetilde{\gamma}_{1t}) = E(\widetilde{R}_{mt}) - E(\widetilde{R}_{0t}) > 0$.

The variable $\beta_{i}^{2}$ is included in (7) to test linearity. The hypothesis of condition C1 is $E(\widetilde{\gamma}_{2t}) = 0$, although $\widetilde{\gamma}_{2t}$ is also allowed to vary stochastically from period to period. Similar statements apply to the term involving $s_i$ in (7), which is meant to be some measure of the risk of security $i$ that is not deterministically related to $\beta_{i}$. The hypothesis of condition C2 is $E(\widetilde{\gamma}_{3t}) = 0$, but $\widetilde{\gamma}_{3t}$ can vary stochastically through time.

The disturbance $\widetilde{\eta}_{it}$ is assumed to have zero mean and to be independent of all other variables in (7). If all portfolio return distributions are to be normal (or symmetric stable), then the variables $\widetilde{\gamma}_{it},\widetilde{\gamma}_{0t},\widetilde{\gamma}_{1t},\widetilde{\gamma}_{2t}$ and $\widetilde{\gamma}_{3t}$ must have a multivariate normal (or symmetric stable) distribution.

## D. Capital Market Efficiency: The Behavior of Returns through Time

C1–C3 are conditions on expected returns and risk that are implied by the two-parameter model. But the model, and especially the underlying assumption of a perfect market, implies a capital market that is efficient in the sense that prices at every point in time fully reflect available information. This use of the word efficient is, of course, not to be confused with portfolio efficiency. The terminology, if a bit unfortunate, is at least standard.

Market efficiency in combination with condition C1 requires that scrutiny of the time series of the stochastic nonlinearity coefficient  $\tilde{\gamma}_{2t}$  does not lead to nonzero estimates of expected future values of  $\tilde{\gamma}_{2t}$ . Formally,  $\tilde{\gamma}_{2t}$  must be a fair game. In practical terms, although nonlinearities are observed ex post, because  $\tilde{\gamma}_{2t}$  is a fair game, it is always appropriate for the investor to act ex ante under the presumption that the two-parameter model, as summarized by (6), is valid. That is, in his portfolio decisions he always assumes that there is a linear relationship between the risk of a security and its expected return. Likewise, market efficiency in the two-parameter model requires that the non- $\beta$  risk coefficient  $\tilde{\gamma}_{3t}$  and the time series of return disturbances  $\tilde{\eta}_{it}$  are fair games. And the fair-game hypothesis also applies to the time series of  $\tilde{\gamma}_{1t} - [E(\tilde{R}_{mt}) - E(\tilde{R}_{0t})]$ , the difference between the risk premium for period t and its expected value.

In the terminology of Fama (1970b), these are “weak-form” propositions about capital market efficiency for a market where expected returns are generated by the two-parameter model. The propositions are weak since they are only concerned with whether prices fully reflect any information in the time series of past returns. “Strong-form” tests would be concerned with the speed-of-adjustment of prices to all available information.

## E. Market Equilibrium with Riskless Borrowing and Lending

We have as yet presented no hypothesis about  $\widetilde{\gamma}_{0t}$  in (7). In the general two-parameter model, given  $E(\widetilde{\gamma}_{2t}) = E(\widetilde{\gamma}_{3t}) = E(\widetilde{\eta}_{it}) = 0$ , then, from (6),  $E(\widetilde{\gamma}_{0t})$  is just  $E(\widetilde{R}_{0t})$ , the expected return on any zero- $\beta$  security. And market efficiency requires that  $\widetilde{\gamma}_{0t} - E(\widetilde{R}_{0t})$  be a fair game.

But if we add to the model as presented thus far the assumption that there is unrestricted riskless borrowing and lending at the known rate $R_{ft}$, then one has the market setting of the original two-parameter “capital asset pricing model” of Sharpe (1964) and Lintner (1965). In this world, since $\beta_f = 0$, $E(\tilde{\gamma}_{0t}) = R_{ft}$. And market efficiency requires that $\tilde{\gamma}_{0t} - R_{ft}$ be a fair game.

It is well to emphasize that to refute the proposition that  $E(\widetilde{\gamma}_{ot}) = R_{ft}$  is only to refute a specific two-parameter model of market equilibrium. Our view is that tests of conditions C1–C3 are more fundamental. We regard C1–C3 as the general expected return implications of the two-parameter model in the sense that they are the implications of the fact that in the two-parameter portfolio model investors hold efficient portfolios, and they are consistent with any two-parameter model of market equilibrium in which the market portfolio is efficient.

## F. The Hypotheses

To summarize, given the stochastic generalization of (2) and (6) that is provided by (7), the testable implications of the two-parameter model for expected returns are:

C1 (linearity)— $E(\widetilde{\gamma}_{2t})=0$ .

C2 (no systematic effects of non- $\beta$ risk) $= E(\tilde{\gamma}_{3t}) = 0.$

C3 (positive expected return-risk tradeoff)— $E(\tilde{\gamma}_{1t}) = E(\tilde{R}_{mt}) - E(\tilde{R}_{0t}) > 0$ .

Sharpe-Lintner (S-L) Hypothesis— $E(\tilde{\gamma}_{0t}) = R_{ft}$.

Finally, capital market efficiency in a two-parameter world requires

$ME$ (market efficiency)—the stochastic coefficients $\tilde{\gamma}_{2t}, \tilde{\gamma}_{3t}, \tilde{\gamma}_{1t} - [E(\tilde{R}_{mt}) - E(\tilde{R}_{0t})]$, $\tilde{\gamma}_{0t} - E(\tilde{R}_{0t})$, and the disturbances $\tilde{\eta}_{it}$ are fair games.$^{4}$

## III. Previous Work $^{5}$

The earliest tests of the two-parameter model were done by Douglas (1969), whose results seem to refute condition C2. In annual and quarterly return data, there seem to be measures of risk, in addition to  $\beta$ , that contribute systematically to observed average returns. These results, if valid, are inconsistent with the hypothesis that investors attempt to hold efficient portfolios. Assuming that the market portfolio is efficient, premiums are paid for risks that do not contribute to the risk of an efficient portfolio.

Miller and Scholes (1972) take issue both with Douglas's statistical techniques and with his use of annual and quarterly data. Using different methods and simulations, they show that Douglas's negative results could be expected even if condition C2 holds. Condition C2 is tested below with extensive monthly data, and this avoids almost all of the problems discussed by Miller and Scholes.

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$\widetilde{\gamma}_{2t}$</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$\widetilde{\gamma}_{3t}$</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$E(\widetilde{\gamma}_{2t}) = E(\widetilde{\gamma}_{3t}) = 0$</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$^{4}$  If  $\widetilde{\gamma}_{2t}$  and  $\widetilde{\gamma}_{3t}$  are fair games, then  $E(\widetilde{\gamma}_{2t}) = E(\widetilde{\gamma}_{3t}) = 0$ . Thus, C1 and C2 are implied by ME. Keeping the expected return conditions separate, however, better emphasizes the economic basis of the various hypotheses.</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$^{5}$  A comprehensive survey of empirical and theoretical work on the two-parameter model is in Jensen (1972).</span></small>

Much of the available empirical work on the two-parameter model is concerned with testing the S-L hypothesis that $E(\widetilde{\gamma}_{0t}) = R_{ft}$. The tests of Friend and Blume (1970) and those of Black, Jensen, and Scholes (1972) indicate that, at least in the period since 1940, on average $\widetilde{\gamma}_{0t}$ is systematically greater than $R_{ft}$. The results below support this conclusion.

In the empirical literature to date, the importance of the linearity condition C1 has been largely overlooked. Assuming that the market portfolio m is efficient, if  $E(\tilde{\gamma}_{2t})$  in (7) is positive, the prices of high- $\beta$  securities are on average too low—their expected returns are too high—relative to those of low- $\beta$  securities, while the reverse holds if  $E(\tilde{\gamma}_{2t})$  is negative. In short, if the process of price formation in the capital market reflects the attempts of investors to hold efficient portfolios, then the linear relationship of (6) between expected return and risk must hold.

Finally, the previous empirical work on the two-parameter model has not been concerned with tests of market efficiency.

## IV. Methodology

The data for this study are monthly percentage returns (including dividends and capital gains, with the appropriate adjustments for capital changes such as splits and stock dividends) for all common stocks traded on the New York Stock Exchange during the period January 1926 through June 1968. The data are from the Center for Research in Security Prices of the University of Chicago.

## A. General Approach

Testing the two-parameter model immediately presents an unavoidable “errors-in-the-variables” problem: The efficiency condition or expected return-risk equation (6) is in terms of true values of the relative risk measure  $\beta_{i}$ , but in empirical tests estimates,  $\hat{\beta}_{i}$ , must be used. In this paper

$$
\widehat {\beta} _ {i} \equiv \frac {\widehat {\operatorname{cov}} (\widetilde {R} _ {i} , \widetilde {R} _ {m})}{\widehat {\sigma} ^ {2} (\widetilde {R} _ {m})},
$$

where $\widehat{\mathrm{cov}} (\widetilde{R}_i,\widetilde{R}_m)$ and $\hat{\sigma}^2 (\widetilde{R}_m)$ are estimates of $\mathrm{cov}(\widetilde{R}_i,\widetilde{R}_m)$ and $\sigma^2 (\widetilde{R}_m)$ obtained from monthly returns, and where the proxy chosen for $\widetilde{R}_{mt}$ is "Fisher's Arithmetic Index," an equally weighted average of the returns on all stocks listed on the New York Stock Exchange in month $t$. The properties of this index are analyzed in Fisher (1966).

Blume (1970) shows that for any portfolio $p$, defined by the weights $x_{ip}, i = 1, 2, \ldots, N$,

$$
\widehat {\beta} _ {p} \equiv \frac {\widehat {\operatorname{cov}} \left(\widetilde {R} _ {p} , \widetilde {R} _ {m}\right)}{\hat {\sigma} ^ {2} \left(\widetilde {R} _ {m}\right)} = \sum_ {i = 1} ^ {N} x _ {i p} \frac {\widehat {\operatorname{cov}} \left(\widetilde {R} _ {i} , \widetilde {R} _ {m}\right)}{\hat {\sigma} ^ {2} \left(\widetilde {R} _ {m}\right)} = \sum_ {i = 1} ^ {N} x _ {i p} \widehat {\beta} _ {i}.
$$

If the errors in the  $\hat{\beta}_{i}$  are substantially less than perfectly positively correlated, the  $\hat{\beta}$ 's of portfolios can be much more precise estimates of true  $\beta$ 's than the  $\hat{\beta}$ 's for individual securities.

To reduce the loss of information in the risk-return tests caused by using portfolios rather than individual securities, a wide range of values of portfolio  $\hat{\beta}_{p}$ 's is obtained by forming portfolios on the basis of ranked values of  $\hat{\beta}_{i}$  for individual securities. But such a procedure, naively executed could result in a serious regression phenomenon. In a cross section of  $\hat{\beta}_{i}$, high observed  $\hat{\beta}_{i}$  tend to be above the corresponding true  $\beta_{i}$  and low observed  $\hat{\beta}_{i}$  tend to be below the true  $\beta_{i}$. Forming portfolios on the basis of ranked  $\hat{\beta}_{i}$  thus causes bunching of positive and negative sampling errors within portfolios. The result is that a large portfolio  $\hat{\beta}_{p}$  would tend to overstate the true  $\beta_{p}$, while a low  $\hat{\beta}_{p}$  would tend to be an underestimate.

The regression phenomenon can be avoided to a large extent by forming portfolios from ranked  $\hat{\beta}_{i}$  computed from data for one time period but then using a subsequent period to obtain the  $\hat{\beta}_{p}$  for these portfolios that are used to test the two-parameter model. With fresh data, within a portfolio errors in the individual security  $\hat{\beta}_{i}$  are to a large extent random across securities, so that in a portfolio  $\hat{\beta}_{p}$  the effects of the regression phenomenon are, it is hoped, minimized. $^{6}$

## B. Details

The specifics of the approach are as follows. Let N be the total number of securities to be allocated to portfolios and let  $\operatorname{int}(N/20)$  be the largest integer equal to or less than N/20. Using the first 4 years (1926–29) of monthly return data, 20 portfolios are formed on the basis of ranked  $\hat{\beta}_{i}$  for individual securities. The middle 18 portfolios each has  $\operatorname{int}(N/20)$  securities. If N is even, the first and last portfolios each has  $\operatorname{int}(N/20) + \frac{1}{2}[N - 20\operatorname{int}(N/20)]$  securities. The last (highest  $\hat{\beta}$ ) portfolio gets an additional security if N is odd.

The following 5 years (1930–34) of data are then used to recompute the  $\hat{\beta}_{i}$ , and these are averaged across securities within portfolios to obtain 20 initial portfolio  $\hat{\beta}_{pt}$  for the risk-return tests. The subscript t is added to indicate that each month t of the following four years (1935–38) these  $\hat{\beta}_{pt}$  are recomputed as simple averages of individual security  $\hat{\beta}_{i}$ , thus adjusting the portfolio  $\hat{\beta}_{pt}$  month by month to allow for delisting of securities. The component  $\hat{\beta}_{i}$  for securities are themselves updated yearly—that is, they are recomputed from monthly returns for 1930 through 1935, 1936, or 1937.

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$^{6}$  The errors-in-the-variables problem and the technique of using portfolios to solve it were first pointed out by Blume (1970). The portfolio approach is also used by Friend and Blume (1970) and Black, Jensen, and Scholes (1972). The regression phenomenon that arises in risk-return tests was first recognized by Blume (1970) and then by Black, Jensen, and Scholes (1972), who offer a solution to the problem that is similar in spirit to ours.</span></small>

As a measure of the non- $\beta$ risk of security $i$ we use $s(\hat{\epsilon}_i)$, the standard deviation of the least-squares residuals $\hat{\epsilon}_{it}$ from the so-called market model

$$
\widetilde {K} _ {i t} = a _ {i} + \beta^ {i} \widetilde {K} _ {m t} + \widetilde {\epsilon} _ {i t}.\tag{8}
$$

The standard deviation  $s(\hat{\epsilon}_{i})$  is a measure of non- $\beta$  risk in the following sense. One view of risk, antithetic to that of portfolio theory, says that the risk of a security is measured by the total dispersion of its return distribution. Given a market dominated by risk averters, this model would predict that a security's expected return is related to its total return dispersion rather than just to the contribution of the security to the dispersion in the return on an efficient portfolio. $^{7}$  If  $B_{i} \equiv \text{cov}(\tilde{R}_{i}, \tilde{R}_{m}) / \sigma^{2}(\tilde{R}_{m})$ , then in (8)  $\text{cov}(\tilde{\epsilon}_{i}, \tilde{R}_{m}) = 0$ , and

$$
\sigma^ {2} \left(\tilde {R} _ {i}\right) = \beta_ {i} ^ {2} \sigma^ {2} \left(\tilde {R} _ {m}\right) + \sigma^ {2} \left(\tilde {\epsilon} _ {i}\right) + 2 \beta_ {i} \operatorname{cov} \left(\tilde {R} _ {m}, \tilde {\epsilon} _ {i}\right).\tag{9}
$$

Thus, from (9), one can say that  $s(\hat{\epsilon}_{i})$  is an estimate of that part of the dispersion of the distribution of the return on security i that is not directly related to  $\beta_{i}$ .

The month-by-month returns on the 20 portfolios, with equal weighting of individual securities each month, are also computed for the 4-year period 1935–38. For each month t of this period, the following cross-sectional regression—the empirical analog of equation (7)—is run:

$$
R _ {p t} = \hat {\gamma} _ {0 t} + \hat {\gamma} _ {1 t} \hat {\beta} _ {p, t - 1} + \hat {\gamma} _ {2 t} \hat {\beta} _ {p, t - 1} ^ {2} + \hat {\gamma} _ {3 t} \bar {s} _ {p, t - 1} (\hat {\epsilon} _ {i}) + \hat {\eta} _ {p t},\tag{10}
$$

$$
p = 1, 2, \dots , 2 0.
$$

The independent variable $\hat{\beta}_{p,t-1}$ is the average of the $\hat{\beta}_i$ for securities in portfolio $p$ discussed above; $\hat{\beta}_{p,t-1}^2$ is the average of the squared values of these $\hat{\beta}_i$ (and is thus somewhat mislabeled); and $\overline{s}_{p,t-1}(\hat{\epsilon}_i)$ is likewise the average of $s(\hat{\epsilon}_i)$ for securities in portfolio $p$. The $s(\hat{\epsilon}_i)$ are computed from data for the same period as the component $\hat{\beta}_i$ of $\hat{\beta}_{p,t-1}$, and like these $\hat{\beta}_i$, they are updated annually.

The regression equation (10) is (7) averaged across the securities in a portfolio, with estimates  $\hat{\beta}_{p,t-1}$ ,  $\hat{\beta}^{2}_{p,t-1}$ , and  $\bar{s}_{p,t-1}(\hat{\epsilon}_{i})$  used as explanatory variables, and with least-squares estimates of the stochastic coefficients  $\hat{\gamma}_{0t}$ ,  $\hat{\gamma}_{1t}$ ,  $\hat{\gamma}_{2t}$ , and  $\hat{\gamma}_{3t}$ . The results from (10)—the time series of month-by-month values of the regression coefficients  $\hat{\gamma}_{0t}$ ,  $\hat{\gamma}_{1t}$ ,  $\hat{\gamma}_{2t}$ , and  $\hat{\gamma}_{3t}$  for the 4-year period 1935–38—are the inputs for our tests of the two-parameter model for this period. To get results for other periods, the steps described above are repeated. That is, 7 years of data are used to form portfolios; the next 5 years are used to compute initial values of the independent variables in (10); and then the risk-return regressions of (10) are fit month by month for the following 4-year period.

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$^{7}$ For those accustomed to the portfolio viewpoint, this alternative model may seem so naïve that it should be classified as a straw man. But it is the model of risk and return implied by the “liquidity preference” and “market segmentation” theories of the term structure of interest rates and by the Keynesian “normal backwardation” theory of commodity futures markets. For a discussion of the issues with respect to these markets, see Roll (1970) and K. Miller (1971).</span></small>

The nine different portfolio formation periods (all except the first 7 years in length), initial 5-year estimation periods, and testing periods (all but the last 4 years in length) are shown in table 1. The choice of 4-year testing periods is a balance of computation costs against the desire to reform portfolios frequently. The choice of 7-year portfolio formation periods and 5–8-year periods for estimating the independent variables  $\hat{\beta}_{p,t-1}$  and  $\bar{s}_{p,t-1}(\hat{\epsilon}_{i})$  in the risk-return regressions reflects a desire to balance the statistical power obtained with a large sample from a stationary process against potential problems caused by any nonconstancy of the  $\beta_{i}$ . The choices here are in line with the results of Gonedes (1973). His results also led us to require that to be included in a portfolio a security available in the first month of a testing period must also have data for all 5 years of the preceding estimation period and for at least 4 years of the portfolio formation period. The total number of securities available in the first month of each testing period and the number of securities meeting the data requirement are shown in table 1.

## C. Some Observations on the Approach

Table 2 shows the values of the 20 portfolios $\hat{\beta}_{p,t-1}$ and their standard errors $s(\hat{\beta}_{p,t-1})$ for four of the nine 5-year estimation periods. Also shown are: $r(R_p, R_m)^2$, the coefficient of determination between $R_{pt}$ and $R_{mt}$; $s(R_p)$, the sample standard deviation of $R_p$; and $s(\hat{\epsilon}_p)$, the standard deviation of the portfolio residuals from the market model of (8), not to be confused with $\bar{s}_{p,t-1}(\hat{\epsilon}_i)$, the average for individual securities, which is also shown. The $\hat{\beta}_{p,t-1}$ and $\bar{s}_{p,t-1}(\hat{\epsilon}_i)$ are the independent variables in the risk return regressions of (10) for the first month of the 4-year testing periods following the four estimation periods shown.

Under the assumptions that for a given security the disturbances $\tilde{\epsilon}_{jt}$ in (8) are serially independent, independent of $\widetilde{R}_{mt}$, and identically distributed through time, the standard error of $\hat{\beta}_i$ is

$$
\sigma (\hat {\beta} _ {i}) = \frac {\sigma (\tilde {\epsilon} _ {i})}{\sqrt {n}   \sigma (\tilde {R} _ {m})},
$$

where $n$ is the number of months used to compute $\hat{\beta}_i$. Likewise,

$$
\sigma (\widetilde {\beta} _ {p, t - 1}) = \frac {\sigma (\widetilde {\epsilon} _ {p})}{\sqrt {n} \sigma (\widetilde {R} _ {m})}.
$$

Thus, the fact that in table 2, $s(\hat{\epsilon}_p)$ is generally on the order of one-third to one-seventh $\bar{s}_{p,t-1}(\hat{\epsilon}_i)$ implies that $s(\hat{\beta}_{p,t-1})$ is one-third to one-seventh $s(\hat{\beta}_i)$. Estimates of $\beta$ for portfolios are indeed more precise than those for individual securities.

TABLE 1

PORTFOLIO FORMATION, ESTIMATION, AND TESTING PERIODS

<table><tr><td rowspan="2"></td><td colspan="5">PERIODS</td></tr><tr><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td></tr><tr><td>Portfolio formation period ...</td><td>1926-29</td><td>1927-33</td><td>1931-37</td><td>1935-41</td><td>1939-45</td></tr><tr><td>Initial estimation period ......</td><td>1930-34</td><td>1934-38</td><td>1938-42</td><td>1942-46</td><td>1946-50</td></tr><tr><td>Testing period ......</td><td>1935-38</td><td>1939-42</td><td>1943-46</td><td>1947-50</td><td>1951-54</td></tr><tr><td>No. of securities available ....</td><td>710</td><td>779</td><td>804</td><td>908</td><td>1,011</td></tr><tr><td>No. of securities meeting data requirement ......</td><td>435</td><td>576</td><td>607</td><td>704</td><td>751</td></tr></table>

Nevertheless, it is interesting to note that if the disturbances $\tilde{\epsilon}_{jt}$ in (8) were independent from security to security, the relative increase in the precision of the $\hat{\beta}$ obtained by using portfolios rather than individual securities would be about the same for all portfolios. We argue in the Appendix, however, that the results from (10) imply that the $\tilde{\epsilon}_{it}$ in (8) are interdependent, and the interdependence is strongest among high-$\beta$ securities and among low-$\beta$ securities. This is evident in table 2: The ratios $s(\hat{\epsilon}_p)/\bar{s}_{p,t-1}(\hat{\epsilon}_i)$ are always highest at the extremes of the $\hat{\beta}_{p,t-1}$ range and lowest for $\hat{\beta}_{p,t-1}$ close to 1.0. But it is important to emphasize that since these ratios are generally less than .33, interdependence among the $\tilde{\epsilon}_{it}$ of different securities does not destroy the value of using portfolios to reduce the dispersion of the errors in estimated $\beta$'s.

Finally, all the tests of the two-parameter model are predictive in the sense that the explanatory variables  $\hat{\beta}_{p,t-1}$  and  $\bar{s}_{p,t-1}(\hat{\epsilon}_{i})$  in (10) are computed from data for a period prior to the month of the returns, the  $R_{pt}$ , on which the regression is run. Although we are interested in testing the two-parameter model as a positive theory—that is, examining the extent to which it is helpful in describing actual return data—the model was initially developed by Markowitz (1959) as a normative theory—that is, as a model to help people make better decisions. As a normative theory the model only has content if there is some relationship between future returns and estimates of risk that can be made on the basis of current information.

Now that the predictive nature of the tests has been emphasized, to simplify the notation, the explanatory variables in (10) are henceforth referred to as $\hat{\beta}_p$, $\hat{\beta}_p^2$, and $\bar{s}_p(\hat{\epsilon}_i)$.

## V. Results

The major tests of the implications of the two-parameter model are in table 3. Results are presented for 10 periods: the overall period 1935–

TABLE 1 (Continued)

<table><tr><td rowspan="2"></td><td colspan="4">PERIODS</td></tr><tr><td>6</td><td>7</td><td>8</td><td>9</td></tr><tr><td>Portfolio formation period ...</td><td>1943-49</td><td>1947-53</td><td>1951-57</td><td>1955-61</td></tr><tr><td>Initial estimation period ......</td><td>1950-54</td><td>1954-58</td><td>1958-62</td><td>1962-66</td></tr><tr><td>Testing period ......</td><td>1955-58</td><td>1959-62</td><td>1963-66</td><td>1967-68</td></tr><tr><td>No. of securities available ....</td><td>1,053</td><td>1,065</td><td>1,162</td><td>1,261</td></tr><tr><td>No. of securities meeting data requirement ......</td><td>802</td><td>856</td><td>858</td><td>845</td></tr></table>

6/68; three long subperiods, 1935–45, 1946–55, and 1956–6/68; and six subperiods which, except for the first and last, cover 5 years each. This choice of subperiods reflects the desire to keep separate the pre- and post-World War II periods. Results are presented for four different versions of the risk-return regression equation (10): Panel D is based on (10) itself, but in panels A–C, one or more of the variables in (10) is suppressed. For each period and model, the table shows:  $\hat{\gamma}_{j}$ , the average of the month-by-month regression coefficient estimates,  $\hat{\gamma}_{jt}$ ;  $s(\hat{\gamma}_{j})$ , the standard deviation of the monthly estimates; and  $\vec{r}^{2}$  and  $s(r^{2})$ , the mean and standard deviation of the month-by-month coefficients of determination,  $r_{t}^{2}$ , which are adjusted for degrees of freedom. The table also shows the first-order serial correlations of the various monthly  $\hat{\gamma}_{jt}$  computed either about the sample mean of  $\hat{\gamma}_{jt}$  [in which case the serial correlations are labeled  $\rho_{M}(\hat{\gamma}_{i})$ ] or about an assumed mean of zero [in which case they are labeled  $\rho_{0}(\hat{\gamma}_{j})$ ]. Finally, t-statistics for testing the hypothesis that  $\hat{\gamma}_{j}=0$  are presented. These t-statistics are

$$
t (\bar {\hat {\gamma}} _ {j}) = \frac {\bar {\hat {\gamma}} _ {j}}{s (\hat {\gamma} _ {j}) / \sqrt {n}},
$$

where n is the number of months in the period, which is also the number of estimates  $\hat{\gamma}_{jt}$  used to compute  $\overline{\hat{\gamma}}_{j}$  and  $s(\hat{\gamma}_{j})$ .

In interpreting these t-statistics one should keep in mind the evidence of Fama (1965a) and Blume (1970) which suggests that distributions of common stock returns are “thick-tailed” relative to the normal distribution and probably conform better to nonnormal symmetric stable distributions than to the normal. From Fama and Babiak (1968), this evidence means that when one interprets large t-statistics under the assumption that the underlying variables are normal, the probability or significance levels obtained are likely to be overestimates. But it is important to note that, with the exception of condition C3 (positive expected return-risk tradeoff), upward-biased probability levels lead to biases toward rejection of the hypotheses of the two-parameter model. Thus, if these hypotheses cannot be rejected when t-statistics are interpreted under the assumption of normality, the hypotheses are on even firmer ground when one takes into account the thick tails of empirical return distributions.

TABLE 2

SAMPLE STATISTICS FOR FOUR SELECTED ESTIMATION PERIODS

<table><tr><td>Statistic</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td><td>9</td><td>10</td></tr><tr><td></td><td colspan="10">Portfolios for Estimation Period 1934-38</td></tr><tr><td> $\widehat{\beta}_{p,t-1}$ </td><td>.322</td><td>.508</td><td>.651</td><td>.674</td><td>.695</td><td>.792</td><td>.921</td><td>.942</td><td>.970</td><td>1.005</td></tr><tr><td> $s(\widehat{\beta}_{p,t-1})$ </td><td>.027</td><td>.027</td><td>.025</td><td>.023</td><td>.028</td><td>.026</td><td>.032</td><td>.029</td><td>.034</td><td>.027</td></tr><tr><td> $r(R_p,R_m)^2$ </td><td>.709</td><td>.861</td><td>.921</td><td>.936</td><td>.912</td><td>.941</td><td>.932</td><td>.946</td><td>.933</td><td>.958</td></tr><tr><td> $s(R_p)$ </td><td>.040</td><td>.058</td><td>.072</td><td>.074</td><td>.077</td><td>.087</td><td>.101</td><td>.103</td><td>.106</td><td>.109</td></tr><tr><td> $s(\hat{\epsilon}_p)$ </td><td>.022</td><td>.022</td><td>.020</td><td>.019</td><td>.023</td><td>.021</td><td>.026</td><td>.024</td><td>.028</td><td>.022</td></tr><tr><td> $\overline{s}_{p,t-1}(\hat{\epsilon}_i)$ </td><td>.085</td><td>.075</td><td>.083</td><td>.078</td><td>.090</td><td>.095</td><td>.109</td><td>.106</td><td>.111</td><td>.097</td></tr><tr><td> $s(\hat{\epsilon}_p)/\overline{s}_{p,t-1}(\hat{\epsilon}_i)$ </td><td>.259</td><td>.293</td><td>.241</td><td>.244</td><td>.256</td><td>.221</td><td>.238</td><td>.226</td><td>.252</td><td>.227</td></tr><tr><td></td><td colspan="10">Portfolios for Estimation Period 1942-46</td></tr><tr><td> $\widehat{\beta}_{p,t-1}$ </td><td>.467</td><td>.537</td><td>.593</td><td>.628</td><td>.707</td><td>.721</td><td>.770</td><td>.792</td><td>.805</td><td>.894</td></tr><tr><td> $s(\widehat{\beta}_{p,t-1})$ </td><td>.045</td><td>.041</td><td>.044</td><td>.037</td><td>.027</td><td>.032</td><td>.035</td><td>.035</td><td>.028</td><td>.040</td></tr><tr><td> $r(R_p,R_m)^2$ </td><td>.645</td><td>.745</td><td>.753</td><td>.829</td><td>.919</td><td>.898</td><td>.889</td><td>.898</td><td>.934</td><td>.896</td></tr><tr><td> $s(R_p)$ </td><td>.035</td><td>.037</td><td>.041</td><td>.041</td><td>.044</td><td>.046</td><td>.049</td><td>.050</td><td>.050</td><td>.057</td></tr><tr><td> $s(\hat{\epsilon}_p)$ </td><td>.021</td><td>.019</td><td>.020</td><td>.017</td><td>.013</td><td>.015</td><td>.016</td><td>.016</td><td>.013</td><td>.018</td></tr><tr><td> $\overline{s}_{p,t-1}(\hat{\epsilon}_i)$ </td><td>.055</td><td>.055</td><td>.063</td><td>.058</td><td>.058</td><td>.063</td><td>.064</td><td>.064</td><td>.062</td><td>.069</td></tr><tr><td> $s(\hat{\epsilon}_p)/\overline{s}_{p,t-1}(\hat{\epsilon}_i)$ </td><td>.382</td><td>.345</td><td>.317</td><td>.293</td><td>.224</td><td>.238</td><td>.250</td><td>.250</td><td>.210</td><td>.261</td></tr><tr><td></td><td colspan="10">Portfolios for Estimation Period 1950-54</td></tr><tr><td> $\widehat{\beta}_{p,t-1}$ </td><td>.418</td><td>.590</td><td>.694</td><td>.751</td><td>.777</td><td>.784</td><td>.929</td><td>.950</td><td>.996</td><td>1.014</td></tr><tr><td> $s(\widehat{\beta}_{p,t-1})$ </td><td>.042</td><td>.047</td><td>.045</td><td>.037</td><td>.038</td><td>.035</td><td>.050</td><td>.038</td><td>.035</td><td>.029</td></tr><tr><td> $r(R_p,R_m)^2$ </td><td>.629</td><td>.723</td><td>.798</td><td>.872</td><td>.878</td><td>.895</td><td>.856</td><td>.913</td><td>.933</td><td>.954</td></tr><tr><td> $s(R_p)$ </td><td>.019</td><td>.025</td><td>.028</td><td>.029</td><td>.030</td><td>.030</td><td>.036</td><td>.036</td><td>.037</td><td>.038</td></tr><tr><td> $s(\hat{\epsilon}_p)$ </td><td>.012</td><td>.013</td><td>.013</td><td>.010</td><td>.010</td><td>.010</td><td>.014</td><td>.011</td><td>.010</td><td>.008</td></tr><tr><td> $\overline{s}_{p,t-1}(\hat{\epsilon}_i)$ </td><td>.040</td><td>.044</td><td>.046</td><td>.048</td><td>.051</td><td>.051</td><td>.052</td><td>.053</td><td>.054</td><td>.057</td></tr><tr><td> $s(\hat{\epsilon}_p)/\overline{s}_{p,t-1}(\hat{\epsilon}_i)$ </td><td>.300</td><td>.295</td><td>.283</td><td>.208</td><td>.196</td><td>.196</td><td>.269</td><td>.208</td><td>.185</td><td>.140</td></tr><tr><td></td><td colspan="10">Portfolios for Estimation Period 1958-62</td></tr><tr><td> $\widehat{\beta}_{p,t-1}$ </td><td>.626</td><td>.635</td><td>.719</td><td>.801</td><td>.817</td><td>.860</td><td>.920</td><td>.950</td><td>.975</td><td>.995</td></tr><tr><td> $s(\widehat{\beta}_{p,t-1})$ </td><td>.043</td><td>.048</td><td>.039</td><td>.046</td><td>.047</td><td>.033</td><td>.037</td><td>.038</td><td>.032</td><td>.037</td></tr><tr><td> $r(R_p,R_m)^2$ </td><td>.783</td><td>.745</td><td>.851</td><td>.835</td><td>.838</td><td>.920</td><td>.913</td><td>.915</td><td>.939</td><td>.925</td></tr><tr><td> $s(R_p)$ </td><td>.030</td><td>.031</td><td>.033</td><td>.037</td><td>.038</td><td>.038</td><td>.041</td><td>.042</td><td>.043</td><td>.044</td></tr><tr><td> $s(\hat{\epsilon}_p)$ </td><td>.014</td><td>.016</td><td>.013</td><td>.015</td><td>.015</td><td>.011</td><td>.012</td><td>.012</td><td>.011</td><td>.012</td></tr><tr><td> $\overline{s}_{p,t-1}(\hat{\epsilon}_i)$ </td><td>.049</td><td>.052</td><td>.056</td><td>.059</td><td>.064</td><td>.061</td><td>.070</td><td>.069</td><td>.068</td><td>.064</td></tr><tr><td> $s(\hat{\epsilon}_p)/\overline{s}_{p,t-1}(\hat{\epsilon}_i)$ </td><td>.286</td><td>.308</td><td>.232</td><td>.254</td><td>.234</td><td>.180</td><td>.171</td><td>.174</td><td>.162</td><td>.188</td></tr></table>

Further justification for using $t$-statistics to test hypotheses on monthly common stock returns is in the work of Officer (1971). Under the assumption that distributions of monthly returns are symmetric stable, he estimates that in the post-World War II period the characteristic exponent for these distributions is about 1.8 (as compared with a value of 2.0 for a normal distribution). From Fama and Roll (1968), for values of the characteristic exponent so close to 2.0 stable nonnormal distributions differ noticeably from the normal only in their extreme tails—that is, beyond the .05 and .95 fractiles. Thus, as long as one is not concerned with precise estimates of probability levels (always a somewhat meaningless activity), interpreting t-statistics in the usual way does not lead to serious errors.

TABLE 2 (Continued)

<table><tr><td>Statistic</td><td>11</td><td>12</td><td>13</td><td>14</td><td>15</td><td>16</td><td>17</td><td>18</td><td>19</td><td>20</td></tr><tr><td colspan="11">Portfolios for Estimation Period 1934-38</td></tr><tr><td> $\widehat{\beta}_{p,t-1}$ </td><td>1.046</td><td>1.122</td><td>1.181</td><td>1.192</td><td>1.196</td><td>1.295</td><td>1.335</td><td>1.396</td><td>1.445</td><td>1.458</td></tr><tr><td> $s(\widehat{\beta}_{p,t-1})$ </td><td>.028</td><td>.031</td><td>.035</td><td>.028</td><td>.029</td><td>.032</td><td>.032</td><td>.053</td><td>.039</td><td>.053</td></tr><tr><td> $r(R_p,R_m)^2$ </td><td>.959</td><td>.956</td><td>.951</td><td>.969</td><td>.966</td><td>.966</td><td>.967</td><td>.922</td><td>.958</td><td>.927</td></tr><tr><td> $s(R_p)$ </td><td>.113</td><td>.122</td><td>.128</td><td>.128</td><td>.129</td><td>.140</td><td>.144</td><td>.154</td><td>.156</td><td>.160</td></tr><tr><td> $s(\hat{e}_p)$ </td><td>.023</td><td>.026</td><td>.029</td><td>.023</td><td>.024</td><td>.026</td><td>.026</td><td>.043</td><td>.032</td><td>.043</td></tr><tr><td> $\overline{s}_{p,t-1}(\hat{e}_i)$ </td><td>.094</td><td>.124</td><td>.120</td><td>.122</td><td>.132</td><td>.125</td><td>.129</td><td>.158</td><td>.145</td><td>.170</td></tr><tr><td> $s(\hat{e}_p)/\overline{s}_{p,t-1}(\hat{e}_i)$ </td><td>.245</td><td>.210</td><td>.242</td><td>.188</td><td>.182</td><td>.208</td><td>.202</td><td>.272</td><td>.221</td><td>.253</td></tr><tr><td colspan="11">Portfolios for Estimation Period 1942-46</td></tr><tr><td> $\widehat{\beta}_{p,t-1}$ </td><td>.949</td><td>.952</td><td>1.010</td><td>1.038</td><td>1.254</td><td>1.312</td><td>1.316</td><td>1.473</td><td>1.631</td><td>1.661</td></tr><tr><td> $s(\widehat{\beta}_{p,t-1})$ </td><td>.031</td><td>.036</td><td>.040</td><td>.030</td><td>.034</td><td>.039</td><td>.041</td><td>.084</td><td>.083</td><td>.077</td></tr><tr><td> $r(R_p,R_m)^2$ </td><td>.942</td><td>.923</td><td>.917</td><td>.954</td><td>.958</td><td>.951</td><td>.945</td><td>.839</td><td>.867</td><td>.887</td></tr><tr><td> $s(R_p)$ </td><td>.059</td><td>.060</td><td>.063</td><td>.064</td><td>.077</td><td>.081</td><td>.081</td><td>.097</td><td>.105</td><td>.106</td></tr><tr><td> $s(\hat{e}_p)$ </td><td>.014</td><td>.016</td><td>.018</td><td>.014</td><td>.016</td><td>.018</td><td>.019</td><td>.039</td><td>.038</td><td>.036</td></tr><tr><td> $\overline{s}_{p,t-1}(\hat{e}_i)$ </td><td>.073</td><td>.074</td><td>.085</td><td>.077</td><td>.096</td><td>.083</td><td>.086</td><td>.134</td><td>.117</td><td>.122</td></tr><tr><td> $s(\hat{e}_p)/\overline{s}_{p,t-1}(\hat{e}_i)$ </td><td>.192</td><td>.216</td><td>.212</td><td>.182</td><td>.167</td><td>.217</td><td>.221</td><td>.291</td><td>.325</td><td>.295</td></tr><tr><td colspan="11">Portfolios for Estimation Period 1950-54</td></tr><tr><td> $\widehat{\beta}_{p,t-1}$ </td><td>1.117</td><td>1.123</td><td>1.131</td><td>1.134</td><td>1.186</td><td>1.235</td><td>1.295</td><td>1.324</td><td>1.478</td><td>1.527</td></tr><tr><td> $s(\widehat{\beta}_{p,t-1})$ </td><td>.039</td><td>.027</td><td>.044</td><td>.033</td><td>.037</td><td>.049</td><td>.045</td><td>.046</td><td>.058</td><td>.086</td></tr><tr><td> $r(R_p,R_m)^2$ </td><td>.934</td><td>.968</td><td>.919</td><td>.952</td><td>.944</td><td>.915</td><td>.933</td><td>.934</td><td>.917</td><td>.841</td></tr><tr><td> $s(R_p)$ </td><td>.042</td><td>.041</td><td>.043</td><td>.042</td><td>.044</td><td>.047</td><td>.049</td><td>.050</td><td>.056</td><td>.060</td></tr><tr><td> $s(\hat{e}_p)$ </td><td>.011</td><td>.007</td><td>.012</td><td>.009</td><td>.010</td><td>.014</td><td>.013</td><td>.013</td><td>.016</td><td>.024</td></tr><tr><td> $\overline{s}_{p,t-1}(\hat{e}_i)$ </td><td>.066</td><td>.057</td><td>.066</td><td>.060</td><td>.064</td><td>.064</td><td>.065</td><td>.068</td><td>.076</td><td>.088</td></tr><tr><td> $s(\hat{e}_p)/\overline{s}_{p,t-1}(\hat{e}_i)$ </td><td>.167</td><td>.123</td><td>.182</td><td>.150</td><td>.156</td><td>.219</td><td>.200</td><td>.192</td><td>.210</td><td>.273</td></tr><tr><td colspan="11">Portfolios for Estimation Period 1958-62</td></tr><tr><td> $\widehat{\beta}_{p,t-1}$ </td><td>1.013</td><td>1.019</td><td>1.037</td><td>1.048</td><td>1.069</td><td>1.081</td><td>1.092</td><td>1.098</td><td>1.269</td><td>1.388</td></tr><tr><td> $s(\widehat{\beta}_{p,t-1})$ </td><td>.038</td><td>.031</td><td>.036</td><td>.033</td><td>.036</td><td>.038</td><td>.045</td><td>.045</td><td>.048</td><td>.065</td></tr><tr><td> $r(R_p,R_m)^2$ </td><td>.922</td><td>.948</td><td>.934</td><td>.945</td><td>.936</td><td>.931</td><td>.907</td><td>.910</td><td>.922</td><td>.886</td></tr><tr><td> $s(R_p)$ </td><td>.045</td><td>.045</td><td>.046</td><td>.046</td><td>.047</td><td>.048</td><td>.049</td><td>.049</td><td>.056</td><td>.063</td></tr><tr><td> $s(\hat{e}_p)$ </td><td>.013</td><td>.010</td><td>.012</td><td>.011</td><td>.012</td><td>.013</td><td>.015</td><td>.015</td><td>.016</td><td>.021</td></tr><tr><td> $\overline{s}_{p,t-1}(\hat{e}_i)$ </td><td>.069</td><td>.066</td><td>.067</td><td>.062</td><td>.070</td><td>.072</td><td>.076</td><td>.068</td><td>.070</td><td>.078</td></tr><tr><td> $s(\hat{e}_p)/\overline{s}_{p,t-1}(\hat{e}_i)$ </td><td>.188</td><td>.152</td><td>.179</td><td>.177</td><td>.171</td><td>.180</td><td>.197</td><td>.220</td><td>.228</td><td>.269</td></tr></table>

SUMMARY RESULTS FOR THE REGRESSION $R_{p} = \hat{\gamma}_{0t} + \hat{\gamma}_{1t}\hat{\beta}_{p} + \hat{\gamma}_{2t}\hat{\beta}_{p}^{2} + \hat{\gamma}_{3t}\bar{5}_{p}(\hat{\xi}_{i}) + \hat{\eta}_{pt}$

<table><tr><td colspan="2" rowspan="2">PERIOD</td><td colspan="19">STATISTIC</td><td></td></tr><tr><td> $\overline{\widehat{\gamma}}_0$ </td><td> $\overline{\widehat{\gamma}}_1$ </td><td> $\overline{\widehat{\gamma}}_2$ </td><td> $\overline{\widehat{\gamma}}_3$ </td><td> $\overline{\widehat{\gamma}}_0 - R_f$ </td><td> $s(\widehat{\gamma}_0)$ </td><td> $s(\widehat{\gamma}_1)$ </td><td> $s(\widehat{\gamma}_2)$ </td><td> $s(\widehat{\gamma}_3)$ </td><td> $\rho_0(\widehat{\gamma}_0 - R_f)$ </td><td> $\rho_M(\widehat{\gamma}_1)$ </td><td> $\rho_0(\widehat{\gamma}_2)$ </td><td> $\rho_0(\widehat{\gamma}_3)$ </td><td> $t(\widehat{\gamma}_0)$ </td><td> $t(\widehat{\gamma}_1)$ </td><td> $t(\widehat{\gamma}_2)$ </td><td> $t(\widehat{\gamma}_3)$ </td><td> $t(\widehat{\gamma}_0 - R_f)$ </td><td> $\bar{r}^2$ </td><td> $s(r^2)$ </td></tr><tr><td colspan="21">Panel A:</td><td></td></tr><tr><td>1935-6/68</td><td>..</td><td>.0061</td><td>.0085</td><td>...</td><td>...</td><td>.0048</td><td>.038</td><td>.066</td><td>...</td><td>...</td><td>.15</td><td>.02</td><td>...</td><td>...</td><td>3.24</td><td>2.57</td><td>...</td><td>...</td><td>2.55</td><td>.29</td><td>.30</td></tr><tr><td>1935-45</td><td>....</td><td>.0039</td><td>.0163</td><td>...</td><td>...</td><td>.0037</td><td>.052</td><td>.098</td><td>...</td><td>...</td><td>.10</td><td>-.03</td><td>...</td><td>...</td><td>.86</td><td>1.92</td><td>...</td><td>...</td><td>.82</td><td>.29</td><td>.29</td></tr><tr><td>1946-55</td><td>....</td><td>.0087</td><td>.0027</td><td>...</td><td>...</td><td>.0078</td><td>.026</td><td>.041</td><td>...</td><td>...</td><td>.18</td><td>.07</td><td>...</td><td>...</td><td>3.71</td><td>.70</td><td>...</td><td>...</td><td>3.31</td><td>.31</td><td>.32</td></tr><tr><td>1956-6/68</td><td>..</td><td>.0060</td><td>.0062</td><td>...</td><td>...</td><td>.0034</td><td>.030</td><td>.044</td><td>...</td><td>...</td><td>.27</td><td>.15</td><td>...</td><td>...</td><td>2.45</td><td>1.73</td><td>...</td><td>...</td><td>1.39</td><td>.28</td><td>.29</td></tr><tr><td>1935-40</td><td>....</td><td>.0024</td><td>.0109</td><td>...</td><td>...</td><td>.0023</td><td>.064</td><td>.116</td><td>...</td><td>...</td><td>.07</td><td>-.09</td><td>...</td><td>...</td><td>.32</td><td>.79</td><td>...</td><td>...</td><td>.31</td><td>.23</td><td>.30</td></tr><tr><td>1941-45</td><td>....</td><td>.0056</td><td>.0229</td><td>...</td><td>...</td><td>.0054</td><td>.034</td><td>.069</td><td>...</td><td>...</td><td>.23</td><td>.15</td><td>...</td><td>...</td><td>1.27</td><td>2.55</td><td>...</td><td>...</td><td>1.22</td><td>.37</td><td>.28</td></tr><tr><td>1946-50</td><td>....</td><td>.0050</td><td>.0029</td><td>...</td><td>...</td><td>.0044</td><td>.031</td><td>.047</td><td>...</td><td>...</td><td>.20</td><td>.04</td><td>...</td><td>...</td><td>1.27</td><td>.48</td><td>...</td><td>...</td><td>1.10</td><td>.39</td><td>.33</td></tr><tr><td>1951-55</td><td>....</td><td>.0123</td><td>.0024</td><td>...</td><td>...</td><td>.0111</td><td>.019</td><td>.035</td><td>...</td><td>...</td><td>.20</td><td>.08</td><td>...</td><td>...</td><td>5.06</td><td>.53</td><td>...</td><td>...</td><td>4.56</td><td>.24</td><td>.29</td></tr><tr><td>1956-60</td><td>....</td><td>.0148</td><td>-.0059</td><td>...</td><td>...</td><td>.0128</td><td>.020</td><td>.034</td><td>...</td><td>...</td><td>.37</td><td>.18</td><td>...</td><td>...</td><td>5.68</td><td>-1.37</td><td>...</td><td>...</td><td>4.89</td><td>.22</td><td>.31</td></tr><tr><td>1961-6/68</td><td>..</td><td>.0001</td><td>.0143</td><td>...</td><td>...</td><td>-.0029</td><td>.034</td><td>.048</td><td>...</td><td>...</td><td>.22</td><td>.09</td><td>...</td><td>...</td><td>.03</td><td>2.81</td><td>...</td><td>...</td><td>-.80</td><td>.32</td><td>.27</td></tr><tr><td colspan="21">Panel B:</td><td></td></tr><tr><td>1935-6/68</td><td>..</td><td>.0049</td><td>.0105</td><td>-.0008</td><td>...</td><td>.0036</td><td>.052</td><td>.118</td><td>.056</td><td>...</td><td>.03</td><td>-.11</td><td>-.11</td><td>...</td><td>1.92</td><td>1.79</td><td>-.29</td><td>...</td><td>1.42</td><td>.32</td><td>.31</td></tr><tr><td>1935-45</td><td>....</td><td>.0074</td><td>.0079</td><td>.0040</td><td>...</td><td>.0073</td><td>.061</td><td>.139</td><td>.074</td><td>...</td><td>-.10</td><td>-.31</td><td>-.21</td><td>...</td><td>1.39</td><td>.65</td><td>.61</td><td>...</td><td>1.36</td><td>.32</td><td>.30</td></tr><tr><td>1946-55</td><td>....</td><td>-.0002</td><td>.0217</td><td>-.0087</td><td>...</td><td>-.0012</td><td>.036</td><td>.095</td><td>.034</td><td>...</td><td>.04</td><td>.00</td><td>.00</td><td>...</td><td>-.07</td><td>2.51</td><td>-2.83</td><td>...</td><td>-.38</td><td>.36</td><td>.32</td></tr><tr><td>1956-6/68</td><td>..</td><td>.0069</td><td>.0040</td><td>.0013</td><td>...</td><td>.0043</td><td>.054</td><td>.116</td><td>.053</td><td>...</td><td>.17</td><td>.07</td><td>.03</td><td>...</td><td>1.56</td><td>.42</td><td>.29</td><td>...</td><td>.97</td><td>.30</td><td>.30</td></tr><tr><td>1935-40</td><td>....</td><td>.0013</td><td>.0141</td><td>-.0017</td><td>...</td><td>.0012</td><td>.069</td><td>.160</td><td>.075</td><td>...</td><td>-.13</td><td>-.36</td><td>-.35</td><td>...</td><td>.16</td><td>.75</td><td>-.19</td><td>...</td><td>.14</td><td>.24</td><td>.30</td></tr><tr><td>1941-45</td><td>....</td><td>.0148</td><td>.0004</td><td>.0108</td><td>...</td><td>.0146</td><td>.050</td><td>.111</td><td>.073</td><td>...</td><td>-.04</td><td>-.19</td><td>-.04</td><td>...</td><td>2.28</td><td>.03</td><td>1.15</td><td>...</td><td>2.24</td><td>.39</td><td>.29</td></tr><tr><td>1946-50</td><td>....</td><td>-.0008</td><td>.0152</td><td>-.0051</td><td>...</td><td>-.0015</td><td>.037</td><td>.104</td><td>.032</td><td>...</td><td>.14</td><td>.04</td><td>.00</td><td>...</td><td>-.18</td><td>1.14</td><td>-1.24</td><td>...</td><td>-.32</td><td>.44</td><td>.32</td></tr><tr><td>1951-55</td><td>....</td><td>.0004</td><td>.0281</td><td>-.0122</td><td>...</td><td>-.0008</td><td>.030</td><td>.085</td><td>.035</td><td>...</td><td>-.17</td><td>-.14</td><td>-.01</td><td>...</td><td>.10</td><td>2.55</td><td>-2.72</td><td>...</td><td>-.20</td><td>.28</td><td>.29</td></tr><tr><td>1956-60</td><td>....</td><td>.0128</td><td>-.0015</td><td>-.0020</td><td>...</td><td>.0108</td><td>.030</td><td>.072</td><td>.029</td><td>...</td><td>.35</td><td>.11</td><td>.26</td><td>...</td><td>3.38</td><td>-.16</td><td>-.54</td><td>...</td><td>2.84</td><td>.25</td><td>.31</td></tr><tr><td>1961-6/68</td><td>..</td><td>.0029</td><td>.0077</td><td>.0034</td><td>...</td><td>-.0000</td><td>.066</td><td>.138</td><td>.064</td><td>...</td><td>.14</td><td>.06</td><td>-.01</td><td>...</td><td>.42</td><td>.53</td><td>.51</td><td>...</td><td>-.01</td><td>.34</td><td>.29</td></tr><tr><td colspan="2" rowspan="2">PERIOD</td><td colspan="20">STATISTIC</td></tr><tr><td> $\widehat{\gamma}_{0}$ </td><td> $\widehat{\gamma}_{1}$ </td><td> $\widehat{\gamma}_{2}$ </td><td> $\widehat{\gamma}_{3}$ </td><td> $\widehat{\gamma}_{0}-R_{f}$ </td><td> $s(\widehat{\gamma}_{0})$ </td><td> $s(\widehat{\gamma}_{1})$ </td><td> $s(\widehat{\gamma}_{2})$ </td><td> $s(\widehat{\gamma}_{3})$ </td><td> $\rho_{0}(\widehat{\gamma}_{0}-R_{f})$ </td><td> $\rho_{M}(\widehat{\gamma}_{1})$ </td><td> $\rho_{0}(\widehat{\gamma}_{2})$ </td><td> $\rho_{0}(\widehat{\gamma}_{3})$ </td><td> $t(\widehat{\gamma}_{0})$ </td><td> $t(\widehat{\gamma}_{1})$ </td><td> $t(\widehat{\gamma}_{2})$ </td><td> $t(\widehat{\gamma}_{3})$ </td><td> $t(\widehat{\gamma}_{0}-R_{f})$ </td><td> $\bar{r}^{2}$ </td><td> $s(r^{2})$ </td></tr><tr><td colspan="22">Panel C:</td></tr><tr><td>1935-6/68</td><td>..</td><td>.0054</td><td>.0072</td><td>...</td><td>.0198</td><td>.0041</td><td>.052</td><td>.065</td><td>...</td><td>.868</td><td>.04</td><td>-.12</td><td>...</td><td>-.04</td><td>2.10</td><td>2.20</td><td>...</td><td>.46</td><td>1.59</td><td>.32</td><td>.31</td></tr><tr><td>1935-45</td><td>....</td><td>.0017</td><td>.0104</td><td>...</td><td>.0841</td><td>.0015</td><td>.073</td><td>.083</td><td>...</td><td>.921</td><td>-.00</td><td>-.26</td><td>...</td><td>-.08</td><td>.26</td><td>1.41</td><td>...</td><td>1.05</td><td>.24</td><td>.32</td><td>.31</td></tr><tr><td>1946-55</td><td>....</td><td>.0110</td><td>.0075</td><td>...</td><td>-.1052</td><td>.0100</td><td>.032</td><td>.056</td><td>...</td><td>.609</td><td>.08</td><td>.02</td><td>...</td><td>-.20</td><td>3.78</td><td>1.47</td><td>...</td><td>-1.89</td><td>3.46</td><td>.34</td><td>.32</td></tr><tr><td>1956-6/68</td><td>..</td><td>.0042</td><td>.0041</td><td>...</td><td>.0633</td><td>.0016</td><td>.040</td><td>.052</td><td>...</td><td>.984</td><td>.12</td><td>.08</td><td>...</td><td>.03</td><td>1.28</td><td>.96</td><td>...</td><td>.79</td><td>.50</td><td>.30</td><td>.29</td></tr><tr><td>1935-40</td><td>....</td><td>.0036</td><td>.0119</td><td>...</td><td>-.0170</td><td>.0035</td><td>.082</td><td>.105</td><td>...</td><td>.744</td><td>-.03</td><td>-.26</td><td>...</td><td>-.18</td><td>.37</td><td>.97</td><td>...</td><td>-.19</td><td>.36</td><td>.25</td><td>.30</td></tr><tr><td>1941-45</td><td>....</td><td>-.0006</td><td>.0085</td><td>...</td><td>.2053</td><td>-.0009</td><td>.061</td><td>.052</td><td>...</td><td>1.091</td><td>.07</td><td>-.29</td><td>...</td><td>-.02</td><td>-.08</td><td>1.25</td><td>...</td><td>1.46</td><td>-.11</td><td>.41</td><td>.30</td></tr><tr><td>1946-50</td><td>....</td><td>.0069</td><td>.0081</td><td>...</td><td>-.0920</td><td>.0062</td><td>.034</td><td>.066</td><td>...</td><td>.504</td><td>.14</td><td>.06</td><td>...</td><td>-.02</td><td>1.56</td><td>.95</td><td>...</td><td>-1.41</td><td>1.40</td><td>.42</td><td>.33</td></tr><tr><td>1951-55</td><td>....</td><td>.0150</td><td>.0069</td><td>...</td><td>-.1185</td><td>.0138</td><td>.029</td><td>.043</td><td>...</td><td>.702</td><td>.06</td><td>-.18</td><td>...</td><td>-.32</td><td>4.05</td><td>1.24</td><td>...</td><td>-1.31</td><td>3.72</td><td>.27</td><td>.29</td></tr><tr><td>1956-60</td><td>....</td><td>.0127</td><td>-.0081</td><td>...</td><td>.0728</td><td>.0107</td><td>.037</td><td>.045</td><td>...</td><td>1.164</td><td>.15</td><td>.15</td><td>...</td><td>.21</td><td>2.68</td><td>-1.40</td><td>...</td><td>.48</td><td>2.26</td><td>.26</td><td>.30</td></tr><tr><td>1961-6/68</td><td>..</td><td>-.0014</td><td>.0122</td><td>...</td><td>.0570</td><td>-.0044</td><td>.042</td><td>.055</td><td>...</td><td>.850</td><td>.10</td><td>.00</td><td>...</td><td>-.19</td><td>-.32</td><td>2.12</td><td>...</td><td>.64</td><td>-.98</td><td>.33</td><td>.27</td></tr><tr><td colspan="22">Panel D:</td></tr><tr><td>1935-6/68</td><td>..</td><td>.0020</td><td>.0114</td><td>-.0026</td><td>.0516</td><td>.0008</td><td>.075</td><td>.123</td><td>.060</td><td>.929</td><td>-.09</td><td>-.09</td><td>-.12</td><td>-.10</td><td>.55</td><td>1.85</td><td>-.86</td><td>1.11</td><td>.20</td><td>.34</td><td>.31</td></tr><tr><td>1935-45</td><td>....</td><td>.0011</td><td>.0118</td><td>-.0009</td><td>.0817</td><td>.0010</td><td>.103</td><td>.146</td><td>.079</td><td>1.003</td><td>-.20</td><td>-.23</td><td>-.24</td><td>-.15</td><td>.13</td><td>.94</td><td>-.14</td><td>.94</td><td>.11</td><td>.34</td><td>.31</td></tr><tr><td>1946-55</td><td>....</td><td>.0017</td><td>.0209</td><td>-.0076</td><td>-.0378</td><td>.0008</td><td>.042</td><td>.096</td><td>.038</td><td>.619</td><td>-.10</td><td>-.00</td><td>-.01</td><td>-.20</td><td>.44</td><td>2.39</td><td>-2.16</td><td>-.67</td><td>.20</td><td>.36</td><td>.32</td></tr><tr><td>1956-6/68</td><td>..</td><td>.0031</td><td>.0034</td><td>-.0000</td><td>.0966</td><td>.0005</td><td>.065</td><td>.122</td><td>.055</td><td>1.061</td><td>.12</td><td>.03</td><td>.01</td><td>-.05</td><td>.59</td><td>.34</td><td>-.00</td><td>1.11</td><td>.10</td><td>.32</td><td>.29</td></tr><tr><td>1935-40</td><td>....</td><td>.0009</td><td>.0156</td><td>-.0029</td><td>.0025</td><td>.0008</td><td>.112</td><td>.171</td><td>.085</td><td>.826</td><td>-.16</td><td>-.23</td><td>-.26</td><td>-.12</td><td>.07</td><td>.78</td><td>-.29</td><td>.03</td><td>.06</td><td>.26</td><td>.30</td></tr><tr><td>1941-45</td><td>....</td><td>.0015</td><td>.0073</td><td>.0014</td><td>.1767</td><td>.0012</td><td>.092</td><td>.109</td><td>.072</td><td>1.181</td><td>-.28</td><td>-.21</td><td>-.22</td><td>-.18</td><td>.12</td><td>.52</td><td>.15</td><td>1.16</td><td>.10</td><td>.43</td><td>.31</td></tr><tr><td>1946-50</td><td>....</td><td>.0011</td><td>.0141</td><td>-.0040</td><td>-.0313</td><td>.0004</td><td>.047</td><td>.106</td><td>.042</td><td>.590</td><td>-.10</td><td>.03</td><td>-.01</td><td>-.12</td><td>.18</td><td>1.03</td><td>-.73</td><td>-.41</td><td>.07</td><td>.44</td><td>.33</td></tr><tr><td>1951-55</td><td>....</td><td>.0023</td><td>.0277</td><td>-.0112</td><td>-.0443</td><td>.0011</td><td>.037</td><td>.085</td><td>.034</td><td>.651</td><td>-.11</td><td>-.13</td><td>-.01</td><td>-.28</td><td>.48</td><td>2.53</td><td>-2.54</td><td>-.53</td><td>.23</td><td>.29</td><td>.30</td></tr><tr><td>1956-60</td><td>....</td><td>.0103</td><td>-.0047</td><td>-.0020</td><td>.0979</td><td>.0083</td><td>.049</td><td>.078</td><td>.032</td><td>1.286</td><td>-.16</td><td>.19</td><td>-.01</td><td>.02</td><td>1.63</td><td>-.47</td><td>-.49</td><td>.59</td><td>1.31</td><td>.28</td><td>.30</td></tr><tr><td>1961-6/68</td><td>..</td><td>-.0017</td><td>.0088</td><td>.0013</td><td>.0957</td><td>-.0046</td><td>.073</td><td>.144</td><td>.066</td><td>.887</td><td>.20</td><td>.00</td><td>.01</td><td>-.15</td><td>-.21</td><td>.58</td><td>.19</td><td>1.02</td><td>-.60</td><td>.35</td><td>.29</td></tr></table>

Inferences based on approximate normality are on even safer ground if one assumes, again in line with the results of Officer (1971), that although they are well approximated by stable nonnormal distributions with  $\alpha \cong 1.8$ , distributions of monthly returns in fact have finite variances and converge—but very slowly—toward the normal as one takes sums or averages of individual returns. Then the distributions of the means of month-by-month regression coefficients from the risk-return model are likely to be close to normal since each mean is based on coefficients for many months.

## A. Tests of the Major Hypotheses of the Two-Parameter Model

Consider first condition C2 of the two-parameter model, which says that no measure of risk, in addition to $\beta$, systematically affects expected returns. This hypothesis is not rejected by the results in panels C and D of table 3. The values of $t(\hat{\gamma}_3)$ are small, and the signs of the $t(\bar{\gamma}_3)$ are randomly positive and negative.

Likewise, the results in panels B and D of table 3 do not reject condition C1 of the two-parameter model, which says that the relationship between expected return and $\beta$ is linear. In panel B, the value of $t(\overline{\hat{\gamma}}_2)$ for the overall period 1935-6/68 is only -.29. In the 5-year subperiods, $t(\overline{\hat{\gamma}}_2)$ for 1951-55 is approximately -2.7, but for subperiods that do not cover 1951-55, the values of $t(\overline{\hat{\gamma}}_2)$ are much closer to zero.

So far, then, the two-parameter model seems to be standing up well to the data. All is for naught, however, if the critical condition C3 is rejected. That is, we are not happy with the model unless there is on average a positive tradeoff between risk and return. This seems to be the case. For the overall period 1935–6/68,  $t(\bar{\hat{\gamma}}_{1})$  is large for all models. Except for the period 1956–60, the values of  $t(\bar{\hat{\gamma}}_{1})$  are also systematically positive in the subperiods, but not so systematically large.

The small $t$-statistics for subperiods reflect the substantial month-to-month variability of the parameters of the risk-return regressions. For example, in the one-variable regressions summarized in panel A, for the period 1935-40, $\overline{\hat{\gamma}}_1 = .0109$. In other words, for this period the average incremental return per unit of $\beta$ was almost 1.1 percent per month, so that on average, bearing risk had substantial rewards. Nevertheless, because of the variability of $\hat{\gamma}_{1t}$—in this period $s(\hat{\gamma}_1)$ is 11.6 percent per month (!)—$t(\overline{\hat{\gamma}}_1)$ is only .79. It takes the statistical power of the large sample for the overall period before values of $\overline{\hat{\gamma}}_1$ that are large in practical terms also yield large $t$-values.

But at least with the sample of the overall period $t(\widehat{\gamma}_1)$ achieves values supportive of the conclusion that on average there is a statistically observable positive relationship between return and risk. This is not the case with respect to $t(\widehat{\gamma}_2)$ and $t(\widehat{\gamma}_3)$. Even, or indeed especially, for the overall period, these $t$-statistics are close to zero.

The behavior through time of  $\hat{\gamma}_{1t}$ ,  $\hat{\gamma}_{2t}$ , and  $\hat{\gamma}_{3t}$  is also consistent with hypothesis ME that the capital market is efficient. The serial correlations  $\rho_{M}(\hat{\gamma}_{1})$ ,  $\rho_{0}(\hat{\gamma}_{2})$ , and  $\rho_{0}(\hat{\gamma}_{3})$ , are always low in terms of explanatory power and generally low in terms of statistical significance. The proportion of the variance of  $\tilde{\gamma}_{jt}$  explained by first-order serial correlation is estimated by  $\rho(\hat{\gamma}_{j})^{2}$  which in all cases is small. As for statistical significance, under the hypothesis that the true serial correlation is zero, the standard deviation of the sample coefficient can be approximated by  $\sigma(\hat{\rho}) = 1/\sqrt{n}$ . For the overall period,  $\sigma(\hat{\rho})$  is approximately .05, while for the 10- and 5-year subperiods  $\sigma(\hat{\rho})$  is approximately .09 and .13, respectively. Thus, the values of  $\rho_{M}(\hat{\gamma}_{1})$ ,  $\rho_{0}(\hat{\gamma}_{2})$ , and  $\rho_{0}(\hat{\gamma}_{3})$  in table 3 are generally statistically close to zero. The exceptions involve primarily periods that include the 1935–40 subperiod, and the results for these periods are not independent. $^{8}$

To conserve space, the serial correlations of the portfolio residuals,  $\hat{\eta}_{pt}$ , are not shown. In these serial correlations, negative values predominate. But like the serial correlations of the  $\hat{\gamma}$ 's, those of the  $\hat{\eta}$ 's are close to zero. Higher-order serial correlations of the  $\hat{\gamma}$ 's and  $\hat{\eta}$ 's have been computed, and these also are never systematically large.

In short, one cannot reject the hypothesis that the pricing of securities is in line with the implications of the two-parameter model for expected returns. And given a two-parameter pricing model, the behavior of returns through time is consistent with an efficient capital market.

## B. The Behavior of the Market

Some perspective on the behavior of the market during different periods and on the interpretation of the coefficients  $\hat{\gamma}_{0t}$  and  $\hat{\gamma}_{1t}$  in the risk-return regressions can be obtained from table 4. For the various periods of table 3, table 4 shows the sample means (and with some exceptions), the standard

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$\hat{\gamma}_{2}$</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$\hat{\gamma}_{3}$</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$= 0$</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$\rho_{0}(\hat{\gamma}_{0)t}-R_{ft})$</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$\hat{\gamma}_{0t}$</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$^{8}$  The serial correlations of  $\hat{\gamma}_{2}$  and  $\hat{\gamma}_{3}$  about means that are assumed to be zero provide a test of the fair game property of an efficient market, given that expected returns are generated by the two-parameter model—that is, given  $E(\hat{\gamma}_{2t}) = E(\hat{\gamma}_{3t}) = 0$ . Likewise,  $\rho_{0}(\hat{\gamma}_{0t} - R_{ft})$  provides a test of market efficiency with respect to the behavior of  $\hat{\gamma}_{0t}$  through time, given the validity of the Sharpe-Lintner hypothesis (about which we have as yet said nothing). But, at least for  $\hat{\gamma}_{2t}$  and  $\hat{\gamma}_{3t}$ , computing the serial correlations about sample means produces essentially the same results.</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$E(\widetilde{\gamma}_{2t}) = E(\widetilde{\gamma}_{3t})$</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$\hat{\gamma}_{2t}$</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$\widehat{\gamma}_{3t}$</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$\widetilde{\gamma}_{1t} - [E(\widetilde{R}_{mt}) - E(\widetilde{R}_{0t})]$</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$\left|\widehat{\gamma}_{1t}\right|$</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$E(\tilde{R}_{mt}) - E(\tilde{R}_{0t})$</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$\rho_{,Y}(\hat{\Upsilon}_{1})$</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$E(\widetilde{R}_{mt}) - E(\widetilde{R}_{0tt})$</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$\hat{\gamma}_{1t}$</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">To test the market efficiency hypothesis on $\widetilde{\gamma}_{1t} - [E(\widetilde{R}_{mt}) - E(\widetilde{R}_{0t})]$, the sample mean of the $\hat{\gamma}_{1t}$ is used to estimate $E(\widetilde{R}_{mt}) - E(\widetilde{R}_{0t})$, thus implicitly assuming that the expected risk premium is constant. That this is a reasonable approximation [in the sense that the $\rho_{1I}(\hat{\gamma}_1)$ are small], probably reflects the fact that variation in $E(\widetilde{R}_{mt}) - E(\widetilde{R}_{0t})$ is trivial relative to the month-by-month variation in $\hat{\gamma}_{1t}$.</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">Finally, it is well to note that in terms of the implications of the serial correlations for making good portfolio decisions—and thus for judging whether market efficiency is a workable representation of reality—the fact that the 'serial correlations are low in terms of explanatory power is more important than whether or not they are low in terms of statistical significance.</span></small>

TABLE 4

THE BEHAVIOR OF THE MARKET

<table><tr><td rowspan="2">PERIOD</td><td colspan="9"> $STATISTIC^*$ </td></tr><tr><td> $\overline{R_m}$ </td><td> $\overline{R_m - R_f}$ </td><td> $\widehat{\gamma}_1$ </td><td> $\widehat{\gamma}_0$ </td><td> $\overline{R_f}$ </td><td> $\frac{\overline{R_m - R_f}}{s(R_m)}$ </td><td> $\widehat{\gamma}_1$ </td><td> $s(R_m)$ </td><td> $s(R_m)$ </td></tr><tr><td>1935-6/68 ......</td><td>.0143</td><td>.0130</td><td>.0085</td><td>.0061</td><td>.0013</td><td>.2136</td><td>.1388</td><td>.061</td><td>.066</td></tr><tr><td>1935-45 ......</td><td>.0197</td><td>.0195</td><td>.0163</td><td>.0039</td><td>.0002</td><td>.2207</td><td>.1844</td><td>.089</td><td>.098</td></tr><tr><td>1946-55 ......</td><td>.0112</td><td>.0103</td><td>.0027</td><td>.0087</td><td>.0009</td><td>.2378</td><td>.0614</td><td>.043</td><td>.041</td></tr><tr><td>1956-6/68 ......</td><td>.0121</td><td>.0095</td><td>.0062</td><td>.0060</td><td>.0026</td><td>.2387</td><td>.1560</td><td>.040</td><td>.044</td></tr><tr><td>1935-40 ......</td><td>.0132</td><td>.0132</td><td>.0109</td><td>.0024</td><td>.0001</td><td>.1221</td><td>.1009</td><td>.108</td><td>.116</td></tr><tr><td>1941-45 ......</td><td>.0274</td><td>.0272</td><td>.0229</td><td>.0056</td><td>.0002</td><td>.4715</td><td>.3963</td><td>.058</td><td>.069</td></tr><tr><td>1946-50 ......</td><td>.0077</td><td>.0070</td><td>.0029</td><td>.0050</td><td>.0007</td><td>.1351</td><td>.0564</td><td>.052</td><td>.047</td></tr><tr><td>1951-55 ......</td><td>.0148</td><td>.0136</td><td>.0024</td><td>.0123</td><td>.0012</td><td>.4174</td><td>.0735</td><td>.033</td><td>.035</td></tr><tr><td>1956-60 ......</td><td>.0090</td><td>.0070</td><td>-.0059</td><td>.0148</td><td>.0020</td><td>.2080</td><td>-.1755</td><td>.034</td><td>.034</td></tr><tr><td>1961-6/68 ......</td><td>.0141</td><td>.0111</td><td>.0143</td><td>.0001</td><td>.0030</td><td>.2567</td><td>.3294</td><td>.043</td><td>.048</td></tr></table>

\* Since $s(R_f)$ is so small relative to $s(R_m)$, $s(R_m - R_f)$, which is not shown, is essentially the same as $s(R_m)$. The standard deviations of $(R_m - R_f)/s(R_m)$ and $\widehat{\gamma}_1/s(R_m)$, also not shown, can be obtained directly from $s(R_m - R_f)$, $s(\widehat{\gamma}_1)$ and $s(R_m)$. Finally, the $t$-statistics for $(\overline{R_m - R_f})/s(R_m)$ and $\overline{\widehat{\gamma}_1}/s(R_m)$ are identical with those for $\overline{R_m - R_f}$ and $\widehat{\gamma}_1$.

deviations, $t$-statistics for sample means, and first-order serial correlations for the month-by-month values of the following variables and coefficients: the market return $R_{mt}$; the riskless rate of interest $R_{ft}$, taken to be the yield on 1-month Treasury bills; $R_{mt} - R_{ft}$; $(R_{mt} - R_{ft}) / s(R_m)$; $\hat{\gamma}_{0t}$ and $\hat{\gamma}_{1t}$, repeated from panel A of table 3; and $\hat{\gamma}_{1t} / s(R_m)$. The $t$-statistics on sample means are computed in the same way as those in table 3.

If the two-parameter model is valid, then in equation (7),  $E(\widetilde{\gamma}_{0t}) = E(\widetilde{R}_{0t})$ , where  $E(\widetilde{R}_{0t})$  is the expected return on any zero- $\beta$  security or portfolio. Likewise, the expected risk premium per unit of  $\beta$  is  $E(\widetilde{R}_{mt}) - E(\widetilde{R}_{0t}) = E(\widetilde{\gamma}_{1t})$ . In fact, for the one-variable regressions of panel A, table 3, that is,

$$
R _ {p t} = \hat {\gamma} _ {0 t} + \hat {\gamma} _ {1 t} \hat {\beta} _ {p} + \hat {\eta} _ {p t},\tag{11}
$$

we have, period by period,

$$
\hat {\gamma} _ {1 t} = R _ {m t} - \hat {\gamma} _ {0 t}.\tag{12}
$$

This condition is obtained by averaging (11) over $p$ and making use of the least-squares constraint

$$
\underset {p} {\Sigma} \hat {\eta} _ {p t} = 0.
$$

Moreover, the least-squares estimate $\hat{\gamma}_{0t}$ can always be interpreted as the return for month $t$ on a zero-$\hat{\beta}$ portfolio, where the weights given to each of the 20 portfolios to form this zero- $\hat{\beta}$ portfolio are the least-squares weights that are applied to the $R_{pt}$ in computing $\hat{\gamma}_{0t}$. $^{10}$

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$\widehat{\beta}_{p}$</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">p</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$R_{pt}$</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$R_{mt}$</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$\hat{\beta}_{p}$</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$R_{pt}$</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$^{9}$  There is some degree of approximation in (12). The averages over p of  $R_{pt}$  and  $\widehat{\beta}_{p}$  are  $R_{mt}$  and 1.0, respectively, only if every security in the market is in some portfolio. With our methodology (see table 1) this is never true. But the degree of approximation turns out to be small: The average of the  $R_{pt}$  is always close to  $R_{mt}$  and the average  $\widehat{\beta}_{p}$  is always close to 1.0.</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$R_{mt}$</span></small>

TABLE 4 (Continued)

<table><tr><td colspan="11"> $STATISTIC^*$ </td></tr><tr><td> $s(\widehat{\gamma}_0)$ </td><td> $s(R_f)$ </td><td> $t(\overline{R}_m)$ </td><td> $t(\overline{R_m - R_f})$ </td><td> $t(\widehat{\gamma}_1)$ </td><td> $t(\widehat{\gamma}_0)$ </td><td> $\rho_M(R_m)$ </td><td> $\rho_M(R_m - R_f)$ </td><td> $\rho_M(\widehat{\gamma}_1)$ </td><td> $\rho_M(\widehat{\gamma}_0)$ </td><td> $\rho_M(R_f)$ </td></tr><tr><td>.038</td><td>.0012</td><td>4.71</td><td>4.28</td><td>2.57</td><td>3.24</td><td>-.01</td><td>-.01</td><td>.02</td><td>.14</td><td>.98</td></tr><tr><td>.052</td><td>.0001</td><td>2.56</td><td>2.54</td><td>1.92</td><td>.86</td><td>-.07</td><td>-.07</td><td>-.03</td><td>.10</td><td>.88</td></tr><tr><td>.026</td><td>.0004</td><td>2.84</td><td>2.60</td><td>.70</td><td>3.71</td><td>.09</td><td>.09</td><td>.07</td><td>.10</td><td>.94</td></tr><tr><td>.030</td><td>.0009</td><td>3.72</td><td>2.92</td><td>1.73</td><td>2.45</td><td>.14</td><td>.14</td><td>.15</td><td>.25</td><td>.92</td></tr><tr><td>.064</td><td>.0001</td><td>1.04</td><td>1.04</td><td>.79</td><td>.32</td><td>-.13</td><td>-.13</td><td>-.09</td><td>.07</td><td>.72</td></tr><tr><td>.034</td><td>.0001</td><td>3.68</td><td>3.65</td><td>2.55</td><td>1.27</td><td>.14</td><td>.14</td><td>.15</td><td>.21</td><td>.83</td></tr><tr><td>.031</td><td>.0003</td><td>1.15</td><td>1.05</td><td>.48</td><td>1.27</td><td>.09</td><td>.09</td><td>.04</td><td>.18</td><td>.97</td></tr><tr><td>.019</td><td>.0004</td><td>3.51</td><td>3.22</td><td>.53</td><td>5.06</td><td>-.02</td><td>-.01</td><td>.08</td><td>-.07</td><td>.89</td></tr><tr><td>.020</td><td>.0007</td><td>2.07</td><td>1.60</td><td>-1.37</td><td>5.68</td><td>.12</td><td>.13</td><td>.18</td><td>.13</td><td>.80</td></tr><tr><td>.034</td><td>.0008</td><td>3.08</td><td>2.44</td><td>2.81</td><td>.03</td><td>.13</td><td>.13</td><td>.09</td><td>.21</td><td>.93</td></tr></table>

In the Sharpe-Lintner two-parameter model of market equilibrium $E(\widetilde{\gamma}_{0t}) = E(\widetilde{R}_{0t}) = R_{ft}$ and $E(\widetilde{\gamma}_{1t}) = E(\widetilde{R}_{mt}) - E(\widetilde{R}_{0t}) = E(\widetilde{\mathbf{R}}_{mt}) - R_{ft}$. In the period 1935-40 and in the most recent period 1961-6/68, $\widehat{\gamma}_{1t}$ is close to $\overline{R_m - R_f}$ and the $t$-statistics for the two averages are similar. In other periods, and especially in the period 1951-60, $\widehat{\gamma}_1$ is substantially less than $\overline{R_m - R_f}$. This is a consequence of the fact that for these periods $\widehat{\gamma}_0$ is noticeably greater than $\overline{R}_f$. In economic terms, the tradeoff of average return for risk between common stocks and short-term bonds has been more consistently large through time than the tradeoff of average return for risk among common stocks. Testing whether the differences between $\overline{R_m - R_f}$ and $\widehat{\gamma}_1$ are statistically large, however, is equivalent to testing the S-L hypothesis $E(\widetilde{\gamma}_{0t}) = R_{ft}$, which we prefer to take up after examining further the stochastic process generating monthly returns.

Finally, although the differences between values of  $\overline{R_{m}-R_{f}}$  for different periods or between values of  $\hat{\gamma}_{1}$  are never statistically large, there is a hint in table 4 that average-risk premiums declined from the pre- to the post-World War II periods. These are average risk premiums per unit of  $\hat{\beta}$ , however, which are not of prime interest to the investor. In making his portfolio decision, the investor is more concerned with the tradeoff of expected portfolio return for dispersion of return—that is, the slope of the efficient set of portfolios. In the Sharpe-Lintner model this slope is always  $[E(\widetilde{R}_{mt}) - R_{ft}]/\sigma(\widetilde{R}_{mt})$ , and in the more general model of Black (1972), it is  $[E(\widetilde{R}_{mt}) - E(\widetilde{R}_{0t})]/\sigma(\widetilde{R}_{mt})$  at the point on the efficient set corresponding to the market portfolio m. In table 4, especially for the three long subperiods, dividing  $\overline{R_{m} - R_{f}}$  and  $\widehat{\gamma}_{1}$ , by  $s(R_{m})$  seems to yield estimated risk premiums that are more constant through time. This results from the fact that any declines in  $\widehat{\gamma}_{1}$  or  $\overline{R_{m} - R_{f}}$  are matched by a quite noticeable downward shift in  $s(R_{m})$  from the early to the later periods (cf. Blume [1970] or Officer [1971]).

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$\left|\widehat{\gamma}_{0t}\right|$</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$\widetilde{\eta}_{pt}$</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">p,</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">p,</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">zero-β</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$\left|\hat{\gamma}_{0t}\right|$</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$\hat{\beta}_{p}$</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$^{10}$  That  $\hat{\gamma}_{0t}$  is the return on a zero- $\hat{\beta}$  portfolio can be shown to follow from the unbiasedness of the least-squares coefficients in the cross-sectional risk-return regressions. If one makes the Gauss-Markov assumptions that the underlying disturbances  $\tilde{\eta}_{pt}$  of (11) have zero means, are uncorrelated across p, and have the same variance for all p, then it follows almost directly from the Gauss-Markov Theorem that the least-squares estimate  $\hat{\gamma}_{0t}$  is also the return for month t on the minimum variance zero- $\hat{\beta}$  portfolio that can be constructed from the 20 portfolio  $\hat{\beta}_{p}$ .</span></small>

## C. Errors and True Variation in the Coefficients $\hat{\gamma}_{jt}$

Each cross-sectional regression coefficient $\hat{\gamma}_{jt}$ in (10) has two components: the true $\tilde{\gamma}_{jt}$ and the estimation error, $\tilde{\phi}_{jt} = \hat{\gamma}_{jt} - \tilde{\gamma}_{jt}$. A natural question is: To what extent is the variation in $\hat{\gamma}_{jt}$ through time due to variation in $\tilde{\gamma}_{jt}$ and to what extent is it due to $\tilde{\phi}_{jt}$? In addition to providing important information about the precision of the coefficient estimates used to test the two-parameter model, the answer to this question can be used to test hypotheses about the stochastic process generating returns. For example, although we cannot reject the hypothesis that $E(\tilde{\gamma}_{2t}) = 0$, does including the term involving $\hat{\beta}_p^2$ in (10) help in explaining the month-by-month behavior of returns? That is, can we reject the hypothesis that for all $t$, $\tilde{\gamma}_{2t} = 0$? Likewise, can we reject the hypothesis that month-by-month $\tilde{\gamma}_{3t} = 0$? And is the variation through time in $\hat{\gamma}_{0t}$ due entirely to $\tilde{\phi}_{0t}$ and to variation in $R_{ft}$?

The answers to these questions are in table 5. For the models and time periods of table 3, table 5 shows for each $\hat{\gamma}_j$: $s^2 (\hat{\gamma}_j)$, the sample variance of the month-by-month $\hat{\gamma}_{jt}$; $s^2 (\widetilde{\phi}_j)$, the average of the month-by-month values of $s^2 (\widetilde{\phi}_{jt})$, where $s(\widetilde{\phi}_{jt})$ is the standard error of $\hat{\gamma}_{jt}$ from the cross-sectional risk-return regression of (10) for month $t$; $s^2 (\widetilde{\gamma}_j)\equiv s^2 (\hat{\gamma}_j) - s^2 (\widetilde{\phi}_j)$; and the $F$-statistic $F = s^2 (\hat{\gamma}_j) / s^2 (\widetilde{\phi}_j)$, which is relevant for testing the hypothesis, $s^2 (\hat{\gamma}_j) = s^2 (\widetilde{\phi}_j)$. The numerator of $F$ has $n - 1$ df, where $n$ is the number of months in the sample period; and the denominator has $n(20 - K)$ df, where $K$ is the number of coefficients $\hat{\gamma}_j$ in the model.$^{11}$

$^{11}$  The standard error of  $\hat{\gamma}_{jt}$ ,  $s(\widetilde{\phi}_{jt})$ , is proportional to the standard error of the risk-return residuals,  $\widehat{\eta}_{pt}$ , for month t, which has 20 - K df. And n values of  $s^{2}(\widetilde{\phi}_{jt})$  are averaged to get  $s^{2}(\widetilde{\phi}_{j})$ , so that the latter has  $n(20 - K)$  df. Note that if the underlying return disturbances  $\widetilde{\eta}_{pt}$  of (10) are independent across p and have identical normal distributions for all p, then  $\hat{\gamma}_{jt}$  is the sample mean of a normal distribution and  $s^{2}(\widetilde{\phi}_{jt})$  is proportional to the sample variance of the same normal distribution. If the process is also assumed to be stationary through time, it then follows that  $s^{2}(\hat{\gamma}_{jt})$  and  $s^{2}(\widetilde{\phi}_{jt})$  are independent, as required by the F-test. Finally, in the F-statistics of table 5, the values of n are 60 or larger, so that, since K is from 2 to 4,  $n(20 - K) \geqslant 960$ . From Mood and Graybill (1963), some upper percentage points of the F-distribution are:

One clear-cut result in table 5 is that there is a substantial decline in the reliability of the coefficients $\hat{\gamma}_{0t}$ and $\hat{\gamma}_{1t}$—that is, a substantial increase in $s^2(\overline{\phi_0})$ and $s^2(\overline{\phi_1})$—when $\hat{\beta}_p^2$ and/or $\bar{s}_p(\hat{\epsilon}_j)$ are included in the risk-return regressions. The variable $\hat{\beta}_p^2$ is obviously collinear with $\hat{\beta}_p$, and, as can be seen from table 2, $\bar{s}_p(\hat{\epsilon}_i)$ likewise increases with $\hat{\beta}_p$. From panels B and C of table 5, the collinearity with $\hat{\beta}_p$ is stronger for $\hat{\beta}_p^2$ than for $\bar{s}_p(\hat{\epsilon}_j)$.

In spite of the loss in precision that arises from multicollinearity, however, the $F$-statistics for $\hat{\gamma}_2$ (the coefficient of $\hat{\beta}_p^2$) and $\hat{\gamma}_3$ [the coefficient of $\bar{s}_p(\hat{e}_j)$] are generally large for the models of panels B and C of table 5, and for the model of panel D which includes both variables. From the $F$-statistics in panel D, it seems that, except for the period 1935-45, the variation through time of $\tilde{\gamma}_{2t}$ is statistically more noticeable than that of $\tilde{\gamma}_{3t}$, but there are periods (1941-45, 1956-60) when the values of $F$ for both $\tilde{\gamma}_{2t}$ and $\tilde{\gamma}_{3t}$ are large.

The $F$-statistics for $\hat{\gamma}_{1t} = \tilde{\gamma}_{1t} + \tilde{\phi}_{1t}$ also indicate that $\tilde{\gamma}_{1t}$ has substantial variation through time. This is not surprising, however, since $\hat{\gamma}_{1t}$ is always directly related to $\tilde{R}_{mt}$. For example, from equation (12), for the one-variable model of panel A, $\hat{\gamma}_{1t} = \tilde{R}_{mt} - \hat{\gamma}_{0t}$.

Finally, the $F$-statistics for $\hat{\gamma}_{0t} = \tilde{\gamma}_{0t} + \tilde{\phi}_{0t}$ are also in general large. And the month-by-month variation in $\tilde{\gamma}_{0t}$ cannot be accounted for by variation in $R_{ft}$. The variance of $R_{ft}$ is so small relative to $s^2(\hat{\gamma}_{0t})$, $s^2(\tilde{\gamma}_{0t})$, and $\overline{s^2(\tilde{\phi}_{0t})}$ that doing the $F$-tests in terms of $\hat{\gamma}_{0t} - R_{ft}$ produces results almost identical with those for $\hat{\gamma}_{0t}$.

Rejection of the hypothesis that $\tilde{\gamma}_{0t} - R_{ft} = 0$ does not imply rejection of the S-L hypothesis—to be tested next—that $E(\tilde{\gamma}_{0t}) = R_{ft}$. Likewise, to find that month-by-month $\tilde{\gamma}_{2t} \neq 0$ and $\tilde{\gamma}_{3t} \neq 0$ does not imply rejection of hypotheses C1 and C2 of the two-parameter model. These hypotheses, which we are unable to reject on the basis of the results in table 3, say that $E(\tilde{\gamma}_{2t}) = 0$ and $E(\tilde{\gamma}_{3t}) = 0$.

What we have found in table 5 is that there are variables in addition to $\hat{\beta}_p$ that systematically affect period-by-period returns. Some of these omitted variables are apparently related to $\hat{\beta}_p^2$ and $\overline{s}_p(\widetilde{e}_i)$. But the latter are almost surely proxies, since there is no economic rationale for their presence in our stochastic risk-return model.

|  | n | $F_{.90}$ | $F_{.95}$ | $F_{.975}$ | $F_{.99}$ | $F_{.995}$ |
| --- | --- | --- | --- | --- | --- | --- |
| 60 (120) | ...... | 1.35 | 1.47 | 1.58 | 1.73 | 1.83 |
| 60 ($\infty$) | ...... | 1.29 | 1.39 | 1.48 | 1.60 | 1.69 |
| 120 (120) | ...... | 1.26 | 1.35 | 1.43 | 1.53 | 1.61 |
| 120 ($\infty$) | ...... | 1.19 | 1.25 | 1.31 | 1.38 | 1.43 |

TABLE 5

COMPONENTS OF THE VARIANCES OF THE $\hat{\gamma}_{jt}$

<table><tr><td colspan="2">PERIOD</td><td> $s^2(\widetilde{\gamma}_0)$ </td><td> $s^2(\widehat{\gamma}_0)$ </td><td> $\overline{s^2(\widetilde{\phi}_0)}$ </td><td>F</td><td> $s^2(\widetilde{\gamma}_1)$ </td><td> $s^2(\widehat{\gamma}_1)$ </td><td> $\overline{s^2(\widetilde{\phi}_1)}$ </td><td>F</td></tr><tr><td colspan="10">Panel A:</td></tr><tr><td>1935-6/68</td><td>...</td><td>.00105</td><td>.00142</td><td>.00037</td><td>3.84</td><td>.00401</td><td>.00436</td><td>.00035</td><td>12.46</td></tr><tr><td>1935-45</td><td>......</td><td>.00182</td><td>.00273</td><td>.00091</td><td>3.00</td><td>.00863</td><td>.00950</td><td>.00087</td><td>10.92</td></tr><tr><td>1946-55</td><td>......</td><td>.00057</td><td>.00066</td><td>.00009</td><td>7.33</td><td>.00163</td><td>.00171</td><td>.00008</td><td>21.38</td></tr><tr><td>1956-6/68</td><td>...</td><td>.00077</td><td>.00090</td><td>.00013</td><td>6.92</td><td>.00181</td><td>.00193</td><td>.00012</td><td>16.08</td></tr><tr><td>1935-40</td><td>......</td><td>.00265</td><td>.00404</td><td>.00139</td><td>2.91</td><td>.01212</td><td>.01347</td><td>.00135</td><td>9.98</td></tr><tr><td>1941-45</td><td>......</td><td>.00086</td><td>.00118</td><td>.00032</td><td>3.69</td><td>.00452</td><td>.00481</td><td>.00029</td><td>16.59</td></tr><tr><td>1946-50</td><td>......</td><td>.00086</td><td>.00094</td><td>.00008</td><td>11.75</td><td>.00216</td><td>.00224</td><td>.00008</td><td>28.00</td></tr><tr><td>1951-55</td><td>......</td><td>.00027</td><td>.00036</td><td>.00009</td><td>4.00</td><td>.00113</td><td>.00121</td><td>.00008</td><td>15.12</td></tr><tr><td>1956-60</td><td>......</td><td>.00032</td><td>.00041</td><td>.00009</td><td>4.56</td><td>.00104</td><td>.00112</td><td>.00008</td><td>21.50</td></tr><tr><td>1961-6/68</td><td>...</td><td>.00100</td><td>.00114</td><td>.00014</td><td>8.14</td><td>.00217</td><td>.00231</td><td>.00014</td><td>16.50</td></tr><tr><td colspan="10">Panel B:</td></tr><tr><td>1935-6/68</td><td>...</td><td>.00092</td><td>.00267</td><td>.00175</td><td>1.52</td><td>.00564</td><td>.01403</td><td>.00839</td><td>1.67</td></tr><tr><td>1935-45</td><td>......</td><td>.00057</td><td>.00377</td><td>.00320</td><td>1.18</td><td>.00372</td><td>.01941</td><td>.01569</td><td>1.24</td></tr><tr><td>1946-55</td><td>......</td><td>.00053</td><td>.00112</td><td>.00059</td><td>1.90</td><td>.00651</td><td>.00897</td><td>.00245</td><td>3.66</td></tr><tr><td>1956-6/68</td><td>...</td><td>.00155</td><td>.00294</td><td>.00139</td><td>2.12</td><td>.00667</td><td>.01338</td><td>.00671</td><td>1.99</td></tr><tr><td>1935-40</td><td>......</td><td>.00018</td><td>.00476</td><td>.00458</td><td>1.04</td><td>.00374</td><td>.02555</td><td>.02181</td><td>1.17</td></tr><tr><td>1941-45</td><td>......</td><td>.00101</td><td>.00254</td><td>.00153</td><td>1.66</td><td>.00389</td><td>.01225</td><td>.00836</td><td>1.46</td></tr><tr><td>1946-50</td><td>......</td><td>.00084</td><td>.00136</td><td>.00052</td><td>2.62</td><td>.00862</td><td>.01071</td><td>.00209</td><td>5.12</td></tr><tr><td>1951-55</td><td>......</td><td>.00024</td><td>.00090</td><td>.00066</td><td>1.36</td><td>.00447</td><td>.00729</td><td>.00282</td><td>2.58</td></tr><tr><td>1956-60</td><td>......</td><td>.00037</td><td>.00087</td><td>.00050</td><td>1.74</td><td>.00289</td><td>.00517</td><td>.00228</td><td>2.27</td></tr><tr><td>1961-6/68</td><td>...</td><td>.00232</td><td>.00431</td><td>.00199</td><td>2.16</td><td>.00928</td><td>.01894</td><td>.00966</td><td>1.96</td></tr><tr><td colspan="10">Panel C:</td></tr><tr><td>1935-6/68</td><td>...</td><td>.00192</td><td>.00266</td><td>.00075</td><td>3.55</td><td>.00285</td><td>.00428</td><td>.00142</td><td>3.01</td></tr><tr><td>1935-45</td><td>......</td><td>.00394</td><td>.00533</td><td>.00139</td><td>3.83</td><td>.00433</td><td>.00717</td><td>.00283</td><td>2.52</td></tr><tr><td>1946-55</td><td>......</td><td>.00083</td><td>.00101</td><td>.00018</td><td>5.61</td><td>.00261</td><td>.00310</td><td>.00050</td><td>6.20</td></tr><tr><td>1956-6/68</td><td>...</td><td>.00100</td><td>.00164</td><td>.00063</td><td>2.60</td><td>.00178</td><td>.00270</td><td>.00092</td><td>2.93</td></tr><tr><td>1935-40</td><td>......</td><td>.00473</td><td>.00669</td><td>.00196</td><td>3.41</td><td>.00732</td><td>.01094</td><td>.00362</td><td>3.02</td></tr><tr><td>1941-45</td><td>......</td><td>.00307</td><td>.00377</td><td>.00070</td><td>5.38</td><td>.00085</td><td>.00274</td><td>.00189</td><td>1.45</td></tr><tr><td>1946-50</td><td>......</td><td>.00103</td><td>.00117</td><td>.00014</td><td>8.36</td><td>.00386</td><td>.00439</td><td>.00053</td><td>8.28</td></tr><tr><td>1951-55</td><td>......</td><td>.00061</td><td>.00083</td><td>.00022</td><td>3.77</td><td>.00140</td><td>.00188</td><td>.00047</td><td>4.00</td></tr><tr><td>1956-60</td><td>......</td><td>.00079</td><td>.00134</td><td>.00055</td><td>2.44</td><td>.00106</td><td>.00204</td><td>.00098</td><td>2.08</td></tr><tr><td>1961-6/68</td><td>...</td><td>.00109</td><td>.00177</td><td>.00068</td><td>2.60</td><td>.00212</td><td>.00300</td><td>.00088</td><td>3.41</td></tr><tr><td colspan="10">Panel D:</td></tr><tr><td>1935-6/68</td><td>...</td><td>.00150</td><td>.00566</td><td>.00406</td><td>1.39</td><td>.00608</td><td>.01521</td><td>.00913</td><td>1.66</td></tr><tr><td>1935-45</td><td>......</td><td>.00233</td><td>.01065</td><td>.00832</td><td>1.28</td><td>.00402</td><td>.02118</td><td>.01716</td><td>1.23</td></tr><tr><td>1946-55</td><td>......</td><td>.00013</td><td>.00176</td><td>.00163</td><td>1.08</td><td>.00647</td><td>.00916</td><td>.00269</td><td>3.41</td></tr><tr><td>1956-6/68</td><td>...</td><td>.00194</td><td>.00420</td><td>.00226</td><td>1.86</td><td>.00763</td><td>.01485</td><td>.00722</td><td>2.06</td></tr><tr><td>1935-40</td><td>......</td><td>.00157</td><td>.01263</td><td>.01106</td><td>1.14</td><td>.00457</td><td>.02910</td><td>.02453</td><td>1.19</td></tr><tr><td>1941-45</td><td>......</td><td>.00340</td><td>.00843</td><td>.00503</td><td>1.68</td><td>.00365</td><td>.01196</td><td>.00832</td><td>1.44</td></tr><tr><td>1946-50</td><td>......</td><td>.00023</td><td>.00220</td><td>.00197</td><td>1.12</td><td>.00858</td><td>.01119</td><td>.00261</td><td>4.29</td></tr><tr><td>1951-55</td><td>......</td><td>.00006</td><td>.00136</td><td>.00130</td><td>1.05</td><td>.00442</td><td>.00719</td><td>.00277</td><td>2.60</td></tr><tr><td>1956-60</td><td>......</td><td>.00092</td><td>.00239</td><td>.00147</td><td>1.62</td><td>.00328</td><td>.00602</td><td>.00274</td><td>2.20</td></tr><tr><td>1961-6/68</td><td>...</td><td>.00260</td><td>.00539</td><td>.00279</td><td>1.93</td><td>.01060</td><td>.02081</td><td>.01021</td><td>2.04</td></tr></table>

## D. Tests of the S-L Hypothesis

In the Sharpe-Lintner two-parameter model of market equilibrium one has, in addition to conditions C1–C3, the hypothesis that  $E(\tilde{\gamma}_{0t}) = R_{ft}$ . The work of Friend and Blume (1970) and Black, Jensen, and Scholes (1972) suggests that the S-L hypothesis is not upheld by the data. At least in the post–World War II period, estimates of  $E(\tilde{\gamma}_{0t})$  seem to be significantly greater than  $R_{ft}$ .

Each of the four models of table 3 can be used to test the S-L hypothe-

TABLE 5 (Continued)

<table><tr><td>PERIOD</td><td> $s^2(\widetilde{\gamma}_2)$ </td><td> $s^2(\widehat{\gamma}_2)$ </td><td> $\overline{s^2(\widetilde{\phi}_2)}$ </td><td>F</td><td> $s^2(\widetilde{\gamma}_3)$ </td><td> $s^2(\widehat{\gamma}_3)$ </td><td> $\overline{s^2(\widetilde{\phi}_3)}$ </td><td>F</td></tr><tr><td colspan="9">Panel A:</td></tr><tr><td>1935-6/68 ...</td><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td></tr><tr><td>1935-45 ....</td><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td></tr><tr><td>1946-55 ....</td><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td></tr><tr><td>1956-6/68 ...</td><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td></tr><tr><td>1935-40 ....</td><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td></tr><tr><td>1941-45 ....</td><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td></tr><tr><td>1946-50 ....</td><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td></tr><tr><td>1951-55 ....</td><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td></tr><tr><td>1956-60 ....</td><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td></tr><tr><td>1961-6/68 ...</td><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td></tr><tr><td colspan="9">Panel B:</td></tr><tr><td>1935-6/68 ...</td><td>.00121</td><td>.00318</td><td>.00197</td><td>1.61</td><td>...</td><td>...</td><td>...</td><td>...</td></tr><tr><td>1935-45 ....</td><td>.00171</td><td>.00548</td><td>.00377</td><td>1.45</td><td>...</td><td>...</td><td>...</td><td>...</td></tr><tr><td>1946-55 ....</td><td>.00063</td><td>.00112</td><td>.00049</td><td>2.29</td><td>...</td><td>...</td><td>...</td><td>...</td></tr><tr><td>1956-6/68 ...</td><td>.00122</td><td>.00278</td><td>.00156</td><td>1.78</td><td>...</td><td>...</td><td>...</td><td>...</td></tr><tr><td>1935-40 ....</td><td>.00041</td><td>.00566</td><td>.00524</td><td>1.08</td><td>...</td><td>...</td><td>...</td><td>...</td></tr><tr><td>1941-45 ....</td><td>.00327</td><td>.00527</td><td>.00201</td><td>2.62</td><td>...</td><td>...</td><td>...</td><td>...</td></tr><tr><td>1946-50 ....</td><td>.00066</td><td>.00103</td><td>.00037</td><td>2.78</td><td>...</td><td>...</td><td>...</td><td>...</td></tr><tr><td>1951-55 ....</td><td>.00058</td><td>.00120</td><td>.00062</td><td>1.94</td><td>...</td><td>...</td><td>...</td><td>...</td></tr><tr><td>1956-60 ....</td><td>.00033</td><td>.00083</td><td>.00050</td><td>1.66</td><td>...</td><td>...</td><td>...</td><td>...</td></tr><tr><td>1961-6/68 ...</td><td>.00182</td><td>.00410</td><td>.00227</td><td>1.81</td><td>...</td><td>...</td><td>...</td><td>...</td></tr><tr><td colspan="9">Panel C:</td></tr><tr><td>1935-6/68 ...</td><td>...</td><td>...</td><td>...</td><td>...</td><td>.341</td><td>.753</td><td>.412</td><td>1.83</td></tr><tr><td>1935-45 ....</td><td>...</td><td>...</td><td>...</td><td>...</td><td>.535</td><td>.847</td><td>.313</td><td>2.71</td></tr><tr><td>1946-55 ....</td><td>...</td><td>...</td><td>...</td><td>...</td><td>.165</td><td>.370</td><td>.206</td><td>1.80</td></tr><tr><td>1956-6/68 ...</td><td>...</td><td>...</td><td>...</td><td>...</td><td>.304</td><td>.968</td><td>.664</td><td>1.46</td></tr><tr><td>1935-40 ....</td><td>...</td><td>...</td><td>...</td><td>...</td><td>.270</td><td>.553</td><td>.282</td><td>1.96</td></tr><tr><td>1941-45 ....</td><td>...</td><td>...</td><td>...</td><td>...</td><td>.840</td><td>1.189</td><td>.349</td><td>3.41</td></tr><tr><td>1946-50 ....</td><td>...</td><td>...</td><td>...</td><td>...</td><td>.118</td><td>.254</td><td>.136</td><td>1.87</td></tr><tr><td>1951-55 ....</td><td>...</td><td>...</td><td>...</td><td>...</td><td>.217</td><td>.493</td><td>.276</td><td>1.79</td></tr><tr><td>1956-60 ....</td><td>...</td><td>...</td><td>...</td><td>...</td><td>.622</td><td>1.355</td><td>.734</td><td>1.85</td></tr><tr><td>1961-6/68 ...</td><td>...</td><td>...</td><td>...</td><td>...</td><td>.105</td><td>.722</td><td>.617</td><td>1.17</td></tr><tr><td colspan="9">Panel D:</td></tr><tr><td>1935-6/68 ...</td><td>.00061</td><td>.00362</td><td>.00301</td><td>1.21</td><td>.276</td><td>.864</td><td>.588</td><td>1.47</td></tr><tr><td>1935-45 ....</td><td>...</td><td>.00624</td><td>.00644</td><td>.97</td><td>.392</td><td>1.001</td><td>.613</td><td>1.63</td></tr><tr><td>1946-55 ....</td><td>.00061</td><td>.00148</td><td>.00087</td><td>1.70</td><td>.028</td><td>.383</td><td>.355</td><td>1.08</td></tr><tr><td>1956-6/68 ...</td><td>.00134</td><td>.00304</td><td>.00169</td><td>1.80</td><td>.374</td><td>1.125</td><td>.751</td><td>1.50</td></tr><tr><td>1935-40 ....</td><td>...</td><td>.00723</td><td>.00886</td><td>.82</td><td>.120</td><td>.682</td><td>.562</td><td>1.21</td></tr><tr><td>1941-45 ....</td><td>.00162</td><td>.00515</td><td>.00353</td><td>1.46</td><td>.720</td><td>1.395</td><td>.675</td><td>2.07</td></tr><tr><td>1946-50 ....</td><td>.00083</td><td>.00180</td><td>.00096</td><td>1.87</td><td>.023</td><td>.348</td><td>.325</td><td>1.07</td></tr><tr><td>1951-55 ....</td><td>.00039</td><td>.00116</td><td>.00077</td><td>1.51</td><td>.038</td><td>.424</td><td>.386</td><td>1.10</td></tr><tr><td>1956-60 ....</td><td>.00037</td><td>.00103</td><td>.00066</td><td>1.56</td><td>.712</td><td>1.654</td><td>.941</td><td>1.76</td></tr><tr><td>1961-6/68 ...</td><td>.00202</td><td>.00440</td><td>.00238</td><td>1.85</td><td>.163</td><td>.787</td><td>.624</td><td>1.26</td></tr></table>

sis.$^{12}$ The most efficient tests, however, are provided by the one-variable

$^{12}$  The least-squares intercepts  $\hat{\gamma}_{0t}$  in the four cross-sectional risk-return regressions can always be interpreted as returns for month t on zero- $\hat{\beta}$  portfolios (n. 10). For the three-variable model of panel D, table 3, the unbiasedness of the least-squares coefficients can be shown to imply that in computing  $\hat{\gamma}_{0t}$ , negative and positive weights are assigned to the 20 portfolios in such a way that the resulting portfolio has not only zero- $\hat{\beta}$  but also zero averages of the  $20\hat{\beta}_{p}^{2}$  and of the  $20\bar{s}_{p}(\hat{e}_{i})$ . Analogous statements apply to the two-variable models of panels B and C.

Black, Jensen, and Scholes test the S-L hypothesis with a time series of monthly returns on a “minimum variance zero- $\hat{\beta}$ portfolio” which they derive directly. It turns model of panel A, since the values of  $s(\hat{\gamma}_{0})$  for this model [which are nearly identical with the values of  $s(\hat{\gamma}_{0}-R_{f})$ ] are substantially smaller than those for other models. Except for the most recent period 1961–6/68, the values of  $\overline{\hat{\gamma}_{0}-R_{f}}$  in panel A are all positive and generally greater than 0.4 percent per month. The value of  $t(\overline{\hat{\gamma}_{0}-R_{f}})$  for the overall period 1935–6/68 is 2.55, and the t-statistics for the subperiods 1946–55, 1951–55, and 1956–60 are likewise large. Thus, the results in panel A, table 3, support the negative conclusions of Friend and Blume (1970) and Black, Jensen, and Scholes (1972) with respect to the S-L hypothesis.

The S-L hypothesis seems to do somewhat better in the two-variable quadratic model of panel B, table 3 and especially in the three-variable model of panel D. The values of $t(\widehat{\gamma}_0 - R_f)$ are substantially closer to zero for these models than for the model of panel A. This is due to values of $\widehat{\gamma}_0 - R_f$ that are closer to zero, but it also reflects the fact that $s(\widehat{\gamma}_0)$ is substantially higher for the models of panels B and D than for the model of panel A.

But the effects of $\hat{\beta}_p^2$ and $\bar{s}_p(\hat{\epsilon}_i)$ on tests of the S-L hypothesis are in fact not at all so clear-cut. Consider the model

$$
\tilde {R} _ {i t} = \tilde {\gamma} _ {0 t} ^ {\prime} + \tilde {\gamma} _ {1 t} ^ {\prime} \beta_ {i} + \tilde {\gamma} _ {2 t} (1 - \beta_ {i}) ^ {2} + \tilde {\gamma} _ {3 t} s _ {i} + \tilde {\eta} _ {i t}.\tag{13}
$$

Equations (7) and (13) are equivalent representations of the stochastic process generating returns, with $\tilde{\gamma}_{1t} = \tilde{\gamma}_{1t}' - 2\tilde{\gamma}_{2t}$ and $\tilde{\gamma}_{0t} = \tilde{\gamma}_{0t}' + \tilde{\gamma}_{2t}$. Moreover, if the steps used to obtain the regression equation (10) from the stochastic model (7) are applied to (13), we get the regression equation,

$$
R _ {p t} = \hat {\gamma} _ {0 t} + \hat {\gamma} _ {1 t} ^ {\prime} \hat {\beta} _ {p} + \hat {\gamma} _ {2 t} (1 - \hat {\beta} _ {p}) ^ {2} + \hat {\gamma} _ {3 t} \bar {s} _ {p} (\hat {\epsilon} _ {i}) + \hat {\eta} _ {p t},\tag{14}
$$

where, just as $\hat{\beta}_p^2$ in (10) is the average of $\hat{\beta}_i^2$ for securities $i$ in portfolio $p$, $(1 - \hat{\beta}_p)^2$ is the average of $(1 - \hat{\beta}_i)^2$. The values of the estimates $\hat{\gamma}_{2t}$ and $\hat{\gamma}_{3t}$ are identical in (10) and (14); in addition, $\hat{\gamma}_{1t} = \hat{\gamma}'_{1t} - 2\hat{\gamma}_{2t}$ and $\hat{\gamma}_{0t} = \hat{\gamma}'_{0t} + \hat{\gamma}_{2t}$. But although the regression equations (10) and (14) are statistically indistinguishable, tests of the hypothesis $E(\hat{\gamma}_{0t}) =$

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">out, however, that this portfolio is constructed under what amounts to the assumptions of the Gauss-Markov Theorem on the underlying disturbances of the one-variable risk-return regression (11). With these assumptions the least-squares estimate  $\hat{\gamma}_{0t}$ , obtained from the cross-sectional risk-return regression of (11) for month t, is precisely the return for month t on the minimum variance zero- $\hat{\beta}$  portfolio that can be constructed from the 20 portfolio  $\hat{\beta}_{p}$ . Thus, the tests of the S-L hypothesis in panel A of table 3 are conceptually the same as those of Black, Jensen, and Scholes.</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$\widehat{\beta}_{p}$</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$\widehat{\gamma}_{0t},$</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$\overline{s}_p(\widehat{\epsilon}_i)$</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$\hat{\beta}_{p}^{2}$</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$\overline{s}_p(\hat{\epsilon}_i)$</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$\hat{\beta}_{p},\hat{\beta}_{p}^{2}$</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">If one makes the assumptions of the Gauss-Markov Theorem on the underlying disturbances of the models of panels B–D of table 3, the regression intercepts for these models can likewise be interpreted as returns on minimum-variance zero-$\widehat{\beta}$ portfolios. These portfolios then differ in terms of whether or not they also constrain the averages of the $20\ \widehat{\beta}_{p}^{2}$ and of the $20\ \overline{s}_{p}(\widehat{\mathbf{e}}_{i})$ to be zero. Given the collinearity of $\widehat{\beta}_{p},\ \widehat{\beta}_{p}^{2}$, and $\overline{s}_{p}(\widehat{\mathbf{e}}_{i})$, however, the assumptions of the Gauss-Markov Theorem cannot apply to all four of the models.</span></small>

$R_{ft}$ from (10) do not yield the same results as tests of the hypothesis $E(\tilde{\gamma}_{0t}^{\prime}) = R_{ft}$ from (14). In panel D of table 3, $\overline{\hat{\gamma}_{0} - R_{f}}$ is never statistically very different from zero, whereas in tests (not shown) from (14), the results are similar to those of panel A, table 3. That is, $\overline{\hat{\gamma}_{0}^{\prime} - R_{f}}$ is systematically positive for all periods but 1961–6/68 and statistically very different from zero for the overall period 1935–6/68 and for the 1946–55, 1951–55, and 1956–60 subperiods.

Thus, tests of the S-L hypothesis from our three-variable models are ambiguous. Perhaps the ambiguity could be resolved and more efficient tests of the hypothesis could be obtained if the omitted variables for which $\overline{s}_p(\hat{\epsilon}_i),\hat{\beta}_p^2$, or $(1 - \hat{\beta}_p)^2$ are almost surely proxies were identified. As indicated above, however, at the moment the most efficient tests of the S-L hypothesis are provided by the one-variable model of panel A, table 3, and the results for that model support the negative conclusions of others.

Given that the S-L hypothesis is not supported by the data, tests of the market efficiency hypothesis that $\tilde{\gamma}_{0t} - E(\tilde{R}_{0t})$ is a fair game are difficult since we no longer have a specific hypothesis about $E(\tilde{R}_{0t})$. And using the mean of the $\hat{\gamma}_{0t}$ as an estimate of $E(\tilde{R}_{0t})$ does not work as well in this case as it does for the market efficiency tests on $\gamma_{1t}$. One should note, however, that although the serial correlations $\rho_M(\hat{\gamma}_0)$ in table 4 are often large relative to estimates of their standard errors, they are small in terms of the proportion of the time series variance of $\hat{\gamma}_{0t}$ that they explain, and the latter is the more important criterion for judging whether market efficiency is a workable representation of reality (see n. 8).

## VI. Conclusions

In sum our results support the important testable implications of the two-parameter model. Given that the market portfolio is efficient—or, more specifically, given that our proxy for the market portfolio is at least approximately efficient—we cannot reject the hypothesis that average returns on New York Stock Exchange common stocks reflect the attempts of risk-averse investors to hold efficient portfolios. Specifically, on average there seems to be a positive tradeoff between return and risk, with risk measured from the portfolio viewpoint. In addition, although there are “stochastic nonlinearities” from period to period, we cannot reject the hypothesis that on average their effects are zero and unpredictably different from zero from one period to the next. Thus, we cannot reject the hypothesis that in making a portfolio decision, an investor should assume that the relationship between a security’s portfolio risk and its expected return is linear, as implied by the two-parameter model. We also cannot reject the hypothesis of the two-parameter model that no measure of risk, in addition to portfolio risk, systematically affects average returns. Finally, the observed fair game properties of the coefficients and residuals of the risk-return regressions are consistent with an efficient capital market—that is, a market where prices of securities fully reflect available information.

## Appendix

## Some Related Issues

## A1. Market Models and Tests of Market Efficiency

The time series of regression coefficients from (10) are, of course, the inputs for the tests of the two-parameter model. But these coefficients can also be useful in tests of capital market efficiency—that is, tests of the speed of price adjustment to different types of new information. Since the work of Fama et al. (1969), such tests have commonly been based on the “one-factor market model”:

$$
R _ {i t} = \hat {a} _ {i} + \hat {\beta} _ {i} R _ {m t} + \epsilon_ {i t}.\tag{15}
$$

In this regression equation, the term involving $R_{mt}$ is assumed to capture the effects of market-wide factors. The effects on returns of events specific to company $i$, like a stock split or a change in earnings, are then studied through the residuals $\hat{\epsilon}_{it}$.

But given that there is period-to-period variation in  $\hat{\gamma}_{0t}$ ,  $\hat{\gamma}_{2t}$ , and  $\hat{\gamma}_{3t}$  in (10) that is above and beyond pure sampling error, then these coefficients can be interpreted as market factors, (in addition to  $R_{mt}$ ) that influence the returns on all securities. To see this, substitute (12) into (11) to obtain the “two-factor market model”:

$$
R _ {p t} = \hat {\gamma} _ {0 t} (1 - \hat {\beta} _ {p}) + \hat {\beta} _ {p} R _ {m t} + \hat {\eta} _ {p t}.\tag{16}
$$

In like fashion, from equation (10) itself we easily obtain the “four-factor market model”:

$$
\begin{array}{c} R _ {p t} = \hat {\gamma} _ {0 t} (1 - \hat {\beta} _ {p}) + \hat {\beta} _ {p} R _ {m t} + \hat {\gamma} _ {2 t} (\hat {\beta} _ {p} ^ {2} - \hat {\beta} _ {p} \bar {\hat {\beta}} ^ {2}) + \hat {\gamma} _ {3 t} \\ \hline [ \bar {s} _ {p} (\hat {\epsilon} _ {i}) - \hat {\beta} _ {p} \bar {\bar {s}} (\hat {\epsilon} _ {i}) ] + \hat {\eta} _ {p t}, \end{array}\tag{17}
$$

where $\overline{\hat{\beta}}^2$ and $\bar{\bar{s}} (\hat{\epsilon}_i)$ are the averages over $p$ of the $\hat{\beta}_p^2$ and the $\bar{s}_p(\hat{\epsilon}_i)$.

Comparing equations (15–17) it is clear that the residuals  $\hat{\epsilon}_{it}$  from the one-factor market model contain variation in the market factors  $\hat{\gamma}_{0t}, \hat{\gamma}_{2t}$ , and  $\hat{\gamma}_{3t}$ . Thus, if one is interested in the effect on a security's return of an event specific to the given company, this effect can probably be studied more precisely from the residuals of the two- or even the four-factor market models of (16) and (17) than from the one-factor model of (15). This has in fact already been done in a study of changes in accounting techniques by Ball (1972), in a study of insider trading by Jaffe (1972), and in a study of mergers by Mandelker (1972).

Ball, Jaffe, and Mandelker use the two-factor rather than the four-factor market model, and there is probably some basis for this. First, one can see from table 5 that because of the collinearity of $\hat{\beta}_p$, $\hat{\beta}_p^2$, and $\bar{s}_p(\hat{\epsilon}_i)$, the coefficient estimates $\hat{\gamma}_{0t}$ and $\hat{\gamma}_{1t}$ have much smaller standard errors in the two-factor model. Second, we have computed residual variances for each of our 20 portfolios for various time periods from the time series of $\hat{\epsilon}_{pt}$ and $\hat{\eta}_{pt}$ from (15), (16), and (17). The decline in residual variance that is obtained in going from (15) to (16) is as predicted: That is, the decline is noticeable over more or less the entire range of $\hat{\beta}_p$ and it is proportional to $(1 - \hat{\beta}_p)^2$. On the other hand, in going from the two- to the four-factor model, reductions in residual variance are generally noticeable only in the portfolios with the lowest and highest $\hat{\beta}_p$, and the reductions for these two portfolios are generally small. Moreover, including $\bar{s}_p(\hat{\epsilon}_i)$ as an explanatory variable in addition to $\hat{\beta}_p$ and $\hat{\beta}_p^2$ never results in a noticeable reduction in residual variances.

## A2. Multifactor Models and Errors in the $\hat{\beta}$

If the return-generating process is a multifactor market model, then the usual estimates of $\beta_{i}$ from the one-factor model of (15) are not most efficient. For example, if the return-generating process is the population analog of (16), more efficient estimates of $\beta_{i}$ could in principle be obtained from a constrained regression applied to

$$
\tilde {R} _ {i t} - \tilde {\gamma} _ {0 t} = \beta_ {i} (\tilde {R} _ {m t} - \tilde {\gamma} _ {0 t}) + \tilde {\eta} _ {i t}.
$$

But this approach requires the time series of the true $\widetilde{\gamma}_{0t}$. All we have are estimates $\widehat{\gamma}_{0t}$, themselves obtained from estimates of $\widehat{\beta}_p$ from the one-factor model of (15).

It can also be shown that with a multifactor return-generating process the errors in the $\hat{\beta}$ computed from the one-factor market model of (8) and (15) are correlated across securities and portfolios. This results from the fact that if the true process is a multifactor model, the disturbances of the one-factor model are correlated across securities and portfolios. Moreover, the interdependence of the errors in the $\hat{\beta}$ is higher the farther the true $\beta$'s are from 1.0. This was already noted in the discussion of table 2 where we found that the relative reduction in the standard errors of the $\hat{\beta}$'s obtained by using portfolios rather than individual securities is lower the farther $\hat{\beta}_p$ is from 1.0.

Interdependence of the errors in the $\widehat{\beta}_p$ also complicates the formal analysis of the effects of errors-in-the-variables on properties of the estimated coefficients (the $\widehat{\gamma}_{jt}$) in the risk-return regressions of (10). This topic is considered in detail in an appendix to an earlier version of this paper that can be made available to the reader on request.

## References

Ball, R. “Changes in Accounting Techniques and Stock Prices.” Ph.D. dissertation, University of Chicago, 1972.

Black, F. “Capital Market Equilibrium with Restricted Borrowing.” J. Bus. 45 (July 1972): 444–55.

Black, F.; Jensen, M.; Scholes, M. “The Capital Asset Pricing Model: Some Empirical Results.” In Studies in the Theory of Capital Markets, edited by Michael Jensen. New York: Praeger, 1972.

Blume, M. E. “Portfolio Theory: A Step toward Its Practical Application.” J. Bus. 43 (April 1970): 152–73.

Douglas, G. W. “Risk in the Equity Markets: An Empirical Appraisal of Market Efficiency.” Yale Econ. Essays 9 (Spring 1969): 3–45.

Fama, E. F. “The Behavior of Stock Market Prices.” J. Bus. 38 (January 1965): 34–105. (a)

——. “Portfolio Analysis in a Stable Paretian Market.” Management Sci. 11 (January 1965): 404–19. (b)

——. “Multiperiod Consumption-Investment Decisions.” A.E.R. 60 (March 1970): 163–74. (a)

——. “Efficient Capital Markets: A Review of Theory and Empirical Work.” J. Finance 25 (May 1970): 383–417. (b)

——. “Risk, Return and Equilibrium.” J.P.E. 79 (January/February 1971): 30–55.

Fama, E. F., and Babiak, H. “Dividend Policy: An Empirical Analysis.” J. American Statis. Assoc. 48 (December 1968): 1132–61.

Fama, E. F.; Fisher, L.; Jensen, M.; Roll, R. “The Adjustment of Stock Prices to New Information.” Internat. Econ. Rev. 10 (February 1969): 1–21.

Fama, E. F., and Miller, M. The Theory of Finance. New York: Holt, Rinehart & Winston, 1972.

Fama, E. F., and Roll, R. “Some Properties of Symmetric Stable Distributions.” J. American Statis. Assoc. 48 (September 1968): 817–36.

Fisher, L. “Some New Stock Market Indexes.” J. Bus. 39 (January 1966): 191–225.

Friend, I., and Blume, M. “Measurement of Portfolio Performance under Uncertainty.” A.E.R. 60 (September 1970): 561–75.

Gonedes, N. J. “Evidence on the Information Content of Accounting Numbers: Accounting-based and Market-based Estimates of Systematic Risk.” J. Financial and Quantitative Analysis (1973): in press.

Jaffe, J. “Security Regulation, Special Information, and Insider Trading.” Ph.D. dissertation, University of Chicago, 1972.

Jensen, M. “The Foundations and Current State of Capital Market Theory.” Bell J. Econ. and Management Sci. 3 (Autumn 1972): 357–98.

Lintner, J. “The Valuation of Risk Assets and the Selection of Risky Investments in Stock Portfolios and Capital Budgets.” Rev. Econ. and Statis. 47 (February 1965): 13–37.

Mandelker, G. “Returns to Stockholders from Mergers.” Ph.D. proposal, University of Chicago, 1972.

Markowitz, H. Portfolio Selection: Efficient Diversification of Investments. New York: Wiley, 1959.

Miller, K. D. “Futures Trading and Investor Returns: An Investigation of Commodity Market Risk Premiums.” Ph.D. dissertation, University of Chicago, 1971.

Miller, M., and Scholes, M. “Rates of Return in Relation to Risk: A Re-Examination of Some Recent Findings.” In Studies in the Theory of Capital Markets, edited by Michael Jensen. New York: Praeger, 1972.

Mood, A. M., and Graybill, F. A. Introduction to the Theory of Statistics. New York: McGraw-Hill, 1963.

Officer, R. R. “A Time Series Examination of the Market Factor of the New York Stock Exchange.” Ph.D. dissertation, University of Chicago, 1971.

Roll, R. The Behavior of Interest Rates. New York: Basic, 1970.

Sharpe, W. F. “Capital Asset Prices: A Theory of Market Equilibrium under Conditions of Risk.” J. Finance 19 (September 1964): 425–42.

Tobin, J. “Liquidity Preference as Behavior towards Risk.” Rev. Econ. Studies 25 (February 1958): 65–86.