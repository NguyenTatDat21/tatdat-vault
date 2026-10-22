# Bootstrap Robust Prescriptive Analytics

Dimitris Bertsimas<sup>∗1</sup> and Bart Van Parys<sup>†1</sup>

<sup>1</sup>Operations Research Center, Massachusetts Institute of Technology

June 9, 2021

## Abstract

We address the problem of prescribing an optimal decision in a framework where the cost function depends on uncertain problem parameters that need to be learned from data. Earlier work proposed prescriptive formulations based on supervised machine learning methods. These prescriptive methods can factor in contextual information on a potentially large number of covariates to take context specific actions which are superior to any static decision. When working with noisy or corrupt data, however, such nominal prescriptive methods can be prone to adverse overfitting phenomena and fail to generalize on out-of-sample data. In this paper we combine ideas from robust optimization and the statistical bootstrap to propose novel prescriptive methods which safeguard against overfitting. We show indeed that a particular entropic robust counterpart to such nominal formulations guarantees good performance on synthetic bootstrap data. As bootstrap data is often a sensible proxy to actual out-of-sample data, our robust counterpart can be interpreted to directly encourage good out-of-sample performance. The associated robust prescriptive methods furthermore reduce to convenient tractable convex optimization problems in the context of local learning methods such as nearest neighbors and Nadaraya-Watson learning. We illustrate our data-driven decision-making framework and our novel robustness notion on a small newsvendor problem.

Keywords: Data Analytics, Distributionally Robust Optimization, Statistical Bootstrap, Nadaraya-Watson Learning, Nearest Neighbors Learning

## 1 Introduction

Most practical decisions need to be made despite the fact that their cost may be uncertain. Indeed, often the cost $L ( z , y )$ of any potential decision z depends on an unknown stochastic parameter y. Stocking goods under uncertain customer demand or devising profitable investment strategies when facing volatile returns are two practical examples. Stochastic optimization aims to minimize expected cost, i.e.,

$$
z ^ {\star} \in \arg \min _ {\bar {z}} \mathbb {E} _ {Y ^ {\star}} [ L (z, y) ]\tag{1}
$$

where the random variable y is distributed as $Y ^ { \star }$ . We assume here implicitly that the minimization is carried out only over those decisions z for which the cost function is well defined, i.e., dom $( \mathbb { E } _ { Y ^ { \star } } [ L ( z , y ) ] )$ . To avoid technicalities we make the standard assumption that the decision $z \in \mathrm { R } ^ { \dim ( z ) }$ and the random variable $y \in \mathrm { R } ^ { \dim ( y ) }$ take values in finite dimensional vector spaces.

Such stochastic optimization formulation makes sense when nothing beyond the distribution of the stochastic variable y is known before a decision is to be made. Often however, additional information concerning a large number of covariates x can be obtained before we need to make our decision. After observing a particular context $x   =   x _ { 0 }$ , the decision should take this additional information into account and the problem in need of attention should not be the classical stochastic optimization problem (1) but rather

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">∗[dbertsim@mit.edu](mailto:dbertsim@mit.edu)</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">†[vanparys@mit.edu](mailto:vanparys@mit.edu)</span></small>

$$
z ^ {\star} (x _ {0}) \in \arg \min _ {z} \mathbb {E} _ {D ^ {\star}} [ L (z, y) | x = x _ {0} ]\tag{2}
$$

where we assume that $x _ { 0 } \in \mathrm { R } ^ { \dim ( x ) }$ consists of all relevant contextual information. We assume that the context x is a random variable with unknown distribution $X ^ { \star }$ whereas $x _ { 0 }$ is one particular observed context. The distribution $D ^ { \star }$ represents here the joint distribution of both the parameter y as well as the covariates x whereas $\mathbb { E } _ { D ^ { \star } } [ L ( z , y ) | x = x _ { 0 } ]$ denotes the expected cost of decision z conditioned on the event $x = x _ { 0 }$ . Denote with $\mathcal { D }$ the set of all distributions supported on the set $\Omega \subseteq \operatorname { R } ^ { \dim ( x ) \times \dim ( y ) }$ of all possible parameter and covariate realizations, then clearly $D ^ { \star } \in \mathcal { D }$ The optimal contextual decision $z ^ { \star } ( x _ { 0 } )$ has minimal cost as measured by the expected value of its loss $L ( z ^ { \star } ( x _ { 0 } ) , y )$ conditioned<sup>1</sup> on all observed contextual information. Unfortunately, distributions are never observed directly but rather must be learned from historical observations.

Only historical data concerning both uncertain parameters and contexts is typically available in practice. Data instead of distributions should hence be the primitive when making decisions under uncertainty. To that end we consider the training data set

$$
\mathrm{tr} := [ \bar {d} _ {1} = (\bar {x} _ {1}, \bar {y} _ {1}), \bar {d} _ {2} = (\bar {x} _ {2}, \bar {y} _ {2}), \dots ].\tag{3}
$$

We use the symbol $4 6 - 9 9$ throughout this paper to emphasize that the training data is here deterministic rather than random. Data consisting of observations of the parameter $y$ as well as the context x is often denoted as supervised training data. Typically only a limited number of historical observations can be used as training data. We will denote with $\operatorname { t r } [ n ] = [ \bar { d } _ { 1 } = ( \bar { x } _ { 1 } , \bar { y } _ { 1 } ) , \ldots , \bar { d } _ { n } = ( \bar { x } _ { n } , \bar { y } _ { n } ) ]$ the training data set consisting of the first n observations in Equation (3). We will assume that the data comes without any time dependence, or if it does, time is explicitly included as an additional covariate. Consequently, most appropriate learning methods will be insensitive to the order of the data points. Hence, the information contained in the data set can be represented compactly through its empirical distribution

$$
D _ {\mathrm{tr} [ n ]} := \frac {1}{n} \sum_ {(\bar {x}, \bar {y}) \in \mathrm{tr} [ n ]} \delta_ {(\bar {x}, \bar {y})}.
$$

To allow for a statistical analysis of data-driven formulations it is convenient to assume that the training data is obtained as independent samples from the unknown distribution $D ^ { \star }$ , i.e., it is generated by

$$
\text {data} := \left[ d _ {1} = \left(x _ {1}, y _ {1}\right) \sim_ {\mathrm{iid}} D ^ {\star}, d _ {2} = \left(x _ {2}, y _ {2}\right) \sim_ {\mathrm{iid}} D ^ {\star}, \dots \right] \sim D ^ {\star \infty}.\tag{4}
$$

Here, we make a distinction between $D ^ { \star \infty }$ as the data generating process and $D ^ { \star }$ the unknown joint distribution between the parameters $y$ and covariates x. The training set is hence supported on the empirical support set $\Omega _ { n }$ which is a subset of Ω. When we denote with $\mathcal { D } _ { n }$ the set of all distributions supported on the set $\Omega _ { n } ,$ then clearly $D _ { \operatorname { t r } [ n ] } \in \mathcal { D } _ { n } \subseteq \mathcal { D }$

## 1.1 Data-Driven Formulations

In this section we briefly position our approach among several distinct alternatives to decision-making with data. Making decisions based on data has received considerable attention in the literature. We restrict attention to three distinct data-driven approaches which result in computationally attractive formulations.

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">D?[ (z, y)|x]</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">(2)</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280"><sup>1</sup>Technically, the conditional expectation E L is a random variable and uniquely defined only up to events of measure zero. That is, the inclusion in can hold merely almost surely; see for instance the standard text by Billingsley (2008). Slightly abusing notation all statements in this paper involving the observation x<sub>0</sub> should be interpreted to hold hence as X -almost surely where X ? e X\* is the distribution of the covariates x.</span></small>

Empirical-Risk-Minimization: The prescription problem $( 2 )$ can alternatively be defined through the risk minimization formulation $z ^ { \star } ( \cdot ) \in$ arg $\begin{array} { r } { \operatorname* { m i n } _ { z \in \mathcal { F } } \; \mathbb { E } _ { D ^ { \star } } [ L ( z ( x ) , y ) ] } \end{array}$ over the set of all functions $\mathcal { F }$ mapping covariates to decisions. One could hence consider

$$
z _ {\mathrm{tr} [ n ]} (\cdot) \in \arg \min _ {z (\cdot) \in \mathcal {C}} \frac {1}{n} \sum_ {(\bar {x}, \bar {y}) \in \mathrm{tr} [ n ]} L (z (\bar {x}), \bar {y})\tag{5}
$$

where $\mathcal { C }$ is a set of functions with suitable properties. Here $\mathcal { C }$ must be a strict subset of the set of all functions $\mathcal { F }$ as to avoid overfitting and encourage generalization. Ban and Rudin (2019) consider the class $\mathcal { C } = \mathcal { F } _ { \mathrm { l i n } }$ consisting of all linear functions. The empirical risk minimization problem (5) then reduces to a convex problem in the coefficients describing the linear functions in $\mathcal { F } _ { \mathrm { l i n } }$ . Ban and Rudin (2019) also establish out-of-sample guarantees in the particular context of a newsvendor problem. Bertsimas and Kallus (2020) prove similar out-of-sample guarantees for the more general prescription problems considered here and show in particular that for any $\delta > 0$ the probability of drawing random data according to Equation (4) and observing

$$
\mathbb {E} _ {D ^ {\star}} [ L (z (x), y) ] \leq \frac {1}{n} \sum_ {(\bar {x}, \bar {y}) \in \mathrm{data} [ n ]} L (z (\bar {x}), \bar {y}) + \bar {L} \sqrt {\log (1 / \delta) / 2 n} + \bar {G} R _ {n} (\mathcal {C})\tag{6}
$$

is at least $1   -   \delta$ for all functions $z ( \cdot ) \in \mathcal { C }$ . The previous inequality bounds, if $z ^ { \star } ( \cdot ) \in \mathcal { C } ,$ the difference between the empirical average cost and the actual expected cost of not only the optimal prescription but in fact all feasible functions in ${ \mathcal { C } } .$ The constants $\bar { L }$ and $\bar { G }$ are taken to satisfy sup $\flat _ { z ,   y }   L ( z , y ) \leq \bar { L }$ and $\begin{array} { r } { \operatorname* { s u p } _ { z \neq z ^ { \prime } ,   y } { ( L ( z , y ) - L ( z ^ { \prime } , y ) ) } / { \left\| z - z ^ { \prime } \right\| _ { \infty } } \leq } \end{array}$ $\bar { G } ,$ respectively. The Rademacher complexity is a measure of the size of the class of considered prescriptive functions C and is defined as

$$
R _ {n} (\mathcal {C}) := \mathbb {E} \Big [ \frac {2}{n} \sup _ {z (\cdot) \in \mathcal {C}} \sum_ {d \in \mathrm{data} [ n ]} \sum_ {k = 1} ^ {\dim (x)} \sigma_ {d, k} z _ {k} (\bar {x}) \Big ]
$$

where $\sigma _ { \bar { d } , k }$ are independent and equiprobably $\{ + 1 , - 1 \}$ and the data is generated as in Equation (4). Bertsimas and Kallus (2020) show furthermore that $R _ { n } ( \mathcal { F } _ { \operatorname* { l i n } } ) \leq \mathcal { O } ( 1 / \sqrt { n } )$ and hence, as expected, when more data is observed stronger out-of-sample guarantees can be established.

By explicitly constraining the considered prescriptors to be elements of ${ \mathcal { C } } ,$ however, bias is introduced when $z ^ { \star } ( \cdot ) \not \in$ ${ \mathcal { C } } .$ There is indeed no reason in general to expect that $z ^ { \star } ( \cdot )$ should possess for instance a linear parametric structure. As pointed out by Bertsimas and Kallus (2020) constraints on the decision may give rise to nonlinearities which are particularly challenging to deal with. Ban and Rudin (2019) do consider nonlinear prescriptions $z _ { \mathrm { t r } [ n ] } ( \cdot )$ implicitly via the introduction of auxiliary nonlinear transformed covariates. In this paper we will however focus on formulations of an entirely different nature instead.

Estimate-First-Optimize-Later: An alternative to the one-shot approach taken by empirical risk minimization formulations is to separate the problem of prescription with covariate information into an estimation and a subsequent optimization step as visualized in Figure 1. In the estimation step an estimator<sup>2</sup> $z \mapsto \mathrm { E } _ { D _ { \mathrm { t r } [ n ] } } ^ { n } [ L ( z , y ) | x = x _ { 0 } ]$ is considered which based on the provided training data estimates the cost of any decision in the context of interest. Such estimators can be obtained using a variety of machine learning methods. Hannah, Powell, and Blei (2010) consider the classical kernel smoothing method proposed independently by Nadaraya (1964) and Watson (1964). Bertsimas and Kallus (2020) consider additional formulations based on nearest neighbors learning discussed in Altman (1992), and regression trees and random forest learning proposed by Breiman (2001). We also want to mention that Elmachtoub and Grigas (2021) refer to this two-step approach as “predict, then optimize” and discuss several of its limitations and suggest improvements.

Estimate-first-optimize-later formulations subsequently prescribe the action

$$
z _ {\mathrm{tr} [ n ]} (x _ {0}) \in \arg \min _ {z} \mathrm{E} _ {D _ {\mathrm{tr} [ n ]}} ^ {n} [ L (z, y) | x = x _ {0} ].\tag{7}
$$

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">n → ∞</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">“E”</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">ED L , y 0 .</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">“ ”</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280"><sup>2</sup>Our notation here alludes to the fact that this estimator function mapping data to cost estimates is often asymptotically with an unbiased estimate of the actual unknown expected cost z 7→ ?[ (z )|x = x ] In our paper the symbol E will be associated with an estimator (a procedure mapping data to cost estimates) while denotes an expectation operator which may define for instance the actual but unknown expected cost.</span></small>

| Data$D_{\text{tr}[n]}$ | Estimator | Cost$\mathrm{E}_{D_{\text{tr}[n]}}^{n}[L(z,y)\|x = x_{0}]$ | Optimizer | Decision$z_{\text{tr}[n]}(x_{0})$ |
| --- | --- | --- | --- | --- |

Figure 1: Estimate-first-optimize-later formulations construct first a cost estimator $z \mapsto \mathrm { E } _ { D _ { \mathrm { t r } [ n } ] } ^ { n } [ L ( z , y ) | x = x _ { 0 } ]$ and subsequently optimize for a decision promising minimum (estimated) cost as in Equation (7).

We will consider in this paper estimate-first-optimize-later formulations based on local learning methods such as Nadaraya-Watson and nearest neighbors learning. In Section 2 we in fact indicate that both can be generalized using the variable metric estimator discussed by Sain (2002). Bertsimas and Kallus (2020) prove that both the Nadaraya-Watson and nearest neighbors formulations are asymptotically consistent under mild assumptions on the training data and loss function. This in stark contrast to empirical risk minimization formulations which are biased whenever $z ^ { \star } ( \cdot ) \not \in \mathcal { C } .$ Empirical risk minimization formulations on the other hand provide through the complexity of the set C an explicit way to remedy adverse overfitting effects. Estimate-first-optimize-later formulations, although often empirically observed to perform well out-of-sample by Ban and Rudin (2019) and Bertsimas and Kallus (2020), come without such an immediate remedy when they do overfit. It is indeed well known that unbiased estimators based on Nadaraya-Watson and nearest neighbors learning typically suffer a large variance in particular when the covariate dimension is large; see Friedman, Hastie, and Tibshirani (2001)[Section 2.5]. Subsequent minimization of the unbiased estimator $z \mapsto \mathrm { E } _ { D _ { \mathrm { t r } [ n ] } } ^ { n } [ L ( z , y ) | x = x _ { 0 } ]$ only amplifies this issue and can results in overly optimistic prescriptors as pointed out by Michaud (1989) and Ban and Rudin (2019). The performance of estimate-first-optimize-later formulations on out-of-sample data can in such settings be very poor.

Robust-Budget-Minimization: It is clear that when given only a limited amount of training data, data-driven formulations must be guarded against overfitting to one specific training data set. Overfitting can be discouraged by minimizing a regularized objective function

$$
z _ {\mathrm{tr} [ n ]} (x _ {0}) \in \arg \min _ {z} \left\{c _ {n} (z, D _ {\mathrm{tr} [ n ]}, x _ {0}) = \mathrm{E} _ {D _ {\mathrm{tr} [ n ]}} ^ {n} [ L (z, y) | x = x _ {0} ] + J _ {\mathrm{tr} [ n ]} (z, x _ {0}) \right\}\tag{8}
$$

consisting of both an asymptotically unbiased cost estimate and an additional non-negative regularization term. The regularization term makes the budgeted cost of any decision conservative but hopefully ensures decisions whose actual costs do not break the estimated budget. We will denote in this paper events in which the estimated budget of the suggested action does not cover its actual cost as disappointing. One way of regularizing is by considering a robust counterpart formulation

$$
z _ {\mathrm{tr} [ n ]} (x _ {0}) \in \arg \min _ {z} \left\{c _ {n} (z, D _ {\mathrm{tr} [ n ]}, x _ {0}) = \sup _ {D \in \mathcal {A} (D _ {\mathrm{tr} [ n ]})} \mathrm{E} _ {D} ^ {n} [ L (z, y) | x = x _ {0} ] \right\}\tag{9}
$$

where the ambiguity set $\mathcal { A } ( D _ { \mathrm { t r } [ n ] } )$ typically consists of all distributions consistent with the observed training data instead of merely the empirical distribution $D _ { \mathrm { t r } [ n ] }$ . As the robust counterpart is with respect to a set of distributions, formulation (9) takes a so-called distributionally robust perspective.

Distributionally robust optimization has attracted significant attention in the context of classical stochastic optimization without contextual information as it can present a disciplined safeguard mechanism against overfitting. By using a robust counterpart with respect to an ambiguity set of distributions around an estimated nominal one, they were shown by Van Parys, Esfahani, and Kuhn (2017) to be minimally biased while still enjoying statistical out-of-sample guarantees. Many interesting choices of the ambiguity set furthermore result in a tractable overall decision-making approach. The ambiguity set can be defined, for example, through confidence intervals for the distribution’s moments as done by Delage and Ye (2010), Popescu (2005), Van Parys, Goulart, and Kuhn (2016), Wiesemann, Kuhn, and Sim (2014), and $\mathrm { Z y }$ mler, Kuhn, and Rustem (2013). Alternatively, Wang, Glynn, and Ye (2016) use an ambiguity set that contains all distributions that achieve a prescribed level of likelihood, while Bertsimas, Gupta, and Kallus (2017) based theirs on distributions which pass a statistical hypothesis test. Distance-based ambiguity sets which contain all distributions sufficiently close to a reference with respect to probability metrics (Ben-Tal et al., 2013) such as the Prokhorov metric (Erdoğan and Iyengar, 2006), the Wasserstein distance (Mohajerin Esfahani and Kuhn, 2018; Pflug and Wozabal, 2007), or the total variation distance (Sun and Xu, 2016) have received a lot of attention in the recent literature. Surprisingly, the merits of distributional robustness in the context of prescription problems with contextual information has not been studied in depth. One major contribution of this paper is to show that the distributional robust perspective applies just as well to prescription problems with contextual information. Furthermore, we show in Section 4 that for a judiciously chosen ambiguity set $\mathcal { A } ( D _ { \mathrm { t r } [ n ] } )$ the resulting robust formulations enjoy interpretable performance guarantees in the context of bootstrapped “out-of-sample” data.

## 1.2 Motivating Example

Before we formally introduce our novel robustness notion based on bootstrap aggregation, we motivate its main idea with the help of an intuitive example which we will explore further in Section 5.1. We single out the newsvendor problem, which is a common model in economics and operations management, for its simplicity. Consider a newspaper vendor who must decide how many copies z to stock each day in the face of uncertain customer demand y well knowing that any unsold copies will be worthless at the end of each day. Ideally, the newsvendor would like to order exactly $z = y$ newspaper as they are a perishable good. Unfortunately, a decision on the order quantity needs to be made before the demand is observed. Fortunately, however, the newsvendor can observe before making the order several covariates $x = x _ { 0 }$ which may correlate with the uncertain demand. A sensible goal is to order a quantity that minimizes the total expected cost according to

$$
z ^ {\star} (x _ {0}) \in \arg \inf _ {z} \quad \mathbb {E} _ {D ^ {\star}} \big [ b \cdot (y - z) ^ {+} + h \cdot (z - y) ^ {+} | x = x _ {0} \big ]\tag{10}
$$

where $D ^ { \star }$ is the joint distribution between costumer demand and observed covariates. The constants $b   \in   \mathrm { R } _ { + }$ and $h \in \mathrm { R } _ { + }$ represent here the marginal opportunity cost of ordering too few newspapers and the loss in revenue associated with ordering surplus newspapers. If the distribution $D ^ { \star }$ is known, then a classical result states that the optimal decision is given by the conditional quantile

$$
z ^ {\star} (x _ {0}) := \inf \left\{z \in \mathrm{R}: \mathbb {E} _ {D ^ {\star}} \big [ \mathbb {1} \{y \leq z \} \big | x = x _ {0} \big ] \geq b / (b + h) \right\}\tag{11}
$$

of the demand distribution in the covariate context of interest.

The classical newsvendor formulation assumes the joint distribution $D ^ { \star }$ between demand and covariates to be known. In practice however distributions are never observed directly but rather must be estimated from a finite amount of training data. Let us for the sake of exposition single out one particular formulation based on nearest neighbors learning. That is, we consider

$$
z _ {\mathrm{tr} [ n ]} (x _ {0}) := \arg \min _ {z} \left\{c _ {n} (z, D _ {\mathrm{tr} [ n ]}, x _ {0}) = \frac {1}{k} \sum_ {(\bar {x}, \bar {y}) \in N _ {n} ^ {k} (x _ {0})} b \cdot (\bar {y} - z) ^ {+} + h \cdot (z - \bar {y}) ^ {+} \right\}\tag{12}
$$

where $N _ { n } ^ { k } ( x _ { 0 } )$ denotes here the k nearest neighbors to the covariate of interest in the provided training data set. Hence, our decision minimizes the budgeted cost as estimated by a classical nearest neighbors learning method. In Figure 2 we visualize this cost estimate as a function of the context of interest to illustrate the nature of the nearest neighbors estimator.

Remark that our data-driven decision $z _ { \mathrm { t r } [ n ] } ( x _ { 0 } )$ only minimizes the predicted cost in the context of interest rather than the unknown out-of-sample actual cost. This implies that once the unknown cost realizes it may exceed the predicted cost budgeted by the newsvendor. Clearly, such disappointment events are very undesirable and may result in financial difficulties for the newsvendor who must now find additional funds to cover the difference. A standard practice in machine learning to quantify the probability of disappointment events is to consider the performance of our decision on validation data. Suppose indeed we could obtain access to independent validation data sets $\operatorname { v d } [ n ] \in V$ each containing the same number of data points as the training data set. A practical measure for disappointment would be the fraction

$$
\frac {1}{| V |} \sum_ {\mathrm{vd} [ n ] \in V} \mathbb {1} \{\mathrm{E} _ {D _ {\mathrm{vd} [ n ]}} ^ {n} \big [ L (z _ {\mathrm{tr} [ n ]} (x _ {0}), y) | x = x _ {0} \big ] \geq c _ {n} (z _ {\mathrm{tr} [ n ]} (x _ {0}), D _ {\mathrm{tr} [ n ]}, x _ {0}) \}\tag{13}
$$

of all validation sets based on which an independent cost estimate for our decision $z _ { \mathrm { t r } [ n ] } ( x _ { 0 } )$ breaks our estimated original budget. Notice that the previous metric critically relies on our ability to obtain large quantities of validation data which in practice may be impossible or very expensive to obtain. We want a measure of disappointment for our cost estimate without access to such independent validation data.

We could try to make up for not having access to independent validation data by considering a resample method instead. Bootstrapping according to Efron (1982) is the process of resampling with replacement a proxy validation data set from the original training data. This resampling procedure is described formally as the stochastic process

$$
\mathrm{bs} := [ (x _ {1, r}, y _ {1, r}) \sim_ {\mathrm{iid}} D _ {\mathrm{tr} [ n ]}, M _ {2, r} = (x _ {2, r}, y _ {2, r}) \sim_ {\mathrm{iid}} D _ {\mathrm{tr} [ n ]}, \dots ] \sim D _ {\mathrm{tr} [ n ]} ^ {\infty}\tag{14}
$$

of resampling independent data points from the empirical distribution of the training data. Again we make a distinction between the bootstrap data generation process $D _ { \mathrm { t r } [ n ] } ^ { \infty }$ and the empirical distribution $D _ { \mathrm { t r } [ n ] }$ of the training data. The bootstrap method hence generates its own synthetic validation data sets directly from the training data. Bootstrap data sets so obtained are merely proxies to actual validation data which ought to be drawn from the stochastic process stated in (4) which generated the training data. In the context of budget minimization formulations, we can sample bootstrap data sets $\mathrm { b s } [ n ] \in B$ and use the fraction

$$
\frac {1}{| B |} \sum_ {\mathrm{bs} [ n ] \in B} \mathbb {1} \{\mathrm{E} _ {D _ {\mathrm{bs} [ n ]}} ^ {n} \big [ L (z _ {\mathrm{tr} [ n ]} (x _ {0}), y) | x = x _ {0} \big ] \geq c _ {n} (z _ {\mathrm{tr} [ n ]} (x _ {0}), D _ {\mathrm{tr} [ n ]}, x _ {0}) \}\tag{15}
$$

as a proxy to the out-of-sample disappointment (13) on actual validation data. As bootstrapping does not require access to any validation data it is a practically viable approach to quantify the out-of-sample performance of budget minimization formulations; see also Figure 2.

## 1.3 Bootstrap Aggregation

In what follows we will in fact consider the limiting bootstrap out-of-sample disappointment in which the number of bootstrap resamples $| B |$ tends to infinity and can formally be defined as

$$
D _ {\mathrm{tr} [ n ]} ^ {\infty} [ \mathrm{E} _ {D _ {\mathrm{bs} [ n ]}} ^ {n} \big [ L (z _ {\mathrm{tr} [ n ]} (x _ {0}), y) | x = x _ {0} \big ] \geq c _ {n} (z _ {\mathrm{tr} [ n ]} (x _ {0}), D _ {\mathrm{tr} [ n ]}, x _ {0}) \big \} ]\tag{16}
$$

as our metric of out-of-sample performance. That is, the bootstrap disappointment probability is the probability that the random predicted cost of our decision as measured by a particular estimator on bootstrap data breaks the original budget for our decision $z _ { \mathrm { t r } [ n ] }$ . We will present in this paper budget minimization formulations for which the bootstrap disappointment can be controlled explicitly. To do so we introduce our notion of the bootstrap robust counterpart of an estimate-first-predict-later formulation.

Definition 1 (Bootstrap Robust Counterpart). The budget function $c _ { n }$ and its associated prescriptor $z _ { \mathrm { t r } [ n ] } ( x _ { 0 } ) \in$ arg minz $c _ { n } ( z , D _ { \operatorname { t r } } , x _ { 0 } )$ are said to be the bootstrap robust counterpart with disappointment $b \in [ 0 , 1 )$ of an estimatefirst-optimize-later formulation with estimator $\begin{array} { r } { \mathrm { E } _ { D _ { \mathrm { t r } [ n ] } } ^ { n } \big [ L ( z _ { \mathrm { t r } [ n ] } ( x _ { 0 } ) , y ) | x = x _ { 0 } \big ] } \end{array}$ if we have

$$
D _ {\mathrm{tr} [ n ]} ^ {\infty} \left[ \mathrm{E} _ {D _ {\mathrm{bs} [ n ]}} ^ {n} \bigl [ L (z _ {\mathrm{tr} [ n ]} (x _ {0}), y) | x = x _ {0} \bigr ] > c _ {n} (z _ {\mathrm{tr} [ n ]} (x _ {0}), D _ {\mathrm{tr} [ n ]}, x _ {0}) \right] \leq b.\tag{17}
$$

![](images/page_6_chart_0.jpg)

(a) Nominal Cost

![](images/page_6_chart_2.jpg)

(b) Bootstrap Robust Cost

Figure 2: Figure (a) illustrates the cost budgeted for a given decision ¯z as a function of the context of interest $x   =   x _ { 0 }$ using the nearest neighbors formulation (12) with $k   =   4 .$ That is, the cost estimate at the context of interest is the average of the empirical costs $L ( \bar { z } , y _ { i } )$ associated with the four training data points $( x _ { i } , y _ { i } ) \in N _ { n } ^ { k } ( x _ { 0 } )$ indicated in red closest to the context of interest. As these nearest neighbors $N _ { n } ^ { k } ( x _ { 0 } )$ are very sensitive to the particular context of interest the associated cost function indicated in black is discontinuous. Figure (b) depicts the associated cost estimates in gray using the nearest neighbors formulation based on five random bootstrap data sets. Evidently, as each bootstrap data set is slightly different the associated cost estimates will differ slightly as well. Definition 1 calls a cost estimate bootstrap robust if only a small fraction b of all such bootstrapped cost estimates would break budget. We depict in red one such robust cost estimate $( b = 0 . 0 5 )$ computed empirically as the corresponding quantile of the cost estimates based on $| B | = 2 0 0 0$ bootstrap data sets. When these bootstrap data sets are good proxies for actual out-of-sample data and if nearest neighbors is an appropriate learning method then the newsvendor can reasonably hope that the associated robust prescription and budget will not disappoint.

Notice however that the bootstrap out-of-sample metric and counterpart as described before are entirely descriptive and do not suggest how to ensure a budget minimization approach does in fact enjoy such good performance. In Section 4 we will present a disciplined approach to do so based on a distributionally robust approach.

The careful reader may remark that data-driven prescription formulations which are bootstrap robust do not promise any theoretical performance guarantees on actual out-of-sample data. Indeed, bootstrap robustness is identified with small disappointment on bootstrap data as opposed to actual out-of-sample data as we have illustrated in Figure 2 in the context of the newsvendor problem. That bootstrap data serves as a sensible proxy to actual out-of-sample data was advanced already by Efron (1982). Hence, one may hope that good performance on bootstrap data will translate to good performance on out-of-sample data as well.

One could try to aim for stronger theoretical guarantees regarding the out-of-sample performance of our proposed robust formulations in the spirit of Equation (6) as done by Ban and Rudin (2019) and Bertsimas and Kallus (2020). However, such theoretical guarantees require parametric assumptions on the prescription function, i.e., $z ^ { \star } \in \mathcal { C }$ . Such assumptions are hard to justify in the context of many practical problems. Even for those problems where such assumptions can be justified, it is unclear whether the Rademacher complexity of a general parametric class of functions C can be determined numerically or whether the provided guarantee is in fact not overly pessimistic. Instead, we will illustrate in Section 5 the empirical efficacy of our bootstrap robust formulations in the context of a small newsvendor problem.

## 1.4 Main Contributions

The three main contributions presented in this paper are as follows.

1. We show that both the classical Nadaraya-Watson and nearest neighbors formulations admit tractable robust counterparts as discussed in Equation (9) for a large variety of ambiguity sets $\mathcal { A } \subseteq \mathcal { D } _ { n }$ . In fact we will do so by treating either formulation as a special case of a more general variable metric estimation formulation. We prove in Section 3 that the resulting budget minimization formulations are computationally as tractable as their nominal counterparts. When for instance the estimate-first-optimize-later formulation reduces to a tractable convex optimization problem then so will its robust counterpart. The previous crucial observation testifies to the practical viability of our robust budget minimization formulations.

Robust Nadaraya-Watson formulations have been proposed before, most notably by Hanasusanto and Kuhn (2013) in the context of robust dynamic programming. However, we point out in Remark 1 that our robust Nadaraya-Watson formulation is of a different nature. Hence, even in the particular context of the Nadaraya-Watson formulation, our application of a distributional robust perspective for prescription problems with contextual information is novel.

2. One particular distributionally robust counterpart based on the relative entropy ball is proven to safeguard against overfitting on bootstrap data as discussed in Definition 1. We derive in Section 4 practical finite sample bootstrap performance guarantees regarding the resulting robust supervised learning formulation. For this particular bootstrap robust counterpart we further derive a more explicit tractable reformulation based on convex duality. Although we do not prove that our bootstrap robust formulations enjoy guaranteed out-of-sample performance, we demonstrate empirically that this is nevertheless the case in the context of a small newsvendor problem discussed in Section 5.

3. Finally, we published a Julia implementation of the algorithms in this work at [https://gitlab.com/vanparys/BootstrapRobustAnalytics.jl](https://gitlab.com/vanparys/BootstrapRobustAnalytics.jl).

## 2 Estimate-First-Optimize-Later Prescriptions

The estimate-first-optimize-later formulations which we defined in Equation (7) are distinct only in so far they are based on different cost estimates. A large variety of methods in machine learning can provide such estimates. We will focus here solely on the Nadaraya-Watson formulation of Ban and Rudin (2019) and Hannah, Powell, and Blei (2010) and the nearest neighbors formulation introduced by Bertsimas and Kallus (2020). In fact, we will treat here both formulations simultaneously by considering a generalization based on the estimator discussed in Sain (2002). As this estimator is a local learning method it is based on the concept of neighborhoods depicted visually in Figure 3.

Definition 2 (Distance & Neighborhood). Let dist $\iota ( \bar { d } , x _ { 0 } ) \geq 0$ for all $\bar { d } \in \Omega$ . Assume this distance function enjoys the discrimination property dist $( \bar { d } , \bar { x } ) = \mathrm { d i s t } ( \bar { d } ^ { \prime } , \bar { x } ) \iff \bar { d } = \bar { d } ^ { \prime }$ for all $\bar { d } ,   \bar { d ^ { \prime } }$ in Ω. Let

$$
N _ {n} ^ {j} (x _ {0}) := \left\{\bar {d} \in \mathrm{tr} [ n ] : \mathrm{dist} (\bar {d}, x _ {0}) \leq R _ {n} ^ {j} \right\}, \text {with} \mathrm{R} _ {\mathrm{n}} ^ {\mathrm{j}} := \min \left\{\mathrm{R} \geq 0 : \left| \left\{\bar {\mathrm{d}} \in \mathrm{tr} [ \mathrm{n} ] : \mathrm{dist} (\bar {\mathrm{d}}, \mathrm{x} _ {0}) \leq \mathrm{R} \right\} \right| \geq \mathrm{j} \right\}
$$

each containing those j distinct points in the training data closest to our context of interest $x _ { 0 }$

The particular distance dist $( \bar { d } , x _ { 0 } )$ should ideally reflect how relevant an observation $\bar { d }$ is to our context of interest $x   =   x _ { 0 }$ . A common choice<sup>3</sup>is to define the distance as a monotonically decreasing function of the Euclidean distance $\left\| \bar{x} - x_{0} \right\|_{2}$ between the covariates.

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">kxi − x0k2 = kxj − x0k</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">¯xi 6= ¯xj</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280"><sup>3</sup>Notice that this distance function does not possess the discrimination property. Indeed, when ¯ ¯ for we have a tie. The lack of discrimination property translates in ambiguously defined neighborhood sets. The discrimination property may be recovered by deterministically breaking ties based for instance on the value of ȳ. Györfi et al. (2006) propose a randomized alternative by augmenting the covariates with an independent auxiliary uniformly distributed random variable on [0, 1]. They prove that by doing so ties occur with probability zero.</span></small>

![](images/page_8_image_0.jpg)

Figure 3: The three and four nearest neighbors (in orange) of the context of interest $x _ { 0 }$ . We depict the neighborhood set $N _ { n } ^ { 3 } ( x _ { 0 } )$ as the orange circle. This neighborhood contains both the three and four nearest neighbors around $x _ { 0 }$ as the most distant nearest neighbor was seen twice in the training data.

Definition 3 (Estimation formulation). Our estimation formulation minimizes the weighted average

$$
z _ {\mathrm{tr} [ n ]} (x _ {0}) \in \arg \min _ {z} \left\{\mathrm{E} _ {D _ {\mathrm{tr} [ n ]}} ^ {n} [ L (z, y) | x = x _ {0} ] := \frac {\mathbb {E} _ {D _ {\mathrm{tr} [ n ]}} \left[ L (z , y) \cdot w _ {n} (x , x _ {0}) \cdot \mathbb {1} \{(x , y) \in N _ {n} ^ {k} (x _ {0}) \} \right]}{\mathbb {E} _ {D _ {\mathrm{tr} [ n ]}} \left[ w _ {n} (x , x _ {0}) \cdot \mathbb {1} \{(x , y) \in N _ {n} ^ {k} (x _ {0}) \} \right]} \right\}\tag{18}
$$

using a positive weighing function $w _ { n }$ over the smallest data neighborhood around the context $x = x _ { 0 }$ containing no less than k out of n observations.

Our estimator hence considers only data within the smallest neighborhood around its context of interest $x = x _ { 0 }$ containing no less than k out of n observations and is insensitive to all other data points. Within the neighborhood $N _ { n } ^ { k } ( x _ { 0 } )$ each data point $( \bar { x } , \bar { y } )$ is weighted as $w _ { n } ( \bar { x } , \bar { y } )   \geq   0$ with the help of a weighing function. It can easily be verified that this estimator is insensitive to the order of the data points in the training data set. Hence, the estimator is indeed only a function of the training data through its empirical distribution and the total number of samples n. Furthermore Assumption 1, which we will assume holds throughout the remainder of this paper, guarantees that formulation (18) is convex.

Assumption 1 (Loss function). The loss function $L ( \bar { z } , \bar { y } )$ in $\mathrm { R } _ { + } \cup \{ + \infty \}$ is convex in z¯ for any ȳ and a measurable function of ȳ for any z¯.

## 2.1 Nadaraya-Watson and Nearest Neighbors Learning

Formulation (18) has several hyper-parameters which have to be chosen with care; the distance function, the number of neighbors, and the weighing function. The statistical properties of the formulation depend on how these hyper-parameters are chosen. We do not try to establish here the statistical consistency of the formulation in its greatest generality. Rather, we briefly discuss the statistical consistency of its two most common special cases: (i) Nadaraya-Watson and (ii) nearest neighbors learning.

The Nadaraya-Watson formulation of Ban and Rudin (2019) and Hannah, Powell, and Blei (2010) is identified with the particular choice $k ( n ) = n$ . The Nadaraya-Watson formulation minimizes indeed the weighted average using a positive weighting function $w _ { n }$ over all observations. Typically, the weighing function is taken to be $w _ { n } ( \bar { x } , x _ { 0 } ) = S ( \left\| \bar { x } - x _ { 0 } \right\| _ { 2 } / h ( n ) )$ with the help of a positive smoothing function S and bandwidth parameter $h ( n )$ Some common popular choices of smoothers are given in Figure 4.

| Name Smoother S |
| --- |
| Uniform 121k∆xk≤1 ETGrpaiaucnussebiciachnnikov 7801ex34(1(p1-(--kkk∆∆∆xxxkkk322)3)/112kk)∆∆/√xxkk2≤≤π11 |

![](images/page_9_chart_1.jpg)

Figure 4: A comparison of popular common smoother functions S.

$$
z _ {\mathrm{tr} [ n ]} (x _ {0}) \in \arg \min _ {z} \left\{\mathrm{E} _ {D _ {\mathrm{tr} [ n ]}} ^ {n} [ L (z, y) | x = x _ {0} ] := \frac {\mathbb {E} _ {D _ {\mathrm{tr} [ n ]}} [ L (z , y) \cdot w _ {n} (x , x _ {0}) ]}{\mathbb {E} _ {D _ {\mathrm{tr} [ n ]}} [ w _ {n} (x , x _ {0}) ]} \right\}.\tag{19}
$$

Choosing the trivial weighing function $w _ { n } ( x , x _ { 0 } )   =   1$ on the other hand yields precisely the nearest neighbors formulation already introduced in Section 1.2. The nearest neighbors formulation indeed minimizes the historical average loss restricted to the smallest data neighborhood around the context $x   =   x _ { 0 }$ containing no less than k observations.

$$
z _ {\mathrm{tr} [ n ]} (x _ {0}) \in \arg \min _ {z} \left\{\mathrm{E} _ {D _ {\mathrm{tr} [ n ]}} ^ {n} [ L (z, y) | x = x _ {0} ] := \frac {\mathbb {E} _ {D _ {\mathrm{tr} [ n ]}} \big [ L (z , y) \cdot \mathbb {1} \{(x , y) \in N _ {n} ^ {k} (x _ {0}) \} \big ]}{\mathbb {E} _ {D _ {\mathrm{tr} [ n ]}} [ \mathbb {1} \{(x , y) \in N _ {n} ^ {k} (x _ {0}) \} ]} \right\}\tag{20}
$$

Theorems 7 and 8 in Appendix A guarantee the point-wise consistency of the cost estimates for a fixed decision for Nadaraya-Watson and nearest neighbors learning, respectively. Point-wise consistency of cost estimates crucially does not immediately establish consistency of the associated budget minimization formulations, i.e.,

$$
\lim _ {n \to \infty} \mathbb {E} _ {D ^ {\star}} \big [ L (z _ {\mathrm{data} [ n ]}, y) | x = x _ {0} \big ] = \min _ {z} \mathbb {E} _ {D ^ {\star}} [ L (z, y) | x = x _ {0} ].\tag{21}
$$

For the latter uniform convergence of the cost estimates needs to be shown. Bertsimas and Kallus (2020) do so under rather mild technical assumptions. Indeed, it suffices to assume that the family of loss functions $\{ L ( \cdot , \bar { y } ) \} _ { \bar { y } }$ is equicontinuous. This equicontinuity assumption is rather mild as any family of functions with common Lipschitz constant is equicontinuous. Lemma 4 of Bertsimas and Kallus (2020) establishes that under equicontinuity if the cost estimates converge, they do so necessarily uniformly in the decision which in turn guarantees consistency of the associated budget minimization formulation; see also Appendix A.

## 2.2 Bootstrap Estimates via Convex Optimization

We show here that estimation on bootstrap data can be posed as a convex optimization problem. The significance of this result will only become fully clear in Section 3. Recall that any bootstrap data set bs[n] shares its observations with the training data set tr[n] from which it is resampled modulo their frequency. In terms of its empirical

distribution $D _ { \mathrm { b s } [ n ] }$ this translates to

$$
D _ {\mathrm{bs} [ n ]} \in \mathcal {D} _ {n, n} := \left\{D: \sum_ {(\bar {x}, \bar {y}) \in \Omega_ {n}} D [ \bar {x}, \bar {y} ] = 1, n \cdot D [ \bar {x}, \bar {y} ] \in \{0, 1, 2, \dots , n \} \quad \forall (\bar {x}, \bar {y}) \in \Omega_ {n} \right\} \subset \mathcal {D} _ {n}.
$$

We will have need for a characterization of our estimator $\mathrm { E } _ { D } ^ { n } [ L ( \bar { z } , y ) | x = x _ { 0 } ]$ defined in Equation (18) as an explicit function of bootstrap distributions D in $\mathcal { D } _ { n , n }$ . This can be done by first associating a partial estimator to each of the neighborhoods sets $N _ { n } ^ { j } ( x _ { 0 } ) , j \in [ n ]$ with the help of a linear optimization problem

$$
\begin{array}{l l} \mathrm{E} _ {D} ^ {n, j} \left[ L (\bar {z}, y) | x = \bar {x} \right] := \sup _ {s > 0, P} & \sum_ {(\bar {x}, \bar {y}) \in N _ {n} ^ {j} (x _ {0})} w _ {n} (\bar {x}, x _ {0}) \cdot L (\bar {z}, \bar {y}) \cdot P [ \bar {x}, \bar {y} ] \\ \text {s.t.} & P [ \bar {x}, \bar {y} ] \geq 0, s \cdot D [ \bar {x}, \bar {y} ] = P [ \bar {x}, \bar {y} ] \quad \forall (\bar {x}, \bar {y}) \in \Omega_ {n}, \\ & \sum_ {(\bar {x}, \bar {y}) \in \Omega_ {n}} P [ \bar {x}, \bar {y} ] = s, \sum_ {(\bar {x}, \bar {y}) \in N _ {n} ^ {j} (x _ {0})} w _ {n} (\bar {x}, x _ {0}) \cdot P [ \bar {x}, \bar {y} ] = 1, \\ & \sum_ {(\bar {x}, \bar {y}) \in N _ {n} ^ {j} (x _ {0})} P [ \bar {x}, \bar {y} ] \geq \frac {k}{n} \cdot s, \sum_ {N _ {n} ^ {j - 1} (x _ {0})} P [ \bar {x}, \bar {y} ] \leq \frac {k - 1}{n} \cdot s. \end{array}\tag{22}
$$

Here an optimization variable $P [ \bar { x } , \bar { y } ]$ for each distinct observed data point $( \bar { x } , \bar { y } )$ in the training data $\operatorname { t r } [ n ]$ is introduced together with an additional variable s. Note that the domain of the partial estimators as a function of the distribution D satisfies

$$
\begin{array}{l l} & \text {dom} \mathrm{E} _ {D} ^ {n, j} \left[ L (z, y) | x = \bar {x} \right] \\ \subseteq & \mathcal {D} _ {n} ^ {j} := \left\{D \in \mathcal {D} _ {n}: \sum_ {N _ {n} ^ {j - 1} (x _ {0})} D [ \bar {x}, \bar {y} ] \leq (k - 1) / n <   k / n \leq \sum_ {(\bar {x}, \bar {y}) \in N _ {n} ^ {j} (x _ {0})} D [ \bar {x}, \bar {y} ] \right\}. \end{array}\tag{23}
$$

For a distribution D to be in the domain of the partial estimator the constraints in the optimization formulation given in equation (22) must indeed be feasible. In other words, there must exist some P and $s   >   0$ for which $s \cdot D [ \bar { x } , \bar { y } ] = P [ \bar { x } , \bar { y } ]$ for all $( \bar { x } , \bar { y } ) \in \Omega _ { n }$ . The last two constraints in equation (22) then imply that any such $D \in \mathcal { D } _ { n }$ must also be in $\mathcal { D } _ { n } ^ { j }$ . We follow here the standard convention that the supremum over an empty set is unbounded from below. Our estimator can now be decomposed as the maximum of each of the partial estimators previously defined. We defer the proof of the following result to Appendix B.1.

Theorem 1 (An Equivalent Optimization Characterization). The estimator defined in (18) can be characterized as

$$
\begin{array}{r l} \mathrm{E} _ {D} ^ {n} [ L (z, y) | x = x _ {0} ] & = \left\{ \begin{array}{l l} \mathrm{E} _ {D} ^ {n, 1} [ L (z, y) | x = x _ {0} ] & \text {if D\in\mathcal {D} _{n} ^{1}}, \\ \vdots & \vdots \\ \mathrm{E} _ {D} ^ {n, n} [ L (z, y) | x = x _ {0} ] & \text {if D\in\mathcal {D} _{n} ^{n}}, \end{array} \right. \\ & = \max _ {j \in [ n ]} \mathrm{E} _ {D} ^ {n, j} [ L (z, y) | x = x _ {0} ] \end{array}
$$

for $D \in \mathcal { D } _ { n , n }$

## 3 Distributionally Robust Prescriptions with Contextual Information

In this paper we extend the distributionally robust optimization perspective to prescription problems with contextual information. We construct generic robust formulations as suggested in Equation (9) with the help of a distribution distance function. In the next section we will then show that bootstrap robustness guarantees can be obtained by considering a very particular entropic distance function. However, we will concern ourselves in this section only with the computational tractability of generic robust formulations.

Definition 4 (Distribution Distance Function). A distribution distance function R is a function quantifying the distance between two empirical distributions in $\mathcal { D } _ { n }$ enjoying the following properties:

(i) Discrimination: $R ( D , D ^ { \prime } ) \geq 0$ for all D and $D ^ { \prime } ]$ , while $R ( D ^ { \prime } , D ) = 0$ if and only if $D ^ { \prime } = D$

(ii) Convexity: R(D, D<sup>0</sup>) is a convex function in D for all fixed $D ^ { \prime }$

We define first a generic robust counterpart following Equation (9) to a nominal formulation with respect to the ambiguity set $\mathcal { A } ( D _ { \operatorname { t r } [ n ] } ) { : = } \big \{ D \in \mathcal { D } _ { n } : R ( D , D _ { \operatorname { t r } [ n ] } ) \leq r \big \}$ consisting of all empirical distributions at distance not exceeding r.

Definition 5 (Distributionally Robust Budget Formulations). The distributionally robust counterpart to a estimatenow-optimize-later formulation with respect to the distribution distance function R is defined as

$$
\begin{array}{r l} z _ {\mathrm{tr} [ n ]} ^ {\mathrm{r}} (x _ {0}) \in \arg \min _ {z} c _ {n} (z, D _ {\mathrm{tr} [ n ]}, x _ {0}) := \sup _ {D} & \mathrm{E} _ {D} ^ {n} [ L (z, Y) | x = x _ {0} ] \\ \text {s.t.} & D \in \mathcal {D} _ {n}, \\ & R (D, D _ {\mathrm{tr} [ n ]}) \leq r. \end{array}\tag{24}
$$

Due to the discrimination property of the distribution distance function, the nominal supervised learning formula tion is recovered when the robustness radius is zero. In that case we are indeed merely robust with respect to the singleton $\big \{ D : R ( D , D _ { \operatorname { t r } [ n ] } ) \leq 0 \big \} = \{ D _ { \operatorname { t r } [ n ] } \}$ . Using a robust counterpart instead of nominal supervised learning formulations should protect us against making prescriptions which do well on the training data set but tend to disappoint on out-of-sample data. The robust training prescription $z _ { \mathrm { t r } [ n ] } ^ { \mathrm { r } } ( x _ { 0 } )$ indeed does well not on one particular empirical training distribution $D _ { \mathrm { t r } [ n ] }$ but rather uniformly well on all distributions $\big \{ D : R ( D , D _ { \operatorname { t r } [ n ] } ) \leq r \big \}$ at distance less than r. The particular distance function R dictates which distributions are close to the empirical training distribution and consequently should be chosen with care. Many popular choices are discussed in detail by Postek, den Hertog, and Melenberg (2016).

We have in Section 2 divided the training data into the nested neighborhoods $N _ { n } ^ { j } ( x _ { 0 } ) , \; j \in [ n ]$ . Each of these neighborhoods sets contains those data points closest to the context of interest $x = x _ { 0 }$ . We associated with each of these neighborhoods partial estimators $\mathrm { E } _ { D } ^ { n , j } \left[ L ( z , y ) | x = x _ { 0 } \right]$ . Theorem 1 showed that our estimator $\mathrm { E } _ { D } ^ { n } [ L ( z , Y ) | x = x _ { 0 } ]$ can be characterized as the maximum of these partial estimators. We likewise first define partial robust estimators via the optimization problems

$$
\begin{array}{l l} c _ {n} ^ {j} (z, D, x _ {0}) := \sup _ {s > 0, P} & \sum_ {(\bar {x}, \bar {y}) \in N _ {n} ^ {j} (x _ {0})} w _ {n} (\bar {x}, x _ {0}) \cdot L (z, \bar {y}) \cdot P [ \bar {x}, \bar {y} ] \\ \text {s.t.} & s \cdot R (P / s, D) \leq s \cdot r, \\ & \sum_ {(\bar {x}, \bar {y}) \in \Omega_ {n}} P [ \bar {x}, \bar {y} ] = s, \sum_ {(\bar {x}, \bar {y}) \in N _ {n} ^ {j} (x _ {0})} w _ {n} (\bar {x}, x _ {0}) \cdot P [ \bar {x}, \bar {y} ] = 1, \\ & \sum_ {(\bar {x}, \bar {y}) \in N _ {n} ^ {j} (x _ {0})} P [ \bar {x}, \bar {y} ] \geq s \cdot k / n, \sum_ {(\bar {x}, \bar {y}) \in N _ {n} ^ {j - 1} (x _ {0})} P [ \bar {x}, \bar {y} ] \leq s \cdot (k - 1) / n. \end{array}\tag{25}
$$

The previous maximization problems characterizing the partial robust estimators are all concave. Its first optimization variable s is one dimensional, while an additional optimization variable $P ( \bar { x } , \bar { y } )$ is introduced for each distinct training data point in the empirical support $\Omega _ { n }$ . Its first constraint is the only nonlinear one and is convex as the perspective function $s \cdot R ( P / s , D )$ is convex jointly in both variables. In the proof of the theorem stated hereafter we show that

$$
c _ {n} ^ {j} (z, D, x _ {0}) = \sup \left\{\mathrm{E} _ {D} ^ {n, j} [ L (z, y) | x = x _ {0} ]: D \in \mathcal {D} _ {n}, R (D, D _ {\operatorname{tr} [ n ]}) \leq r \right\}
$$

is indeed the robust counterpart of the partial estimators associated with the nested neighborhoods $N _ { n } ^ { j } ( x _ { 0 } )$

Theorem 2 (Robust Estimation Formulation). Our robust estimation formulation $( 2 4 )$ can be reformulated as the convex optimization problem

$$
z _ {\mathrm{tr} [ n ]} ^ {\mathrm{r}} (x _ {0}) \in \arg \min _ {z} c _ {n} (z, D _ {\mathrm{tr} [ n ]}, x _ {0}) = \arg \min _ {z} \max _ {j \in [ n ]} c _ {n} ^ {j} (z, D _ {\mathrm{tr} [ n ]}, x _ {0}).\tag{26}
$$

Proof. The chain of equalities

$$
\begin{array}{r l} \big \{(s > 0, P) : \exists D \in \mathcal {D} _ {n} \text {s.t.} s \cdot D = P, R (D, D _ {\mathrm{tr} [ n ]}) \leq r \big \} & = \big \{(s > 0, P) : R (P / s, D _ {\mathrm{tr} [ n ]}) \leq r \big \} \\ & = \big \{(s > 0, P) : s \cdot R (P / s, D _ {\mathrm{tr} [ n ]}) \leq s \cdot r \big \} \end{array}
$$

implies that the robust partial budget function $c _ { n } ^ { j } ( z , D _ { \mathrm { t r } [ n ] } , x _ { 0 } )$ correspond exactly to the robust version

$$
\sup \left\{\mathrm{E} _ {D} ^ {n, j} \left[ L (z, y) | x = x _ {0} \right]: D \in \mathcal {D} _ {n}, R (D, D _ {\operatorname{tr} [ n ]}) \leq r \right\}
$$

of the partial estimators. We have from Theorem 1 the decomposition $c _ { n } ( z , D _ { \operatorname { t r } [ n ] } , x _ { 0 } ) : = { \qopname \relax n { m a x } } _ { j \in [ n ] } c _ { n } ^ { j } ( z , D _ { \operatorname { t r } [ n ] } , x _ { 0 } )$ The final optimization formulation is convex as it consists of minimizing the maximum of the individually convex partial budget functions $c _ { n } ^ { j } ( z , D _ { \mathrm { t r } [ n ] } , x _ { 0 } )$ as per standing Assumption 1. □

The previous theorem guarantees the computational tractability of our robust estimation formulation and in particular entails as special cases both robust Nadaraya-Watson and nearest neighbors formulations. We conclude this section by stating that for the former formulation a less involved characterization can be obtained. We defer the proof of this result to Appendix B.3.

Corollary 1. (Robust Nadaraya-Watson Formulation) The robust Nadaraya-Watson learning formulation $\langle k ( n ) =$ n) can be reformulated as the convex optimization problem $z _ { \operatorname { t r } [ n ] } ^ { \operatorname { r } } ( x _ { 0 } ) \in { \operatorname { a r g } \operatorname* { m i n } } _ { z } c _ { n } ( z , D _ { \operatorname { t r } [ n ] } , x _ { 0 } )$ with

$$
\begin{array}{r l} {c _ {n} (z, D _ {\mathrm{tr} [ n ]}, x _ {0}) =} & {\sup _ {s > 0, P} \sum_ {(\bar {x}, \bar {y}) \in \Omega_ {n}} w _ {n} (\bar {x}, x _ {0}) \cdot L (z, \bar {y}) \cdot P [ \bar {x}, \bar {y} ]} \\ {\mathrm{s.t.}} & {s \cdot R (P / s, D _ {\mathrm{tr} [ n ]}) \leq s \cdot r,} \\ & {\sum_ {(\bar {x}, \bar {y}) \in \Omega_ {n}} P [ \bar {x}, \bar {y} ] = s, \sum_ {(\bar {x}, \bar {y}) \in \Omega_ {n}} w _ {n} (\bar {x}, x _ {0}) \cdot P [ \bar {x}, \bar {y} ] = 1.} \end{array}
$$

Remark 1. Robust Nadaraya-Watson formulations have been proposed before, most notably by Hanasusanto and Kuhn (2013) in the context of robust dynamic programming. We briefly take here the opportunity to point out that our robust Nadaraya-Watson formulation is different. The robust Nadaraya-Watson formulations found in Hanasusanto and Kuhn (2013) correspond directly to the more restricted alternative

$$
\begin{array}{r l} {c _ {n} ^ {\prime} (z, D _ {\mathrm{tr} [ n ]}, x _ {0}) := \sup _ {D}} & {\sum_ {(\bar {x}, \bar {y}) \in \Omega_ {n}} w _ {n} (\bar {x}, x _ {0}) \cdot L (z, \bar {y}) \cdot D [ \bar {x}, \bar {y} ] / \sum_ {(\bar {x}, \bar {y}) \in \Omega_ {n}} w _ {n} (\bar {x}, x _ {0}) \cdot D [ \bar {x}, \bar {y} ]} \\ {\mathrm{s.t.}} & {R (D, D _ {\mathrm{tr} [ n ]}) \leq r,} \\ & {\sum_ {(\bar {x}, \bar {y}) \in \Omega_ {n}} w _ {n} (\bar {x}, x _ {0}) \cdot D [ \bar {x}, \bar {y} ] = \sum_ {(\bar {x}, \bar {y}) \in \Omega_ {n}} w _ {n} (\bar {x}, x _ {0}) \cdot D _ {\mathrm{tr} [ n ]} [ \bar {x}, \bar {y} ].} \end{array}
$$

In Hanasusanto and Kuhn (2013) one particular convex distribution distance function R based on a scaled version of the Pearson distance is singled out. In terms of the convex reformulation given in Corollary 1, this alternative can be seen to correspond to simply restricting the optimization variable $s   >   0$ to take the particular value $s =$ $\textstyle 1 / { \sum _ { ( \bar { x } , \bar { y } ) \in \Omega _ { n } } w _ { n } ( \bar { x } , x _ { 0 } ) \cdot D _ { \operatorname { t r } [ n ] } [ \bar { x } , \bar { y } ] }$ . Even in the particular context of the Nadaraya-Watson formulation, our notion of distributional robustness hence seems to be novel.

## 4 Bootstrap Robust Prescriptions with Contextual Information

In this section we indicate that for a judiciously chosen distribution distance function our robust prescriptive formulations can be guaranteed to be bootstrap robustness as defined in Definition 1.

Definition 6 (The Bootstrap Distance Function). For two empirical distributions D and $D ^ { \prime }$ in $\mathcal { D } _ { n }$ we define their bootstrap distance as

$$
B (D, D ^ {\prime}) := \sum_ {(\bar {x}, \bar {y}) \in \Omega_ {n}} D [ \bar {x}, \bar {y} ] \cdot \log \left(\frac {D [ \bar {x} , \bar {y} ]}{D ^ {\prime} [ \bar {x} , \bar {y} ]}\right).\tag{27}
$$

The relative entropy is also known as information for discrimination, cross-entropy, information gain or Kullback-Leibler divergence (Kullback and Leibler, 1951). We first prove that its associated robust estimation formulations are statistically consistent under mild conditions.

## 4.1 Statistical Consistency

The bootstrap robust Nadaraya-Watson formulation will be consistent for bounded loss functions when the robustness radius $r ( n )$ is appropriately scaled with respect to the bandwidth parameter $h ( n )$

Theorem 3 (Bootstrap Robust Nadaraya-Watson Formulation). Assume a bounded loss function $L ( \bar { z } , \bar { y } ) < \bar { L } < \infty$ for all feasible decisions z¯ and parameters ȳ. Let $h ( n ) = c n ^ { - \delta }$ for some $c > 0$ and $\delta \in ( 0 , 1 / \mathrm { d i m } ( x ) )$ . Let S be any of the smoother functions listed in Figure 4 and the weighing function is taken to be $w _ { n } ( \bar { x } , x _ { 0 } ) = S ( \left\| \bar { x } - x _ { 0 } \right\| _ { 2 } / h ( n ) )$ Let the robustness radius satisfy $\scriptstyle \operatorname* { l i m } _ { n \to \infty } { \sqrt { r ( n ) } } / h ( n ) ^ { \dim ( x ) } { \mathrm { ~ = ~ } } 0$ for distribution distance function $R = B$ Then, bootstrap robust estimation (with $k ( n ) = n )$ is asymptotically consistent for any $D ^ { \star }$ , i.e., with probability one

$$
\lim _ {n \to \infty} \mathbb {E} _ {D ^ {\star}} \Big [ L (z _ {\mathrm{data} [ n ]} ^ {r (n)}, y) | x = x _ {0} \Big ] = \min _ {z} \mathbb {E} _ {D ^ {\star}} [ L (z, y) | x = x _ {0} ].
$$

We defer the proof of the previous result to Appendix B.4. A similar result established in Appendix B.5 holds for the bootstrap robust nearest neighbors formulation when the robustness radius $r ( n )$ is scaled appropriately as a function of the number of nearest neighbors $k ( n )$ :

Theorem 4 (Bootstrap Robust Nearest Neighbors Formulation). Assume a bounded loss function $L ( z , \bar { y } ) < \bar { L } < \infty$ for all feasible decisions z¯ and parameters ȳ. Let dist $( \bar { d }   =   ( \bar { x } , \bar { y } ) , x _ { 0 } )   =   \left\| \bar { x } - x _ { 0 } \right\| _ { 2 }$ and follow the randomized tie breaking rule discussed in Györfi et al. (2006). Let $k ( n )   =   \lceil \operatorname* { m i n } \{ c n ^ { \delta } , n \} \rceil$ for some $c > 0$ and $\delta   \in   ( 0 , 1 )$ . Let the robustness radius satisfy lim $\operatorname { l i } _ { n \to \infty } n \sqrt { r ( n ) } / k ( n ) = 0$ for distribution distance function $R = B$ . Then, bootstrap robust estimation $( w _ { n } ( \bar { x } , x _ { 0 } ) = 1 )$ is asymptotically consistent for any $D ^ { \star }$ , i.e., with probability one

$$
\lim _ {n \to \infty} \mathbb {E} _ {D ^ {\star}} \Big [ L (z _ {\mathrm{data} [ n ]} ^ {r (n)}, y) | x = x _ {0} \Big ] = \min _ {z} \mathbb {E} _ {D ^ {\star}} [ L (z, y) | x = x _ {0} ].
$$

## 4.2 Bootstrap Performance

We will now see that a particular robustness radius is advisable if a certain bootstrap performance is required. To establish that besides consistency, the bootstrap robust estimation formulation suffers only a limited bootstrap disappointment, we will need one elementary result from large deviation theory. The following theorem characterizes the essential large deviation behavior of the empirical distribution $D _ { \mathrm { b s } [ n ] }$ of the bootstrap data resampled from the training data as outlined in Equation (14).

Theorem 5 (The Bootstrap Inequality (Csiszár, 1984, Theorem 1)). The probability that the random bootstrap distribution $D _ { \mathrm { b s } [ n ] }$ realizes in any convex set $\mathcal { C } \subseteq \mathcal { D } _ { n }$ satisfies the finite sample inequality

$$
D _ {\mathrm{tr} [ n ]} ^ {\infty} \left[ D _ {\mathrm{bs} [ n ]} \in \mathcal {C} \right] \leq \exp \left(- n \cdot \inf _ {D \in \mathcal {C}} B (D, D _ {\mathrm{tr} [ n ]})\right), \quad \forall n \geq 1.\tag{28}
$$

The geometry of the bootstrap inequality is visualized in Figure 5.

Notice that for the optimization problem defining the partial budget functions $c _ { n } ^ { j }$ to be nontrivial for the empirical training distribution $D _ { \mathrm { t r } [ n ] }$ , the robustness radius r defining our ambiguity set needs to be bigger than the minimum robustness radius

$$
\begin{array}{c l} r _ {n} ^ {j} := \inf & R (D, D _ {\mathrm{tr} [ n ]}) \\ \text {s.t.} & D \in \mathcal {D} _ {n} ^ {j} \end{array}\tag{29}
$$

![](images/page_14_image_0.jpg)

Figure 5: Visualization of the bootstrap inequality (28) stated in Theorem 5. The probability $D _ { \mathrm { t r } [ n ] } ^ { \infty } ( D _ { \mathrm { b s } [ n ] } \in \mathcal { C } )$ decays with increasing number of samples n at the exponential rate $r \; : = \; { \operatorname* { i n f } } _ { D \in { \mathcal { C } } } B \big ( D , D _ { \operatorname { t r } [ n ] } \big )$ , which can be interpreted as the bootstrap distance of the empirical training distribution $D _ { \mathrm { t r } [ n ] }$ to the set of interest C.

where $\mathcal { D } _ { n } ^ { j }$ was defined in (23). If this is the case, then the feasible set of the optimization problem (25) defining the partial budget cost $c _ { n } ^ { j }$ is indeed non-empty. The extremal bootstrap radii are characterized too as the solution of a tractable convex optimization problem (29). These extremal bootstrap radii will come to play an important role in the characterization of the bootstrap disappointment suffered by our robust formulation as stated by the following theorem.

Theorem 6 (Bootstrap Performance of Robust Formulations). Our robust formulation with bootstrap distance function $( R = B )$ and robustness radius r suffers a bootstrap disappointment defined in (17) at most

$$
b (n) = \sum_ {j \in [ n ]} \exp \big (- n \cdot \max \{r, r _ {n} ^ {j} \} \big).
$$

Proof. Let us fix a training data set with empirical distribution $D _ { \mathrm { t r } [ n ] }$ and consider a given decision ¯z. Let $\bar { c } _ { n } ^ { j } : =$ $\mathrm { E } _ { D _ { \mathrm { t r } [ n ] } } ^ { n , j } \left[ L ( \bar { z } , y ) | x = x _ { 0 } \right]$ with $\bar { c } _ { n } = \operatorname { m a x } _ { j \in [ n ] } \bar { c } _ { n } ^ { j }$ be the budgeted cost based on the training data. In order to prove the theorem, it suffices to characterize the probability of the event that the empirical distribution $D _ { \mathrm { b s } [ n ] }$ of random bootstrap data resampled from the training data realizes in the set $\mathcal { C } = \{ D \in \mathcal { D } _ { n } : c _ { n } ( \bar { z } , D , x _ { 0 } ) > \bar { c } _ { n } \} = \cup _ { j \in [ n ] } \mathcal { C } _ { j }$ with

$$
\begin{array}{r l} \mathcal {C} _ {j} := & \Big \{D \in \mathcal {D} _ {n} ^ {j}: \mathrm{E} _ {D} ^ {n, j} \left[ L (\bar {z}, y) | x = x _ {0} \right] > \bar {c} _ {n} \Big \} \\ = & \{D \in \mathcal {D} _ {n} ^ {j}: \sum_ {(\bar {x}, \bar {y}) \in N _ {n} ^ {j} (x _ {0})} w _ {n} (\bar {x}, x _ {0}) \cdot L (\bar {z}, \bar {y}) \cdot D [ \bar {x}, \bar {y} ] > \bar {c} _ {n} \cdot \sum_ {(\bar {x}, \bar {y}) \in N _ {n} ^ {j} (x _ {0})} w _ {n} (\bar {x}, x _ {0}) \cdot D [ \bar {x}, \bar {y} ] \}. \end{array}
$$

Each of the partial sets $\mathcal { C } _ { j }$ is a convex polyhedron. We can use the union bound to establish

$$
D _ {\mathrm{tr} [ n ]} ^ {\infty} (D _ {\mathrm{bs} [ n ]} \in \mathcal {C}) \leq \sum_ {j \in [ n ]} D _ {\mathrm{tr} [ n ]} ^ {n} (D _ {\mathrm{bs} [ n ]} \in \mathcal {C} _ {j}).
$$

The robust budget cost ${ \bar { c } } _ { n }$ is constructed precisely as to ensure that inf $\ { } _ { D \in \mathcal { C } _ { j } } R ( D , D _ { \operatorname { t r } [ n ] } ) { > } r$ . Indeed, we have the implication $\bar { D } \: \in \: \mathcal { C } _ { j } \: \implies \: \operatorname { E } _ { \bar { D } } ^ { n , j } \left[ L ( \bar { z } , y ) | x = x _ { 0 } \right] \: > \: \bar { c } _ { n } \: \geq \: \operatorname* { s u p } \left\{ \operatorname { E } _ { D } ^ { n , j } \left[ L ( \bar { z } , y ) | x = x _ { 0 } \right] \: | \: R ( D , D _ { \operatorname { t r } [ n ] } ) \: \leq \: r , \: D \: \in \: \mathcal { D } _ { n } \right\}$ which in turn itself implies $R ( \bar { D } , D _ { \mathrm { t r } [ n ] } ) > r$ . By virtue of the inclusion $\mathcal { C } _ { j } \subseteq \mathcal { D } _ { n } ^ { j }$ , evidently, we must also have that inf ${ } _ { D \in \mathcal { C } _ { j } } R ( D , D _ { \operatorname { t r } [ n ] } ) > r _ { n } ^ { j } : = \operatorname* { i n f } \{ R ( D , D _ { \operatorname { t r } [ n ] } ) : D \in \mathcal { D } _ { n } ^ { j } \}$ . Hence, the result follows from the bootstrap inequality (28) applied to each of the probabilities $D _ { \mathrm { t r } [ n ] } ^ { \infty } ( D _ { \mathrm { b s } [ n ] }   \in   \mathcal { C } _ { j } )$ as in this particular case the employed distribution distance function $( R = B )$ coincides with the bootstrap distance function. □

The previous theorem guarantees a minimum exponential decay rate for the bootstrap disappointment of any bootstrap robust counterpart formulation, i.e.,

$$
\operatorname * {l i m s u p} _ {n \to \infty} \frac {1}{n} \log b (n) \leq - r.\tag{30}
$$

The bootstrap inequality (28) is asymptotically exact in the exponential rate. Sanov’s Theorem, c.f., Dembo and Zeitouni (2009, Theorem 6.2.10), indeed establishes that

$$
- \inf _ {D \in \operatorname{int} \mathcal {C}} B (D, D _ {\mathrm{tr}}) \leq \liminf _ {n \to \infty} \frac {1}{n} \log D _ {\mathrm{tr}} ^ {\infty} \left[ D _ {\mathrm{bs} [ n ]} \in \mathcal {C} \right]\tag{31}
$$

for any event set C and distribution $D _ { \mathrm { t r } }$ . Via this lower bound, our bootstrap robust distance function can be shown to the smallest distance function for the guarantee in Equation (30), and hence by extension also Theorem $6 ,$ holds. The following proposition states indeed that for any other distance function R which is larger than B on some nonempty open set, the guarantee presented Equation (30) fails to hold in general. The proof of the following result is deferred to Appendix B.2.

Proposition 1. Consider a distance function R with $R ( D ^ { \prime } , D _ { \mathrm { t r } } )   >   B ( D , D _ { \mathrm { t r } } )   =   r$ for some $D , D _ { \mathrm { t r } }   \in   \mathcal { D } _ { n }$ and all D0in some open neighborhood ${ \mathcal { N } } \subseteq { \mathcal { D } } _ { n }$ around $D   \in   { \mathcal { N } } .$ There exists a nominal formulation so that its robust counterpart given in Equation $( 2 4 )$ and disappointment set $\mathcal { R }   =   \{ D   \in   \mathcal { D } _ { n }   :   \mathrm { E } _ { D } ^ { n } [ L ( z _ { \mathrm { t r } } ^ { \mathrm { r } } ( x _ { 0 } ) , y ) | x   =   x _ { 0 } ]   >$ $\begin{array} { r } { \operatorname* { s u p } _ { R ( D ^ { \prime } , D _ { \mathrm { t r } } ) \leq r } \mathrm { E } _ { D ^ { \prime } } ^ { n } [ L ( z _ { \mathrm { t r } } ^ { \mathrm { r } } ( x _ { 0 } ) , y ) | x = x _ { 0 } ] \} } \end{array}$ satisfy

$$
- r <   \liminf _ {n \to \infty} \frac {1}{n} \log D _ {\mathrm{tr}} ^ {\infty} \left[ D _ {\mathrm{bs} [ n ]} \in \mathcal {R} \right].
$$

The previous result indicates that our bootstrap distance function B is in some precise sense optimal in safeguarding any nominal formulation against overfitting on bootstrap data. Choosing the robustness radius $r ( n )$ yielding a desired bootstrap disappointment b cannot however be done analytically. However, thanks to the convex characterization (29) of the minimum bootstrap radii $r _ { n } ^ { j }$ it can nevertheless be carried out numerically in a tractable fashion. It is also trivial to see that adding robustness to the extent $r ( n ) \geq ( \operatorname { l o g } ( n ) + \operatorname { l o g } ( 1 / b ) ) / n$ suffices to have bootstrap disappointment at most b. When we scale the robustness radius in such a way that

$$
\lim _ {n \to \infty} \frac {r (n) \cdot n}{\log (n)} = \infty
$$

then the disappointment on bootstrap data asymptotically converges to zero when the number of training data points n tends to infinity. To be asymptotically consistent the robust nearest neighbors formulation needs to satisfy lim $\operatorname { a } _ { n \to \infty } n \sqrt { r ( n ) } / k ( n ) { = } 0$ as pointed out in Theorem 4. Asymptotically vanishing disappointment on bootstrap data can be combined with consistency by taking a number of nearest neighbors $k ( n )   =   \lceil \operatorname* { m i n } \{ c n ^ { \delta } , n \} \rceil$ for some $c > 0$ and $\delta \in ( 0 , 1 )$ while at the same time scaling the robustness radius as $r ( n ) = t n ^ { \gamma }$ with $- 1 < \gamma < 2 ( \delta - 1 )$ for any $t > 0$ . For the Nadaraya-Watson formulation a slightly improved result can be established and is stated in Corollary 2. We omit its proof and refer the reader to Appendix B.6.

Corollary 2 (Bootstrap Performance of the Nadaraya-Watson Formulation). The robust formulation $( w i t h \; k ( n ) =$ n) with bootstrap distance function $( R = B )$ suffers bootstrap disappointment as defined in (17) at most

$$
b (n) = \exp (- n \cdot r).
$$

Adding robustness to the extent $r ( n ) \geq \operatorname { l o g } ( 1 / b ) / n$ already suffices here to have bootstrap disappointment at most b. When we scale the robustness radius in such a way now that li $\operatorname { n } _ { n \to \infty } r ( n ) \cdot n = \infty$ then the disappointment on bootstrap data asymptotically converges to zero when the number of training data points n tends to infinity. To be asymptotically consistent the robust Nadaraya-Watson formulation needs to satisfy lim $\scriptstyle { \mathrm { i } } _ { n \to \infty }   { \sqrt { r ( n ) } } / { h ( n ) ^ { \dim ( x ) } } \; = \; 0$ as pointed out in Theorem 3. Asymptotically vanishing disappointment on bootstrap data can also here be combined with consistency by scaling the bandwidth parameter $h ( n ) = c n ^ { \delta }$ for some $c > 0$ and $\delta \in ( 0 , 1 / \mathrm { d i m } ( x ) )$ while at the same time scaling the robustness radius as $r ( n ) = t n ^ { \gamma }$ with $- 1 < \gamma < 2 \delta \cdot \dim ( x )$ for any $t > 0$

## 4.3 Dual Formulations

Despite the previous encouraging results regarding the bootstrap performance and consistency of our robust estimation formulation, it is still stated as the solution to a saddle point problem in Equation (26). Both the size and the number of the maximization problems constituting the bootstrap robust formulation grow linearly with the amount of training data samples. The following lemma alleviates one of these concerns by considering a dual formulation of the maximization problems characterizing the partial robust cost functions. We defer its proof to Appendix B.7.

Lemma 1 (Dual representation estimation). The partial bootstrap robust $( R   =   B )$ budget $c _ { n } ^ { j } ( \bar { z } , D , x _ { 0 } )$ can be represented using a dual convex optimization problem as

$$
\begin{array}{l l} \text {inf} & \alpha \\ \text {s.t.} & \alpha \in \mathrm{R}, \eta \in \mathrm{R} _ {+} ^ {2}, \nu \in \mathrm{R} _ {+}, \\ & \nu \log \Big (\sum_ {(\bar {x}, \bar {y}) \in N _ {n} ^ {j - 1} (x _ {0})} \exp ([ (L (\bar {z}, \bar {y}) - \alpha) \cdot w _ {n} (\bar {x}, x _ {0}) + \eta_ {1} - \eta_ {2} ] / \nu) \cdot D [ \bar {x}, \bar {y} ] \\ & \quad + \sum_ {(\bar {x}, \bar {y}) \in N _ {n} ^ {j} (x _ {0}) \setminus N _ {n} ^ {j - 1} (x _ {0})} \exp ([ (L (\bar {z}, \bar {y}) - \alpha) \cdot w _ {n} (\bar {x}, x _ {0}) + \eta_ {1} ] / \nu) \cdot D [ \bar {x}, \bar {y} ] \\ & \quad + \sum_ {\Omega_ {n} \setminus N _ {n} ^ {j} (x _ {0})} D [ \bar {x}, \bar {y} ] \Big) + r \cdot \nu - \frac {k}{n} (\eta_ {1} - \eta_ {2}) - \frac {\eta_ {2}}{n} \leq 0. \end{array}\tag{32}
$$

when the robustness radius satisfies $r > r _ { n } ^ { j }$ for all $D \in \mathcal { D } _ { n }$

The main advantage of using the previous convex dual formulation of the robust budget functions is that finding the optimal prescription $z _ { \mathrm { t r } [ n ] } ^ { r } ( x _ { 0 } )$ now merely requires the solution of a convex optimization problem over the decision z and three additional dual variables $\alpha ,   \beta ,$ and η for each $j \in [ n ]$ . The dependence on the amount of training data is not completely eliminated as the constraint in the dual characterization (32) of the partial robust budget $c _ { n } ^ { j }$ still counts $j$ terms. As the robust nearest neighbors cost function $c _ { n }$ consists of the maximum of all of these partial robust cost functions we still have to account for a total number of $O ( n ^ { 2 } )$ such terms.

For the particular case of a bootstrap robust nearest neighbors formulation, Lemma 1 and Equation (26) guarantee the following convex representation.

<div class="docvortex-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Example: Bootstrap Robust Nearest-Neighbors Formulation

$z_{\mathrm{tr}[n]}^{r}(x_{0}) \in \arg \min \max_{j \in [n]} \alpha_{j}$

s.t. $z \in \mathrm{R}^{\dim(z)}$, $\alpha_{j} \in \mathrm{R}$, $\eta_{j} \in \mathrm{R}_{+}^{2}$, $\nu_{j} \in \mathrm{R}_{+}$ $\forall j \in [n]$,

$\nu_{j} \log \left( \sum_{(\bar{x},\bar{y}) \in N_{n}^{j-1}(x_{0})} \exp([L(z,\bar{y}) - \alpha_{j} + \eta_{j,1} - \eta_{j,2}] / \nu_{j}) \cdot D_{\mathrm{tr}[n]}[\bar{x},\bar{y}] \right.$

$\left. + \sum_{(\bar{x},\bar{y}) \in N_{n}^{j}(x_{0}) \setminus N_{n}^{j-1}(x_{0})} \exp([L(z,\bar{y}) - \alpha_{j} + \eta_{j,1}] / \nu_{j}) \cdot D_{\mathrm{tr}[n]}[\bar{x},\bar{y}] \right.$

$\left. + \sum_{\Omega_{n} \setminus N_{n}^{j}(x_{0})} D_{\mathrm{tr}[n]}[\bar{x},\bar{y}]\right) + r \cdot \nu_{j} - \frac{k}{n} (\eta_{j,1} - \eta_{j,2}) - \frac{\eta_{j,2}}{n} \leq 0 \quad \forall j \in [n].$
</div>

For the Nadaraya-Watson formulation a more compact optimization formulation can be derived. We defer the proof of the next result to Appendix B.8.

Lemma 2 (Dual Representation Nadaraya-Watson Estimation). The bootstrap robust $( R = B )$ cost $c _ { n } ( \bar { z } , D , x _ { 0 } )$

for $k ( n ) = n$ can be represented using a dual convex optimization problem as

$$
\begin{array}{l l} \text {inf} & \alpha \\ \text {s.t.} & \alpha \in \mathrm{R}, \nu \in \mathrm{R} _ {+}, \\ & \nu \cdot \log \left(\sum_ {(\bar {x}, \bar {y}) \in \Omega_ {n}} \exp \left((L (\bar {z}, \bar {y}) - \alpha) \cdot w _ {n} (\bar {x}, x _ {0}) / \nu\right) \cdot D [ \bar {x}, \bar {y} ]\right) + r \cdot \nu \leq 0. \end{array}\tag{33}
$$

for all $D \in \mathcal { D } _ { n }$

For the particular case of a bootstrap robust Nadaraya-Watson formulation, Lemma 2 and Equation (26) guarantee the following simplified convex representation.

<div class="docvortex-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Example: Bootstrap Robust Nadaraya-Watson Formulation

$z_{\mathrm{tr}[n]}^{r}(x_{0}) \in \arg \min \quad \alpha$

s.t. $z \in \mathrm{R}^{\dim(z)}, \alpha \in \mathrm{R}, \nu \in \mathrm{R}_{+},$

$\nu \cdot \log \left( \sum_{(\bar{x},\bar{y}) \in \Omega_{n}} \exp \left( (L(z,\bar{y}) - \alpha) \cdot w_{n}(\bar{x},x_{0}) / \nu \right) \cdot D_{\mathrm{tr}[n]}[\bar{x},\bar{y}] \right) + r \cdot \nu \leq 0.$
</div>

## 5 Numerical Example

We first briefly discuss how our supervised learning formulations were solved and trained in practice. All algorithms were implemented in Julia (Bezanson et al., 2017). The nominal Nadaraya-Watson and nearest neighbors formulations of Ban and Rudin (2019), Bertsimas and Kallus (2020), and Hannah, Powell, and Blei (2010) were implemented with the help of the Convex.jl package developed by Udell et al. (2014). Taking advantage of the dual representations given in Lemmas 2 and 1, the same procedure was followed for their robust counterparts with respect to the bootstrap distance function as well. The corresponding exponential cone optimization problems were solved numerically with the ECOS interior point solver by Domahidi, Chu, and Boyd (2013).

Both the Nadaraya-Watson and nearest neighbors formulations require several hyper parameters such as the smoother function S or the number of neighbors to be learned from data. We considered a Nadaraya-Watson formulation using the Gaussian smoother function given in Figure 4. Likewise, we considered the classical nearest neighbors formulation with the Mahalanobis distance metric

$$
d ((\bar {x}, \bar {y}), x _ {0}) = (\bar {x} - x _ {0}) ^ {\top} \Sigma_ {\mathrm{tr}[ n ]} ^ {- 1} (\bar {x} - x _ {0})
$$

based on the empirical variance and the empirical mean of the covariate data. Potential ties among equidistant points were broken based on the method discussed by Györfi et al. (2006). The bandwidth parameter $h ( n )$ and the number of nearest neighbors $k ( n )$ were determined based on the squared prediction loss performance of the corresponding Nadaraya-Watson or nearest neighbors predictive learner on ten data sets cross validated from the training data.

## 5.1 A Newsvendor Problem

We reconsider the newsvendor problem stated in Equation (10). To illustrate the approach we assume that the newsvendor considers both the day of the week $w \in \{ \mathrm { M o n d a y } , \ldots , \mathrm { S u n d a y } \}$ and the outside temperature $t \in \mathrm { R }$ as features which potentially influence customer demand. We consider synthetic training data drawn as independent samples drawn from the conditional distribution

$$
D ^ {\star} (x _ {0} = (t _ {0}, w _ {0})) = N (1 0 0 + (t _ {0} - 2 0) + 2 0 \cdot \mathbb {I} (w _ {0} \in \{\text {Weekend} \}), 1 6)
$$

and where the day of the week and outside temperature are independent random variables distributed uniformly and normally as $N ( 2 0 , 4 )$ , respectively. We shall use this synthetic data newsvendor problem to illustrate the bootstrap disappointment of the robust Nadaraya-Watson and nearest neighbors formulations in a particular context of interest, i.e., $x _ { 0 } = ( t _ { 0 } , w _ { 0 } ) = ( 1 0 ^ { \circ } \mathrm { C } ,$ Friday). We remark that Ban and Rudin (2019) discuss a Nadaraya-Watson learning formulation of a similar data-driven newsvendor problem which they denote as a kernel optimization formulation.

We first investigate to what extent our bootstrap robust formulations guard against disappointment on both synthetic bootstrap data and actual out-of-sample validation data. Given an action $z _ { \mathrm { t r } [ n ] } ^ { r }$ calibrated to the training data set and its budgeted cost estimate $c _ { n } ( z _ { \operatorname { t r } [ n ] } ^ { r } , D _ { \operatorname { t r } [ n ] } , x _ { 0 } )$ , we approximate its bootstrap and out-of-sample validation disappointment as suggested in Equations (15) and (13) using a large number $| B | = | V | = 2 0 , 0 0 0$ of resamples. In Figure 6, we present these disappointment probabilities as a function of the number of training samples for the nominal and robust Nadaraya-Watson and nearest neighbors formulations. The nominal Nadaraya-Watson of Ban and Rudin (2019) and Hannah, Powell, and Blei (2010) and the nearest neighbors formulation by Bertsimas and Kallus (2020) corresponds to the cases depicted with $r   =   0$ . Such nominal formulations do not safeguard against overfitting as they disappoint on both synthetic bootstrap data and actual out-of-sample data about half the time. The dotted lines visualize the upper bounds concerning the bootstrap disappointment of the bootstrap robust Nadaraya-Watson and nearest neighbors formulation given in Corollary 2 and Theorem 6, respectively. The guarantee in case of the nearest neighbors formulation is not as tight as its Nadaraya-Watson counterpart mostly due to the use of the union bound in the proof of Theorem 6. Nevertheless, large deviation theory via Equation (31) ensures that the empirical bootstrap disappointments and their corresponding theoretical upper bound in either formulation drop to zero at the same exponential rate r. Finally, the fact that the disappointment probability on actual out-of-sample data trends down at a similar rate with increasing number of samples as the disappointment on synthetic bootstrap data indicates that bootstrap data is here a sensible proxy to actual out-of-sample data.

Working with synthetic data also gives us the opportunity to compare the robust and nominal formulations in terms of their actual expected cost and out-of-sample disappointment. Indeed, as the distribution $D ^ { \star }$ is known we can quantify the actual cost $\mathbb { E } _ { D ^ { \star } } \big [ L ( z _ { \mathrm { d a t a } [ n ] } , y ) | x = x _ { 0 } \big ]$ of any proposed decisions $z _ { \mathrm { d a t a } [ n ] }$ analytically. To guarantee a fair comparison, the robustness radius used here for the formulation proposed by Hanasusanto and Kuhn (2013) was chosen so that both formulations matched in terms of their in-sample estimated or budgeted cost $c _ { n } ( z _ { \operatorname { t r } [ n ] } ( x _ { 0 } ) , D _ { \operatorname { t r } [ n ] } , x _ { 0 } )$ which hence is not reported. Proposition 1 indicates that our bootstrap distance function should be preferred when guarding formulations against disappointment on bootstrap data over any other distance function which as indicated in Remark 1 includes the distance function considered by Hanasusanto and Kuhn (2013). However, this advantage is rather small and both formulations enjoy a similar very performance as indicated in Table 1 in which we report the actual cost $c _ { \mathrm { o o s } }$ and disappointment on both bootstrap data $b _ { \mathrm { i n } }$ and out-of-sample data $b _ { \mathrm { o o s } }$ aggregated over 250 independent training data sets. That being said, the main practical advantage of our bootstrap distance function is that its size r can be calibrated in advance to guarantee a certain bootstrap disappointment (here $b = 0 . 1 )$ via Theorem 6 (or Corollary 2) whereas the robustness radius of the distance function in the formulation Hanasusanto and Kuhn (2013) comes with no such interpretation and ordinaril would need to be calibrated using a potentially computationally expensive validation procedure.

We are also interested in seeing how each of the methods fares if we augment the covariates with a number d of irrelevant spurious observations generated from independently sampling a standard normal distribution. It should not come as a surprise that when no spurious covariates are introduced the robust approaches in blue outperform their nominal counterparts in orange significantly as can be seen in Figure 7. The reported cost is the average among 20, 000 random training sets each of length $n = 2 0 0$ . Here, the amount of robustification r used in either formulation was determined based on ten fold cross validation. Given only $n   =   2 0 0$ training samples, both the

![](images/page_19_chart_0.jpg)

(a) Nadaraya-Watson Formulations

![](images/page_19_chart_2.jpg)

(b) Nearest Neighbors Formulations

![](images/page_19_chart_4.jpg)

(c) Nadaraya-Watson Formulations

![](images/page_19_chart_6.jpg)

(d) Nearest Neighbors Formulations

Figure 6: The empirical bootstrap disappointment b (first row) and the out-of-sample disappointment (second row) of the Nadaraya-Watson (first column) and nearest neighbors (second column) formulations in function of the number of samples n. The nominal Nadaraya-Watson and nearest neighbors formulation corresponds to the case $r = 0 .$ Such nominal formulations do not safeguard against overfitting either on bootstrap or actual out-of-sample data as they disappoint on both about half the time. The dotted lines visualize the upper bounds concerning the bootstrap disappointment of the bootstrap robust Nadaraya-Watson and nearest neighbors formulation given in Theorem 2 and Theorem 6, respectively. Large deviation theory (Csiszár, 1984) indicates that these bootstrap upper bounds and the actual bootstrap disappointments of either formulation drop to zero at the same exponential rate r. Finally, the fact that the disappointment on actual out-of-sample data trends down at a similar rate with increasing number of samples as the disappointment on synthetic bootstrap data indicates that bootstrap data is here a sensible proxy to actual out-of-sample data.

<table><tbody><tr><td rowspan="2"></td><td colspan="3">BR (b = 0.1)</td><td colspan="3">HK (matched)</td></tr><tr><td>b<sub>in</sub></td><td>b<sub>oos</sub></td><td>c<sub>oos</sub></td><td>b<sub>in</sub></td><td>b<sub>oos</sub></td><td>c<sub>oos</sub></td></tr><tr><td>N = 100</td><td>0.0209</td><td>0.0944</td><td>26.3145</td><td>0.0206</td><td>0.0948</td><td>26.524</td></tr><tr><td>N = 150</td><td>0.0012</td><td>0.0068</td><td>21.0093</td><td>0.0010</td><td>0.0067</td><td>20.9988</td></tr><tr><td>N = 200</td><td>0.0025</td><td>0.0126</td><td>17.2461</td><td>0.0023</td><td>0.0126</td><td>16.9906</td></tr><tr><td>N = 250</td><td>0.0159</td><td>0.0261</td><td>14.3198</td><td>0.0142</td><td>0.0287</td><td>13.6155</td></tr></tbody></table>

Table 1: Comparison between our bootstrap robust Nadaraya-Watson formulation (BR) and the robust formulation (HK) proposed by Hanasusanto and Kuhn (2013).

![](images/page_20_chart_0.jpg)

(a) Nadaraya-Watson Formulations

![](images/page_20_chart_2.jpg)

(b) Nearest Neighbors Formulations

Figure 7: The average actual cost $\mathbb { E } _ { D ^ { \star } } [ L ( z , y ) | x = x _ { 0 } ]$ of the decisions proposed by the nominal and robust Nadaraya-Watson formulation as well as the nominal and robust nearest neighbors formulation. The reported cost is the average among 20, 000 random training sets each of length $n = 2 0 0$ The dimension d reflects the number of spurious covariates introduced. The black line correspond to the optimal full information cost min<sub>z</sub> $\mathbb { E } _ { D ^ { \star } } [ L ( z , y ) | x = x _ { 0 } ]$ , while the red line represents the optimal no information cost min<sub>z</sub> $\mathbb { E } _ { D ^ { \star } } [ L ( z , y ) ]$ . The robust formulations dominate with large statistical significance their nominal counterparts when no spurious covariates $( d = 0 )$ are introduced. When spurious covariates are introduced $( d > 0 )$ the cost predictions $\mathrm { E } _ { D _ { \mathrm { t r } [ n ] } } ^ { n } [ L ( z , y ) | x = x _ { 0 } ]$ on which all formulations are based tend to be under-calibrated leading to both a loss of performance and leave limited room for improvement via robustification.

robust Nadaraya-Watson and nearest neighbors formulation do indeed come close to the theoretically minimal cost min<sub>z</sub> $\mathbb { E } _ { D ^ { \star } } [ L ( z , y ) | x = x _ { 0 } ]$ visualized as the black line for reference. As more spurious covariates are injected in the training data set, the performance of any data-driven method must evidently degrade. Ultimately as d tends to infinity, the noise completely drowns out the signal. The performance of data-driven methods is expected to tend to the optimal cost min<sub>z</sub> $\mathbb { E } _ { D ^ { \star } } [ L ( z , y ) ]$ without using any covariate information and is visualized as the red line.

Remark 2. It is perhaps curious to observe that the performance of the nominal Nadaraya-Watson and nearest neighbors decisions behave differently than their robust counterparts. Counter-intuitively, the performance of both nominal formulations initially improves with the introduction of spurious covariates. We observed empirically that when no spurious covariates are introduced the nominal cost estimates $\mathrm { E } _ { D _ { \mathrm { t r } [ n ] } } ^ { n } [ L ( \bar { z } , y ) | x = x _ { 0 } ]$ for all z¯ on which the nominal formulations are based tend to overfit the training data. Consequently, the nominal actions suffer poor out-of-sample performance. Our robust formulations do a good $j o b$ in alleviating this adverse phenomenon without much performance loss. The introduction of artificial noise in the data through spurious covariates seems to provide implicit protection against overfitting to the training data by preventing the selection, at least when using cross-validation, of a small bandwidth parameter $h ( n )$ or a small number of neighbors $k ( n )$ in the Nadaraya-Watson and nearest neighbor formulation, respectively. The addition of spurious covariates has a similar effect as robustification but crucially does comes with a loss of performance.

A supervised data version of this newsvendor problem is discussed by Ban and Rudin (2019) based on the empirical risk formulation stated in Equation (5) with $\mathcal { C } = \mathcal { F } _ { \mathrm { l i n } }$ the set of all linear functions and an estimate-first-optimizelater formulation using a Nadaraya-Watson estimator. In this synthetic example, the full information solution stated in Equation (11) simplifies to

$$
z ^ {\star} (x _ {0} = (t _ {0}, w _ {0})) = 1 0 0 + (t _ {0} - 2 0) + 2 0 \cdot \mathbb {I} (w _ {0} \in \{\text {Weekend} \}) + 4 \sqrt {2} \operatorname{erf} ^ {- 1} ((b - h) / (b + h))
$$

![](images/page_21_chart_0.jpg)

![](images/page_21_chart_1.jpg)

Figure 8: Comparison with the empirical risk minimization (ERM) and Nadaraya-Watson (NW) formulations proposed in Ban and Rudin (2019). The reported cost $\mathbb { E } _ { D ^ { \star } } \big [ L ( z _ { \mathrm { d a t a } [ n ] } , y ) | x = x _ { 0 } \big ]$ is the average among a 1, 000 random data sets. Naive application of the ERM formulation yields a biased learning method which does not achieve the minimum cost (indicated as the dotted black line) even in the large sample limit in contrast to the the nonparametric robust Nadaraya-Watson and nearest neighbors formulations as well as the formulation (HK) proposed by Hanasusanto and Kuhn (2013). With the help of a factor model, the ERM formulation can be made to achieve the minimum cost and in fact does so with fewer samples than the nonparametric learning formulations. We also show the out-of-sample disappointment of the three nonparametric approaches. We remark here that as empirical risk formulations do not come with a cost estimate for their optimal action in the context of interest they do not come with a similar notion of out-of-sample disappointment. Our bootstrap robust nearest neighbors formulation dominates here the other two nonparametric formulations both in terms of expected cost as well as out-of-sample disappointment.

where erf denotes the standard error function. When representing the categorical variables naively as integers, i.e., $\{ \operatorname { M o n d a y } , \ldots , \operatorname { S u n d a y } \} = \{ 1 , \ldots , 7 \}$ , the function $z ^ { \star } ( \cdot ) \not \in \mathcal { F } _ { \operatorname* { l i n } }$ is not linear in this representation and hence as discussed in the introduction, the associated empirical risk minimization formulation is biased. Consequently, the empirical risk formulation does not converge to the full information solution as empirically verified in Figure 8. In stark contrast, our robust Nadaraya-Watson and nearest neighbors formulations as well as the formulation proposed by Hanasusanto and Kuhn (2013) do not require such parametric assumptions on the full information solution to be asymptotically consistent. Indeed, as illustrated in Figure $^ { 8 , }$ all eventually achieve the full information minimum cost when n tends to infinity. In this example, our bootstrap robust nearest neighbors formulation dominates the other nonparametric formulations both in terms of expected cost as well as out-of-sample disappointment.

Clearly, by considering a standard “dummy” factor representation (Friedman, Hastie, and Tibshirani, 2001)[Section 3.2] of the categorical variables the full information solution $z ^ { \star } ( \cdot )$ becomes linear. Consequently, the empirical risk formulation with such factor model does converge to the full information solution and does so faster than our nonparametric learning formulations; see again Figure 8. This observation is not surprising and very much in line with the the fact that parametric learning is statistically more powerful when its parametric assumptions apply but may fail when its assumptions do not hold. In practice, which method should be favored will hence strongly depend on whether or not sensible parametric assumptions can be assumed on the prescription function $z ^ { \star } ( \cdot )$ in a particular application. Furthermore, the computational speed of each formulation will in practice also be of importance. In Figure 9 we indicate that as each formulation requires merely the solution of a convex optimization problem the computational times do not exceed one second. However, as remarked already by Ban and Rudin (2019), the nonparametric formulations are as a whole computationally less demanding than the empirical risk minimization formulations.

![](images/page_22_chart_0.jpg)

Figure 9: Comparison of all discussed formulations in terms of the time it takes to solve them. As ultimately all formulations require the solution of a convex optimization problem the computational times do not exceed one second. As remarked already by Ban and Rudin (2019), the nonparametric formulations (Robust NN, NW, Robust NW, HK) are as a whole computationally less demanding than the empirical risk formulations (ERM, ERM (Factor)). The difference between our bootstrap robust Nadaraya-Watson formulation and the formulation proposed by Hanasusanto and Kuhn (2013) in terms of computational times is negligible and barely visible.

## Acknowledgments

The authors would like to thank the reviewers for their careful reading of this manuscript which greatly improved its overall exposition. The second author is generously supported by the Early Post.Mobility fellowship No. 165226 of the Swiss National Science Foundation.

## References

Altman, N.S. (1992). “An introduction to kernel and nearest-neighbor nonparametric regression”. In: The American Statistician 46.3, pp. 175–185.

Ban, G.-Y. and C. Rudin (2019). “The big data newsvendor: Practical insights from machine learning”. In: Operations Research 67.1, pp. 90–108.

Ben-Tal, A., D. Den Hertog, A. De Waegenaere, B. Melenberg, and G. Rennen (2013). “Robust solutions of optimization problems affected by uncertain probabilities”. In: Management Science 59.2, pp. 341–357.

Bertsimas, D., V. Gupta, and N. Kallus (2017). “Robust sample average approximation”. In: Mathematical Programming, pp. 1–66.

Bertsimas, D. and N. Kallus (2020). “From predictive to prescriptive analytics”. In: Management Science 66.3, pp. 1025–1044.

Bezanson, J., A. Edelman, S. Karpinski, and V.B. Shah (2017). “Julia: A fresh approach to numerical computing”. In: SIAM Review 59.1, pp. 65–98.

Billingsley, P. (2008). Probability and Measure. John Wiley & Sons.

Breiman, L. (2001). “Random forests”. In: Machine learning 45.1, pp. 5–32.

Csiszár, I. (1984). “Sanov property, generalized I-projection and a conditional limit theorem”. In: The Annals of Probability 12.3, pp. 768–793.

Delage, E. and Y. Ye (2010). “Distributionally robust optimization under moment uncertainty with application to data-driven problems”. In: Operations Research 58.3, pp. 595–612.

Dembo, A. and O. Zeitouni (2009). Large deviations techniques and applications. Vol. 38. Springer Science & Business Media.

Domahidi, A., E. Chu, and S. Boyd (2013). “ECOS: An SOCP solver for embedded systems”. In: European Control Conference (ECC), pp. 3071–3076.

Efron, B. (1982). The Jackknife, the Bootstrap and Other Resampling Plans. SIAM.

Elmachtoub, Adam N and Paul Grigas (2021). “Smart “predict, then optimize””. In: Management Science.

Erdoğan, E. and G. Iyengar (2006). “Ambiguous chance constrained problems and robust optimization”. In: Mathematical Programming 107.1–2, pp. 37–61.

Friedman, J., T. Hastie, and R. Tibshirani (2001). The Elements of Statistical Learning. Vol. 1. Springer Series in Statistics. Springer.

Györfi, L., M. Kohler, A. Krzyzak, and H. Walk (2006). A Distribution-Free Theory of Nonparametric Regression. Springer Science & Business Media.

Hanasusanto, G.A. and D. Kuhn (2013). “Robust data-driven dynamic programming”. In: Advances in Neural Information Processing Systems, pp. 827–835.

Hannah, L., W. Powell, and D.M. Blei (2010). “Nonparametric density estimation for stochastic optimization with an observable state variable”. In: Advances in Neural Information Processing Systems, pp. 820–828.

Kullback, S. and R. A. Leibler (1951). “On information and sufficiency”. In: The Annals of Mathematical Statistics 22.1, pp. 79–86.

Michaud, R. O. (1989). “The Markowitz optimization enigma: Is ‘optimized’ optimal?” In: Financial Analysts Journal 45.1, pp. 31–42.

Mohajerin Esfahani, P. and D. Kuhn (2018). “Data-driven distributionally robust optimization using the Wasserstein metric: Performance guarantees and tractable reformulations”. In: Mathematical Programming 171.1-2, pp. 115–166.

Nadaraya, E.A. (1964). “On estimating regression”. In: Theory of Probability & Its Applications 9.1, pp. 141–142.

Pflug, G. and D. Wozabal (2007). “Ambiguity in portfolio selection”. In: Quantitative Finance 7.4, pp. 435–442.

Popescu, I. (2005). “A semidefinite programming approach to optimal-moment bounds for convex classes of distributions”. In: Mathematics of Operations Research 30.3, pp. 632–657.

Postek, K., D. den Hertog, and B. Melenberg (2016). “Computationally tractable counterparts of distributionally robust constraints on risk measures”. In: SIAM Review 58.4, pp. 603–650.

Sain, S.R. (2002). “Multivariate locally adaptive density estimation”. In: Computational Statistics & Data Analysis 39.2, pp. 165–186.

Sun, H. and H. Xu (2016). “Convergence analysis for distributionally robust optimization and equilibrium problems”. In: Mathematics of Operations Research 41.2, pp. 377–401.

Udell, M., K. Mohan, D. Zeng, J. Hong, S. Diamond, and S. Boyd (2014). “Convex optimization in Julia”. In: SC14 Workshop on High Performance Technical Computing in Dynamic Languages.

Van Parys, B.P.G., P.M. Esfahani, and D. Kuhn (2017). “From data to decisions: Distributionally robust optimization is optimal”. In: ArXiv. url: [https://arxiv.org/abs/1505.05116](https://arxiv.org/abs/1505.05116).

Van Parys, B.P.G., P.J. Goulart, and D. Kuhn (2016). “Generalized Gauss inequalities via semidefinite programming”. In: Mathematical Programming 156.1-2, pp. 271–302.

Walk, H. (2010). “Strong laws of large numbers and nonparametric estimation”. In: Recent Developments in Applied Probability and Statistics. Springer, pp. 183–214.

Wang, Z., P.W. Glynn, and Y. Ye (2016). “Likelihood robust optimization for data-driven newsvendor problems” In: Computational Management Science 12.2, pp. 241–261.

Watson, G.S. (1964). “Smooth regression analysis”. In: Sankhyā: The Indian Journal of Statistics, Series A 26.4, pp. 359–372.

Wiesemann, W., D. Kuhn, and M. Sim (2014). “Distributionally robust convex optimization”. In: Operations Research 62.6, pp. 1358–1376.

Zymler, S., D. Kuhn, and B. Rustem (2013). “Distributionally robust joint chance constraints with second-order moment information”. In: Mathematical Programming 137.1-2, pp. 167–198.

## A Uniform Consistent Estimators

Nadaraya-Watson estimation can be shown to be point-wise consistent when using an appropriately scaled bandwidth parameter $h ( n )$ for any of the smoother functions listed in Figure 4:

Theorem 7 (Walk (2010)). Let us have a loss function satisfying $\mathbb { E } _ { D ^ { \star } } [ | L ( \bar { z } , y ) | \cdot \operatorname* { m a x } \{ \operatorname { l o g } ( | L ( \bar { z } , y ) | ) , 0 \} ] < \infty$ for all z¯. Let the bandwidth $h ( n ) = c n ^ { - \delta }$ for some $c > 0$ and $\delta \in ( 0 , 1 / \mathrm { d i m } ( x ) )$ . Let S be any of the smoother functions listed in Figure $4$ and the weighing function is taken to be $w _ { n } ( x , x _ { 0 } ) = S ( \left\| x - x _ { 0 } \right\| _ { 2 } / h ( n ) )$ . The ${ \mathfrak { e } } n ,$ our estimation formulation $( w i t h ~ k ( n ) = n )$ is asymptotically consistent for any $D ^ { \star } , \; i . e .$ , with probability one we have

$$
\lim _ {n \to \infty} \mathrm{E} _ {D _ {\text {data} [ n ]}} ^ {n} [ L (\bar {z}, y) | x = x _ {0} ] = \mathbb {E} _ {D ^ {\star}} [ L (\bar {z}, y) | x = x _ {0} ] \quad \forall \bar {z}.
$$

Nearest neighbors estimation is also consistent under very mild technical conditions provided that the number of neighbors $k ( n )$ is scaled appropriately with the number of training data samples:

Theorem 8 (Walk (2010)). Assume dist $\begin{array} { r } { \mathrm { i } ( \bar { d }   =   ( \bar { x } , \bar { y } ) , x _ { 0 } )   =   \left\| \bar { x } - x _ { 0 } \right\| _ { 2 } } \end{array}$ and follow the random tie breaking rule discussed in Györfi et al. (2006). Let $k ( n ) = \lceil \operatorname* { m i n } \{ c n ^ { \delta } , n \} \rceil$ for some $c > 0$ and $\delta \in ( 0 , 1 )$ . Then, our estimation formulation (with $w _ { n } ( \bar { x } , x _ { 0 } ) = 1 )$ is asymptotically consistent for any $D ^ { \star }$ , i.e., with probability one we have

$$
\lim _ {n \to \infty} \mathrm{E} _ {D _ {\mathrm{data} [ n ]}} ^ {n} [ L (\bar {z}, y) | x = x _ {0} ] = \mathbb {E} _ {D ^ {*}} [ L (\bar {z}, y) | x = x _ {0} ] \quad \forall \bar {z}.
$$

An estimator is denoted as uniformly consistent if the event

$$
\lim _ {n \to \infty} D ^ {\star \infty} \left[ \max _ {\bar {z}} | \mathrm{E} _ {D _ {\mathrm{data} [ n ]}} ^ {n} [ L (\bar {z}, y) | x = x _ {0} ] - \mathbb {E} _ {D ^ {\star}} [ L (\bar {z}, y) | x = x _ {0} ] | \leq \epsilon \right] = 1\tag{34}
$$

for any $\epsilon > 0$ and $D ^ { \star }$ . That $\mathrm { i s } ,$ the estimator predicts the cost for all potential decisions well to any arbitrary accuracy when only given access to a sufficiently large amount of training data. It is not difficult to see that this uniform consistency in turn implies the consistency of the budget minimization formulation. Indeed, with probability one we have

$$
\boxed {\lim _ {n \to \infty} D ^ {\star \infty} \left[ \min _ {z} \mathbb {E} _ {D ^ {\star}} [ L (z, y) | x = x _ {0} ] + \epsilon \geq \mathrm{E} _ {D _ {\mathrm{data} [ n ]}} ^ {n} [ L (z ^ {\star} (x _ {0}), y) | x = x _ {0} ] \right] = 1}\tag{35}
$$

$$
\mathrm{E} _ {D _ {\mathrm{data} [ n ]}} ^ {n} [ L (z ^ {\star} (x _ {0}), y) | x = x _ {0} ] \geq \mathrm{E} _ {D _ {\mathrm{data} [ n ]}} ^ {n} \big [ L (z _ {\mathrm{data} [ n ]}, y) | x = x _ {0} \big ]\tag{36}
$$

$$
\lim _ {n \to \infty} D ^ {\star \infty} \left[ \mathrm{E} _ {D _ {\mathrm{data} [ n ]}} ^ {n} \big [ L (z _ {\mathrm{data} [ n ]}, y) | x = x _ {0} \big ] \geq \mathbb {E} _ {D ^ {\star}} \big [ L (z _ {\mathrm{data} [ n ]}, y) | x = x _ {0} \big ] - \epsilon \right] = 1\tag{37}
$$

Here, the limit (35) follows from the consistency of the estimator with regards to the full information decision $z ^ { \star } ( x _ { 0 } )$ Inequality (36) is a direct consequence of the characterization of the data-driven decision $z _ { \mathrm { d a t a } [ n ] }$ as a minimizer of $\mathrm { E } _ { D _ { \mathrm { t r } [ n ] } } ^ { n } [ L ( z , y ) | x = x _ { 0 } ]$ . Remarking that maxz¯ $| \mathbb { E } _ { D _ { \mathrm { d a t a } [ n ] } } ^ { n } [ L ( \bar { z } , y ) | x = x _ { 0 } ] - \mathbb { E } _ { D ^ { * } } [ L ( \bar { z } , y ) | x = x _ { 0 } ] | \leq \epsilon \implies$ $\begin{aligned} { \mathbb { E } _ { D _ { \operatorname { d a t a } [ n ] } } ^ { n } \big [ L ( z _ { \operatorname { d a t a } [ n ] } , y ) | x = x _ { 0 } \big ] \geq \mathbb { E } _ { D ^ { * } } \big [ L ( z _ { \operatorname { d a t a } [ n ] } , y ) | x = x _ { 0 } \big ] - \epsilon } \\ \end{aligned}$ the limit (37) follows from the uniform consistency of the estimator stated in Equation (34). Chaining the inequalities in results (35), (36) and (37) implies that

$$
\lim _ {n \to \infty} D ^ {\star \infty} \left[ 0 \leq \mathbb {E} _ {D ^ {\star}} \big [ L (z _ {\text {data} [ n ]}, y) | x = x _ {0} \big ] - \min _ {z} \mathbb {E} _ {D ^ {\star}} [ L (z, y) | x = x _ {0} ] \leq 2 \epsilon \right] = 1.
$$

Here the optimality gap between the cost of the full information decision $z ^ { \star } ( x _ { 0 } )$ and the cost of the data-driven decision $z _ { \mathrm { d a t a } [ n ] }$ is bounded by 2. As this result holds for any arbitrary $\epsilon \; > \; 0$ the data-driven formulation is asymptotically consistent.

## B Proofs

## B.1 Proof of Theorem 1

Proof. First note that the domain of the partial estimators as a function of the distribution D satisfies

$$
\mathrm{dom} \mathrm{E} _ {\mathrm{D}} ^ {\mathrm{n}, \mathrm{j}} [ \mathrm{L} (\mathrm{z}, \mathrm{Y}) | \mathrm{x} = \mathrm{x} _ {0} ] \subseteq \mathcal {D} _ {\mathrm{j}} ^ {\mathrm{n}}.
$$

For a distribution D to be in the domain of the partial estimator the constraints in equation (22) must indeed be feasible. In other words, there must exists some $P$ and $s > 0$ for which $s \cdot D [ \bar { x } , \bar { y } ] = P [ \bar { x } , \bar { y } ]$ for all $( \bar { x } , \bar { y } ) \in \Omega _ { n }$ . The last two constraints in equation (22) then imply that any such $D \in \mathcal { D } _ { n }$ must also be in $\mathcal { D } _ { n } ^ { j }$

Any $D \in \mathcal { D } _ { n , n }$ is the empirical distribution of some bootstrap data set, say bs[n], consisting of n observations from the training data set. Each set $\mathcal { D } _ { n , n } ^ { j }   : =   \mathcal { D } _ { n } ^ { j } \cap \mathcal { D } _ { n , n }$ has a very natural interpretation in terms of $N _ { n } ^ { j } ( x _ { 0 } )$ being the smallest neighborhood containing at least k observations of this associated bootstrap data set bs[n]. Indeed, $D \in \mathcal { D } _ { n , n } ^ { j }$ is in terms of the associated data set equivalent to

$$
\begin{array}{r c l l} k & \leq & \sum_ {(\bar {x}, \bar {y}) \in \mathrm{bs} [ n ]} \mathbb {1} \{(\bar {x}, \bar {y}) \in N _ {n} ^ {j} (x _ {0}) \} & = n \cdot \sum_ {(\bar {x}, \bar {y}) \in N _ {n} ^ {j} (x _ {0})} D [ \bar {x}, \bar {y} ], \\ k & > & \sum_ {(\bar {x}, \bar {y}) \in \mathrm{bs} [ n ]} \mathbb {1} \{(\bar {x}, \bar {y}) \in N _ {n} ^ {j - 1} (x _ {0}) \} & = n \cdot \sum_ {(\bar {x}, \bar {y}) \in N _ {n} ^ {j - 1} (x _ {0})} D [ \bar {x}, \bar {y} ]. \end{array}
$$

The first inequality implies that the neighborhood $N _ { n } ^ { j } ( x _ { 0 } )$ contains at least k observations of the associated data set. Note that the sets $N _ { n } ^ { j } ( x _ { 0 } )$ are increasing with increasing j in terms of set inclusion. The latter inequality hence implies that the biggest smaller neighborhood $N _ { n } ^ { j - 1 } ( x _ { 0 } )$ does not contain k observations. Both conditions taken together thus imply that $N _ { n } ^ { j } ( x _ { 0 } )$ is the smallest neighborhood which contains at least k samples of the bootstrap data set. Any D in $\mathcal { D } _ { n , n }$ is an element in one and only one set $\mathcal { D } _ { n , n } ^ { j }$ as the smallest neighborhood containing at least k samples is uniquely defined for any data set. Formally, $\mathcal { D } _ { n , n } ^ { j } \cap \mathcal { D } _ { n , n } ^ { j ^ { \prime } }   =   \emptyset$ for all $j \neq j ^ { \prime }$ and moreover $\cup _ { j \in [ n ] } \mathcal { D } _ { n , n } ^ { j } = \mathcal { D } _ { n , n }$ . Notice also that the only feasible s in the constraints defining the partial predictors in equation (22) is the particular choice $\textstyle s = 1 / { \sum _ { ( \bar { x } , \bar { y } ) \in N _ { n } ^ { j } ( x _ { 0 } ) } w _ { n } ( \bar { x } , x _ { 0 } ) \cdot P [ \bar { x } , \bar { y } ] } > 0$ . Hence, we must have that for any $D \in \mathcal { D } _ { n , n } ^ { j }$ the partial estimator equates to

$$
\mathrm{E} _ {D} ^ {n, j} \left[ L (\bar {z}, y) | x = x _ {0} \right] = \frac {\sum_ {(\bar {x} , \bar {y}) \in N _ {n} ^ {j} (x _ {0})} L (\bar {z} , \bar {y}) \cdot w _ {n} (\bar {x} , x _ {0}) \cdot D (\bar {x} , \bar {y})}{\sum_ {(\bar {x} , \bar {y}) \in N _ {n} ^ {j} (x _ {0})} w _ {n} (\bar {x} , x _ {0}) \cdot D (\bar {x} , \bar {y})}\tag{\(\forall \bar{z}\}
$$

which is precisely the weighted average over the neighborhood $N _ { n } ^ { j } ( x _ { 0 } )$ . We have hence for all ¯z that

$$
\begin{array}{r l} & {\max _ {j \in [ 1, \dots , n ]} \mathrm{E} _ {D} ^ {n, j} \left[ L (\bar {z}, y) | x = x _ {0} \right] = \left\{ \begin{array}{l l} \frac {\sum_ {(\bar {x} , \bar {y}) \in N _ {n} ^ {1} (x _ {0})} L (\bar {z} , \bar {y}) \cdot w _ {n} (\bar {x} , x _ {0}) \cdot D [ \bar {x} , \bar {y} ]}{\sum_ {(\bar {x} , \bar {y}) \in N _ {n} ^ {1} (x _ {0})} w _ {n} (\bar {x}, x _ {0}) \cdot D [ \bar {x}, \bar {y} ]} & \mathrm{for} \mathrm{D} \in \mathcal {D} _ {\mathrm{n}} ^ {1}, \\ \vdots & \vdots \\ \frac {\sum_ {(\bar {x} , \bar {y}) \in N _ {n} ^ {n} (x _ {0})} L (\bar {z} , \bar {y}) \cdot w _ {n} (\bar {x} , x _ {0}) \cdot D (\bar {x} , \bar {y})}{\sum_ {(\bar {x}, \bar {y}) \in N _ {n} ^ {n} (x _ {0})} w _ {n} (\bar {x}, x _ {0}) \cdot D (\bar {x}, \bar {y})} & \mathrm{for} \mathrm{D} \in \mathcal {D} _ {\mathrm{n}} ^ {\mathrm{n}}. \end{array} \right.} \\ & {\qquad = \mathrm{E} _ {D} ^ {n} [ L (\bar {z}, y) | x = x _ {0} ]} \end{array}
$$

as we have argued that $D \in \mathcal { D } _ { n , n } ^ { j }$ if and only if $N _ { n } ^ { j } ( x _ { 0 } )$ is the smallest neighborhood containing at least k data points. As the empirical distribution D and associated data set bs[n] were chosen arbitrary the result follows.

## B.2 Proof of Proposition 1

Proof. Observe that $\{ D \in \mathcal { D } _ { n } : R ( D , D _ { \operatorname { t r } } ) \leq r \} \cap \mathcal { N } = \emptyset$ by construction. Furthermore, $\{ D \in \mathcal { D } _ { n } : R ( D , D _ { \operatorname { t r } } ) \leq r \}$ is convex as R is convex in its first argument. Without loss of generality, the neighborhood N is convex as well. By the Hahn–Banach separation Theorem an open convex set can be separated linearly from any other disjoint convex set. That is, there must exist a function G and constant $a \in \mathrm { R }$ so that

$$
\mathbb {E} _ {D} [ G (x, y) ] \leq a <   \mathbb {E} _ {D ^ {\prime}} [ G (x, y) ] \quad \forall D \in \{D \in \mathcal {D} _ {n}: R (D, D _ {\mathrm{tr}}) \leq r \}, D ^ {\prime} \in \mathcal {N}.
$$

Hence, int $\mathcal { N } \: = \: \mathcal { N } \: \subseteq \: \mathcal { R } ^ { \prime } \: : = \: \{ D \: \in \: \mathcal { D } _ { n } \: : \: \mathbb { E } _ { D } [ G ( x , y ) ] \: > \: a \: \geq \: \operatorname* { s u p } _ { R ( D ^ { \prime } , D _ { W } ) \leq r } \mathbb { E } _ { D ^ { \prime } } [ G ( x , y ) ] \} \: \subseteq \: \mathcal { R }$ with $\mathcal { R }   =   \{ D   \in$ $\begin{array} { r } { \mathcal { D } _ { n } : \mathrm { E } _ { D } ^ { n } [ L ( z _ { \mathrm { t r } } ^ { \mathrm { r } } ( x _ { 0 } ) , y ) | x = x _ { 0 } ] > \operatorname* { s u p } _ { R ( D ^ { \prime } , D _ { \mathrm { t r } } ) \leq r } \mathrm { E } _ { D ^ { \prime } } ^ { n } [ L ( z _ { \mathrm { t r } } ^ { \mathrm { r } } ( x _ { 0 } ) , y ) | x = x _ { 0 } ] \} } \end{array}$ the disappointment set of a nominal formulation based on the cost estimator $( z , D )   \mapsto   \mathrm { E } _ { D } ^ { n } [ L ( z , y ) | x   =   x _ { 0 } ]   =   \mathrm { E } _ { D } [ G ( x , y ) ]$ . Consequently, following inequality (31) we have

$$
- \inf _ {D ^ {\prime} \in \mathcal {N}} B (D ^ {\prime}, D _ {\mathrm{tr}}) \leq \operatorname * {l i m i n f} _ {n \to \infty} \frac {1}{n} \log D _ {\mathrm{tr}} ^ {\infty} \left[ D _ {\mathrm{bs} [ n ]} \in \mathcal {N} \right] \leq \operatorname * {l i m i n f} _ {n \to \infty} \frac {1}{n} \log D _ {\mathrm{tr}} ^ {\infty} \left[ D _ {\mathrm{bs} [ n ]} \in \mathcal {R} \right]
$$

The stated result hence follows should we have inf $\begin{array} { r } { \underset { D ^ { \prime } \in \mathcal { N } } { \mathrm { ~ } } B ( D ^ { \prime } , D _ { \mathrm { t r } } ) < r . } \end{array}$ As $\mathcal { N }$ is an open set there exists $\lambda \in (0,1)$ so that $D ( \lambda )   =   \lambda D   +   ( 1   -   \lambda ) D _ { \mathrm { t r } [ n ] }   \in   \mathcal { N }$ . From convexity of B we have $B ( D ( \lambda ) , D _ { \mathrm { t r } } )   \leq   \lambda B ( D , D _ { \mathrm { t r } [ n ] } )   +   ( 1   -$ $\lambda ) B ( D _ { \mathrm { t r } } , D _ { \mathrm { t r } } )   <   r$ for any $\lambda   \in   (0,1)$ using that $B ( D , D _ { \mathrm { t r } } )   =   r$ and $B ( D _ { \mathrm { t r } } , D _ { \mathrm { t r } } )   =   0$ . Hence, indeed we have inf $\begin{aligned} { \begin{array} { l } { \displaystyle { \left[ { { D } } ^ { \prime } \in \mathcal { N } \right. } { B } ( { { D } } ^ { \prime } , { { D } } _ { \operatorname { t r } } ) \leq { B } ( { { D } } ( \lambda ) , { { D } } _ { \operatorname { t r } } ) < r } \\ \end{array} } \\ \end{aligned}$ □

## B.3 Proof of Corollary 1

Proof. Remark that from the definition of the Nadaraya-Watson cost estimate

$$
\mathrm{E} _ {D _ {\mathrm{tr} [ n ]}} ^ {n} [ L (z, y) | x = x _ {0} ] := \mathbb {E} _ {D _ {\mathrm{tr} [ n ]}} [ L (z, y) \cdot w _ {n} (x, x _ {0}) ] / \mathbb {E} _ {D _ {\mathrm{tr} [ n ]}} [ w _ {n} (x, x _ {0}) ]
$$

given in (19) it follows that we have

$$
\begin{array}{l l} \mathrm{E} _ {D _ {\mathrm{tr} [ n ]}} ^ {n} [ L (z, y) | x = x _ {0} ] := \max _ {s > 0, P} & \sum_ {(\bar {x}, \bar {y}) \in \Omega_ {n}} w _ {n} (\bar {x}, x _ {0}) \cdot L (z, \bar {y}) \cdot P [ \bar {x}, \bar {y} ] \\ \text {s.t.} & P [ \bar {x}, \bar {y} ] = D [ \bar {x}, \bar {y} ] \cdot s \quad \forall (\bar {x}, \bar {y}) \in \Omega_ {n}, \\ & \sum_ {(\bar {x}, \bar {y}) \in \Omega_ {n}} P [ \bar {x}, \bar {y} ] = s, \sum_ {(\bar {x}, \bar {y}) \in \Omega_ {n}} w _ {n} (\bar {x}, x _ {0}) \cdot P [ \bar {x}, \bar {y} ] = 1. \end{array}
$$

Indeed, the only feasible s is such that $\begin{array} { r } { s   =   1 / { \sum _ { ( \bar { x } , \bar { y } ) \in \Omega _ { n } } w _ { n } ( \bar { x } , x _ { 0 } ) \cdot P [ \bar { x } , \bar { y } ] } } \end{array}$ . Hence, the only feasible $P$ is $P =$ $\textstyle D / { \sum _ { ( \bar { x } , \bar { y } ) \in \Omega _ { n } } w _ { n } ( \bar { x } , x _ { 0 } ) \cdot P [ \bar { x } , \bar { y } ] }$ and the equivalence follows. The chain of equalities

$$
\begin{array}{r l} \big \{(s, P) : \exists D \text {s.t.} s \cdot D = P, R (D, D _ {\mathrm{tr} [ n ]}) \leq r \big \} & = \big \{(s, P) : R (P / s, D _ {\mathrm{tr} [ n ]}) \leq r \big \} \\ & = \big \{(s, P) : s \cdot R (P / s, D _ {\mathrm{tr} [ n ]}) \leq s \cdot r \big \} \end{array}
$$

imply that the robust budget function $c _ { n } ( z , D _ { \mathrm { t r } [ n ] } , x _ { 0 } )$ corresponds exactly to the optimization formulation claimed in the corollary. □

## B.4 Proof of Theorem 3

Proof. We first show the uniform convergence of the robust budget function to its nominal counterpart when the loss function $L ( \bar { z } , \bar { y } ) < \bar { L } < \infty$ is bounded. Let us first consider a given training data set $\operatorname { t r } [ n ]$ . Note that because of its definition as robust counterpart of our estimator, we have that our robust budget can be bounded as

$$
\mathrm{E} _ {D _ {\mathrm{tr} [ n ]}} ^ {n} [ L (\bar {z}, y) | x = x _ {0} ] \leq c _ {n} (\bar {z}, D _ {\mathrm{tr} [ n ]}, x _ {0}) \leq \mathrm{E} _ {D _ {\mathrm{wc} [ n ]}} ^ {n} [ L (\bar {z}, y) | x = x _ {0} ] + \alpha
$$

for some worst-case distributions $D _ { \mathrm { w c } [ n ] }$ at distance at most $B ( D _ { \mathrm { w c } [ n ] } , D _ { \mathrm { t r } [ n ] } ) \: \leq \: r ( n )$ from the training distribution for any arbitrary $\alpha   >   0$ In terms of the total variation distance, we have that $\left\| D _ { \mathrm { w c } [ n ] } - D _ { \mathrm { t r } [ n ] } \right\| _ { 1 } \leq$ $\sqrt { B ( D _ { \operatorname { w c } [ n ] } , D _ { \operatorname { t r } [ n ] } ) / 2 } \leq \sqrt { r ( n ) / 2 }$ following Pinkser’s inequality.

The Nadaraya-Watson estimate based on the worst-case distribution is the fraction

$$
\mathrm{E} _ {D _ {\mathrm{wc} [ n ]}} ^ {n} [ L (\bar {z}, y) | x = x _ {0} ] := \frac {\sum_ {(\bar {x} , \bar {y}) \in \Omega_ {n}} L (\bar {z} , \bar {y}) \cdot w _ {n} (\bar {x} , x _ {0}) \cdot D _ {\mathrm{wc} [ n ]} [ \bar {x} , \bar {y} ] / h (n) ^ {d}}{\sum_ {(\bar {x} , \bar {y}) \in \Omega_ {n}} w _ {n} (\bar {x} , x _ {0}) \cdot D _ {\mathrm{wc} [ n ]} [ \bar {x} , \bar {y} ] / h (n) ^ {d}}
$$

where we denote here $d = \dim ( x )$ for conciseness. We have that the denominator of the Nadaraya-Watson estimator is lower bounded by

$$
\begin{array}{r l} & {\sum_ {(\bar {x}, \bar {y}) \in \Omega_ {n}} w _ {n} (\bar {x}, x _ {0}) / h (n) ^ {d} D _ {\mathrm{wc} [ n ]} [ \bar {x}, \bar {y} ]} \\ & {= \sum_ {(\bar {x}, \bar {y}) \in \Omega_ {n}} w _ {n} (\bar {x}, x _ {0}) / h (n) ^ {d} D _ {\mathrm{tr} [ n ]} [ \bar {x}, \bar {y} ] + \sum_ {(\bar {x}, \bar {y}) \in \Omega_ {n}} w _ {n} (\bar {x}, x _ {0}) / h (n) ^ {d} \left(D _ {\mathrm{wc} [ n ]} [ \bar {x}, \bar {y} ] - D _ {\mathrm{tr} [ n ]} [ \bar {x}, \bar {y} ]\right)} \\ & {\geq \sum_ {(\bar {x}, \bar {y}) \in \Omega_ {n}} w _ {n} (\bar {x}, x _ {0}) / h (n) ^ {d} D _ {\mathrm{tr} [ n ]} [ \bar {x}, \bar {y} ] - \left(\max _ {(\bar {x}, \bar {y}) \in \Omega_ {n}} w _ {n} (\bar {x}, x _ {0})\right) \sqrt {r (n) / 2} / h (n) ^ {d}} \\ & {\geq \sum_ {(\bar {x}, \bar {y}) \in \Omega_ {n}} w _ {n} (\bar {x}, x _ {0}) / h (n) ^ {d} D _ {\mathrm{tr} [ n ]} [ \bar {x}, \bar {y} ] - \sqrt {r (n) / 2} / h (n) ^ {d}} \end{array}
$$

Here the first inequality follows from the Cauchy-Schwartz inequality $\left| a ^ { \top } b \right| \leq \left\| a \right\| _ { \infty } \cdot \left\| b \right\| _ { 1 }$ . Notice that here the weights $0   \leq   w _ { n } ( \bar { x } , x _ { 0 } )   \leq   w _ { n } ( x _ { 0 } , x _ { 0 } )   \leq   1$ are all non-negative and bounded from above by one for all smoother functions in Figure 4. Lemma 6 in Walk (2010) establishes that the limit

$$
\operatorname * {l i m i n f} _ {n \to \infty} \sum_ {(\bar {x}, \bar {y}) \in \Omega_ {n}} w _ {n} (\bar {x}, x _ {0}) / h (n) ^ {d} D _ {\mathrm{data}[ n ]} [ \bar {x}, \bar {y} ] = 2 d (x _ {0}) > 0
$$

is positive with probability one. Taken together with the premise lim $\scriptstyle { \frac { 1 } { 1 - n \to \infty } } { \sqrt { r ( n ) } } / h ( n ) ^ { d } = 0$ this establishes the existence of a large enough sample size $n _ { 0 }$ such that for all $n \geq n _ { 0 }$ the denominator of the Nadaraya-Watson estimator satisfies $\begin{array} { r } { \sum _ { ( \bar { x } , \bar { y } ) \in \Omega _ { n } } w _ { n } ( \bar { x } , x _ { 0 } ) / h ( n ) ^ { d } D _ { \operatorname { w c } [ n ] } [ \bar { x } , \bar { y } ] \mathop { \geq } d ( x _ { 0 } ) } \\ \end{array}$ and $\begin{array} { l l } { \sum _ { ( \bar { x } , \bar { y } ) \in \Omega _ { n } } w _ { n } ( \bar { x } , x _ { 0 } ) / h ( n ) ^ { d } D _ { \operatorname { t r } [ n ] } [ \bar { x } , \bar { y } ] \geq 2 \sqrt { r ( n ) / 2 } / h ( n ) ^ { d } } \\ \end{array}$ Similarly, the nominator of the Nadaraya-Watson estimator satisfies

$$
\begin{array}{r l} & {\sum_ {(\bar {x}, \bar {y}) \in \Omega_ {n}} L (\bar {z}, \bar {y}) \cdot w _ {n} (\bar {x}, x _ {0}) \cdot D _ {\mathrm{wc} [ n ]} [ \bar {x}, \bar {y} ] / h (n) ^ {d}} \\ {\leq} & {\sum_ {(\bar {x}, \bar {y}) \in \Omega_ {n}} L (\bar {z}, \bar {y}) \cdot w _ {n} (\bar {x}, x _ {0}) \cdot D _ {\mathrm{tr} [ n ]} [ \bar {x}, \bar {y} ] / h (n) ^ {d} + \sqrt {r (n) / 2} / h (n) ^ {d}.} \end{array}
$$

In what follows we will use the inequality $a / ( b - x ) \leq a / b + 2 a / b \cdot x$ for all $x \leq b / 2$ when $a , b > 0$ . This inequality follows trivially from the definition of convexity of the function $a / ( b - x )$ for all $x \leq b$ when $a , b > 0$ . Using the previous inequalities we can establish when $n \geq n _ { 0 }$ the following claims

$$
\begin{array}{l} \mathrm{E} _ {D _ {\mathrm{wc} [ n ]}} ^ {n} [ L (\bar {z}, y) | x = x _ {0} ] \\ \leq \frac {\sum_ {(\bar {x} , \bar {y}) \in \Omega_ {n}} L (\bar {z} , \bar {y}) \cdot w _ {n} (\bar {x} , x _ {0}) \cdot D _ {\mathrm{tr} [ n ]} [ \bar {x} , \bar {y} ] / h (n) ^ {d}}{\sum_ {(\bar {x} , \bar {y}) \in \Omega_ {n}} w _ {n} (\bar {x} , x _ {0}) \cdot D _ {\mathrm{wc} [ n ]} [ \bar {x} , \bar {y} ] / h (n) ^ {d}} + \frac {\sqrt {r (n) / 2}}{h (n) ^ {d} d (x _ {0})} \\ \leq \frac {\sum_ {(\bar {x} , \bar {y}) \in \Omega_ {n}} L (\bar {z} , \bar {y}) \cdot w _ {n} (\bar {x} , x _ {0}) \cdot D _ {\mathrm{tr} [ n ]} [ \bar {x} , \bar {y} ] / h (n) ^ {d}}{\sum_ {(\bar {x} , \bar {y}) \in \Omega_ {n}} w _ {n} (\bar {x} , x _ {0}) \cdot D _ {\mathrm{tr} [ n ]} [ \bar {x} , \bar {y} ] / h (n) ^ {d} - \sqrt {r (n) / 2} / h (n) ^ {d}} + \frac {\sqrt {r (n) / 2}}{h (n) ^ {d} d (x _ {0})} \\ \leq \mathrm{E} _ {D _ {\mathrm{tr} [ n ]}} ^ {n} [ L (\bar {z}, y) | x = x _ {0} ] + 2 \mathrm{E} _ {D _ {\mathrm{tr} [ n ]}} ^ {n} [ L (\bar {z}, y) | x = x _ {0} ] \sqrt {r (n) / 2} / h (n) ^ {d} + \frac {\sqrt {r (n) / 2}}{h (n) ^ {d} d (x _ {0})} \\ \leq \mathrm{E} _ {D _ {\mathrm{tr} [ n ]}} ^ {n} [ L (\bar {z}, y) | x = x _ {0} ] + (2 \bar {L} + 1 / d (x _ {0})) \sqrt {r (n) / 2} / h (n) ^ {d}. \end{array}
$$

The nominal Nadaraya-Watson estimator is uniformly consistent, i.e.,

$$
| \mathrm{E} _ {D _ {\text {data} [ n ]}} ^ {n} [ L (\bar {z}, y) | x = x _ {0} ] - \mathbb {E} _ {D ^ {*}} [ L (\bar {z}, y) | x = x _ {0} ] | \leq \epsilon (n)
$$

for $\begin{array} { r } { \operatorname* { l i m } _ { n \to \infty } \epsilon ( n ) = 0 } \end{array}$ as discussed before. It hence trivially follows that the robust Nadaraya-Watson estimator is uniformly consistent as well. Indeed, from the previous inequality it follows that

$$
| c _ {n} (\bar {z}, D _ {\mathrm{data} [ n ]}, x _ {0}) - \mathbb {E} _ {D ^ {*}} [ L (\bar {z}, y) | x = x _ {0} ] | \leq \epsilon (n) + (2 \bar {L} + 1 / d (x _ {0})) \sqrt {r (n) / 2} / h (n) ^ {d} + \alpha
$$

with probability one for all ¯z. This inequality holds for any arbitrary $\alpha > 0$ . Uniform consistency then directly implies here an asymptotically diminishing optimality gap

$$
\mathbb {E} _ {D ^ {*}} \left[ L \left(z _ {\text {data} [ n ]} ^ {r}, y\right) \mid x = x _ {0} \right] - \min _ {z} \mathbb {E} _ {D ^ {*}} \left[ L (\bar {z}, y) \mid x = x _ {0} \right] \leq 2 \epsilon (n) + \left(4 \bar {L} + 2 / d \left(x _ {0}\right)\right) \sqrt {r (n) / 2} / h (n) ^ {d}.
$$

Using that lim $\scriptstyle { \cdot } n \to \infty \; { \sqrt { r ( n ) } } / h ( n ) ^ { d }$ yields the wanted result immediately.

□

## B.5 Proof of Theorem 4

Proof. We show the uniform convergence of the robust budget function to the unknown cost, that is, and any bounded function $L ( \bar { z } , \bar { y } ) < \bar { L } < \infty$ for all ¯z and ȳ. Let us first consider a given training data set $\operatorname { t r } [ n ]$ without ties. That is, we have that $\left| N _ { n } ^ { j } ( x _ { 0 } ) \right| = j$ for all $j \in [ n ]$ . Note that because of its definition as robust counterpart of the estimator $\mathrm { E } _ { D _ { \mathrm { t r } [ n ] } } ^ { n } [ L ( \bar { z } , y ) | x = x _ { 0 } ]$ , we have that the robust cost can be bounded as

$$
\mathrm{E} _ {D _ {\mathrm{tr} [ n ]}} ^ {n} [ L (\bar {z}, y) | x = x _ {0} ] \leq c _ {n} (z _ {\mathrm{tr} [ n ]} ^ {r}, D _ {\mathrm{tr} [ n ]}, x _ {0}) \leq \mathrm{E} _ {D _ {\mathrm{wc} [ n ]}} ^ {j ^ {\star}} [ L (\bar {z}, y) | x = x _ {0} ] + \alpha
$$

for some worst-case distributions $D _ { \mathrm { w c } [ n ] } \: \in \: \mathcal { D } _ { n } ^ { j \star }$ at distance at most $B ( D _ { \mathrm { w c } [ n ] } , D _ { \mathrm { t r } [ n ] } )   \leq   r ( n )$ from the training distribution for any arbitrary $\alpha > 0$ . In terms of the total variation distance, we have that $\left\| D _ { \mathrm { w c } [ n ] } - D _ { \mathrm { t r } [ n ] } \right\| _ { 1 } \leq$ $\sqrt { B ( D _ { \operatorname { w c } [ n ] } , D _ { \operatorname { t r } [ n ] } ) / 2 } \; \leq \; \sqrt { r ( n ) / 2 }$ following Pinkser’s inequality. The nearest-neighbors estimate based on the worst-case distribution is defined as the fraction

$$
\mathrm{E} _ {D _ {\mathrm{wc} [ n ]}} ^ {n} [ L (\bar {z}, y) | x = x _ {0} ] := \frac {\sum_ {(\bar {x} , \bar {y}) \in N _ {n} ^ {j ^ {\star}} (x _ {0})} L (\bar {z} , \bar {y}) \cdot D _ {\mathrm{wc} [ n ]} [ \bar {x} , \bar {y} ]}{\sum_ {(\bar {x} , \bar {y}) \in N _ {n} ^ {j ^ {\star}} (x _ {0})} D _ {\mathrm{wc} [ n ]} [ \bar {x} , \bar {y} ]}.
$$

The neighborhood parameter $j ^ { \star }$ satisfies by definition $\textstyle \sum _ { ( \bar { x } , \bar { y } ) \in N _ { n } ^ { j \star } ( x _ { 0 } ) } D _ { \operatorname { w c } [ n ] } [ \bar { x } , \bar { y } ] \geq k ( n ) / n$ . The previous inequality bounds the denominator from below by $k ( n ) / n$ . Using the Cauchy-Schwartz inequality $\left| a ^ { \top } b \right| \leq \left\| a \right\| _ { \infty } \cdot \left\| b \right\|$ as well as the Pinkser inequality, the nominator of the Nadaraya-Watson estimator satisfies

$$
\begin{array}{r l} & \sum_ {(\bar {x}, \bar {y}) \in N _ {n} ^ {j ^ {\star}} (x _ {0})} L (\bar {z}, \bar {y}) \cdot D _ {\mathrm{wc} [ n ]} [ \bar {x}, \bar {y} ] \\ \leq & \sum_ {(\bar {x}, \bar {y}) \in N _ {n} ^ {j ^ {\star}} (x _ {0})} L (\bar {z}, \bar {y}) \cdot D _ {\mathrm{tr} [ n ]} [ \bar {x}, \bar {y} ] + \bar {L} \sqrt {r (n) / 2}. \end{array}
$$

We also have that from the definition of the total variation distance that $\| D _ { \operatorname { t r } [ n ] } - D _ { \operatorname { w c } [ n ] } \| _ { 1 } { \geq } D _ { \operatorname { t r } [ n ] } [ N _ { n } ^ { j \star } ( x _ { 0 } ) ] -$ $D _ { \mathrm { w c } [ n ] } [ N _ { n } ^ { j \star } ( x _ { 0 } ) ]   \geq   ( j ^ { \star } - k ( n ) ) / n$ . We have also $\| D _ { \operatorname { w c } [ n ] } - D _ { \operatorname { t r } [ n ] } \| _ { 1 } \: \geq \: D _ { \operatorname { w c } [ n ] } [ N _ { n } ^ { j \star - 1 } ( x _ { 0 } ) ] - D _ { \operatorname { t r } [ n ] } [ N _ { n } ^ { j \star - 1 } ( x _ { 0 } ) ] \: \geq \:$ $( k ( n ) - j ^ { \star } ) / n$ . Last two inequalities imply that we can use the bound $\sqrt { r ( n ) / 2 } \geq \| D _ { \operatorname { t r } [ n ] } { - } D _ { \operatorname { w c } [ n ] } \| _ { 1 } \geq \left| k ( n ) - j ^ { \star } \right| / n$ By applying first the Cauchy-Schwartz inequality again and then the previously obtained bounds we can obtain

$$
\sum_ {(\bar {x}, \bar {y}) \in N _ {n} ^ {j ^ {\star}} (x _ {0})} L (\bar {z}, \bar {y}) D _ {\mathrm{tr} [ n ]} [ \bar {x}, \bar {y} ]
$$

$$
\leq \sum_ {(\bar {x}, \bar {y}) \in N _ {n} ^ {k (n)} (x _ {0})} L (\bar {z}, \bar {y}) D _ {\mathrm{tr} [ n ]} [ \bar {x}, \bar {y} ] + \bar {L} | D _ {\mathrm{tr} [ n ]} \{N _ {n} ^ {j \star} (x _ {0}) ] - D _ {\mathrm{tr} [ n ]} [ N _ {n} ^ {k (n)} (x _ {0}) ] |
$$

$$
\leq \sum_ {(\bar {x}, \bar {y}) \in N _ {n} ^ {k (n)} (x _ {0})} L (\bar {z}, \bar {y}) D _ {\mathrm{tr} [ n ]} [ \bar {x}, \bar {y} ] + \bar {L} | j ^ {\star} - k (n) | / n
$$

$$
\leq \sum_ {(\bar {x}, \bar {y}) \in N _ {n} ^ {k (n)} (x _ {0})} L (\bar {z}, \bar {y}) D _ {\mathrm{tr} [ n ]} [ \bar {x}, \bar {y} ] + \bar {L} \sqrt {r (n) / 2}.
$$

Hence,

$$
\mathrm{E} _ {D _ {\mathrm{tr} [ n ]}} ^ {n} [ L (\bar {z}, y) | x = x _ {0} ] \leq c _ {n} (\bar {z}, D _ {\mathrm{tr} [ n ]}, x _ {0}) \leq \mathrm{E} _ {D _ {\mathrm{tr} [ n ]}} ^ {n} [ L (\bar {z}, y) | x = x _ {0} ] + \frac {2 \bar {L} n \sqrt {r (n) / 2}}{k (n)} + \alpha\tag{38}
$$

for any arbitrary training data set without ties. Ties among data points when using the random tie breaking method are a probability zero event which we may ignore. We already know that the nearest neighbors estimator is uniformly consistent. That is, we have that $| \mathrm { E } _ { D _ { \mathrm { d a t a } [ n ] } } ^ { n } [ L ( \bar { z } , y ) | x = x _ { 0 } ] - \mathbb { E } _ { D ^ { \star } } [ L ( \bar { z } , y ) | x = x _ { 0 } ]   | \leq \epsilon ( n )$ with probability one and $\begin{array} { r } { \operatorname* { l i m } _ { n \to \infty } \epsilon ( n ) = 0 } \end{array}$ . When the robustness radius does shrinks at an appropriate rate, i.e., its size compared to the bandwidth parameter is negligible $\left( \operatorname* { l i m } _ { n \to \infty } n { \sqrt { r ( n ) } } / k ( n ) = 0 \right)$ , then uniform consistency of budget estimator $c _ { n }$ follows by taking the limit for n tends to infinity for the chain of inequalities in (38) applied to $D _ { \mathrm { d a t a } [ n ] }$ and observing that $\alpha > 0$ is arbitrarily small. Uniform consistency of the nearest-neighbors formulation follows by the exact same argument as given in proof of Theorem 3 in case of the Nadaraya-Watson formulation. □

## B.6 Proof of Corollary 2

Proof. Let us fix a training data set with empirical training distribution $D _ { \mathrm { t r } [ n ] }$ and a given decision z. Let $\bar { c } _ { n } : =$ $\mathrm { E } _ { D _ { \mathrm { t r } [ n ] } } ^ { n } [ L ( \bar { z } , y ) | x = x _ { 0 } ]$ be the budgeted cost based on the training data with $k ( n )   =   n$ . In order to prove the theorem, it suffices to characterize the probability of the event that the empirical distribution $D _ { \mathrm { b s } [ n ] }$ of random bootstrap data resampled from the training data realizes in the set

$$
\mathcal {C} := \left\{D \in \mathcal {D} _ {n}: \begin{array}{l l} & \exists s > 0, s \cdot \sum_ {(\bar {x}, \bar {y}) \in \Omega_ {n}} w _ {n} (\bar {x}, x _ {0}) \cdot L (\bar {z}, y) \cdot D (\bar {x}, \bar {y}) > \bar {c} _ {n}, \\ & s \cdot \sum_ {(\bar {x}, \bar {y}) \in \Omega_ {n}} w _ {n} (\bar {x}, x _ {0}) \cdot D (\bar {x}, \bar {y}) = 1 \end{array} \right\}
$$

as follows from Corollary 1. After eliminating the auxiliary variable s we arrive at the description $\mathcal { C } = \{ D \in \mathcal { D } _ { n }$ $\textstyle \sum _ { ( \bar { x } , \bar { y } ) \in \Omega _ { n } } w _ { n } ( \bar { x } , x _ { 0 } ) \cdot L ( \bar { z } , y ) \cdot D ( \bar { x } , \bar { y } ) > \bar { c } _ { n } \cdot \sum _ { ( \bar { x } , \bar { y } ) \in \Omega _ { n } } w _ { n } ( \bar { x } , x _ { 0 } ) \cdot D ( \bar { x } , \bar { y } ) \}$ . The set C is a convex polyhedron. The robust budget cost ${ \bar { c } } _ { n }$ is constructed to ensure that in $\mathrm { f } _ { D \in \mathcal { C } } R ( D , D _ { \mathrm { t r } [ n ] } )   >   r$ . Indeed, we have the rather direct implication $\bar { D } \in \mathcal { C } \implies \operatorname { E } _ { \bar { D } } ^ { n } [ L ( \bar { z } , y ) | x = x _ { 0 } ] > \bar { c } _ { n } = \operatorname* { s u p } \left\{ \operatorname { E } _ { D } ^ { n } [ L ( \bar { z } , y ) | x = x _ { 0 } ] \mid R ( D , D _ { \operatorname { t r } [ n ] } ) \leq r \right\}$ which in turn itself implies $R ( \bar { D } , D _ { \mathrm { t r } [ n ] } ) > r$ . Hence, the result follows from the bootstrap inequality (28) applied to the probability $D _ { \mathrm { t r } [ n ] } ^ { \infty } ( D _ { \mathrm { b s } [ n ] } \in \mathcal { C } )$ as in this particular case the employed distribution distance function $( R = B )$ coincides with the bootstrap distance function. □

## B.7 Proof Lemma 1

Proof. We will employ standard Lagrangian duality on the convex optimization characterization (25) of the partial nearest neighbors cost function associated $c _ { n } ^ { j } ( \bar { z } , D , x _ { 0 } )$ . The Lagrangian function associated with the primal optimization problem in (25) is denoted here at the function

$$
\begin{array}{l} \mathcal {L} (P, s; \alpha , \beta , \eta , \nu) := \\ \sum_ {(\bar {x}, \bar {y}) \in N _ {n} ^ {j} (x _ {0})} w _ {n} (\bar {x}, x _ {0}) \cdot L (z, \bar {y}) \cdot P [ x, y ] + \left(1 - \sum_ {(\bar {x}, \bar {y}) \in N _ {n} ^ {j - 1} (x _ {0})} w _ {n} (\bar {x}, x _ {0}) \cdot P [ \bar {x}, \bar {y} ]\right) \alpha \\ + \left(\sum_ {(\bar {x}, \bar {y}) \in N _ {n} ^ {j} (x _ {0})} P [ \bar {x}, \bar {y} ] - \frac {k}{n} \cdot s\right) \eta_ {1} + \left(\frac {k - 1}{n} \cdot s - \sum_ {(\bar {x}, \bar {y}) \in N _ {n} ^ {j - 1} (x _ {0})} P [ \bar {x}, \bar {y} ]\right) \eta_ {2} \\ + \left(\sum_ {(\bar {x}, \bar {y}) \in \Omega_ {n}} P [ \bar {x}, \bar {y} ] - s\right) \beta + \left(r \cdot s - \sum_ {(\bar {x}, \bar {y}) \in \Omega_ {n}} P [ \bar {x}, \bar {y} ] \log \left(\frac {P [ \bar {x} , \bar {y} ]}{s \cdot D [ \bar {x} , \bar {y} ]}\right)\right) \nu \end{array}
$$

where P and s are the primal variables of the primal optimization problem (25) and $\alpha , \beta , \eta$ and ν the dual variables associated with each of its constraints. Collecting the relevant terms in the Lagrangian function results

in $\mathcal { L } ( P , s ; \alpha , \beta , \nu ) =$

$$
\begin{array}{l} \mathcal {L} (1, s, \alpha , \beta , \nu) = \\ \alpha + s (r \nu - \beta - \frac {k}{n} (\eta_ {1} - \eta_ {2}) - \frac {\eta_ {2}}{n}) \\ \quad + \sum_ {(\bar {x}, \bar {y}) \in N _ {n} ^ {j - 1} (x _ {0})} \left[ P [ \bar {x}, \bar {y} ] ((L (z, y) - \alpha) \cdot w _ {n} (\bar {x}, x _ {0}) + \beta + \eta_ {1} - \eta_ {2}) - \nu P [ \bar {x}, \bar {y} ] \log \left(\frac {P [ \bar {x} , \bar {y} ]}{s \cdot D [ \bar {x} , \bar {y} ]}\right) \right] \\ \quad + \sum_ {(\bar {x}, \bar {y}) \in N _ {n} ^ {j} (x _ {0}) \setminus N _ {n} ^ {j - 1} (x _ {0})} \left[ P [ \bar {x}, \bar {y} ] ((L (z, y) - \alpha) \cdot w _ {n} (\bar {x}, x _ {0}) + \beta + \eta_ {1}) - \nu P [ \bar {x}, \bar {y} ] \log \left(\frac {P [ \bar {x} , \bar {y} ]}{s \cdot D [ \bar {x} , \bar {y} ]}\right) \right] \\ \quad + \sum_ {(\bar {x}, \bar {y}) \in \Omega_ {n} \setminus \mathbb {N} _ {n} ^ {j} (x _ {0})} \left[ P [ \bar {x}, \bar {y} ] \beta - \nu P [ \bar {x}, \bar {y} ] \log \left(\frac {P [ \bar {x} , \bar {y} ]}{s \cdot D [ \bar {x} , \bar {y} ]}\right) \right] \end{array}
$$

The dual function of the primal optimization problem (25) is identified with the concave function $g ( \alpha , \beta , \eta , \nu ) : =$ inf $_ { P \geq 0 , \: s > 0 } \: \mathcal { L } ( P , s ; \alpha , \beta , \nu )$ . Using the same manipulations as presented in the proof of Lemma 2 we can express the dual function as $g ( \alpha , \beta , \eta , \nu ) =$

$$
\begin{array}{r l} & = \sup _ {s > 0} \alpha + s (r \nu - \beta - \frac {k}{n} (\eta_ {1} - \eta_ {2}) - \frac {\eta_ {2}}{n}) + s \nu \sum_ {(\bar {x}, \bar {y}) \in \Omega_ {n} \setminus N _ {n} ^ {j} (x _ {0})} D [ \bar {x}, \bar {y} ] \exp \left(\frac {\beta}{\nu} - 1\right) \\ & \qquad + s \nu \sum_ {(\bar {x}, \bar {y}) \in N _ {n} ^ {j - 1} (x _ {0})} D [ \bar {x}, \bar {y} ] \exp \left(\frac {(L (z , \bar {y}) - \alpha) \cdot w _ {n} (\bar {x} , x _ {0}) + \beta + \eta_ {1} - \eta_ {2}}{\nu} - 1\right) \\ & \qquad + s \nu \sum_ {(\bar {x}, \bar {y}) \in N _ {n} ^ {j} (x _ {0}) \setminus N _ {n} ^ {j - 1} (x _ {0})} D [ \bar {x}, \bar {y} ] \exp \left(\frac {(L (z , \bar {y}) - \alpha) \cdot w _ {n} (\bar {x} , x _ {0}) + \beta + \eta_ {1}}{\nu} - 1\right). \end{array}
$$

Our dual function can be expressed alternatively as

$$
\begin{array}{r l} g (\alpha , \beta , \eta , \nu) = \Big \{\alpha : r \cdot \nu - \frac {k}{n} (\eta_ {1} - \eta_ {2}) - \frac {\eta_ {2}}{n} + \nu \sum_ {(\bar {x}, \bar {y}) \in \Omega_ {n} \setminus N _ {n} ^ {j} (x _ {0})} D [ \bar {x}, \bar {y} ] \exp \Big (\frac {\beta}{\nu} - 1 \Big) \\ & \quad + \nu \sum_ {(\bar {x}, \bar {y}) \in N _ {n} ^ {j - 1} (x _ {0})} D [ \bar {x}, \bar {y} ] \exp \Big (\frac {(L (z , \bar {y}) - \alpha) \cdot w _ {n} (\bar {x} , x _ {0}) + \beta + \eta_ {1} - \eta_ {2}}{\nu} - 1 \Big) \\ & \quad + \nu \sum_ {(\bar {x}, \bar {y}) \in N _ {n} ^ {j} (x _ {0}) \setminus N _ {n} ^ {j - 1} (x _ {0})} D [ \bar {x}, \bar {y} ] \exp \Big (\frac {(L (z , \bar {y}) - \alpha) \cdot w _ {n} (\bar {x} , x _ {0}) + \beta + \eta_ {1}}{\nu} - 1 \Big) \leq \beta \Big \}. \end{array}
$$

The dual optimization problem of the primal problem (25) is now found as $\operatorname* { i n f } _ { \alpha , \beta , \nu \geq 0 } \: g ( \alpha , \beta , \nu )$ . As the primal optimization problem in (25) is convex, strong duality holds under Slater’s condition which is satisfied whenever $r   >   r _ { n } ^ { j }$ . Using first-order optimality conditions, the optimal $\beta ^ { \star }$ must satisfy the relationship $\beta ^ { \star }   =   - \nu +$ $\nu \operatorname { l o g } ( \textstyle \sum _ { ( \bar { x } , \bar { y } ) \in N _ { \kappa } ^ { l - 1 } ( x _ { 0 } } D [ \bar { x } , \bar { y } ] \operatorname { e x p } ( [ ( L ( z , \bar { y } ) - \alpha ) \cdot w _ { n } ( \bar { x } , x _ { 0 } ) + \eta _ { 1 } - \eta _ { 2 } ] / \nu ) + \textstyle \sum _ { ( \bar { x } , \bar { y } ) \in N _ { \kappa } ^ { l } ( x _ { 0 } ) \setminus N _ { \kappa } ^ { l - 1 } ( x _ { 0 } ) } D [ \bar { x } , \bar { y } ] \operatorname { e x p } ( [ ( L ( z , \bar { y } ) - \alpha ) \cdot w _ { n } ( \bar { x } , x _ { 0 } ) + \eta _ { 1 } - \eta _ { 2 } ] / \nu ) ) )$ $\alpha ) \cdot w _ { n } ( \bar { x } , x _ { 0 } ) + \eta _ { 1 } ] / \nu ) + \textstyle \sum _ { ( \bar { x } , \bar { y } ) \in N _ { n } ^ { j } ( x _ { 0 } ) \setminus N _ { n } ^ { j - 1 } ( x _ { 0 } ) } D [ \bar { x } , \bar { y } ] )$ . Substituting the optimal value of $\beta ^ { \star }$ in the back in the dual optimization problem gives

$$
\begin{array}{l} \inf _ {\alpha , \beta , \nu \geq 0} g (\alpha , \beta , \eta , \nu) = \inf _ {\alpha , \nu \geq 0} g (\alpha , \beta^ {\star}, \eta , \nu) \\ \qquad = \inf \Big \{\alpha \in \mathrm{R}: \exists \nu \in \mathrm{R} _ {+}, \exists \eta \in \mathrm{R} _ {+} ^ {2}, r \cdot \nu - \frac {k}{n} (\eta_ {1} - \eta_ {2}) - \frac {\eta_ {2}}{n} \cdot \nu \\ \qquad + \nu \log (\sum_ {(\bar {x}, \bar {y}) \in N _ {n} ^ {j - 1} (x _ {0})} \exp ([ (L (z, \bar {y}) - \alpha) \cdot w _ {n} (\bar {x}, x _ {0}) + \eta_ {1} - \eta_ {2} ] / \nu) \cdot D [ \bar {x}, \bar {y} ] \\ \qquad + \sum_ {(\bar {x}, \bar {y}) \in N _ {n} ^ {j} (x _ {0}) \setminus N _ {n} ^ {j - 1} (x _ {0})} \exp ([ (L (z, \bar {y}) - \alpha) \cdot w _ {n} (\bar {x}, x _ {0}) + \eta_ {1} ] / \nu) \cdot D [ \bar {x}, \bar {y} ] \\ \qquad + \sum_ {\Omega_ {n} \setminus N _ {n} ^ {j} (x _ {0})} D [ \bar {x}, \bar {y} ]) \leq 0 \Big \}. \end{array}
$$

## B.8 Proof Lemma 2

Proof. We will employ standard Lagrangian duality on the convex optimization characterization of the Nadaraya-Watson cost function given in Corollary 1. The Lagrangian function associated with the primal optimization problem is denoted here at the function

$$
\begin{array}{c} \mathcal {L} (P, s; \alpha , \beta , \nu) := \sum_ {(\bar {x}, \bar {y}) \in \Omega_ {n}} w _ {n} (\bar {x}, x _ {0}) \cdot L (\bar {z}, \bar {y}) \cdot P [ \bar {x}, \bar {y} ] + \left(1 - \sum_ {(\bar {x}, \bar {y}) \in \Omega_ {n}} w _ {n} (\bar {x}, x _ {0}) \cdot P [ \bar {x}, \bar {y} ]\right) \alpha + \\ \left(\sum_ {(\bar {x}, \bar {y}) \in \Omega_ {n}} P [ \bar {x}, \bar {y} ] - s\right) \beta + \left(r \cdot s - \sum_ {(\bar {x}, \bar {y}) \in \Omega_ {n}} P [ \bar {x}, \bar {y} ] \log \left(\frac {P [ \bar {x} , \bar {y} ]}{s \cdot D [ \bar {x} , \bar {y} ]}\right)\right) \nu \end{array}
$$

where P and s are the primal variables of the primal optimization problem given in Corollary 1 and $\alpha , \; \beta$ and ν the dual variables associated with each of its constraints. Collecting the relevant terms in the Lagrangian function results in

$$
\mathcal {L} (P, s; \alpha , \beta , \nu) = \alpha + s (r \nu - \beta) + \sum_ {(\bar {x}, \bar {y}) \in \Omega_ {n}} \left[ P [ \bar {x}, \bar {y} ] ((L (\bar {z}, \bar {y}) - \alpha) \cdot w _ {n} (\bar {x}, x _ {0}) + \beta) - \nu P [ \bar {x}, \bar {y} ] \log \left(\frac {P [ \bar {x} , \bar {y} ]}{s \cdot D [ \bar {x} , \bar {y} ]}\right) \right]
$$

The dual function of the primal optimization problem is identified with $\begin{array} { r } { g ( \alpha , \beta , \nu )   : =   \operatorname* { i n f } _ { P \geq 0 ,   s > 0 } \mathcal { L } ( P , s ; \alpha , \beta , \nu ) } \end{array}$ Our dual function can be expressed alternatively as $g ( \alpha , \beta , \nu ) =$

$$
\begin{array}{c} \sup _ {s > 0} \alpha + s (r \nu - \beta) + \sup _ {P \geq 0} \sum_ {(\bar {x}, \bar {y}) \in \Omega_ {n}} \Big [ P [ \bar {x}, \bar {y} ] ((L (\bar {z}, \bar {y}) - \alpha) \cdot w _ {n} (\bar {x}, x _ {0}) + \beta) - \nu P [ \bar {x}, \bar {y} ] \log \left(\frac {P [ \bar {x} , \bar {y} ]}{s \cdot D [ \bar {x} , \bar {y} ]}\right) \Big ] \\ = \sup _ {s > 0} \alpha + s (r \nu - \beta) + \sum_ {(\bar {x}, \bar {y}) \in \Omega_ {n}} \sup _ {P [ \bar {x}, \bar {y} ] \geq 0} \Big [ P [ \bar {x}, \bar {y} ] ((L (\bar {z}, \bar {y}) - \alpha) \cdot w _ {n} (\bar {x}, x _ {0}) + \beta) - \nu P [ \bar {x}, \bar {y} ] \log \left(\frac {P [ \bar {x} , \bar {y} ]}{s \cdot D [ \bar {x} , \bar {y} ]}\right) \Big ] \\ = \sup _ {s > 0} \alpha + s (r \nu - \beta) + s \sum_ {(\bar {x}, \bar {y}) \in \Omega_ {n}} D [ \bar {x}, \bar {y} ] [ \sup _ {\lambda \geq 0} \lambda ((L (\bar {z}, \bar {y}) - \alpha) \cdot w _ {n} (\bar {x}, x _ {0}) + \beta) - \nu \lambda \log (\lambda) ]. \end{array}
$$

The inner maximization problems over λ can be dealt with using the Fenchel conjugate of the $\lambda \mapsto \lambda$ · log λ function as

$$
\begin{array}{l} = \sup _ {s > 0} \alpha + s (r \nu - \beta) + s \nu \sum_ {(\bar {x}, \bar {y}) \in \Omega_ {n}} D [ \bar {x}, \bar {y} ] \exp \left(\frac {(L (\bar {z} , \bar {y}) - \alpha) \cdot w _ {n} (\bar {x} , x _ {0}) + \beta}{\nu} - 1\right) \\ = \left\{\alpha : r \nu + \nu \sum_ {(\bar {x}, \bar {y}) \in \Omega_ {n}} D [ \bar {x}, \bar {y} ] \exp \left(\frac {(L (\bar {z} , \bar {y}) - \alpha) \cdot w _ {n} (\bar {x} , x _ {0}) + \beta}{\nu} - 1\right) \leq \beta \right\}. \end{array}
$$

The dual optimization problem is now found as $\operatorname { i n f } _ { \alpha , \beta , \nu \geq 0 } \: g ( \alpha , \beta , \nu )$ . As our primal optimization is convex, strong duality holds under Slater’s condition which is satisfied whenever $r > 0$ . Using first-order optimality conditions, the optimal $\beta ^ { \star }$ must satisfy $\begin{array} { r } { \beta ^ { \star } = - \nu + \nu \log ( \sum _ { ( \bar { x } , \bar { y } ) \in \Omega _ { n } } D [ \bar { x } , } \end{array}$ ȳ] exp $( ( L ( \bar { z } , \bar { y } ) - \alpha ) \cdot w _ { n } ( \bar { x } , x _ { 0 } ) / \nu ) )$ . Substituting the optimal value of $\beta ^ { \star }$ in the back in the dual optimization problem gives

$$
\left| \begin{array}{l} \inf _ {\alpha , \beta , \nu \geq 0} g (\alpha , \beta , \nu) = \inf _ {\alpha , \nu \geq 0} g (\alpha , \beta^ {\star}, \nu) \\ \qquad = \inf \left\{\alpha \in \mathrm{R}: \exists \nu \in \mathrm{R} _ {+}, r \nu + \nu \log \left(\sum_ {(\bar {x}, \bar {y}) \in \Omega_ {n}} D [ \bar {x}, \bar {y} ] \exp \left(\frac {(L (\bar {z} , \bar {y}) - \alpha) \cdot w _ {n} (\bar {x} , x _ {0})}{\nu}\right)\right) \leq 0 \right\}. \end{array} \right.
$$