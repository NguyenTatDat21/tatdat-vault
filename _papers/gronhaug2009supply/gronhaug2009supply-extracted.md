619 LECTUATNOTESICAEOSTMCS AND MATHEMATICAL SYSTEMS

Luca Bertazzi M. Grazia Speranza Jo A.E.E. van Nunen (Editors)

Innovations in Distribution Logistics

# Lecture Notes in Economics and Mathematical Systems

Founding Editors:

M. Beckmann H.P. Künzi

Managing Editors:

Prof. Dr. G. Fandel

Fachbereich Wirtschaftswissenschaften

Fernuniversität Hagen

Feithstr. 140/AVZ II, 58084 Hagen, Germany

Prof. Dr. W. Trockel

Institut für Mathematische Wirtschaftsforschung (IMW)

Universität Bielefeld

Universitätsstr. 25, 33615 Bielefeld, Germany

Editorial Board:

A. Basile, A. Drexl, H. Dawid, K. Inderfurth, W. Kürsten

619

# Innovations in Distribution Logistics

Professor Luca Bertazzi Professor M. Grazia Speranza Universit degli Studi di Bresciaà Dipartimento Metodi Quantitativi Contrada da S. Chiara 50 25122 Brescia Italy bertazzi@eco.unibs.it speranza@eco.unibs.it

ISBN 978-3-540-92943-7 DOI 10.1007/978-3-540-92944-4

Lecture Notes in Economics and Mathematical Systems ISSN 0075-8442

Library of Congress Control Number: 2008944011

© 2009 Springer-Verlag Berlin Heidelberg

Printed on acid-free paper

9 8 7 6 5 4 3 2 1

springer.com

Professor Jo. A. E. E. van Nunen Erasmus University Rotterdam School of Management Department of Decision and Information Sciences Burg. Oudlaan 50, Roomnr. T09-30 3062 PA Rotterdam The Netherlands jnunen@rsm.nl

e-ISBN 978-3-540-92944-4

Cover design:SPi Publishing Services, India

This work is subject to copyright. All rights are reserved, whether the whole or part of the material is concerned, specifically the rights of translation, reprinting, reuse of illustrations, recitation, broadcasting, reproduction on microfilm or in any other way, and storage in data banks. Duplication of this publication or parts thereof is permitted only under the provisions of the German Copyright Law of September 9, 1965, in its current version, and permissions for use must always be obtained from Springer-Verlag. Violations are liable for prosecution under the German Copyright Law.

The use of general descriptive names, registered names, trademarks, etc. in this publication does not imply, even in the absence of a specific statement, that such names are exempt from the relevant protective laws and regulations and therefore free for general use.

# Preface

The globalization of markets and the availability of new information technologies have stimulated research in distribution logistics in the last few years. Classical transportation, routing and inventory problems are being more and more studied from a supply chain management perspective and the on-line information made available by the new technologies is more and more used in the decision processes.

A scientific approach to the most innovative logistic problems, combined with a high level of attention towards practice, has motivated a series of “International workshops in distribution logistics (IWDL)”. This volume includes some of the papers that have been presented at the IWDL2006, the workshop of the IWDL series which was in Brescia (Italy) in October 2006.

In this volume we focus on the distribution network, which represents the most complex and critical part of the logistic system, and cover several areas, in particular distribution network design, supply chain optimization, internal logistics, routing problems, transportation and e-business, and location problems.

Due to the variety of the topics in the domain of distribution logistics covered by this volume, we decided to present the contributions in alphabetical order of the name of the first author. The reader will find through the index the topic he/she is most interested in. This volume is thought to be an important reference for researchers and also for PhD and Master students.

We would like to thank the authors of the papers for their contributions. All the papers submitted for publication in this volume were been subjected to a refereeing process and we are deeply indebted to the referees whose professional help has been fundamental to ensure a high quality level of this volume.

Brescia, Rotterdam February 2009

## Contents

- **Management Policies in a Dynamic Multi-Period Routing Problem**
- Enrico Angelelli, Nicola Bianchessi, Renata Mansini, M. Grazia Speranza ... 1
- **Optimizing the Storage Area Dimension in a Production System**
- Luca Bertazzi .... 17
- **On-line Routing per Mobile Phone: A Case on Subsequent Deliveries of Newspapers**
- Thomas Bieding, Simon Görtz, Andreas Klose .... 29
- **Service Design Models for Rail Intermodal Transportation**
- Teodor Gabriel Crainic .... 53
- **C.A.s.S.a.n.D.r.A.: Computerized AnalysiS for Supply ChAiN**
- **DistRibution Activity**
- Laura Di Giacomo, Ettore Di Lena, Giacomo Patrizi, Livia Pomaranzi,
- Federico Sensi .... 69
- **Ship Routing and Scheduling with Persistence and Distance Objectives**
- Kjetil Fagerholt, Jarl Eirik Korsvik, Arne Løkketangen .... 89
- **Logistics in Real-Time: Inventory-Routing Operations**
- **Under Stochastic Demand**
- Ricardo Giesen, Hani S. Mahmassani, Patrick Jaillet .... 109
- **On Optimizing Production Nodes in Supply Chain Systems**
- Davide Giglio, Riccardo Minciardi, Simona Sacone, Silvia Siri .... 149
- **Approximate Optimal Order Batch Sizes in a Parallel-aisle Warehouse**
- Yeming Gong, René de Koster .... 175
- **Supply Chain Optimization for the Liquefied Natural Gas Business**
- Roar Grønhaug, Marielle Christiansen .... 195

- **Modeling The Pre-Auction Stage: The Truckload Case**
- Gianfranco Guastaroba, Renata Mansini, M. Grazia Speranza ..... 219
- **Applications of the Double Standard Model for Ambulance Location**
- Gilbert Laporte, François V. Louveaux, Frédéric Semet, Arnaud Thirion ..... 235
- **A Pricing Algorithm for the Vehicle Routing Problem with Soft Time Windows**
- Federico Liberatore, Giovanni Righini, Matteo Salani ..... 251
- **Effective Algorithms for a Bounded Version of the Uncapacitated TPP**
- Renata Mansini, Barbara Tocchella ..... 267

## List of Contributors

**Enrico Angelelli** University of Brescia, Italy, angele@eco.unibs.it

**Luca Bertazzi** University of Brescia, Italy, bertazzi@eco.unibs.it

**Nicola Bianchessi** University of Brescia, Italy, bianche@eco.unibs.it

**Thomas Bieding** Vodafone D2 GmbH, Germany, thomas.bieding@vodafone.com

**Marielle Christiansen** Norwegian University of Science and Technology, Norway, marielle.christiansen@ iot.ntnu.no

**Teodor Gabriel Crainic** University of Quebec in Montreal, Canada, theo@crt.umontreal.ca

**Rene de Koster** ´ RSM Erasmus University, Netherlands, rkoster@rsm.nl

**Laura Di Giacomo** LIX, Ecole ´ Polytechnique, France, digiacomo@lix.polytechnique.fr

**Ettore Di Lena** Ente Nazionale Energia Elettrica, Italy, ettore.dilena@enel.it

**Kjetil Fagerholt** Norwegian University of Science and Technology, Norway, kjetil.fagerholt@iot.ntnu.no

**Ricardo Giesen** Pontificia Universidad Católica de Chile, Chile, Giesen@ing.puc.cl

**Davide Giglio** University of Genova, Italy, davide.giglio@unige.it

**Yeming Gong** RSM Erasmus University, The Netherlands, ygong@rsm.nl

**Simon Gortz ¨** University of Wuppertal, Germany, simon.goertz@wiwi.uni-wuppertal.de

**Roar Grønhaug** Norwegian University of Science and Technology, Norway, roar.gronhaug@iot.ntnu.no

**Gianfranco Guastaroba** University of Brescia, Italy, guastaro@eco.unibs.it

**Patrick Jaillet** Massachusetts Institute of Technology, USA, Jaillet@MIT.edu

**Andreas Klose** University of Aarhus, Denmark, aklose@imf.au.dk

**Jarl Eirik Korsvik** Norwegian University of Science and Technology, Norway, korsvik@ntnu.no

**Gilbert Laporte** HEC Montréal, Canada, gilbert@crt.umontreal.ca

**Federico Liberatore** University of Milan, Italy, fliberatore@crema.unimi.it

**Arne Løkketangen** Molde University College, Norway, Arne.Lokketangen@hiMolde.no

François V. Louveaux Facultés Universitaires Notre-Dame de la Paix, Belgium, francois.louveaux@fundp.ac.be

**Hani S. Mahmassani** Northwestern University, USA, Masmah@northwestern.edu

**Renata Mansini** University of Brescia, Italy, rmansini@ing.unibs.it

**Riccardo Minciardi** University of Genova, Italy, riccardo.minciardi@unige.it

**Giacomo Patrizi** La Sapienza, Università di Roma, Italy, g.patrizi@caspur.it

**Livia Pomaranzi** Chefaro Pharma Italia, Italy, livia.pomaranzi@chefaro.it

**Giovanni Righini** University of Milan, Italy, righini@dti.unimi.it

**Simona Sacone** University of Genova, Italy, simona.sacone@unige.it

**Matteo Salani** Ecole Politechnique ´ Fédérale de Lausanne, Switzerland, matteo.salani@epfl.ch

**Fred´ eric Semet** ´ LAMIH-ROI, Université de Valenciennes et du Hainaut-Cambrésis, France, and Université de Montréal, Canada, frederic.semet@univ-valenciennes.fr

**Federico Sensi** Enprovia Software Engineering, Italy, Federico-Sensi@libero.it

**Silvia Siri** University of Genova, Italy, silvia.siri@unige.it

**Maria Grazia Speranza** University of Brescia, Italy, speranza@eco.unibs.it

**Arnaud Thirion** Facultés Universitaires Notre-Dame de la Paix, Belgium, thirionarnaud@hotmail.com

**Barbara Tocchella** University of Brescia, Italy, barbara.tocchella@ing.unibs.it

# Management Policies in a Dynamic Multi-Period Routing Problem

Enrico Angelelli<sup>1</sup>, Nicola Bianchessi<sup>2</sup>, Renata Mansini<sup>3</sup>, and M. Grazia Speranza<sup>4</sup>

1 Dipartimento Metodi Quantitativi, University of Brescia, Italy angele@eco.unibs.it

2 Dipartimento Metodi Quantitativi, University of Brescia, Italy bianche@eco.unibs.it

3 Dipartimento di Elettronica per l’Automazione, University of Brescia, Italy rmansini@ing.unibs.it

4 Dipartimento Metodi Quantitativi, University of Brescia, Italy speranza@eco.unibs.it

**Summary.** In this paper we analyze the Dynamic Multi-Period Routing Problem (DMPRP), where a fleet of uncapacitated vehicles has to satisfy customers’ pick-up requests. The service of each customer can take place the day the request is issued or the day after. At the beginning of a day a set of requests are already known and have to be served during the day. Additional requests may arrive during the day while the vehicles are traveling. In this context we perform different types of analysis, each one characterized by the comparison of alternative management policies. The first analysis compares a policy which decides, at the time the request is issued, whether to accept or reject it to a policy that accepts all the requests and decides, at a later time, which ones to forward to a back-up service company. The second evaluates the advantages of a collaborative service policy where a fleet of vehicles is managed by a unique decision maker with respect to a policy where the same vehicles are managed independently. Finally, in the last analysis a policy where each new request is taken into account as soon as it is issued is compared to a policy where all the requests issued during a day are analyzed at the end of the day. Extensive computational results evaluating the number of lost requests and the distance traveled provide interesting insights.

**Key words:** Dynamic multi-period routing problems, Postponable requests, Management policies

## 1 Introduction

Dynamic settings are receiving an increasing attention in routing problems thanks also to a wider use of communication devices in vehicles equipment. Nowadays, the use of GPS systems allows a central unit to constantly know the location of vehicles and to take dynamic decisions on the basis of the overall situation of vehicles and customers. Such situation evolves during the day and previous plans may be modified because new requests are issued by customers or because some unexpected event took place such as a delay due to traffic congestion. It is expected that such dynamic management improves the competitiveness of a company, allowing a better service at a lower cost.

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">L. Bertazzi et al. (eds.), Innovations in Distribution Logistics, Lecture Notes in Economics and Mathematical Systems 619, DOI: 10.1007/978-3-540-92944-4,</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">-c 2009 Springer-Verlag Berlin Heidelberg</span></small>

While the literature on static routing problems is wide, the literature on dynamic routing problems is limited, though it has consistently grown in the last years. Comprehensive surveys on dynamic problems can be found in Psaraftis [10, 11] and, more recently, in Ghiani et al. [5]. Among the most relevant contributions in this domain we recall Savelsbergh and Sol [12] and Yang et al. [13] for the management of dynamic fleet of vehicles; Gendreau et al. [4] and Ichoua et al. [6] for real-time vehicle routing and dispatching problems in long-distance courier services; Mitrović-Minić et al. [8] and Mitrović-Minić and Laporte [9] for the dynamic pick-up and delivery problem with time windows and Madsen et al. [7] for a dynamic dial-a-ride system characterized by multiple capacities and multiple objectives. Finally, Angelelli et al. [2, 3] perform a competitive analysis for some policies in a simple dynamic multi-period setting.

The dynamic setting we consider in this paper is the Dynamic Multi-Period Routing Problem (DMPRP) introduced in [1]. The problem is characterized by pick-up requests arriving in real time to the central depot of a courier company. A fleet of uncapacitated vehicles is available for the service. Every morning these vehicles leave the depot and have to return to the depot at the end of the day. Thanks to modern communication technology, the company knows the exact position of its vehicles at any time instant and is able to forecast their positions in the near future. The company can react to on-line requests and possibly modify the previous traveling plans. The distinctive features of this dynamic problem with respect to those analyzed in the literature is that requests can be served within two days from their issuance. This means that when a request is issued, a deadline is associated to it. Thus, every day, the requests can be either off-line when they are known in advance (i.e. they have been issued the day before but not serviced yet) or on-line when they come over in real-time, while the vehicles are traveling. Moreover, requests are also classified as postponable or unpostponable. If a request is unpostponable it has to be inserted in the currently traveled routes, on the contrary if it is postponable it can be served either today or tomorrow. The objective of the company is to maximize the number of serviced requests while minimizing the average operational cost per day.

The most common approach used in the literature to solve a dynamic problem is based on a repeated re-optimization of the off-line problem. In [1], the authors introduce different short term strategies characterized by a look-ahead period and a short term objective. For each strategy, a corresponding re-optimization problem is defined and iteratively solved by means of a Variable Neighborhood Search (VNS) meta-heuristic. An extensive computational analysis of the impact each short term strategy has on the long term objective of the problem is provided.

In the present paper, we evaluate and compare alternative management policies, by making use of the solution framework presented in [1]. The scope of the paper is to focus on the possible advantages that a company can achieve by applying some management policies concerning, for instance, the treatment of new customers and of on-line information. In this perspective we perform three different types of analysis, each one characterized by two alternative management policies. In the first we compare the management policy on the basis of which an immediate decision is taken, at the time a request is issued, on whether to accept or reject it to the policy which accepts all the requests and, at a later time, forwards some of the requests, if needed, to a back-up service company. Then, we study the advantages of a collaborative service policy where a fleet of vehicles is managed by a unique decision maker with respect to a less flexible policy where the same vehicles are managed independently. Finally, the third analysis compares a policy where each new request is taken into account as soon as it is issued to a policy where all the requests issued during a day are analyzed at the end of the day. Comparison is made by means of extensive computational results evaluating the number of lost requests and the distance traveled.

## 2 The Dynamic Multi-Period Problem

A fleet of uncapacitated vehicles $V \; = \; \{ v _ { 1 } , \ldots , v _ { m } \}$ is available to satisfy requests issued by customers. The positions of the vehicles are known to the central depot at any time during the day. Moreover, the vehicles can communicate with the central depot. At the beginning of each day a set of requests are known that have to be served during the day (unpostponable requests). These requests are assigned to the vehicles and the vehicles leave the depot and start traveling on the basis of an initial plan. During the day new requests may be issued by customers. Unpostponable requests can be accepted only until a fixed time L in the morning (e.g. noon or 1:00 PM). We define as postponable all the requests issued during the day that can be served in the same day or postponed to the day after. The time length of each working day is equal to τ. This is also the maximum time available to each vehicle route, i.e. we will refer to the length of a route by meaning a time length. Decisions are repeated over a time horizon of T days.

All requests are requests of a pick-up service. In fact, it is assumed that delivery requests are not consistent with this dynamic setting, since if a delivery request is issued during the day, then a vehicle cannot be deviated to serve the new customer. Moreover, if a vehicle leaves the depot with the load to be delivered to a customer, the service of that customer cannot later be assigned to a different vehicle. In case the company satisfies both pick-up and delivery requests, the assumption is that the fleet is divided into two parts, a part dedicated to the delivery service and the other part dedicated to the pick-up service. The part dedicated to the delivery service works as traditionally in a static context where the vehicles follow during the day the plan assigned to them at the beginning of the day. The part dedicated to the pick-up service is managed dynamically.

The central depot may elaborate new plans during the day and communicates the changes to the vehicles. The changes in a vehicle plan may concern the inclusion of new customers, the deletion of customers or both. The vehicle can receive the new plans at any time and possibly deviate from its previous route while traveling between two customers. The goal is the minimization of the total service cost over the whole horizon. Such major target has been formalized through two hierarchical objectives. The first one is the maximization of the number of requests directly served by the company, which is equivalent to the minimization of the number of not served requests, i.e. rejected or forwarded to the backup service, depending on the policy. The second one is the minimization of the length of the routes traveled per serviced request.

## 2.1 The Solution Framework

In [1] the authors introduced in a rolling horizon solution framework the concept of a Short Term Strategy (STS). A STS includes the definition of a re-optimization problem that is solved by means of a Variable Neighborhood Search (VNS) heuristic. Before the beginning of the day and then at regular intervals (re-optimizations intervals) the re-optimization problem is solved. The first re-optimization problem considers unpostponable requests only and provides for each vehicle a route that starts and ends at the depot. The subsequent re-optimization problems take into account all known requests (postponable and unpostponable) and provide for each vehicle a route that starts at the forecasted position of the vehicle at the end of the re-optimization according to the previously planned routes and ends at the depot.

Time is denoted during the day with $t \in [ 0 , \tau ]$ . We indicate by $R _ { P } ( t )$ and $R _ { U } ( t )$ the set of postponable and unpostponable requests at a given time t, respectively. We also denote by $R ( t ) = R _ { P } ( t ) \cup R _ { U } ( t )$ the total set of the requests known at time t. Let Δt be the length of the re-optimization interval and let $t ^ { \prime } = t   +   \varDelta t$ . The set $R ( t ^ { \prime } )$ differs from $R ( t )$ for the inclusion of all the new requests which have become available during the last re-optimization interval Δt and for the elimination of all the requests served in the meantime.

A maximum time $O p t T i m e \leq \mathcal { A } t$ is made available to the algorithm that solves each re-optimization problem. The solution found is implemented until the end of the next re-optimization phase. The generated routes are followed by the vehicles from time $t + O p t T i m e$ to time $t ^ { \prime } + O p t T i m e$ , that is until the routes obtained with the subsequent re-optimization have become available.

## 2.2 The Short Term Strategy

In [1] several Short Term Strategies have been analyzed and compared. A Short Term Strategy (STS) consists of the following main components:

1. A look-ahead period: The period of time over which the re-optimization problem is defined;

2. A short term objective: The criterion used to evaluate the quality of a solution in the re-optimization problem;

3. A re-optimization problem: The off-line problem which is formulated and solved, after a look-ahead period and a short term objective have been defined;

4. A re-optimization interval: The length of the time interval between the solution of two consecutive re-optimization problems.

Let $r _ { P } ^ { 1 }$ and $r _ { U } ^ { 1 }$ represent the number of postponable and unpostponable requests served today, respectively. Moreover, let $r ^ { 1 }$ and $l ^ { 1 }$ denote the total number of served requests and the total length of the routes traveled in the current day, respectively. Let $r ^ { 2 }$ and $l ^ { 2 }$ denote the number of served requests and the total length of the routes traveled the day after, respectively. The class of strategies that in [1] turned out to be the most successful has a 2-day look-ahead period, and the following objective function:

$$
\min \quad \alpha l ^ {1} + (1 - \alpha) l ^ {2} + (r _ {P} ^ {1} + r ^ {2}) K _ {2} + r _ {U} ^ {1} K _ {1}\tag{1}
$$

where $\alpha$ is a real number such that $0   \leq   \alpha   \leq   1$ , and $K _ { 1 } ,   K _ { 2 }$ are negative constant values such that $K _ { 1 } \ll K _ { 2 } \ll 0$ . The function maximizes the number of unpostponable served requests (term $r _ { U } ^ { 1 } K _ { 1 } )$ and, as second hierarchical objective, maximizes the total number of postponable requests to be served within the day after (term $( r _ { P } ^ { 1 } + r ^ { 2 } ) K _ { 2 } )$ . Actually, the requests that are postponable today will become unpostponable tomorrow and have to be served within tomorrow. Finally, the third hierarchical objective is the minimization of the weighted sum of the lengths of the routes traveled today and tomorrow (term $\alpha l ^ { 1 } + ( 1 - \alpha ) l ^ { 2 } )$ . We decided to set $\alpha   =   1 ^ { - }$ so that a decrease in the distance traveled today is to be preferred to any decrease in the distance traveled tomorrow.

Throughout the paper we indicate by 2-day look-ahead(Δt) the 2-day look-ahead strategy with the short term objective function (1) and $\alpha$ set to 1−. Each of the analyzed management policies, with one exception only, can be implemented by means of a straightforward implementation of the 2-day look-ahead(Δt) strategy.

## 3 Comparison of Alternative Management Policies

In the following we consider three real situations where different management policies can be implemented. We analyze and compare different policies by making use of a proper implementation of the 2-day look-ahead(Δt) strategy.

## 3.1 Accept/reject vs. Delay Policy

When a new request is issued, the central unit of a company can immediately check whether it is possible to serve it given the available fleet of vehicles. The decision has to be taken on the basis of the already accepted requests possibly modifying the current routing plan. The company accepts to serve the request if it can be feasibly inserted in the current plan. Otherwise the company rejects the request. We call this policy accept/reject. Since we assume that there are requests that can be served in the day of their issuance or postponed to the day after, a more customer oriented version of the accept/reject policy is of interest: an accept/reject policy where the day in which the service will be accomplished is fixed once for all and is made known to the customer as soon as his/her request is accepted ( fixed day accept/reject policy).

In the same situation, the company may follow an alternative policy where no request is rejected. Since the fleet may not be sufficient to satisfy all the issued requests, a contract with a back-up service company has to be made in such a way that, in case of need, some of the customers will be served by the back-up company. In this case, the back-up company is informed on the customers to be served at the end of the morning. This policy, called delay, allows the company to postpone the decision about the customers to serve directly and the customers to be served by the back-up company. At the same time the company offers a better service, since no customer is ever rejected.

The delay policy can be implemented by means of the 2-day look-ahead(Δt) with any fixed value of the parameter Δt. On the contrary, to implement the accept/reject policy the Δt characterizing the strategy should be small enough to allow the defini tion of a new re-optimization problem as soon as a new request is issued. Moreover, the solution framework itself has to be modified so that if a request is accepted it will be certainly served and will be never excluded by future re-optimizations. Otherwise, if an arriving request is not immediately included in the current solution it will be definitely discarded from the system.

## 3.2 Collaborative vs. Individual Transportation Policy

Traditionally, transportation companies have focused their attention on controlling and reducing their own costs to increase profitability. More recently, companies have started to explore the possibility to share information with other companies and to develop common transportation plans with further reduction of costs. A collaborative transportation policy might open up cost saving opportunities that are impossible to achieve with an internal company policy.

We compare a collaborative transportation policy where the route plans of a fleet of vehicles are designed by a unique decision maker who brings together all customer requests to a policy where the same vehicles are managed independently (individual transportation policy). The situation refers to the real case where the service provided by a company with a large fleet of vehicles is compared to that provided by different smaller companies which globally own the same number of vehicles but whose route plans are managed independently. In both cases we consider a delay policy.

## 3.3 Dynamic vs. Static Policy

A dynamic policy is attractive because it may reduce operational costs and guarantee a better service level. However, it also implies additional costs due to the devices needed for the communication and a different organization. Do the benefits compensate the costs? We compare a dynamic policy to a policy where the vehicles follow the route plans made available at the beginning of the day and based on the requests that arrived the day before. Since for this policy all requests issued during a day are analyzed only at its end we call it static policy. In practice, this policy may occur in those companies where vehicles do not have a communication system equipment which makes possible for the central unit to know their location at each time instant and to dynamically change their route plans. The static policy can be implemented by setting the re-optimization interval Δt equal to the working time τ. Whereas the dynamic policy can be implemented by means of the 2-day look-ahead(Δt) strategy with any value of the parameter Δt.

## 4 Computational Results

## 4.1 Testing Environment

The computational analysis has been carried out on random scenarios, where the requests are uniformly distributed over a service area of $1 0 0 \times 1 0 0   k m ^ { 2 }$ . Each scenario is characterized by a planning horizon of $T   =   5$ days and a daily working time of $\tau = 1 0$ h (from 8:00 AM to 6:00 PM). A scenario is also characterized by a parameter λ of a Poisson distribution according to which the requests are dynamically generated. The parameter λ is the mean arrival rate of requests per day and is assumed to take one of the following values: 100, 200, 300, 400, 500. Since a scenario can be characterized by the presence of unpostponable requests, we have assumed that, with a probability equal to $\frac{1}{3}$ , the requests issued before 1:00 PM are unpostponable. The service is provided by means of a fleet of three uncapacitated vehicles, each of them traveling at a constant speed of $2 5   \mathrm { k m   h ^ { - 1 } }$ . In order to make all results comparable, an additional day is considered to complete the work of the not yet served requests. In fact, if not so, an improper advantage might be obtained by postponing as many requests as possible from day T to day $T + 1$

Given a scenario, we generate five instances which differ for the number of the daily requests and for their geographical location. In particular, each request coordinates are randomly selected among the customer coordinates in the sets r1 and r2 of the Solomon’s instances for the Vehicle Routing Problem with Time Windows. In all the instances, the coordinates of the depot are those of the Solomon’s ones. Moreover, requests are listed for each day in increasing order of their release time.

In the following computational experiments some features of this general data setting have been modified according to the type of policies taken into account. For instance, the generated scenarios may not have unpostponable requests. The number of not served requests and the distance traveled are evaluated for each policy in order to discuss the advantages of their application.

All computational experiments have been carried out on a 1.5GHz Intel Pentium IV machine with 512MB of RAM.

## 4.2 Re-Optimization Time Interval Influence

Before analyzing the different policies behavior we have conducted some preliminary experiments testing alternative 2-day look-ahead strategies differing for the value of the re-optimization interval Δt (respectively, set to 30, 150, 300, 600, 900, 1,800, 3,600). We aim at possibly identifying the best re-optimization time.

To implement the short term strategies we have set the parameter OptTime representing the re-optimization time given to the VNS meta-heuristic equal to $\max\{\frac{1}{12}\mathcal{A}t,\ 30\ s\}$ . In [1] the re-optimization time was set to $\frac { 1 } { 1 2 } \varLambda t$ and various values of the re-optimization interval Δt were tested. However, as the minimum tested value was $\lambda t = 3,600   s$ the value of the re-optimization time turned out to take reasonable values, never smaller than 300 s. In the experiments we discuss here the tested values of the re-optimization interval are much smaller and implied the need to avoid the situation where the re-optimization time could take values smaller than 30 s. We evaluated, on the basis of a set of preliminary experiments, that the VNS does not require more than 30 s to solve the tested instances.

The trend of the number of lost requests as a function of $\varDelta t$ is shown in Fig. 1 where the results for each scenario depending on λ are provided. It is evident how, independently of the scenario, the minimum number of lost requests is found for $\mathcal { A } t   =   3 0 \mathrm { ~ s ~ }$ . In particular, if we consider those scenarios where the number of lost requests is quite high $( \mathrm{i.e.}   \lambda \geq 300 )$ this number reduces on average by 50.66% when moving from $\mathcal{A}t = 3, 600  to  \mathcal{A}t = 30  s .$

![](images/page_16_chart_5.jpg)

Fig. 1. 2-day look-ahead strategies with different Δt: not served requests

In Fig. 2 we plot the average distance traveled per served request as function of Δt under the different scenarios. Again, independently of λ, the average distance traveled to serve a request tends to reduce when Δt shrinks: the lower the time between two consecutive re-optimizations the more efficient the transportation service.

These preliminary experiments have lead to the final decision to set $\mathcal { A } t = 3 0$ for all the policies but the static one.

## 4.3 Accept/reject vs. Delay Policy

In the following we discuss the computational results obtained when comparing accept/reject policies to the delay policy.

Table 1 is divided into three parts, one for each of the analyzed policies. The first column in each part provides the average number of lost requests when the corresponding policy is applied under the five different scenarios. Each column gap<sub>d</sub> measures the average percent increase in the number of not served requests of the analyzed policy with respect to the delay policy. Similarly, $g a p _ { a / r }$ measures the percentage increase of the number of lost requests of the fixed day accept/reject policy when compared to its basic version without fixed day. A negative percentage value (as for $\lambda = 2 0 0 )$ means that, on average, the fixed day policy has provided a lower number of lost requests.

Table 2 shows the average total distance traveled by the vehicles. The meaning of each column is the same as for Table 1.

If we consider the scenarios with λ ≥ 300 the accept/reject policy looses on average 71.91% more requests than the delay policy. The result is even worse if we consider the fixed day accept/reject policy.

Table 1. Delay vs. accept/reject policies: number of not served requests

<table><tr><td> $\lambda$ </td><td>Delay #</td><td colspan="2">Accept/reject # gap $_d$ (%)</td><td colspan="3">fixed day accept/reject # gap $_d$ (%) gap $_{a/r}$ (%)</td></tr><tr><td>100</td><td>0.00</td><td>0.00</td><td>-</td><td>0.40</td><td>100.00</td><td>100.00</td></tr><tr><td>200</td><td>16.40</td><td>21.00</td><td>28.05</td><td>19.00</td><td>15.85</td><td>-9.52</td></tr><tr><td>300</td><td>52.00</td><td>88.40</td><td>70.00</td><td>101.60</td><td>95.38</td><td>14.93</td></tr><tr><td>400</td><td>94.60</td><td>162.60</td><td>71.88</td><td>175.80</td><td>85.84</td><td>8.12</td></tr><tr><td>500</td><td>157.6</td><td>274.00</td><td>73.86</td><td>276.60</td><td>75.51</td><td>0.95</td></tr></table>

When considering traveled distances, one can notice that, for each scenario, all policies tend to completely use the available vehicles: But for only one case (λ = 300), the average distances traveled by applying the three policies differ from each other for a percentage less than 1%.

![](images/page_18_chart_2.jpg)

![](images/page_18_chart_3.jpg)

![](images/page_18_chart_4.jpg)

![](images/page_18_chart_5.jpg)

![](images/page_18_chart_6.jpg)

Fig. 2. 2-day look-ahead strategies with different Δt: average distance traveled per served request

Table 2. Delay vs. accept/reject policies: distance traveled

<table><tr><td> $\lambda$ </td><td>Delayl</td><td colspan="2">Accept/rejectl gap $_{d}$ (%)</td><td colspan="3">Fixed day accept/rejectl gap $_{d}$ (%) gap $_{a/r}$ (%)</td></tr><tr><td>100</td><td>513,482.63</td><td>511,915.97</td><td>-0.31</td><td>516,256.46</td><td>0.54</td><td>0.85</td></tr><tr><td>200</td><td>588,000.22</td><td>588,730.57</td><td>0.12</td><td>587,590.58</td><td>-0.07</td><td>-0.19</td></tr><tr><td>300</td><td>615,194.60</td><td>618,585.07</td><td>0.55</td><td>621,880.01</td><td>1.09</td><td>0.53</td></tr><tr><td>400</td><td>627,632.89</td><td>632,123.91</td><td>0.72</td><td>633,111.51</td><td>0.87</td><td>0.16</td></tr><tr><td>500</td><td>633,372.85</td><td>636,490.40</td><td>0.49</td><td>636,841.83</td><td>0.55</td><td>0.06</td></tr></table>

## 4.4 Collaborative vs. Individual Transportation Policy

In this class of experiments we have selected the scenario characterized by $\lambda = 3 0 0$ and, since the value of λ is fixed, we increased the number of instances to 10.

Since the fleet consists of three uncapacitated vehicles we compared the policy of a company which can decide for the route planning of all the three vehicles to the individual transportation policy applied by three different companies each one exploiting one vehicle only. Since, in each instance, the requests are sorted in increasing order of their release time, we have generated three smaller instances. The three small instances consider one request every three requests starting with the first, the second and the third request of the sorted list, respectively. From a practical point of view, this is equivalent to assume that each of the three vehicles in the individual transportation policy cover the same $1 0 0 \times 1 0 0 \: k m ^ { 2 }$ geographical area.

Table 3 provides the number of not served requests in each of the 10 instances by the collaborative transportation policy (column 2) and by the three individual transportation policies applied to the derived instances (columns 3–5). The last line of the table provides the average values. By moving from individual transportation transportation systems to a collaborative one the number of lost requests decreases, on average, by an order of magnitude.

Table 4 shows the distance traveled by the three vehicles in the collaborative system (column 2) and that traveled by each of the three vehicles in the individual one (columns 3–5) as well as their sum (column 6). The last column provides the percent gap between values of column 2 and column 6 computed as $\frac { \sum _ { i = 1 } ^ { i = 3 } l _ { i } { - } l } { l }$ . As before, the last line provides average values out of the 10 instances. The advantages provided by a collaborative transportation policy are evident also in terms of traveled distance. The total distance traveled by the sum of three vehicles managed individually is, on average, higher by 4.77% even if the number of serviced requests is much lower (cfr. column 5 in Table 3).

Table 3. Collaborative vs. individual transportation policy: number of not served requests

| Instance | # | $\#_1$ | $\#_2$ | $\#_3$ | $\sum_{i=1}^{i=3} \#_i$ |
| --- | --- | --- | --- | --- | --- |
| 1 | 46 | 184 | 183 | 168 | 535.00 |
| 2 | 54 | 192 | 185 | 198 | 575.00 |
| 3 | 44 | 203 | 195 | 193 | 591.00 |
| 4 | 54 | 183 | 188 | 193 | 564.00 |
| 5 | 62 | 192 | 183 | 198 | 573.00 |
| 6 | 53 | 194 | 194 | 185 | 573.00 |
| 7 | 46 | 191 | 187 | 175 | 553.00 |
| 8 | 44 | 187 | 180 | 181 | 548.00 |
| 9 | 39 | 183 | 183 | 187 | 553.00 |
| 10 | 66 | 205 | 199 | 193 | 597.00 |
|  | 50.80 | 191.40 | 187.70 | 187.10 | 566.20 |

Table 4. Collaborative vs. individual transportation policy: distance traveled

| Instance | $l$ | $l_{1}$ | $l_{2}$ | $l_{3}$ | $\sum_{i=1}^{i=3} l_{i}$ | gap (%) |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 611,830.00 | 213,116.62 | 213,115.80 | 213,234.55 | 639,466.97 | 4.52 |
| 2 | 619,250.07 | 214,464.66 | 214,033.89 | 213,555.14 | 642,053.69 | 3.68 |
| 3 | 617,810.59 | 215,376.95 | 213,560.64 | 214,432.88 | 643,370.47 | 4.14 |
| 4 | 607,299.61 | 214,673.09 | 212,627.13 | 213,197.80 | 640,498.02 | 5.47 |
| 5 | 619,782.75 | 214,658.65 | 213,588.85 | 214,084.49 | 642,331.99 | 3.64 |
| 6 | 595,790.27 | 214,671.30 | 213,490.68 | 209,136.81 | 637,298.79 | 6.97 |
| 7 | 609,354.19 | 214,887.06 | 214,401.58 | 214,989.29 | 644,277.93 | 5.73 |
| 8 | 615,016.16 | 214,169.54 | 212,961.75 | 214,310.70 | 641,441.99 | 4.30 |
| 9 | 614,192.44 | 214,833.80 | 214,613.17 | 214,843.07 | 644,290.04 | 4.90 |
| 10 | 613,412.14 | 214,297.79 | 212,961.39 | 213,079.88 | 640,339.06 | 4.39 |
|  | 612,373.82 | 214,514.95 | 213,535.49 | 213,486.46 | 641,536.90 | 4.77 |

## 4.5 Dynamic vs. Static Policy

Since on-line unpostponable requests cannot be managed by a static policy, in this class of experiments we have considered postponable requests only. A comment is required in order to better understand the results. Our general assumption is that we want to guarantee the service of a request within the end of the day following its issuance. This means that, on average, 1.5 days are available to serve a request when the dynamic policy is applied and only 1 day when the static policy is chosen.

In Table 5 for each scenario (value of λ) the average number of not served requests for the static policy (column 3) and for the dynamic one (column 2) are shown. If we analyze the values for $\lambda \geq 3 0 0$ the number of not served requests increases, on average, by 7 times when the static policy is considered instead of the dynamic one.

Table 5. Dynamic vs. static policy: number of not served requests

| λ | #dynamic | #static |
| --- | --- | --- |
| 100 | 0.00 | 1.40 |
| 200 | 3.20 | 62.80 |
| 300 | 19.40 | 193.60 |
| 400 | 38.20 | 329.40 |
| 500 | 79.60 | 501.80 |

In Table 6 we report the average distance traveled to serve a request when the dynamic policy (column 2) and the static policy (column 3) are applied, respectively. By analyzing the results it is evident how, independently of the value of λ, the dynamic policy leads to a more efficient transportation system: the gap between the values in columns 2 and 3 is, on average, 9.49%.

Table 6. Dynamic vs. static policy: average distance traveled per served request

| λ | $l_{dynamic}$ | $l_{static}$ | gap(%) |
| --- | --- | --- | --- |
| 100 | 799.14 | 898.10 | 12.38 |
| 200 | 494.62 | 536.41 | 8.45 |
| 300 | 366.59 | 388.61 | 6.01 |
| 400 | 283.00 | 301.36 | 6.49 |
| 500 | 232.44 | 251.30 | 8.12 |

## Conclusions

In this paper we analyzed, from a management point of view, a dynamic environment for a carrier. The vehicles are equipped with communication devices that make it possible to a central control unit to evaluate in real-time new service requests and re-route the vehicles whenever beneficial. We tested different scenarios where each scenario is characterized by a different intensity of traffic. The first result we have obtained is that a reduction of the interval between two consecutive re-optimizations of the service from 1 h down to 30 s reduces the number of lost customers and the distance traveled. Thus, in all the subsequent experiments we have fixed the re-optimization interval to 30 s.

We then studied a number of different management policies a carrier may decide to follow to carry out the service to its customers. We analyzed the policies by evaluating two performance criteria: the number of lost customers and the distance traveled by the vehicles.

One of the management issues a carrier has to face is whether to give an immediate accept/reject answer to a service request on the basis of the previously accepted requests and the fleet of available vehicles or to accept all customers and, in case of need, to make use of a back-up company at a later time. The results of the experiments have shown that the latter policy is much more effective as the number of customer served by the vehicles of the carrier increases on average by more than 70% and the distance traveled increases only slightly.

It is well known that a large carrier can take advantage of its size to increase the average load of a vehicle and reduce the number of empty trips with respect to a smaller carrier. Small carriers are frequent in Europe and in Italy in particular. Small carriers may merge or at least implement a collaborative strategy to improve their overall performance. The comparison of the behavior of three carriers that own one vehicle each to the behavior of a hypothetical carrier that owns the three vehicles shows that a collaborative strategy dramatically increases the number of served customers and at the same time reduces the traveled distance.

Finally, we compared a dynamic environment with a static one. The dynamic environment requires investment costs in communication devices and a more complex and dynamic organization. Is it worthwhile? We have shown that the dynamic environment reduces the number of lost customers by almost an order of magnitude while reducing at the same time the traveled distance.

While in most cases a model and a solution algorithm for a routing problem are designed and tested with an operational point of view we have taken in this paper a managerial point of view and have provided, thanks to the availability of a software for the optimization of a dynamic routing environment, to quantify the advantages and disadvantages of different management policies.

## References

[1] E. Angelelli, N. Bianchessi, R. Mansini, and M.G. Speranza. Short term strategies for a dynamic multi-period routing problem. Quaderno di ricerca n. 278, Dipartimento Metodi Quantitativi, Università degli Studi di Brescia, 2007, to appear on Transportation Research Part C.

[2] E. Angelelli, M.W.P. Savelsbergh, and M.G. Speranza. Competitive analysis for dynamic multi-period uncapacitated routing problems. Networks, 49:308–317, 2007.

[3] E. Angelelli, M.W.P. Savelsbergh, and M.G. Speranza. Competitive analysis of a dispatch policy for a dynamic multi-period routing problem. Operations Research Letters, 35:713–721, 2007.

[4] M. Gendreau, F. Guertin, J-Y. Potvin, and E. Taillard. Parallel tabu search for real-time vehicle routing and dispatching. Transportation Science, 33:381–390, 1999.

[5] G. Ghiani, F. Guerriero, G. Laporte, and R. Musmanno. Real-time vehicle routing: Solution concepts, algorithms and parallel computing strategies. European Journal of Operational Research, 151:1–11, 2003.

[6] S. Ichoua, M. Gendreau, and J-Y Potvin. Diversion issues in real-time vehicle dispatching. Transportation Science, 34:426–438, 2000.

[7] O.B.G. Madsen, H.F. Ravn, and J.M. Rygaard. A heuristic algorithm for a dialride problem with time windows, multiple capacities and multiple objectives. Annals of Operations Research, 60:193–208, 1995.

[8] S. Mitrović-Minić, R. Krishnamurti, and G. Laporte. The double-horizon heuristic for the dynamic pickup and delivery problem with time windows. Transportation Research Part B, 38:669–685, 2004.

[9] S. Mitrović-Minić and G. Laporte. Waiting strategies for the dynamic pickup and delivery problem with time windows. Transportation Research Part B, 38:635–655, 2004.

[10] H.N. Psaraftis. Dynamic vehicle routing: Status and prospects. Annals of Operations Research, 61:143–164, 1995.

[11] H.N. Psaraftis. Dynamic vehicle routing problems. In B.L. Golden and A.A. Assad, editors, Vehicle Routing: Methods and Studies, pages 223–248. Elsevier Science, Amsterdam, 1998.

[12] M.W.P. Savelsbergh and M. Sol. Drive: Dynamic routing of independent vehicles. Operations Research, 46:474–490, 1998.

[13] J. Yang, P. Jaillet, and H. Mahmassani. Real-time multivehicle truckload pickup and delivery problems. Transportation Science, 38:135–148, 2004.

# Optimizing the Storage Area Dimension in a Production System

Luca Bertazzi

Department of Quantitative Methods, University of Brescia, Italy bertazzi@eco.unibs.it

**Summary.** We study the problem of determining the optimal dimension of a work-in-process storage area in a two-line production system with delays and breakdowns. We propose a stochastic model and prove theoretical results that allow us to implement an exact algorithm for the solution of the model. We optimally solve a real instance and carry out a sensitivity analysis to evaluate if the optimal solution is stable when the initial data are perturbed.

**Key words:** Production, Storage area, Stochastic models

## 1 Introduction

The problem of determining the right storage area dimension plays an important role in production systems. In fact, companies need to reduce costs, but at the same time to operate in markets that change every day and stimulate them to have a diversified and customer-oriented production. To operate in this way, a correct dimensioning of the storage areas and an efficient planning and scheduling are necessary. Serial production lines have been studied to find models for determining the right buffer dimension. The typical aim is to find rules for the storage space allocation (see [1, 2, 3, 4]). What we want to do is different: To develop a stochastic model that minimizes the sum of storage costs and of delay and break costs that occur during the process. The system we study is a two-line assembly production system, where a work-in-process storage area precedes the assembly stage. We solve a real instance provided by a primary company located in Brescia (Italy) and which is part of a multinational group which produces industrial vehicles. The production is customer-oriented: The daily production program is based on the demand of the customers. Each customer places an order to one of the dealers of the company; then, the dealer transfers the order to the commercial direction located in Turin (Italy), which sends it to the production service direction located in Brescia. Finally, in the production plant located in Brescia the order is transformed in an executive program. During this step, a storage space has to be allocated in order to guarantee a regular production at minimum cost.

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">L. Bertazzi et al. (eds.), Innovations in Distribution Logistics, Lecture Notes</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">in Economics and Mathematical Systems 619, DOI: 10.1007/978-3-540-92944-4,</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">-c 2009 Springer-Verlag Berlin Heidelberg</span></small>

The paper is organized as follow. In Sect. 2 the problem is described and formulated. In Sect. 3 an exact algorithm is proposed and some particular cases are analyzed. Finally, in Sect. 4 the real instance is optimally solved and a sensitivity analysis is carried out.

## 2 Problem Description and Formulation

The production plant located in Brescia is a two-line production system that produces specific components of industrial vehicles (see Fig. 1). Line 1 produces chassis, while line 2 produces cabs. Each item produced by line 1 is matched with a specific item produced by line 2. Line 1 is affordable, while line 2 has two types of problems: First, the items can take longer time than their scheduled time to finish their processing cycle, whenever the items are not conform to the assigned quality standards. Second, breakdowns may happen. Since any delay in line 2 can stop the production process, a work-in-process storage area is made available in line 2.

![](images/page_25_image_6.jpg)

Fig. 1. The production system

Our aim is to determine the right dimension of this storage area. It is necessary to balance the opposite effects of different cost components. In fact, there is not only the inventory cost, but also the penalty cost due to a wrong dimension of the storage area. Our aim is to find the dimension of the storage area that minimizes the expected total cost $E ( C )$ , given by the sum of the investment cost I and the expected operative cost $E ( O )$ . The investment cost is deterministic, while the expected operative cost, which depends on the break probability, can be expressed as follows. Let R be the break event and $\bar { R }$ be the complementary no-break event, $p ( R )$ be the probability that a break occurs during the production, $p ( \bar { R } )   =   1   -   p ( R )$ be the probability that nobreak occurs during the production, $E ( c | R )$ be the expected cost if there is a break in one of the machines and $E ( c | \bar { R } )$ be the expected cost in the opposite case. Then,

$$
E (O) = E (c | \bar {R}) p (\bar {R}) + E (c | R) p (R),
$$

where the expected break cost $E ( c | R )$ is the sum of the cost for production loss $( P L )$ of the expected cost for delay $E ( D | R )$ and the expected cost at the restart of the production $E ( S | R )$ . Therefore, the optimization model can be written in compact form as follows:

$$
\min _ {x} I + E (c | \bar {R}) p (\bar {R}) + [ P L + E (D | R) + E (S | R) ] p (R),\tag{1}
$$

where each cost component depends on the dimension x of the storage area expressed in terms of number of hours of stock. Our aim is to find the value of x that minimizes the total expected cost $E ( C )$ . Let us now formulate each cost component.

## 2.1 Investment Cost

Every node in a production process implies an investment cost for establishment and for development. When the node is a storage area, the investment cost is related to the dimension of the area. If $C _ { 0 }$ denotes the investment cost of one unit of storage area per year, then the total investment cost is:

$$
I = C _ {0} x.
$$

## 2.2 Expected Operative Cost

The expected operative cost $E ( O )$ is composed of two different cost components, the first depending on the delays and the second on the breaks occurred during the production.

## Expected No-Break Cost

The first component of the expected operative cost is the so called expected no-break cost (or failed sequence cost). This cost is generated when an item takes longer time than its scheduled time to finish its processing cycle. This can happen when the item is not conform to the assigned quality standards and, therefore, it has to be corrected to attain the desired level. These corrections break the planned production sequence. Therefore, two situations can happen: Either the late-comer item has a delay not greater than the dimension of the storage area (in hours) or it has a delay greater than it. In the former case, the item becomes available in time to be matched with its complementary and therefore the corresponding no-break cost is equal to zero. In the latter case, the item cannot be matched with its complementary in the production line and therefore it must be driven out of the production line. Additional working time is necessary to match it with its complementary and therefore a no-break cost is charged. Let $k = 1 , 2 \ldots , \beta$ be the number of late-comer items per production hour, $h$ be the number of working hours per day, $\delta$ be the number of working days per year, $p ( k | \bar { R } )$ be the probability to have $k$ late-comer items per hour, given that the no-break event occurs, and $C _ { 1 }$ be the unit cost to match one late-comer item with its complementary out of the production line. Then, the expected no-break cost can be expressed as:

$$
E (c | \bar {R}) = \sum_ {k = 1} ^ {\beta} E (c | k, \bar {R}) p (k | \bar {R}),
$$

where $E ( c | k , \bar { R } )$ is the expected cost to have k late-comer items per hour. Let $r =$ $1 , 2 , \ldots , \alpha$ be the number of hours of delay. Then, if $E ( c | r , k , \bar { R } )$ is the expected cost to have r hours of delay and k late-comer items, then $E ( c | k , \bar { R } )$ can be expressed as:

$$
E (c | k, \bar {R}) = \sum_ {r = 1} ^ {\alpha} E (c | r, k, \bar {R}) p (r | k, \bar {R}),
$$

which is equal to

$$
E (c | k, \bar {R}) = C _ {1} k h \delta \sum_ {r = x + 1} ^ {\alpha} p (r | k, \bar {R}),
$$

as $E ( c | r , k , \bar { R } )$ is equal to 0 for $1   \leq   r   \leq   x$ and to $C _ { 1 } k h \delta$ for $x   <   r   \leq   \alpha$ , because it does not depend on the number of hours of delay. If we denote by $p ( r i t > x | k , \bar { R } ) =$ $\begin{array} { r } { \sum _ { r = x + 1 } ^ { \alpha } p ( r | k , \bar { R } ) } \end{array}$ , the expected no-break cost is:

$$
E (c | \bar {R}) = C _ {1} h \delta \sum_ {k = 1} ^ {\beta} k p (r i t > x | k, \bar {R}) p (k | \bar {R}).\tag{2}
$$

## Expected Break Cost

There is a break cost when an R event happens. This type of events are often caused by breakdowns. In this case, the main problem is not due to costs, but to the fact that the production process is stopped. This type of events would be really catastrophic if there are not sufficient stocks that make possible to go ahead with the production until the failed process restarts. The expected break cost is the sum of the following three components:

## 1. Cost for production loss

The cost for production loss represents the most evident effect of a breakdown. If there is no storage area or it is not adequate, there is a clear loss of added value. If $C _ { 2 }$ denotes the added value of one hour of production, then the cost per production loss is:

$$
P L = C _ {2} \delta \max (\alpha - x, 0).
$$

## 2. Expected cost for delay

There is a cost for delay when, in the case of a break, an inadequate storage area makes not possible to restore the right sequence in the production. Let n, with $n = 1 , 2 , \ldots , x ,$ be the index of the hours of items in the storage area. It represents the numbers of hours the corresponding items remain in the storage area before matching their complementary items.

Consider first the case with $x \leq \alpha .$ For each $n , k$ of the corresponding items, with $k = 1 , 2 , \ldots , \beta$ and probability $p ( k | R )$ , can be in the storage area just to replace late-comer items. If the delay of the corresponding late-comer items is greater than n, these items cannot be replaced in time and therefore must be matched with their complementary items out of the production line. This happens with probability $\begin{array} { r } { p ( r i t > n | k , R ) = \sum _ { r = n + 1 } ^ { \alpha } p ( r | k , \bar { R } ) } \end{array}$ . Therefore, if $x \leq \alpha$ , the expected cost for delay is:

$$
E (D | R) = C _ {1} \delta \sum_ {n = 1} ^ {x} \sum_ {k = 1} ^ {\beta} k p (r i t > n | k, R) p (k | R) \quad x \leq \alpha .
$$

Consider now the case with $x \; > \; \alpha .$ . In this case, the items corresponding to $n = 1 , 2 \ldots , x   -   \alpha$ are already in the right sequence. Instead, for each $n = x - \alpha +$ $1 , \ldots , x , k$ of the corresponding items, with $k = 1 , 2 , \ldots , \beta$ and probability $p ( k | R )$ respectively, can be in the storage area just to replace late-comer items. If the delay of the corresponding late-comer items is greater than n, these items cannot be replaced in time and therefore must be matched with their complementary items out of the production line. This happens with probability $p ( r i t > n | k , R ) =$ $\begin{array} { r } { \sum _ { r = n + 1 } ^ { \alpha } p ( r | k , \bar { R } ) } \end{array}$ . Therefore, if $x > \alpha$ , the expected cost for delay is:

$$
E (D | R) = C _ {1} \delta \sum_ {n = x - \alpha + 1} ^ {x} \sum_ {k = 1} ^ {\beta} k p (r i t > n | k, R) p (k | R) \quad x > \alpha .
$$

## 3. Expected cost at the restart

At the restart of the production, another type of cost has to be charged. In fact, after the stop of the production, the number of hours of stock in the storage area is too small to restore the right sequence in the production. This cost has to be charged until the storage area is full. Since $\gamma$ hours of production are needed to recover one hour of stock, the expected cost at the restart is equal to the expected cost for delay multiplied by $\gamma ,$ that is:

$$
E (S | R) = \gamma E (D | R).
$$

## 3 Determining the Optimal Stock Dimension

In this section we propose an exact algorithm to solve the stochastic model described above. Let us first prove the following results.

**Lemma 1.** $p ( r i t >   x | k , \bar { R } )$ is a decreasing function in x for $1 \leq x <$ α and $p ( r i t >$ $x | k , \bar { R } ) = 0   f _ { } { o r } \; x \geq \alpha .$

Proof. We know that $\begin{array} { r } { \sum _ { r = 1 } ^ { \alpha } p ( r | k , \bar { R } ) \; = \; 1 } \end{array}$ . Therefore, since $p ( r i t \; > \; 1 | k , \bar { R } ) \; = \; 1 \; -$ $p ( 1 | k , \bar { R } )$ and $p ( r i t   >   x | k , \bar { R } )   =   p ( r i t   >   x   -   1 | k , \bar { R } )   -   p ( x | k , \bar { R } )$ for $1   <   x   <   \alpha ,$ then $p ( r i t > x | k , \bar { R } )$ is a decreasing function in x for $1 \leq x < \alpha$ , and $p ( r i t > x | k , \bar { R } ) = 0$ for $x \geq \alpha .$

The following corollary holds.

**Corollary 1.** $E ( c | \bar { R } )$ is a decreasing function in x for $1 \leq x < \alpha$ and $E ( c | \bar { R } ) = 0   f o r$ $x \geq \alpha .$

Lemma 2. $\textstyle \sum _ { n = x - \alpha + 1 } ^ { x } p ( r i t > n | k , R )$ is a decreasing function in x for $\alpha < x < 2 \alpha - 1$ and is equal to 0 for $x \geq 2 \alpha - 1$

Proof. For $\begin{array} { r } { x = \alpha + 1 , \sum _ { n = x - \alpha + 1 } ^ { x } p ( r i t > n | k , R ) = p ( r i t > 2 | k , R ) + p ( r i t > 3 | k , R ) + \ldots + p ( r i t > n | k , R ) } \end{array}$ $\begin{array} { r } { p ( r i t > \alpha | k , R ) + p ( r i t > \alpha + 1 | k , R ) . \; \mathrm { F o r } \; \alpha + 1 < x < 2 \alpha , \sum _ { n = x - \alpha + 1 } ^ { x } p ( r i t > n | k , R ) = 0 . } \end{array}$ $\begin{array} { r } { \sum _ { n = ( x - 1 ) - \alpha + 1 } ^ { x } p ( r i t > n | k , R ) - p ( r i t > x - 1 | k , R ) } \end{array}$ . Since $p ( r i t > s | k , R ) = 0 \; \mathrm { f o r } \; s \geq \alpha ,$ then $\textstyle \sum _ { n = x - \alpha + 1 } ^ { x } p ( r i t > n | k , R )$ is a decreasing function in $x$ for $\alpha < x < 2 \alpha - 1$ and it is equal to 0 for $x \geq 2 \alpha - 1$

The following corollary holds.

**Corollary 2.** E(D|R) = 0 and $E ( S | R ) = 0 \; f o r \; x \geq 2 \alpha - 1$

The previous results allow us to prove the following theorem.

**Theorem 1.** Any dimension of the storage area $x > 2$ α cannot be optimal.

Proof. For $x \geq 2 \alpha$ , the expected no-break cost $E ( c | \bar { R } ) \; = \; 0$ thanks to Corollary 1, the cost for production loss $P L   =   0$ by definition and the expected cost for delay $E ( D | R )   =   0$ and the expected cost at the restart $E ( S   | R ) =   0$ thanks to Corollary 2. Therefore, since the total cost corresponding to $x \geq 2 \alpha { \mathrm { ~ i s ~ } } C _ { 0 } x ,$ any solution $x > 2 \alpha$ is dominated by $x = 2 \alpha$

Given Theorem 1, the optimal dimension of the storage area $x ^ { * }$ can be obtained by complete enumeration of the integer values of x in the interval [1, 2α].

## Analysis of Particular Cases

To complete our analysis, we now study some particular cases, interesting from the practical point of view.

## a) Standard Production Systems

The model studied in the previous section considers a production system with a customer-oriented production. Therefore, each item processed in the line 1 has to be matched to the corresponding item processed in the line 2. Let us now consider the case in which the production is standardized. In this case, the model becomes simpler, because the investment cost I and the cost for loss production $P L$ only are included in the objective function.

**Theorem 2.** In any standard production system, any dimension of the storage area $x > \alpha$ cannot be optimal. Moreover, $i f C _ { 2 } > C _ { 0 }$ , then $x ^ { * } = \alpha ;$ otherwise, $x ^ { * } = 1$

Proof. For $x \; \geq \; \alpha ,$ the investment cost $I \; = \; C _ { 0 } x$ and the cost for production loss $P L = 0$ by definition. Therefore, since the total cost is $C _ { 0 } x _ { 1 }$ then any solution $x > \alpha$ is dominated by $x \; = \; \alpha .$ . Consider now any solution $1 \; \leq \; x \; \leq \; \alpha .$ The total cost is $C _ { 0 } x   +   C _ { 2 } ( \alpha   -   x )$ . Therefore, if $C _ { 2 } > C _ { 0 }$ , then the optimal solution is $x ^ { * } = \alpha$ , otherwise it is $x ^ { * } = 1$

## b) No-Break Systems

Consider now the case in which there are no process stops caused by a break, but only delays due to products not conform to the assigned quality standard. In this case, the investment cost I and the expected no-break cost $E ( c | \bar { R } )$ only are included in the objective function.

**Theorem 3.** In any no-break system, any dimension of the storage area $x > \alpha$ cannot be optimal.

Proof. For $x ~ \geq ~ \alpha$ , the investment cost $I \; = \; C _ { 0 } x$ and the expected no-break cost $E ( c | \bar { R } )   =   0$ . Therefore, since the total cost is $C _ { 0 } x _ { 1 }$ any solution $x > \alpha$ is dominated by $x = \alpha .$

## 4 Computational Results

In this section we apply the exact algorithm developed in the previous section to solve the real instance. Let us first list the data of this instance:

\- Maximum number of hours of delay α: $6 ;$

\- Maximum number of late-comer items per production hour $\beta ; 6$ ;

\- Investment cost of one unit of storage area per year $C _ { 0 } { : } ~ 8 { , } 3 0 0$ Euro;

Unit cost to match one late-comer item with its complementary out of the production line $C _ { 1 } ; 2 1 7$ Euro;

\- Added value of one hour of production $C _ { 2 }$ : 116,203 Euro;

\- Number of working hours per day h: 16;

\- Number of working days per year δ: 225;

\- Number of hours to obtain 1 h of stock γ: 5;

Probability that a break occurs in the process p(R): 3.1%;

Distribution of late-comer items:

| Late-comer items | Cases | Frequency(%) |
| --- | --- | --- |
| 1 | 3 | 9.4 |
| 2 | 4 | 12.5 |
| 3 | 5 | 15.6 |
| 4 | 6 | 18.8 |
| 5 | 8 | 25.0 |
| 6 | 6 | 18.8 |
|  | 32 | 100 |

This distribution has been obtained on the basis of historical data. We assume that both the probability $p ( k | R )$ of having k late-comer items given that there is a break and the probability $p ( k | \bar { R } )$ of having k late-comer items given there is no a break are equal to the frequency of having k late-comer items.

Distribution of hours of delay:

| Hours of delay | Cases | Frequency(%) |
| --- | --- | --- |
| 1 | 1 | 6.3 |
| 2 | 2 | 12.5 |
| 3 | 2 | 12.5 |
| 4 | 3 | 18.8 |
| 5 | 5 | 31.3 |
| 6 | 3 | 18.8 |
|  | 16 | 100 |

This distribution has been obtained on the basis of historical data. We assume that the probability $p ( r | k , \bar { R } )$ of having a delay equal to r given that there are k late-comer items and no break is equal to the frequency of having a delay equal to r.

Table 1 shows the application of the exact algorithm to the real instance. It is organized as follows. Column 1 gives the dimension of the storage area, column 2 the corresponding investment cost, column 3 the corresponding expected no-break cost, column 4 the corresponding cost for production loss, column 5 the corresponding expected cost for delay, column 6 the corresponding expected cost at the restart and, finally, column 7 the corresponding expected total cost.

The optimal solution corresponds to a dimension of the storage area of 10 h, with a total expected cost of 89,704.66.

Table 1. Iterations in the solution algorithm

| x | I | E(c\|R) | PL | E(D\|R) | E(S\|R) | E(C) |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 8,300.00 | 2,883,726.56 | 130,728,375.00 | 180,232.91 | 901,164.55 | 6,888,733.98 |
| 2 | 16,600.00 | 2,499,229.69 | 104,582,700.00 | 336,434.77 | 1,682,173.83 | 5,742,994.13 |
| 3 | 24,900.00 | 2,114,732.81 | 78,437,025.00 | 468,605.57 | 2,343,027.83 | 4,592,784.51 |
| 4 | 33,200.00 | 1,537,987.50 | 52,291,350.00 | 564,729.78 | 2,823,648.93 | 3,249,581.48 |
| 5 | 41,500.00 | 576,745.31 | 26,145,675.00 | 600,776.37 | 3,003,881.84 | 1,522,626.54 |
| 6 | 49,800.00 | 0.00 | 0.00 | 600,776.37 | 3,003,881.84 | 161,544.40 |
| 7 | 58,100.00 | 0.00 | 0.00 | 420,543.46 | 2,102,717.29 | 136,321.08 |
| 8 | 66,400.00 | 0.00 | 0.00 | 264,341.60 | 1,321,708.01 | 115,567.54 |
| 9 | 74,700.00 | 0.00 | 0.00 | 132,170.80 | 660,854.00 | 99,283.77 |
| 10 | 83,000.00 | 0.00 | 0.00 | 36,046.58 | 180,232.91 | 89,704.66 |
| 11 | 91,300.00 | 0.00 | 0.00 | 0.00 | 0.00 | 91,300.00 |
| 12 | 99,600.00 | 0.00 | 0.00 | 0.00 | 0.00 | 99,600.00 |

## Sensitivity Analysis

Our aim is now to evaluate if the optimal dimension of the storage area $x ^ { * }   =   1 0$ h is stable when the initial data are perturbed. The sensitivity analysis we carry out is based on the variation of one parameter at a time in a given interval. The results are shown in Tables 2 and 3. Table 2 is organized as follows. Columns 1–2 show the results obtained when the investment cost of one unit of storage area per year $C _ { 0 }$ is modified from 0 to 20,000. Columns 3–4 show the results obtained when the unit cost to match one late-comer item with its complementary out of the production line $C _ { 1 }$ is modified from 0 to 400. Columns 5–6 show the results obtained when the added value of 1 h of production $C _ { 2 }$ is modified from 0 to 400,000. Finally, the columns 7–8 show the results obtained when the probability that a break occurs $p ( R )$ is modified from 0 to 10%.

The results show that the optimal solution is equal to 10 for values of $C _ { 0 }$ between 7,000 and 17,000, while it increases to 11 for values lower than 7,000 and reduces to 9 for values grater than 17,000. The optimal solution is equal to 10 for $C _ { 1 }$ between 120 and 260, while it reduces up to 6 for values lower than 120 and increases to 11 for values grater than 260. The optimal solution does not vary when the added value of 1 h of production $C _ { 2 }$ is modified. Finally, the optimal solution is equal to 10 for values of $p ( R )$ between 1.5 and 3.5%, while it reduces up to 6 for values lower than 1.5% and increases to 11 for values grater than 3.5%.

Table 3 shows the results obtained by varying the distribution probabilities of both late-comer items and of the hours of delay. For the late-comer items, one thousand distribution probabilities have been generated in the following way. Given a maximum number $a$ of late-comer items, the number of cases for each number $k = 1 , 2 , \ldots , 6$ of late-comer items has been randomly generated as an integer number between 0 and a on the basis of a uniform distribution. For the hours of delay, one thousand distribution probabilities have been generated in the following way. Given a maximum number $b$ of late-comer items, the number of cases for each number $r = 1 , 2 , \ldots , 6$ of hours of delay has been randomly generated as an integer number between 0 and b on the basis of a uniform distribution. Table 3 is organized as follows. Column 1 gives the optimal dimension $x ^ { * }$ of the storage area. Columns 2, 3 and 4 show, for each value of $x ^ { * }$ , the percentage of times this value has been the optimal one in the one thousand instances generated with $a = 4$ and b = 3, $a = 8$ and $b = 5$ and, finally, $a = 1 6$ and $b = 1 0$ , respectively.

Table 2. Sensitivity analysis: varying costs and probability of break

| $C_0$ | $x^*$ | $C_1$ | $x^*$ | $C_2$ | $x^*$ | p(R)(%) | $x^*$ |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 11 | 0 | 6 | 0 | 10 | 0.0 | 6 |
| 1,000 | 11 | 20 | 6 | 20,000 | 10 | 0.5 | 6 |
| 2,000 | 11 | 40 | 6 | 40,000 | 10 | 1.0 | 8 |
| 3,000 | 11 | 60 | 7 | 60,000 | 10 | 1.5 | 10 |
| 4,000 | 11 | 80 | 9 | 80,000 | 10 | 2.0 | 10 |
| 5,000 | 11 | 100 | 9 | 100,000 | 10 | 2.5 | 10 |
| 6,000 | 11 | 120 | 10 | 120,000 | 10 | 3.0 | 10 |
| 7,000 | 10 | 140 | 10 | 140,000 | 10 | 3.5 | 10 |
| 8,000 | 10 | 160 | 10 | 160,000 | 10 | 4.0 | 11 |
| 9,000 | 10 | 180 | 10 | 180,000 | 10 | 4.5 | 11 |
| 10,000 | 10 | 200 | 10 | 200,000 | 10 | 5.0 | 11 |
| 11,000 | 10 | 220 | 10 | 220,000 | 10 | 5.5 | 11 |
| 12,000 | 10 | 240 | 10 | 240,000 | 10 | 6.0 | 11 |
| 13,000 | 10 | 260 | 10 | 260,000 | 10 | 6.5 | 11 |
| 14,000 | 10 | 280 | 11 | 280,000 | 10 | 7.0 | 11 |
| 15,000 | 10 | 300 | 11 | 300,000 | 10 | 7.5 | 11 |
| 16,000 | 10 | 320 | 11 | 320,000 | 10 | 8.0 | 11 |
| 17,000 | 10 | 340 | 11 | 340,000 | 10 | 8.5 | 11 |
| 18,000 | 9 | 360 | 11 | 360,000 | 10 | 9.0 | 11 |
| 19,000 | 9 | 380 | 11 | 380,000 | 10 | 9.5 | 11 |
| 20,000 | 9 | 400 | 11 | 400,000 | 10 | 10.0 | 11 |

The results show that the dimension of 10 has been the optimal one in more than 50% of the instances for each of the combinations of a and $b$ .

The conclusion of the sensitivity analysis is that the optimal dimension of 10 is stable when the initial data are perturbed.

Table 3. Sensitivity analysis: varying distribution probabilities

| $x^{*}$ | (4,3)(%) | (8,5)(%) | (16,10)(%) |
| --- | --- | --- | --- |
| 1 | 0.00 | 0.00 | 0.00 |
| 2 | 0.00 | 0.00 | 0.00 |
| 3 | 0.00 | 0.00 | 0.00 |
| 4 | 0.00 | 0.00 | 0.00 |
| 5 | 0.00 | 0.00 | 0.00 |
| 6 | 0.10 | 0.00 | 0.00 |
| 7 | 0.50 | 0.60 | 0.30 |
| 8 | 5.10 | 5.20 | 3.90 |
| 9 | 24.00 | 25.10 | 25.00 |
| 10 | 51.20 | 50.20 | 53.50 |
| 11 | 19.10 | 18.90 | 17.30 |
| 12 | 0.00 | 0.00 | 0.00 |

## Conclusions

We studied the problem of determining the optimal dimension of a work-in-process storage area in a two-line production system with delays and breakdowns. The stochastic model and the algorithm we proposed allowed us to exactly solve the real instance with a stable solution and can be easily extended to solve more general two-line production systems.

## Acknowledgements

The author wishes to acknowledge the contribution of Marco Bertella at an early stage of this paper and the useful suggestions of Maria Grazia Speranza that allowed to improve the paper.

## References

[1] Conway, R., Maxwell, W., McClain, J.O., Thomas, L.J. (1988), The Role of Work-In-Process Inventory in Serial Production Lines, Operations Research 2, 229–241.

[2] Hillier, F.S., So, K.C., Boling, R.W. (1993), Toward Characterizing the Optimal Allocation of Storage Space in Production Line Systems with Variable Processing Times, Management Science 39, 126–133.

[3] Papadopoulos, H.T., Vidalis, M.I. (1998), Optimal Buffer Storage Allocation in Balanced Reliable Production Lines, International Transactions in Operational Research 5, 325–339.

[4] So, K.C. (1997), Optimal buffer allocation strategy for minimizing workin-process inventory in uncapacitated production lines, IIE Transactions 29, 81-88.

# On-line Routing per Mobile Phone: A Case on Subsequent Deliveries of Newspapers

Thomas Bieding1, Simon Görtz2, and Andreas Klose<sup>3</sup>

1 Vodafone D2 GmbH, Germany thomas.bieding@vodafone.com

2 Faculty of Economics and Social Sciences, University of Wuppertal, Germany simon.goertz@wiwi.uni-wuppertal.de

3 Department of Mathematical Sciences, University of Aarhus, Denmark aklose@imf.au.dk

**Summary.** On-line routing is concerned with building vehicle routes in an on-going fashion in such a way that customer requests arriving dynamically in time are efficiently and effectively served. An indispensable prerequisite for applying on-line routing methods is mobile communication technology. Additionally it is of utmost importance that the employed communication system is suitable integrated with the firm’s enterprise application system and business processes. On basis of a case study, we describe in this paper a system that is cheap and easy to implement due to the use of simple mobile phones. Additionally, we address the question how on-line routing methods can be integrated in this system.

**Key words:** On-line and dynamic vehicle routing, Mobile communication, Mobile business and solutions

## 1 Introduction

On-line routing is concerned with building vehicle routes in an on-going fashion in such a way that customer requests arriving dynamically in time are efficiently and effectively served. Although dynamic routing problems and quantitative methods for on-line routing have been discussed in the scientific literature since a seminal paper of Psaraftis [21], the technology required for implementing on-line dispatching of vehicles was till recently not available at a cost allowing a widespread use. An indispensable prerequisite for applying on-line routing methods is mobile communication technology. Drivers must be timely informed about the next stop to approach; the dispatching centre must be informed about the driver’s location and the status of the delivery. The availability of a mobile communication system alone is, however, not sufficient. It is important that the communication system is properly interfaced with the firm’s IT system, enterprise applications and data bases. A suitable hardware and software solution for interconnecting enterprise applications and the mobile communication system should also allow to easily integrate on-line routing algorithms.

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">L. Bertazzi et al. (eds.), Innovations in Distribution Logistics, Lecture Notes</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">in Economics and Mathematical Systems 619, DOI: 10.1007/978-3-540-92944-4,</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">-c 2009 Springer-Verlag Berlin Heidelberg</span></small>

In the information management area, the more general topic of integrating mobile co-workers in a firm’s IT system is also discussed under the buzzword of mobile business and mobile logistics (see, e.g., [32]). This paper describes a mobile business solution that heavily relies on the use of mobile phones and the wireless application protocol (WAP). An advantage of such a system is its low cost and its ease of use. Furthermore, integrating algorithms for on-line routing should be relatively straightforward. A case concerning the subsequent delivery of newspapers will serve as a base for illustrating the potential benefits of such a system. The next section details this case and Sect. 3 subsumes the case under the broader field of mobile business. Moreover, alternative mobile communication technologies are briefly described. Section 4 discusses then in some detail the above mentioned web/WAP-based mobile communication system, its benefits and potential drawbacks. Section 5 attends to the different decision problems arising when planning vehicle routes for subsequent newspaper delivery. A short overview of the literature on some methods for dynamic vehicle routing is given in Sect. 6. The discussion of these methods will reveal that there seems to be a gap between deterministic reoptimisation heuristics, on the one hand, and relatively simple dispatching rules based on queueing theory and stochastic arguments, on the other hand. Section 7 lists some further application examples. Finally, a summary and outlook is given in Sect. 8.

## 2 A Practical Case: Subsequent Deliveries of Newspapers

Distributing and selling magazines and newspapers is a difficult business. The competitive pressure is substantial, and publishing houses should achieve high print runs in order to earn some money. Subscribers that regularly receive a certain title are thus very important, and publishers usually invest a relatively large amount of money in trying to attract more subscribers. It is therefore important to keep these kind of customers.

The newspaper delivery is usually performed by third-party carriers. In case that a subscriber did not receive his accustomed, e.g., daily newspaper, he will complain about this at a call centre. The operator will then apologise for the inconvenience and assure subsequent delivery of the issue as fast as possible. Customer complaints arrive dynamically and have to be treated on additional delivery routes. For the case of a medium-sized regional newspaper publisher, the whole process of subsequent delivery can be described as follows.

1. A customer complains the non-delivered newspaper issue at the call centre.

2. The operator collects the case’s data and feeds them into a software system. The customer chooses between a voucher and a subsequent delivery of the missing issue.

<table><tr><td>medium</td><td colspan="6">process step</td></tr><tr><td>digital</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>facsimile</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>phone</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>leaflet</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td>customer</td><td>call center</td><td>local branch</td><td>driver</td><td>main centre</td><td>IT system</td></tr></table>

Fig. 1. Information transfer characterised by “media break”

3. In case the customer chooses a subsequent delivery, a corresponding delivery order is triggered. The order is transmitted by facsimile or phone to a local branch of the publisher. A printout of the order is made and handed to a driver that performs the delivery. Drivers that already started their delivery tours may then receive additional orders by trunking.

4. The driver notifies the publisher’s dispatching centre about the completed delivery, and an operator marks the order as completed in the firm’s software system.

The following figures underpin the dimension of the subsequent deliveries.

• The publisher distributes three local newspapers as well as one supra-regional newspaper in Germany.

Within the ordinary delivery process, local branches and driver sites are equipped with about 60 additional copies per driver for the purposes of potential subsequent deliveries.

Each driver executes, on average, 25 subsequent deliveries on each of the 280 delivery days per year. On a peak day, about more than 45 deliveries are performed by a driver.

Delivery drivers serve predefined delivery areas. A delivery tour starts in the morning and ends at midday. A driver either works as a freelancer or is employed by a carrier; his compensation depends on the time spent on delivery and the distance driven. The average distance of a delivery tour is about 20 km.

According to the firm’s actual figures, 26 drivers are in total daily employed for subsequent delivery. This amounts to 26 · 280 · 20 km = 145, 600 km spent on subsequent delivery per year.

Apparently, a relatively large number of different media (computer, facsimile, phone, paper, trunking) is used for the purposes of transferring information. The dashed line in Fig. 1 shows the status quo of information transmission characterised by a number of “media breaks”. Obviously, this kind of communication has a number of drawbacks:

• Permanent communication with the drivers is not possible.

Drivers cannot promptly notify the dispatching centre (main centre) about a completed delivery.

The dispatching centre has no ongoing information about the status of a delivery and the driver’s route.

• Due to the large number of different media used, the communication process is slow, costly and fault prone.

The solid line in Fig. 1 depicts an ideal state where all required information is centralised in a digital form from the point when a customer complaint arrives. Technologies as well as technical, managerial and organisational methods for achieving this degree of integration of mobile co-workers is a major concern of mobile business. The subject of mobile business and possible mobile communication solutions are briefly described in the next section. The mobile communication system should then allow to integrate the driver into the firm’s IT system, to streamline and centralise the information process and, finally, to integrate methods for performing the routing in some “intelligent way”.

## 3 Mobile Business and Mobile Communication Solutions

The integration of mobile technology into any kind of business process is called mobile business. Mobile business hence deals with the exchange of goods, services and information using mobile devices [35].

The use of mobile technologies emerges new business processes. These are characterised by mobility, reachability, localisation and personalisation. The user of a mobile device such as a mobile phone or a personal digital assistant (PDA) can access networks, products and services while on the move. This is important in context of the use of time critical information like news services or stock tickers. Mobile users can also be reached by other people and service providers regardless of place and time. This feature is especially vital to business processes that regularly need to reach their mobile workforce and pass them new tasks and instructions [23]. A person, who carries a mobile device which is on-line, can be localised. The ability to determine a location of a specific user is very important for location-sensitive services. Logistic companies may be interested in identifying the current position of a vehicle or determining a mobile co-worker who is the closest to the place of the latest customer’s request. In addition, a mobile user can also be identified; there is usually a one-to-one correspondence between a mobile device and the person who is carrying it.

Mobile business is based on network technologies, service technologies, mobile middleware and mobile devices as well as mobile localisation and personalisation technologies [34]. In the following, these mobile technologies are briefly described.

Wireless network technologies enable data transfer between devices which are not connected physically. They differ in transmission rate (bandwidth) and their suitability for mobile business application. Regional analogue systems for speech service were the first generation of mobile systems. The first standard based on digital signal transmission was the GSM (Global System for Mobile communication). This second generation (2G) is the starting point of the development of mobile business. In the meanwhile, GSM has spread in most countries. Its low transfer rate of 9.6 Kbps allows only simple applications like SMS, fax or voice mail [23]. The introduction of a faster network (2.5G) has allowed new services. The GPRS (General Packet Radio Service) can attain speeds up to 115 Kbps (theoretically up to 171 Kbps) and enables an ‘always-on’ connection between a mobile device and the network. The GPRS standard is a packet-switched protocol. Like the wired internet, data are split into parcels called packets, to which a unique address is appended. A mobile GPRS device uses network capacity only when packets are actually being sent or received although it is, in effect, permanently connected to the network. EDGE (Enhanced Data for GSM Evolution) is a faster version of GSM wireless service that enables data to be delivered at rates up to 384 Kbps. It is considered to be a 2.5G technology, although originally designed to evolve GSM to 3G [1]. The transfer rate is comparable to the speed that is offered by low-end ADSL services and could support even streaming short video clips and other multi media applications. Nevertheless, EDGE is an intermediate step to UMTS (Universal Mobile Telephone System). UMTS is counted to the third generation of mobile communication systems. This technology enables transfer rates up to 2 Mbps to stationary or mobile users but still rates up to 382 Kbps to fast moving users like drivers. UMTS promises a wide range of mobile business opportunities, including real-time applications, videoconferencing and massive volumes of transferred data. An alternative to UMTS is WLAN (wireless local area network) technology based on the IEEE 802.11 standard. The bit rates for the widespread 802.11g have gone up to 54 Mbps likely to be shared among 20–30 users. 802.11b enables a transfer rate of 11 Mbps. WLAN enables communication between devices equipped with a wireless network interface in the basic service set. This is the set of all stations that can communicate with each other. As long as a user is moving around within the basic service set he is still connected to the network.

Service technologies like SMS and WAP provide content and applications to mobile devices. SMS (Short Message Service) is a service available on most mobile devices as mobile phones, laptops, PDAs that permits the sending and receiving of short text messages. The length of the message is limited by the constraint of the signalling protocol to 140 bytes. This translates up to 160 characters. The WAP is a global standard for mobile communication and wireless connection to the internet. The restrictions of mobile phones and PDAs make it impossible to provide all services of computer based web browsers to mobile devices. Therefore, WAP browsers are designed to provide at least the basic services. Mobile internet sites are called WAP sites. They are written in, or dynamically converted to WML (wireless markup language). The mobile sites are accessed and interpreted via WAP browser and displayed on the mobile device. Although WAP is now the protocol used for almost all world’s mobile internet sites, some authors see the end of this technology [34].

Mobile middleware provides a way to connect and exchange information between mobile and stationary devices. It includes transmission technologies as well as special storage technologies. For example, Bluetooth is a radio standard and communication protocol designed for communication of mobile devices with each other, when they are in range up to 10 m. The used short-range radio frequency is secure and globally unlicensed. Money cards and GMS SIM cards (subscriber identity module) are so-called smart cards. These are pocket-sized cards with embedded integrated circuits. Most smart cards contain memory and microprocessor components and are capable of providing security services. These components allow to identify users.

Mobile localisation and personalisation technologies allow to provide geographic and personalised applications and services. The most important localisation technology is the Global Positioning System (GPS). It is a satellite navigation system based on 24 satellites. The transmitted signals allow GPS receivers to nearly determine the exact location and speed. GPS is free for everybody’s use. GPS-technology can easily be integrated in mobile devices. Personalisation technologies collect and provide information to tailor a mobile device application, which is personalised according to the interest of an individual or on user attributes such as role, field of work, or task lists.

Mobile business divides in two categories, mobile B2C (or m-commerce) and mobile solutions. Mobile solutions are used to re-engineer internal business processes [32]. There are two types of application areas: mobile Business-to-Machine and mobile Business-to-Employee (B2E). The first type comprises the controlling and monitoring of machines and plants; the latter the integration of mobile co-workers to the firm’s IT infrastructure. Horizontal mobile B2E solutions provide mobile access to standard applications such as groupware solutions. Vertical solutions are employed to improve specific business processes. The objective is a better integration of the mobile co-worker into the business process by means of data acquisition and transmission without media breaks. The opportunities and complexity of mobile technology is sufficient to create a mobile solution. The success of a mobile solution strongly depends on the software solution implemented to the mobile devices and middleware. A complete mobile business solution integrates mobile technology, applications and data base systems into the backend. This encloses the rules of data access and other security aspects, the management of data synchronisation between mobile devices and the firm’s backend, and the business logic [32]. The later is the core module of a mobile solution. Business logic deals with real life business objects. It handles the storage of objects, prescribes the interaction of different business objects and defines the routes and the methods by which business objects are accessed, updated and synchronised. Business logic comprises business rules and workflows. Hence, a mobile business solution is generally very complex and hard to achieve by means of standard tools and procedures. In many cases, it is necessary to develop and to implement customised solutions. The next section concretises a mobile solution developed for the case of subsequent newspaper delivery and some other “mobile re-engineering projects”.

## 4 A Web/WAP Based Mobile Communication System

This section describes a simply structured mobile communication system used in the case of subsequent newspaper delivery (see also [8]). Due to its ease of use and low cost, the system seems well-suited for small and medium-sized companies.

The system establishes an indirect communication channel between the dispatching centre and the mobile co-worker (driver) via a web and WAP server and mobile phones. Figure 2 shows the system’s general architecture. The structure shown in this figure is not exclusively related to the case of subsequent newspaper delivery but also applies to similar mobile business processes. The following parties are involved in the communication process: At a firm’s main centre, a central data base/ERP system is kept. The data base feeds a web and WAP server with required information and also extracts data from there. In case of the newspaper delivery example, the main centre is the firm’s main branch that is also responsible for dispatching vehicles. Decentralized co-workers may also be connected to the system via the web and WAP server. In contrast to mobile co-workers their location is fixed and they are connected using (non-mobile) remote access technology. In case of the newspaper example, there are no decentralized co-workers. There is, however, the call centre acting as a branch of the main centre and directly connected to its data base by means of remote intranet technology. Finally, there are the mobile co-workers sharing information with the other parties via the web and WAP server. In case of our example, the mobile co-workers are the drivers performing the subsequent delivery of newspapers. Which information is shared how and when between which actors will be explained later below, based on the case of subsequent newspaper delivery. Beforehand, it is shown how the mobile co-workers are integrated to the system.

Mobile co-workers are equipped with mobile devices. The device can be a notebook, PDA, or simply a cellular phone. The last device has a number of advantages in case that its display capabilities are sufficient for the application in question. The device is relatively cheap, most people are very familiar with it, and special agreements and contracts with the cellular radio provider allow to keep transmission costs very low. To this end, GPRS is used for transmitting data. In case of this technique, transmission costs depend on the volumes of transmitted data. Hence, a permanent connection between the mobile co-worker and the central web server can be established, whereas the conventional GSM technology uses a time-based billing system.

For accessing and viewing web pages, the mobile phone must be WAP enabled. A web server as well as a WAP server are then used for processing and answering requests sent by the mobile devices. These two kind of servers just provide different views on the same data extracted from the same data base. The servers are operated by an application service provider. Although the servers as well as other software tools (PERL, PHP) required for extracting information from the central data bases and building dynamic web pages are very cheap or even free software, operating and using such a system requires some expertise that a smaller firm possibly cannot acquire.

Sufficient security of a mobile co-worker’s access to the web/WAP server can be ensured in different ways. The mobile devices’ MAC addresses are registered at the server, and only registered devices may access the system. Additionally, authenticated access via a user name and password can be established. For the purposes of establishing secure data transmission, cellular radio providers furthermore offer VPN (“virtual private network”) tunnelling techniques. Access to the web/WAP server is then only granted via the provider’s VPN tunnel, and only calls approved by the provider’s radius server are put through. Moreover, the cellular phone’s identification number is then additionally transmitted for security reasons.

![](images/page_43_image_2.jpg)

Fig. 2. Components of the mobile communication system

Web pages are dynamically built using PHP (“hypertext preprocessor”). The required information (customer’s address, product demanded, time until delivery should be completed, additional short information regarding the customer and his location) is extracted from the main centre’s data base. The operators at the call centre who process the customer requests feed the data base with a customer’s data by means of the same familiar software system that the firm had used for these purposes since a long time. Different techniques can then be applied for transmitting the required data from the data base to the web server. The data base may be directly accessed using ODBC (“open data base connectivity”); the data may also be directly send via the hypertext transfer protocol (HTTP) and then extracted and processed by means of a PERL script. Other possible methods are to use the file transfer protocol (FTP) by first sending the data to a FTP server, or to send the data as a simple e-mail attachment. Privacy and data security is ensured by encryption and a secure socket layer connection.

The following example further illustrates the (real-time) communication between a driver and the central data base via the web/WAP server. Figure 3 shows the dispatching centre’s view on the system’s main page. The main page offers different options for further processing: Data may be downloaded again for further analysis using spreadsheet computation (e.g., for tracking arrival times, response times, actual tour duration, etc.) If necessary, additional customer requests may be entered manually (e.g., in case of missing or misentered data), and some functions for administering the system are provided. Most important is the information about customer requests/complaints of the current day. Figure 4 shows a fictive example of such a list. Customer requests are already assigned here to certain carriers that have to serve the request. The displayed information comprises: the carrier’s identification number; the customer’s id, name, address, and his demand; the time the request was posed; if and at which time the message was read by the driver, and the status of delivery. The driver has access to relevant parts of this information in a different form by means of a WAP enabled cellular phone. The information is displayed in two different forms. First, a simple list of all customer requests to be served by the driver is shown as in Fig. 5a. Each entry of this list just contains the customer’s address and the time the request was generated. Using the phone’s function keys, the driver can click on an entry in order to see all relevant information concerning the specific customer request (see Fig. 5b). After performing the delivery, the driver marks a request as completed in a similar simple way by just using the function keys of his mobile phone (Fig. 6). This information is promptly transferred back to the web/WAP server as well as the firm’s central data base, where now the customer request is marked as served (see Fig. 7). This way sufficient bidirectional and on-going communication between the dispatching centre and the drivers is established.

![](images/page_44_image_2.jpg)

Fig. 3. Dispatching centre’s view on the system’s main page<sup>∗</sup>

| *The main page’s menu shows the following entries: |
| --- |
| Order status |
| • Single delivery tour: → Display customer requests on a given tour assigned to certain carrier |
| Download |
| • Data: → Download data for spreadsheet access |
| System |
| • Administration: → Initialize test data; configure WAP display |
| • Input data: → Manually enter customer orders |

![](images/page_45_image_2.jpg)

Fig. 4. Dispatching centre’s view on the list of customer requests<sup>∗</sup>

The columns of the table displaying the customer requests show the following information: Carrier’s identification number (1); customer number (2); customer’s name (3) and address by street (4), zip code (5), and city (6); product demanded (7); date and time when the request was created (8); if the request was already read by the driver (9); date and time the request was read the last time (10); status of delivery completion (11).

It seems obvious that this kind of integrated mobile communication system has a number of advantages compared to the previously employed system, even without the incorporation of on-line routing algorithms. Especially, the following points can be raised:

![](images/page_46_image_2.jpg)

(a) Short list of customer orders by address and creation date and time

![](images/page_46_image_4.jpg)

(b) Detailed information on customer order: name, address, product demanded, creation date and time, time when delivery has to be completed, etc.

Fig. 5. Driver’s view on the list of customer requests and a single customer order

![](images/page_46_image_7.jpg)

(a)“Should the customer’s order be really marked as completed?”

![](images/page_46_image_9.jpg)

(b) “Order marked as completed. Continue”

Fig. 6. After delivery, customer requests are marked as completed

Drivers are not only informed about new orders; the required bidirectional communication is possible and customer orders are not only fulfilled but also digitally processed in an integrated way by the drivers.

• The aforementioned media breaks arising when transmitting information are reduced to a minimum.

• The driver’s actions are integrated in the firm’s IT system. The process of subsequent delivery is thereby accelerated and substantial time savings could be realised.

• Drivers get prompt information and are able to better plan next deliveries to be made.

• The system is very cheap and easy to use; drivers are very familiar with a cellular phone.

• Finally, the system is a prerequisite for implementing on-line routing algorithms.

![](images/page_47_image_2.jpg)

Fig. 7. Drivers actions are recorded and written back to the data base<sup>∗</sup> ∗ See Fig. 4 for a translation of the table’s columns.

## 5 Decision Problems to be Addressed

Which kind of subproblems arise when planning dynamic vehicle routes for subsequent newspaper delivery depends on the overall solution approach adopted. Moreover, the firm’s willingness and ability to implement organisational changes has to be taken into account. Currently, the firm predefines the drivers’ delivery areas, which generally favours a cluster first-route second approach. Especially, the following subproblems may then be distinguished:

1. Design of delivery areas,

2. Location planning,

3. Determining operating times,

4. Operational on-line routing.

Constraints to be taken into account are especially a minimum and maximum operating time of a route as well as a maximum allowed response time. A vehicle’s capacity does in this case not play any role. Obviously, the total time spent by the drivers must not exceed a given maximum. However, a too short route duration is also impractical; the earnings granted to a driver are then too low and no driver will like to operate such a route. The response time is the time that passed from the arrival of a customer request until its attendance. Short response times are part of a high customer service, but also very costly. A certain maximum response time must not be exceeded. Below this limit, the response time can be viewed as a soft constraint; attaining short response times is then more an objective than a constraint.

![](images/page_48_image_2.jpg)

Fig. 8. Prefixed delivery areas without (a) and with (b) “variable borders”

Objectives are more difficult to postulate than constraints. The problem is multi-objective in nature. Customer service and delivery costs have to be balanced, both the service dimension as well as the cost dimension are however difficult to measure. Moreover, the uncertainty of customer requests adds to the complexity of finding appropriate objectives, since in this case not only expected costs but also robustness of solutions is an issue. In order to obtain some operational objectives it is required to use some surrogate performance measures, which usually are (average) response time, travel distance and time, and the number of delivery tours.

In the sequel, the above mentioned subproblems are further described.

## 5.1 Design of Delivery Areas

When using a cluster first-route second approach, the first step consists in dividing the whole delivery area into a number of sub-areas that are then assigned to one or several drivers. Although customer requests arrive dynamically and are “stochastic”, the subscribers and their locations itself are of course known. Different alternative methods for obtaining reasonable clusters of subscribers might then be applied for defining delivery areas. Objectives to be taken into account are the minimisation of the number of required drivers as well as the minimisation of the (expected) travel times and distances.

Since customer requests arrive at random, it seems reasonable not to fully pre fix the delivery areas, but to allow exchanges of customer nodes at the “borders” of delivery areas as illustrated in Fig. 8. In Fig. 8a, the fixed areas result in an unfavourable dynamically emerging route for subregion B and some distances can be saved if “border customers” are exchanged between subregions as in Fig. 8b.

In both cases, the clustering will not be part of an on-line algorithm, but computed beforehand by means of a suitable method. Because, subscriber locations are known and also historical customer data can be made available, one might also take a two-stage stochastic programming approach for performing the clustering. The use of two-stage stochastic programs has already been proposed in the literature on stochastic vehicle routing problems [13, 27]. In our case, the first stage decisions would refer to the clustering, while second stage decisions would be the routing or, alternatively, in order to take the dynamically arriving customer demands better into account, recourse actions as, e.g., inserting a customer node in a route.

## 5.2 Location Planning

After completing a customer request, the driver has either to wait until he receives a new customer order or to finish his route and return to his home base. As already mentioned, reliable historical customer data is available in case of the subsequent newspaper delivery. Obviously, dynamic and stochastic routing problems have generally much in common, provided that dependable historical data is available.

Due to the probabilistic nature of a demand case, one might thus rise the question at which location a driver should wait for a next customer request. Possible alternative waiting points are, e.g.,

• A central point as, e.g., the median of the driver’s delivery area,

• The closest customer/subscriber location,

• The customer’s location with largest probability of a positive demand,

• A suitable customer location selected by considering a combination of the two criteria above.

Larsen et al.[17] investigate further possible rules on which such “repositioning decisions” might be based for the case of the “a priori travelling saleman problem with time windows”. The performance (average response time, travel distance and time, number of delivery tours) of different rules for driver repositioning should then be tested within simulation experiments using empirically validated assumptions regarding the customer arrival process.

## 5.3 Determining Operating Times

Neither the exact start and end times of a route are fixed nor is it required to start a route immediately after a customer request has arrived. Rather, it seems advisable to delay the start of a driver’s route in order to gather more information. There is obviously a trade-off between the customer service degree and the delivery costs if the routes’ start times are postponed. In case of the delivery area of Wuppertal, e.g., 80 % of all customer complaints are known until 10 AM; and 90 % are known until 11 AM. Moreover, routes computed on the base of full information are, on average, 30 % shorter than the routes that emerged dynamically. When delaying the start time of routes, a larger percentage of customer requests gets known in advance; this should allow to perform the routing in such a way that the drivers’s waiting and travel times as well as the distances driven are reduced compared to a situation where less information is available. On the other hand, delaying start times results of course in longer response times. Possible strategies for determining starting times are, e.g., to begin a route if a given percentage of the expected number of customer requests is known in advance. Simulation experiments should then be carried out in order to measure the performance (average response time, travel distance and time, number of delivery tours) of different rules for determining start times.

## 5.4 Operational On-Line Routing

The on-line routing consists in inserting dynamically arriving customer requests into one of the emerging routes in some “intelligent” or even “optimal” way. Section 6 describes some methods applicable to this purpose. The dynamic routing of customer requests can, e.g., be based on dynamic versions of standard (parallel) insertion procedures for the vehicle routing problem with time windows [20, 26], possibly followed by some post-optimisation of the customer sequences by means of, e.g., a Lin-Kernighan type local search heuristic [16, 18]. A reoptimisation is then triggered whenever a new customer request arrives. Again it might be useful not to directly communicate the resulting next stop to the driver, but to delay this decision for some time or as long as possible in order to gather more information.

For the purposes of the on-line routing, the mobile communication system has to be enhanced by a GPS as well as a GIS (“geographical information system”) component. The on-line routing requires information about the current position of the drivers. To this end, the drivers can, e.g, be equipped with GPS receivers. Although GPS technology works quite accurately, it is fault prone to some extend, and sometimes a GPS signal cannot be received due to some interferences. Recently, GPS devices are getting cheaper; but equipping every driver with such a device can still be a too large investment for a small firm. Nowadays, there are also cellular phones available that are equipped with an additional GPS module. The GPS device should, however, work as an automatic vehicle locating system [19] and be able to automatically send positioning information to the web/WAP server if a corresponding request was sent from the server to this device. A GPS system is, however, not a conditio sine qua non. The mobile communication system described above allows to locate the driver exactly, directly after fulfilment of a customer request. The drivers’ position between two customer nodes may then be simply estimated using appropriate measures of travel times and distances.

In addition, the customer locations must be geo-coded and travel distances and times need to be computed. Because the newspaper subscribers are known in advance, this task can be completed beforehand using, e.g, commercial geo-coding and route planning servers (see, e.g., [30]). Since in urban areas travel times can vary substantially, it can probably be necessary to use some on-line traffic information system (see, e.g., [11]) in order to obtain more accurate travel time information. On the other extreme, it might also be possible to work with a rather cheap solution that just uses “adjusted” Euclidean distances and travel time estimates in dependence of distances and time of day. Dillmann [9] and Dillmann et al. [10] report on good experiences with such a simplified approach.

Integrating the aforementioned mobile communication system and on-line routing algorithms is relatively straightforward. The algorithms can run on one or several servers in the background. The required input data is pushed forward from the web server whenever a new customer request arrives, and an algorithm’s results are written back to the web server.

## 6 Overview of Some Methods for On-Line Routing

This section briefly reviews some selected methods for on-line routing. Especially, relatively simple dispatching rules based on stochastic arguments are contrasted with “reoptimisation” procedures that do not include some kind of lookahead capability. Comprehensive surveys on methods for dynamic routing problems can be found in [14, 15, 21, 22]. Stochastic approaches to dynamic routing problems were proposed by Bertsimas and van Ryzin [4, 5], whilst a tabu search procedure of Gendreau et al. [12] as well as a column generation method of Savelsbergh and Sol [25] can be mentioned as representatives of the second group of methods.

## 6.1 Reoptimisation Approaches

Savelsbergh and Sol [25] propose a column generation approach to a dynamic version of the pickup-and-delivery problem. Column generation is used here to generate a number of feasible routes. The routes as well as the master problem are then reoptimised at fixed points in time during the working day, taking all known unfulfilled transportation requests and partial routes operated so far into account. The algorithm proposed by Savelsbergh and Sol uses heuristics to solve the pricing subproblems as long as this way columns of negative reduced cost can be found. An advantage of the column generation procedure is that a large number of alternative high quality routes is available, in which new transportation requests can then be inserted for the purposes of reoptimising the problem. Furthermore, in order to make feasible integral solutions more quickly available, primal heuristics are often invoked. The method is used for solving a dynamic pickup-and-delivery problem of a large carrier. The loads are relatively large and have to be transported over longer distances. It can thus be assumed that the number of requests that dynamically arrive per time unit is relatively small, which makes such a complex and computational demanding method as a column generation procedure feasible.

Gendreau et al. [12] propose a tabu search heuristic for (repeatedly) solving a dynamic vehicle routing problem with time windows. The procedure is based on the adaptive memory programming framework suggested by Rochat and Taillard [24] for the vehicle routing problem and by Taillard et al. [29] as a general unifying metaheuristic solution approach. The method first constructs I > 1 initial solutions using a randomised insertion procedure. Generated solutions are improved by means of a tabu search method, and the best solutions encountered so far are stored in a pool. New solutions are then constructed by recombining routes taken from the pooled solutions, completing the resulting partial solution to a route plan and reapplying the tabu search method. A parallel version of this method is implemented by simultaneously applying the tabu search to different initial solutions on different processors. In order to take the dynamics into account, the method runs in the background working on improving solutions as long as no new event (new customer order, completion of an order) occurs. If a new customer request arrives, the request is inserted into every solution of the solution pool; then a reoptimisation is triggered. In case that a customer order is completed, the information about the next stop of the best solution obtained so far is transmitted to the vehicle. An obvious advantage of this procedure is that, as in the case of the column generation method above, a number of diverse (and probably good) solutions is available, into which new customer orders can be inserted. Moreover, in this case, a feasible solution that can be used to dynamically dispatch the vehicles is always available. As a disadvantage of this method, the large requirements on computing power and computing equipment can be mentioned. Furthermore, as all kind of reoptimisation methods, the procedure does not include a lookahead capability that tries to take the stochastic nature of the problem into account.

## 6.2 Stochastic Approaches

Bertsimas and van Ryzin [4, 5] apply relatively simple rules for dispatching vehicles in case of a stochastic and dynamic vehicle routing problem. Bertsimas and Simchi-Levi [3] give a further brief overview of these methods. Swihart and Papastavrou [28] present a similar analysis of a single vehicle pickup and delivery problem. In [4], Bertsimas and van Ryzin consider the Travelling Repairman Problem, and in [5] they extend the analysis to the case of multiple and capacitated vehicles. The problem is modelled as a queueing system. To this end, it is assumed that customer requests arrive independently according to a Poisson process, that customer locations are uniformly distributed in a square region of the Euclidean plane, and that the objective is to minimise the customers’ total system time, which is the time elapsed between arrival of a demand and the time the server completes the service of the customer. Bertsimas and van Ryzin propose and analyse then a number of different dispatching rules and heuristics. For the case of a single uncapacitated vehicle they give the following heuristics and results:

1. In case of low traffic when the arrival rate approaches zero, the so-called stochastic median strategy (SQM) is optimal. The SQM strategy locates the server at the median of the region and serves the demand in a first come, first served (FCFS) order while returning to the median after each service.

2. A FCFS strategy that services the demands in the order in which they arrive is approximately 36 % above the optimum in case of light traffic.

3. The partitioning strategy extends the above simple rule by first dividing the service region into a number of equally sized subregions. The FCFS rule is then applied to each subregion. This heuristic gives a constant factor approximation in case of high traffic when the interarrival times approach the service times.

4. The travelling salesman (TS) strategy first waits until n customer requests have arrived and afterwards builds an optimal travelling salesman tour over these customers. Then this process is repeated. In case of high traffic and a suitable large value of n, the policy gives a better constant factor approximation than the partitioning strategy above.

5. An even better approximation is obtained in case of high traffic by means of spacefilling curves (SC). A spacefilling curve g is a continuous mapping of the interval $C   =   [ 0 , 1 )$ onto the unit square $S   =   C \times C$ such that $\| g ( a ) - g ( a ^ { \prime } ) \| \leq$ $2   \sqrt { | a - a ^ { \prime } | }$ for all $a , a ^ { \prime } \; \in \; C$ . The SC strategy maps the customer coordinates on the interval C, and then repeatedly visits dynamically arriving customers by sweeping the interval C in increasing order.

6. The simple “nearest neighbour” policy just services the closest available demand after every service completion. The method performed well within a number of simulation experiments performed by Bertsimas and Ryzin (note that the objective is to minimise the customers’ system time).

In [5], Bertsimas and van Ryzin analyse dispatching rules for the case of $m > 1$ vehicles as well for the case of a capacitated vehicle that can serve at most q customers. The heuristics below are proposed for the m vehicle case.

1. The m stochastic queue median policy extends the SQM strategy for a single vehicle by determining the m-median of the service region. Each vehicle returns then to the closest median after completing a single customer service. The policy is optimal in case of light traffic.

2. The randomised assignment strategy randomly assigns customer demands to each vehicle and then services each subprocess using a single server strategy.

3. The travelling salesman strategy waits as above until n customers have arrived. Then an optimal travelling saleman tour is built and the next available vehicle is used to serve the route. Routes are served according to the FCFS principle. The procedure’s performance factor depends on the number m of vehicles.

4. The modified travelling salesman strategy divides the service region into k subregions and applies the above TS strategy with parameter $n / k$ to each subregion. The procedure gives a constant factor approximation for the high traffic case.

5. The deterministic strategy works similar as the strategy above. The strategy collects however demands to routes for a given amount of time. Moreover, after a given amount of time has elapsed, the next subregion is served. The procedure has the same worst-case performance as the above TS strategy.

6. The independent partitioning policy divides the service region into m subregions and applies any of the single server strategies for each vehicle.

Finally, Bertsimas and van Ryzin consider the following methods for the case of a capacitated vehicle:

1. The qRP-strategy divides the service area into a given number of subregions. If q customer requests arrived in a certain subregion, the first available vehicle is used to serve these customers.

2. The qTP-strategy waits until $n \geq q$ customer requests have arrived. An optimal travelling salesman tour over the n customers is then partitioned into feasible vehicle routes.

An advantage of the above procedures is their simplicity and that they take account of the problem’s stochastic nature. Compared to reoptimisation procedures, the above rules seem, however, rather rigid and inflexible. The results of Bertsimas and van Ryzin depend furthermore on a number of limiting assumptions. It is questionable if the above approaches also perform reasonably good in case of non-Euclidean distances, non-uniformly distributed customers, non-Poisson arrival processes, and an objective that does not only consist in minimising the customers’ system time. Nevertheless, the above strategies may give some guidelines for adding lookahead capabilities to reoptimisation procedures, e.g., by means of locating one or more suitable waiting points in the service region. As already mentioned in Sect. 5.1, a further possible approach for including stochastic considerations might be to first build subregions or clusters of customers by means of a two-stage stochastic programming procedure with recourse, and then to apply a suitable dynamic reoptimisation heuristic to each cluster/subregion. A further way of exploiting stochastic information might also be the construction of a priori routes that are then used as guidelines for dynamically dispatching vehicles. Bertsimas [2] finds closed-form expressions for the expected length of the routes to be performed by a capacitated vehicle if a giant tour is already given and customer demands are stochastic. He also provides lower and upper bounds on an optimal a priori giant tour. Thomas and White [31] discuss “anticipatory route selection” as a further interesting idea for tackling the problem. A single uncapacitated vehicle performs pickups and deliveries, earning a reward for pickups and adding to the total cost when travelling. The probability that a customer requests a pickup depends on the time t. The problem is to determine a policy for selecting the next node to visit such that the expected total cost of a trip from an origin to the destination is minimised. The problem is formulated as a Markov decision process and some structural results concerning the cost function and optimal policy are presented. Moreover, for a few small examples the optimal anticipatory policy is computed by means of stochastic dynamic programming. The required computational effort is however far too large, which underpins the need for heuristic procedures for solving the stochastic dynamic program.

## 7 Further Application Areas

The depicted case of subsequent newspaper delivery is a neat example of a specific class of applications characterised by a relatively high degree of dynamics. On the one hand, it is not known when new customer complaints arrive; on the other hand, customer requests should be fulfilled quickly in order to achieve low response times. An on-line connection is thus needed for ensuring the required bidirectional exchange of information between dispatcher, mobile co-worker, and the data base backend. The WAP standard employed for this purpose shows furthermore the advantage that any mobile device supporting this protocol can be used without installing additional software on this device. A simple bookmark suffices to grant easy access to the server. A permanent connection between the server and the mobile devices must however be established.

A number of other mobile business cases show a much less degree of dynamics. The information required by the mobile co-workers is then known before start of their work. Hence, a connection between the mobile co-worker and the data base has just to be established on demand, e.g., for downloading data, updating status information on the data base server, updating data stored on the mobile device, uploading data to the data base after work finish. These kind of applications require specific pieces of software to be installed on the mobile devices itself.

A further application example of the web/WAP-based system of Sect. 4 is the recording and supervision of delivery times for press wholesalers and newspaper publishers. In this business, accurate information about delivery times and route durations is of vital importance for future planning. Bieding [6, 7] describes a JAVA based system that exploits the mobile communication system of Sect. 4 for this purpose. The system extends an older solution based on RFID technology and has successfully been used in practice for about 200 carriers. A specific software allowing to download the required data from the mobile devices during the delivery is installed on the cellular phones. Using this device, the driver confirms arrival and departure and only after this confirmation a status update is sent to the data base. An associated web application allows then to receive detailed information about the delivery times and offers several customised reports.

Private mail companies exploit a similar system for controlling their mail delivery [33]. Detailed information about mail still to be delivered is accessed by couriers via a cellular phone and the described web/WAP-based system. The couriers work in an off-line status; only in case of a status change, information is sent to the data base server. Status changes occur, e.g., in case of a successful delivery, in case that mail is returned to the sender, in case of a second delivery attempt, etc. The associated web application serves here more as an information tool. A further event management system based on a set of rules for automatically monitoring the work process is however additionally installed. For example, if the courier did not download data before a given deadline, an e-mail is automatically sent to the dispatcher. Also, when some mail is not delivered after a given time span, an automatically generated e-mail informs the supervisor about this. The event management system helps to significantly reduce a dispatcher’s and supervisor’s workload; only in case of a failure, they are informed in detail, allowing them to react immediately. On-line routing methods can also play an important role in this kind of application, e.g., when pick-up orders should be sent to the “nearest” courier.

Mobile business applications are also widely used in the field of private nursing. The employees get detailed working plans sent to their mobile device. In most cases PDAs or also smart phones are used. Not only arrival and departure at the customer places are confirmed, also every single outpatient care activity will be confirmed and corresponding information sent to the company’s data base. This way, the complete invoicing process is highly automated on a digital level, as recommended by the German health insurance companies. An additional on-line routing could help to identify and reduce delays.

Also for service technicians, mobile business applications provide several advan tages. Service orders can easily be forwarded to the responsible field force employee with all specific information required to successfully complete orders. Assigning orders to technicians can be based, e.g., on criteria like distance and a technician’s available capacity.

The advantages of such mobile business applications are obvious. Digital interactive information transmission without any media break by means of integrated applications and systems significantly reduces the amount of communication and enables real-time availability of important information. In fact, this provides essential transparency for monitoring, managing and optimising important processes outside the companies’ buildings. In combination with location-based services and on-line routing additional advantages and cost reduction could be realised.

## 8 Summary and Outlook

This paper introduced a web/WAP server based mobile communication system that enables a firm to easily integrate mobile co-workers into its IT system. The use of the system was illustrated for the case of subsequent newspaper deliveries of a medium-sized publishing house in Germany. It was also shown that this system allows a straightforward integration of on-line vehicle routing algorithms, and some possible applicable methods were reviewed.

The mobile communication system described here exemplifies that todays communication and information technology allows to quickly build mobile communication systems that are based on a relatively simple system architecture as well as cheap and easy-to-handle system components. Such systems are of course not only useful for supporting on-line routing; they generally allow to implement mobile business processes in a firm’s IT system, to streamline the information flows and to avoid thereby a number of dysfunctional “media breaks”. This way the necessary prerequisites for supporting mobile logistic processes by means of optimisation and quantitative methods in general are established. The development, investigation and implementation of suitable optimisation methods for controlling logistic processes on-line is then surely a fruitful research area. Regarding techniques for supporting dynamic routing, there seems to exist a gap between stochastic approaches, on the one hand, and reoptimisation methods, on the other hand. While the first group of methods stresses the stochastic aspects of dynamic routing, the second family of methods, although powerful, miss lookahead capabilities. Integrating both methodological approaches in some way might thus be helpful for obtaining further improvements.

## References

[1] AlShaali S, Varshney U (2005) On the usability of mobile commerce. International Journal of Mobile Communication 3:29-37.

[2] Bertsimas DJ (1992) A vehicle routing problem with stochastic demand. Operations Research 40:574–585.

[3] Bertsimas DJ, Simchi-Levi D (1996) A new generation of vehicle routing research: Robust algorithms, addressing uncertainty. Operations Research 44:286–304.

[4] Bertsimas DJ, van Ryzin G (1991) A stochastic and dynamic vehicle routing problem in the Euclidean plane. Operations Research 39:601–615.

[5] Bertsimas DJ, van Ryzin G (1993) Stochastic and dynamic vehicle routing in the Euclidean plane with multiple capacitated vehicles. Operations Research 41:60–76.

[6] Bieding TJ (2001) Wann wird der Kunde wirklich beliefert. Logistik Heute 6.

[7] Bieding TJ (2004) Planning and controlling the daily delivery to the same customers – problems and adequate solutions. In: Fleischmann B, Klose A (eds) Distribution Logistics - Advanced Solutions to practical Problems. Lecture Notes in Economics and Mathematical Systems 544. Springer, Berlin Heidelberg New York.

[8] Bieding TJ, Ehrle C (2004) Nachlieferungen per Handy übertragen. dnv - Der neue Vertrieb 19.

[9] Dillmann R (2002) Strategic vehicle problems in practice – a pure software problem or a problem requiring scientific advice. In: Klose A, Van Wassenhove LN, Speranza MG (eds) Quantitative Approaches to Distribution Logistics and Supply Chain Management. Lecture Notes in Economics and Mathematical Systems 519. Springer, Berlin Heidelberg New York.

[10] Dillmann R, Becker B, Beckefeld V (1996) Practical aspects of route planning for magazine and newspaper wholesalers. European Journal of Operational Research 90:1–12.

[11] Fleischmann B, Gnutzmann S, Sandvoß E (2004) Dynamic vehicle routing based on online traffic information. Transportation Science 38:420–433.

[12] Gendreau M, Guertin F, Potvin J-Y, Taillard ED (1999) Parallel tabu search for real-time vehicle routing and dispatching. Transportation Science 33:381–390.

[13] Gendreau M, Laporte G, Séguin R (1996) Stochastic vehicle routing. European Journal of Operational Research 88:3–12.

[14] Gendreau M, Potvin J-Y (1998) Dynamic vehicle routing and dispatching. In: Crainic TG, Laporte G (eds) Fleet Management and Logistics. Kluwer Academic Publishers, London Dordrecht Boston.

[15] Ghiani G, Guerriero F, Laporte G, Musmanno R (2003) Real-time vehicle routing: Solution concepts, algorithms and parallel computing strategies. European Journal of Operational Research 151:1–11.

[16] Helsgaun K (2000) An effective implementation of the Lin-Kernighan traveling salesman heuristic. European Journal of Operational Research 126:106–130.

[17] Larsen A, Madsen OBG, Solomon MM (2004) The a priori dynamic traveling salesman problem with time windows. Transportation Science 38:459-472.

[18] Lin S, Kernighan BW (1973) An effective heuristic for the traveling-salesman problem. Operations Research 21:498–516.

[19] Mintsis G, Basbas S, Papaioannou P, Taxiltaris C, Tziavos IN (2004) Applica tions of GPS technology in the land transportation system. European Journal of Operational Research 152:399–409.

[20] Potvin J-Y, Rousseau J-M (1993) A parallel route building algorithm for the vehicle routing and scheduling problem with time windows. European Journal of Operational Research 66:331–340.

[21] Psaraftis HN (1988) Dynamic vehicle routing problems. In: Golden BL, Assad AA (eds) Vehicle Routing: Methods and Studies. North-Holland, Amsterdam.

[22] Psaraftis HN (1995) Dynamic vehicle routing: Status and prospects. Annals of Operations Research 61:143–164.

[23] Okhrin I, Richter K (2005) Mobile Business – Framework, Business Applications and Practical Implementation in Logistics Companies. Arbeitsberichte Mobile Internet Business Nr. 1, Frankfurt.

[24] Rochat Y, Taillard ED (1995) Probabilistic diversification and intensification in local search for vehicle routing. Journal of Heuristics 1:147–167.

[25] Savelsbergh M, Sol M (1998) Drive: Dynamic routing of independent vehicles. Operations Research 46:474–490.

[26] Solomon MM (1987) Algorithms for the vehicle routing and scheduling problem with time window constraints. Operations Research 35:254–265.

[27] Stewart WR, Golden BL (1983) Stochastic vehicle routing: A comprehensive approach. European Journal of Operational Research 14:371–385.

[28] Swihart MR, Papastavrou JD (1999) A stochastic and dynamic model for the single-vehicle pick-up and delivery problem. European Journal of Operational Research 114:447–464.

[29] Taillard ED, Gambardella LM, Gendreau M, Potvin J-Y (1998) Adaptive memory programming: A unified view of meta-heuristics. Technical Report IDSIA-19-98, IDSIA Lugano.

[30] Tarantilis CD, Diakoulaki D, Kiranoudis CT (2004) Combination of geographical information system and efficient routing algorithms for real life distribution operations. European Journal of Operational Research 152:437–453.

[31] Thomas BW, White CC (2004) Anticipatory route selection. Transportation Science 38:473487.

[32] Wichmann T (2004) Prozesse optimieren mit Mobile Solutions. Berlecon Research Report 03/2004. http://www.berlecon.de/research/reports.php.

[33] Wilhelm H (2006) Differenzierungsmerkmal Sendungsverfolgung. Presentation, 4. Lizenznehmerforum der Bundesnetzagentur, 22. November 2006, Bonn. http://www.bundesnetzagentur.de/media/archive/8380.pdf.

[34] Wirtz BW (2001) Electronic Business. Gabler, Wiesbaden.

[35] Zobel J (2001) Mobile Business and M-Commerce. Hanser, München.

# Service Design Models for Rail Intermodal Transportation

Teodor Gabriel Crainic

NSERC Industrial Research Chair in Logistics Management, Department of Management and Technology, School of Business and Management

and CIRRELT, University of Quebec in Montreal, Canada theo@crt.umontreal.ca

**Summary.** Intermodal transportation forms the backbone of the world trade and exhibits sig nificant growth resulting in modifications to the structure of maritime and land -based trans portation systems, as well as in the increase of the volume and value of intermodal traffic moved by each individual mode. Railroads play an important role within the intermodal chain. Their own interests and environment-conscious public policy have railroads aiming to increase their market share. To address the challenge of efficiently competing with trucking in offering customers timely, flexible, and “low”-cost transportation services, railroads propose new types of services and enhanced performances. From an Operations Research point of view, this requires that models be revisited and appropriate methods be devised. The paper discusses some of these issues and developments focusing on tactical planning issues and identifies challeng ing and promising research directions.

**Key words:** Intermodal transportation, Freight rail carriers, Tactical planning, Fullasset-utilization policies, Intermodal shuttle networks, Design-balanced service network design

## 1 Introduction

Intermodal transportation forms the backbone of the world trade and exhibits significant growth. The value of multimodal shipments in the U.S., including parcel, postal service, courier, truck-and-rail, truck-and-water, and rail-and-water, increased from about 662 billion US dollars to about 1.1 trillion in a period of nine years (1993 to 2003 [31]). In the same period, the total annual world container traffic grew from some 113.2 millions of TEUs (20 feet equivalent container units) to almost 255 millions, reaching an estimated 304 millions of TEUs by 2005.

Intermodal transportation involves, sometimes integrates, at least two modes and services of transportation to improve the efficiency of the door-to-door distribution process. The growth in intermodal traffic thus resulted in significant modifications to the structure of maritime and land-based transportation systems as well as in major increase of the volumes and value of intermodal traffic moved by each individual mode. Thus, for example, in 2003, for the first time ever, intermodal freight surpassed coal as a source of revenue for major, Class I, U.S. railroads, representing 23% of the carriers’ gross revenue [31]. The growth of intermodal rail traffic in the U.S., which reached 11 million trailers (26% of total) and containers (76%) in 2004, is the direct result of the rapid growth in the use of containers for international trade, imports accounting for the majority of the intermodal activity [31].

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">L. Bertazzi et al. (eds.), Innovations in Distribution Logistics, Lecture Notes</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">in Economics and Mathematical Systems 619, DOI: 10.1007/978-3-540-92944-4,</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">-c 2009 Springer-Verlag Berlin Heidelberg</span></small>

Governmental policy may also contribute to re-structuring intermodal transportation and shifting parts of the land part of the journey from trucking toward rail and water (interior and coastal navigation). This is, for example, the main focus of the European Union as stated in its 2001 White Paper on transportation [20]. The reason for this is to reduce road congestion and promote environmentally friendlier modes of transportation. The instruments favored to implement such policies vary from road taxes to penalize truck-based transportation to the support of new rail services for intermodal traffic.

The performance of intermodal transportation depends directly on the performance of the key individual elements of the chain, navigation companies, railroads, motor carriers, ports, etc., as well as on the quality of their interactions regarding operations, information, and decisions. The Intelligent Transportation Systems and Internet-fueled electronic business technologies provide the framework to address the latter challenges. Regarding the former, carriers and terminals, on their own or in collaboration, strive to continuously improve their performance. Railroads are no exception. Indeed, for intermodal as for general traffic, railroads face significant challenges to efficiently compete with trucking in offering customers timely, flexible, and “low”-cost, long-haul transportation services.

Railroads are rising to the challenge by proposing new types of services and enhanced performances. Thus, North-American railroads have created intermodal subdivisions that operate so-called “land-bridges” providing efficient container transportation by long, double-stack trains between the East and the West coasts and between these ports and the industrial core of the continent (so-called “mini” landbridges). Most North-American railroads are now enforcing some form of scheduled service. In Europe, where congestion has long forced the scheduling of trains, the separation of the infrastructure ownership from service providing increases the competition and favors the emergence of new carriers and services. Moreover, the expansion of the Community to the east provides the opportunity to introduce new services that avoid the over-congested parts of the European network. New container and trailer-dedicated shuttle-train networks are thus being created within the European Community.

The planning and management processes of these new railroad-based intermodal systems and operations are generally no different from those of “traditional” systems in terms of issues and goals, profitability, efficiency, and customer satisfaction. The “new” operating policies introduce, however, elements and requirements into the planning processes which, from an Operations Research point of view, require that models be revisited and appropriate methods be devised.

This paper aims to discuss some of these issues and developments. It focuses on the tactical planning of rail intermodal services in North America and Europe and is based on a number of observations and on-going projects. Its goal is to be informative, point to challenges, and identify opportunities for research aimed at both methodological developments and actual applications.

## 2 Intermodal and Rail-Based Transportation

Many transportation systems are multimodal, their infrastructure supporting various transportation modes, such as truck, rail, air, and ocean/river navigation, carriers operating and offering transportation services on these modes. Then, broadly defined, intermodal transportation refers to the transportation of people or freight from their origin to their destination by a sequence of at least two transportation modes. Transfers from one mode to the other are performed at intermodal terminals, which may be a sea port or an in-land terminal, e.g., rail yards, river ports, airports, etc. Although both people and freight can be transported using an intermodal chain, in this paper, we focus on the latter.

The fundamental idea of intermodal transportation is to consolidate loads for efficient long-haul transportation performed by large ocean vessels and, on land, mostly by rail and truck. Local pick-up and delivery is usually performed by truck. Most of the freight intermodal transportation is performed by using containers. Intermodal transportation is not restricted, however, to containers and intercontinental exchanges. For instance, the transportation of express and regular mail is intermodal, involving air and land long-haul transportation by rail or truck, as well as local pick up and delivery operations by truck [16]. Moving trailers on rail is also identified as intermodal. In this paper, we focus on container and trailer-based transportation by railroads.

Intermodal transportation systems and railroads may be described as being based on consolidation. A consolidation transportation system is structured as a hub-and-spoke network, where shipments for a number of origin-destination points may be transferred via intermediate consolidation facilities, or hubs, such as airports, seaport container terminals, rail yards, truck break-bulk terminals, and intermodal platforms. An example of such a network with three hubs and seven regional terminals is illustrated in Fig. 1 [7]. In hub-and-spoke networks, low-volume demands are first moved from their origins to a hub where traffic is sorted (classified) and grouped (consolidated). The aggregated traffic is then moved in between hubs by efficient, “high” frequency and capacity, services. Loads are then transferred to their destination points from the hubs by lower frequency services often utilizing smaller vehicles. When the level of demand is sufficiently high, direct services may be run between a hub and a regional terminal.

Railroads operate most of their services according to a double-consolidation policy based on a series of activities taking place at rail hubs, the so-called classification or marshaling yards. The first consolidation activity concerns the sorting and grouping of railcars into blocks. A block is thus made up of cars of possibly different origins and destinations, which travel as a single unit between the origin and destination of the block. Consequently, the only operation that could be performed on a block at a yard which is not its destination is to transfer it from one service to another. The second consolidation activity taking place at yards, known as train make up, concerns the grouping of blocks into trains. Although a hub-and-spoke network structure results in a more efficient utilization of resources and lower costs for shippers, it also incurs a higher amount of delays and a lower reliability due to longer routes and the additional operations performed at terminals. Carriers thus face a number of issues and challenges in providing services that are simultaneously profitable and efficient for the firm and high quality and cost effective for customers. Operations Research has contributed a rich set of models and methods to assist addressing these issues and challenges at all levels of planning and management, classically identified as strategic (long term), tactical (medium term), and operational (short term). A more in-depth treatment of these topics may be found, for example, in the reviews of Cordeau, Toth, and Vigo [11], Crainic [12, 13], Crainic and Laporte [17], and Crainic and Kim [16]. In this paper, we focus on tactical planning issues.

![](images/page_62_image_2.jpg)

Fig. 1. A hub-and-spoke network [7]

## 3 New Rail Intermodal Services

Rail transportations systems evolved according to the geographic, demographic, economic, and sociological characteristics of the countries and continents they belong to. North American and European railroads were no exception. Yet, recently, a number of similar trends emerge. Traditional North American railroad operating policies were based on long-term contracts for the transportation of high volumes of mostly bulk commodities. Cost per ton/mile (or km) was the main performance measure, with somewhat little attention being paid to delivery performance. Consequently, rail services in North America, and mostly everywhere else in the world, were organized around loose schedules, indicative cut-off times for customers, “go-when-full” operating policies, and significant marshaling activities in yards. This resulted in rather long and unreliable trip times that generated both inefficient asset utilization and loss of market share. This was not appropriate for the requirements of intermodal transportation and the North American rail industry responded through [14]:

1. A significant re-structuring of the industry through a series of mergers, acquisitions, and alliances which, although far from being over, has already drastically reduced the number of companies resulting in a restricted number of major players.

2. The creation of separate divisions to address the needs of intermodal traffic, operating dedicated fleets of cars and engines, and marshaling facilities (even when located within regular yards). Double-stack convoys have created the landbridges that ensure an efficient container movement across North America.

3. An evolution toward planned and scheduled modes of operation and the introduction of booking systems and full-asset-utilization operating policies.

Booking systems bring intermodal rail freight services closer to the usual mode of operation of passenger services by any regular mode of transportation, train, bus, or air. In this context, each class of customers or origin-destination market has a certain space allocated on the train and customers are required to call in advance and reserve the space they require. The process may be phone or Internet based but is generally automatic, even though some negotiations may occur when the train requested by the customer is no longer available. This new approach to operating intermodal rail services brings advantages for the carrier, in terms of operating costs and asset utilization, and the customers (once they get used to the new operating mode) in terms of increased reliability, regular and predictable service and, eventually, better price. A full-asset-utilization operation policy generally corresponds to operating regular and cyclically-scheduled services with fixed composition. In other words, given a specific frequency (daily or every given number of days), each service occurrence operates a train of the same capacity (length, number of cars, tonnage) and composition, that is, the same blocks make up all the occurrences of the service, each block displaying a fixed definition: origin, destination, number of total cars, and number of cars for each origin-destination included in its composition.

A full-asset-utilization operation policy generally corresponds to operating regular and cyclically-scheduled services with fixed composition. In other words, given a specific frequency (daily or every given number of days), each service occurrence operates a train of the same capacity (length, number of cars, tonnage) and composition, that is, the same blocks make up all the occurrences of the service, each block displaying a fixed definition: origin, destination, number of total cars, and number of cars for each origin-destination included in its composition.

Assets, engines, rail cars and even crews, assigned to a system based on fullasset-utilization operation policies can then “turn” continuously following circular routes and schedules (which include maintenance activities for vehicles and rest periods for crews) in the time-space service network, as schematically illustrated in Fig. 2 for a system with three yards and six time periods [3]. The solid lines in the service-network (left) part of Fig. 2 represent services. There is one service from node 1 to node 3 (black arcs) and one service from node 3 to node 2 (gray arcs), both with daily frequency. Dotted arcs indicate repositioning moves (between different nodes) and holding arcs (between different time representations of same node). One feasible vehicle circuit in the time-space service network is illustrated in the right part of Fig. 2. The vehicle operates the service from node 3 to node 2, starting in time period 1 and arriving in time period 3. Then from period 3 to period 4 the vehicle is repositioned to node 1, where it is held for two time periods. In period 6 the vehicle operates the service from node 1 to node 3, arriving at time 1 where the same pattern of movements starts all over again. The planning of systems operating according to such policies requires the development of new models and methods, as described in the next section.

![](images/page_64_image_2.jpg)

Fig. 2. Full-asset-utilization-based service network and vehicle circuit [3]

Most Western Europe railroads have for a long time now operated their freight trains according to strict schedules, similarly to their passenger trains. This facilitated both the interaction of passenger and freight trains and the quality of service offered to customers. Particular characteristics of infrastructure (e.g., low overpasses and infrastructure for electric traction) and territory (short inter-station distances) make for shorter trains than in North America and forbid double-stack trains. Booking systems are, however, being implemented and full-asset-utilization and revenue management operating policies are being contemplated. Moreover, intermodal shuttle-service networks are being implemented in several regions of the European Union to address the requirements of the European Commission policy and the congested state of the infrastructure (e.g., [1, 27]).

Indeed, European railroads face a number of particular challenges. First, the rail infrastructure, as almost the entire transportation infrastructure in Europe, is very congested. Second, the liberalization of the rail industry in Europe has led to the separation of the traditional national rail companies into infrastructure owners and service operators. The former manage the infrastructure and associated network capacity, while the latter operate trains according to the capacity acquired from the infrastructure managers. This liberalization favors the emergence of new rail operators providing specialized services, in particular intermodal rail shuttle services between cities with high traffic demand.

The limited capacity of most of the infrastructure, at least in the western part of the network, together with the increasing number of operators, forces the allocation of capacity according to pre-defined routes and times, which makes planning decisions and the efficient utilization of resources more difficult. The European Union, the member states, and the corresponding rail authorities are implementing steps, however, toward interoperability and an interconnected trans-European rail network for freight trains, the so-called freight freeways [19]. As a result, one assists at the emergence of large service networks across the European continent operated by single operators or by alliances of operators, similar to those seen in the airline industry. The resulting service networks will be complex to plan and operate and appropriate models and methods must be developed. Pedersen and Crainic [27] detail the case and propose a first service network design model.

To alleviate the congestion in the “central” part of the network while working toward the goal of increasing the market share of rail and navigation, new intermodal services are being studied using the networks of countries that have recently joined the Union. Andersen and Christiansen [1] describe such a project. The Longchain Polcorridor study [24] aims to develop a new intermodal transport corridor between Northern and South-Eastern Europe taking advantage of previously unused railway capacity in Poland, the Czech Republic and Austria, and thus create a fast and reliable transport solution than can compete with the more traditional route through Germany. The authors propose a formulation to determine an optimal service level and design that accounts for both operating costs and a number of service quality criteria. An extensive network of inland waterways, sea transport, trucking services, and other railway lines will be used as distribution networks at the extremities of the new network. This requires external synchronization of schedules with partner carriers. Internal synchronization is also required to account for power-equipment switching at particular borders due to different technical standards between participating national railroads. Andersen, Crainic, and Christiansen [3] propose formulations for this case.

## 4 Impact on Planning Models

A study of the trends observed in North America and Europe, illustrated by the cases mentioned in the previous section, indicates a number of converging issues. One may sum up these issues by noticing that the operations and asset management of intermodal railroads are more and more similar to those of long-haul passenger transportation, airlines and fast rail, in particular. Services are thus precisely scheduled and service space is booked in advance. Moreover, schedules are repetitive (cyclic) and synchronized, both internally among the railroad’s own services and externally with those of partner carriers. This implies tighter consolidation, classification, transfer, and make-up operations at terminals, as well as scheduling assets for maximum but efficient utilization.

Traditionally, planning was performed through a series of tasks, planning models being used one after another to address particular issues: design of the service network and schedules, power (locomotive) assignment and management, empty railcar repositioning and fleet management, and so on. This approach was not particular to railroads or freight transportation; it was typical of the traditional management structure and planning processes of most industrial firms facing complex issues. From an Operations Research point of view, it reflected the limitations of our capabilities in addressing large-scale combinatorial formulations with complex additional constraints. Managerial structures evolve, however, and our capabilities are continuously being enhanced, both in terms of computer power and methodology sophistication. The trend toward integrated models addressing in a comprehensive formulation several issues previously treated separately, initially observed within the airline industry (e.g., [5]) is now influencing the development of planning methods for railroad operations, most particularly within the field of intermodal transport.

To briefly illustrate these issues and the corresponding challenges, we turn to service network design in the context of full-asset-utilization operating policies. We conclude the section by identifying a number of other “new” planning issues offering exiting research perspectives.

## 4.1 Service Network Design

Recall that service network design is concerned with the planning of operations related to the selection, routing, and scheduling of services, the consolidation and make-up activities at terminals, and the routing of freight of each particular demand through the physical and service network of the company (see, for example, the surveys of Crainic for service network design [12] and long-haul land transportation [13], Crainic and Kim [16] and Macharis and Bontekoning [25] for intermodal transportation, Christiansen et al. [10, 9] for maritime navigation, and Cordeau, Toth, and Vigo [11] for railroads. These activities are a part of tactical planning at a systemwide level. The two main types of decisions considered in service network design address the determination of the service network and the routing of demand. In the railroad context, the former refers to selecting the train routes and attributes, such as the frequency or the schedule of each service. The latter is concerned with the itineraries that specify how to move the flow of each demand, including the services and terminals used, the operations performed at these terminals, etc. The objective is generally concerned with the minimization of a global measure of the performance of the system that includes the operating costs of providing services, performing yard operations, and moving freight, as well as service-quality measures usually based on delays to equipment and loads. The term “generalized cost” is often used in these cases.

The basic service network design mathematical models take the form of deterministic, fixed cost, capacitated, multicommodity network design (CMND) formulations [26, 12, 16]. Let S represent the service network, defined on a graph representing the physical infrastructure of the system (yards, stations, and the rail links connecting them), which specifies the transportation services that could be offered. Each potential service s ∈ S is characterized by a number of attributes such as its route, capacity measured in number of vehicles, length, total weight, or a combination thereof, service class indicating the speed and priority, as well as, eventually power type, preferred traffic or restrictions, etc. When schedules are to be determined, a time-space network $\mathcal { G } ~ = ~ \{ \mathcal { N } , \mathcal { A } \}$ is introduced (see Fig. 2). Nodes representing the terminals (yards and stations) of the system are repeated at all periods (e.g., days) of the considered planning horizon (e.g., a week) yielding the set N. Nodes in N representing the same terminal at two consecutive time periods are connected by holding arcs, and departure times from origin, as well as arrival at and departure times from intermediary stops are associated to each service. Set $\mathcal { A }$ is then the union of the holding and service arcs. The service network is used to move commodities $p \in { \mathcal { P } }$ defined by their origins, destinations, the period of availability at origin and, eventually the due date at destination, the type of product or vehicle to be used, priority class, and so on. The demand for product $p$ is denoted $d _ { p }$ . Traffic moves according to itineraries defined within the model as service paths $l \in \mathcal { L } ^ { p }$ for commodity $p ,$ each specifying the intermediary terminals where operations (e.g., consolidation or transfer) are to be performed and the sequence of services between each pair of consecutive terminals where work is performed.

Flow routing decisions are then represented by decision variables $h _ { l } ^ { p }$ indicating the volume of product $p$ moved using its itinerary $l \in \mathcal { L } ^ { p }$ , and service selection decision variables $y _ { s } ,   s \in \mathcal { S } ,$ define whether the particular service is operated (i.e., it will leave at the associated departure time) or not. Let $y = \{ y _ { s } \}$ and $h = \{ h _ { l } ^ { p } \}$ be the decision-variable vectors. Let also $f _ { s }$ denote the “fixed” cost of operating service s and $c _ { l } ^ { p }$ stand for the unit transportation cost along itinerary $l \in \mathcal { L } ^ { p }$ of commodity $p .$ The core service network design model minimizes the total generalized system cost, while satisfying the demand for transportation and the service standards:

$$
\text {Minimize} \quad \sum_ {s \in \mathcal {S}} f _ {s} y _ {s} + \sum_ {p \in \mathcal {P}} \sum_ {l \in \mathcal {L} ^ {p}} c _ {l} ^ {p} h _ {l} ^ {p} + \phi (y, h)\tag{1}
$$

$$
\text {subject to} \quad \sum_ {l \in \mathcal {L} ^ {p}} h _ {l} ^ {p} = d _ {p}, p \in \mathcal {P},\tag{2}
$$

$$
y _ {s} \in \{0, 1 \}, s \in \mathcal {S},\tag{3}
$$

$$
h _ {l} ^ {p} \geq 0, l \in \mathcal {L} ^ {p}, p \in \mathcal {P},\tag{4}
$$

$$
(y, h) \in \chi ,\tag{5}
$$

where $\phi ( y , h )$ indicates additional restrictions, e.g., service capacity, expressed as utilization targets, which may be allowed to be violated at the expense of additional penalty costs. Relations 5 stand for the classical linking constraints (i.e., no flow may use an unselected service), as well as for additional constraints reflecting partic ular characteristics, requirements, restrictions, and policies (e.g., particular routing or load-to-service assignment rules) particular to the carrier considered in application.

The class of models represented by the previous formulation does not account for the utilization of assets. Yet, to adequately plan operations according to a fullasset-utilization operating policy requires the asset circulation issue to be integrated into the service network design model. Adding constraints enforcing the conservation of the flow of vehicles at terminals is the first step in reaching this goal. These constraints take the form

$$
\sum_ {s \in \mathcal {S}} y _ {s i ^ {+}} - \sum_ {s \in \mathcal {S}} y _ {s i ^ {-}} = 0, i \in \mathcal {N},\tag{6}
$$

where $s i ^ { + }$ indicates the services that arrive and stop or terminate at node (yard) $i \in N$ , while $s i ^ { - }$ stands, symmetrically, for the services that initiate their journeys or stop and depart from node i. The resulting models, denoted design-balanced capacitated multicommodity network design (DBCMND) by Pedersen, Crainic, and Madsen [28], account for coherent movements in and out of terminals (particularly when“empty” movements are allowed) and yield cyclic and repetitive schedules for the fleet of vehicles associated to services.

This generalization of the CMND model has not been studied much. A few applications may be found in planning maritime liner [9] or ferry [22] routes and express postal services, e.g., [6, 21], where vehicles, ships and airplanes, have high acquisition and utilization costs and their management is central to the efficient operation of the system. For land-based carriers, while empty-vehicle considerations were usually part of the most comprehensive service network design models, the emphasis was not on the management of the fleet. Thus, for example, Powell [29] considered the balance of loaded and empty truck balance at terminals in a static model for designing Less-Than-Truckload motor-carrier services that did not consider vehicle schedules. For rail, Crainic, Ferland, and Rousseau [15] (see also [18]) addressed the issue by adding a product to represent the demand for empty-car repositioning movements. The model was static and no asset schedule or route considerations were explicitly included. More recently, Smilowitz, Atamtürk, and Daganzo [30] developed a timedependent formulation similar to the one presented above for truck operations within an express postal network and proposed a particularly tailored procedure where, first, the linear programming relaxation of the problem is solved (approximately, for large problem instances) using column generation and, second, a feasible solution is obtained by applying repetitively a sequence of rounding and cut-generation procedures.

The DBCMND is a difficult problem with an added “complexity layer” compared to the CMND and much work is required to study it and develop efficient exact and heuristic solution methods. A few efforts are under way. Pedersen and Crainic [27] studied the design of a network of shuttle intermodal trains in Europe using a DBCMND model that included detailed yard operations (excluding car classification). The resulting formulation was sufficiently small, however, to allow commercial software to be used. Pedersen, Crainic, and Madsen [28] introduced arc and cycle-based DBCMND formulations and proposed a two-stage, tabu search-based meta-heuristic that is shown to be efficient for problem instances up to 700 service arcs and 400 commodities. Andersen, Crainic, and Christiansen [3] extended the arcbased formulation to account for coordination of multiple fleets and synchronization of schedules among subsystems. The analysis was performed within the scope of the design of new north-south intermodal services in Central Europe and emphasized the benefit of increased inter-system integration and coordination. The same authors also studied various DBCMND formulations, where product flows were represented either by arc or path variables, while design decisions were represented either by arcs or cycle variables [2]. Notice that the latter correspond to circuits of vehicles, the service selection (design) decisions becoming thus implicit in the selection of strategies for fleet management. Commercial software was used for experimentation and results showed a very good computational behavior for cycle-based formulations in terms of computational efficiency and quality of the final solution (when the optimal solution could not be reached within the time available). Recently, Andersen et al. [4] proposed a first branch-and-price algorithm for the generic cycle-based DBCMND formulation.

The contributions briefly reviewed above are very encouraging, but significant work is still required on models, algorithms, and applications. Regarding models, we need to better understand the DBCMND class of formulations and their properties. Initial results seem to indicate that cycle-based formulations outperform arc-based ones, but more in-depth studies are required to fully characterize the various formulations and explain their respective behaviors. Work is also required in developing tighter lower and upper bounds on the optimal solution to these formulations. Lagrangean relaxation and decomposition approaches have provided interesting results for other classes of network design problems and are worthy of investigation in developing good lower bounds for DBCMND problems. Using the solutions of lower bound methods to compute “good” upper bounds proved difficult for CMND problems and we expect it to present an even greater challenge for DBCMND problems for which identifying feasible solutions is proving to be far from trivial [28].

Turning to applications, stating a DBCMND formulation is generally only the first step to a complete model. Actual railroad planning applications bring a rich set of additional constraints that add both to the realism and the complexity of the formulation. Pedersen and Crainic [27] thus discussed the need for a more general definition of “period” within time-dependent formulations to capture adequately the time intervals when services overlap at terminals and inter-service transfers may be performed. The authors also emphasized the need for a more detailed representation of terminal operations than it is usually the case in service network design models to capture their delay and capacity impacts on the general performance of the system. This aspect is also emphasized by Andersen, Crainic, and Christiansen [3] who detailed the operations in terminals connecting the system studied to adjacent maritime and land systems, and presented a first quantification of the benefits of synchronizing services both internally, among services using possibly different vehicle fleets, and externally with services belonging to neighboring systems. The authors also examined and quantified the impact of a number of fleet-management considerations, such as limits on the length of vehicle routes and bounds on the number of departures for particular services. One need to follow up on these early efforts by focusing on two main areas. One the one hand, the study of integrating fleet management and service network design must be continued to identify relevant issues and the most appropriate modeling approaches, and to analyze their impact on the resulting transportation plan and, ultimately, on the performance of the rail system. On the other hand, the models must be enriched to account for other important planning issues, such as congestion related to yard (and, eventually, line) operations and the management of more than one class of assets.

Last but not least, significant algorithmic work is required. The methods proposed so far addressed simple model formulations and have often been tested on problem instances that do not cover the full dimensions of actual large-scale applications. Both exact and meta-heuristic solution methods must be developed for the models described above. Given the dimensions and complexity (e.g., in the number of interacting and possibly conflicting components) of these formulations, we expect parallel optimization approaches to play an important role in addressing real-life applications.

## 4.2 Additional Issues

Many other issues related to the planning and operations of intermodal and, more generally, consolidation-based freight transportation offer rich research challenges and opportunities.

Consider, for example, that, although bookings tend to “smooth” out demand, the variability inherent to the system is not altogether eliminated since regular operations tend to be disrupted by a number of phenomena. Thus, for example, ocean liner ships do not always arrive at container port terminals according to schedule and custom and security verifications may significantly delay the release of containers. When this occurs, rail intermodal operations out of the corresponding ports are severely strained: there might be several days without arrivals, followed by a large turnout of arriving containers. Optimization approaches [14] may be used to adjust service over a medium-term horizon in such a way that a full-asset-utilization policy is still enforced, but a certain amount of flexibility is added to services to better fit service and demand. Such approaches may become even more effective when appropriate information sharing and container-release time mechanisms are implemented.

Among the other relevant challenging research issues, let’s not forget the explicit consideration of stochastic elements in tactical planning models. Preliminary results [23] indicate that the plans thus obtained are different and “better” from a robustness point of view than those of traditional deterministic models, but much more work is needed in this field. Terminal planning issues also require attention. While the literature dedicated to container port terminals is rather rich, there is almost nothing dedicated to rail yards within the intermodal context (the work by Bostel and Dejax [8] is the only exception we are aware of and it is directed toward an innovative but as yet not implemented rail transportation system). On a more operational level, work is required relative to detailed fleet management procedures to mitigate the impact of incidents and accidents on service and to guide the process of getting back to normal operations following such disruptions.

## 5 Conclusions

We have discussed a number of service and operating strategies railroads propose to improve the performance of their operations, increase their market share of intermodal traffic, and efficiently compete with trucking in offering customers timely, flexible, and “low”-cost transportation services. This evolution, including the advance bookings and full-asset-utilization policies increasingly implemented by existing and planned railroad intermodal systems, challenges current models and methods for the design of services and the management of operations. Focusing on tactical planning issues, we have briefly examined these impacts and have identified research challenges and opportunities.

## Acknowledgments

Partial funding for this project has been provided by the Natural Sciences and Engineering Research Council of Canada (NSERC) through its Discovery Grants and Chairs and Faculty Support programs

## References

[1] Andersen, J. and Christiansen, M. Optimal Design of New Rail Freight Services. Journal of the Operational Research Society, 2007. forthcoming.

[2] Andersen, J., Crainic, T.G., and Christiansen, M. Service Network Design with Asset Management: Formulations and Comparative Analyzes. Publication CIRRELT-2007-40, CIRRELT - Centre de recherche sur les transports, Université de Montréal, Montréal, QC, Canada, 2007.

[3] Andersen, J., Crainic, T.G., and Christiansen, M. Service Network Design with Management and Coordination of Multiple Fleets. European Journal of Operations Research, 2007. forthcoming.

[4] Andersen, J., Grønhaug, R., Christiansen, M., and Crainic, T.G. Branchand-Price for Service Network Design with Asset Management Constraints. Publication-2007-55, CIRRELT - Centre de recherche sur les transports, Université de Montréal, Montréal, QC, Canada, 2007.

[5] Barnhart, C., Johnson, E.L., Nemhauser, G.L., and Vance, P.H. Crew Scheduling. In Hall, R.W., editor, Handbook of Transportation Science, pages 517–560. Kluwer Academic Publishers, Norwell, MA, second edition, 2003.

[6] Barnhart, C. and Schneur, R.R. Network Design for Express Freight Service. Operations Research, 44(6):852–863, 1996.

[7] Bektaş, T. and Crainic, T.G. A Brief Overview of Intermodal Transportation. In Taylor, G.D., editor, Logistics Engineering Handbook. Taylor and Francis Group, 2007. forthcoming.

[8] Bostel, N. and Dejax, P. Models and Algorithms for Container Allocation Problems on Trains in a Rapid Transshipment Shunting Yard. Transportation Science, 32(4):370–379, 1998.

[9] Christiansen, M., Fagerholt, K., Nygreen, B., and Ronen, D. Maritime Transportation. In Barnhart, C. and Laporte, G., editors, Transportation, volume 14 of Handbooks in Operations Research and Management Science, pages 189–284. North-Holland, Amsterdam, 2007.

[10] Christiansen, M., Fagerholt, K., and Ronen, D. Ship Routing and Scheduling: Status and Perspectives. Transportation Science, 38(1):1–18, 2004.

[11] Cordeau, J.-F., Toth, P., and Vigo, D. A Survey of Optimization Models for Train Routing and Scheduling. Transportation Science, 32(4):380–404, 1998.

[12] Crainic, T.G. Network Design in Freight Transportation. European Journal of Operational Research, 122(2):272–288, 2000.

[13] Crainic, T.G. Long-Haul Freight Transportation. In Hall, R.W., editor, Handbook of Transportation Science, pages 451–516. Kluwer Academic Publishers, Norwell, MA, second edition, 2003.

[14] Crainic, T.G., Bilegan, I.-C., and Gendreau, M. Fleet Management for Advanced Intermodal Services - Final report, Report for Transport Canada. Publication CRT-2006-13, Centre de recherche sur les transports, Université de Montréal, Montréal, QC, Canada, 2007.

[15] Crainic, T.G., Ferland, J.-A., and Rousseau, J.-M. A Tactical Planning Model for Rail Freight Transportation. Transportation Science, 18(2):165–184, 1984.

[16] Crainic, T.G. and Kim, K.H. Intermodal Transportation. In Barnhart, C. and Laporte, G., editors, Transportation, volume 14 of Handbooks in Operations Research and Management Science, pages 467–537. North-Holland, Amsterdam, 2007.

[17] Crainic, T.G. and Laporte, G. Planning Models for Freight Transportation. European Journal of Operational Research, 97(3):409–438, 1997.

[18] Crainic, T.G. and Rousseau, J.-M. Multicommodity, Multimode Freight Transportation: A General Modeling and Algorithmic Framework for the Service Network Design Problem. Transportation Research Part B: Methodological, 20:225–242, 1986.

[19] European Commission. A Strategy for Revitalizing the Community’s Railways. Whipe paper, Office for official publications of the European Communities, Luxembourg, 1996.

[20] European Commission. European Transport Policy for 2010: Time to Decide. Whipe paper, Office for official publications of the European Communities, Luxembourg, 2001. Available on line at http://www.europa.eu.int/comm/energy transport/en/lb en.html.

[21] Kim, D., Barnhart, C., Ware, K., and Reinhardt, G. Multimodal Express Package Delivery: A Service Network Design Application. Transportation Science, 33(4):391–407, 1999.

[22] Lai, M.F. and Lo, H.K. Ferry Service Network Design: Optimal Fleet Size, Routing and Scheduling. Transportation Research Part A: Policy and Practice, 38:305–328, 2004.

[23] Lium, A.-G., Crainic, T.G., and Wallace, S. A Study of Demand Stochasticity in Service Network Design. Transportation Science, 2007. forthcoming.

[24] Longchain Polcorridor Project Description. EUREKA, http://www.eureka.be/.

[25] Macharis, C. and Bontekoning, Y.M. Opportunities for OR in Intermodal Freight Transport Research: A Review. European Journal of Operational Research, 153(2):400–416, 2004.

[26] Magnanti, T.L. and Wong, R.T. Network Design and Transportation Planning: Models and Algorithms. Transportation Science, 18(1):1–55, 1984.

[27] Pedersen, M.B. and Crainic, T.G. Optimization of Intermodal Freight Service Schedules on Train Canals. Publication CÏRRELT-2007-51, CIRRELT - Centre de recherche sur les transports, Université de Montréal, Montréal, QC, Canada, 2007.

[28] Pedersen, M.B., Crainic, T.G., and Madsen, O.B.G. Models and Tabu Search Meta-heuristics for Service Network Design with Asset-Balance Requirements. Transportation Science, 2007. forthcoming.

[29] Powell, W.B. A Local Improvement Heuristic for the Design of Less-than-Truckload Motor Carrier Networks. Transportation Science, 20(4):246–357, 1986.

[30] Smilowitz, K.R., Atamtürk, A, and Daganzo, C.F. Deferred Item and Vehicle Routing within Integrated Networks. Transportation Research Part E: Logistics and Transportation, 39:305–323, 2003.

[31] U.S. Department of Transportation. Freight in America. Technical report, Research and Innovative Technology Administration, Bureau of Transportation Statistics, Washington D.C., 2006. Available on line at http://www.bts.gov/publications/freight in america/.

# C.A.s.S.a.n.D.r.A.: Computerized AnalysiS for Supply ChAiN DistRibution Activity

Laura Di Giacomo<sup>1</sup>, Ettore Di Lena<sup>2</sup>, Giacomo Patrizi, Livia Pomaranzi, and Federico Sensi<sup>5</sup>

1 LIX, Ecole Polytechnique, Palaiseau, France ´ digiacomo@lix.polytechnique.fr

2 Ente Nazionale Energia Elettrica, Rome, Italy ettore.dilena@enel.it

3 La Sapienza, Università di Roma, Italy g.patrizi@caspur.it

4 Chefaro Pharma Italia, Rome, Italy livia.pomaranzi@chefaro.it

5 Enprovia Software Engineering, Italy Federico-Sensi@libero.it

**Summary.** Supply Chain Management (SCM) is an important activity in all producing organizations. To determine efficient policies over a given time interval, it is necessary to consider a simultaneous dynamic estimation and optimization algorithm over the disposable data base. The aim of this paper is to present the Data Driven algorithm, describe its implementation and show through some preliminary applications its potential advantages. To ensure that Certainty Equivalent optimal policies prevail this aspect will be analyzed.

**Key words:** Optimal estimation and control, Dynamic nonlinear, Supply chain management

## 1 Introduction

Positive synergisms can be enhanced by appropriate Supply Chain Management (SCM) policies in an organization. These benefits can be obtained by studying suitable dynamic and nonlinear mathematical models of the activities to be pursued.

These dynamic and nonlinear processes permit a careful monitoring of the changes in the actions in time and the mutual combination of the results of different actions [16]. However, if these decision making mechanisms are not carefully designed, since activities may have greatly differing requirements, instead of achieving greater levels of efficiency, the supply chain policy formulated may incur in severe instabilities, indeterminacy in the process and be technically uncontrollable [8].

Mathematical System Theory [12] permits the formulation of Dynamical systems, under various conditions, as non anticipatory functional forms and can be solved as multi-objective dynamic nonlinear problems, useful in representing generalized SCM structures with many agents. Nonlinear multi functions or point-to-set maps are essential to formulate accurate optimal robust SCM plans [2] and to analyze uncertainty and feedback.

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">L. Bertazzi et al. (eds.), Innovations in Distribution Logistics, Lecture Notes</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">in Economics and Mathematical Systems 619, DOI: 10.1007/978-3-540-92944-4,</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">-c 2009 Springer-Verlag Berlin Heidelberg</span></small>

Model relationships and parameters are difficult to determine a priori or by experience, as they evolve in unpredictable ways, so suitable simultaneous estimation and optimization algorithms must be formulated to specify the model. In fact these relationships must be determined as instruments to control accurately the phenomenon, rather than as realist approaches [9]. In such implementations the problem of estimability, stability and certainty equivalents of policies become fundamental [18] [20], but these are often not considered [15]. In large scale models with dynamics, nonlinearities and uncertainties ignoring these aspects may be perilous [10].

Model estimates may be biased, heteroscedastic subject to excessive disturbances, while the residual disturbances tend to be serially correlated [6]. So proper estimation techniques must be effected, to absorb all systematic variation by formulating a simultaneous estimation dynamic nonlinear optimal algorithm, such that disturbances are subject to suitable constraints, which will ensure that these satisfy all the required statistical conditions [8, 17].

The form of the relationships of the model and their coefficients must be determined in the space of the parameters and the values of the control variables must be determined in the space of the variables. Since it can be shown that these two spaces are interrelated, a simultaneous optimization algorithm to solve the combined problem must be defined [8].

The aim of this paper is to present this algorithm, describe its implementation and show through some preliminary applications its advantages. In particular it will be shown how certainty equivalents of optimal policies can be obtained in spite of stochastic disturbances and uncertainties.

The outline of the paper is the following. After the introduction, the formulation of representative dynamic nonlinear stochastic system of supply chains is presented for a multi-level process. In Sect. 3 the proposed dynamic system algorithm and the certainty equivalence of a system are described, while the major statistical properties are indicated, in Sect. 4. Then in Sect. 5 an application will be presented, showing comparative results of various solution strategies. Finally appropriate conclusions will be drawn.

## 2 Analysis of SCM Activity

Optimal production levels in a firm with multiple stages depend on economies of scale and the integrated SCM policy. The determination of an optimal SCM plan is a complex nonlinear dynamic problem with stochastic elements and uncertainties, in which all the various decisions must be evaluated simultaneously.

The aim of this section is to characterize a model of a SCM system integrated with a set of representative stages, such as inventory, production policy and distribution and marketing management stages.

Inventory management policies pervade all the stages of production of a firm and involve management decisions regarding raw-materials, goods in process and manufactured goods, which will be collectively indicated as items. It follows therefore that at each intermediate stage between departments and plants items inventories must be considered [11].

The demand and the cost schedules associated, with inventory management should be generally considered as stochastic processes, changing in time as non-stationary stochastic processes [11]. Without loss of generality, assume that no backlogging occurs. Also a particular lost sales policy is allowed and the limit may be specified.

Multi-level proportional lot sizing and scheduling problems may be proposed with given lead times in production [13] under the general structure of empirical processes.

**Definition 1.** An Empirical Process is an ordered set of dated Input and Output variables arranged hierarchically in the form of a Gozinto chart or some similar suitable hierarchical scheme, subprocess by subprocess, to formulate a flow model of the potential operations to be carried out on the underlying phenomenon, so as to determine suitable optimal controls, with respect to some merit function [5].

Limited capacity is also assumed and demand is considered varying, but contrary to many other formulations all the data relevant for the planning process is not assumed deterministic, but must be obtained from the past operations. Machines break down and uncertain events may occur. The operational time for activities is not usually a constant, but depends on a number of environmental aspects.

Dynamic adaptive stochastic diffusion processes are considered for sales models to determine the global SCM plan [3]. The consumption is influenced by a series of events which are random and sequential and depend on environmental factors and Marketing mix plans.

Consumers can be divided into two broad categories:

Innovators: groups of consumers who are attracted by the novelty of the product and therefore respond well to mass communication through promotion and advertising.

• Imitators: groups of consumers more conservative than the previous group, who react mostly from word of mouth communication.

Without loss of generality assume that the number of individuals who purchase a product at time t is the same as the number of units of the product purchased, since every consumer purchases one unit of product in the period [14] and each group will be characterized by the segment of each group.

Consider the following symbols:

$f _ { 0 } ^ { j } ( q _ { t } ^ { j } , t )$ be the non negative setup cost for item j for a quantity $q _ { t } ^ { j }$ at period t,

$f ^ { j } ( I _ { t - 1 } ^ { j } , t )$ be the non negative holding cost for holding one item $j$ in stock at time t for one period until time t + 1 regarding $I _ { t } ^ { j }$ items present at the initial period t,

$h ^ { k } ( I _ { t } ^ { 1 } , \ldots , I _ { t } ^ { B } , t ) \quad k = 1 , \ldots , K _ { t }$ be the $K _ { t }$ physical space, budget and other capacity constraints which must be satisfied in period t,

$D _ { t } ^ { j } = d ^ { j } ( n ^ { j } ( t ) )$ be the demand for the item $j$ at time $t ,$

$J$ number of items considered in the system,

$a _ { i j }$ is a ‘gozinto’ factor. Its value is zero if item $j$ is not an immediate successor of item i. Otherwise its value is set at $\hat { a } _ { i } ^ { j } ,$ , the quantity of item that is directly needed to produce one item $j ,$

$C _ { t } ^ { m }$ be the available capacity of machine m in period $t ,$

$I _ { t } ^ { j }$ Inventory item j at the end of period t,

$\mathcal { I } _ { m }$ be the set of all items that share the same machine $m ,$

• M be the number of machines,

$m ^ { j }$ the machine on which item $j$ is produced,

$p _ { m } ^ { j }$ capacity needed for producing one unit of item $j$ on machine m,

$S _ { j }$ be the set of immediate successors of item $j ,$

$T$ be the number of periods considered,

$\nu _ { j }$ Positive and integral lead time in production for item $j ,$

qj $q _ { t } ^ { j }$ acquisition or production quantity of item $j$ at time t,

• $x _ { t } ^ { j }$ binary variable to indicate whether a setup for item $j$ occurs in period $t , ( x _ { t } ^ { j } = 1 )$ or not $( x _ { t } ^ { j } = 0 )$

$n ^ { j } ( t )$ number of individuals which will purchase an item $j$ in the interval $( t , t + 1 )$ ,

$Y ^ { j } ( t )$ marketing and distribution activities in period t,

$a ^ { j } \left( t , Y ^ { j } ( t ) , Y ^ { j } ( t - 1 ) , \cdots , Y ^ { j } ( t - k ) \right)$ innovation coefficient relative to product $j$ at time $t ,$ conditioned on the past marketing activities $Y ^ { j } ( t ) , Y ^ { j } ( t - 1 ) , \cdots , Y ^ { j } ( t - k )$ , for some $k < t ,$

$b ^ { j } ( t , Y ^ { j } ( t , k ) )$ imitation coefficient relative to product $j$ at time t, conditioned on the past marketing activities as above,

$\tilde { N } ^ { j } \left( t , Y ^ { j } ( t - 1 ) , Y ^ { j } ( t - 2 ) ) , \cdots , Y ^ { j } ( t - k ) \right)$ total number of potential consumers of item $j$ at time t and subject to marketing and distributional influences $Y ^ { j } ( t - k )$ , for some $k < t ,$

$N ^ { j } ( t )$ total number of potential consumers that have purchased the item $j$ from the initial period $( \; 0 \; )$ to the present t,

$r \left( n ^ { j } ( t ) \right)$ be the net revenue function for the sale of $n ^ { j } ( t )$ units of items $j$ in period t which will include the direct marketing cost $Y ^ { j } ( t )$

The specification of suitable typified representation of the SCM decisions model permits the dynamic system structure to be formulated:

$$
M a x \quad F = \sum_ {j = 1} ^ {J} \left\{\sum_ {t = 1} ^ {T} r \left(n ^ {j} (t)\right) - \sum_ {t = 1} ^ {T} f _ {o} ^ {j} (q _ {t} ^ {j}, t) x _ {t} ^ {j} + f ^ {j} (I _ {t - 1} ^ {j}, t) / 2 \right\}\tag{1}
$$

$$
\text {s.t.} \quad I _ {t} ^ {j} = I _ {(t - 1)} ^ {j} + q _ {t} ^ {j} - D _ {t} ^ {j} - \sum_ {i \in S _ {j}} a _ {j i} q _ {t} ^ {i} \quad \forall j \in J; \quad \forall t = 1, 2, \dots , T\tag{2}
$$

$$
I _ {t} ^ {j} \geq \sum_ {i \in S _ {j}} \sum_ {\tau = 1} ^ {\min (t + v _ {j}, T)} a _ {j i} q _ {\tau} ^ {i} \quad \forall j \in J; \quad \forall \tau = 0, 1, \dots , T - 1\tag{3}
$$

$$
0 \leq h ^ {k} (q _ {t} ^ {1}, \dots , q _ {t} ^ {J}, t) \quad \forall k = 1, \dots , K _ {t}; \quad \forall t = 1, 2, \dots , T\tag{4}
$$

$$
p _ {m} ^ {j} q _ {t} ^ {j} \leq C _ {t} ^ {m _ {j}} (y _ {(t - 1)} ^ {j} + y _ {t} ^ {j}) \quad \forall j \in J; \quad t = 1, \dots , T\tag{5}
$$

$$
\sum_ {j \in \mathcal {I} _ {m}} p _ {m} ^ {j} q _ {t} ^ {j} \leq C _ {t} ^ {m} \quad m = 1, \dots , M; \quad t = 1, \dots , T\tag{6}
$$

$$
\sum_ {j \in \mathcal {I} _ {m}} y _ {t} ^ {j} \leq 1 \quad m = 1, \dots , M; \quad t = 1, \dots , T\tag{7}
$$

$$
(y _ {t} ^ {j} - y _ {(t - 1)} ^ {j}) \leq x _ {t} ^ {j} \quad \forall j \in J; \quad t = 1, \dots , T\tag{8}
$$

$$
n ^ {j} (t) = \left[ \hat {a} _ {j} + \hat {b} _ {j} \frac {N ^ {j} (t)}{\tilde {N} ^ {j} (t , Y ^ {j} (t , k))} \right] \left(\tilde {N} ^ {j} (t, Y ^ {j} (t, k)) - N (t)\right) \forall t = N + 1, \dots , \mathcal {T}\tag{9}
$$

$$
D _ {t} ^ {j} = d ^ {j} (n _ {t} ^ {j}) \quad \forall j = 1, \dots , J; \quad \forall t = N + 1\tag{10}
$$

$$
\hat {a} _ {j} = a _ {j} (t, Y ^ {j} (t - 1), k), Y ^ {j} (t)) \quad \forall j = 1, \dots , J; \quad \forall t = N + 1, \dots , \mathcal {T}\tag{11}
$$

$$
\hat {b} _ {j} = b _ {j} (t, Y ^ {j} ((t - 1), k), Y ^ {j} (t)) \quad \forall j = 1, \dots , J; \quad \forall t = N + 1, \dots , \mathcal {T}\tag{12}
$$

$$
x _ {t} ^ {j} \in \{0, 1 \}\tag{13}
$$

$$
y _ {t} ^ {j} \in \{0, 1 \} \quad \forall j \in J; \quad t = 1, \dots , T\tag{14}
$$

$$
0 \leq v _ {t} ^ {j}, q _ {t} ^ {j} \quad \forall j = 1, 2, \dots , J; \quad \forall t = 1, 2, \dots , T\tag{15}
$$

$$
0 \leq I _ {t} ^ {j}, q _ {t} ^ {j}, x _ {t} ^ {j} \quad \forall j \in J; \quad t = 1, \dots , T\tag{16}
$$

The revenue for the firm is determined from the sales of the items and inventory management costs, including production setup and holding costs in (1) over the time interval. The amounts of items acquired or produced in any period, as relevant, are given by $q _ { t } ^ { j }$ and the binary variables $x _ { t } ^ { j }$ indicate whether at time t a quantity is ordered or launched in production. The amount of items in stock available at time $t + 1$ for each good $j   =   1 , 2 , . . . , J$ are specified by $(2) - (3)$ . A set of equations (4) specify the limitations on the inventory, production or physical space limitations.

The set of equations (5) permits the production of item j to be cycled on the machine m at time t to continue the production from the preceding period if $\{ y _ { ( t - 1 ) } = 1$ without any additional setup cost for the period t, as the (8) since if $y _ { ( t - 1 ) } ^ { j } = 1 , y _ { t } ^ { j } = 1$ then $( y _ { t } ^ { j } - y _ { ( t - 1 ) } ^ { j } ) = 0$ then the binary variable $x _ { t } ^ { j } = 0$ due to the maximization of (1).

The capacity of any machine m must be sufficient to produce the desired items, considering the capacity required for each item, as indicated in (6). In the set of equations (7) the production of an item j is launched only once on a machine, while the (8) manage the eventual continuity of production, as indicated above.

The sales predicted in each period t is indicated by the (9) for each item (which also may be null). In (10) the demand for each item is derived from the sales by decomposing the ‘Gozinto’ charts, primarily on applying the (2) and (3), but actually the whole system is involved.

The number of items predicted depends on the appropriate consumer segment, depending on complex coefficients. The functional form and the parameters must be determined from the (11) and (12), while the values of the variables of the marketing mix must be determined over the time periods by maximization. The last four sets equations (13)–(16) limit the variation of most of the variables.

Due to the non stationary characteristics of the stochastic process, the cost and demand schedules will depend on the optimal level and other dynamic aspects, as well as the functional form and the parameters which should be determined. The model must be estimated and optimized simultaneously with respect to the historical data time series processes of the firm for the whole Dynamic System and the activities from $t = - T _ { H } , \cdots , 0 , 1 , \cdots , T$ , where the period $( - T _ { H } , \cdots , 0 )$ is the known historical period, while the prediction interval is specified as $( 1 , \cdots , T )$

## 3 Dynamic System Models

Dynamical Systems are useful to refine concepts and represent applications by appropriate modeling, while whole hierarchies of phenomena may be represented by such systems.

**Definition 2.** [12]: A Dynamical System is a composite mathematical object defined by the following axioms:

1. There is a given time set T, a state set X, a set of input values U, a set of acceptable input functions $\mathcal { Q } = \omega : \mathcal { Q } \rightarrow U ,$ , a set of output values Y and a set of output functions $\varGamma = \gamma : \varGamma \rightarrow Y .$

2. (Direction of time). T is an ordered subset of the reals.

3. The input space Ω satisfies the following conditions:

a) (Nontriviality). Ω is nonempty.

b) (Concatenation of inputs). An input segment $\omega _ { ( t _ { 1 } , t _ { 2 } ] } , \omega \in \mathcal { Q }$ restricted to $( t _ { 1 } , t _ { 2 } ] \cap T$ . If ω, $\omega ^ { \prime }   \in   \mathcal { Q }$ and $t _ { 1 } \; < \; t _ { 2 } \; < \; t _ { 3 }$ there is an $\omega ^ { \prime \prime }   \in   \mathcal { Q }$ such that $\omega _ { ( t _ { 1 } , t _ { 2 } ] } ^ { \prime \prime } = \omega _ { ( t _ { 1 } , t _ { 2 } ] }$ and $\omega _ { ( t _ { 2 } , t _ { 3 } ] } ^ { \prime \prime } = \omega _ { ( t _ { 2 } , t _ { 3 } ] } ^ { \prime } .$

4. There is a state transition function ϕ : $T   \times   T   \times   X   \times   \mathcal { Q } \to X$ whose value is the state $x ( t ) = \varphi ( t ; \tau , x , \omega ) \in X$ resulting at time $t \in T$ from the initial state $x = x ( \tau ) \in X$ at the initial time $\tau \in T$ under the action of the input ω $\in \varOmega . \varphi$ has the following properties:

a) (Direction of time). $\varphi$ is defined for all $t \geq \tau ,$ , but not necessarily for all $t < \tau ,$

b) (Consistency). $\varphi ( t ; t , x , \omega ) = x$ for all $t \in T$ , all $x \in X$ and all $\omega \in \varOmega ,$

c) (Composition property). For any $t _ { 1 } < t _ { 2 } < t _ { 3 }$ there results:

$$
\varphi (t _ {3}; t _ {1}, x, \omega) = \varphi (t _ {3}; t _ {2}, \varphi (t _ {2}; t _ {1}, x, \omega), \omega)
$$

for all $x \in X$ and all $\omega \in \varOmega ,$

d) (Causality). $I f \omega , \omega ^ { \prime } \in \mathcal { Q }$ and $\omega _ { ( \tau , t ] } = \omega _ { ( \tau , t ] } ^ { \prime }$ then $\varphi ( t ; \tau , x , \omega ) = \varphi ( t ; \tau , x , \omega ^ { \prime } )$

5. There is a given readout map η $: T \times X \to Y$ which defines the output $y ( t ) =$ $\eta ( t , x ( t ) )$ . The map $( \tau , t ] \rightarrow Y$ given by $\sigma \mapsto \eta ( \sigma , \varphi ( \sigma , \tau , x , \omega ) ) ,   \sigma \in ( \tau , t ] ,$ , is an output segment, that is the restriction $\gamma _ { ( \tau , t ] }$ of some $\gamma \in \varGamma \; t o \; ( \tau , t ] .$

From the accounting data and the ‘gozinto’ charts, input U and output Y sets of dated quantities are obtained. As the process may be highly nonlinear with marked lags, intermediary vectors, indicated as states $x _ { t } \; \in \; X$ are used with an opportune transition function. The effect of activities at an instant t on the state of the system is called an event, specified as $( t , x ) , t \in T , x \in X$ . A trajectory may be understood as the graph of the state as a consequence of the variation in time, given as $( t , \varphi ( x _ { t } , u _ { t } ) )$ .

A sufficiently general representation of a dynamic system may be formulated, with a slight abuse of notation, in the following way:

$$
x _ {t + 1} = \varphi (x _ {t}, u _ {t})\tag{17}
$$

$$
y _ {t} = \eta (x _ {t})\tag{18}
$$

where:

$x _ { t } \in X$ is the vector of the state of the dynamical system at period t

$u _ { t } \in U$ is the vector of the control variables of the dynamical system at period t

$y _ { t } \in Y$ is the vector of the output of the dynamical system at period t

Dynamical systems are based on intermediary set of states and transition func tions, by applying the simultaneous estimation and optimization algorithm to determine the State set X and the transition function [19]. Under appropriate conditions the representation of the system will result unique, as will be indicated below.

**Definition 3.** Given two states $x _ { t _ { 0 } }$ and $\hat { x } _ { t _ { 0 } }$ belonging to systems S and $\hat { S }$ which may not be identical, but have a common input space Ω and output space Y, the two states are said to be equivalent if and only if for all input segments $\omega _ { [ t _ { 0 } , t ) } \in \varOmega$ the response segment of S starting in state $x _ { t _ { 0 } }$ is identical with the response segment of S starting ˆ in state $\hat { x } _ { t _ { 0 } } ;$ that is

$$
x _ {t _ {0}} \cong \hat {x} _ {t _ {0}} \Leftrightarrow \eta (t, \varphi (x _ {t _ {0}}, \omega_ {[ t _ {0}, t ]})) = \hat {\eta} (t, \hat {\varphi} (\hat {x} _ {t _ {0}}, \omega_ {[ t _ {0}, t ]})) \quad \forall t \in T, t _ {0} \leq t, \forall \omega_ {[ t _ {0}, t ]} \in S, \hat {S}\tag{19}
$$

The systems $S$ and $\hat { S }$ may be two representations of a SCM system and their policies.

**Definition 4.** A system is in reduced form if there are no distinct states in its state space which are equivalent to each other.

Suppose the actual system consists in reduced form, derivable from the firm’s data base.

**Definition 5.** Systems S and $\hat { S }$ are equivalent $S \equiv { \hat { S } }$ if and only if to every state in the state space of S there corresponds an equivalent state in the state space $o f \hat { S }$ and vice versa.

Remark 1. Certain aspects of the SCM representation and the policy that entails should be determined:

1. Can a certain state $s ^ { * } \in S$ be reached from the present state, or if the dynamical system attains a given state $x _ { t }$ at time $t = 0$ can it also be made to reach a certain state $x ^ { * }$ . Evidently it is required to determine the set of states reachable from a specific state $x _ { t }$

2. Can a dynamical system be driven to a given state by an input $u _ { t }$ . Controllability is concerned with the connectedness properties of the system representation.

3. Reachability and controllability lead naturally to the determination of a dynamical system’s observability, which provides the conditions to determine the given actual state uniquely.

4. The stability of the system is important since it provides conditions on the way the trajectories will evolve a given perturbation or an admissible control.

Reachability, controllability and stability are seldom formally examined in SCM policy formulation, although at every period, exogenous events can arise to nullify even the best plan formulated, because the controllability of the system was not researched. So these aspects should be studied to ensure the feasibility of the SCM policy.

**Definition 6.** Simple and multiple experiments involve different sets of input/output pairs:

A simple experiment is an input/output pair $( u _ { [ t _ { 0 } , t ) } , y _ { [ t _ { 0 } , t ) } )$ that is, given the system in an unknown state an input $u _ { [ t _ { 0 } , t ) }$ is applied over the interval of time $( t _ { 0 } , t )$ and the output $y _ { [ t _ { 0 } , t ) }$ is observed.

• A multiple experiment of size M consists of M input/output pairs $( u _ { [ t _ { 0 } , t ) } ^ { i } , y _ { [ t _ { 0 } , t ) } ^ { i } \; i =$ $1 , 2 , . . . , M )$ where on applying on the i-th realization of the M systems the input $( u _ { [ t _ { 0 } , t ) } ^ { i } ) _ { i }$ , the i-th output $y _ { [ t _ { 0 } , t ) } ^ { i }$ is observed.

While a simple experiment is thought as a stimulus and response experiment, multiple experiments are more complex and define multi-determined reactions, such as synergisms of the system.

**Definition 7.** A system is simply (multiple) observable at state $x _ { t _ { 0 } }$ if and only if a simple experiment (a multiple experiment) permits the determination of that state uniquely.

**Definition 8.** Equivalence of dynamic systems can be distinguished:

• Two systems are simply equivalent if it is impossible to distinguish them by any simple experiment.

• Two systems are multiply equivalent if it is impossible to distinguish them by any multiple experiment.

**Theorem 1.** [12]: If two systems are multiply equivalent then they are equivalent.

**Definition 9.** A system is initial-state determinable if the initial state $x _ { 0 }$ can be determined from an experiment on the system started at $x _ { 0 }$

**Theorem 2.** [12]: A system is in reduced form if and only if it is initial-state determinable by an infinite multiple experiment.

The Definitions 6–9 and the results given in Theorems 1–2 formally justify the possibility of defining one or more representations of the dynamical system. The distinction between systems that are simply equivalent and multiply equivalent is crucial, as comparative static or equilibrium models will be simply equivalent, while for the analysis of dynamical systems which are multiple equivalent allow to compare different representations and determine the optimal trajectory for the system.

Thus consider,

**Definition 10.** An ex ante solution is a solution formed in a given period t based on anticipated outcome of future activities maturing in period t + 1 and consists of the forecast of the optimal values of the control variables.

**Definition 11.** An ex post solution is a solution formed in a given period t, regarding outcomes of activities maturing in period t + 1 which are assumed known (with foreknowledge), in period t so as to determine the optimal values of the control variables in period t + 1.

Let a phenomenon be represented by a multiply equivalent dynamic system in an initial-state determinable and the state in period t + 1 be predicted in period t. The state at t + 1 may be obtained from a representation of another copy of such a system in the period $t + 1$ . The state of period t + 1 predicted in period t on the basis of the knowledge in the same period, will be equivalent to the state at period $t + 1$ on the basis of the knowledge at period t + 1, which is indicated as the ex post state.

**Theorem 3.** An ex ante multiply equivalent Dynamic system in an initial-state is equivalent to an ex post system, also a multiply equivalent dynamic system in an initial-state.

**Proof**: By Theorem 1 the ex ante dynamical system is multiply equivalent and its initial state is in reduced form by Theorem 2.

Furthermore by the same reasoning the ex post dynamical system is also a multiply equivalent and its initial state is in reduced form.

By Definitions 4 and 5 they are state equivalent.

**Corollary 1.** A Certainty Equivalent solution consists of an optimal solution to an optimization problem determined as an ex ante solution in the control variables $u ^ { * }$ which are also optimal ex post.

The state of the systems are equivalent if the state transition functions do not exhibit significant random variation. The eventual random variation will be negligible, but the expected value of the disturbances in both cases will assume null values while the variance of the processes may be positive, but the autocorrelation and cross-correlation must be zero and the processes are stationary.

This formulation is analogous to the properties derived earlier by different methods [18, 20].

No limitations have been enforced for the output equations (18). The random disturbances of these forms may vary. The income resulting, as an output variable may differ, due to disturbances, although optimal solution values of the control variables will be identical in the two processes.

The SCM dynamic estimation problems and optimal policy determination should be formulated by such an approach with a data driven formulation.

## 4 Specification of the Statistical Properties

All the statistical properties of given estimates of the residuals should be fulfilled at every iteration, so suitable constraints must be defined, together with the specification of the model of the phenomenon and the global optimization problem should be solved for all the undetermined variables. Thus a number of independent statistical properties must be satisfied, which may be represented as:

$$
\gamma (x _ {i + 1}, x _ {t}, u _ {i}, y _ {t + 1}, y _ {t}, w _ {t}, v _ {t}, \theta_ {1}, \theta_ {2}) \geq 0 \quad t = 1, 2, \dots , T\tag{20}
$$

where:

$w _ { t } , \nu _ { t }$ are random residual disturbances, to be determined so that a number of conditions specified in the set of equations (20) are satisfied,

$\theta _ { 1 } , \theta _ { 2 }$ are parameters to specify the system, such that the conditions specified by (20) are satisfied.

The set of statistical conditions that the residuals must satisfy to obtain the correct estimates are the following [8]:

1. The parameter estimates are unbiased, this means that:

• As the size of the data set grows larger, the estimated parameters tend to the asymptotic (true) values.

2. The parameter estimates are consistent, which require the following conditions to be satisfied:

• The estimated parameters are asymptotically unbiased,

• The variance of the parameter estimate must tend to zero as the data set tends to infinity.

3. The parameter estimates are asymptotically efficient,

• The estimated parameters are consistent,

• The estimated parameters have smaller asymptotic variance as compared to any other consistent estimator.

4. The residuals have the smallest possible variance and to ensure that this is so:

The variance of the residuals must be minimum,

• The residuals must be homoscedastic,

• The residuals must not be serially correlated.

5. The residuals are unbiased (have zero mean).

6. The residuals have a non informative distribution (usually, the Gaussian distribution). If the distribution of the residuals is informative, the extra information could somehow be exploited by reducing the variance of the residuals, their bias etc. with the result that better estimates are obtained.

Through a correct implementation of statistical estimation techniques, a set of equation (20) can be specified. The parameter estimates are as close as possible to their asymptotic (true) values, all the information that is available is used to determine precise estimates, so the residual uncertainty and the approximation in the data fit is reduced to the maximum extent possible. Thus the estimates of the parameters, which satisfy all these conditions, are the ‘best’ possible in a ‘technical sense’ [1].

To the SCM algorithm to determine the optimal policy, indicated by the system (1)–(16) must be added the statistical conditions described above. This can be indicated, for clarity as:

$$
\text {Min} \quad J = \sum_ {t = 1} ^ {T} c (x _ {t}, u _ {t}, y _ {t})\tag{21}
$$

$$
x _ {t + 1} = \varphi (x _ {t}, u _ {t}, y _ {t}, w _ {t}: \theta_ {1}) \quad t = - T _ {H}, \dots , 0, 1, 2, \dots , T - 1\tag{22}
$$

$$
y _ {t + 1} = \eta (x _ {t}, u _ {t}, v _ {t}: \theta_ {2}) \quad t = - T _ {H}, \dots , 0, 1, 2, \dots , T - 1\tag{23}
$$

$$
0 \leq \gamma (x _ {t + 1}, x _ {t}, u _ {t}, y _ {t + 1}, y _ {t}, w _ {t}, v _ {t}, \theta_ {1}, \theta_ {2}), t = - T _ {H}, \dots , 0, 1, \dots , T - 1\tag{24}
$$

where the system has been expressed as a coherent dynamical system reformulated from system (1)–(16) and the statistical conditions constrains that have been specified summarily above.

For major clarity, but with no loss of generality, in this representation, opportune terms are added to each expression as residuals $w _ { t } , \; \nu _ { t }$ and parameters $\theta _ { 1 } ,   \theta _ { 2 }$ to be determined to satisfy the conditions.

By recursing on the specifications, i.e. by changing the functional form, and increasing the number of independent variables considered, better and better fits can be obtained, both with regard to the historical data and the predicted optimal control policy, so the optimal control problem (21)–(24) will be solved iteratively.

The mathematical program will be formulated with respect to the residual variables, but it is immediate that for a given functional form, the unknown parameters will be specified and thus the unknowns of the problem will also be defined and available. Thus the mathematical program is fully specified for each functional form to be considered.

In fact the residual terms are given from the (22) and (23) as:

$$
\begin{array}{l l} w _ {t} = \hat {x} _ {t + 1} - \varphi_ {h} (\hat {x} _ {t}, \hat {u} _ {t}, \hat {y} _ {t}: \theta_ {1}) & t = - T _ {H}, \dots , 0, 1, 2, \dots , T - 1, \quad h \in \Omega \\ v _ {t} = \hat {y} _ {t + 1} - \eta_ {k} (x _ {t}, u _ {t}, v _ {t}: \theta_ {2}) & t = - T _ {H}, \dots , 0, 1, 2, \dots , T - 1, \quad k \in \Gamma \end{array}\tag{25}
$$

(26)

where ˆ., as usual indicates the historical values of a variable and thus suitable values of $\theta _ { 1 } , \theta _ { 2 }$ must be determined by the mathematical program, such that all the constraints expressed in terms of $w _ { i } , \nu _ { i } \; \forall i$ are specified.

The constraints which are added regarding the residuals imply the satisfaction of the moments of the Gaussian distribution function [8].

Remark 2. The proposed algorithm dominates the traditional procedures. The algorithm determines always a solution which satisfies all the statistical conditions posed, if the system is feasible, or no solution is determinable.

This solution will ensure that the parameter estimates are unbiased, consistent, asymptotically efficient estimates with minimum variance and the residuals have finite variance and are unbiased. If the estimates determined are sufficiently precise, which can be obtained by appropriate modifications in the model specification, certainty equivalence of the solution will be satisfied by Corollary 1.

## 5 Computational Results

The SCM problem are traditionally formulated as a three stage problem in which the functional form and the parameters estimates are considered known, so that the optimal policy can be determined conditioned on these aspects. Potential uncertainties are not considered ex ante which will render the ex post solution unacceptable, as Theorem 3 is not satisfied.

A Dynamical system formulation of the model, determined by a simultaneous estimation and optimization system as described in Sect. 4, the global objective function will consist of the maximization of the revenue over an interval of time. The state and input output system equations are formulated for each stage consecutively. All the variables must be integrated in a global structure, redefined in a coherent consistent way [8] so that the solution will satisfy all the statistical conditions, as in Remark 2 and the optimal solution will consequently satisfy Theorem 3.

The aim of this section is to show by an application that all the results of this paper are fulfilled. Of course extensive experiments are deemed, but these results are useful to show this objective.

This approach was implemented and solved with the algorithm and for comparison purposes two commercial routines: Lancelot, [7] and Cplex [4] were used with differing estimation procedures.

A simulation of a firm was carried out for illustrative purposes, represented by 48 variables and 18 control variables derived from the system (1)–(16). Also 23 relationships were obtained for the system by considering 2 raw materials, 2 production units and 2 marketing mix variables each consisting of five marketing variables with regard to two manufactured goods.

The 48 variables represent the state variables and the output variables at each period, such as the stock of the two manufactured goods, two raw materials and semi manufactured items, as well as the labor employed on each production unit and the number of individuals who will purchase a manufactured good in that period, the revenue and costs in the period and so on. Instead the 18 control variables for each period include the 10 marketing variables and the price levels chosen and the intermediary six items to carry out the production.

Many non linear and dynamic relationships were introduced in the simulation, as evident in Fig. 1. On the basis the optimal policy for the next six periods the optimal policies were determined and compared.

![](images/page_86_chart_8.jpg)

Fig. 1. Time series for income in monetary units

The following algorithms were implemented and the results are shown in Tables 1–3 and in Fig. 2:

1. The average values of the coefficients were obtained from the dated values of the perturbed coefficients, used in the simulation, to specify the non linear system to be solved for the next 6 periods with Lancelot, applying the non linear model. The income obtained was 211,227,602 m.u.(monetary units) over the six periods.

2. The estimation of the parameters of the system was determined by S.P.S.S. based on the simulation data set. The optimal solution over the same is determined by a linear system since it is solved by the Cplex linear program, and an income of 197,167,817 m.u on six periods were predicted.

3. The **C.A.s.S.a.n.D.r.A.** routine was applied on the data set to solve the simultaneous estimation and optimization problem regarding the dynamic relationships for the prediction over the next six periods, with a predicted income of 217,708,547 m.u.

In the first implementation, the model is influenced by random variation and dy namic effects, yet the non linear specification of the system leads to an improvement of 7.13% over the second implementation. The effect of applying dynamic parameters and non linear relationships in **C.A.s.S.a.n.D.r.A.** leads to a further improvement of 4.02% over the first implementation, while the aggregate improvement of this non linear implementation over the linearized three stages implementation was 11.15%.

The Lancelot solution yields a haphazard unstable development path, probably not acceptable to Management, but it reflects the behavior of the income curve in the past. These aspects are consequential to the approach consisting of three stages as indicated in Sect. 1 and Remark (1 sub 4).

The improvement in performance with a simultaneous estimation and optimization approach is relevant, as indicated in Sect. 3, while the consideration of linear modelization leads to relevant inefficiencies.

![](images/page_87_chart_8.jpg)

Fig. 2. Comparisons of SCM plans for different implementations

The Cplex implementation provides a linear growth of income, due to the use of a linear program as the optimization instrument and an estimation process linear in the parameters, so the ex ante solution may be comforting as an equilibrium growth could be appreciated but this solution is unrealistic and inefficient.

The growth trajectory indicated by the **C.A.s.S.a.n.D.r.A.** routine is stable and provides the best results in apparent adverse market conditions. The ex ante solution obtained is equivalent to the ex post solution, as Theorem 3 and Corollary 1 hold and is confirmed by numeric values.

Table 1. Prediction of optimal activities for six periods: Lancelot and Cplex algorithms

<table><tr><td></td><td colspan="6">Lancelot</td></tr><tr><td>Variable</td><td>pd.1</td><td>pd.2</td><td>pd.3</td><td>pd.4</td><td>pd.5</td><td>pd. 6</td></tr><tr><td> $Y_{a}^{1}(t)$ </td><td>185.0</td><td>191.8</td><td>192.0</td><td>192.3</td><td>192.0</td><td>192.6</td></tr><tr><td> $Y_{b}^{1}(t)$ </td><td>199.1</td><td>199.0</td><td>199.0</td><td>199.9</td><td>199.1</td><td>199.0</td></tr><tr><td> $Y_{c}^{1}(t)$ </td><td>199.0</td><td>199.0</td><td>199.0</td><td>199.0</td><td>199.1</td><td>199.1</td></tr><tr><td> $Y_{d}^{1}(t)$ </td><td>199.0</td><td>199.1</td><td>199.1</td><td>199.0</td><td>199.1</td><td>199.1</td></tr><tr><td> $Y_{e}^{1}(t)$ </td><td>177.8</td><td>181.3</td><td>198.0</td><td>199.2</td><td>199.7</td><td>199.1</td></tr><tr><td> $Y_{f}^{1}(t)$ </td><td>14,103.0</td><td>14,103.0</td><td>14,103.0</td><td>14,103.0</td><td>14,103.0</td><td>14,103.0</td></tr><tr><td> $Y_{a}^{2}(t)$ </td><td>186.0</td><td>194.1</td><td>200.0</td><td>204.9</td><td>204.9</td><td>214.3</td></tr><tr><td> $Y_{b}^{2}(t)$ </td><td>186.0</td><td>196.1</td><td>202.3</td><td>206.9</td><td>206.9</td><td>214.3</td></tr><tr><td> $Y_{c}^{2}(t)$ </td><td>199.0</td><td>199.0</td><td>199.0</td><td>199.0</td><td>199.0</td><td>199.0</td></tr><tr><td> $Y_{d}^{2}(t)$ </td><td>161.4</td><td>162.1</td><td>180.0</td><td>212.6</td><td>212.6</td><td>308.2</td></tr><tr><td> $Y_{e}^{2}(t)$ </td><td>1,532.0</td><td>1,532.0</td><td>1,532.0</td><td>1,532.0</td><td>1,532.0</td><td>1,532.0</td></tr><tr><td> $Y_{f}^{2}(t)$ </td><td>15,852.0</td><td>15,852.0</td><td>15,852.0</td><td>15,852.0</td><td>15,852.0</td><td>15,852.0</td></tr><tr><td> $q_{t}^{1}$ </td><td>667.0</td><td>667.0</td><td>667.0</td><td>667.0</td><td>667.0</td><td>667.0</td></tr><tr><td> $q_{t}^{2}$ </td><td>47.2</td><td>204.0</td><td>205.0</td><td>204.0</td><td>204.9</td><td>204.9</td></tr><tr><td> $q_{t}^{3}$ </td><td>47.2</td><td>504.0</td><td>205.0</td><td>204.9</td><td>204.9</td><td>204.9</td></tr><tr><td> $q_{t}^{4}$ </td><td>208.0</td><td>19.6</td><td>196.4</td><td>199.0</td><td>199.0</td><td>204.4</td></tr><tr><td> $q_{t}^{5}$ </td><td>61.7</td><td>17.0</td><td>15.2</td><td>230.7</td><td>230.7</td><td>210.3</td></tr><tr><td> $q_{t}^{6}$ </td><td>0.0</td><td>14.4</td><td>10.7</td><td>0.0</td><td>0.0</td><td>75.1</td></tr><tr><td>Revenue(000)</td><td>33,135.3</td><td>36,642.6</td><td>149,409.0</td><td>2,982.4</td><td>3,029.6</td><td>3,028.7</td></tr></table>

Some control variables $Y _ { f } ^ { 1 } ( t ) , Y _ { f } ^ { 2 } ( t )$ which are the prices to be levied for the manufactured goods are analogous in the three implementations, while other control variables exhibit pronounced variation between implementations, while for specific control variables variation within an implementation may be large.

For the first two implementations the differences in many of the control variables are large, while incomes are very close, except in one period, which implies that multiple policies can be determined with very different control variables. There also seems to be a multiplicative factor in the values of the control variables for the policy determined for the **C.A.s.S.a.n.D.r.A.** algorithm compared to the Lancelot policy. However, except for one period, which could be considered an outlier, the income of the former policy is an improvement between 20-50%.

Table 2. Prediction of optimal activities for six periods: Lancelot and Cplex algorithms

<table><tr><td></td><td colspan="6">Cplex</td></tr><tr><td>Variable</td><td>pd.1</td><td>pd.2</td><td>pd.3</td><td>pd.4</td><td>pd.5</td><td>pd. 6</td></tr><tr><td> $Y_{a}^{1}(t)$ </td><td>7,411.0</td><td>7,123.0</td><td>7,491.0</td><td>7,061.0</td><td>6,924.0</td><td>7,023.0</td></tr><tr><td> $Y_{b}^{1}(t)$ </td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td></tr><tr><td> $Y_{c}^{1}(t)$ </td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td></tr><tr><td> $Y_{d}^{1}(t)$ </td><td>9,950.0</td><td>9,950.0</td><td>9,950.0</td><td>9,950.0</td><td>9,950.0</td><td>9,950.0</td></tr><tr><td> $Y_{e}^{1}(t)$ </td><td>4,000.0</td><td>4,000.0</td><td>4,000.0</td><td>4,000.0</td><td>4,000.0</td><td>4,000.0</td></tr><tr><td> $Y_{f}^{1}(t)$ </td><td>14,103.0</td><td>14,103.0</td><td>14,103.0</td><td>14,103.0</td><td>14,103.0</td><td>14,103.0</td></tr><tr><td> $Y_{a}^{2}(t)$ </td><td>60,000.0</td><td>60,000.0</td><td>60,000.0</td><td>60,000.0</td><td>60,000.0</td><td>60,000.0</td></tr><tr><td> $Y_{b}^{2}(t)$ </td><td>1.0</td><td>1.0</td><td>1.0</td><td>1.0</td><td>1.0</td><td>1.0</td></tr><tr><td> $Y_{c}^{2}(t)$ </td><td>2.0</td><td>2.0</td><td>2.0</td><td>2.0</td><td>2.0</td><td>2.0</td></tr><tr><td> $Y_{d}^{2}(t)$ </td><td>4.0</td><td>4.0</td><td>4.0</td><td>4.0</td><td>4.0</td><td>4.0</td></tr><tr><td> $Y_{e}^{2}(t)$ </td><td>22,153.0</td><td>17,124.0</td><td>26,210.0</td><td>14,509.0</td><td>36,656.0</td><td>17,565.0</td></tr><tr><td> $Y_{f}^{2}(t)$ </td><td>15,852.0</td><td>15,852.0</td><td>15,852.0</td><td>15,852.0</td><td>15,852.0</td><td>15,852.0</td></tr><tr><td> $q_{t}^{1}$ </td><td>8,900.0</td><td>8,900.0</td><td>8,900.0</td><td>8,900.0</td><td>8,900.0</td><td>8,900.0</td></tr><tr><td> $q_{t}^{2}$ </td><td>2,220.0</td><td>2,220.0</td><td>2,220.0</td><td>2,220.0</td><td>2,220.0</td><td>2,220.0</td></tr><tr><td> $q_{t}^{3}$ </td><td>8,900.0</td><td>8,900.0</td><td>8,900.0</td><td>8,900.0</td><td>8,900.0</td><td>8,900.0</td></tr><tr><td> $q_{t}^{4}$ </td><td>1,000.0</td><td>1,000.0</td><td>1,000.0</td><td>1,000.0</td><td>1,000.0</td><td>1,000.0</td></tr><tr><td> $q_{t}^{5}$ </td><td>50.0</td><td>50.0</td><td>50.0</td><td>50.0</td><td>50.0</td><td>50.0</td></tr><tr><td> $q_{t}^{6}$ </td><td>5,510.0</td><td>5,510.0</td><td>5,510.0</td><td>5,510.0</td><td>5,510.0</td><td>5,510.0</td></tr><tr><td>Revenue(000)</td><td>32,862.0</td><td>32,861.9</td><td>32,860.8</td><td>32,861.1</td><td>32,860.7</td><td>32,861.1</td></tr></table>

The stability of the solution of **C.A.s.S.a.n.D.r.A.** is due to the certainty equivalent requirement, as with differing dynamic lags, the residual variance was always of order $0 . 8 \times 1 0 ^ { - 9 }$ and the estimated model is extremely close to the actual model. This was verified in a number of implementations with different initial points and different initial models. In the S.P.S.S. application, the least residual variance was $0 . 7 \times 1 0 ^ { 6 }$ , which is reasonable as the data values vary and are very large.

Table 3. Prediction of optimal activities for six periods: Cassandra algorithm

<table><tr><td></td><td colspan="6">Cassandra</td></tr><tr><td>Variable</td><td>pd.1</td><td>pd.2</td><td>pd.3</td><td>pd.4</td><td>pd.5</td><td>pd. 6</td></tr><tr><td> $Y_{a}^{1}(t)$ </td><td>8,915.0</td><td>8,915.0</td><td>8,915.0</td><td>0.0</td><td>8,915.0</td><td>8,915.0</td></tr><tr><td> $Y_{b}^{1}(t)$ </td><td>8,915.0</td><td>8,915.0</td><td>8,915.0</td><td>8,195.0</td><td>8,915.0</td><td>8,915.0</td></tr><tr><td> $Y_{c}^{1}(t)$ </td><td>8,985.0</td><td>8,985.0</td><td>8,985.0</td><td>0.0</td><td>8,985.0</td><td>8,985.0</td></tr><tr><td> $Y_{d}^{1}(t)$ </td><td>9,950.0</td><td>9,950.0</td><td>9,950.0</td><td>0.0</td><td>9,950.0</td><td>9,950.0</td></tr><tr><td> $Y_{e}^{1}(t)$ </td><td>4,000.0</td><td>4,000.0</td><td>4,000.0</td><td>1.0</td><td>4,000.0</td><td>4,000.0</td></tr><tr><td> $Y_{f}^{1}(t)$ </td><td>14,103.0</td><td>14,103.0</td><td>14,103.0</td><td>14,103.0</td><td>14,103.0</td><td>14,103.0</td></tr><tr><td> $Y_{a}^{2}(t)$ </td><td>60,000.0</td><td>60,000.0</td><td>60,000.0</td><td>1.0</td><td>60,000.0</td><td>60,000.0</td></tr><tr><td> $Y_{b}^{2}(t)$ </td><td>60,000.0</td><td>60,000.0</td><td>60,000.0</td><td>1.0</td><td>60,000.0</td><td>60,000.0</td></tr><tr><td> $Y_{c}^{2}(t)$ </td><td>58,208.0</td><td>58,208.0</td><td>58,208.0</td><td>2.0</td><td>58,208.0</td><td>58,208.0</td></tr><tr><td> $Y_{d}^{2}(t)$ </td><td>61,628.0</td><td>61,628.0</td><td>61,628.0</td><td>4.0</td><td>61,628.0</td><td>61,628.0</td></tr><tr><td> $Y_{e}^{2}(t)$ </td><td>37,276.0</td><td>37,276.0</td><td>37,276.0</td><td>156.0</td><td>37,276.0</td><td>37,276.0</td></tr><tr><td> $Y_{f}^{2}(t)$ </td><td>15,852.0</td><td>15,852.0</td><td>15,852.0</td><td>15,852.0</td><td>15,852.0</td><td>15,852.0</td></tr><tr><td> $q_{t}^{1}$ </td><td>8,900.0</td><td>8,900.0</td><td>8,900.0</td><td>170.0</td><td>8,900.0</td><td>8,900.0</td></tr><tr><td> $q_{t}^{2}$ </td><td>9,900.0</td><td>9,900.0</td><td>9,900.0</td><td>222.0</td><td>9,900.0</td><td>9,900.0</td></tr><tr><td> $q_{t}^{3}$ </td><td>8,900.0</td><td>8,900.0</td><td>8,900.0</td><td>500.0</td><td>8,900.0</td><td>8,900.0</td></tr><tr><td> $q_{t}^{4}$ </td><td>1,000.0</td><td>1,000.0</td><td>1,000.0</td><td>50.0</td><td>1,000.0</td><td>1,000.0</td></tr><tr><td> $q_{t}^{5}$ </td><td>1,000.0</td><td>1,000.0</td><td>1,000.0</td><td>50.0</td><td>1,000.0</td><td>1,000.0</td></tr><tr><td> $q_{t}^{6}$ </td><td>5,510.0</td><td>5,510.0</td><td>5,510.0</td><td>250.0</td><td>5,510.0</td><td>5,510.0</td></tr><tr><td>Revenue(000)</td><td>46,591.2</td><td>26,988.7</td><td>26,988.7</td><td>19,904.5</td><td>59,649.7</td><td>39,585.7</td></tr></table>

The result obtained is encouraging and is in line with the methodological results that have been expressed in Corollary 1, so further experimentation seems to be worthwhile [8].

It follows from Theorem 3 that the ex ante solution is optimal compared to the ex post solution, since all the conditions of the theorem and the preceding ones are verified by the **C.A.s.S.a.n.D.r.A.** algorithm.

Experimental comparisons cannot be carried out, since multiple copies of a real firm are never available and balanced experiments performed on random selections of multiple cases cannot be carried out in practice. It would seem that comparisons of different algorithms, as proposed here, could never be carried out by realistic experiments, but the approach formulated in this paper permits the formulation of an instrumentalist approach isomorphically to proposed realistic experiments.

Suppose that an SCM over a number of periods is formulated with **C.A.s.S.a.n.D. r.A.**. The solution is certainty equivalent, as indicated in Corollary 1. Further other systems based on other assumptions may be formulated with similar precision if possible. Depending on their assumed structure simple or multiply equivalent systems will be formulated, as indicated in Definition 5. Various ex ante solutions may be determined which can be compared to the ex ante solution of the **C.A.s.S.a.n.D.r.A.** algorithm, which is a proxy solution to the ex post solution (Theorem 3).

If a single experimental firm is available, the **C.A.s.S.a.n.D.r.A.** ex ante policy can be enacted and this policy can be compared to the expost optimal solution determined at the end of the interval. The latter should be similar to the ex ante solution and the comparative results with other solutions will indicate the efficiency of the different approaches.

Clearly this experiment is isomorphic to a complete multiple experiment carried out on the equivalent of many copies of experimental firms.

## 6 Conclusions

A Supply Chain Management system can be modeled by nonlinear stochastic and dynamical systems, to avoid suboptimization arising from simplifications in the representation. The analysis may be carried out at the highest level of generality with as few a priori assumptions as possible. Data Driven modeling system should be used rather than refer to managerial insights and anecdotal evidence.

Stochastic disturbances and exogenous events may modify the trajectories of de velopment so that the reachability of the goals should be ascertained periodically. Also the controllability of the system must be checked periodically to ensure that the system can still be controlled to achieve the desired aim. As the dynamic SCM system will inevitably be subject to uncertainty, accurate plans may only be defined by considering the properties of the dynamical system in a certainty equivalent context.

Within the Mathematical System framework presented in this paper, all the important aspects described above can be verified and by ensuring, when possible, that multiply equivalent systems are derived, so optimal solutions, both ex ante and ex post are determined, even though the output results may differ somewhat, without influencing the optimal solution.

This methodology allows, multiply equivalent systems to be determined, so that the system can be embedded in an optimal control problem and determine a certainty equivalent optimal solution. Precise alternative experiments can be effected and different exogenous factors may be evaluated precisely.

This approach seems to be useful for the modeling of SCM to determine precise policies.

## References

[1] T. Amemiya. Advanced Econometrics. Blackwell, Oxford, 1985.

[2] J.-P. Aubin. Viability Theory. Birkhäuser, Boston, 1991.

[3] F. M. Bass, T. V. Krishnan, and D. C. Jain. Why the bass model fits without decision variables. Marketing Science, 3:203–223, 1994.

[4] R. E. Bixby. Implementing the simplex method: the initial basis. Journal of Computing, 4:267–284, 1992.

[5] E. S. Buffa. Modern Production Management. Wiley, New York, 1977.

[6] C. Chatfield. Model uncertainty, data mining and statistical inference. Journal of the Royal Statistical Soc. Series A, 158:419 – 466, 1995.

[7] A. R. Conn, N. I. M. Gould, and P. L. Toint. Trust-Region Methods. MPS-SIAM, Philadelphia, 2000.

[8] L. Di Giacomo and G. Patrizi. Dynamic nonlinear modelization of operational supply chain systems. Journal of Global Optimization, 34:503–534, 2006.

[9] L. Di Giacomo and G. Patrizi. Foundations of supply chain management: towards a normative theory of supply and demand chain management. submitted for pubblication, 2007.

[10] J. Gondzio, R. Sarkissian, and J.-Ph. Vial. Parallel implementation of a central decomposition method for solving large scale planning problems. Computational Optimization and Applications, 19:5–29, 2001.

[11] G. Hadley and T. M. Whithin. Analysis of Inventory Systems. Prentice-Hall, Englewood Cliffs, N. J., 1963.

[12] R. E. Kalman, P. L. Falb, and M. A. Arbib. Topics in Mathematical System Theory. McGraw-Hill, New York, 1969.

[13] A. Kimms. Multi-level Lot Sizing and Scheduling - Methods for Capacitated, Dynamic and Deterministic Models. Physica Verlag, Heidelberg, 1997.

[14] V. Mahajan, E. Muller, and R. V. Srivastava. Using innovation diffusion models to develop adopter catagories. Journal of Marketing Research, 11:37–50, 1990.

[15] A. Nagurney, J. Cruz, and D. Matsypura. Dynamics of global supply chain supernetworks. Mathematical and Computer Modelling, 37:963–983, 2003.

[16] A. Nagurney, K. Fe, J. Cruz, K. Hancock, and F. Southworth. Dynamics of supply chains: a multilevel (logistical/informational/financial) network perspective. Environment and Planning, B29:795–818, 2000.

[17] G. Patrizi. S.O.C.R.A.t.E.S. simultaneous optimal control by recursive and adaptive estimation system: Problem formulation and computational results. In M. Lassonde, editor, Optimization and Approximation, Vth International Conference on Approximation and Optimization in the Carribean. Springer Verlag, Berlin, 2000.

[18] H. A. Simon. Dynamic programming under uncertainty with a quadratic criterion function. Econometrica, 24:74–81, 1956.

[19] T. Söderström and P. Stoica. System Identification. Prentice-Hall, Englewood Cliffs, N.J., 1989.

[20] H. Theil. A note on certainty equivalence in dynamic programming. Econometrica, 25:346–349, 1957.

# Ship Routing and Scheduling with Persistence and Distance Objectives

Kjetil Fagerholt<sup>1,2,3</sup>, Jarl Eirik Korsvik<sup>3</sup>, and Arne Løkketangen<sup>4</sup>

1 Industrial Economics and Technology Management, Norwegian University of Science and Technology, Norway kjetil.fagerholt@iot.ntnu.no

2 Norwegian Marine Technology Research Institute (MARINTEK), Norway

3 Department of Marine Technology, Norwegian University of Science and Technology, Trondheim, Norway korsvik@ntnu.no

4 Department of Informatics, Molde University College, Norway Arne.Lokketangen@hiMolde.no

**Summary.** It is well known that decision support systems (DSSs) usually only solve models that simplify and approximate the real problem. The planners might therefore be more interested in a set of diverse high quality solutions to choose from, than in only the optimal (or near-optimal) solution to the model as is usually produced by a DSS. In ship routing and scheduling plans are generated following a rolling horizon principle, where schedules are updated when new relevant information appears. However, the planners have often already made commitments to the customers for the next few voyages, for instance regarding arrival times and which ships that are assigned to service given cargoes. Therefore, the planners are interested in a set of high quality schedules that are close to the current (baseline) schedule in the near future, and diverse from each other in more distant time. We suggest a multi-start heuristic, including a persistence penalty function and distance measures, to produce such schedules. The method has been tested on a set of real-life problems and it provides valuable decision support flexibility for planners in shipping companies.

**Key words:** Ship routing and scheduling, Decision support, Distance measure, Persistence

## 1 Introduction

Ocean shipping is the major transportation mode in international trade and more than 6 billion tons of goods are carried by ships every year [15]. A ship involves a major capital investment, and its daily income and operating costs often amount to several thousands of dollars. Proper planning of the fleet of vessels is therefore crucial for shipping companies to survive in an increasingly competitive market.

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">L. Bertazzi et al. (eds.), Innovations in Distribution Logistics, Lecture Notes in Economics and Mathematical Systems 619, DOI: 10.1007/978-3-540-92944-4,</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">-c 2009 Springer-Verlag Berlin Heidelberg</span></small>

In this paper we focus on decision support for short-term routing and scheduling problems faced by many tramp shipping companies transporting bulk products. A shipping company operating in the tramp market usually has a set of mandatory contract cargoes that they are committed to carry, while trying to increase their profit from optional spot cargoes. The mandatory contract cargoes come from long-term contracts between the shipping company and the cargo owners (shippers). Each cargo (contract and spot) consists of a given quantity to be shipped between a given pair of ports. There are given time windows for loading of the cargoes and sometimes also for unloading. The fleet used for transporting the cargoes is heterogeneous where the ships have different load capacities, speeds, equipment, etc. The ship routing and scheduling problem mainly deals with (1) selecting spot cargoes to service, (2) assigning cargoes to ships in the fleet, and (3) deciding optimal ship routes and schedules. All these tasks must in principle be performed simultaneously. The planners in the shipping companies daily solve this ship routing and scheduling problem, which is basically similar to a multi-vehicle pickup and delivery problem with time windows (m-PDPTW), as described by [8].

TurboRouter [9] is a decision support system (DSS) developed by MARINTEK in Trondheim for solving this type of ship routing and scheduling problems by using local search-based heuristics [2]. However, the model solved by this DSS represents only a simplification of the real-world problem. When implementing and testing the DSS at shipping companies, we have often experienced that there exist constraints that are fuzzy and hard to model. There are sometimes also secondary objectives, which can be unclear, hard to model or to give proper weight to, in addition to the primary one (that usually is measured in monetary terms). The inherent stochastic nature of ocean shipping (for instance sailing times that are influenced by weather conditions) also contributes to make the real-life problem hard to model and to solve. During the work with TurboRouter and from discussing with planners in shipping companies, we realized that it was hardly possible to model all these complicating aspects in a good manner, neither was it desirable. This was something the planners wanted to evaluate themselves, based on their experience. However, a good contribution for the planners would be a DSS that could present a set of diverse high quality solutions to analyze and choose from instead of only one optimal (or near-optimal) solution.

In ship routing and scheduling, planning follows a rolling horizon principle, where plans are updated when new information (new cargoes, ship delays, etc.) appears. Figure 1 illustrates a typical workflow for the planning process.

When the planners perform a complete rescheduling using TurboRouter, the solution after rescheduling is often very different from the solution prior to the changes. However, the planners have often already made commitments to some of the customers, for instance regarding time for start of servicing, and they may have nominated specific ships for loading given cargoes. The planners are therefore interested in new solutions that are in some sense close to the current solution, the baseline solution, for cargoes where commitments have been made, usually in the near future. (See the following sections for the explanations of our measures).

![](images/page_96_image_2.jpg)

Fig. 1. Scheduling workflow at a typical tramp shipping company

The aim of this paper is to develop and present a method that can find and identify such a set of high quality solutions to ship routing and scheduling problems. It is desirable that these solutions are close to the baseline solution in the near future but diverse from each other in the more distant time. In our heuristic search method, we include a persistence penalty function in the objective function for finding solutions close to the baseline solution. For finding a diverse set of high quality solutions we use a structural distance measure.

There exist several references on previous work on similar ship routing and scheduling problems that we study in this paper, see for instance [2, 1] and [11]. A thorough review of ship routing and scheduling problems in general is given by [7]. However, there has been little focus on producing a diverse set of high quality solutions to these problems instead of only the optimal (or near-optimal) solution. Brown et al.[5] consider optimization and persistence in general. They emphasize that new solutions that retain the features of the baseline solution are more acceptable to decision makers than solutions that require more changes. They incorporate this kind of persistence in modelling linear, mixed-integer and integer linear programs. Brown et al. [3] deal with optimizing submarine berthing with a persistence incentive. When the current berthing plan is revised they introduce a penalty in the objective function for moving submarines. In a sample problem the persistence penalty reduced the number of revisions by 75%. Brown et al. [4] describe a problem of scheduling coast guard district cutters. An optimization model is described for solving the problem. In order to avoid major unnecessary changes when revising an accepted schedule they replace the original objective with a surrogate objective that preserves persistence. The cost of the new schedule is constrained to not cost more than the prior schedule.

Within land-based routing, [12] consider various similarity functions for the vehicle routing problem based on structural difference between solutions. The similarity functions or distance measures are used to choose a diverse set of high quality solutions to present to the planner using a decision support system. Their distance measure relies heavily on depot concept, and is thus not directly applicable for ship routing. Sörensen [14] discusses distance measures based on string comparison. The problems are characterized by the fact that the order in which the items appear in the solution is important. The problems discussed include the single-machine and multiple-machine scheduling problems, the traveling salesman problem, vehicle routing problems, and many others. Sörensen [13] considers route stability in vehicle routing decisions. A distance measure is used to create a metaheuristic approach that will find solutions”close” (in the solution space) to a given baseline solution and at the same time have a high quality in the sense that the total distance traveled is small.

The remainder of the paper is organized as follows: Sect. 2 gives a mathematical formulation of the ship routing and scheduling problem. Section 3 deals with the persistence objective to achieve new solutions close to a given baseline solution, while Sect. 4 describes a distance measure used to evaluate the difference between two solutions. A multi-start heuristic is proposed in Sect. 5 to solve the ship routing and scheduling problem with persistence and distance objectives. A computational study is presented in Sect. 6. Finally, Sect. 7 provides a summary and some concluding remarks.

## 2 Mathematical Formulation

This section describes a mathematical formulation of the ship routing and scheduling problem based on a model presented by [6] for a similar problem. Let N be the set of cargoes indexed by i. Associated with the loading port of cargo i there is a node $i ,$ and with the corresponding unloading port a node $N + i ,$ where N is the number of cargoes (both contract and optional spot cargoes) that may be serviced during the planning horizon. Let $\mathcal { N } _ { P }   =   \{ 1 , . . . , N \}$ be the set of loading (or pickup) nodes and $\mathcal { N } _ { D } = \{ N + 1 , . . . , 2 N \}$ be the set of unloading (or delivery) nodes. The set of loading nodes $N _ { P }$ is divided into two subset, $\mathcal { N } _ { P } = \mathcal { N } _ { C } \cup \mathcal { N } _ { O }$ , where $\mathcal { N } _ { C }$ is the set of loading nodes associated with the contract cargoes the shipping company is committed to transport, while $N _ { O }$ represents the loading nodes for the optional spot cargoes. Let $\mathcal { V }$ be the set of ships in the fleet indexed by v. Then, $( \mathcal { N } _ { \nu } , \mathcal { R } _ { \nu } )$ is the network associated with a specific ship v. Not all ships can visit all ports and take all cargoes. Denote by $\mathcal { F } _ { \nu }$ the set of feasible nodes for ship v. Then, $\mathcal { N } _ { \nu }   =   \mathcal { F } _ { \nu } \cup \{ o \left( \nu \right) , d \left( \nu \right) \}$ is the set of nodes that can be visited by ship v, where $\rho \left( \nu \right)$ and $d ( \nu )$ represent the origin and destination node for ship v. The origin node $\rho \left( \nu \right)$ can either be a port or a point at sea, while the destination node $d \left( \nu \right)$ is the last planned unloading node for ship v. Here $\mathcal { R } _ { \nu }$ contains the set of all feasible arcs that can be sailed by ship v. Further let $\mathcal { N } _ { P \nu } = \mathcal { N } _ { P } \cap \mathcal { N } _ { \nu }$ and $\mathcal { N } _ { D \nu } = \mathcal { N } _ { D } \cap \mathcal { N } _ { \nu }$ be the sets of loading and unloading node that can be visited by ship v, respectively. There is a revenue $R _ { i }$ for transporting cargo i. The quantity of cargo i is given by $Q _ { i }$ , while the capacity of ship v is given by $V _ { C A P _ { v } }$ For each arc, $T _ { S i j v }$ represents the calculated sailing time from node i to node j with ship v including service time at node i. Let $[ T _ { \mathit { M N i } } , T _ { \mathit { M X i } } ]$ denote the time window associated to node i. The cost $C _ { i j v }$ represents the sailing cost between node i and j for ship v including port cost at node i.

We use the following types of variables: the binary flow variable $x _ { i j \nu } , \nu _ { \mathrm { ~   ~ } } \in$ $\mathcal { V } , ( i , j ) \in \mathcal { H } _ { v }$ equals 1, if ship v sails from node i directly to node $j ,$ and 0 otherwise. The time variable $t _ { i \nu } , \nu \in \mathcal { V } , i \in \mathcal { N } _ { \nu }$ represents the time at which ship v begins service at node i, while variable $l _ { i \nu } , \nu \in \mathcal { V } , i \in \mathcal { N } _ { \nu } \backslash d ( \nu )$ gives the total load onboard ship v just after the service is completed at node i.

Then, the formulation of the ship routing and scheduling problem can be given as follows:

$$
\max \sum_ {v \in \mathcal {V}} \sum_ {(i, j) \in \mathcal {A} _ {v} | i \in \mathcal {N} _ {P _ {v}}} R _ {i} x _ {i j v} - \sum_ {v \in \mathcal {V}} \sum_ {(i, j) \in \mathcal {A} _ {v}} C _ {i j v} x _ {i j v},\tag{1}
$$

subject to

$$
\sum_ {v \in \mathcal {V}} \sum_ {j \in \mathcal {N} _ {v}} x _ {i j v} = 1,
$$

$$
\forall i \in \mathcal {N} _ {C},\tag{2}
$$

$$
\sum_ {v \in \mathcal {V}} \sum_ {j \in \mathcal {N} _ {v}} x _ {i j v} \leq 1,
$$

$$
\forall i \in \mathcal {N} _ {O},\tag{3}
$$

$$
\sum_ {j \in \mathcal {N} _ {P _ {v}} \cup \{d (v) \}} x _ {o (v) j v} = 1,
$$

$$
\forall v \in \mathcal {V},\tag{4}
$$

$$
\sum_ {i \in \mathcal {N} _ {v}} x _ {i j v} - \sum_ {i \in \mathcal {N} _ {v}} x _ {j i v} = 0, \quad \forall v \in \mathcal {V}, j \in \mathcal {N} _ {v} \backslash \{o (v), d (v) \},\tag{5}
$$

$$
\sum_ {i \in \mathcal {N} _ {D v} \cup \{o (v) \}} x _ {i d (v) v} = 1,
$$

$$
\forall v \in \mathcal {V},\tag{6}
$$

$$
x _ {i j v} \left(t _ {i v} + T _ {S i j v} - t _ {j v}\right) \leq 1, \quad \forall v \in V, (i, j) \in \mathcal {A} _ {v},\tag{7}
$$

$$
T _ {M N i} \leq t _ {i v} \leq T _ {M X i},
$$

$$
\forall i \in \mathcal {N} _ {v},\tag{8}
$$

$$
x _ {i j v} \left(l _ {i v} + Q _ {j} - l _ {j v}\right) = 0, \quad \forall v \in \mathcal {V}, (i, j) \in \mathcal {A} _ {v} | j \in \mathcal {N} _ {P v},\tag{9}
$$

$$
x _ {i, N + j, v} \left(l _ {i v} - Q _ {j} - l _ {N + j, v}\right) = 0, \quad \forall v \in \mathcal {V}, (i, N + j) \in \mathcal {A} _ {v} | j \in \mathcal {N} _ {P v},\tag{10}
$$

$$
l _ {o (v)} = 0,
$$

$$
\forall v \in \mathcal {V},\tag{11}
$$

$$
\sum_ {j \in \mathcal {N} _ {v}} Q _ {i} x _ {i j v} \leq l _ {i v} \leq \sum_ {j \in \mathcal {N} _ {v}} V _ {C A P v} x _ {i j v},
$$

$$
\forall v \in \mathcal {V}, i \in \mathcal {N} _ {P _ {V}},\tag{12}
$$

$$
0 \leq l _ {N + i, v} \leq \sum_ {j \in \mathcal {N} _ {v}} (V _ {C A P v} - Q _ {i}) x _ {N + i, j v}, \quad \forall v \in \mathcal {V}, i \in \mathcal {N} _ {P v},\tag{13}
$$

$$
\sum_ {j \in \mathcal {N} _ {v}} x _ {i j v} - \sum_ {j \in \mathcal {N} _ {v}} x _ {j, N + i, v} = 0,
$$

$$
\forall v \in \mathcal {V}, i \in \mathcal {N} _ {P _ {V}},\tag{14}
$$

$$
t _ {i v} + T _ {S I, N + i, v} - t _ {N + i, v} \leq 0,
$$

$$
\forall v \in \mathcal {V}, i \in \mathcal {N} _ {P _ {V}},\tag{15}
$$

$$
x _ {i j v} \in \{0, 1 \},
$$

$$
\forall v \in \mathcal {V}, (i, j) \in \mathcal {A} _ {v}.\tag{16}
$$

The objective function (1) maximizes the profit of operating the fleet. Constraints (2) ensure that all mandatory contract cargoes are transported exactly once, while (3) guarantee that all optional spot cargoes are transported at most once. Constraints (4)-(6) describe the flow on the sailing route used by ship v. Constraints (7) describe the compatibility between routes and schedules. If ship v sails from node i to node j the constraints ensure that the start time of service at node j is greater or equal to the start time of service at node i plus the sailing time from node i to j including service time at node i. The time window constraints are given by (8). If ship v is not visiting node i, we will get an artificial starting time within the time windows for that (i, v)-combination. Constraints (9) and (10) give the relationship between the binary flow variables and the ship load at each loading and unloading port, respectively. The initial load condition for each ship is given by (11), while (12) and (13) represent the ship capacity constraints at loading and unloading nodes, respectively. The coupling constraints (14) and the precedence constraints (15) ensure that both the pickup and delivery node for cargo i belongs to the same route and that the delivery node is visited later than the pickup node. Finally, the formulation includes binary requirements (16) on the flow variables.

## 3 Persistence Penalty Function

As described in Sect. 1, ship routing and scheduling follows a rolling horizon principle, where rescheduling is performed when new information appears. However small modification of the input can often amplify into major changes to the current plan (baseline solution). In the baseline solution, especially in the near future, commitments have often been made regarding time for start of servicing and specific ships may have been nominated for transporting given cargoes. Even if it is possible to make changes for cargoes where commitments are made, it is usually not desirable unless there are compelling reasons to do so. For instance, when decisions are made regarding which ship that are planned to service a given cargo, additional equipment or services needed for the port operation, like pilot, tugs and port services may be arranged in advance. The fleet of ships is heterogeneous and if a cargo is rescheduled and assigned to another ship, or is to be serviced at another time, other equipment or services may be required. Then the old arrangements must be cancelled and new ones made. Even if it is possible to make changes it may require a lot of work to do so. When a customer is given a specific time for when he will be served he might be unwilling to accept another time (even if it is within the original time window). The customer might have made his own commitments to other participants in the supply chain, or the customer’s storage facilities or production might be dependent on the specified pickup/delivery time.

To achieve solutions that are close to the baseline solution for cargoes where commitments have been made, we introduce a persistence penalty function to penalize solutions deviating from the baseline solution for these cargoes. To describe the persistence penalty function we use the following notation. We denote the baseline solution as B. The new solution after rescheduling is denoted by A. We let the parameter $U _ { i } ^ { A B }$ be equal to one if cargo i is served by different ships in solutions A and B, and zero otherwise. $T _ { i } ^ { A }$ and $\bar { T } _ { i } ^ { \vec { B } }$ represent the time when service starts at node i in solutions A and B, respectively. The cargo-ship penalty, $P _ { 1 i }$ , is the penalty for servicing cargo i by a different ship in the new solution compared with the baseline solution. Finally the cargo-time penalty, $P _ { 2 i }$ , is the penalty per time unit difference in service start at node i. For cargoes where no commitments have been made, both persistence penalties, $P _ { 1 i }$ and $P _ { 2 i }$ , are equal to zero.

The persistence penalty function for solution A can now be given as follows:

$$
P (A) = \sum_ {i \in \mathcal {N} _ {P}} P _ {1 i} U _ {i} ^ {A B} + \sum_ {i \in \mathcal {N} _ {P} \cup \mathcal {N} _ {D}} P _ {2 i} \left| T _ {i} ^ {A} - T _ {i} ^ {B} \right|\tag{17}
$$

This persistence penalty function (17) is included in the objective function when solving the ship routing and scheduling problem.

## 4 Distance Measure

In the ship routing and scheduling problem, the most important difference between two solutions is which ships that service the different cargoes. In our distance measure we therefore calculate the number of cargoes that have changed ship between two solutions. This can be seen as the Hamming distance between the solutions, see [10]. The parameter $U _ { i } ^ { A B }$ is again equal to one if cargo i is serviced by different ships in solutions A and B, and zero otherwise. The normalized Hamming distance (a value between 0 and 1) between solutions A and B is given as follows:

$$
D _ {A B} = \frac {1}{N} \sum_ {i \in \mathcal {N} _ {P}} U _ {i} ^ {A B}\tag{18}
$$

The Hamming distance is normalized to make it independent of case. All distance measures can (and should) be normalized to the 0–1 range, see [12]. It can be noted that the penalty function (17) is similar to the normalized Hamming distance (18) if all penalties $P _ { 1 i }$ are equal to $\frac { 1 } { N }$ and all $P _ { 2 i }$ are zero. However, as mentioned in the previous section, this will not be the case for practical problem solving.

For a general vehicle routing problem (VRP), the Hamming distance is known to be a weak distance measure. In the classical VRP the fleet of vehicles is homogenous and the vehicles start at a given depot. Because of this it makes no difference which vehicle that services a given customer. The focus on distances measure for vehicle routing problems has therefore been to produce routes that are structurally different regarding which customers, and the sequence of the customers, that are serviced together on the same route, see for instance [12, 14]. In ship routing and scheduling problems, we usually have a heterogeneous fleet of ships, and due to the reasons described above the number of different cargo-ship combinations between two solutions is more important for the planner than structurally different routes regarding the sequence of the customers (nodes).

## 5 Solution Method

The solution method is based on the ideas from [2], where a multi-start local search heuristic for the ship routing and scheduling problem is presented. In the multi-start heuristic a number of start solutions are generated by using a constructive heuristic. A part of each solution is randomly generated and the rest is generated by using a deterministic constructive insertion heuristic. The local search operators used are both intra-route and inter-route operators. Intra-route operators try to improve the route of one single ship, while inter-route operators looks for improvement by moving cargoes between ships. The local search heuristic we use consists of three operators:

1-resequence: cargo i (both the loading and unloading node) is removed from the route of ship v. The cargo is then reinserted in the best position in the route of the same ship.

Reassign: removes a cargo from the route of a ship v and tries to find the best feasible insertion of the cargo into the route of another ship u. If there is one or more rejected cargoes in the cargo list, i.e. cargoes for which the heuristic has not found any feasible insertion so far, the heuristic tries to find a place for one of them in the route of ship v.

2-interchange: two cargoes i and j are removed from the routes of ships v and u, respectively, and are then inserted in the best feasible position in the routes of ships u and v, respectively.

The persistence penalty function (17) described in Sect. 3 is included in the objective function when evaluating given moves. This will ensure solutions that are close to the baseline solution in near future. The distance measure (18) described in Sect. 4 is included in the multi-start heuristic to find a diverse set of start solutions and in order to choose the final solutions to present to the planner. In the algorithm described below we let l represent the number of start solutions generated, m the number of start solutions to be improved by local-search and n the number of final solutions to present to the planner. We let $T _ { 1 }$ and $T _ { 2 }$ represent threshold distance values (between 0 and 1). A pseudo-code of the multi-start heuristic is formulated in Fig. 2. The sub-routine SELECT-SOLUTIONS is called in step 3 and 6 of the MULTI-START algorithm to ensure a diverse set of start solutions and final solutions respectively. In the sub-routine we start by selecting the solution with best objective value in the sorted list of solutions Y to choose from. This solution is included in the list of selected solutions, X. We then go through the rest of the solutions in list Y. Before including a solution from list Y in list X, we calculate the distances to all other solutions selected so far using distance measure (18). If all distances are greater or equal to the threshold distance value, t (equal to $T _ { 1 }$ and $T _ { 2 }$ , respectively), the solution is selected.

## 6 Computational Study

A computational study has been performed on four test cases based on real data from two different bulk shipping companies operating in the tramp shipping segment. Section 6.1 describes the test cases. In Sect. 6.2 we perform analyses to decide proper values on the penalties in the persistence penalty function (17) described in

![](images/page_102_image_2.jpg)

Fig. 2. Pseudo-code for the multi-start heuristic

Sect. 3. Section 6.3 presents analyses to decide proper values on the threshold distance values which are included in the multi-start heuristic to get a diverse set of solutions. Section 6.4 presents computational results where different solutions to the test cases are compared regarding solution quality (profit) and distance (closeness) to the baseline solution.

## 6.1 Description of Test Cases

Cases 1 and 2 are collected from a shipping company transporting dry bulk commodities such as rock, iron ore and cement. A chemical commodity shipping company is the basis for cases 3 and 4. The test cases are summarized in Table 1. The number of cargoes includes both the cargoes in the baseline solution and the new optional spot cargoes. The number of spot cargoes is displayed in a separate row.

## 6.2 Setting Persistence Penalties

The cargo-ship penalty $P _ { 1 i }$ and the cargo-time penalties $P _ { 2 i }$ and $P _ { 2 ( N + i ) }$ in the persistence penalty function (17) given in Sect. 3 have to be decided for each cargo. In Sect. 3 we described that it is desirable when rescheduling that new solutions are close to the baseline solution for some cargoes where certain commitments are made. These cargoes are usually the cargoes that are planned to be serviced in near future of the baseline solution and we will refer to these cargoes as persistence important cargoes. In the computational study we regard the cargoes that have the ending of the loading time window within the first third of the planning period as persistence important cargoes. This can of course be chosen to another value by the decision maker and the importance of each cargo can also be decided individually. To illustrate that it is often more difficult to make changes early than late in the baseline solution, we use penalties that are linearly decreasing with time, as shown in Fig. 3.

Table 1. Test cases

| Case | 1 | 2 | 3 | 4 |
| --- | --- | --- | --- | --- |
| Planning horizon [days] | 30 | 30 | 90 | 150 |
| # cargoes | 24 | 31 | 17 | 40 |
| # optional spot cargoes | 4 | 4 | 4 | 6 |
| # ships | 7 | 13 | 5 | 6 |

![](images/page_103_chart_5.jpg)

Fig. 3. Persistence penalty as a function of time

To decide the proper values of the penalties we use sensitivity analyses. Case 2 is here used as an example illustration. The multi-start heuristic used includes a random element in the generation of start solutions. Therefore, in order to make sensible comparisons we perform ten runs of the algorithm and report average values. Figure 4 shows that the average profit gap from the best solution (regarding profit only) increases with the maximum cargo-ship penalty cost $P _ { 1 M A X }$ . The figure also shows the average number of persistence important cargoes that have changed ship after rescheduling for different values on $P _ { 1 M A X }$ . From the figure we see that with

$P _ { 1 M A X }$ equal to zero, the average profit gap from best solution is 0% while the average number of cargo-ship changes is 5.1. Increasing the maximum penalty cost will increase the average profit gap while reducing the number of cargo-ship changes. With a maximum penalty cost equal to 0.25% of the baseline objective value the solutions found after rescheduling have on average zero cargo-ship changes and an average profit gap from best solution equal to 0.5%.

![](images/page_104_chart_3.jpg)

Fig. 4. Sensitivity analysis for the cargo-ship penalty for case 2

Similar analysis as for the maximum cargo-ship penalty cost $P _ { 1 M A X }$ is performed for the maximum cargo-time penalty cost and the results are shown in Fig. 5. From the figure we see with $P _ { 2 M A X }$ equal to zero, the average profit gap from best solution is 0% while the total cargo-time difference for the persistence important cargoes is on average 7.9 days between a new solution and the baseline solution. Increasing the maximum cargo-time penalty cost will increase the average profit gap but reduce the total cargo-time difference.

From this we choose the values of the maximum cargo-ship penalty $P _ { 1 M A X }$ and the maximum cargo-time penalty $P _ { 2 M A X }$ . For case 2, it seems reasonable to set $P _ { 1 M A X }$ in the range $0 . 1 5   -   0 . 2 5 \%$ of baseline objective value and $P _ { 2 M A X }$ in the range $0.004 - 0.016\%$ of baseline objective value. With these settings, the multi-start heuristic produces high-quality solutions that are close to the baseline solution (for the cargoes in near future). In the rest of the computational study we use for case 2; $P_{1MAX}=0.25\%$ of baseline objective value and $P_{2MAX}=0.016\%$ of baseline objective value.

![](images/page_105_chart_2.jpg)

Fig. 5. Sensitivity analysis for the cargo-time penalty for case 2

Similar analyses are also performed for the other test cases and corresponding values on the penalties are chosen. The penalties are case specific and must be adapted to the different shipping companies and the problem at hand.

## 6.3 Setting Threshold Distance Values

In the multi-start heuristic described in Sect. 5 we use two acceptation threshold distance values; $T _ { 1 }$ and $T _ { 2 }$ . Threshold distance value $T _ { 1 }$ is used to ensure a diverse set of start solutions while threshold distance value $T _ { 2 }$ is used to ensure a diverse set of final solutions. Figure 6 shows the number of different start solutions for different values on the threshold distance value $T _ { 1 }$ . Case 2 is again used as an example illustration. From the figure we see that if we generate 500 start solutions and use $T _ { 1 } = 0 . 4$ approximately 170 of the start solutions will be considered as sufficiently different to each other.

![](images/page_106_chart_4.jpg)

Fig. 6. Number of different start solutions for case 2

Figure 6 is produced without persistence penalties in the objective function. Including the persistence penalties presented in Sect. 6.2 in the objective function has only a small impact on the number of sufficiently different start solutions. For example if we generate 500 start solutions and use $T _ { 1 } = 0 . 4$ the number of different start solutions are reduced from 172 to 162 when including persistence penalties.

Figure 7 shows, both with and without persistence penalties in the objective function, the number of final solutions that are considered to be sufficiently different from each other for various values of the threshold distance value $T _ { 2 }$ . Case 2 is again used as an example illustration. We have generated 500 start solutions and use a threshold distance value $T _ { 1 }   =   0 . 4$ . When the threshold distance value $T _ { 2 }   =   0$ , the number of different final solutions after the multi-start local search is performed is equal to the number of different start solutions (which is 172 (without persistence penalties) and 162 (with persistence penalties)). From figure we see that the number of final solutions considered to be sufficiently different from each other decreases with the threshold distance value. There will also be some fewer different final solutions when including persistence penalties in the objective function. The persistence penalties will direct the local search towards the baseline solution for the persistence important cargoes and more of the final solutions will be similar compared with the solutions we find without persistence penalties in the objective function. Because we seek solutions that are close to the baseline solution for the persistence important cargoes we choose a lower acceptation threshold distance value $T _ { 2 }$ for solutions that are close to the baseline solution than for solutions that are far from the baseline solution. For case 2, we use acceptation threshold distance value $T _ { 2 }   =   0 . 3$ when we generate solutions without persistence penalties in the objective function, while we use $T _ { 2 }   =   0 . 2$ when we seek solutions close to the baseline solution. Then, we get 59 and 71 sufficiently different final solutions to choose from, respectively.

![](images/page_107_chart_3.jpg)

Fig. 7. Number of different final solutions for case 2

Similar analyses are done for the other test cases and corresponding values on the acceptation threshold distances are chosen.

## 6.4 Computational Results

We have tested the multi-start heuristic on the test cases described in Sect. 6.1 and the results are summarized in Tables 2 and 3. Table 2 shows the three best solutions to test case 2 when we optimize with respect to profit only, case 2a, and with respect to profit and persistence penalty cost, case 2b. In the table, we report the average number of persistence important cargoes that have changed ship, the average total cargo-time difference for the persistence important cargoes, the average penalty cost and the average profit gap from the best solution (with respect to profit only). The last rows in the table include the distance matrix which reports the average distance between the solutions. From Table 2 we see that including persistence penalties in the objective function has a great effect on finding high quality solutions that are close to the baseline solution. Comparing the best solution for test cases 2a and 2b, we see that the average-ship changes is reduced from 6.2 to 0, while the average total cargotime difference is reduced from 8.2 to 0 days when including persistence penalties. However, the average profit gap from the best solution is a little bit larger for case 2b. The profit gap for the best solution to test case 2a is 0% from the best solution while for test case 2b the profit gap is 0.5%. The average distances between the solutions are larger for case 2a than for case 2b. The reason for this is that we accept a smaller acceptation threshold distance for solutions that are close to the baseline solution, see Sect. 6.3.

Table 2. Computational results for case 2

<table><tr><td></td><td colspan="3">Case 2a (profit objective)</td><td colspan="3">Case 2b (profit incl. persistence penalty)</td></tr><tr><td>Solution</td><td>1</td><td>2</td><td>3</td><td>1</td><td>2</td><td>3</td></tr><tr><td>Avg. cargo-ship changes (#)</td><td>6.2</td><td>5.0</td><td>6.7</td><td>0</td><td>1.0</td><td>1.1</td></tr><tr><td>Avg. total caro-time difference (days)</td><td>8.2</td><td>7.1</td><td>9.1</td><td>0</td><td>1.7</td><td>0.7</td></tr><tr><td>Avg. penalty cost (% of baseline profit)</td><td>1.7</td><td>1.4</td><td>1.8</td><td>0</td><td>0.3</td><td>0.2</td></tr><tr><td>Avg. profit gap from best solution (%)</td><td>0</td><td>0.1</td><td>0.3</td><td>0.5</td><td>0.4</td><td>0.8</td></tr><tr><td>Distance matrix</td><td>1</td><td>2</td><td>3</td><td>1</td><td>2</td><td>3</td></tr><tr><td>1</td><td>-</td><td>0.38</td><td>0.44</td><td>-</td><td>0.26</td><td>0.23</td></tr><tr><td>2</td><td></td><td>-</td><td>0.36</td><td></td><td>-</td><td>0.35</td></tr><tr><td>3</td><td></td><td></td><td>-</td><td></td><td></td><td>-</td></tr></table>

Table 3 shows the best solution regarding profit and the best solution regarding profit and penalty cost for each of the four test cases. As in Table 2, we report the average number of persistence important cargoes that have changed ship, the average total cargo-time difference for the persistence important cargoes, the average penalty cost and the average profit gap from the best solution (with respect to profit only). The average value for cases 1-4 a) and for cases 1-4 b) is shown in the two last columns. Remark that for case 4, the average total cargo-time difference is reduced from 86.5 days to 0.3 days when including persistence penalties. The reason for the large decrease is that the time windows are quite wide for this test case, specially the unloading time windows. From the table we see that the profit gap increases, on average from 0.18% to 0.68%, when including the penalty costs in the objective function. In return the persistence penalties direct the multi-start heuristic towards solutions that are very close to the baseline solution with respect to the persistence important cargoes.

Table 3. Computational results for cases 1-4

| Case | 1a | 1b | 2a | 2b | 3a | 3b | 4a | 4b | avg. a) | avg. b) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Avg. cargo-ship changes (#) | 5.9 | 0.7 | 6.3 | 0 | 3.7 | 1.6 | 12.7 | 1.1 | 7.13 | 0.85 |
| Avg. total cargo-time difference (days) | 12.6 | 2.4 | 8.2 | 0 | 5.4 | 1.4 | 86.5 | 0.3 | 28.18 | 1.03 |
| Avg. penalty cost (% of baseline profit) | 7.2 | 1.1 | 1.7 | 0 | 1.3 | 0.4 | 6.1 | 0.3 | 4.08 | 0.45 |
| Avg. profit gap from best solution (%) | 0.3 | 0.7 | 0 | 0.5 | 0.1 | 0.6 | 0.3 | 0.9 | 0.18 | 0.68 |

Figure 8 shows a new user interface from the DSS TurboRouter [9] for a reduced test case. In the figure, each ship is represented by a colour. The baseline solution is denoted B, while the three new solutions after rescheduling are denoted, S.1, S.2 and S.3. The Gannt diagram shows which ship each cargo is assigned to and the day when service starts (for both loading and unloading), for each of the four solutions. Cargoes 8 and 11 are new spot cargoes and are not serviced in the baseline solution. It is desirable that new solutions are close to the baseline solution for the part to the left of the vertical line in the figure. The new solution, S.2, is the solution closest to the baseline solution. However it should be noted that the solution includes one spot cargo less than solutions S.1 and S.3. The possibility to evaluate a set of solutions, instead of only the optimal (or near-optimal) solution, will in such cases provide valuable decision support flexibility for the planners.

![](images/page_110_image_2.jpg)

Fig. 8. Gannt diagram from TurboRouter showing information about the solutions

## 7 Summary and Concluding Remarks

In this paper we focus on decision support for a short-term routing and scheduling problem faced by many tramp shipping companies. TurboRouter is a decision support system (DSS) developed for solving such problems by using local searchbased heuristics, see [2]. However, the model solved by a DSS is only an approximation to the underlying real-life problem. After evaluating the use of TurboRouter in different shipping companies, we realized the need for a DSS that can present a set of good diverse solutions to choose from instead of only one optimal (or near-optimal) solution.

In ship routing and scheduling, planning follows a rolling horizon principle, where plans are updated when new information appears. When planners perform a complete rescheduling using TurboRouter, the solution after rescheduling is often very different from the solution prior to the changes. However, the planners have often already made commitments to some of the customers, for instance regarding time for start of servicing, and they may have nominated specific ships for loading given cargoes. The planners are therefore interested in new solutions close to the previous solution for cargoes where commitments are made, usually in the near future.

This paper presents a method that presents a set of good solutions to ship routing and scheduling problems. It is desirable that these solutions are close to the baseline solution in the near future but diverse from each other in more distant time. The heuristic methods include a persistence penalty function in the objective function, for achieving solutions close to the baseline solution, and a distance measure for finding a diverse set of solutions.

The computational study shows that introducing small persistence penalties in the objective function directs the search towards solutions very close to the baseline solution. The quality (profit) of the solutions is just slightly worse than the solutions found when we optimize with respect to profit only, but the number of cargo-ship changes and the cargo-time difference are considerable reduced. The distance measure is used to find a diverse set of solutions the planner can choose from. A version of the algorithm presented will be implemented in TurboRouter [9]. Introducing persistence and distance objectives when solving ship routing and scheduling problems seem to provide valuable decision support flexibility for planners in shipping companies.

## 8 Acknowledgment

This research was carried out with financial support from the INSUMAR and OPTI-MAR projects, funded by the Research Council of Norway. We are also grateful to the shipping companies that provided real data for the test cases used in the computational study.

## References

[1] D.O. Bausch, G.G. Brown, and D. Ronen. Scheduling short-term marine transport of bulk products. Maritime Policy and Management, 25(4):335–348, 1998.

[2] G. Brønmo, M. Christiansen, K. Fagerholt, and B. Nygreen. A multi-start local search heuristic for ship scheduling - a computational study. Computers & Operations Research, 34(3):884–899, 2007.

[3] G.G. Brown, K.J. Cormican, S. Lawphongpanich, and D.B. Widdis. Optimizing submarine berthing with a persistence incentive. Naval Research Logistics, 44:301–318, 1997.

[4] G.G. Brown, R.F. Dell, and R.A. Farmer. Scheduling coast guard district cutters. Interfaces, 26(2):59–72, 1996.

[5] G.G. Brown, R.F. Dell, and R.K. Wood. Optimization and persistence. Interfaces, 27(5):15–37, 1997.

[6] M. Christiansen, K. Fagerholt, B. Nygreen, and D. Ronen. Maritime transportation. In C. Barnhart and G. Laporte, editors, Transportation, volume 14 of Handbooks in Operations Research and Management Science, pages 189–284. Elsevier Science, 2007.

[7] M. Christiansen, K. Fagerholt, and D. Ronen. Ship routing and scheduling: Status and perspectives. Transportation Science, 38(1):1–18, 2004.

[8] J. Desrosiers, Y. Dumas, M.M. Solomon, and F. Soumis. Time constrained routing and scheduling. In M.O. Ball, T.L. Magnanti, C.L. Monma, and G.L. Nemhauser, editors, Network Routing, volume 8 of Handbooks in Operations Research and Management Science, pages 35–139. Elsevier Science, 1995.

[9] K. Fagerholt. A computer-based decision support system for vessel fleet scheduling - experience and future research. Decision Support Systems, 37(1):35–47, 2004.

[10] R.W. Hamming. Error-detecting and error-correcting codes. Bell System Technical Journal, 29(2):147–160, 1950.

[11] S.-H. Kim and K.-K. Lee. An optimisation-based decision support system for ship scheduling. Computers & Industrial Engineering, 33(3-4):689–692, 1997.

[12] A. Løkketangen and D.L. Woodruff. Similarity functions for VRP decision support. Working paper submitted, 2007.

[13] K. Sörensen. Route stability in vehicle routing decisions: a bi-objective approach using metaheuristics. Central European Journal of Operations Research, 14(2):193–207, 2006.

[14] K. Sörensen. Distance measures based on the edit distance for permutation-type representations. Journal of Heuristics, 13(1):35–47, 2007.

[15] UNCTAD. Review of maritime transport, 2006. United Nations, New York and Geneva, 2006.

# Logistics in Real-Time: Inventory-Routing Operations Under Stochastic Demand

Ricardo Giesen<sup>1</sup>, Hani S. Mahmassani<sup>2</sup>, and Patrick Jaillet<sup>3</sup>

1 Department of Transport Engineering and Logistics, Pontificia Universidad Católica de Chile, Chile Giesen@ing.puc.cl

2 Transportation Center, Northwestern University, USA Masmah@northwestern.edu

3 Department of Civil & Environmental Engineering, Massachusetts Institute of Technology, USA Jaillet@MIT.edu

**Summary.** This chapter studies real-time distribution strategies and their associated benefits for a two-level distribution system, from one depot to N retailers, wherein vehicle delivery routes can be updated using real-time information about current inventory levels and vehicle status. Three rolling horizon approaches are proposed in which plans are updated using a mathematical programming formulation. The proposed re-planning strategies are compared against two benchmark policies using a general discrete-event simulation framework. Proposed replanning strategies are shown to systematically outperform the two benchmark policies.

**Key words:** Logistics, Inventory Routing problem, Vendor managed inventory, Online vehicle routing problem, Dynamic fleet management, Intelligent transportation systems (ITS), Commercial vehicle operations (CVO), Real-time information, On-line problems, Freight transportation

## 1 Introduction

The focus of this Chapter is on formulating Inventory-Routing Problems (IRPs) in a stochastic dynamic environment with real-time information about current inventory levels, as well as delivery vehicle locations and status. The main objectives are to: (a) formulate and analyze the Online Inventory Routing Problem (OIRP), explicitly taking into account real-time information about fleet status and inventory levels at different facilities; (b) develop operational-control strategies to operate a distribution system in which transportation and inventory control are coordinated, tailored to different degrees of real-time information; and (c) evaluate the performance of the proposed real-time strategies and the value of using real-time information in a centrally operated or collaborative distribution system, along with conditions that affect this performance.

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">L. Bertazzi et al. (eds.), Innovations in Distribution Logistics, Lecture Notes</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">in Economics and Mathematical Systems 619, DOI: 10.1007/978-3-540-92944-4,</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">-c 2009 Springer-Verlag Berlin Heidelberg</span></small>

This research is motivated by three main considerations: (a) the recognized importance of logistics and distribution systems in the national and local economy (see for example, La Londe, 1994; Ghiani et al., 2004) (b) the current trend to coordinate logistic operations, discussed among others by (Thomas and Griffin, 1996, Campbell et al., 1998, Bertazzi et al., 2007), and (c) the opportunities offered by Information and Communication Technologies (ICT) to operate and control a system in real-time, which allow sharing information between different stages in a supply chain at progressively reduced costs (Rabah and Mahmassani, 2002).

Relevant ICT developments can be divided into three groups: communication and tracking devices that can automate information input to and transmission between computer systems (see, e.g., Blanchard, 2003; Datta, 2003; Masters and La Londe, 1994); Commercial Vehicle Operations (CVO) technologies that allow the control of a fleet of vehicles on a real-time basis (see Regan et al., 1995); and software and Decision-Support Systems (DSS) that provide data processing capabilities at a particular facility (Rutner et al., 2003; Fleischmann and Meyr, 2003; Simchi-Levi et al., 2003). These systems increase the speed and accuracy with which data is entered, gathered, and communicated, and provide real-time visibility into inventory levels throughout the distribution system and better control over a fleet of vehicles.

In summary, with access to real-time information on the current state of the system – i.e. inventory levels at each facility and status of the fleet – managers can react faster to changes in predicted demand patterns or traffic conditions, and make online decisions on a continuing basis to adjust and improve routing plans accordingly. However, the operational decisions are complex, since the underlying problems are combinatorial and unfold in real-time, precluding the evaluation of all possible alternatives by the decision maker. Moreover, the stochastic nature of such systems implies that information about the state of the system is gradually revealed and cannot be accurately predicted in advance. In order to take maximum advantage of real-time information made available by ICTs, supply-chain managers need to use information effectively. That requires the development of models and algorithms that can exploit the full potential of real-time information for distribution-logistic operations.

While previous published contributions on IRPs share some common elements, most of the problems addressed in the literature consider systems that have different characteristics. A detailed review is presented in Baita et al. (1998), Campbell et al. (1998), Campbell and Savelsbergh (2002), Kleywegt et al. (2002), Giesen (2007), and Bertazzi et al. (2007). The main difference between problems found in the literature, with the exception of Giesen et al. (2005), with the problem addressed in the present Chapter, is that vehicle plans are not modified after they leave the depot.

Finally, previous research on real-time fleet management has focused on how to serve load demands for transportation services that are exogenous to the system, in the context of dynamic vehicle-routing problems (Gendreau et al., 1999, Larsen et al., 2002, Larsen et al., 2004, Jehova et al., 2006), pick up and delivery problems with full truck loads (Regan et al., 1995, Regan et al., 1996, Yang et al., 2004, Kim et al., 2002, Kim et al., 2004), and pick up and delivery problems with multiple loads (Mitrovic-Minic et al., 2004, Gendreau et al., 2006).

In this research, routing decisions are coordinated with inventory control. In that fashion, it is expected that monitoring inventory levels would allow improving the forecast and coordination of transportation activities, giving the operator the option to visit a facility earlier than needed to take advantage of transportation savings. That could be particularly useful when demand is highly variable and/or unpredictable, which is normally the case when final consumers are separated by several echelons from the echelon considered, or as a consequence of the phenomenon known as the bullwhip effect (Lee et al., 1997, Fine, 1998, Chen et al., 2000).

The specific distribution system considered is a two-level supply chain, in which a set of geographically dispersed facilities facing stochastic demands have to be repeatedly replenished from a central warehouse (or depot) over a long period of time. The facilities to be replenished could represent final customers, retailers who serve demand from final customers, or distribution centers from which a set of additional facilities are replenished. In this system, products are transported from the depot to the set of retailers by a vehicle with limited capacity, the plans for which can be updated with real-time information about the state of the system, thanks to modern information and communication capabilities. This problem is designated as the Online Inventory Routing Problem (OIRP) under real-time information. The OIRP is formulated and solved considering inventory allocation and transportation decisions together. As such, the OIRP considers the trade-off among transportation, inventory holding, and stock-out costs.

Key features of this OIRP are the presence of uncertainty about future consumption rates at different facilities, and the possibility of updating plans based on accurate real-time information about the complete state of the system. This is in contrast with deterministic environments, in which decisions can be made with perfect hindsight, thus real-time operational capabilities would not modify the nature of the problem. The possibility of updating plans on a quasi-continuous basis, given information on demand realizations, makes possible some additional decisions to update truck-route plans, such as modifying the set and/or the sequence of subsequent customers to be visited; diverting a truck from its current destination to visit a different facility; and adjusting amounts to be delivered to subsequent customers in the route.

Such an operational environment could enable more efficient use of existing resources and increase system reliability. However, the design of effective strategies to operate the system can be extremely difficult. On one hand, the dispatcher faces a fleet-routing and scheduling problem – which is combinatorial – to obtain new operational plans. Since even simplified static and deterministic versions of the inventoryrouting problem are computationally hard (Bertazzi et al., 2007), a trade off between quality of solution and speed should be considered in the search for new plans. On the other hand, given that plans can be modified at any time, based on new information, the events and circumstances under which a plan update would be beneficial should be specified.

The rest of the chapter is organized as follows. In the next section, a detailed definition of the problem studied and general approach are presented. Section 3 discusses re-planning strategies for the OIRP under real-time information, presenting a detailed mechanism of how a central decision maker would operate under these policies, and presents a formulation for the routing problem used to update plans corresponding to the problem of interest under real-time information. Section 4 describes the simulation framework developed to evaluate the different strategies proposed, and presents experimental results and analysis from these simulations. Concluding remarks are presented in the final section.

## 2 Problem Definition

## 2.1 Main Assumptions

In this research – unlike the common view in real-time fleet management problems where load demands are exogenous to the system – decisions to replenish inventory, by how much, in what sequence, and by which vehicle, are conducted in an integrated real-time decision framework. In addition a central-planner approach to the problem is assumed. That is, the system is operated and controlled by a central decision maker, with real-time information about the complete state of the system, who seeks to move inventories in the system in such a way as to maximize total expected profit in the long-run for the entire system.

Also, it is assumed that upper hierarchical (strategic and tactical) decisions about the system configuration are given, e.g., the set of facilities to be refilled from a particular distribution center, and the characteristics of the fleet of vehicles assigned to serve those facilities are not directly considered. Moreover, in this initial development, a single-vehicle approach to the problem is assumed.

Demand processes at different facilities are assumed to be the only source of uncertainty; travel times between facilities are assumed to be fixed and known even though, in real-world applications, particularly in urban areas, uncertainties in traffic conditions could lead to significant travel time variation. Moreover, time associated with loading and unloading operations is not considered. In addition, is assumed that demands are known in probability distribution, and that these demand processes at retailers cannot be affected by the central decision maker.

Another important assumption is that daily and weekly cycle operation characteristics are not taken into account; that is, the system is assumed to be operating continuously, without interruption. Moreover, labor-related constraints are not considered. In short, it is assumed that the vehicle and all facilities are always in operation; i.e., deliveries can be scheduled at any time, with neither time windows for particular facilities nor restrictions on the number of hours that a driver can operate a vehicle. Therefore, delivery routes are constrained only by the vehicle’s capacity to transport products. Those other types of constraints would cloud the analysis, and interfere with the initial fundamental insights of interest in this investigation; future extensions could readily incorporate such constraints for implementation purposes.

## 2.2 Preliminaries and Problem Parameters

In order to present the OIRP, the following general notation is used. The set of retailers is designated as , $\Im   =   \{ 1 , 2 , . . . , i , . . . , N \}$ , and the set of all facilities (depot and retailers) as $\mathfrak { I } _ { 0 } ,   \mathfrak { I } _ { 0 } \equiv \mathfrak { I } \cup \{ 0 \}$ . Those $N { + } 1$ facilities are denoted by sub-index $i   =   0 { , } 1$ $2 , \ldots , N$ (sub-index 0 is for the depot) and are located in a bounded subset in the Euclidean space. The function $d _ { i j }$ gives the Euclidean distance between facilities i and $j ,$ or between a facility i and the vehicle location $j .$ Each retailer i has a maximum capacity to store inventory, $\kappa _ { i } ,$ measured in the units of the single product considered. In addition, the vehicle has limited capacity, $r ,$ measured in the same units, and is assumed to travel at constant speed according to the Euclidean metric. Without loss of generality, the vehicle speed is assumed to be one.

Each retailer i serves an independent demand process. In general, it is assumed that each facility serves a compound Poisson demand process, in which customer arrivals to retailers follow Poisson processes, and customers’ demand sizes are independent discrete random variables. Demand processes have associated arrival rates $\lambda _ { i } \left( t \right)$ for retailer i at time t. In addition, customer demand sizes are assumed to be Poisson distributed with mean $\theta _ { i } \left( t \right)$ . Thus the expected demand per unit of time at retailer i at time $t , \mu _ { i } \left( t \right)$ , can be calculated as $\mu _ { i } \left( t \right) = \lambda _ { i } \left( t \right) \cdot \theta _ { i } \left( t \right)$

The state of the system at time $t , X ( t )$ , can be described by the following parameters: (1) inventory levels at time $t , \iota ( t ) = ( \iota _ { 1 } ( t ) , . . . , \iota _ { i } ( t ) , . . . . , \iota _ { N } ( t ) )$ , where $\iota _ { i } ( t )$ is the inventory level at facility i at time $t ,   ( 2 )$ location of the truck at time $t ,   \ell ( t )$ , and (3) load remaining in the truck at time $t , \nu ( t )$ . Hence, the state of the system at time t can be expressed as:

$$
X (t) = \left[ \iota (t) \ell (t) \nu (t) \right]\tag{1}
$$

The decision maker can update plans at any epoch t based on $X \left( t \right)$ and past events, but without knowledge of future events. Plan updates are implemented immediately unless the vehicle is moving, in which case a time lag – between the epoch when a decision to update a plan is made and the plan is implemented – is considered. This is modeled using a time projection, which takes into account the time from the moment the decision to update the current plan is made until the new plan begins to be executed. Hence, instead of considering the actual state of the system at time t in the solution procedure, the state of the system is projected to a time $( t + \partial t )$ $\tilde { X } \left( t + \partial t \right)$ , assuming expected consumption rates and truck current speed and destination, where $\partial t$ is the projection time, which includes any solution procedure used to update plans and the time required for the driver to modify his current destination.

In the OIRP, there are three sets of cost parameters: (1) transportation cost per unit of distance traveled by the vehicle, TC, (2) inventory holding costs at each retailer $i ,   h _ { i }$ for retailer $i ,$ and (3) penalty associated with each unit of demand lost during stock-out, $p _ { i }$ at retailer i.

## 2.3 Decision Variables, Main Constraints and Objective Function

In this OIRP system, decisions available to the decision maker are related to truck plans, and consist of when, and how truck plans are updated. A plan or policy π, can be specified by the sequence of facilities to be visited, amounts to be delivered, and arrival times, to each one of those facilities. In addition, since the state of the system is continuously monitored and plans can be updated at any time, plan update epochs are also decision variables.

The main constraints that must be satisfied in the OIRP are related to the dynamics of the system and could be stated as follows:

(a) Inventory levels at each retailer are always non-negative and less than their capacity, i.e. $0 \leq \iota _ { i } \left( t \right) \leq \kappa _ { i } ,$ for $i \in \mathfrak { I }$ , and all t.

(b) At consumption epochs, if the demand size is greater than the inventory level at a particular facility, that inventory decrease the demand size, otherwise the difference between the demand size and the inventory remaining is lost demand and the inventory level decreases to zero.

(c) Inventory levels at retailers increase at delivery epochs by an amount equal to the amount delivered.

(d) The load remaining in the truck is always non negative, i.e., $\upsilon ( t ) \geq 0$ , for all t.

(e) The amount delivered to a retailer i is not greater than the load remaining in the vehicle at that delivery epoch, and the load remaining in the vehicle after the delivery is decreased by the quantity delivered.

(f) The total amount delivered in a tour does not exceed its capacity.

(g) The location of the truck is modified whenever the truck is not idle, and the truck moves toward the next facility at unit speed.

The objective of the central decision maker is to move the inventories in the system so as to minimize the expected total operating cost, composed of: (1) total transportation costs, (2) total inventory holding costs, and (3) total lost sales penalty costs.

Thus far, the formal definition of the problem studied in this Chapter has been introduced. The next section discusses major sources of complexity, the general approach that is being used to deal with the OIRP, and the proposed re-optimization strategies.

## 3 Proposed Real-Time Strategies for the OIRP

This section presents the general approach to deal with the OIRP, two benchmark policies used to compare the proposed strategies, and the formulation and design of re-optimization based strategies. Under those strategies, the inventory control side of the problem is solved first without considering joint replenishment to different facilities; the resulting fill-up-to levels are then used in a local off-line problem which is then solved in different real-time control strategies, reflecting different degrees of real-time information, to update plans.

## 3.1 General Approach

As previously stated, the OIRP does not seem to be tractable. Among the main difficulties in solving this control problem are:

(a) Simplified static and deterministic versions of the problem are NP-Hard, i.e., given the complete stream of future demands at each retailer, the associated inventory-routing problem, to optimally schedule deliveries to retailers, is very difficult to solve. In addition to the sequencing complexity of the problem, it is difficult to correctly capture the effect of short-term decisions on long-term costs, since deliveries depend on the time and amount reloaded in the previous visit to that facility. An optimal solution to the problem would require a long-term planning horizon; therefore, it is unlikely that the problem could be solved to near optimality in a reasonable time even for small problem-instances. This precludes the use of a complete static and deterministic IRP formulation for re-planning purposes in real-time operations.

(b) In addition to the combinatorial challenge of the static version of the problem, demands are dynamic and stochastic, and decisions can be updated at any time. In fact – in contrast with other real-time fleet operation problems in which requests to the system are clearly decision epochs – in the OIRP, final customer-demand epochs occur so often that it would be infeasible to adjust plans at each one of them. Thus, update epochs are not clearly defined, and obtaining the best update epoch is not trivial.

(c) Because retailer deliveries can be combined on the same route, optimal policies to serve each retailer depend not only upon that retailer’s inventory level, but also upon the state of the complete system. In fact, transportation costs to service a particular facility are not fixed, but depend upon the set of facilities served on the same route (Campbell et al., 1998, Bertazzi et al., 2007). Moreover, since a single vehicle serves all retailers, the lead time to replenish a particular retailer might be affected by congestion, in terms of the number of additional deliveries that are scheduled before that visit.

(d) Advances in real-time online combinatorial optimization neither provide tools to solve problems, such as the OIRP, to optimality nor give clear guidance on how to exploit online information in its operation (Grötschel et al., 2001b, Grötschel et al., 2001a).

(e) Finally, as in most real-time combinatorial problems, there is a trade-off between the quality of a new plan and the response time at update epochs.

Those difficulties preclude solving the problem or finding an optimal policy directly from the formulation presented in the previous section. Instead, an approach is proposed wherein the inventory control side of the problem is solved first, taking into account only a simplified version of the routing problem. In this approach, inventory reorder parameters are established for each facility and then used as target levels on a routing problem used to update plans.

For the proposed approach, different operational policies are proposed, tailored for different degrees of sophistication in terms of ICT. Those policies are based on a rolling-horizon framework, wherein new operational plans are repeatedly generated, based on updated information about the state of the system, and are implemented until the next update epoch is reached. In that scheme, operational strategies are defined by when and how plans are updated.

In terms of plan update epochs, three different cases are analyzed, ordered in terms of decreasing ICT requirements: (1) truck routes can be continuously updated, allowing for en-route diversions, (2) truck routes can be updated only at facilities (en-route diversion not allowed), and (3) truck routes cannot be updated after the truck leaves the depot, i.e. truck plans can be updated only upon tour completion. In all cases, full information about the state of the system at plan update epochs is assumed, and a Mixed-Integer Programming (MIP) problem formulation is solved for new plan generation.

In order to evaluate and compare proposed real-time strategies discrete-event simulation experiments are conducted. The proposed policies are compared to each other and against two benchmark policies described next.

## 3.2 Benchmark Policies

There are no accepted benchmarls for evaluating real-time fleet operational strategies. As discussed by Kim (2003), “detailed specifications of the problem have a significant impact on the performance of a policy.” Since the OIRP has not been studied before, two benchmark policies are introduced and developed.

The first benchmark policy, BENCH1, emulates what can be achieved operating the system in a decentralized manner with agents following optimal policies. In BENCH1, each retailer manages his own inventory, placing orders to a central supplier who, once a day, schedules deliveries for previous-day orders. In this case, based on the orders received at the end of each day, the supplier creates routes solving a Vehicle-Routing Problem (VRP). Each retailer will follow an optimal continuousreview policy to control his inventory, which in this case corresponds to an (s, S) policy. That $\dot { \mathbf { i } } \mathbf { s } ,$ each retailer will place an order of size (S-s) immediately if his inventory level is below s. The optimal parameters for an (s, S) policy can be obtained using Zheng and Federgruen algorithm (1991) or by exhaustive search over the feasible region.

The second benchmark policy, Most-Urgent-Next (MUN) is based on a simple greedy decision rule. Under MUN, at each delivery epoch, the vehicle is send next to refill the retailer closest to run out of inventory. To select the next retailer to be refilled, inventory levels are inspected, and the time at which each retailer would run out of inventory, if not visited, is calculated based on average consumption rates. If the vehicle has enough load remaining to refill the selected retailer, it would be sent directly to that location, otherwise it would go first to be refilled at the depot and then to that retailer. In that policy, each retailer i is refilled up to a pre-specified target level, $S _ { i } ,$ or up to capacity $K _ { i }$ . MUN implementation assumes that inventory levels are monitored and that routes are created so that the next delivery is decided upon refilling a retailer. In this strategy, whenever the vehicle is at the depot, a decision on waiting an additional time or departing immediately has to be weighed until vehicle departure. To evaluate the effect of waiting-additional-time decisions, for each facility the expected increment in lost sales costs is compared against transportation costs savings associated with waiting an additional time interval. If the expected increment in lost sale costs are smaller than transportation cost savings an additional time interval is waited, otherwise the vehicle is send to the most urgent facility.

In these benchmark policies, operational control parameters, such as reorder levels, are adjusted based on the specific parameters of each scenario.

## 3.3 Off-Line Optimization Problem Formulation

This subsection presents the local off-line problem used on optimization based control strategies to update plans. First, the general approach to locally update plan is presented. Second, optimization of refilling levels method is presented. Finally, a mathematical formulation of the routing problem used to update delivery plans is presented.

## a) Preliminaries

One of the main difficulties in formulating this problem is to be able to capture the effect of short-term decisions on long-run costs. If the customers were visited in isolation of each other using direct deliveries from the depot, served by independent vehicles, the optimal policy for each customer could be computed. In this case, a well known result on inventory control for single items inventory systems with stochastic consumption rates, constant replenishment lead times, and standard cost assumptions is the optimality of (s, S) policies, see for example Axsäter (2000) and Zipkin (2000). In an (s, S) policy each time the inventory position (inventory on hand plus on order minus backorders) is below s a delivery is scheduled to send a quantity equal to S minus the inventory position, so the inventory position becomes equal to S.

However, since only one truck is serving all customers and customer deliveries can be combined on the same route, transportation (delivery) costs are not fixed. Indeed, they would depend on the set of customers that are served together on the same route. Then the optimal policy to serve each customer would depend not only on its inventory level, but also on the complete state of the system.

To deal with this problem, optimal refilling levels for each facility are first specified, assuming that there is no pattern of deliveries. These levels are then kept as targets to refill up to, on each delivery, when plans are generated. However, there are only penalties associated with violating them as they are not included as hard constraints in the off-line routing problem. The off-line routing problem generates a plan that stipulates for each customer the next delivery time and quantity to refill, based on reorder quantities and on the current state of the system, i.e. inventory levels at each facility, and location and load remaining on the truck. This plan is obtained by minimizing the sum of transportation costs, and expected Lost Sales Penalty (LSP) costs, subject to visiting all customers once during the planning horizon.

In the next subsection, the method used to compute reorder quantities for each facility is presented, followed by the mathematical formulation of the off-line routing problem.

## b) Optimization of Refilling Levels

To compute the target refilling levels for each facility, the sum of expected costs (per time unit) for all facilities is minimized, assuming there is no pattern of deliveries and the truck visits only one customer per route. That is, the truck goes back to the depot after refilling a customer, and from there would go to the next customer as needed. Since the truck visits only one customer per route, transportation costs associated with serving a particular customer are fixed. However, even though customers are visited in isolation, the possibility of waiting for service due to the (single) truck serving other facilities is incorporated. Additionally, unlike traditional inventory systems where quantities are fixed after orders are placed, quantities can be updated upon arrival at the customer.

Then, using a policy that places orders when the inventory level is s and refills up to level S, the expected cost per time unit (AC) at steady state at each facility could be calculated using the renewal reward theorem (see for example [35]). An approximation made in the calculation of AC (in (3) below) is to neglect the impact of expected stock-out time during the cycle on the cycle length and holding costs (see Axsäter, 2000 pp. 65), as follows:

$$
A C _ {i} = \frac {\mathrm{E} [ \text {cost per cycle} ]}{\mathrm{E} [ \text {cycle length} ]}\tag{2}
$$

$$
A C _ {i} \approx \frac {F T C _ {i} + h _ {i} \left(\frac {S _ {i} - s _ {i}}{\mu_ {i}} + L _ {i}\right) \left((s _ {i} - L _ {i} \mu_ {i}) + \frac {1}{2} (S _ {i} - s _ {i} + L _ {i} \mu_ {i})\right) + p _ {i} \cdot \sigma_ {i} \sqrt {L _ {i}} \cdot G \left(\frac {s _ {i} - L _ {i} \mu_ {i}}{\sigma_ {i} \sqrt {L _ {i}}}\right)}{\left(\frac {S _ {i} - s _ {i}}{\mu_ {i}} + L _ {i}\right)}\tag{3}
$$

where $F T C _ { i }$ is the fixed transportation cost to serve retailer i (in isolation); G(x) is the loss function that gives the expected number of lost sales at the end of a period with demand distributed N(0,1) given that the initial inventory level is x (see Axsäter, 2000); and $L _ { i } = T + d _ { 0 i } + W _ { i }$ , is the sum of the review period, $T$ , and the total lead time. The length of the review period, $T ,$ is the time between plan updates and depends on the policy implemented. The lead time is composed of travel time from the depot to retailer $i ,   d _ { 0 i }$ , and the expected waiting time $W _ { i }$ for retailer i. This expected waiting time could be expressed, as a function of reorder quantities, using the following recursive expression:

$$
W _ {i} = \sum_ {j \neq i} \left\{\underbrace {\operatorname* {P r} \{\text {ret.} j \text {is in service} \}} _ {\beta_ {j}} \cdot \left(d _ {0 j}\right) + \underbrace {\operatorname* {P r} \{\text {ret.} j \text {is waiting for service} \}} _ {\gamma_ {j}} \cdot \left(2 d _ {0 j}\right) \right\}\tag{4}
$$

$$
\beta_ {j} = \frac {2 d _ {0 j}}{\left(\frac {S _ {j} - s _ {j}}{\mu_ {j}}\right) + L _ {j}},\tag{5}
$$

and

$$
\gamma_ {j} = \frac {W _ {j}}{\left(\frac {S _ {j} - s _ {j}}{\mu_ {j}}\right) + L _ {j}}\tag{6}
$$

where $\beta$ and $\gamma$ are the proportion of the cycle in which a retailer is being served and waits for service, respectively. To evaluate the waiting times for all facilities, given a vector of reorder quantities, a bisection procedure is used iteratively until the waiting times for all facilities are consistent.

Finally, to obtain the optimal reorder quantities, the sum of average cost for all facilities is minimized, subject to $L _ { i } = T + d ( 0 , i ) + W _ { i } ;$ equations (4), (5), and $( 6 ) ;$ and $\textstyle \sum _ { i } 2 d _ { 0 i } \cdot ( \mu _ { i } / ( S _ { i } - s _ { i } ) )   <   1$ . The first four are definitional constraints, and the fourth implies that truck utilization rate should be less than 100%. This problem is solved using a steepest decent numerical procedure, in which at each step the gradient is evaluated numerically. Then, the solutions found in this step are used as input parameters every time the off-line routing problem presented in the next subsection is called.

## c) Mathematical Formulation of the Problem

In this off-line routing problem, the current inventory levels at all facilities are considered as given, as are the load remaining and the distance to all facilities for the truck. When the truck is at the depot the load remaining is equal to the truck capacity. Additional input parameters are the transportation cost TC [\$/hr]; inventory holding cost $h_{i}   [\mathrm{\bar{S}/unit-day}]$ ; lost sales cost $p _ { i }$ [\$/unit]; and order up to level $S _ { i }$ [units].

It is assumed that the central decision maker would try to follow the optimal reorder up to S policy for each customer. However, since patterns of deliveries are not considered, he/she would deviate from that policy to take advantage of transportation savings. In order to measure the impact on transportation and inventory cost of deviating from the reorder up to S policy, Incremental Inventory Costs (IIC) for each facility are computed. These IIC are calculated as a one time deviation from the reorder up to S policy, assuming that after this deviation the optimal policy is resumed. These IIC can be expressed as the sum of expected Incremental Transportation Costs (ITC), and expected Lost Sales Penalty costs (LSP). Notice that the impacts on holding costs are only considered through the specification of reorder up to levels. To compute ITC, first notice that if each retailer is considered in isolation, for a given consumption rate $\mu ,$ the minimum transportation costs are achieved when deliveries arrive when the inventory level is zero and the quantity delivered is S. In this case transportation costs per unit of time are $F T C \cdot ( \mu / S )$ . Then ITC, associated with scheduling a delivery of size $q$ units at time t after the current time, given that the current inventory level is $\iota ,$ could be expressed as

$$
I T C (q, t / \iota) = \left(\frac {F T C}{\left(\frac {q}{\mu}\right)} - \frac {F T C}{\left(\frac {S}{\mu}\right)}\right) \left(\frac {q}{\mu}\right) = F T C \cdot \left(\frac {\mu}{q} - \frac {\mu}{S}\right) \left(\frac {q}{\mu}\right) = F T C \cdot \left(1 - \frac {q}{S}\right)\tag{7}
$$

where $0 \leq q \leq ( S - \iota   +   \mu   \cdot   t )$ , and S is the optimal reorder up to level. On the other hand, expected Lost Sale Penalty (LSP) costs, associated with scheduling a delivery at time t after the current time, given that the current inventory level is ι, could be computed, approximating the distribution of total demand during t as $\mathrm { N } ( t \mu , t \sigma ^ { 2 } )$ , as:

$$
L S P (t / \iota) = p \cdot \int_ {\iota} ^ {\infty} (u - \iota) f _ {D (t)} (u) d u\tag{8}
$$

$$
LS  P(t / \iota) = p\cdot \sigma \sqrt{t}\int_{\substack{\frac{\iota - t\mu}{\sigma\sqrt{t}}}}^{\infty}\left(v - \left(\frac{\iota - t\mu}{\sigma\sqrt{t}}\right)\right)\phi (v)dv = p\cdot \sigma \sqrt{t}\cdot G\left(\frac{\iota - t\mu}{\sigma\sqrt{t}}\right)\tag{9}
$$

Based on these IIC, an off-line problem could be formulated similarly to a vehicle routing problem (VRP), where the next visit to each customer is scheduled based on its current inventory level, but adding in the objective function the IIC. This static off-line problem is formulated as minimizing the sum of IIC for all retailers and total transportation costs for the next delivery, subject to visiting all customers once during the planning period (next week) and inventory levels not exceeding order – up-to levels, S, for each retailer.

Thus, the variables of this problem are:

$q _ { i } ^ { r }$ : Quantity to be delivered to retailer i by the truck in its $r ^ { t h }$ tour, where tours are numbered from 0 (0 is the current tour).

$$
x _ {i j} ^ {r} = \left\{ \begin{array}{l} 1 \text {If facility} j \text {is visited immediately after facility} i \text {by the truck} \\ \quad \text {in its} r ^ {t h} \text {tour} \\ 0 \text {Otherwise} \end{array} \right.
$$

$$
y _ {i} ^ {r} = \left\{ \begin{array}{l} 1 \text {If facility i is served by the truck in its r^{th} tour} \\ 0 \text {Otherwise} \end{array} \right.
$$

$t _ { i }$ : Arrival time to retailer i. $( i \in \mathfrak { I } )$ .

$t _ { 0 } ^ { r } ;$ Arrival time to the depot by the truck in its $r ^ { t h }$ tour. $t _ { 0 } ^ { 0 }$ is the truck arrival time to the depot in its current tour.

In addition, the parameters of this model are:

$\iota _ { i }$ : Retailer i current inventory level.

$\kappa _ { i }$ : Retailer i capacity to store inventory.

$\gamma$ : Truck capacity.

ν : Load remaining in the truck, which is equal to $\gamma$ when the truck is at the depot.

TC : Transportation cost per unit of distance traveled by the truck. This is measured in [\$/hr], since the truck moves at constant speed.

$h _ { i }$ : Retailer i inventory holding cost [\$/unit-day].

$p _ { i }$ : Retailer i lost sales cost per unit of demand not satisfied [\$/unit].

$S _ { i }$ : Retailer i order up to level [units].

$s _ { i }$ : Retailer i reorder level [units].

: Facility where the truck is currently located. $\ell   \in   \{ 0 , 1 , 2 , . . . , N , N + 1 \}$ , it is equal to N+1 when truck is en-route. In this case, a dummy node, N+1, is created at the projected position.

$d _ { i j } \cdot$ Distance from facility i to facility j. Notice that when the truck is en-route distance from the dummy node $N { + } 1$ to all facilities should be included.

$\Re   \equiv   \{ 0 , 1 , 2 , . . . , R \}$ : Set of tours (routes) for the truck in the planning horizon, where R is the maximum number of tours not considering the current tour $( r = 0 )$ Thus, $r \in \mathfrak { R }$

H : Length of planning horizon (maximum number of hours of operation).

The Mixed Integer Programming (MIP) formulation is presented below:

$$
\text {Min.} \sum_ {i \in \mathfrak {I}} L S P _ {i} (t _ {i} / \iota_ {i}) + \sum_ {i \in \mathfrak {I}} \sum_ {r \in \Re} I T C _ {i} (q _ {i} ^ {r}, t _ {i} / \iota_ {i}) \cdot y _ {i} ^ {r} + T C \cdot \sum_ {i \in \mathfrak {I} _ {0}} \sum_ {j \in \mathfrak {I} _ {0}: j \neq i} d _ {i j} \cdot \left(\sum_ {r \in \Re} x _ {i j} ^ {r}\right)\tag{10}
$$

$$
\begin{array}{l} = \sum_ {i \in \mathfrak {I}} \left\{p _ {i} \cdot \sigma_ {i} \sqrt {t _ {i}} \cdot G \left(\frac {\iota_ {i} - t _ {i} \mu_ {i}}{\sigma_ {i} \sqrt {t _ {i}}}\right) \right\} + \sum_ {i \in \mathfrak {I}} \sum_ {r \in \Re} F T C _ {i} \cdot y _ {i} ^ {r} - \sum_ {i \in \mathfrak {I}} \sum_ {r \in \Re} F T C _ {i} \cdot \left(\frac {q _ {i} ^ {r}}{S _ {i}}\right) + \\ T C \cdot \sum_ {i \in \mathfrak {I} _ {0}} \sum_ {j \in \mathfrak {I} _ {0}: j \neq i} d _ {i j} \cdot \left(\sum_ {r \in \Re} x _ {i j} ^ {r}\right) \end{array}
$$

Subject to:

(11)

$$
\sum_ {j \in \mathfrak {I} _ {0}: j \neq i} \sum_ {r \in \mathfrak {R}} x _ {i j} ^ {r} = 1 \quad , \text {for} i \in \mathfrak {I}\tag{12}
$$

$$
\sum_ {i \in \mathfrak {I}} x _ {i 0} ^ {r} = 1 \quad , \text {for} r = 1, 2, \dots , R\tag{13}
$$

$$
\sum_ {i \in \mathfrak {I}} x _ {i 0} ^ {0} + x _ {N + 1, 0} ^ {0} = 1\tag{14}
$$

$$
\sum_ {j \in \mathfrak {T} _ {0}: j \neq \ell} x _ {\ell j} ^ {0} = 1\tag{15}
$$

$$
\sum_ {j \in \mathfrak {I} _ {0}: j \neq i} x _ {i j} ^ {0} = \sum_ {j \in \mathfrak {I} _ {0}: j \neq i} x _ {j i} ^ {0} + \mathbf {1} \left\{i = \ell \right\}, \text {if} \ell \neq N + 1; \text {for} i \in \mathfrak {I}\tag{16}
$$

$$
\sum_ {j \in \mathfrak {I} _ {0}: j \neq i} x _ {i j} ^ {0} = \sum_ {j \in \mathfrak {I} _ {0}: j \neq i} x _ {j i} ^ {0} + x _ {N + 1, i} ^ {0}, \text {if} \ell = N + 1; \text {for} i \in \mathfrak {I}\tag{17}
$$

$$
\sum_ {j \in \mathfrak {I} _ {0}: j \neq i} x _ {i j} ^ {r} = \sum_ {j \in \mathfrak {I} _ {0}: j \neq i} x _ {j i} ^ {r}, \text {for} i \in \mathfrak {I} _ {0}; r = 1, 2, \dots , R\tag{18}
$$

$$
\sum_ {j \in \mathfrak {J}} x _ {0 j} ^ {1} \leq \sum_ {i = 1} ^ {N + 1} x _ {i 0} ^ {0}\tag{19}
$$

$$
\sum_ {j \in \mathfrak {I}} x _ {0 j} ^ {r} \leq \sum_ {i \in \mathfrak {I}} x _ {i 0} ^ {(r - 1)} \quad , \text {for} r = 2, 3, \dots , R\tag{20}
$$

$$
\sum_ {i \in \mathfrak {I}} x _ {\ell i} ^ {0} \geq \sum_ {i \in \mathfrak {I}: i \neq j} x _ {i j} ^ {0}, \text {for} j \in \mathfrak {I}\tag{21}
$$

$$
\sum_ {i \in \mathfrak {I}} x _ {0 i} ^ {r} \geq \sum_ {i \in \mathfrak {I}: i \neq j} x _ {i j} ^ {r}, \text {for} j \in \mathfrak {I}; r = 1, 2, \dots , R\tag{22}
$$

$$
t _ {j} \geq t _ {i} + d _ {i j} - M \left(1 - x _ {i j} ^ {r}\right), \text {for} i \in \mathfrak {I}; j \in \mathfrak {I}; r \in \mathfrak {R}\tag{23}
$$

$$
t _ {j} \leq t _ {i} + d _ {i j} + M \left(1 - x _ {i j} ^ {r}\right), \text {for} i \in \mathfrak {I}; j \in \mathfrak {I}; r \in \Re\tag{24}
$$

$$
t _ {j} \geq d _ {\ell j} - M \left(1 - x _ {\ell j} ^ {0}\right), \text {for} j \in \mathfrak {I}\tag{25}
$$

$$
t _ {j} \leq d _ {\ell j} + M \left(1 - x _ {\ell j} ^ {0}\right), \text {if} \ell \neq 0, \text {for} j \in \mathfrak {I}\tag{26}
$$

$$
t _ {j} \geq t _ {0} ^ {r} + d _ {0 j} - M \left(1 - x _ {0 j} ^ {(r + 1)}\right) \quad , \text {for} j \in \mathfrak {I}, r \in \Re\tag{27}
$$

$$
t _ {\ell} = 0, \text {if} \ell \neq N + 1\tag{28}
$$

$$
t _ {0} ^ {0} \geq d _ {N + 1, 0} - M \left(1 - x _ {N + 1, 0} ^ {0}\right), \text {if} \ell = N + 1\tag{29}
$$

$$
t _ {0} ^ {0} \leq d _ {N + 1, 0} + M \left(1 - x _ {N + 1, 0} ^ {0}\right) \quad , \text {if} \ell = N + 1\tag{30}
$$

$$
t _ {0} ^ {r} \geq t _ {i} + d _ {i 0} - M \left(1 - x _ {i 0} ^ {r}\right), \text {for} i \in \mathfrak {I}; r \in \Re\tag{31}
$$

$$
t _ {0} ^ {r} \leq t _ {i} + d _ {i 0} + M \left(1 - x _ {i 0} ^ {r}\right), \text {for} i \in \mathfrak {I}; r \in \Re\tag{32}
$$

$$
t _ {0} ^ {r} \geq t _ {0} ^ {(r - 1)} \quad , \text {for} r = 1, 2, \dots , R\tag{33}
$$

$$
t _ {0} ^ {R} \leq \mathrm{H}\tag{34}
$$

$$
\sum_ {j \in \mathfrak {I} _ {0}: j \neq i} x _ {i j} ^ {r} = y _ {i} ^ {r}, \text {for} i \in \mathfrak {I}; r \in \Re\tag{35}
$$

$$
0 \leq q _ {i} ^ {r} \leq \mathcal {Y} \cdot y _ {i} ^ {r}, \text {for} i \in \mathfrak {I}; r \in \Re\tag{36}
$$

$$
\sum_ {i \in \mathfrak {I}} q _ {i} ^ {r} \leq \mathcal {Y}, \text {for} r = 1, 2, \dots , R\tag{37}
$$

$$
\sum_ {i \in \mathfrak {I}} q _ {i} ^ {0} \leq \nu\tag{38}
$$

$$
s _ {i} - \iota_ {i} + \mu_ {i} t _ {i} \leq \sum_ {r \in \Re} q _ {i} ^ {r} \leq S _ {i} - \iota_ {i} + \mu_ {i} t _ {i}, \text {for} i \in \Im : i \neq \ell\tag{39}
$$

$$
\min \{(s _ {\ell} - \iota_ {\ell}), \nu \} \leq q _ {\ell} ^ {0} \leq S _ {\ell} - \iota_ {\ell}, \text {if} \ell \neq N + 1\tag{40}
$$

$$
x _ {i j} ^ {r} \in \{0, 1 \} \text {and} y _ {i} ^ {r} \in \{0, 1 \} \quad , \text {for} i \in \mathfrak {I} _ {0}; j \in \mathfrak {I} _ {0}; r \in \mathfrak {R}\tag{41}
$$

$$
x _ {N + 1, j} ^ {0} \in \{0, 1 \} \quad , \text {if} \ell = N + 1, \text {for} j \in \mathfrak {I} _ {0}\tag{42}
$$

The objective function (10)–(11) minimizes the sum of the total expected lost sale penalties at each facility for the next scheduled visit, and the total transportation costs.

All tours start at the depot with a full truck, with the exception of the current tour, $r = 0$ , in which the truck starts at any facility or en-route (at node $N { + } 1 )$ , and the truck might not be full (its current load is ν).

Constraint (12) ensures that the next visit for each retailer is programmed. Equations (13) and (14) ensure that the truck returns to the depot in all its tours. Constraint (15) dictates that the truck should leave from its current location. Constraints (16)– (17)–(18) give continuity of flow ensuring that the number of arrivals equals the number of departures at each node. Constraints (19)–(20) ensure that subsequent routes could be traveled only if the previous route is completed. Constraints (21)–(22) ensure that current route leave the initial node and subsequent routes leave the depot to visit retailers. Constraints (23) through (33) ensure that the arrival times at each facility are consistent with travel times between them and the initial conditions, where M is a big number. Constraint (34) dictates that the last route should be completed before the end of the planning horizon H. Constraint (35) relates facilities served on each route with its links. Constraints (36) guarantee that only customers visited from a particular route could receive deliveries from it. Constraints (37)–(38) ensure that the truck capacities are not exceeded and that the quantity delivered cannot exceed the load remaining in the vehicle. Constraints (39)–(40) guarantee that inventory levels should not exceed the order up to level, $S _ { i }$ and inventory level should be greater than $s _ { i }$ after refilling; however an exception is allowed at the current facility if the load remaining in the truck is insufficient (40).

As mentioned, the purpose of this formulation is to update truck plans making use of updated information about the state of the system. The next section describes three strategies that solve this formulation in a rolling horizon framework.

## 3.4 Re-optimization Based Real-Time Strategies

The off-line problem described in the previous section will be used to determine how to update truck routes and inventory allocations in a rolling horizon framework. Different policies could be devised based on how often the off-line problem is solved and/or how many steps of the current solution are implemented before solving a new instance with updated system state information. Three policies, ordered in terms of increasing ICT requirement, are presented and tested. These are Replan at Tour Completion (RTC), Replan at Delivery Epochs (RDE), and Replan at Delivery Epochs with possible en-route diversions (RDE+div).

## a) Replan at Tour Completion (RTC) Strategy

In Replan at Tour Completion (RTC), the off-line IRP is solved each time the truck returns to the depot, i.e. completes a tour, and only the first route of the current solution is implemented. In this policy, the review period, T, used to compute the optimal refill levels, is obtained as the expected distance on a tour over the set of retailers.

## b) Replan at Delivery Epochs (RDE) Strategy

In Replan at Delivery Epochs (RDE), the off-line problem is called at delivery epochs. Each time a truck arrives to a facility, either a retailer or the depot (delivery epoch), an off-line IRP is solved and the solution implemented until the next delivery epoch. That is the amount specified by the solution is delivered at the current facility, and the truck is sent to the next facility specified by the solution. In this policy, the review period, T, used to compute the optimal refilling levels, is obtained as the expected distance between two retailers.

## c) Replan at Delivery Epochs with Possible En-Route Diversion (RDE+div) Strategy

In Replan at Delivery Epochs with possible en-route diversion (RDE+div), plans are updated at delivery epochs, as in RDE, as well as when demand disruptions occur. In this case, inventory levels are continuously monitored while the vehicle is traveling; whenever a facility’s consumption since the last plan update falls below or above 3 standard deviations from its expected demand, the current plan is updated. To update the plan, the state of the system (i.e. the location of the truck and inventory levels assuming expected consumption rates) is first projected. Then, based on the projected state of the system, an off-line routing problem is solved and the next step implemented. In this strategy, the truck could be diverted if in the new plan the next facility to be visited differs from the current destination.

In order to solve the off-line IRP formulation used in these strategies, the first term in equation is piecewise linearized, so that small instances can be efficiently solved using CPLEX 10.0 with default settings. This problem can be solved in a few seconds for most instances with less than six facilities and a few minutes for instance with less than nine facilities. The design of heuristics to solve larger size instances is beyond the scope of this Chapter, and is left as a future extension.

## 4 Simulation Experiments and Results

This section describes the experiments designed to evaluate and compare proposed real-time policies, and discusses the results. Simulation runs were performed with all three re-optimization strategies, RTC, RDE and RDE+div, as well as the two benchmark policies, BENCH1 and MUN presented in the previous section.

## 4.1 Simulation Scenarios

This section presents the main elements and defining parameters of the simulated scenarios. First, the set of fixed parameters used in all simulations is introduced. Second, parameters in scenarios with steady-state demand processes are defined. Third, inventory reorder levels are obtained for each combination of strategy and scenario simulated. Finally, experiments with demand disruption at one facility are presented.

Because of limited computational resources (each simulation run takes hours of computer time – even days for some re-optimization strategies –), a full factorial design was not practical, so not all parameter combinations were applied. For each strategy, simulations were performed for four cases of facility layouts, and 12 param eter sets, representing typical cost settings, probabilistic scenarios, and constraints.

Distances between facilities are Euclidean and are measured in units of time [hours], because it is assumed, without loss of generality, that the vehicle moves at unit speed. All facilities are located in a square region, with side length of 4 h, with the depot in the center of the square region, i.e. the depot is located at (2, 2). In all cases simulated, seven retailers and one depot are considered. In case 0, retailers are symmetrically distributed around the depot at 1.2 h apart, and in cases 1 to 3 they are randomly distributed in the region. Figures 1 through 4 show the locations of facilities for each case. Facilities were renumbered to coincide with their position in the TSP tour.

In addition to the location of facilities for each case studied, the following set of parameters is considered as fixed: the vehicle capacity, $\mathcal { T } = 4 0 0$ [units]; the length of the planning horizon used on the off-line problem for re-optimization strategies, $\mathrm { H } = 1 0 0$ [hrs] which is also assumed to be the amount of working hours per week; lost sales penalty costs, $p _ { i } = 1 0 0   [ \mathrm { \AA / u n i t } ]$ for all retailers; and the fixed transportation costs used to obtain refill levels for re-optimization strategies, $F T C _ { i } = 2 \cdot d _ { 0 i } \cdot T C _ { i }$ which is computed as twice the cost of a tour from the depot only to that retailer. In addition, the time projection used in the case of diverting the vehicle is 6 min, i.e. $\partial t = 6   \mathrm { m i n }$

Two sets of scenarios were studied: (1) products with high inventory-holding costs and no capacity constraints at retailers’ sites, and (2) products with low inventory-holding costs and capacity constraints at retailers’ sites. Scenarios with low inventory holding costs and no capacity constraints at retailers were not considered, since for those scenarios the best policy would be full-truckload deliveries.

For each set of scenarios, a base case was considered. Parameter set 1 is the base case for high inventory-holding cost scenarios, in which $TC = 100   [\mathrm{S/hr}],   h_i = 10$ [\$/unit-day] for all retailers, and demand parameters are the same for all retailers, and

![](images/page_130_chart_2.jpg)

Fig. 1. Location of facilities for Case 0 (Symmetric case)

![](images/page_130_chart_4.jpg)

Fig. 2. Location of facilities for Case 1

![](images/page_131_chart_2.jpg)

Fig. 3. Location of facilities for Case 2

equal to $\lambda _ { i } = 5 0$ [arrivals/Day] and $\theta _ { i } = 1$ [units], for all i. This demand process can be approximated as $N ( 5 0 , 1 0 ^ { 2 } )$ for daily periods. For low inventory-holding cost scenarios, Parameter set 7 is the base case, in which $h_{i}=1\ [\mathrm{S/unit-day}], \kappa_{i}=100$ [units] for all retailers, and the remaining parameters are the same as in Parameter set 1.

![](images/page_131_chart_5.jpg)

Fig. 4. Location of facilities for Case 3

In order to analyze the impact of transportation costs and demand variability on the proposed policies, ten additional scenarios were designed, as shown in Table 1. In scenarios with high (low) inventory holding costs and without (with) retailer capacity constraints, parameter sets 2 and 3 (8 and 9) capture variation in transportation costs, whereas parameter sets 4 to 6 (10 to 12) reflect differing levels of demand variability.

In the experimental design, the magnitude of each cost parameter is less relevant than the relationship among them. For that reason, the scenarios studied vary the ratio between transportation and inventory costs.

The reorder parameters of the (s, S) policy used in BENCH1 were obtained using Zheng and Federgruen algorithm (1991). RTC and RDE reorder parameters were obtained using the procedure described in Sect. 3.3.2. The only difference between RTC and RDE is the review period considered. In RTC the expected TSP length was used, and in RDE the expected distance between two facilities was used. For the MUN strategy, RDE refilling up to levels, S, were used.

Table 1. Simulation scenarios

| Parameter Set | TC[$/hr] | h[$/day] | κ[units] | λ[arrivals/day] | θ[units] | Approx.N(μ,σ2) |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 100 | 10 | ∞ | 50 | 1 | N(50,102) |
| 2 | 33 | 10 | ∞ | 50 | 1 | N(50,102) |
| 3 | 300 | 10 | ∞ | 50 | 1 | N(50,102) |
| 4 | 100 | 10 | ∞ | 10.5 | 4.8 | N(50,172) |
| 5 | 100 | 10 | ∞ | 4.35 | 11.5 | N(50,252) |
| 6 | 100 | 10 | ∞ | 2.4 | 20.8 | N(50,332) |
| 7 | 100 | 1 | 100 | 50 | 1 | N(50,102) |
| 8 | 33 | 1 | 100 | 50 | 1 | N(50,102) |
| 9 | 300 | 1 | 100 | 50 | 1 | N(50,102) |
| 10 | 100 | 1 | 100 | 10.5 | 4.8 | N(50,172) |
| 11 | 100 | 1 | 100 | 4.35 | 11.5 | N(50,252) |
| 12 | 100 | 1 | 100 | 2.4 | 20.8 | N(50,332) |

## 4.2 Simulation Results

For every combination of strategy and set of parameters studied, simulations were carried for 30 replication runs of 100 h (1 week) each, and all four facility layout cases. For each parameter set, the different strategies were simulated with common random numbers (for demand generation), and the same initial conditions. The initial conditions for the first replication were the same for all strategies in the same scenario, starting with the vehicle at the depot, and the same initial inventory levels. The effect of initial conditions is only relevant up to the first visit to each facility, which is small compared to the length of each run to have significant effects. Moreover, those initial conditions were only used in the first replication, and results suggest that transient-state effects are negligible.

For each simulation run, the following measures of performance were examined: average transportation costs; average inventory holding costs; and average lost-sale penalty costs. For each of those measures, interval estimates were obtained. These results are presented in Appendix.

## 4.3 Analysis of Results

Simulations were carried only under typical system parameters, and run under idealized probabilistic distributions. Thus, the results presented are valid only for the range of values studied, which are nonetheless intended to be representative of realworld applications, and hence adequate to provide general insight for them.

For all parameter sets considered, the three proposed online strategies systematically outperformed benchmark strategies. The best proposed strategies achieved reductions in average total costs of approximately 30 and 15% compared against benchmark policies BENCH1 and MUN, respectively. The average cost improvements were computed as the average of:

$$
\frac {(\text {Avg. Total Cost of Strategy} - \text {Avg. Total Cost of BENCH})}{\text {Avg. Total Cost of BENCH}} \cdot 100\%\tag{43}
$$

For all sets of parameters and cases considered. Moreover, the optimal decentralized benchmark policy, BENCH1, was systematically outperformed by centralized strategies. This can be explained in part by the fact that BENCH1 tends to carry more inventory to protect against longer lead times. In addition, all proposed strategies achieved less variability in average costs than the BENCH1 strategy.

Among re-optimization strategies, those that update plans at delivery epochs, RDE and RDE+div, were the best strategies for the set of parameters considered. The possibility of diversion – either en-route or when the vehicle is idle at the depot – improves system performance in scenarios with low inventory-holding costs and high demand variability. However, further research is needed to better delineate scenarios in which en-route diversion could be beneficial, since in RDE vehicle idle time at the depot is set upon arrival and not updated, even when that might be profitable. The benefits of re-planning at delivery epochs tend to be higher in cases where there are clusters of facilities close to each other and/or near to the depot, such as in case 2.

As noted, experiments were carried out for two sets of scenarios: (1) products with high inventory-holding costs, and (2) products with low inventory-holding costs and retailer capacity constraints. As shown in Fig. 5, a comparison of the two sets of scenarios illustrates that re-planning strategies tended to increase their benefits relative to the benchmark policies when applied to scenarios with low inventoryholding costs.

![](images/page_134_chart_2.jpg)

Fig. 5. Impact of inventory holding cost

In Figs. 6 and 7, reductions in average total costs for proposed re-planning strategies vs. the two benchmark policies are illustrated. In scenarios with high inventory-holding costs (Fig. 6), the benefits of the proposed strategies tend to decrease (increase) as transportation costs increase, when compared with BENCH1 (MUN). That again can be explained by the longer lead times in BENCH1, requiring facilities to carry more inventory. Thus, the higher the inventory-holding costs, the worse the performance of BENCH1.

In scenarios with low inventory-holding costs and retailer capacities (Fig. 7), the benefit of the proposed strategies tends to increase, as transportation costs increase when compared to any of the benchmark policies. Thus, with the exception of BENCH1, for scenarios with high inventory-holding costs, the benefits of the proposed re-planning strategies tend to increase as a function of the proportion of transportation costs in the total cost function.

Among re-planning strategies when transportation costs are more significant in the total costs, re-planning at delivery epochs is less beneficial, compared with replanning only at tour completions. A comparison between RDE and RTC shows that RDE reduced by approximately 11, 8, and 4% the average total costs in scenarios with high inventory-holding costs, i.e. under parameter sets 2 (TC = 33), 1 (TC = 100), and 3 (TC = 300), respectively. In scenarios with low inventory-holding costs, the differences are less dramatic and remain relatively constant (around 2.5%) with respect to changes in transportation costs. Those differences could be explained mainly by the higher inventory levels maintained under RTC, which amplify the differences between RDE and RTC when inventory-holding costs are predominant in the total cost function.

![](images/page_135_chart_2.jpg)

Fig. 6. Impact of increments in transportation costs in scenarios with high inventory holding cost, parameter sets 1, 2 and 3

![](images/page_135_chart_4.jpg)

Fig. 7. Impact of increments in transportation costs in scenarios with low inventory holding cost, parameter sets 7, 8 and 9

As shown in Fig. 8, with high inventory-holding costs, as demand variability increases, the benefits of the proposed strategies tend to decrease, compared to benchmark strategies. Conversely, in scenarios with low inventory-holding costs and capacity constraints (Fig. 9), the benefits of the proposed strategies tend to increase vs. BENCH1 and decrease vs. MUN, as demand variability increases. As expected, MUN becomes more competitive in scenarios with very high demand variability. In scenarios with increased demand variability, i.e. those with parameter sets 5, 6, 11, and 12, the advantage of re-planning at delivery epochs vs. only at tour completion tends to be slightly higher than in scenarios with less demand variability.

The possibility of diversion – either en-route or when the vehicle is idle at the depot – improves system performance in scenarios with low inventory-holding costs and high demand variability. However, further research is needed to identify scenarios in which en-route diversion would be beneficial.

![](images/page_136_chart_4.jpg)

Fig. 8. Impact of increments in demand variability in scenarios with high inventory-holding costs, parameter sets 1, 4, 5 and 6

## 5 Conclusion

In this Chapter the OIRP was introduced and three rolling horizon strategies were proposed, corresponding to different degrees of sophistication in terms of ICT. The central idea of the proposed approach (which is then applied online with varying triggers depending on the operational control strategy followed), is to establish inventory reorder parameters for each facility, and use those as target levels in the routing problem solved to update the plans. These target levels are obtained by solving the inventory control side of the problem first, assuming known transport costs corresponding to a simplified version of the routing problem. The routing problem used to update plans includes both transportation and inventory-related costs in its objective function, and is formulated as a MIP, solved for small instances in the experiments presented in the paper using a commercial solver.

![](images/page_137_chart_2.jpg)

Fig. 9. Impact of increments in demand variability in scenarios with low inventory-holding costs, parameter sets 7, 10, 11 and 12

The proposed strategies were compared against two benchmark policies using a general discrete-event simulation framework. The proposed re-planning strategies are shown to systematically outperform the two benchmark policies. Among proposed strategies, those that update plans at delivery epochs exhibited superior performance for the set of parameters considered in the experiments.

The work presented here represents a first step in addressing the complex problem of optimally operating logistics processes in real-time. It has been previously established that combining inventory planning with fleet operation could result in potentially considerable savings relative to operating each process separately. Operating the two processes jointly in real-time can help realize those advantages, and amplify them substantially by responding more effectively to demand fluctuations. The specific problem addressed in this Chapter can be extended along several dimensions, including multiple-vehicle fleets, additional echelons, multiple product types, among many others. For systems with non-affiliated retailers, the problem and approach presented here provide an example of collaborative logistics, which give rise to interesting problem classes and open significant opportunities for novel approaches and mechanisms for achieving mutual gains through online collaboration.

## Acknowledgments

The first author would like to thank the Chilean National Fund for the Development of Scientific and Technological Research (FONDECYT Project 1107218) for partially financing this research.

## References

[1] Axaäter, S. (2000) Inventory control, Boston, Mass.; London, Kluwer Academic.

[2] Baita, F., Ukovich, W., Pesenti, R. & Favaretto, D. (1998) Dynamic routingand-inventory problems: A review. Transportation Research Part a-Policy and Practice, 32, 585-598.

[3] Bertazzi, L., Savelsbergh, M. & Speranza, M. G. (2007) Inventory Routing.

[4] Blanchard, D. (2003) Fears of ”Big Brother” sidetrack Benetton’s smart tag initiative. Transportation and Distribution, 44, 20.

[5] Campbell, A. M., Clarke, L. W. & Savelsbergh, M. (1998) The inventory routing problem. In, Crainic T. G. & Laporte, G. (Eds.) Fleet Management and Logistics. Dordrecht, The Netherlands, Kluwer Academic Publishers.

[6] Campbell, A. M. & Savelsbergh, M. (2002) Inventory Routing in Practice. In Toth, P. & Vigo, D. (Eds.) The Vehicle Routing Problem. SIAM Monographs on Discrete Mathematics and Applications.

[7] Chen, F., Drezner, Z., Ryan, J. K. & Simchi-Levi, D. (2000) Quantifying the bullwhip effect in a simple supply chain: The impact of forecasting, lead times, and information. Management Science, 46, 436-443.

[8] Datta, S. (2003) Radio frequency identification (RFID) made easy. MIT forum for supply chain innovation.

[9] Fine, C. H. (1998) Clockspeed: winning industry control in the age of temporary advantage, Reading, Mass., Perseus Books.

[10] Fleischmann, B. & Meyr, H. (2003) Planning Hierarchy, Modeling and Advance Planning Systems. IN Kok, A. G. D. & Graves, S. C. (Eds.) Supply chain management: design, coordination and operation. Elsevier.

[11] Gendreau, M., Guertin, F., Potvin, J. Y. & Seguin, R. (2006) Neighborhood search heuristics for a dynamic vehicle dispatching problem with pick-ups and deliveries. Transportation Research Part C-Emerging Technologies, 14, 157-174.

[12] Gendreau, M., Guertin, F., Potvin, J. Y. & Taillard, E. (1999) Parallel tabu search for real-time vehicle routing and dispatching. Transportation Science, 33, 381-390.

[13] Ghiani, G., Musmanno, R. & Laporte, G. (2004) Introduction to logistics systems planning and control, Chichester, West Sussex; Hoboken, NJ, USA, J. Wiley.

[14] Giesen, R. (2007) Online Inventory Replenishment and Fleet Routing Decisions Under Real-Time Information. Ph.D. Dissertation, University of Maryland, College Park.

[15] Giesen, R., Mahmassani, H. S. & Jaillet, P. (2005) Strategies for online inventory routing problem under real-time information. Transportation Research Record 1923, Network Modeling 2005, 164-179.

[16] Grötschel, M., Krumke, S. O. & Rambau, J. (2001a) Online Optimization of Complex Transportation Systemes. In Grötschel, M., Krumke, S. O. & Rambau, J. (Eds.) Online optimization of large scale systems. Berlin; New York, Springer.

[17] Grötshel, M., Krumke, S. O., Rambau, J., Winter, T. & Zimmermann, U. W. (2001b) Combinatorial Online Optimization in Real-Time. In Grötschel, M., Krumke, S. O. & Rambau, J. (Eds.) Online Optimization of Large Scale Systems. Berlin; New York, Springer.

[18] Ichoua, S., Gendreau, M. & Potvin, J. Y. (2006) Exploiting knowledge about future demands for real-time vehicle dispatching. Transportation Science, 40, 211-225.

[19] Kim, Y. (2003) Hybrid Approaches To Solve Dynamic Fleet Management Problems. Ph D dissertation, The University of Texas at Austin.

[20] Kim, Y., Mahmassani, H. S. & Jaillet, P. (2002) Dynamic truckload truck routing and scheduling in oversaturated demand situations. Transportation Network Modeling 2002, 66-71.

[21] Kim, Y. J., Mahmassani, H. S. & Jaillet, P. (2004) Dynamic truckload routing, scheduling, and load acceptance for large fleet operation with priority demands. Transportation Network Modeling 2004, 120-128.

[22] Kleywegt, A. J., Nori, V. S. & Savelsbergh, M. W. P. (2002) The Stochastic inventory routing problem with direct deliveries. Transportation Science, 36, 94-118.

[23] La Londe, B. J. (1994) Evolution of the integrated logistics concept. In Robeson, J. F., Copacino, W. C. & Howe, R. E. (Eds.) The Logistics Handbook. New York, The Free Press.

[24] Larsen, A., Madsen, O. & Solomon, M. (2002) Partially dynamic vehicle routing - models and algorithms. Journal of the Operational Research Society, 53, 637-646.

[25] Larsen, A., Madsen, O. B. G. & Solomon, M. M. (2004) The A priori dy namic traveling salesman problem with time windows.Transportation Science, 38, 459-472.

[26] Lee, H. L., Padmanbhan, V. & Whang, S. (1997) The bullwhip effect in supply chains. Sloan Management Review, 38, 93-102.

[27] Masters, J. M. & La Londe, B. J. (1994) The role of new information technology in the practice of traffic management. In Robeson, J. F., Copacino, W. C. & Howe, R. E. (Eds.) The Logistics Handbook. New York, The Free Press.

[28] Mitrovic-Minic, S., Krishnamurti, R. & Laporte, G. (2004) Double-horizon based heuristics for the dynamic pickup and delivery problem with time windows. Transportation Research Part B-Methodological, 38, 669-685.

[29] Rabah, M. & Mahmassani, H. S. (2002) Impact of information and communication technologies on logistics and freight transportation - Example of vendormanaged inventories. Freight Transportation 2002, 10-19.

[30] Regan, A. C., Mahmassani, H. S. & Jaillet, P. (1995) Improving the efficiency of commercial vehicle operations using real-time information: potential uses and assignment strategies. Transportation Research Record, 188-198.

[31] Regan, A. C., Mahmassani, H. S. & Jaillet, P. (1996) Dynamic decision making for commercial fleet operations using real-time information. Transportation Research Record, 91-97.

[32] Rutner, S. M., Gibson, B. J. & Williams, S. R. (2003) The impacts of the integrated logistics systems on electronic commerce and enterprise resource planning systems. Transportation Research Part E-Logistics and Transportation Review, 39, 83-93.

[33] Simchi-Levi, D., Kaminsky, P. & Simchi-Levi, E. (2003) Designing and managing the supply chain: concepts, strategies, and case studies, Boston, McGraw-Hill/Irwin.

[34] Thomas, D. J. & Griffin, P. M. (1996) Coordinated supply chain management. European Journal of Operational Research, 94, 1-15.

[35] Wolff, R. W. (1989) Stochastic modeling and the theory of queues, Englewood Cliffs, N.J., Prentice Hall.

[36] Yang, J., Jaillet, P. & Mahmassani, H. (2004) Real-time multivehicle truckload pickup and delivery problems. Transportation Science, 38, 135-148.

[37] Zheng, Y. S. & Federgruen, A. (1991) Finding Optimal (S, S) Policies Is About as Simple as Evaluating a Single Policy. Operations Research, 39, 654-665.

[38] Zipkin, P. H. (2000) Foundations of inventory management, Boston, McGraw-Hill.

## Appendix

Fig. 10. Simulation results: parameter set 1 $TC = 100   [\mathrm{S/hr}]$ $h_{i}=50[\mathrm{S/veck}]$ $\lambda _ { i }   =   5 0 [$ [arrivals/ day], $\theta _ { i }   =   1$ [units] for all i

<table><tr><td rowspan="2">Strategy</td><td rowspan="2"></td><td colspan="5">Case 0 (Symmetric case)</td></tr><tr><td>Inv. Holding Cost</td><td>Lost Sales Cost</td><td>Total Inv. Cost</td><td>Transp. Cost</td><td>Total Cost</td></tr><tr><td rowspan="3">BENCH1</td><td>Mean</td><td>22,569</td><td>2,041</td><td>24,610</td><td>3,428</td><td>28,038</td></tr><tr><td>St Dev</td><td>862</td><td>1,474</td><td>1,244</td><td>164</td><td>1,240</td></tr><tr><td>CV</td><td>0.04</td><td>0.72</td><td>0.05</td><td>0.05</td><td>0.04</td></tr><tr><td rowspan="3">MUN</td><td>Mean</td><td>12,843</td><td>1,901</td><td>14,744</td><td>6,415</td><td>21,159</td></tr><tr><td>St Dev</td><td>539</td><td>1,798</td><td>1,572</td><td>494</td><td>1,633</td></tr><tr><td>CV</td><td>0.04</td><td>0.95</td><td>0.11</td><td>0.08</td><td>0.08</td></tr><tr><td rowspan="3">RTC</td><td>Mean</td><td>16,221</td><td>167</td><td>16,388</td><td>4,621</td><td>21,008</td></tr><tr><td>St Dev</td><td>646</td><td>278</td><td>591</td><td>241</td><td>561</td></tr><tr><td>CV</td><td>0.04</td><td>1.67</td><td>0.04</td><td>0.05</td><td>0.03</td></tr><tr><td rowspan="3">RDE</td><td>Mean</td><td>13,997</td><td>312</td><td>14,308</td><td>4,943</td><td>19,252</td></tr><tr><td>St Dev</td><td>227</td><td>387</td><td>486</td><td>258</td><td>543</td></tr><tr><td>CV</td><td>0.02</td><td>1.24</td><td>0.03</td><td>0.05</td><td>0.03</td></tr><tr><td rowspan="3">RDE+div</td><td>Mean</td><td>14,158</td><td>228</td><td>14,386</td><td>4,980</td><td>19,366</td></tr><tr><td>St Dev</td><td>234</td><td>304</td><td>307</td><td>248</td><td>397</td></tr><tr><td>CV</td><td>0.02</td><td>1.33</td><td>0.02</td><td>0.05</td><td>0.02</td></tr><tr><td rowspan="2">Strategy</td><td rowspan="2"></td><td colspan="5">Case 1</td></tr><tr><td>Inv. Holding Cost</td><td>Lost Sales Cost</td><td>Total Inv. Cost</td><td>Transp. Cost</td><td>Total Cost</td></tr><tr><td rowspan="3">BENCH1</td><td>Mean</td><td>22,812</td><td>2,928</td><td>25,739</td><td>4,363</td><td>30,103</td></tr><tr><td>St Dev</td><td>841</td><td>2,302</td><td>1,852</td><td>432</td><td>1,963</td></tr><tr><td>CV</td><td>0.04</td><td>0.79</td><td>0.07</td><td>0.10</td><td>0.07</td></tr><tr><td rowspan="3">MUN</td><td>Mean</td><td>16,361</td><td>1,763</td><td>18,124</td><td>7,437</td><td>25,561</td></tr><tr><td>St Dev</td><td>725</td><td>1,672</td><td>1,393</td><td>545</td><td>1,541</td></tr><tr><td>CV</td><td>0.04</td><td>0.95</td><td>0.08</td><td>0.07</td><td>0.06</td></tr><tr><td rowspan="3">RTC</td><td>Mean</td><td>18,895</td><td>321</td><td>19,215</td><td>5,308</td><td>24,523</td></tr><tr><td>St Dev</td><td>703</td><td>498</td><td>886</td><td>330</td><td>911</td></tr><tr><td>CV</td><td>0.04</td><td>1.55</td><td>0.05</td><td>0.06</td><td>0.04</td></tr><tr><td rowspan="3">RDE</td><td>Mean</td><td>17,287</td><td>307</td><td>17,594</td><td>5,536</td><td>23,130</td></tr><tr><td>St Dev</td><td>316</td><td>410</td><td>498</td><td>317</td><td>602</td></tr><tr><td>CV</td><td>0.02</td><td>1.34</td><td>0.03</td><td>0.06</td><td>0.03</td></tr><tr><td rowspan="3">RDE+div</td><td>Mean</td><td>17,238</td><td>239</td><td>17,477</td><td>5,606</td><td>23,083</td></tr><tr><td>St Dev</td><td>327</td><td>271</td><td>417</td><td>354</td><td>592</td></tr><tr><td>CV</td><td>0.02</td><td>1.13</td><td>0.02</td><td>0.06</td><td>0.03</td></tr><tr><td rowspan="2">Strategy</td><td rowspan="2"></td><td colspan="5">Case 2</td></tr><tr><td>Inv. Holding Cost</td><td>Lost Sales Cost</td><td>Total Inv. Cost</td><td>Transp. Cost</td><td>Total Cost</td></tr><tr><td rowspan="3">BENCH1</td><td>Mean</td><td>22,721</td><td>1,432</td><td>24,153</td><td>3,041</td><td>27,194</td></tr><tr><td>St Dev</td><td>683</td><td>1,691</td><td>1,576</td><td>216</td><td>1,665</td></tr><tr><td>CV</td><td>0.03</td><td>1.18</td><td>0.07</td><td>0.07</td><td>0.06</td></tr><tr><td rowspan="3">MUN</td><td>Mean</td><td>12,725</td><td>612</td><td>13,337</td><td>7,366</td><td>20,703</td></tr><tr><td>St Dev</td><td>381</td><td>1,202</td><td>1,104</td><td>525</td><td>1,372</td></tr><tr><td>CV</td><td>0.03</td><td>1.97</td><td>0.08</td><td>0.07</td><td>0.07</td></tr><tr><td rowspan="3">RTC</td><td>Mean</td><td>14,903</td><td>660</td><td>15,563</td><td>4,367</td><td>19,930</td></tr><tr><td>St Dev</td><td>362</td><td>755</td><td>693</td><td>264</td><td>701</td></tr><tr><td>CV</td><td>0.02</td><td>1.14</td><td>0.04</td><td>0.06</td><td>0.04</td></tr><tr><td rowspan="3">RDE</td><td>Mean</td><td>12,647</td><td>680</td><td>13,327</td><td>4,922</td><td>18,249</td></tr><tr><td>St Dev</td><td>250</td><td>574</td><td>636</td><td>230</td><td>640</td></tr><tr><td>CV</td><td>0.02</td><td>0.84</td><td>0.05</td><td>0.05</td><td>0.04</td></tr><tr><td rowspan="3">RDE+div</td><td>Mean</td><td>12,658</td><td>443</td><td>13,101</td><td>4,919</td><td>18,019</td></tr><tr><td>St Dev</td><td>252</td><td>592</td><td>667</td><td>235</td><td>739</td></tr><tr><td>CV</td><td>0.02</td><td>1.34</td><td>0.05</td><td>0.05</td><td>0.04</td></tr><tr><td rowspan="2">Strategy</td><td rowspan="2"></td><td colspan="5">Case 3</td></tr><tr><td>Inv. Holding Cost</td><td>Lost Sales Cost</td><td>Total Inv. Cost</td><td>Transp. Cost</td><td>Total Cost</td></tr><tr><td rowspan="3">BENCH1</td><td>Mean</td><td>23,221</td><td>1,821</td><td>25,041</td><td>3,355</td><td>28,396</td></tr><tr><td>St Dev</td><td>901</td><td>1,620</td><td>1,410</td><td>279</td><td>1,488</td></tr><tr><td>CV</td><td>0.04</td><td>0.89</td><td>0.06</td><td>0.08</td><td>0.05</td></tr><tr><td rowspan="3">MUN</td><td>Mean</td><td>14,696</td><td>1,046</td><td>15,742</td><td>6,650</td><td>22,392</td></tr><tr><td>St Dev</td><td>616</td><td>1,234</td><td>981</td><td>555</td><td>1,244</td></tr><tr><td>CV</td><td>0.04</td><td>1.18</td><td>0.06</td><td>0.08</td><td>0.06</td></tr><tr><td rowspan="3">RTC</td><td>Mean</td><td>16,938</td><td>534</td><td>17,473</td><td>4,466</td><td>21,939</td></tr><tr><td>St Dev</td><td>528</td><td>667</td><td>855</td><td>282</td><td>851</td></tr><tr><td>CV</td><td>0.03</td><td>1.25</td><td>0.05</td><td>0.06</td><td>0.04</td></tr><tr><td rowspan="3">RDE</td><td>Mean</td><td>14,960</td><td>257</td><td>15,217</td><td>4,727</td><td>19,943</td></tr><tr><td>St Dev</td><td>337</td><td>576</td><td>535</td><td>222</td><td>627</td></tr><tr><td>CV</td><td>0.02</td><td>2.24</td><td>0.04</td><td>0.05</td><td>0.03</td></tr><tr><td rowspan="3">RDE+div</td><td>Mean</td><td>15,020</td><td>212</td><td>15,232</td><td>4,805</td><td>20,037</td></tr><tr><td>St Dev</td><td>308</td><td>326</td><td>410</td><td>198</td><td>478</td></tr><tr><td>CV</td><td>0.02</td><td>1.54</td><td>0.03</td><td>0.04</td><td>0.02</td></tr></table>

30 replication with common random numbers

Results in [\$/week]

Fig. 11. Simulation results: parameter set 2 $\mathrm{TC}=33[\mathrm{S}/\mathrm{hr}]$ $h _ { i }   =   5 0$ [\$/week], $\lambda _ { i }   =   5 0$ [arrivals/day], $\theta _ { i }   =   1$ [units] for all i

<table><tr><td rowspan="2">Strategy</td><td rowspan="2"></td><td colspan="5">Case 0 (Symmetric case)</td></tr><tr><td>Inv. Holding Cost</td><td>Lost Sales Cost</td><td>Total Inv. Cost</td><td>Transp. Cost</td><td>Total Cost</td></tr><tr><td rowspan="3">BENCH1</td><td>Mean</td><td>21,344</td><td>181</td><td>21,525</td><td>1,408</td><td>22,932</td></tr><tr><td>St Dev</td><td>461</td><td>502</td><td>544</td><td>38</td><td>536</td></tr><tr><td>CV</td><td>0.02</td><td>2.78</td><td>0.03</td><td>0.03</td><td>0.02</td></tr><tr><td rowspan="3">MUN</td><td>Mean</td><td>11,904</td><td>1,748</td><td>13,651</td><td>2,476</td><td>16,128</td></tr><tr><td>St Dev</td><td>489</td><td>1,579</td><td>1,290</td><td>186</td><td>1,278</td></tr><tr><td>CV</td><td>0.04</td><td>0.90</td><td>0.09</td><td>0.08</td><td>0.08</td></tr><tr><td rowspan="3">RTC</td><td>Mean</td><td>14,906</td><td>315</td><td>15,220</td><td>1,689</td><td>16,910</td></tr><tr><td>St Dev</td><td>477</td><td>670</td><td>775</td><td>72</td><td>770</td></tr><tr><td>CV</td><td>0.03</td><td>2.13</td><td>0.05</td><td>0.04</td><td>0.05</td></tr><tr><td rowspan="3">RDE</td><td>Mean</td><td>12,649</td><td>187</td><td>12,837</td><td>1,890</td><td>14,727</td></tr><tr><td>St Dev</td><td>231</td><td>282</td><td>281</td><td>72</td><td>301</td></tr><tr><td>CV</td><td>0.02</td><td>1.50</td><td>0.02</td><td>0.04</td><td>0.02</td></tr><tr><td rowspan="3">RDE+div</td><td>Mean</td><td>12,635</td><td>236</td><td>12,871</td><td>1,901</td><td>14,772</td></tr><tr><td>St Dev</td><td>248</td><td>313</td><td>312</td><td>84</td><td>293</td></tr><tr><td>CV</td><td>0.02</td><td>1.33</td><td>0.02</td><td>0.04</td><td>0.02</td></tr><tr><td rowspan="2">Strategy</td><td rowspan="2"></td><td colspan="5">Case 1</td></tr><tr><td>Inv. Holding Cost</td><td>Lost Sales Cost</td><td>Total Inv. Cost</td><td>Transp. Cost</td><td>Total Cost</td></tr><tr><td rowspan="3">BENCH1</td><td>Mean</td><td>20,641</td><td>1,886</td><td>22,527</td><td>1,920</td><td>24,447</td></tr><tr><td>St Dev</td><td>699</td><td>1,950</td><td>1,512</td><td>72</td><td>1,535</td></tr><tr><td>CV</td><td>0.03</td><td>1.03</td><td>0.07</td><td>0.04</td><td>0.06</td></tr><tr><td rowspan="3">MUN</td><td>Mean</td><td>15,338</td><td>2,274</td><td>17,612</td><td>2,632</td><td>20,244</td></tr><tr><td>St Dev</td><td>802</td><td>2,434</td><td>2,076</td><td>189</td><td>2,081</td></tr><tr><td>CV</td><td>0.05</td><td>1.07</td><td>0.12</td><td>0.07</td><td>0.10</td></tr><tr><td rowspan="3">RTC</td><td>Mean</td><td>17,971</td><td>432</td><td>18,402</td><td>1,873</td><td>20,275</td></tr><tr><td>St Dev</td><td>703</td><td>801</td><td>869</td><td>119</td><td>891</td></tr><tr><td>CV</td><td>0.04</td><td>1.86</td><td>0.05</td><td>0.06</td><td>0.04</td></tr><tr><td rowspan="3">RDE</td><td>Mean</td><td>16,246</td><td>282</td><td>16,527</td><td>1,980</td><td>18,507</td></tr><tr><td>St Dev</td><td>313</td><td>330</td><td>412</td><td>124</td><td>399</td></tr><tr><td>CV</td><td>0.02</td><td>1.17</td><td>0.02</td><td>0.06</td><td>0.02</td></tr><tr><td rowspan="3">RDE+div</td><td>Mean</td><td>16,212</td><td>243</td><td>16,455</td><td>1,987</td><td>18,442</td></tr><tr><td>St Dev</td><td>297</td><td>367</td><td>415</td><td>91</td><td>403</td></tr><tr><td>CV</td><td>0.02</td><td>1.51</td><td>0.03</td><td>0.05</td><td>0.02</td></tr><tr><td rowspan="2">Strategy</td><td rowspan="2"></td><td colspan="5">Case 2</td></tr><tr><td>Inv. Holding Cost</td><td>Lost Sales Cost</td><td>Total Inv. Cost</td><td>Transp. Cost</td><td>Total Cost</td></tr><tr><td rowspan="3">BENCH1</td><td>Mean</td><td>20,559</td><td>787</td><td>21,345</td><td>1,300</td><td>22,646</td></tr><tr><td>St Dev</td><td>418</td><td>859</td><td>835</td><td>55</td><td>848</td></tr><tr><td>CV</td><td>0.02</td><td>1.09</td><td>0.04</td><td>0.04</td><td>0.04</td></tr><tr><td rowspan="3">MUN</td><td>Mean</td><td>11,087</td><td>985</td><td>12,072</td><td>2,576</td><td>14,648</td></tr><tr><td>St Dev</td><td>405</td><td>1,006</td><td>873</td><td>177</td><td>864</td></tr><tr><td>CV</td><td>0.04</td><td>1.02</td><td>0.07</td><td>0.07</td><td>0.06</td></tr><tr><td rowspan="3">RTC</td><td>Mean</td><td>13,720</td><td>490</td><td>14,210</td><td>1,635</td><td>15,845</td></tr><tr><td>St Dev</td><td>348</td><td>632</td><td>671</td><td>81</td><td>707</td></tr><tr><td>CV</td><td>0.03</td><td>1.29</td><td>0.05</td><td>0.05</td><td>0.04</td></tr><tr><td rowspan="3">RDE</td><td>Mean</td><td>11,243</td><td>518</td><td>11,761</td><td>1,903</td><td>13,664</td></tr><tr><td>St Dev</td><td>203</td><td>611</td><td>619</td><td>81</td><td>639</td></tr><tr><td>CV</td><td>0.02</td><td>1.18</td><td>0.05</td><td>0.04</td><td>0.05</td></tr><tr><td rowspan="3">RDE+div</td><td>Mean</td><td>11,275</td><td>386</td><td>11,661</td><td>1,952</td><td>13,613</td></tr><tr><td>St Dev</td><td>193</td><td>411</td><td>439</td><td>109</td><td>452</td></tr><tr><td>CV</td><td>0.02</td><td>1.07</td><td>0.04</td><td>0.06</td><td>0.03</td></tr><tr><td rowspan="2">Strategy</td><td rowspan="2"></td><td colspan="5">Case 3</td></tr><tr><td>Inv. Holding Cost</td><td>Lost Sales Cost</td><td>Total Inv. Cost</td><td>Transp. Cost</td><td>Total Cost</td></tr><tr><td rowspan="3">BENCH1</td><td>Mean</td><td>21,317</td><td>493</td><td>21,811</td><td>1,389</td><td>23,199</td></tr><tr><td>St Dev</td><td>482</td><td>745</td><td>843</td><td>43</td><td>842</td></tr><tr><td>CV</td><td>0.02</td><td>1.51</td><td>0.04</td><td>0.03</td><td>0.04</td></tr><tr><td rowspan="3">MUN</td><td>Mean</td><td>13,287</td><td>909</td><td>14,195</td><td>2,316</td><td>16,511</td></tr><tr><td>St Dev</td><td>504</td><td>1,452</td><td>1,146</td><td>181</td><td>1,151</td></tr><tr><td>CV</td><td>0.04</td><td>1.60</td><td>0.08</td><td>0.08</td><td>0.07</td></tr><tr><td rowspan="3">RTC</td><td>Mean</td><td>15,735</td><td>247</td><td>15,981</td><td>1,604</td><td>17,585</td></tr><tr><td>St Dev</td><td>464</td><td>480</td><td>666</td><td>72</td><td>697</td></tr><tr><td>CV</td><td>0.03</td><td>1.95</td><td>0.04</td><td>0.04</td><td>0.04</td></tr><tr><td rowspan="3">RDE</td><td>Mean</td><td>13,682</td><td>363</td><td>14,045</td><td>1,751</td><td>15,795</td></tr><tr><td>St Dev</td><td>209</td><td>501</td><td>516</td><td>75</td><td>512</td></tr><tr><td>CV</td><td>0.02</td><td>1.38</td><td>0.04</td><td>0.04</td><td>0.03</td></tr><tr><td rowspan="3">RDE+div</td><td>Mean</td><td>13,766</td><td>238</td><td>14,004</td><td>1,790</td><td>15,794</td></tr><tr><td>St Dev</td><td>205</td><td>374</td><td>410</td><td>90</td><td>426</td></tr><tr><td>CV</td><td>0.01</td><td>1.57</td><td>0.03</td><td>0.05</td><td>0.03</td></tr></table>

Results in [\$/week]

30 replication with common random numbers

Fig. 12. Simulation results: parameter Set 3 TC = 300 [\$/hr], $h_{i}=50[\mathrm{S/veck}]$ $\lambda _ { i }   =   5 0$ [arrivals/day], $\theta _ { i }   =   1$ [units] for all i

<table><tr><td rowspan="2">Strategy</td><td rowspan="2"></td><td colspan="5">Case 0 (Symmetric case)</td></tr><tr><td>Inv. Holding Cost</td><td>Lost Sales Cost</td><td>Total Inv. Cost</td><td>Transp. Cost</td><td>Total Cost</td></tr><tr><td rowspan="3">BENCH1</td><td>Mean</td><td>29,895</td><td>488</td><td>30,383</td><td>8,441</td><td>38,825</td></tr><tr><td>St Dev</td><td>642</td><td>731</td><td>761</td><td>688</td><td>1,156</td></tr><tr><td>CV</td><td>0.02</td><td>1.50</td><td>0.03</td><td>0.08</td><td>0.03</td></tr><tr><td rowspan="3">MUN</td><td>Mean</td><td>19,248</td><td>829</td><td>20,077</td><td>15,671</td><td>35,748</td></tr><tr><td>St Dev</td><td>707</td><td>1,386</td><td>1,114</td><td>1,459</td><td>2,103</td></tr><tr><td>CV</td><td>0.04</td><td>1.67</td><td>0.06</td><td>0.09</td><td>0.06</td></tr><tr><td rowspan="3">RTC</td><td>Mean</td><td>20,780</td><td>368</td><td>21,147</td><td>9,666</td><td>30,814</td></tr><tr><td>St Dev</td><td>628</td><td>577</td><td>743</td><td>749</td><td>1,050</td></tr><tr><td>CV</td><td>0.03</td><td>1.57</td><td>0.04</td><td>0.08</td><td>0.03</td></tr><tr><td rowspan="3">RDE</td><td>Mean</td><td>19,086</td><td>448</td><td>19,534</td><td>10,027</td><td>29,562</td></tr><tr><td>St Dev</td><td>470</td><td>547</td><td>517</td><td>682</td><td>931</td></tr><tr><td>CV</td><td>0.02</td><td>1.22</td><td>0.03</td><td>0.07</td><td>0.03</td></tr><tr><td rowspan="3">RDE+div</td><td>Mean</td><td>19,167</td><td>452</td><td>19,619</td><td>10,063</td><td>29,682</td></tr><tr><td>St Dev</td><td>437</td><td>483</td><td>538</td><td>709</td><td>914</td></tr><tr><td>CV</td><td>0.02</td><td>1.07</td><td>0.03</td><td>0.07</td><td>0.03</td></tr><tr><td rowspan="2">Strategy</td><td rowspan="2"></td><td colspan="5">Case 1</td></tr><tr><td>Inv. Holding Cost</td><td>Lost Sales Cost</td><td>Total Inv. Cost</td><td>Transp. Cost</td><td>Total Cost</td></tr><tr><td rowspan="3">BENCH1</td><td>Mean</td><td>30,680</td><td>1,703</td><td>32,383</td><td>10,581</td><td>42,965</td></tr><tr><td>St Dev</td><td>980</td><td>1,742</td><td>1,813</td><td>845</td><td>2,226</td></tr><tr><td>CV</td><td>0.03</td><td>1.02</td><td>0.06</td><td>0.08</td><td>0.05</td></tr><tr><td rowspan="3">MUN</td><td>Mean</td><td>21,104</td><td>1,529</td><td>22,633</td><td>16,244</td><td>38,877</td></tr><tr><td>St Dev</td><td>1,063</td><td>1,710</td><td>1,426</td><td>1,885</td><td>2,254</td></tr><tr><td>CV</td><td>0.05</td><td>1.12</td><td>0.06</td><td>0.12</td><td>0.06</td></tr><tr><td rowspan="3">RTC</td><td>Mean</td><td>24,095</td><td>609</td><td>24,705</td><td>11,183</td><td>35,888</td></tr><tr><td>St Dev</td><td>874</td><td>934</td><td>1,132</td><td>897</td><td>1,555</td></tr><tr><td>CV</td><td>0.04</td><td>1.53</td><td>0.05</td><td>0.08</td><td>0.04</td></tr><tr><td rowspan="3">RDE</td><td>Mean</td><td>22,833</td><td>529</td><td>23,362</td><td>11,523</td><td>34,886</td></tr><tr><td>St Dev</td><td>536</td><td>624</td><td>800</td><td>1,062</td><td>1,364</td></tr><tr><td>CV</td><td>0.02</td><td>1.18</td><td>0.03</td><td>0.09</td><td>0.04</td></tr><tr><td rowspan="3">RDE+div</td><td>Mean</td><td>22,800</td><td>505</td><td>23,305</td><td>11,578</td><td>34,883</td></tr><tr><td>St Dev</td><td>738</td><td>682</td><td>966</td><td>1,012</td><td>1,448</td></tr><tr><td>CV</td><td>0.03</td><td>1.35</td><td>0.04</td><td>0.09</td><td>0.04</td></tr><tr><td rowspan="2">Strategy</td><td rowspan="2"></td><td colspan="5">Case 2</td></tr><tr><td>Inv. Holding Cost</td><td>Lost Sales Cost</td><td>Total Inv. Cost</td><td>Transp. Cost</td><td>Total Cost</td></tr><tr><td rowspan="3">BENCH1</td><td>Mean</td><td>28,522</td><td>727</td><td>29,250</td><td>7,470</td><td>36,719</td></tr><tr><td>St Dev</td><td>661</td><td>1,167</td><td>1,231</td><td>716</td><td>1,562</td></tr><tr><td>CV</td><td>0.02</td><td>1.60</td><td>0.04</td><td>0.10</td><td>0.04</td></tr><tr><td rowspan="3">MUN</td><td>Mean</td><td>16,594</td><td>4,798</td><td>21,393</td><td>15,627</td><td>37,020</td></tr><tr><td>St Dev</td><td>781</td><td>3,346</td><td>2,759</td><td>2,391</td><td>2,722</td></tr><tr><td>CV</td><td>0.05</td><td>0.70</td><td>0.13</td><td>0.15</td><td>0.07</td></tr><tr><td rowspan="3">RTC</td><td>Mean</td><td>19,246</td><td>771</td><td>20,017</td><td>8,978</td><td>28,995</td></tr><tr><td>St Dev</td><td>655</td><td>1,172</td><td>1,023</td><td>796</td><td>1,247</td></tr><tr><td>CV</td><td>0.03</td><td>1.52</td><td>0.05</td><td>0.09</td><td>0.04</td></tr><tr><td rowspan="3">RDE</td><td>Mean</td><td>17,627</td><td>553</td><td>18,180</td><td>9,578</td><td>27,758</td></tr><tr><td>St Dev</td><td>428</td><td>765</td><td>888</td><td>819</td><td>1,218</td></tr><tr><td>CV</td><td>0.02</td><td>1.38</td><td>0.05</td><td>0.09</td><td>0.04</td></tr><tr><td rowspan="3">RDE+div</td><td>Mean</td><td>17,561</td><td>469</td><td>18,031</td><td>9,566</td><td>27,597</td></tr><tr><td>St Dev</td><td>460</td><td>417</td><td>537</td><td>663</td><td>869</td></tr><tr><td>CV</td><td>0.03</td><td>0.89</td><td>0.03</td><td>0.07</td><td>0.03</td></tr><tr><td rowspan="2">Strategy</td><td rowspan="2"></td><td colspan="5">Case 3</td></tr><tr><td>Inv. Holding Cost</td><td>Lost Sales Cost</td><td>Total Inv. Cost</td><td>Transp. Cost</td><td>Total Cost</td></tr><tr><td rowspan="3">BENCH1</td><td>Mean</td><td>29,530</td><td>1,009</td><td>30,539</td><td>8,368</td><td>38,907</td></tr><tr><td>St Dev</td><td>905</td><td>1,053</td><td>1,118</td><td>745</td><td>1,399</td></tr><tr><td>CV</td><td>0.03</td><td>1.04</td><td>0.04</td><td>0.09</td><td>0.04</td></tr><tr><td rowspan="3">MUN</td><td>Mean</td><td>20,035</td><td>449</td><td>20,484</td><td>14,654</td><td>35,138</td></tr><tr><td>St Dev</td><td>818</td><td>555</td><td>949</td><td>1,645</td><td>2,134</td></tr><tr><td>CV</td><td>0.04</td><td>1.24</td><td>0.05</td><td>0.11</td><td>0.06</td></tr><tr><td rowspan="3">RTC</td><td>Mean</td><td>22,267</td><td>372</td><td>22,639</td><td>9,184</td><td>31,823</td></tr><tr><td>St Dev</td><td>636</td><td>444</td><td>689</td><td>821</td><td>1,207</td></tr><tr><td>CV</td><td>0.03</td><td>1.19</td><td>0.03</td><td>0.09</td><td>0.04</td></tr><tr><td rowspan="3">RDE</td><td>Mean</td><td>20,555</td><td>561</td><td>21,116</td><td>9,563</td><td>30,678</td></tr><tr><td>St Dev</td><td>416</td><td>806</td><td>822</td><td>832</td><td>1,286</td></tr><tr><td>CV</td><td>0.02</td><td>1.44</td><td>0.04</td><td>0.09</td><td>0.04</td></tr><tr><td rowspan="3">RDE+div</td><td>Mean</td><td>20,594</td><td>573</td><td>21,167</td><td>9,585</td><td>30,751</td></tr><tr><td>St Dev</td><td>533</td><td>592</td><td>673</td><td>803</td><td>1,089</td></tr><tr><td>CV</td><td>0.03</td><td>1.03</td><td>0.03</td><td>0.08</td><td>0.04</td></tr></table>

Results in [\$/week]

30 replication with common random numbers

Fig. 13. Simulation results: parameter set 4 TC = 100 [\$/hr], $h_{i}=50[\mathrm{S/veck}]$ $\lambda _ { i }   =   1 0 . 5$ [arrivals/day], $\theta _ { i }   =   4 . 8$ [units] for all i

<table><tr><td rowspan="2">Strategy</td><td rowspan="2"></td><td colspan="5">Case 0 (Symmetric case)</td></tr><tr><td>Inv. Holding Cost</td><td>Lost Sales Cost</td><td>Total Inv. Cost</td><td>Transp. Cost</td><td>Total Cost</td></tr><tr><td rowspan="3">BENCH1</td><td>Mean</td><td>26,668</td><td>1,924</td><td>28,592</td><td>3,293</td><td>31,885</td></tr><tr><td>St Dev</td><td>833</td><td>1,779</td><td>1,870</td><td>238</td><td>1,922</td></tr><tr><td>CV</td><td>0.03</td><td>0.92</td><td>0.07</td><td>0.07</td><td>0.06</td></tr><tr><td rowspan="3">MUN</td><td>Mean</td><td>16,535</td><td>923</td><td>17,458</td><td>6,903</td><td>24,360</td></tr><tr><td>St Dev</td><td>531</td><td>996</td><td>1,118</td><td>514</td><td>1,339</td></tr><tr><td>CV</td><td>0.03</td><td>1.08</td><td>0.06</td><td>0.07</td><td>0.05</td></tr><tr><td rowspan="3">RTC</td><td>Mean</td><td>20,424</td><td>863</td><td>21,287</td><td>4,757</td><td>26,044</td></tr><tr><td>St Dev</td><td>636</td><td>989</td><td>1,109</td><td>331</td><td>1,169</td></tr><tr><td>CV</td><td>0.03</td><td>1.15</td><td>0.05</td><td>0.07</td><td>0.04</td></tr><tr><td rowspan="3">RDE</td><td>Mean</td><td>17,050</td><td>1,018</td><td>18,068</td><td>5,197</td><td>23,265</td></tr><tr><td>St Dev</td><td>355</td><td>855</td><td>798</td><td>303</td><td>820</td></tr><tr><td>CV</td><td>0.02</td><td>0.84</td><td>0.04</td><td>0.06</td><td>0.04</td></tr><tr><td rowspan="3">RDE+div</td><td>Mean</td><td>16,934</td><td>727</td><td>17,660</td><td>5,326</td><td>22,987</td></tr><tr><td>St Dev</td><td>436</td><td>804</td><td>769</td><td>333</td><td>831</td></tr><tr><td>CV</td><td>0.03</td><td>1.11</td><td>0.04</td><td>0.06</td><td>0.04</td></tr><tr><td rowspan="2">Strategy</td><td rowspan="2"></td><td colspan="5">Case 1</td></tr><tr><td>Inv. Holding Cost</td><td>Lost Sales Cost</td><td>Total Inv. Cost</td><td>Transp. Cost</td><td>Total Cost</td></tr><tr><td rowspan="3">BENCH1</td><td>Mean</td><td>26,615</td><td>2,797</td><td>29,412</td><td>4,326</td><td>33,738</td></tr><tr><td>St Dev</td><td>1,055</td><td>2,524</td><td>2,131</td><td>401</td><td>2,200</td></tr><tr><td>CV</td><td>0.04</td><td>0.90</td><td>0.07</td><td>0.09</td><td>0.07</td></tr><tr><td rowspan="3">MUN</td><td>Mean</td><td>19,530</td><td>1,282</td><td>20,812</td><td>7,222</td><td>28,034</td></tr><tr><td>St Dev</td><td>957</td><td>1,953</td><td>1,806</td><td>543</td><td>1,972</td></tr><tr><td>CV</td><td>0.05</td><td>1.52</td><td>0.09</td><td>0.08</td><td>0.07</td></tr><tr><td rowspan="3">RTC</td><td>Mean</td><td>23,530</td><td>524</td><td>24,054</td><td>5,388</td><td>29,442</td></tr><tr><td>St Dev</td><td>908</td><td>839</td><td>1,185</td><td>317</td><td>1,225</td></tr><tr><td>CV</td><td>0.04</td><td>1.60</td><td>0.05</td><td>0.06</td><td>0.04</td></tr><tr><td rowspan="3">RDE</td><td>Mean</td><td>20,716</td><td>649</td><td>21,365</td><td>5,867</td><td>27,231</td></tr><tr><td>St Dev</td><td>430</td><td>690</td><td>701</td><td>480</td><td>882</td></tr><tr><td>CV</td><td>0.02</td><td>1.06</td><td>0.03</td><td>0.08</td><td>0.03</td></tr><tr><td rowspan="3">RDE+div</td><td>Mean</td><td>20,810</td><td>307</td><td>21,118</td><td>5,872</td><td>26,990</td></tr><tr><td>St Dev</td><td>428</td><td>555</td><td>611</td><td>431</td><td>686</td></tr><tr><td>CV</td><td>0.02</td><td>1.81</td><td>0.03</td><td>0.07</td><td>0.03</td></tr><tr><td rowspan="2">Strategy</td><td rowspan="2"></td><td colspan="5">Case 2</td></tr><tr><td>Inv. Holding Cost</td><td>Lost Sales Cost</td><td>Total Inv. Cost</td><td>Transp. Cost</td><td>Total Cost</td></tr><tr><td rowspan="3">BENCH1</td><td>Mean</td><td>26,427</td><td>1,817</td><td>28,244</td><td>2,953</td><td>31,196</td></tr><tr><td>St Dev</td><td>1,117</td><td>1,751</td><td>1,602</td><td>254</td><td>1,662</td></tr><tr><td>CV</td><td>0.04</td><td>0.96</td><td>0.06</td><td>0.09</td><td>0.05</td></tr><tr><td rowspan="3">MUN</td><td>Mean</td><td>15,341</td><td>1,651</td><td>16,992</td><td>7,352</td><td>24,343</td></tr><tr><td>St Dev</td><td>540</td><td>1,621</td><td>1,570</td><td>563</td><td>1,590</td></tr><tr><td>CV</td><td>0.04</td><td>0.98</td><td>0.09</td><td>0.08</td><td>0.07</td></tr><tr><td rowspan="3">RTC</td><td>Mean</td><td>19,364</td><td>545</td><td>19,909</td><td>4,340</td><td>24,249</td></tr><tr><td>St Dev</td><td>751</td><td>596</td><td>982</td><td>287</td><td>989</td></tr><tr><td>CV</td><td>0.04</td><td>1.09</td><td>0.05</td><td>0.07</td><td>0.04</td></tr><tr><td rowspan="3">RDE</td><td>Mean</td><td>15,385</td><td>699</td><td>16,084</td><td>4,976</td><td>21,060</td></tr><tr><td>St Dev</td><td>273</td><td>641</td><td>617</td><td>311</td><td>673</td></tr><tr><td>CV</td><td>0.02</td><td>0.92</td><td>0.04</td><td>0.06</td><td>0.03</td></tr><tr><td rowspan="3">RDE+div</td><td>Mean</td><td>15,458</td><td>812</td><td>16,270</td><td>5,125</td><td>21,395</td></tr><tr><td>St Dev</td><td>269</td><td>784</td><td>806</td><td>310</td><td>817</td></tr><tr><td>CV</td><td>0.02</td><td>0.96</td><td>0.05</td><td>0.06</td><td>0.04</td></tr><tr><td rowspan="2">Strategy</td><td rowspan="2"></td><td colspan="5">Case 3</td></tr><tr><td>Inv. Holding Cost</td><td>Lost Sales Cost</td><td>Total Inv. Cost</td><td>Transp. Cost</td><td>Total Cost</td></tr><tr><td rowspan="3">BENCH1</td><td>Mean</td><td>27,080</td><td>2,313</td><td>29,393</td><td>3,318</td><td>32,711</td></tr><tr><td>St Dev</td><td>849</td><td>2,482</td><td>2,267</td><td>255</td><td>2,309</td></tr><tr><td>CV</td><td>0.03</td><td>1.07</td><td>0.08</td><td>0.08</td><td>0.07</td></tr><tr><td rowspan="3">MUN</td><td>Mean</td><td>17,761</td><td>860</td><td>18,621</td><td>6,730</td><td>25,351</td></tr><tr><td>St Dev</td><td>682</td><td>965</td><td>1,089</td><td>550</td><td>1,238</td></tr><tr><td>CV</td><td>0.04</td><td>1.12</td><td>0.06</td><td>0.08</td><td>0.05</td></tr><tr><td rowspan="3">RTC</td><td>Mean</td><td>21,753</td><td>1,165</td><td>22,918</td><td>4,513</td><td>27,431</td></tr><tr><td>St Dev</td><td>943</td><td>1,582</td><td>1,557</td><td>294</td><td>1,565</td></tr><tr><td>CV</td><td>0.04</td><td>1.36</td><td>0.07</td><td>0.07</td><td>0.06</td></tr><tr><td rowspan="3">RDE</td><td>Mean</td><td>18,207</td><td>911</td><td>19,118</td><td>4,893</td><td>24,011</td></tr><tr><td>St Dev</td><td>439</td><td>1,205</td><td>1,020</td><td>305</td><td>1,031</td></tr><tr><td>CV</td><td>0.02</td><td>1.32</td><td>0.05</td><td>0.06</td><td>0.04</td></tr><tr><td rowspan="3">RDE+div</td><td>Mean</td><td>18,213</td><td>578</td><td>18,791</td><td>4,949</td><td>23,740</td></tr><tr><td>St Dev</td><td>510</td><td>672</td><td>627</td><td>322</td><td>764</td></tr><tr><td>CV</td><td>0.03</td><td>1.16</td><td>0.03</td><td>0.07</td><td>0.03</td></tr></table>

Results in [\$/week]

30 replication with common random numbers

Fig. 14. Simulation results: parameter set $5\  TC =100\ [\ \mathrm{S/hr}]$ $h_{i}=50[\mathrm{S/veck}]$ $\lambda _ { i }   =   4 . 3 5$ [arrivals/day], $\theta _ { i }   =   1 1 . 5$ [units] for all i

<table><tr><td rowspan="2">Strategy</td><td rowspan="2"></td><td colspan="5">Case 0 (Symmetric case)</td></tr><tr><td>Inv. Holding Cost</td><td>Lost Sales Cost</td><td>Total Inv. Cost</td><td>Transp. Cost</td><td>Total Cost</td></tr><tr><td rowspan="3">BENCH1</td><td>Mean</td><td>30,862</td><td>2,273</td><td>33,135</td><td>3,105</td><td>36,241</td></tr><tr><td>St Dev</td><td>1,292</td><td>2,761</td><td>2,590</td><td>243</td><td>2,615</td></tr><tr><td>CV</td><td>0.04</td><td>1.21</td><td>0.08</td><td>0.08</td><td>0.07</td></tr><tr><td rowspan="3">MUN</td><td>Mean</td><td>19,999</td><td>1,509</td><td>21,508</td><td>7,251</td><td>28,759</td></tr><tr><td>St Dev</td><td>1,043</td><td>1,693</td><td>1,803</td><td>598</td><td>2,105</td></tr><tr><td>CV</td><td>0.05</td><td>1.12</td><td>0.08</td><td>0.08</td><td>0.07</td></tr><tr><td rowspan="3">RTC</td><td>Mean</td><td>25,127</td><td>2,488</td><td>27,615</td><td>4,981</td><td>32,596</td></tr><tr><td>St Dev</td><td>989</td><td>2,867</td><td>2,857</td><td>437</td><td>2,860</td></tr><tr><td>CV</td><td>0.04</td><td>1.15</td><td>0.10</td><td>0.09</td><td>0.09</td></tr><tr><td rowspan="3">RDE</td><td>Mean</td><td>19,988</td><td>1,895</td><td>21,883</td><td>5,358</td><td>27,241</td></tr><tr><td>St Dev</td><td>419</td><td>1,540</td><td>1,473</td><td>436</td><td>1,615</td></tr><tr><td>CV</td><td>0.02</td><td>0.81</td><td>0.07</td><td>0.08</td><td>0.06</td></tr><tr><td rowspan="3">RDE+div</td><td>Mean</td><td>20,272</td><td>1,383</td><td>21,654</td><td>5,558</td><td>27,212</td></tr><tr><td>St Dev</td><td>485</td><td>1,386</td><td>1,370</td><td>381</td><td>1,499</td></tr><tr><td>CV</td><td>0.02</td><td>1.00</td><td>0.06</td><td>0.07</td><td>0.06</td></tr><tr><td rowspan="2">Strategy</td><td rowspan="2"></td><td colspan="5">Case 1</td></tr><tr><td>Inv. Holding Cost</td><td>Lost Sales Cost</td><td>Total Inv. Cost</td><td>Transp. Cost</td><td>Total Cost</td></tr><tr><td rowspan="3">BENCH1</td><td>Mean</td><td>30,842</td><td>4,103</td><td>34,945</td><td>4,083</td><td>39,028</td></tr><tr><td>St Dev</td><td>1,354</td><td>4,971</td><td>4,560</td><td>375</td><td>4,586</td></tr><tr><td>CV</td><td>0.04</td><td>1.21</td><td>0.13</td><td>0.09</td><td>0.12</td></tr><tr><td rowspan="3">MUN</td><td>Mean</td><td>23,346</td><td>1,259</td><td>24,606</td><td>7,219</td><td>31,825</td></tr><tr><td>St Dev</td><td>1,117</td><td>1,514</td><td>1,478</td><td>853</td><td>2,139</td></tr><tr><td>CV</td><td>0.05</td><td>1.20</td><td>0.06</td><td>0.12</td><td>0.07</td></tr><tr><td rowspan="3">RTC</td><td>Mean</td><td>28,961</td><td>1,647</td><td>30,607</td><td>5,616</td><td>36,223</td></tr><tr><td>St Dev</td><td>1,605</td><td>1,640</td><td>2,242</td><td>472</td><td>2,197</td></tr><tr><td>CV</td><td>0.06</td><td>1.00</td><td>0.07</td><td>0.08</td><td>0.06</td></tr><tr><td rowspan="3">RDE</td><td>Mean</td><td>24,254</td><td>1,248</td><td>25,502</td><td>6,386</td><td>31,888</td></tr><tr><td>St Dev</td><td>637</td><td>1,519</td><td>1,367</td><td>571</td><td>1,487</td></tr><tr><td>CV</td><td>0.03</td><td>1.22</td><td>0.05</td><td>0.09</td><td>0.05</td></tr><tr><td rowspan="3">RDE+div</td><td>Mean</td><td>24,592</td><td>959</td><td>25,551</td><td>6,327</td><td>31,878</td></tr><tr><td>St Dev</td><td>709</td><td>1,350</td><td>1,375</td><td>584</td><td>1,455</td></tr><tr><td>CV</td><td>0.03</td><td>1.41</td><td>0.05</td><td>0.09</td><td>0.05</td></tr><tr><td rowspan="2">Strategy</td><td rowspan="2"></td><td colspan="5">Case 2</td></tr><tr><td>Inv. Holding Cost</td><td>Lost Sales Cost</td><td>Total Inv. Cost</td><td>Transp. Cost</td><td>Total Cost</td></tr><tr><td rowspan="3">BENCH1</td><td>Mean</td><td>30,787</td><td>2,473</td><td>33,260</td><td>2,919</td><td>36,179</td></tr><tr><td>St Dev</td><td>1,061</td><td>2,254</td><td>2,035</td><td>274</td><td>2,165</td></tr><tr><td>CV</td><td>0.03</td><td>0.91</td><td>0.06</td><td>0.09</td><td>0.06</td></tr><tr><td rowspan="3">MUN</td><td>Mean</td><td>18,397</td><td>2,570</td><td>20,967</td><td>7,416</td><td>28,384</td></tr><tr><td>St Dev</td><td>599</td><td>2,245</td><td>2,082</td><td>770</td><td>2,188</td></tr><tr><td>CV</td><td>0.03</td><td>0.87</td><td>0.10</td><td>0.10</td><td>0.08</td></tr><tr><td rowspan="3">RTC</td><td>Mean</td><td>24,345</td><td>1,885</td><td>26,229</td><td>4,363</td><td>30,593</td></tr><tr><td>St Dev</td><td>963</td><td>2,152</td><td>2,193</td><td>482</td><td>2,229</td></tr><tr><td>CV</td><td>0.04</td><td>1.14</td><td>0.08</td><td>0.11</td><td>0.07</td></tr><tr><td rowspan="3">RDE</td><td>Mean</td><td>18,311</td><td>2,872</td><td>21,182</td><td>5,361</td><td>26,543</td></tr><tr><td>St Dev</td><td>418</td><td>2,646</td><td>2,545</td><td>501</td><td>2,645</td></tr><tr><td>CV</td><td>0.02</td><td>0.92</td><td>0.12</td><td>0.09</td><td>0.10</td></tr><tr><td rowspan="3">RDE+div</td><td>Mean</td><td>18,589</td><td>1,596</td><td>20,184</td><td>5,312</td><td>25,496</td></tr><tr><td>St Dev</td><td>344</td><td>1,633</td><td>1,741</td><td>501</td><td>1,848</td></tr><tr><td>CV</td><td>0.02</td><td>1.02</td><td>0.09</td><td>0.09</td><td>0.07</td></tr><tr><td rowspan="2">Strategy</td><td rowspan="2"></td><td colspan="5">Case 3</td></tr><tr><td>Inv. Holding Cost</td><td>Lost Sales Cost</td><td>Total Inv. Cost</td><td>Transp. Cost</td><td>Total Cost</td></tr><tr><td rowspan="3">BENCH1</td><td>Mean</td><td>31,057</td><td>3,478</td><td>34,536</td><td>3,098</td><td>37,634</td></tr><tr><td>St Dev</td><td>1,391</td><td>3,501</td><td>3,377</td><td>252</td><td>3,371</td></tr><tr><td>CV</td><td>0.04</td><td>1.01</td><td>0.10</td><td>0.08</td><td>0.09</td></tr><tr><td rowspan="3">MUN</td><td>Mean</td><td>21,483</td><td>999</td><td>22,482</td><td>6,897</td><td>29,378</td></tr><tr><td>St Dev</td><td>1,187</td><td>1,158</td><td>1,457</td><td>848</td><td>2,098</td></tr><tr><td>CV</td><td>0.06</td><td>1.16</td><td>0.06</td><td>0.12</td><td>0.07</td></tr><tr><td rowspan="3">RTC</td><td>Mean</td><td>26,585</td><td>1,774</td><td>28,359</td><td>4,703</td><td>33,062</td></tr><tr><td>St Dev</td><td>1,204</td><td>2,158</td><td>2,348</td><td>303</td><td>2,343</td></tr><tr><td>CV</td><td>0.05</td><td>1.22</td><td>0.08</td><td>0.06</td><td>0.07</td></tr><tr><td rowspan="3">RDE</td><td>Mean</td><td>21,582</td><td>1,767</td><td>23,348</td><td>5,591</td><td>28,940</td></tr><tr><td>St Dev</td><td>494</td><td>1,567</td><td>1,615</td><td>551</td><td>1,651</td></tr><tr><td>CV</td><td>0.02</td><td>0.89</td><td>0.07</td><td>0.10</td><td>0.06</td></tr><tr><td rowspan="3">RDE+div</td><td>Mean</td><td>21,587</td><td>905</td><td>22,492</td><td>5,639</td><td>28,131</td></tr><tr><td>St Dev</td><td>525</td><td>1,315</td><td>1,209</td><td>544</td><td>1,384</td></tr><tr><td>CV</td><td>0.02</td><td>1.45</td><td>0.05</td><td>0.10</td><td>0.05</td></tr></table>

Results in [\$/week]

30 replication with common random numbers

Fig. 15. Simulation results: parameter set 6 $\mathrm{TC}=100\ \left[\mathrm{S/hr}\right]$ $h_{i}=50[\mathrm{S/veck}]$ $\lambda _ { i }   =   2 . 4$ [arrivals/day], $\theta _ { i }   =   2 0 . 8$ [units] for all i

<table><tr><td rowspan="2">Strategy</td><td rowspan="2"></td><td colspan="5">Case 0 (Symmetric case)</td></tr><tr><td>Inv. Holding Cost</td><td>Lost Sales Cost</td><td>Total Inv. Cost</td><td>Transp. Cost</td><td>Total Cost</td></tr><tr><td rowspan="3">BENCH1</td><td>Mean</td><td>34,425</td><td>4,670</td><td>39,096</td><td>3,044</td><td>42,140</td></tr><tr><td>St Dev</td><td>1,691</td><td>4,308</td><td>3,834</td><td>325</td><td>3,758</td></tr><tr><td>CV</td><td>0.05</td><td>0.92</td><td>0.10</td><td>0.11</td><td>0.09</td></tr><tr><td rowspan="3">MUN</td><td>Mean</td><td>23,539</td><td>1,954</td><td>25,493</td><td>7,302</td><td>32,795</td></tr><tr><td>St Dev</td><td>1,197</td><td>1,728</td><td>1,783</td><td>881</td><td>1,941</td></tr><tr><td>CV</td><td>0.05</td><td>0.88</td><td>0.07</td><td>0.12</td><td>0.06</td></tr><tr><td rowspan="3">RTC</td><td>Mean</td><td>29,653</td><td>4,261</td><td>33,914</td><td>5,281</td><td>39,195</td></tr><tr><td>St Dev</td><td>1,614</td><td>3,799</td><td>3,574</td><td>523</td><td>3,630</td></tr><tr><td>CV</td><td>0.05</td><td>0.89</td><td>0.11</td><td>0.10</td><td>0.09</td></tr><tr><td rowspan="3">RDE</td><td>Mean</td><td>23,151</td><td>4,040</td><td>27,190</td><td>5,717</td><td>32,907</td></tr><tr><td>St Dev</td><td>633</td><td>2,860</td><td>2,841</td><td>479</td><td>2,775</td></tr><tr><td>CV</td><td>0.03</td><td>0.71</td><td>0.10</td><td>0.08</td><td>0.08</td></tr><tr><td rowspan="3">RDE+div</td><td>Mean</td><td>23,482</td><td>2,630</td><td>26,112</td><td>5,793</td><td>31,906</td></tr><tr><td>St Dev</td><td>524</td><td>2,704</td><td>2,699</td><td>417</td><td>2,749</td></tr><tr><td>CV</td><td>0.02</td><td>1.03</td><td>0.10</td><td>0.07</td><td>0.09</td></tr><tr><td rowspan="2">Strategy</td><td rowspan="2"></td><td colspan="5">Case 1</td></tr><tr><td>Inv. Holding Cost</td><td>Lost Sales Cost</td><td>Total Inv. Cost</td><td>Transp. Cost</td><td>Total Cost</td></tr><tr><td rowspan="3">BENCH1</td><td>Mean</td><td>34,452</td><td>5,503</td><td>39,955</td><td>4,050</td><td>44,005</td></tr><tr><td>St Dev</td><td>1,673</td><td>4,789</td><td>4,108</td><td>414</td><td>4,211</td></tr><tr><td>CV</td><td>0.05</td><td>0.87</td><td>0.10</td><td>0.10</td><td>0.10</td></tr><tr><td rowspan="3">MUN</td><td>Mean</td><td>26,848</td><td>2,233</td><td>29,081</td><td>7,225</td><td>36,306</td></tr><tr><td>St Dev</td><td>1,119</td><td>2,763</td><td>2,382</td><td>776</td><td>2,527</td></tr><tr><td>CV</td><td>0.04</td><td>1.24</td><td>0.08</td><td>0.11</td><td>0.07</td></tr><tr><td rowspan="3">RTC</td><td>Mean</td><td>33,758</td><td>2,504</td><td>36,262</td><td>5,824</td><td>42,086</td></tr><tr><td>St Dev</td><td>1,463</td><td>3,145</td><td>3,157</td><td>479</td><td>3,215</td></tr><tr><td>CV</td><td>0.04</td><td>1.26</td><td>0.09</td><td>0.08</td><td>0.08</td></tr><tr><td rowspan="3">RDE</td><td>Mean</td><td>27,965</td><td>3,227</td><td>31,192</td><td>7,002</td><td>38,194</td></tr><tr><td>St Dev</td><td>841</td><td>2,572</td><td>2,350</td><td>560</td><td>2,517</td></tr><tr><td>CV</td><td>0.03</td><td>0.80</td><td>0.08</td><td>0.08</td><td>0.07</td></tr><tr><td rowspan="3">RDE+div</td><td>Mean</td><td>28,194</td><td>1,324</td><td>29,518</td><td>6,785</td><td>36,303</td></tr><tr><td>St Dev</td><td>833</td><td>1,997</td><td>2,050</td><td>720</td><td>2,134</td></tr><tr><td>CV</td><td>0.03</td><td>1.51</td><td>0.07</td><td>0.11</td><td>0.06</td></tr><tr><td rowspan="2">Strategy</td><td rowspan="2"></td><td colspan="5">Case 2</td></tr><tr><td>Inv. Holding Cost</td><td>Lost Sales Cost</td><td>Total Inv. Cost</td><td>Transp. Cost</td><td>Total Cost</td></tr><tr><td rowspan="3">BENCH1</td><td>Mean</td><td>34,610</td><td>3,952</td><td>38,563</td><td>2,734</td><td>41,297</td></tr><tr><td>St Dev</td><td>1,464</td><td>2,876</td><td>2,592</td><td>331</td><td>2,660</td></tr><tr><td>CV</td><td>0.04</td><td>0.73</td><td>0.07</td><td>0.12</td><td>0.06</td></tr><tr><td rowspan="3">MUN</td><td>Mean</td><td>21,356</td><td>3,562</td><td>24,918</td><td>7,523</td><td>32,441</td></tr><tr><td>St Dev</td><td>841</td><td>2,225</td><td>1,930</td><td>857</td><td>1,944</td></tr><tr><td>CV</td><td>0.04</td><td>0.62</td><td>0.08</td><td>0.11</td><td>0.06</td></tr><tr><td rowspan="3">RTC</td><td>Mean</td><td>28,890</td><td>1,965</td><td>30,855</td><td>4,419</td><td>35,274</td></tr><tr><td>St Dev</td><td>1,271</td><td>2,334</td><td>2,813</td><td>498</td><td>2,829</td></tr><tr><td>CV</td><td>0.04</td><td>1.19</td><td>0.09</td><td>0.11</td><td>0.08</td></tr><tr><td rowspan="3">RDE</td><td>Mean</td><td>21,304</td><td>4,612</td><td>25,916</td><td>5,247</td><td>31,163</td></tr><tr><td>St Dev</td><td>587</td><td>3,785</td><td>3,640</td><td>548</td><td>3,844</td></tr><tr><td>CV</td><td>0.03</td><td>0.82</td><td>0.14</td><td>0.10</td><td>0.12</td></tr><tr><td rowspan="3">RDE+div</td><td>Mean</td><td>21,667</td><td>2,631</td><td>24,298</td><td>5,800</td><td>30,098</td></tr><tr><td>St Dev</td><td>453</td><td>2,452</td><td>2,386</td><td>646</td><td>2,430</td></tr><tr><td>CV</td><td>0.02</td><td>0.93</td><td>0.10</td><td>0.11</td><td>0.08</td></tr><tr><td rowspan="2">Strategy</td><td rowspan="2"></td><td colspan="5">Case 3</td></tr><tr><td>Inv. Holding Cost</td><td>Lost Sales Cost</td><td>Total Inv. Cost</td><td>Transp. Cost</td><td>Total Cost</td></tr><tr><td rowspan="3">BENCH1</td><td>Mean</td><td>35,055</td><td>3,169</td><td>38,224</td><td>3,119</td><td>41,343</td></tr><tr><td>St Dev</td><td>1,409</td><td>2,945</td><td>3,135</td><td>290</td><td>3,112</td></tr><tr><td>CV</td><td>0.04</td><td>0.93</td><td>0.08</td><td>0.09</td><td>0.08</td></tr><tr><td rowspan="3">MUN</td><td>Mean</td><td>25,234</td><td>1,656</td><td>26,891</td><td>7,029</td><td>33,920</td></tr><tr><td>St Dev</td><td>1,309</td><td>1,979</td><td>1,978</td><td>789</td><td>2,347</td></tr><tr><td>CV</td><td>0.05</td><td>1.19</td><td>0.07</td><td>0.11</td><td>0.07</td></tr><tr><td rowspan="3">RTC</td><td>Mean</td><td>31,198</td><td>2,420</td><td>33,618</td><td>4,926</td><td>38,544</td></tr><tr><td>St Dev</td><td>1,359</td><td>2,973</td><td>2,462</td><td>423</td><td>2,527</td></tr><tr><td>CV</td><td>0.04</td><td>1.23</td><td>0.07</td><td>0.09</td><td>0.07</td></tr><tr><td rowspan="3">RDE</td><td>Mean</td><td>24,729</td><td>4,071</td><td>28,800</td><td>6,065</td><td>34,865</td></tr><tr><td>St Dev</td><td>762</td><td>3,254</td><td>2,833</td><td>634</td><td>2,964</td></tr><tr><td>CV</td><td>0.03</td><td>0.80</td><td>0.10</td><td>0.10</td><td>0.09</td></tr><tr><td rowspan="3">RDE+div</td><td>Mean</td><td>25,215</td><td>2,420</td><td>27,635</td><td>6,213</td><td>33,848</td></tr><tr><td>St Dev</td><td>609</td><td>2,029</td><td>1,893</td><td>642</td><td>1,937</td></tr><tr><td>CV</td><td>0.02</td><td>0.84</td><td>0.07</td><td>0.10</td><td>0.06</td></tr></table>

Results in [\$/week]

30 replication with common random numbers

Fig. 16. Simulation results: parameter set 7 TC = 100 [\$/hr], $h_{i}=5[\mathrm{S/veck}]$ $\lambda _ { i }   =   5 0 [$ [arrivals/ day], $\theta _ { i }   =   1$ [units] for all i

<table><tr><td rowspan="2">Strategy</td><td rowspan="2"></td><td colspan="5">Case 0 (Symmetric case)</td></tr><tr><td>Inv. Holding Cost</td><td>Lost Sales Cost</td><td>Total Inv. Cost</td><td>Transp. Cost</td><td>Total Cost</td></tr><tr><td rowspan="3">BENCH1</td><td>Mean</td><td>2,178</td><td>440</td><td>2,618</td><td>4,158</td><td>6,776</td></tr><tr><td>St Dev</td><td>41</td><td>605</td><td>594</td><td>173</td><td>588</td></tr><tr><td>CV</td><td>0.02</td><td>1.38</td><td>0.23</td><td>0.04</td><td>0.09</td></tr><tr><td rowspan="3">MUN</td><td>Mean</td><td>2,066</td><td>762</td><td>2,828</td><td>4,648</td><td>7,476</td></tr><tr><td>St Dev</td><td>75</td><td>1,357</td><td>1,325</td><td>484</td><td>1,355</td></tr><tr><td>CV</td><td>0.04</td><td>1.78</td><td>0.47</td><td>0.10</td><td>0.18</td></tr><tr><td rowspan="3">RTC</td><td>Mean</td><td>2,153</td><td>183</td><td>2,336</td><td>3,215</td><td>5,551</td></tr><tr><td>St Dev</td><td>58</td><td>350</td><td>351</td><td>172</td><td>414</td></tr><tr><td>CV</td><td>0.03</td><td>1.92</td><td>0.15</td><td>0.05</td><td>0.07</td></tr><tr><td rowspan="3">RDE</td><td>Mean</td><td>2,098</td><td>220</td><td>2,318</td><td>3,134</td><td>5,452</td></tr><tr><td>St Dev</td><td>46</td><td>246</td><td>232</td><td>211</td><td>328</td></tr><tr><td>CV</td><td>0.02</td><td>1.12</td><td>0.10</td><td>0.07</td><td>0.06</td></tr><tr><td rowspan="3">RDE+div</td><td>Mean</td><td>2,104</td><td>93</td><td>2,197</td><td>3,183</td><td>5,380</td></tr><tr><td>St Dev</td><td>42</td><td>227</td><td>233</td><td>177</td><td>309</td></tr><tr><td>CV</td><td>0.02</td><td>2.44</td><td>0.11</td><td>0.06</td><td>0.06</td></tr><tr><td rowspan="2">Strategy</td><td rowspan="2"></td><td colspan="5">Case 1</td></tr><tr><td>Inv. Holding Cost</td><td>Lost Sales Cost</td><td>Total Inv. Cost</td><td>Transp. Cost</td><td>Total Cost</td></tr><tr><td rowspan="3">BENCH1</td><td>Mean</td><td>2,004</td><td>2,128</td><td>4,132</td><td>5,872</td><td>10,004</td></tr><tr><td>St Dev</td><td>67</td><td>1,633</td><td>1,590</td><td>196</td><td>1,643</td></tr><tr><td>CV</td><td>0.03</td><td>0.77</td><td>0.38</td><td>0.03</td><td>0.16</td></tr><tr><td rowspan="3">MUN</td><td>Mean</td><td>2,024</td><td>1,299</td><td>3,323</td><td>6,397</td><td>9,720</td></tr><tr><td>St Dev</td><td>87</td><td>1,892</td><td>1,845</td><td>680</td><td>1,800</td></tr><tr><td>CV</td><td>0.04</td><td>1.46</td><td>0.56</td><td>0.11</td><td>0.19</td></tr><tr><td rowspan="3">RTC</td><td>Mean</td><td>2,135</td><td>177</td><td>2,311</td><td>4,360</td><td>6,671</td></tr><tr><td>St Dev</td><td>74</td><td>341</td><td>341</td><td>306</td><td>548</td></tr><tr><td>CV</td><td>0.03</td><td>1.93</td><td>0.15</td><td>0.07</td><td>0.08</td></tr><tr><td rowspan="3">RDE</td><td>Mean</td><td>2,098</td><td>307</td><td>2,405</td><td>4,208</td><td>6,613</td></tr><tr><td>St Dev</td><td>44</td><td>479</td><td>467</td><td>334</td><td>606</td></tr><tr><td>CV</td><td>0.02</td><td>1.56</td><td>0.19</td><td>0.08</td><td>0.09</td></tr><tr><td rowspan="3">RDE+div</td><td>Mean</td><td>2,087</td><td>184</td><td>2,271</td><td>4,286</td><td>6,557</td></tr><tr><td>St Dev</td><td>45</td><td>292</td><td>286</td><td>339</td><td>508</td></tr><tr><td>CV</td><td>0.02</td><td>1.59</td><td>0.13</td><td>0.08</td><td>0.08</td></tr><tr><td rowspan="2">Strategy</td><td rowspan="2"></td><td colspan="5">Case 2</td></tr><tr><td>Inv. Holding Cost</td><td>Lost Sales Cost</td><td>Total Inv. Cost</td><td>Transp. Cost</td><td>Total Cost</td></tr><tr><td rowspan="3">BENCH1</td><td>Mean</td><td>2,196</td><td>603</td><td>2,799</td><td>3,931</td><td>6,731</td></tr><tr><td>St Dev</td><td>56</td><td>781</td><td>768</td><td>200</td><td>753</td></tr><tr><td>CV</td><td>0.03</td><td>1.30</td><td>0.27</td><td>0.05</td><td>0.11</td></tr><tr><td rowspan="3">MUN</td><td>Mean</td><td>1,991</td><td>429</td><td>2,420</td><td>4,729</td><td>7,149</td></tr><tr><td>St Dev</td><td>63</td><td>648</td><td>644</td><td>490</td><td>813</td></tr><tr><td>CV</td><td>0.03</td><td>1.51</td><td>0.27</td><td>0.10</td><td>0.11</td></tr><tr><td rowspan="3">RTC</td><td>Mean</td><td>2,056</td><td>444</td><td>2,500</td><td>3,059</td><td>5,559</td></tr><tr><td>St Dev</td><td>61</td><td>476</td><td>442</td><td>249</td><td>472</td></tr><tr><td>CV</td><td>0.03</td><td>1.07</td><td>0.18</td><td>0.08</td><td>0.08</td></tr><tr><td rowspan="3">RDE</td><td>Mean</td><td>1,955</td><td>323</td><td>2,278</td><td>3,062</td><td>5,339</td></tr><tr><td>St Dev</td><td>41</td><td>650</td><td>647</td><td>196</td><td>718</td></tr><tr><td>CV</td><td>0.02</td><td>2.02</td><td>0.28</td><td>0.06</td><td>0.13</td></tr><tr><td rowspan="3">RDE+div</td><td>Mean</td><td>1,945</td><td>175</td><td>2,119</td><td>3,071</td><td>5,191</td></tr><tr><td>St Dev</td><td>42</td><td>266</td><td>273</td><td>236</td><td>394</td></tr><tr><td>CV</td><td>0.02</td><td>1.53</td><td>0.13</td><td>0.08</td><td>0.08</td></tr><tr><td rowspan="2">Strategy</td><td rowspan="2"></td><td colspan="5">Case 3</td></tr><tr><td>Inv. Holding Cost</td><td>Lost Sales Cost</td><td>Total Inv. Cost</td><td>Transp. Cost</td><td>Total Cost</td></tr><tr><td rowspan="3">BENCH1</td><td>Mean</td><td>2,165</td><td>1,108</td><td>3,273</td><td>4,215</td><td>7,489</td></tr><tr><td>St Dev</td><td>60</td><td>1,241</td><td>1,214</td><td>205</td><td>1,271</td></tr><tr><td>CV</td><td>0.03</td><td>1.12</td><td>0.37</td><td>0.05</td><td>0.17</td></tr><tr><td rowspan="3">MUN</td><td>Mean</td><td>2,083</td><td>424</td><td>2,507</td><td>5,073</td><td>7,579</td></tr><tr><td>St Dev</td><td>77</td><td>647</td><td>616</td><td>526</td><td>757</td></tr><tr><td>CV</td><td>0.04</td><td>1.53</td><td>0.25</td><td>0.10</td><td>0.10</td></tr><tr><td rowspan="3">RTC</td><td>Mean</td><td>2,151</td><td>264</td><td>2,416</td><td>3,185</td><td>5,600</td></tr><tr><td>St Dev</td><td>61</td><td>488</td><td>494</td><td>252</td><td>637</td></tr><tr><td>CV</td><td>0.03</td><td>1.85</td><td>0.20</td><td>0.08</td><td>0.11</td></tr><tr><td rowspan="3">RDE</td><td>Mean</td><td>2,115</td><td>188</td><td>2,303</td><td>3,156</td><td>5,458</td></tr><tr><td>St Dev</td><td>38</td><td>311</td><td>305</td><td>225</td><td>407</td></tr><tr><td>CV</td><td>0.02</td><td>1.66</td><td>0.13</td><td>0.07</td><td>0.07</td></tr><tr><td rowspan="3">RDE+div</td><td>Mean</td><td>2,114</td><td>105</td><td>2,218</td><td>3,205</td><td>5,424</td></tr><tr><td>St Dev</td><td>48</td><td>227</td><td>232</td><td>249</td><td>314</td></tr><tr><td>CV</td><td>0.02</td><td>2.17</td><td>0.10</td><td>0.08</td><td>0.06</td></tr></table>

Results in [\$/week]

30 replication with common random numbers

Fig. 17. Simulation results: parameter set 8 TC = 33 [\$/hr], $h_{i}=5[\mathrm{S/veck}]$ $\lambda _ { i }   =   5 0$ [arrivals/day], $\theta _ { i }   =   1$ [units] for all i

<table><tr><td rowspan="2">Strategy</td><td rowspan="2"></td><td colspan="5">Case 0 (Symmetric case)</td></tr><tr><td>Inv. Holding Cost</td><td>Lost Sales Cost</td><td>Total Inv. Cost</td><td>Transp. Cost</td><td>Total Cost</td></tr><tr><td rowspan="3">BENCH1</td><td>Mean</td><td>2,228</td><td>107</td><td>2,335</td><td>1,411</td><td>3,746</td></tr><tr><td>St Dev</td><td>46</td><td>333</td><td>324</td><td>34</td><td>330</td></tr><tr><td>CV</td><td>0.02</td><td>3.11</td><td>0.14</td><td>0.02</td><td>0.09</td></tr><tr><td rowspan="3">MUN</td><td>Mean</td><td>2,086</td><td>364</td><td>2,450</td><td>1,575</td><td>4,025</td></tr><tr><td>St Dev</td><td>97</td><td>619</td><td>576</td><td>158</td><td>612</td></tr><tr><td>CV</td><td>0.05</td><td>1.70</td><td>0.24</td><td>0.10</td><td>0.15</td></tr><tr><td rowspan="3">RTC</td><td>Mean</td><td>2,153</td><td>126</td><td>2,279</td><td>1,062</td><td>3,341</td></tr><tr><td>St Dev</td><td>53</td><td>315</td><td>292</td><td>89</td><td>286</td></tr><tr><td>CV</td><td>0.02</td><td>2.50</td><td>0.13</td><td>0.08</td><td>0.09</td></tr><tr><td rowspan="3">RDE</td><td>Mean</td><td>2,106</td><td>133</td><td>2,240</td><td>1,049</td><td>3,288</td></tr><tr><td>St Dev</td><td>37</td><td>324</td><td>317</td><td>68</td><td>322</td></tr><tr><td>CV</td><td>0.02</td><td>2.43</td><td>0.14</td><td>0.06</td><td>0.10</td></tr><tr><td rowspan="3">RDE+div</td><td>Mean</td><td>2,109</td><td>93</td><td>2,202</td><td>1,053</td><td>3,255</td></tr><tr><td>St Dev</td><td>36</td><td>168</td><td>172</td><td>77</td><td>202</td></tr><tr><td>CV</td><td>0.02</td><td>1.80</td><td>0.08</td><td>0.07</td><td>0.06</td></tr><tr><td rowspan="2">Strategy</td><td rowspan="2"></td><td colspan="5">Case 1</td></tr><tr><td>Inv. Holding Cost</td><td>Lost Sales Cost</td><td>Total Inv. Cost</td><td>Transp. Cost</td><td>Total Cost</td></tr><tr><td rowspan="3">BENCH1</td><td>Mean</td><td>2,082</td><td>727</td><td>2,809</td><td>1,989</td><td>4,799</td></tr><tr><td>St Dev</td><td>59</td><td>859</td><td>839</td><td>48</td><td>842</td></tr><tr><td>CV</td><td>0.03</td><td>1.18</td><td>0.30</td><td>0.02</td><td>0.18</td></tr><tr><td rowspan="3">MUN</td><td>Mean</td><td>2,028</td><td>860</td><td>2,888</td><td>2,142</td><td>5,030</td></tr><tr><td>St Dev</td><td>80</td><td>1,184</td><td>1,142</td><td>160</td><td>1,184</td></tr><tr><td>CV</td><td>0.04</td><td>1.38</td><td>0.40</td><td>0.07</td><td>0.24</td></tr><tr><td rowspan="3">RTC</td><td>Mean</td><td>2,148</td><td>322</td><td>2,470</td><td>1,440</td><td>3,910</td></tr><tr><td>St Dev</td><td>58</td><td>439</td><td>458</td><td>109</td><td>461</td></tr><tr><td>CV</td><td>0.03</td><td>1.36</td><td>0.19</td><td>0.08</td><td>0.12</td></tr><tr><td rowspan="3">RDE</td><td>Mean</td><td>2,064</td><td>358</td><td>2,423</td><td>1,427</td><td>3,850</td></tr><tr><td>St Dev</td><td>51</td><td>549</td><td>541</td><td>112</td><td>577</td></tr><tr><td>CV</td><td>0.02</td><td>1.53</td><td>0.22</td><td>0.08</td><td>0.15</td></tr><tr><td rowspan="3">RDE+div</td><td>Mean</td><td>2,068</td><td>213</td><td>2,281</td><td>1,448</td><td>3,729</td></tr><tr><td>St Dev</td><td>50</td><td>338</td><td>340</td><td>96</td><td>373</td></tr><tr><td>CV</td><td>0.02</td><td>1.59</td><td>0.15</td><td>0.07</td><td>0.10</td></tr><tr><td rowspan="2">Strategy</td><td rowspan="2"></td><td colspan="5">Case 2</td></tr><tr><td>Inv. Holding Cost</td><td>Lost Sales Cost</td><td>Total Inv. Cost</td><td>Transp. Cost</td><td>Total Cost</td></tr><tr><td rowspan="3">BENCH1</td><td>Mean</td><td>2,231</td><td>308</td><td>2,539</td><td>1,359</td><td>3,897</td></tr><tr><td>St Dev</td><td>40</td><td>593</td><td>591</td><td>42</td><td>588</td></tr><tr><td>CV</td><td>0.02</td><td>1.92</td><td>0.23</td><td>0.03</td><td>0.15</td></tr><tr><td rowspan="3">MUN</td><td>Mean</td><td>1,845</td><td>90</td><td>1,934</td><td>1,797</td><td>3,731</td></tr><tr><td>St Dev</td><td>49</td><td>184</td><td>173</td><td>174</td><td>259</td></tr><tr><td>CV</td><td>0.03</td><td>2.05</td><td>0.09</td><td>0.10</td><td>0.07</td></tr><tr><td rowspan="3">RTC</td><td>Mean</td><td>1,874</td><td>377</td><td>2,251</td><td>1,053</td><td>3,304</td></tr><tr><td>St Dev</td><td>38</td><td>635</td><td>615</td><td>71</td><td>621</td></tr><tr><td>CV</td><td>0.02</td><td>1.68</td><td>0.27</td><td>0.07</td><td>0.19</td></tr><tr><td rowspan="3">RDE</td><td>Mean</td><td>1,745</td><td>421</td><td>2,166</td><td>1,092</td><td>3,258</td></tr><tr><td>St Dev</td><td>37</td><td>447</td><td>440</td><td>70</td><td>435</td></tr><tr><td>CV</td><td>0.02</td><td>1.06</td><td>0.20</td><td>0.06</td><td>0.13</td></tr><tr><td rowspan="3">RDE+div</td><td>Mean</td><td>1,750</td><td>236</td><td>1,986</td><td>1,089</td><td>3,075</td></tr><tr><td>St Dev</td><td>48</td><td>363</td><td>347</td><td>88</td><td>360</td></tr><tr><td>CV</td><td>0.03</td><td>1.54</td><td>0.17</td><td>0.08</td><td>0.12</td></tr><tr><td rowspan="2">Strategy</td><td rowspan="2"></td><td colspan="5">Case 3</td></tr><tr><td>Inv. Holding Cost</td><td>Lost Sales Cost</td><td>Total Inv. Cost</td><td>Transp. Cost</td><td>Total Cost</td></tr><tr><td rowspan="3">BENCH1</td><td>Mean</td><td>2,215</td><td>194</td><td>2,409</td><td>1,417</td><td>3,826</td></tr><tr><td>St Dev</td><td>51</td><td>534</td><td>542</td><td>35</td><td>532</td></tr><tr><td>CV</td><td>0.02</td><td>2.76</td><td>0.22</td><td>0.02</td><td>0.14</td></tr><tr><td rowspan="3">MUN</td><td>Mean</td><td>2,027</td><td>259</td><td>2,286</td><td>1,753</td><td>4,039</td></tr><tr><td>St Dev</td><td>83</td><td>458</td><td>419</td><td>158</td><td>429</td></tr><tr><td>CV</td><td>0.04</td><td>1.77</td><td>0.18</td><td>0.09</td><td>0.11</td></tr><tr><td rowspan="3">RTC</td><td>Mean</td><td>2,101</td><td>280</td><td>2,381</td><td>1,079</td><td>3,460</td></tr><tr><td>St Dev</td><td>57</td><td>501</td><td>496</td><td>74</td><td>526</td></tr><tr><td>CV</td><td>0.03</td><td>1.79</td><td>0.21</td><td>0.07</td><td>0.15</td></tr><tr><td rowspan="3">RDE</td><td>Mean</td><td>2,007</td><td>170</td><td>2,177</td><td>1,099</td><td>3,276</td></tr><tr><td>St Dev</td><td>43</td><td>273</td><td>277</td><td>70</td><td>299</td></tr><tr><td>CV</td><td>0.02</td><td>1.61</td><td>0.13</td><td>0.06</td><td>0.09</td></tr><tr><td rowspan="3">RDE+div</td><td>Mean</td><td>2,009</td><td>98</td><td>2,107</td><td>1,121</td><td>3,228</td></tr><tr><td>St Dev</td><td>40</td><td>228</td><td>230</td><td>71</td><td>247</td></tr><tr><td>CV</td><td>0.02</td><td>2.33</td><td>0.11</td><td>0.06</td><td>0.08</td></tr></table>

Results in [\$/week]

30 replication with common random numbers

Fig. 18. Simulation results: parameter set $9\  TC = 300\ [\%/hr]$ $h_{i}=5[\mathrm{S/veck}]$ $\lambda _ { i }   =   5 0 [$ [arrivals/ day], $\theta _ { i }   =   1$ [units] for all i

<table><tr><td rowspan="2">Strategy</td><td rowspan="2"></td><td colspan="5">Case 0 (Symmetric case)</td></tr><tr><td>Inv. Holding Cost</td><td>Lost Sales Cost</td><td>Total Inv. Cost</td><td>Transp. Cost</td><td>Total Cost</td></tr><tr><td rowspan="3">BENCH1</td><td>Mean</td><td>2,007</td><td>3,317</td><td>5,324</td><td>11,593</td><td>16,917</td></tr><tr><td>St Dev</td><td>63</td><td>2,482</td><td>2,445</td><td>550</td><td>2,587</td></tr><tr><td>CV</td><td>0.03</td><td>0.75</td><td>0.46</td><td>0.05</td><td>0.15</td></tr><tr><td rowspan="3">MUN</td><td>Mean</td><td>2,077</td><td>426</td><td>2,503</td><td>14,269</td><td>16,772</td></tr><tr><td>St Dev</td><td>95</td><td>442</td><td>427</td><td>1,532</td><td>1,648</td></tr><tr><td>CV</td><td>0.05</td><td>1.04</td><td>0.17</td><td>0.11</td><td>0.10</td></tr><tr><td rowspan="3">RTC</td><td>Mean</td><td>2,132</td><td>172</td><td>2,304</td><td>9,507</td><td>11,811</td></tr><tr><td>St Dev</td><td>63</td><td>279</td><td>283</td><td>776</td><td>826</td></tr><tr><td>CV</td><td>0.03</td><td>1.62</td><td>0.12</td><td>0.08</td><td>0.07</td></tr><tr><td rowspan="3">RDE</td><td>Mean</td><td>2,096</td><td>192</td><td>2,288</td><td>9,358</td><td>11,646</td></tr><tr><td>St Dev</td><td>36</td><td>301</td><td>290</td><td>491</td><td>642</td></tr><tr><td>CV</td><td>0.02</td><td>1.57</td><td>0.13</td><td>0.05</td><td>0.06</td></tr><tr><td rowspan="3">RDE+div</td><td>Mean</td><td>2,109</td><td>140</td><td>2,249</td><td>9,466</td><td>11,715</td></tr><tr><td>St Dev</td><td>44</td><td>251</td><td>251</td><td>597</td><td>621</td></tr><tr><td>CV</td><td>0.02</td><td>1.80</td><td>0.11</td><td>0.06</td><td>0.05</td></tr><tr><td rowspan="2">Strategy</td><td rowspan="2"></td><td colspan="5">Case 1</td></tr><tr><td>Inv. Holding Cost</td><td>Lost Sales Cost</td><td>Total Inv. Cost</td><td>Transp. Cost</td><td>Total Cost</td></tr><tr><td rowspan="3">BENCH1</td><td>Mean</td><td>1,799</td><td>7,725</td><td>9,524</td><td>15,720</td><td>25,244</td></tr><tr><td>St Dev</td><td>62</td><td>2,998</td><td>2,977</td><td>1,000</td><td>3,075</td></tr><tr><td>CV</td><td>0.03</td><td>0.39</td><td>0.31</td><td>0.06</td><td>0.12</td></tr><tr><td rowspan="3">MUN</td><td>Mean</td><td>2,009</td><td>929</td><td>2,937</td><td>18,889</td><td>21,826</td></tr><tr><td>St Dev</td><td>67</td><td>1,205</td><td>1,168</td><td>1,384</td><td>1,469</td></tr><tr><td>CV</td><td>0.03</td><td>1.30</td><td>0.40</td><td>0.07</td><td>0.07</td></tr><tr><td rowspan="3">RTC</td><td>Mean</td><td>2,060</td><td>1,001</td><td>3,060</td><td>12,338</td><td>15,399</td></tr><tr><td>St Dev</td><td>62</td><td>837</td><td>852</td><td>853</td><td>1,310</td></tr><tr><td>CV</td><td>0.03</td><td>0.84</td><td>0.28</td><td>0.07</td><td>0.09</td></tr><tr><td rowspan="3">RDE</td><td>Mean</td><td>2,029</td><td>873</td><td>2,902</td><td>12,072</td><td>14,974</td></tr><tr><td>St Dev</td><td>39</td><td>745</td><td>741</td><td>945</td><td>1,097</td></tr><tr><td>CV</td><td>0.02</td><td>0.85</td><td>0.26</td><td>0.08</td><td>0.07</td></tr><tr><td rowspan="3">RDE+div</td><td>Mean</td><td>2,031</td><td>493</td><td>2,524</td><td>12,172</td><td>14,696</td></tr><tr><td>St Dev</td><td>47</td><td>635</td><td>638</td><td>783</td><td>1,046</td></tr><tr><td>CV</td><td>0.02</td><td>1.29</td><td>0.25</td><td>0.06</td><td>0.07</td></tr><tr><td rowspan="2">Strategy</td><td rowspan="2"></td><td colspan="5">Case 2</td></tr><tr><td>Inv. Holding Cost</td><td>Lost Sales Cost</td><td>Total Inv. Cost</td><td>Transp. Cost</td><td>Total Cost</td></tr><tr><td rowspan="3">BENCH1</td><td>Mean</td><td>2,056</td><td>3,174</td><td>5,229</td><td>10,616</td><td>15,845</td></tr><tr><td>St Dev</td><td>69</td><td>2,274</td><td>2,233</td><td>748</td><td>2,359</td></tr><tr><td>CV</td><td>0.03</td><td>0.72</td><td>0.43</td><td>0.07</td><td>0.15</td></tr><tr><td rowspan="3">MUN</td><td>Mean</td><td>2,022</td><td>2,323</td><td>4,345</td><td>12,921</td><td>17,266</td></tr><tr><td>St Dev</td><td>101</td><td>2,007</td><td>1,966</td><td>1,470</td><td>2,024</td></tr><tr><td>CV</td><td>0.05</td><td>0.86</td><td>0.45</td><td>0.11</td><td>0.12</td></tr><tr><td rowspan="3">RTC</td><td>Mean</td><td>2,089</td><td>685</td><td>2,774</td><td>8,874</td><td>11,647</td></tr><tr><td>St Dev</td><td>61</td><td>703</td><td>678</td><td>753</td><td>1,110</td></tr><tr><td>CV</td><td>0.03</td><td>1.03</td><td>0.24</td><td>0.08</td><td>0.10</td></tr><tr><td rowspan="3">RDE</td><td>Mean</td><td>2,058</td><td>430</td><td>2,488</td><td>8,747</td><td>11,234</td></tr><tr><td>St Dev</td><td>46</td><td>563</td><td>549</td><td>619</td><td>871</td></tr><tr><td>CV</td><td>0.02</td><td>1.31</td><td>0.22</td><td>0.07</td><td>0.08</td></tr><tr><td rowspan="3">RDE+div</td><td>Mean</td><td>2,065</td><td>380</td><td>2,445</td><td>8,881</td><td>11,326</td></tr><tr><td>St Dev</td><td>55</td><td>1,100</td><td>1,085</td><td>662</td><td>1,236</td></tr><tr><td>CV</td><td>0.03</td><td>2.89</td><td>0.44</td><td>0.07</td><td>0.11</td></tr><tr><td rowspan="2">Strategy</td><td rowspan="2"></td><td colspan="5">Case 3</td></tr><tr><td>Inv. Holding Cost</td><td>Lost Sales Cost</td><td>Total Inv. Cost</td><td>Transp. Cost</td><td>Total Cost</td></tr><tr><td rowspan="3">BENCH1</td><td>Mean</td><td>1,991</td><td>3,514</td><td>5,505</td><td>11,643</td><td>17,148</td></tr><tr><td>St Dev</td><td>66</td><td>2,453</td><td>2,412</td><td>667</td><td>2,464</td></tr><tr><td>CV</td><td>0.03</td><td>0.70</td><td>0.44</td><td>0.06</td><td>0.14</td></tr><tr><td rowspan="3">MUN</td><td>Mean</td><td>2,050</td><td>880</td><td>2,930</td><td>14,527</td><td>17,457</td></tr><tr><td>St Dev</td><td>89</td><td>1,169</td><td>1,116</td><td>1,470</td><td>2,068</td></tr><tr><td>CV</td><td>0.04</td><td>1.33</td><td>0.38</td><td>0.10</td><td>0.12</td></tr><tr><td rowspan="3">RTC</td><td>Mean</td><td>2,096</td><td>721</td><td>2,816</td><td>9,178</td><td>11,995</td></tr><tr><td>St Dev</td><td>62</td><td>807</td><td>831</td><td>689</td><td>1,194</td></tr><tr><td>CV</td><td>0.03</td><td>1.12</td><td>0.30</td><td>0.08</td><td>0.10</td></tr><tr><td rowspan="3">RDE</td><td>Mean</td><td>2,072</td><td>617</td><td>2,688</td><td>9,036</td><td>11,724</td></tr><tr><td>St Dev</td><td>48</td><td>637</td><td>632</td><td>733</td><td>1,041</td></tr><tr><td>CV</td><td>0.02</td><td>1.03</td><td>0.23</td><td>0.08</td><td>0.09</td></tr><tr><td rowspan="3">RDE+div</td><td>Mean</td><td>2,056</td><td>493</td><td>2,550</td><td>9,121</td><td>11,670</td></tr><tr><td>St Dev</td><td>46</td><td>569</td><td>570</td><td>570</td><td>821</td></tr><tr><td>CV</td><td>0.02</td><td>1.15</td><td>0.22</td><td>0.06</td><td>0.07</td></tr></table>

Results in [\$/week]

30 replication with common random numbers

Fig. 19. Simulation results: parameter set $10\  TC  = 100\ [\ \ \ \ \ \ \ \ \ \ h_i = 5[\ \ \ \ \ \ \ \ \lambda_i = 10.5$ [arrivals/day], $\theta _ { i }   =   4 . 8$ [units] for all i

<table><tr><td rowspan="2">Strategy</td><td rowspan="2"></td><td colspan="5">Case 0 (Symmetric case)</td></tr><tr><td>Inv. Holding Cost</td><td>Lost Sales Cost</td><td>Total Inv. Cost</td><td>Transp. Cost</td><td>Total Cost</td></tr><tr><td rowspan="3">BENCH1</td><td>Mean</td><td>2,173</td><td>2,082</td><td>4,255</td><td>4,119</td><td>8,374</td></tr><tr><td>St Dev</td><td>58</td><td>2,259</td><td>2,229</td><td>200</td><td>2,281</td></tr><tr><td>CV</td><td>0.03</td><td>1.09</td><td>0.52</td><td>0.05</td><td>0.27</td></tr><tr><td rowspan="3">MUN</td><td>Mean</td><td>2,227</td><td>808</td><td>3,035</td><td>5,007</td><td>8,042</td></tr><tr><td>St Dev</td><td>107</td><td>914</td><td>915</td><td>600</td><td>1,130</td></tr><tr><td>CV</td><td>0.05</td><td>1.13</td><td>0.30</td><td>0.12</td><td>0.14</td></tr><tr><td rowspan="3">RTC</td><td>Mean</td><td>2,395</td><td>658</td><td>3,054</td><td>3,782</td><td>6,836</td></tr><tr><td>St Dev</td><td>94</td><td>786</td><td>768</td><td>237</td><td>801</td></tr><tr><td>CV</td><td>0.04</td><td>1.19</td><td>0.25</td><td>0.06</td><td>0.12</td></tr><tr><td rowspan="3">RDE</td><td>Mean</td><td>2,273</td><td>652</td><td>2,925</td><td>3,603</td><td>6,528</td></tr><tr><td>St Dev</td><td>57</td><td>1,264</td><td>1,250</td><td>297</td><td>1,307</td></tr><tr><td>CV</td><td>0.02</td><td>1.94</td><td>0.43</td><td>0.08</td><td>0.20</td></tr><tr><td rowspan="3">RDE+div</td><td>Mean</td><td>2,281</td><td>602</td><td>2,883</td><td>3,620</td><td>6,503</td></tr><tr><td>St Dev</td><td>52</td><td>877</td><td>859</td><td>321</td><td>913</td></tr><tr><td>CV</td><td>0.02</td><td>1.46</td><td>0.30</td><td>0.09</td><td>0.14</td></tr><tr><td rowspan="2">Strategy</td><td rowspan="2"></td><td colspan="5">Case 1</td></tr><tr><td>Inv. Holding Cost</td><td>Lost Sales Cost</td><td>Total Inv. Cost</td><td>Transp. Cost</td><td>Total Cost</td></tr><tr><td rowspan="3">BENCH1</td><td>Mean</td><td>2,000</td><td>3,985</td><td>5,986</td><td>5,721</td><td>11,707</td></tr><tr><td>St Dev</td><td>68</td><td>2,999</td><td>2,958</td><td>257</td><td>2,971</td></tr><tr><td>CV</td><td>0.03</td><td>0.75</td><td>0.49</td><td>0.04</td><td>0.25</td></tr><tr><td rowspan="3">MUN</td><td>Mean</td><td>2,183</td><td>1,023</td><td>3,206</td><td>6,661</td><td>9,867</td></tr><tr><td>St Dev</td><td>106</td><td>1,241</td><td>1,199</td><td>571</td><td>1,162</td></tr><tr><td>CV</td><td>0.05</td><td>1.21</td><td>0.37</td><td>0.09</td><td>0.12</td></tr><tr><td rowspan="3">RTC</td><td>Mean</td><td>2,419</td><td>726</td><td>3,145</td><td>5,181</td><td>8,326</td></tr><tr><td>St Dev</td><td>114</td><td>901</td><td>917</td><td>269</td><td>953</td></tr><tr><td>CV</td><td>0.05</td><td>1.24</td><td>0.29</td><td>0.05</td><td>0.11</td></tr><tr><td rowspan="3">RDE</td><td>Mean</td><td>2,273</td><td>634</td><td>2,907</td><td>5,212</td><td>8,119</td></tr><tr><td>St Dev</td><td>52</td><td>906</td><td>900</td><td>553</td><td>1,074</td></tr><tr><td>CV</td><td>0.02</td><td>1.43</td><td>0.31</td><td>0.11</td><td>0.13</td></tr><tr><td rowspan="3">RDE+div</td><td>Mean</td><td>2,292</td><td>637</td><td>2,929</td><td>5,080</td><td>8,009</td></tr><tr><td>St Dev</td><td>49</td><td>932</td><td>927</td><td>357</td><td>993</td></tr><tr><td>CV</td><td>0.02</td><td>1.46</td><td>0.32</td><td>0.07</td><td>0.12</td></tr><tr><td rowspan="2">Strategy</td><td rowspan="2"></td><td colspan="5">Case 2</td></tr><tr><td>Inv. Holding Cost</td><td>Lost Sales Cost</td><td>Total Inv. Cost</td><td>Transp. Cost</td><td>Total Cost</td></tr><tr><td rowspan="3">BENCH1</td><td>Mean</td><td>2,199</td><td>2,081</td><td>4,280</td><td>3,842</td><td>8,122</td></tr><tr><td>St Dev</td><td>75</td><td>1,643</td><td>1,630</td><td>196</td><td>1,613</td></tr><tr><td>CV</td><td>0.03</td><td>0.79</td><td>0.38</td><td>0.05</td><td>0.20</td></tr><tr><td rowspan="3">MUN</td><td>Mean</td><td>2,161</td><td>541</td><td>2,702</td><td>4,971</td><td>7,674</td></tr><tr><td>St Dev</td><td>110</td><td>707</td><td>663</td><td>487</td><td>926</td></tr><tr><td>CV</td><td>0.05</td><td>1.31</td><td>0.25</td><td>0.10</td><td>0.12</td></tr><tr><td rowspan="3">RTC</td><td>Mean</td><td>2,408</td><td>466</td><td>2,874</td><td>3,459</td><td>6,334</td></tr><tr><td>St Dev</td><td>110</td><td>578</td><td>591</td><td>271</td><td>645</td></tr><tr><td>CV</td><td>0.05</td><td>1.24</td><td>0.21</td><td>0.08</td><td>0.10</td></tr><tr><td rowspan="3">RDE</td><td>Mean</td><td>2,190</td><td>690</td><td>2,881</td><td>3,586</td><td>6,466</td></tr><tr><td>St Dev</td><td>43</td><td>946</td><td>949</td><td>484</td><td>1,120</td></tr><tr><td>CV</td><td>0.02</td><td>1.37</td><td>0.33</td><td>0.13</td><td>0.17</td></tr><tr><td rowspan="3">RDE+div</td><td>Mean</td><td>2,195</td><td>364</td><td>2,559</td><td>3,431</td><td>5,990</td></tr><tr><td>St Dev</td><td>54</td><td>520</td><td>504</td><td>284</td><td>596</td></tr><tr><td>CV</td><td>0.02</td><td>1.43</td><td>0.20</td><td>0.08</td><td>0.10</td></tr><tr><td rowspan="2">Strategy</td><td rowspan="2"></td><td colspan="5">Case 3</td></tr><tr><td>Inv. Holding Cost</td><td>Lost Sales Cost</td><td>Total Inv. Cost</td><td>Transp. Cost</td><td>Total Cost</td></tr><tr><td rowspan="3">BENCH1</td><td>Mean</td><td>2,159</td><td>2,412</td><td>4,571</td><td>4,126</td><td>8,697</td></tr><tr><td>St Dev</td><td>72</td><td>2,049</td><td>2,017</td><td>225</td><td>2,051</td></tr><tr><td>CV</td><td>0.03</td><td>0.85</td><td>0.44</td><td>0.05</td><td>0.24</td></tr><tr><td rowspan="3">MUN</td><td>Mean</td><td>2,233</td><td>570</td><td>2,804</td><td>5,155</td><td>7,959</td></tr><tr><td>St Dev</td><td>101</td><td>737</td><td>729</td><td>533</td><td>836</td></tr><tr><td>CV</td><td>0.05</td><td>1.29</td><td>0.26</td><td>0.10</td><td>0.11</td></tr><tr><td rowspan="3">RTC</td><td>Mean</td><td>2,442</td><td>710</td><td>3,152</td><td>3,805</td><td>6,957</td></tr><tr><td>St Dev</td><td>108</td><td>939</td><td>919</td><td>288</td><td>910</td></tr><tr><td>CV</td><td>0.04</td><td>1.32</td><td>0.29</td><td>0.08</td><td>0.13</td></tr><tr><td rowspan="3">RDE</td><td>Mean</td><td>2,297</td><td>468</td><td>2,765</td><td>3,653</td><td>6,418</td></tr><tr><td>St Dev</td><td>50</td><td>758</td><td>746</td><td>264</td><td>790</td></tr><tr><td>CV</td><td>0.02</td><td>1.62</td><td>0.27</td><td>0.07</td><td>0.12</td></tr><tr><td rowspan="3">RDE+div</td><td>Mean</td><td>2,296</td><td>558</td><td>2,854</td><td>3,744</td><td>6,598</td></tr><tr><td>St Dev</td><td>45</td><td>864</td><td>868</td><td>298</td><td>899</td></tr><tr><td>CV</td><td>0.02</td><td>1.55</td><td>0.30</td><td>0.08</td><td>0.14</td></tr></table>

Results in [\$/week]

30 replication with common random numbers

Fig. 20. Simulation results: parameter set $11\  TC  = 100\ [\$/hr],\ h_{i} = 5[\$/weak],\ \lambda_{i} = 4.35$ [arrivals/day], $\theta _ { i } = 1 1 . 5$ [units] for all i

<table><tr><td rowspan="2">Strategy</td><td rowspan="2"></td><td colspan="5">Case 0 (Symmetric case)</td></tr><tr><td>Inv. Holding Cost</td><td>Lost Sales Cost</td><td>Total Inv. Cost</td><td>Transp. Cost</td><td>Total Cost</td></tr><tr><td rowspan="3">BENCH1</td><td>Mean</td><td>2,155</td><td>7,635</td><td>9,790</td><td>4,017</td><td>13,807</td></tr><tr><td>St Dev</td><td>112</td><td>5,935</td><td>5,883</td><td>297</td><td>5,990</td></tr><tr><td>CV</td><td>0.05</td><td>0.78</td><td>0.60</td><td>0.07</td><td>0.43</td></tr><tr><td rowspan="3">MUN</td><td>Mean</td><td>2,432</td><td>985</td><td>3,417</td><td>5,626</td><td>9,042</td></tr><tr><td>St Dev</td><td>123</td><td>1,166</td><td>1,159</td><td>560</td><td>1,302</td></tr><tr><td>CV</td><td>0.05</td><td>1.18</td><td>0.34</td><td>0.10</td><td>0.14</td></tr><tr><td rowspan="3">RTC</td><td>Mean</td><td>2,704</td><td>1,200</td><td>3,903</td><td>4,612</td><td>8,515</td></tr><tr><td>St Dev</td><td>139</td><td>1,811</td><td>1,743</td><td>360</td><td>1,969</td></tr><tr><td>CV</td><td>0.05</td><td>1.51</td><td>0.45</td><td>0.08</td><td>0.23</td></tr><tr><td rowspan="3">RDE</td><td>Mean</td><td>2,438</td><td>2,003</td><td>4,441</td><td>4,102</td><td>8,543</td></tr><tr><td>St Dev</td><td>59</td><td>1,963</td><td>1,958</td><td>359</td><td>2,036</td></tr><tr><td>CV</td><td>0.02</td><td>0.98</td><td>0.44</td><td>0.09</td><td>0.24</td></tr><tr><td rowspan="3">RDE+div</td><td>Mean</td><td>2,467</td><td>1,476</td><td>3,943</td><td>4,199</td><td>8,142</td></tr><tr><td>St Dev</td><td>57</td><td>1,778</td><td>1,758</td><td>355</td><td>1,965</td></tr><tr><td>CV</td><td>0.02</td><td>1.20</td><td>0.45</td><td>0.08</td><td>0.24</td></tr><tr><td rowspan="2">Strategy</td><td rowspan="2"></td><td colspan="5">Case 1</td></tr><tr><td>Inv. Holding Cost</td><td>Lost Sales Cost</td><td>Total Inv. Cost</td><td>Transp. Cost</td><td>Total Cost</td></tr><tr><td rowspan="3">BENCH1</td><td>Mean</td><td>1,997</td><td>11,111</td><td>13,108</td><td>5,463</td><td>18,571</td></tr><tr><td>St Dev</td><td>112</td><td>5,915</td><td>5,856</td><td>334</td><td>5,932</td></tr><tr><td>CV</td><td>0.06</td><td>0.53</td><td>0.45</td><td>0.06</td><td>0.32</td></tr><tr><td rowspan="3">MUN</td><td>Mean</td><td>2,365</td><td>1,828</td><td>4,193</td><td>7,101</td><td>11,294</td></tr><tr><td>St Dev</td><td>115</td><td>2,188</td><td>2,141</td><td>679</td><td>2,086</td></tr><tr><td>CV</td><td>0.05</td><td>1.20</td><td>0.51</td><td>0.10</td><td>0.18</td></tr><tr><td rowspan="3">RTC</td><td>Mean</td><td>2,703</td><td>1,454</td><td>4,157</td><td>6,321</td><td>10,479</td></tr><tr><td>St Dev</td><td>134</td><td>1,850</td><td>1,793</td><td>417</td><td>1,933</td></tr><tr><td>CV</td><td>0.05</td><td>1.27</td><td>0.43</td><td>0.07</td><td>0.18</td></tr><tr><td rowspan="3">RDE</td><td>Mean</td><td>2,462</td><td>1,752</td><td>4,214</td><td>6,097</td><td>10,311</td></tr><tr><td>St Dev</td><td>66</td><td>2,302</td><td>2,289</td><td>596</td><td>2,526</td></tr><tr><td>CV</td><td>0.03</td><td>1.31</td><td>0.54</td><td>0.10</td><td>0.24</td></tr><tr><td rowspan="3">RDE+div</td><td>Mean</td><td>2,488</td><td>921</td><td>3,409</td><td>6,006</td><td>9,414</td></tr><tr><td>St Dev</td><td>64</td><td>1,253</td><td>1,225</td><td>521</td><td>1,543</td></tr><tr><td>CV</td><td>0.03</td><td>1.36</td><td>0.36</td><td>0.09</td><td>0.16</td></tr><tr><td rowspan="2">Strategy</td><td rowspan="2"></td><td colspan="5">Case 2</td></tr><tr><td>Inv. Holding Cost</td><td>Lost Sales Cost</td><td>Total Inv. Cost</td><td>Transp. Cost</td><td>Total Cost</td></tr><tr><td rowspan="3">BENCH1</td><td>Mean</td><td>2,199</td><td>6,968</td><td>9,167</td><td>3,689</td><td>12,857</td></tr><tr><td>St Dev</td><td>84</td><td>4,807</td><td>4,759</td><td>282</td><td>4,894</td></tr><tr><td>CV</td><td>0.04</td><td>0.69</td><td>0.52</td><td>0.08</td><td>0.38</td></tr><tr><td rowspan="3">MUN</td><td>Mean</td><td>2,406</td><td>1,310</td><td>3,716</td><td>5,258</td><td>8,975</td></tr><tr><td>St Dev</td><td>133</td><td>2,227</td><td>2,155</td><td>756</td><td>2,089</td></tr><tr><td>CV</td><td>0.06</td><td>1.70</td><td>0.58</td><td>0.14</td><td>0.23</td></tr><tr><td rowspan="3">RTC</td><td>Mean</td><td>2,728</td><td>1,732</td><td>4,460</td><td>4,306</td><td>8,766</td></tr><tr><td>St Dev</td><td>131</td><td>1,873</td><td>1,841</td><td>374</td><td>1,947</td></tr><tr><td>CV</td><td>0.05</td><td>1.08</td><td>0.41</td><td>0.09</td><td>0.22</td></tr><tr><td rowspan="3">RDE</td><td>Mean</td><td>2,398</td><td>1,974</td><td>4,372</td><td>4,129</td><td>8,501</td></tr><tr><td>St Dev</td><td>58</td><td>1,550</td><td>1,561</td><td>620</td><td>1,679</td></tr><tr><td>CV</td><td>0.02</td><td>0.79</td><td>0.36</td><td>0.15</td><td>0.20</td></tr><tr><td rowspan="3">RDE+div</td><td>Mean</td><td>2,436</td><td>653</td><td>3,088</td><td>4,073</td><td>7,161</td></tr><tr><td>St Dev</td><td>61</td><td>940</td><td>944</td><td>577</td><td>1,060</td></tr><tr><td>CV</td><td>0.03</td><td>1.44</td><td>0.31</td><td>0.14</td><td>0.15</td></tr><tr><td rowspan="2">Strategy</td><td rowspan="2"></td><td colspan="5">Case 3</td></tr><tr><td>Inv. Holding Cost</td><td>Lost Sales Cost</td><td>Total Inv. Cost</td><td>Transp. Cost</td><td>Total Cost</td></tr><tr><td rowspan="3">BENCH1</td><td>Mean</td><td>2,144</td><td>7,516</td><td>9,659</td><td>3,960</td><td>13,620</td></tr><tr><td>St Dev</td><td>88</td><td>4,136</td><td>4,083</td><td>197</td><td>4,123</td></tr><tr><td>CV</td><td>0.04</td><td>0.55</td><td>0.42</td><td>0.05</td><td>0.30</td></tr><tr><td rowspan="3">MUN</td><td>Mean</td><td>2,415</td><td>946</td><td>3,361</td><td>5,691</td><td>9,052</td></tr><tr><td>St Dev</td><td>85</td><td>1,372</td><td>1,337</td><td>654</td><td>1,289</td></tr><tr><td>CV</td><td>0.04</td><td>1.45</td><td>0.40</td><td>0.11</td><td>0.14</td></tr><tr><td rowspan="3">RTC</td><td>Mean</td><td>2,715</td><td>1,144</td><td>3,859</td><td>4,678</td><td>8,537</td></tr><tr><td>St Dev</td><td>140</td><td>1,398</td><td>1,353</td><td>398</td><td>1,444</td></tr><tr><td>CV</td><td>0.05</td><td>1.22</td><td>0.35</td><td>0.09</td><td>0.17</td></tr><tr><td rowspan="3">RDE</td><td>Mean</td><td>2,459</td><td>1,823</td><td>4,282</td><td>4,458</td><td>8,740</td></tr><tr><td>St Dev</td><td>71</td><td>2,178</td><td>2,142</td><td>530</td><td>2,402</td></tr><tr><td>CV</td><td>0.03</td><td>1.19</td><td>0.50</td><td>0.12</td><td>0.27</td></tr><tr><td rowspan="3">RDE+div</td><td>Mean</td><td>2,502</td><td>784</td><td>3,287</td><td>4,562</td><td>7,849</td></tr><tr><td>St Dev</td><td>74</td><td>1,138</td><td>1,130</td><td>376</td><td>1,162</td></tr><tr><td>CV</td><td>0.03</td><td>1.45</td><td>0.34</td><td>0.08</td><td>0.15</td></tr></table>

Results in [\$/week]

30 replication with common random numbers

Fig. 21. Simulation results: parameter set 12 $\left(  TC  = 100 \left[ \mathbb{S}/ hr  \right] \right.$ $h_{i}=5[\mathrm{S/veck}]$ $\lambda _ { i }   =   2 . 4$ [arrivals/day], $\theta _ { i }   =   2 0 . 8$ [units] for all i)

<table><tr><td rowspan="2">Strategy</td><td rowspan="2"></td><td colspan="5">Case 0 (Symmetric case)</td></tr><tr><td>Inv. Holding Cost</td><td>Lost Sales Cost</td><td>Total Inv. Cost</td><td>Transp. Cost</td><td>Total Cost</td></tr><tr><td rowspan="3">BENCH1</td><td>Mean</td><td>2,137</td><td>18,784</td><td>20,921</td><td>3,758</td><td>24,679</td></tr><tr><td>St Dev</td><td>145</td><td>8,613</td><td>8,512</td><td>363</td><td>8,639</td></tr><tr><td>CV</td><td>0.07</td><td>0.46</td><td>0.41</td><td>0.10</td><td>0.35</td></tr><tr><td rowspan="3">MUN</td><td>Mean</td><td>2,673</td><td>1,174</td><td>3,847</td><td>6,441</td><td>10,288</td></tr><tr><td>St Dev</td><td>118</td><td>1,487</td><td>1,460</td><td>671</td><td>1,474</td></tr><tr><td>CV</td><td>0.04</td><td>1.27</td><td>0.38</td><td>0.10</td><td>0.14</td></tr><tr><td rowspan="3">RTC</td><td>Mean</td><td>2,906</td><td>4,250</td><td>7,156</td><td>5,436</td><td>12,592</td></tr><tr><td>St Dev</td><td>149</td><td>4,277</td><td>4,239</td><td>471</td><td>4,401</td></tr><tr><td>CV</td><td>0.05</td><td>1.01</td><td>0.59</td><td>0.09</td><td>0.35</td></tr><tr><td rowspan="3">RDE</td><td>Mean</td><td>2,626</td><td>3,741</td><td>6,367</td><td>4,641</td><td>11,008</td></tr><tr><td>St Dev</td><td>82</td><td>3,575</td><td>3,563</td><td>385</td><td>3,475</td></tr><tr><td>CV</td><td>0.03</td><td>0.96</td><td>0.56</td><td>0.08</td><td>0.32</td></tr><tr><td rowspan="3">RDE+div</td><td>Mean</td><td>2,660</td><td>2,214</td><td>4,874</td><td>4,779</td><td>9,653</td></tr><tr><td>St Dev</td><td>66</td><td>2,021</td><td>2,034</td><td>517</td><td>2,128</td></tr><tr><td>CV</td><td>0.02</td><td>0.91</td><td>0.42</td><td>0.11</td><td>0.22</td></tr><tr><td rowspan="2">Strategy</td><td rowspan="2"></td><td colspan="5">Case 1</td></tr><tr><td>Inv. Holding Cost</td><td>Lost Sales Cost</td><td>Total Inv. Cost</td><td>Transp. Cost</td><td>Total Cost</td></tr><tr><td rowspan="3">BENCH1</td><td>Mean</td><td>2,017</td><td>17,912</td><td>19,928</td><td>5,131</td><td>25,059</td></tr><tr><td>St Dev</td><td>127</td><td>7,455</td><td>7,373</td><td>349</td><td>7,482</td></tr><tr><td>CV</td><td>0.06</td><td>0.42</td><td>0.37</td><td>0.07</td><td>0.30</td></tr><tr><td rowspan="3">MUN</td><td>Mean</td><td>2,571</td><td>2,220</td><td>4,791</td><td>7,824</td><td>12,615</td></tr><tr><td>St Dev</td><td>127</td><td>2,385</td><td>2,345</td><td>733</td><td>2,368</td></tr><tr><td>CV</td><td>0.05</td><td>1.07</td><td>0.49</td><td>0.09</td><td>0.19</td></tr><tr><td rowspan="3">RTC</td><td>Mean</td><td>2,866</td><td>3,121</td><td>5,986</td><td>7,362</td><td>13,349</td></tr><tr><td>St Dev</td><td>129</td><td>3,558</td><td>3,512</td><td>560</td><td>3,604</td></tr><tr><td>CV</td><td>0.05</td><td>1.14</td><td>0.59</td><td>0.08</td><td>0.27</td></tr><tr><td rowspan="3">RDE</td><td>Mean</td><td>2,652</td><td>1,920</td><td>4,572</td><td>7,253</td><td>11,826</td></tr><tr><td>St Dev</td><td>68</td><td>1,667</td><td>1,654</td><td>605</td><td>1,739</td></tr><tr><td>CV</td><td>0.03</td><td>0.87</td><td>0.36</td><td>0.08</td><td>0.15</td></tr><tr><td rowspan="3">RDE+div</td><td>Mean</td><td>2,660</td><td>1,946</td><td>4,606</td><td>7,451</td><td>12,057</td></tr><tr><td>St Dev</td><td>71</td><td>1,832</td><td>1,814</td><td>543</td><td>1,889</td></tr><tr><td>CV</td><td>0.03</td><td>0.94</td><td>0.39</td><td>0.07</td><td>0.16</td></tr><tr><td rowspan="2">Strategy</td><td rowspan="2"></td><td colspan="5">Case 2</td></tr><tr><td>Inv. Holding Cost</td><td>Lost Sales Cost</td><td>Total Inv. Cost</td><td>Transp. Cost</td><td>Total Cost</td></tr><tr><td rowspan="3">BENCH1</td><td>Mean</td><td>2,232</td><td>13,941</td><td>16,173</td><td>3,398</td><td>19,571</td></tr><tr><td>St Dev</td><td>122</td><td>8,261</td><td>8,195</td><td>303</td><td>8,219</td></tr><tr><td>CV</td><td>0.05</td><td>0.59</td><td>0.51</td><td>0.09</td><td>0.42</td></tr><tr><td rowspan="3">MUN</td><td>Mean</td><td>2,617</td><td>2,381</td><td>4,997</td><td>5,639</td><td>10,636</td></tr><tr><td>St Dev</td><td>132</td><td>2,314</td><td>2,324</td><td>711</td><td>2,297</td></tr><tr><td>CV</td><td>0.05</td><td>0.97</td><td>0.47</td><td>0.13</td><td>0.22</td></tr><tr><td rowspan="3">RTC</td><td>Mean</td><td>2,926</td><td>3,228</td><td>6,154</td><td>4,816</td><td>10,970</td></tr><tr><td>St Dev</td><td>130</td><td>3,391</td><td>3,354</td><td>486</td><td>3,479</td></tr><tr><td>CV</td><td>0.04</td><td>1.05</td><td>0.54</td><td>0.10</td><td>0.32</td></tr><tr><td rowspan="3">RDE</td><td>Mean</td><td>2,616</td><td>2,712</td><td>5,328</td><td>4,683</td><td>10,011</td></tr><tr><td>St Dev</td><td>74</td><td>2,434</td><td>2,426</td><td>759</td><td>2,389</td></tr><tr><td>CV</td><td>0.03</td><td>0.90</td><td>0.46</td><td>0.16</td><td>0.24</td></tr><tr><td rowspan="3">RDE+div</td><td>Mean</td><td>2,669</td><td>1,805</td><td>4,474</td><td>4,667</td><td>9,142</td></tr><tr><td>St Dev</td><td>78</td><td>1,884</td><td>1,861</td><td>604</td><td>2,051</td></tr><tr><td>CV</td><td>0.03</td><td>1.04</td><td>0.42</td><td>0.13</td><td>0.22</td></tr><tr><td rowspan="2">Strategy</td><td rowspan="2"></td><td colspan="5">Case 3</td></tr><tr><td>Inv. Holding Cost</td><td>Lost Sales Cost</td><td>Total Inv. Cost</td><td>Transp. Cost</td><td>Total Cost</td></tr><tr><td rowspan="3">BENCH1</td><td>Mean</td><td>2,168</td><td>14,369</td><td>16,537</td><td>3,766</td><td>20,303</td></tr><tr><td>St Dev</td><td>97</td><td>7,092</td><td>7,049</td><td>289</td><td>7,109</td></tr><tr><td>CV</td><td>0.04</td><td>0.49</td><td>0.43</td><td>0.08</td><td>0.35</td></tr><tr><td rowspan="3">MUN</td><td>Mean</td><td>2,711</td><td>1,360</td><td>4,071</td><td>6,624</td><td>10,695</td></tr><tr><td>St Dev</td><td>136</td><td>1,965</td><td>1,967</td><td>792</td><td>2,176</td></tr><tr><td>CV</td><td>0.05</td><td>1.44</td><td>0.48</td><td>0.12</td><td>0.20</td></tr><tr><td rowspan="3">RTC</td><td>Mean</td><td>2,917</td><td>2,907</td><td>5,824</td><td>5,410</td><td>11,235</td></tr><tr><td>St Dev</td><td>121</td><td>4,036</td><td>4,015</td><td>386</td><td>4,119</td></tr><tr><td>CV</td><td>0.04</td><td>1.39</td><td>0.69</td><td>0.07</td><td>0.37</td></tr><tr><td rowspan="3">RDE</td><td>Mean</td><td>2,668</td><td>2,066</td><td>4,734</td><td>5,480</td><td>10,214</td></tr><tr><td>St Dev</td><td>78</td><td>2,432</td><td>2,423</td><td>650</td><td>2,565</td></tr><tr><td>CV</td><td>0.03</td><td>1.18</td><td>0.51</td><td>0.12</td><td>0.25</td></tr><tr><td rowspan="3">RDE+div</td><td>Mean</td><td>2,710</td><td>1,175</td><td>3,886</td><td>5,405</td><td>9,291</td></tr><tr><td>St Dev</td><td>69</td><td>1,753</td><td>1,732</td><td>744</td><td>2,099</td></tr><tr><td>CV</td><td>0.03</td><td>1.49</td><td>0.45</td><td>0.14</td><td>0.23</td></tr></table>

Results in [\$/week]

30 replication with common random numbers

# On Optimizing Production Nodes in Supply Chain Systems

Davide Giglio<sup>1</sup>, Riccardo Minciardi<sup>2</sup>, Simona Sacone<sup>3</sup>, and Silvia Siri<sup>4</sup>

1 Department of Communications, Computers and Systems Science, University of Genova, Italy davide.giglio@unige.it

2 Department of Communications, Computers and Systems Science, University of Genova, Italy riccardo.minciardi@unige.it

3 Department of Communications, Computers and Systems Science, University of Genova, Italy simona.sacone@unige.it

4 Department of Communications, Computers and Systems Science, University of Genova, Italy silvia.siri@unige.it

**Summary.** In this chapter a supply chain system is considered, focusing in particular on a single production node. For the single node we propose a hybrid model that combines a continuous-time dynamics, associated with the production process, with a discrete-event dynamics, related to arrivals of raw materials and departures of finite products. The system state variables are given by the inventory levels of raw materials and finite products, while the decisions to be taken concern the arrival process (in terms of number of orders, quantities and ordering time instants), the production process (definition of the production function) and the departure process (determination of the delivery time instants). The resulting optimiza tion problem is nonlinear and functional and it is decomposed into two subproblems that are studied separately (the former is related to the production and the delivery process, the latter concerns the replenishment policy). Some properties of the optimal solution of these subproblems are shown and, in some cases, the optimal control strategies are found. In the final part of the chapter, the proposed optimization approach is extended to consider the case of multi-site schemes, by introducing two simple cases of cooperative and competitive structures.

**Key words:** Supply chain systems, Hybrid model, Optimization, Replenishment problem

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">L. Bertazzi et al. (eds.), Innovations in Distribution Logistics, Lecture Notes in Economics and Mathematical Systems 619, DOI: 10.1007/978-3-540-92944-4,</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">-c 2009 Springer-Verlag Berlin Heidelberg</span></small>

## 1 Introduction

Analysis, planning and control of distributive logistic systems represent nowadays a major research field, which has aroused great interest of companies as well. Actually, because of the ever increasing competition, companies must always be efficient and productive, with ambitious objectives such as maximizing service levels, complying with required due-dates, minimizing inventory levels at each stage of the network, minimizing transportation and infrastructure costs. For this reason, the integration of production, distribution and inventory management results to be a crucial aspect to be considered. In this context, different groups of researchers have devoted their attention to the design, analysis, optimization and management of distributed production systems, in order to define optimal decisions or coordination schemes for the different decision makers acting in such networks. All these aspects are summarized in the common expression supply chain management, which emphasizes the view of the company as a part of a chain composed of different stages, such as suppliers, manufacturers, assemblers, warehouses, customers [1, 2, 3].

From a modelling point of view, a supply chain can be represented in different ways, corresponding to centralized or decentralized structures, to analytical or simulation models, and so on. For the single node of a distributed production system, an important distinction is between continuous-time models and discrete-event models: in the former case, models are referred to as fluid models, in which all the quantities are represented by means of continuous variables; in the latter case, the whole system dynamics is driven by the occurring of asynchronous events which usually change the values of system state variables. Many continuous-time models have been developed for representing production systems. Among them, an important research stream consists in the determination of analytical solutions for production systems that have to meet a random demand [4, 5, 6]. Other works are relative to multi-inventory systems in which demand is supposed to be unknown but generally bounded and the proposed control schemes are aimed at defining appropriate inventory levels in order to meet such demand [7, 8]. On the other hand, discrete-event models are generally suited for representing real case studies with a high level of detail or for comparing different scenarios characterized by the presence of stochastic aspects, for which an analytical evaluation is too difficult. In [9] a discrete-event simulation model is used for an integrated product supply chain system, where different decision makers act and real-time information is provided. In [10] a simulation-based optimization framework involving simultaneous perturbation stochastic approximation is developed for supply chain systems.

The objective of the present work is the definition of a model for a single node of a supply chain and the statement and solution of a relative optimization problem. The ultimate objective of our research work consists in studying the behaviour of a supply chain system, by defining some coordination mechanisms among the different nodes of the network; as a consequence, each node needs to be analytically represented at a quite aggregate level of detail. Moreover, in our model, we want to focus on the interactions among the different nodes; this means that for each production node the process of raw material arrivals and finite product departures must be represented in detail. For all these reasons, the model that we have defined integrates some aspects of continuous-time models with other aspects of discrete-event approaches. On one hand, fluid models generally allow to determine closed-loop solutions (that is, solutions expressed as functions of the current system state) for planning/control problems, while they normally do not represent in detail the interactions with external entities (such as arrivals and departures of parts). On the other hand, discrete-event models can describe a supply chain system with a high level of detail, managing stochastic aspects as well, but they do not allow the definition of analytical solutions. Since our objective is that of defining an analytical approach for a single production node interacting with other nodes in a supply chain, the resulting model we propose is a hybrid model combining a continuous dynamics (corresponding to the production process) with discrete-event processes (representing the arrivals of raw materials and departures of finite products).

In this work, we propose an optimization procedure based on this hybrid model, acting at a tactical/operational decision level and being relevant to the minimization of order costs, inventory costs and costs due to deviations from the external demand; decisions concern the process of raw material arrivals, the process of finite product deliveries and the production effort. The resulting optimization problem is hard to be solved and, then,it is decomposed into two subproblems. The former subproblem refers to the determination of the optimal production effort and the optimal product departure process, whereas the latter subproblem corresponds to the determination of the optimal replenishment policy. The overall optimization problem and its decomposition have already been presented in [11, 12, 13, 14], where only the first subproblem has been fully described and dealt with. One of the main novelties of the present work is a detailed analysis of the second subproblem (which has been defined in [15]) and, thus, the definition of a solution procedure for the overall optimization problem.

As a further innovative aspect, in this work some basic multi-site structures are considered, which exploit the solution procedure determined for the single nodes of a supply chain. Generally speaking, if a supply chain is represented as a decentralized structure, several decision agents are considered, each one provided with its own information set, giving rise to either a cooperative or a competitive environment. In the case of cooperation among different agents, the main aspect to consider is the way in which the coordination of the various decisional entities may be achieved. On the contrary, in the case of competition, the decisional agents are provided not only with different information sets, but also with individual performance objectives. In this work, two simple schemes are presented: a competitive environment of two parallel producers which compete for serving a customer and a cooperative framework of two producers belonging to subsequent stages in the supply chain.

The paper is organized as follows. In Sect. 2 the proposed model and optimization problem for a production node in a supply chain system is defined. The decomposition of the optimization problem into two subproblems is also discussed in the same section. Sections 3 and 4 are devoted to the statement and solution of the first and second subproblem, respectively. Some simple multi-site structures are discussed in Sect. 5, where the described optimization procedure is adopted and exploited by different decision agents in the network.

## 2 The Optimization Problem for a Single Node in a Supply Chain

A single node of a supply chain is here modeled as a production center, where raw parts arriving from suppliers (or from previous nodes in the chain) are manufactured and immediately transformed into final products, without considering any assembly operation. More specifically, each part entering the single node is supposed to be processed by a single operation and, then, it is transformed into one product. A schematization of this model is represented in Fig. 1, where the two inventories refer to raw materials and final products, respectively; the corresponding inventory levels at time t are indicated with variables $\xi ( t )$ and x(t).

![](images/page_156_image_5.jpg)

Fig. 1. Schematization of the production node

As previously specified in the Introduction, the proposed model is a hybrid model, which combines a continuous-time dynamics, related to the production process, together with a discrete-event dynamics, associated with arrivals of raw materials and departures of finite products. The production process is represented by a production effort k(t), which models the portion of the overall work-capacity K assigned to the production at time t. On the other hand, arrivals of raw materials and departures of finite products are modelled as discrete-event processes, in which the events (arrivals and departures) are not equally spaced in time. In particular, in the arrival process, Γ is the number of raw material arrivals, within the considered time horizon, $\delta _ { i } , i = 1 , \ldots , \varGamma ,$ is the time instant at which the i-th arrival takes place, and $\theta _ { i } , i = 1 , \ldots , \varGamma ,$ is the amount of raw materials entering the node at time instant $\delta _ { i } ,$ that is the i-th ordered quantity (Fig. 2). In an analogous way, the flow of products delivered to clients is represented as a finite sequence of departures (Fig. 3), characterized by the following quantities: N, that is the number of finite products requests, within the considered time horizon, $t _ { i } ,   i = 1 , \ldots , N ,$ that is the time instant at which the i-th departure of finite products occurs, $Q _ { i } ,   i   =   1 , \ldots , N ,$ that is the amount of finite products leaving the system at time instant $t _ { i } .$ . Moreover, the external demand is characterized by the due-date of the i-th departure of finite products (i.e., the i-th lot), namely $t _ { i } ^ { * } , i = 1 , \ldots , N .$ It is assumed that the required quantities in the external demand are satisfied and then they correspond to $Q _ { i }$

![](images/page_157_chart_2.jpg)

Fig. 2. The arrival of raw materials

![](images/page_157_chart_4.jpg)

Fig. 3. The delivery of finite products

The system state variables are inventory levels $\xi ( t )$ and $x ( t )$ , whereas decisions concern the following issues:

• The arrival process, i.e., how many orders to place (Γ), the ordering time instants $( \delta _ { i } ,   i = 1 , \ldots , \varGamma )$ , and the quantities to order $( \theta _ { i } ,   i = 1 , \ldots , \varGamma )$

• The production process, corresponding to the function $k ( t ) , 0 \leq t \leq t _ { N } ;$

• The departure process, i.e., the delivering time instants for each lot of finite products $( t _ { i } ,   i = 1 , \ldots , N )$

Taking into account the asynchronous time instants which characterize the arrival and the departure processes, the state equations of the proposed single node model can be written, for the raw material inventory and for the finite product inventory, respectively, as

$$
\xi (\delta_ {i + 1}) = \xi (\delta_ {i}) - \int_ {\delta_ {i}} ^ {\delta_ {i + 1}} k (t) \mathrm{d} t + \Theta_ {i + 1} \quad i = 0, \dots , \Gamma - 1\tag{1}
$$

$$
x (t _ {i + 1}) = x (t _ {i}) + \int_ {t _ {i}} ^ {t _ {i + 1}} k (t) \mathrm{d} t - Q _ {i + 1} \quad i = 0, \dots , N - 1\tag{2}
$$

where $\delta _ { 0 } = 0 , t _ { 0 } = 0$ , and $\xi ( 0 )$ and $x ( 0 )$ are given initial inventory levels.

The proposed optimization takes into account the order cost $C ^ { o }$ due to the acquisition of raw materials from suppliers, the cost $C ^ { I }$ relevant to the inventory occupancy, and the cost $C ^ { T }$ relevant to the deviations from the due-dates, stated, respectively, as in the following

$$
\left| C ^ {O} = \sum_ {i = 1} ^ {\Gamma} \left(c _ {f} + c _ {v} \Theta_ {i}\right) \right|\tag{3}
$$

$$
C ^ {I} = H _ {\xi} \int_ {0} ^ {\delta_ {F}} \xi (t) \mathrm{d} t + H _ {x} \int_ {0} ^ {t _ {N}} x (t) \mathrm{d} t\tag{4}
$$

$$
\left| \mathcal {C} ^ {T} = \alpha \sum_ {i = 1} ^ {N} (t _ {i} - t _ {i} ^ {*}) ^ {2} \right|\tag{5}
$$

where $c _ { f }$ and $c _ { \nu }$ are the fixed and variable unitary order costs, respectively, $H _ { \xi }$ and $H _ { x }$ are the unitary inventory costs for raw materials and finite products, respectively, while α is a suitable parameter, weighing the deviation of the delivering times from the corresponding due-dates. As regards the expression of cost term $C ^ { T }$ , note that early and late deliveries are equally penalized. Every deviation from the corresponding due-date yields a decrease of the node service level, which results to be a crucial performance indicator in a supply chain system. This is the reason why a quadratic form of the cost has been chosen, aiming at strongly penalizing deviations from duedates.

The overall optimization problem can then be stated as follows.

**Problem 1.** Given the initial conditions $\delta _ { 0 } = 0 , t _ { 0 } = 0 , \xi ( 0 ) \geq 0$ , and $x ( 0 ) \geq 0$ , find

$$
\min_{\substack{\Gamma ,  \delta_{i},\Theta_{i},i = 1,\ldots ,\Gamma \\ t_{i},i = 1,\ldots ,N\\ k(t),  0\leq i\leq t_{IN}}}C_{1} = C^{O} + C^{I} + C^{T}
$$

subject to (1), (2), and

$$
0 \leq k (t) \leq K \quad 0 \leq t \leq t _ {N}\tag{6}
$$

$$
\delta_ {i + 1} > \delta_ {i} \quad i = 0, \dots , \Gamma - 1\tag{7}
$$

$$
t _ {i + 1} > t _ {i} \quad i = 0, \dots , N - 1\tag{8}
$$

$$
\xi (t) \geq 0 \quad \quad 0 <   t \leq \delta_ {\Gamma}\tag{9}
$$

$$
x (t) \geq 0 \quad 0 <   t \leq t _ {N}\tag{10}
$$

$$
\Theta_ {i} > 0 \quad i = 1, \dots , \Gamma\tag{11}
$$

Problem 1 is a nonlinear functional optimization problem, thus a simplified version of this problem is needed. The heuristic approach proposed here is that of decomposing it into two subproblems (of course, this decomposition approach leads to a sub-optimal solution of Problem 1):

1. The first subproblem consists in minimizing the inventory cost for final products and the deviations from due-dates; the decision variables regard the production effort $( k ( t ) , 0 \leq t \leq t _ { N } )$ and the departure process $( t _ { i } , \; i = 1 , \ldots , N )$ , assuming to have unlimited available raw materials;

2. The second subproblem is relevant to the minimization of the inventory cost for raw materials and order costs; the decision variables are associated with the arrival process $( T , \delta _ { i }$ and $\theta _ { i } , i = 1 , \ldots , \varGamma )$ , with the fixed production effort coming as a solution of the first subproblem.

By defining

$$
C _ {2} = H _ {x} \int_ {0} ^ {t _ {N}} x (t) d t + \alpha \sum_ {i = 1} ^ {N} (t _ {i} - t _ {i} ^ {*}) ^ {2}\tag{12}
$$

$$
\left| \mathcal {C} _ {3} = \sum_ {i = 1} ^ {\Gamma} \left(c _ {f} + c _ {v} \Theta_ {i}\right) + H _ {\xi} \int_ {0} ^ {\delta_ {r}} \xi (t) d t \right|\tag{13}
$$

the first and the second subproblem can be stated, respectively, as follows.

**Problem 2.** Given the initial conditions $t _ { 0 } = 0$ and $x ( 0 ) \geq 0$ , find

$$
\min_{\substack{t_{i},i = 1,\dots ,N\\ k(t),0\leq i\leq n}}\mathcal{C}_{2}
$$

subject to (2), (6), (8) and (10).

**Problem 3.** Given the initial conditions $\delta _ { 0 } = 0$ and $\xi ( 0 ) \geq 0 ,$ , and given $k ( t ) = k ^ { o } ( t )$ solution of Problem 2, find

$$
\min _ {\Gamma , \delta_ {i}, \Theta_ {i}, i = 1, \dots , \Gamma} \mathcal {C} _ {3}
$$

subject to (1), (7), (9), and (11).

Note that Problem 2 still is a functional optimization problem, while Problem 3 is a parametric optimization problem. In the following, these two problems will be studied, in order to find some properties of their optimal solutions and, thus, to define solution procedures for the two problems. Problem 2 will be analysed in Sect. 3, whereas Problem 3 will be studied in Sect. 4.

## 3 Solution of Problem 2

In this section, Problem 2 is analysed and some fundamental results about the optimal solution of the problem will be reported. The proofs of the theorems are only sketched in the present section, whereas their complete version can be found in [14].

As previously pointed out, Problem 2 is a functional optimization problem, as a function $k ( t )$ has to be determined over the considered optimization interval. A first simple result can be provided, in order to convert Problem 2 into a more tractable (parametric) optimization problem. Note that, in the following, $k ^ { \circ } ( t )$ refer to the optimal pattern of the decision variable $k ( t )$

**Proposition 1.** In the optimal solution of Problem 2, the function $k ( t )$ is such that in each time interval between two subsequent delivery instants, $e . g . , \; ( t _ { i } , t _ { i + 1 } ]$ , the following conditions hold

$$
k ^ {\circ} (t) \equiv 0, \quad t _ {i} <   t <   t _ {i} + \tau_ {i}, \quad i = 0, \dots , N - 1\tag{14}
$$

$$
k ^ {\circ} (t) \equiv K, \quad t _ {i} + \tau_ {i} <   t \leq t _ {i + 1}, \quad i = 0, \dots , N - 1\tag{15}
$$

for some $\tau _ { i }$ such that $0 \leq \tau _ { i } \leq t _ { i + 1 } - t _ { i } .$ . Note that the value $k ^ { \circ } ( t _ { i }   +   \tau _ { i } )$ is irrelevant, and thus it is not necessary to precise it in the statement of the proposition; it is possible to set either $k ^ { \circ } ( t _ { i } + \tau _ { i } ) = 0 \; o r \; k ^ { \circ } ( t _ { i } + \tau _ { i } ) = K ,$ , indifferently.

Proof. Suppose, ab absurdo, that an optimal solution of Problem 2 exists that does not satisfy conditions (14), (15). This implies that a time interval $\tau _ { i }$ such that $0 \leq$ $\tau _ { i } \leq t _ { i + 1 } - t _ { i }$ exists, where one or both of the following conditions hold:

(a) there is an interval $( t _ { i } + \tau _ { i } , t _ { i + 1 } )$ of nonzero length in which the value of $k ( t )$ is not constantly its maximum value, that is,

$$
k (t) \not \equiv K, \quad t _ {i} + \tau_ {i} <   t \leq t _ {i + 1}
$$

with $\tau _ { i } < t _ { i + 1 } - t _ { i }$

(b) there are some intervals (at least one) of nonzero length, preceding time instant $t _ { i } + \tau _ { i }$ , in which the value of $k ( t )$ is not identically zero, that is,

$$
k (t) \not \equiv 0, \quad \overline {{t}} _ {i} <   t <   \overline {{\overline {{t}} _ {i}}}
$$

with $t _ { i } \leq \overline { { t } } _ { i } < \overline { { \overline { { t } } } } _ { i } \leq t _ { i } + \tau _ { i }$

Then, in case condition (a) occurs, it is immediate to understand that a new solution can be obtained by “reducing” the length of the interval $( t _ { i } + \tau _ { i } , t _ { i + 1 } )$ , and imposing that in such interval the production effort is at its maximum value, i.e.,

$$
k (t) \equiv K, \quad t _ {i} + \tau_ {i} ^ {\prime} <   t \leq t _ {i + 1}
$$

being $\tau _ { i } ^ { \prime } > \tau _ { i } ,$ and $\begin{array} { r } { \int _ { t _ { i } + \tau _ { i } } ^ { t _ { i } + 1 } k ( t )   \mathrm { d } t = \int _ { t _ { i } + \tau _ { i } ^ { \prime } } ^ { t _ { i } + 1 } k ( t )   \mathrm { c } } \end{array}$ dt.

Evidently, this new solution is characterized by the same value of cost $C ^ { T }$ , but it has a lower value of cost $C ^ { I }$ , then the original solution cannot be optimal.

Similar considerations apply in connection with condition b), or even with reference to the combination of the two conditions. 

The result provided by Proposition 1 allows to convert the functional optimization problem into a parametric one, by restricting the search for optimal solutions of Problem 2 to those characterized by functions $k ( t )$ satisfying conditions (14), (15). Thus, it is possible to define

$\tau _ { i } , \; i = 0 , \ldots , N - 1$ , that represents the (nonnegative) idle time between $t _ { i }$ and $t _ { i + 1 } ;$

$T _ { i } , ~ i = 0 , \ldots , N - 1$ , that is the (nonnegative) production time between $t _ { i }$ and $t _ { i + 1 }$

Thanks to Proposition 1, Problem 2 can also be stated as a multistage optimal control problem. First of all, the following assumptions will be made concerning the parameters characterizing Problem 1:

• The initial inventory level is all consumed to satisfy the first order, that is

$$
x (0) <   Q _ {1}\tag{16}
$$

This assumption is not restrictive since, if this condition is not verified, in the optimal solution of Problem 2 no production is realized $( T _ { i }   =   0 )$ for a certain number of orders starting from the first one; then, the beginning of the sequence of orders can be simply shifted onward till meeting condition (16);

• The two terms of cost function $C _ { 2 }$ are “well balanced”, that is the inventory cost has not a prevailing effect with respect to the deviation cost from due-dates; this corresponds to suppose that

$$
H _ {x} K <   \alpha\tag{17}
$$

If such a condition were not fulfilled, then the optimization problem would be of poor interest.

Taking into account Proposition 1 and on the basis of the above considerations, cost function $C _ { 2 }$ can now be written as

$$
\mathcal {C} _ {4} = H _ {x} \sum_ {i = 0} ^ {N - 1} \left(x (t _ {i}) (\tau_ {i} + T _ {i}) + \frac {K T _ {i} ^ {2}}{2}\right) + \alpha \sum_ {i = 0} ^ {N - 1} \left(\tau_ {i} + T _ {i} + t _ {i} - t _ {i + 1} ^ {*}\right) ^ {2}\tag{18}
$$

Furthermore, the state equation (2) and the time instants $t _ { i } ,   i = 1 , \ldots , N$ can be expressed, respectively, as

$$
x (t _ {i}) = x (t _ {i - 1}) + K T _ {i - 1} - Q _ {i} \quad i = 1, \dots , N\tag{19}
$$

$$
t _ {i} = t _ {i - 1} + \tau_ {i - 1} + T _ {i - 1} \quad i = 1, \dots , N\tag{20}
$$

On these bases, Problem 2 can be re-stated as follows.

**Problem 4.** Given the initial conditions $t _ { 0 } = 0$ and $x ( 0 ) \geq 0$ , find

$$
\min _ {\tau_ {i}, T _ {i}, i = 0, \dots , N - 1} C _ {4}
$$

where $C _ { 4 }$ is given by (18), subject to (19), (20) and

$$
T _ {i} \geq 0 \quad i = 0, \dots , N - 1\tag{21}
$$

$$
\tau_ {i} \geq 0 \quad i = 0, \dots , N - 1\tag{22}
$$

$$
x (t _ {i}) \geq 0 \quad i = 1, \dots , N\tag{23}
$$

It is apparent that Problem 4 is structured into N stages, being $x ( t _ { i } )$ and $t _ { i }$ the state variables at stage $i , \tau _ { i - 1 }$ and $T _ { i - 1 }$ the control variables acting at the same stage. Obviously, Problem 4 can be also viewed as a mathematical programming problem with non linear objective and non linear constraints. It can be solved by mathematical programming solvers, yielding the optimal control law in an open-loop form for a specific value of the initial conditions. In this work, instead, we are interested in adopting optimal control strategies defined as functions of the system state, that is, solutions typically denoted as closed-loop ones. Then, we will find the solution of Problem 4 as a set of optimal feedback control strategies. In order to do that, it is first of all necessary to discuss some significant properties of the optimal solution of Problem 4. Note that in the following propositions the values $T _ { i } ^ { \circ }$ and $\tau _ { i } ^ { \circ } ,   i   =$ $0 , \ldots , N - 1$ , refer to the optimal values of the decision variables $T _ { i }$ and $\tau _ { i } ,   i   =$ $0 , \ldots , N - 1$ , respectively.

**Proposition 2.** In the optimal solution of Problem 4, the decision variable $T _ { i }$ is always positive, that is

$$
T _ {i} ^ {\circ} > 0 \quad i = 0, \dots , N - 1\tag{24}
$$

Proof. The value of the inventory level just after the generic delivery time instant $t _ { i }$ is given by

$$
x (t _ {i}) = x (t _ {i - 1}) + K T _ {i - 1} - Q _ {i} \geq 0, \quad i = 1, \dots , N\tag{25}
$$

Note that, in an optimal solution of Problem 4, the inequality $x ( t _ { i - 1 } )   <   Q _ { i }$ must hold. In fact, if $x ( t _ { i - 1 } )$ were greater or equal to $Q _ { i }$ , this would imply that the whole quantity of products required at the delivery time $t _ { i }$ has been manufactured during the time intervals preceding $t _ { i - 1 }$ (remember also that condition (16) prevents the initial inventory contents from being still partially available after the first delivery time instant). But, due to the structure of the cost function (including the inventory cost), this is never convenient since it makes the cost function value increase without providing any advantage. Then, some part of the required quantity $Q _ { i }$ has to be produced just during time interval $( t _ { i - 1 } , t _ { i } )$ , that is, $x ( t _ { i - 1 } ) < \mathcal { Q } _ { i }$ , as above claimed. Thus, by taking into account (25), condition $T _ { i - 1 } ^ { \circ } > 0 ,   i = 1 , \ldots , N$ , is proved.

**Proposition 3.** In the optimal solution of Problem 4, $\mathit { i f } \tau _ { i } > 0 \mathit { f o r }$ some $i \in \{ 1 , \ldots , N -$ 1}, that is, if the i-th time interval $( t _ { i } , t _ { i + 1 } )$ includes a nonzero idle time, then the inventory level $x ( t _ { i } )$ (that is, just after the delivery at time instant $t _ { i } )$ is zero.

Proof. Suppose, ab absurdo, $x ( t _ { i } ) = \bar { x } > 0$ and $\tau _ { i } \; > \; 0 ,$ , in an optimal solution. Products corresponding to this inventory level $x ( t _ { i } )$ have been realised in time interval $( t _ { i - 1 } , t _ { i } )$ or in previous time intervals, and they cannot be part of the initial inventory that is all consumed, by assumption, to satisfy the first order. These products are not necessary for order deliveries realised in $t _ { i }$ or before and certainly they are not all necessary for order deliveries after $t _ { i } ,$ owing to condition $\tau _ { i } > 0$ . This implies that a solution with $\tau _ { i } > 0$ and $x ( t _ { i } ) = \bar { \bar { x } }$ such that $0 \leq \bar { \bar { x } } < \bar { x }$ is feasible and guarantees the same deliveries in the same time instants (thus yielding the same value of cost $C ^ { T } )$ but with a lower value of the inventory cost $C ^ { I }$ . This proves that any solution with $\tau _ { i } > 0$ and $x ( t _ { i } ) > 0$ cannot be optimal.

![](images/page_163_chart_5.jpg)

Fig. 4. Behaviour of the state variable x(t) in the optimal solution

On the basis of the above propositions, it turns out that the behaviour of the state variable $x ( t )$ in the optimal solution is of the type represented in Fig. 4. Note that the overall sequence of time intervals can be decomposed into a set of $S ~ ( 1 \leq$ $S \leq N )$ subsequences of time intervals in which the resource works at the maximum production effort, except in a portion of the first time interval of the subsequence for which $k ( t ) \: = \: 0 , \: t _ { i } \: \leq \: t \: \leq \: t _ { i } \: + \: \tau _ { i }$ , being $\tau _ { i }   >   0$ . Note also that, save the first time interval $( t _ { 0 } , t _ { 1 } )$ (which may include, for the possible presence of a nonzero initial inventory level, a time interval in which $k ( t ) = 0$ with a nonzero inventory level), for all subsequent idle intervals the inventory level must be equal to zero, as represented in Fig. 4.

For notational purposes, still referring to an optimal solution of Problem 4, a set $\varXi$ is defined, gathering the indexes corresponding to the beginning of the different subsequences, namely:

$$
\Xi = \{\sigma_ {j}, j = 1, \dots , S \}\tag{26}
$$

where $\sigma _ { 1 } = 0$ and obviously $\tau _ { \sigma _ { j } } > 0 , j = 2 , \ldots , S$ , by definition of the set $\varXi .$

The S subsequences correspond to $\{ \sigma _ { 1 } , \ldots , \sigma _ { 2 } - 1 \} , \{ \sigma _ { 2 } , \ldots , \sigma _ { 3 } - 1 \} , \ldots , \{ \sigma _ { S } , \ldots ,$ $\sigma _ { S + 1 } - 1 \}$ . Moreover, for the sake of notational convenience, define $\sigma _ { S + 1 }   =   N .$ For instance, in the example reported in Fig. 4, it turns out $S = 3 , \varXi = \{ 0 , 1 , 4 \}$ and the three subsequences are defined as {0}, {1, 2, 3}, {4}.

Note that the decomposition of the overall optimization horizon into S subsequences of time intervals allow to decompose the problem of finding the optimal control strategies at each stage i, $i = 0 , \ldots , N - 1$ , into S independent control problems, each conditioned by the initial values, $\mathrm{i.e.,} \quad t_{\sigma_j}, x(t_{\sigma_j}), j = 1, \ldots, S$ . In order to find the optimal solution of Problem 4 it is then necessary to first solve the problem by mathematical programming to find the positive idle times, hence the set $\varXi$ . Once known this set $\varXi ,$ optimal strategies for each subsequence are derived, as explained in the following.

For the sake of simplicity, from now on, the weights appearing in the cost function will be expressed in a more compact form, introducing the term $\gamma \; = \; \alpha \backslash H _ { x }$ Condition (17) then yields:

$$
K <   \gamma\tag{27}
$$

**Theorem 1.** Consider a generic j-th subsequence composed of $\rho > 1$ orders (with $\boldsymbol { o } = \sigma _ { j + 1 }   -   \overline { { \sigma _ { j } } } \big )$ , the optimal solution at each stage of the subsequence is the following.

Case 1) For the first stage of the subsequence, that is stage $( i - 1 ) = \sigma _ { j } { : }$

• if the inventory level at the end of stage $( i - 1 )$ is positive:

$$
T _ {i - 1} ^ {\circ} = t _ {i} ^ {*} - \frac {1}{\nu + 1} C _ {i + 1} - \frac {(\nu + 2) K - 2 (\nu + 1) \gamma}{2 (\nu + 1) \gamma K} Q _ {i} + \frac {K - 2 (\nu + 1) \gamma}{2 (\nu + 1) \gamma K} x (t _ {i - 1})\tag{28}
$$

$$
\tau_ {i - 1} ^ {\circ} = \frac {1}{\nu + 1} C _ {i + 1} - t _ {i - 1} + \frac {K - 2 (\nu + 1) \gamma}{2 (\nu + 1) \gamma K} Q _ {i} - \frac {K - 2 (\nu + 1) \gamma}{2 (\nu + 1) \gamma K} x (t _ {i - 1})\tag{29}
$$

• if the inventory level at the end of stage (i − 1) is zero:

$$
T _ {i - 1} ^ {\circ} = \frac {Q _ {i} - x (t _ {i - 1})}{K}\tag{30}
$$

$$
\tau_ {i - 1} ^ {\circ} = \frac {1}{\nu + 1} t _ {i} ^ {*} + \frac {1}{\nu + 1} C _ {i + 1} - t _ {i - 1} - \frac {Q _ {i}}{K} - \frac {K - 2 (\nu + 1) \gamma}{2 (\nu + 1) \gamma K} x (t _ {i - 1})\tag{31}
$$

where ν is the total number of stages in the subsequence whose inventory level goes to zero, and the generic constant $C _ { i + 1 }$ is calculated iteratively depending on data of the whole subsequence, following these steps:

• for $i = \sigma _ { j + 1 } .$

$$
C _ {i} = t _ {i} ^ {*} - \frac {Q _ {i}}{K}\tag{32}
$$

• from $i = \sigma _ { j + 1 } - 1$ backward to $i = \sigma _ { j } + 3 .$

– if the inventory level at the end of the stage i is positive:

$$
C _ {i} = C _ {i + 1} - \frac {\nu_ {i} + 1}{K} Q _ {i} + \frac {Q _ {i}}{2 \gamma}\tag{33}
$$

– if the inventory level at the end of the stage i is zero:

$$
C _ {i} = C _ {i + 1} + t _ {i} ^ {*} - \frac {\nu_ {i} + 1}{K} Q _ {i}\tag{34}
$$

where $\nu _ { i }$ is the number of stages whose inventory is equal to zero, from the stage i (included) to the last stage of the subsequence.

Case 2) For the intermediate stage of the subsequence, that is stage $( i - 1 ) = \sigma _ { j } +$ $1 , \ldots , \sigma _ { j + 1 } - 2 ,$ , when $\rho > 2 .$

• if the inventory level at the end of stage (i − 1) is positive:

$$
T _ {i - 1} ^ {\circ} = t _ {i} ^ {*} - t _ {i - 1} - \frac {Q _ {i}}{2 \gamma} \qquad \tau_ {i - 1} ^ {\circ} = 0\tag{35}
$$

• if the inventory level at the end of stage (i − 1) is zero:

$$
T _ {i - 1} ^ {\circ} = \frac {Q _ {i} - x (t _ {i - 1})}{K} \quad \tau_ {i - 1} ^ {\circ} = 0\tag{36}
$$

Case 3) For the last stage of the subsequence, that is stage $( i - 1 ) = \sigma _ { j + 1 } - 1$

$$
T _ {i - 1} ^ {\circ} = \frac {Q _ {i} - x (t _ {i - 1})}{K} \quad \tau_ {i - 1} ^ {\circ} = 0\tag{37}
$$

Sketch of the proof. The results stated in the Theorem have been found applying dynamic programming techniques, starting from the last interval (stage) of a subsequence and proceeding backwards up to the first interval (stage). First of all, the last stage of a subsequence, that is stage $( n - 1 )$ , is considered and the relative problem is stated, as a function of the initial conditions $t _ { n - 1 } , x ( t _ { n - 1 } )$ , and of the decision variables $\tau _ { n - 1 }$ and $T _ { n - 1 }$ . In this case, the optimal values of the decision variables are found, as stated in the Theorem, and the optimal cost-to-go at stage (n − 1) is obtained.

Then, the intermediate stage is considered, but different cases must be analysed. Actually, the intermediate stage can be stage $( n - 2 )$ , or $( n - 3 )$ , or previous stages; thus, each of these stages has been considered, starting from stage $( n - 2 )$ . In this case, the problem is stated adding the cost-to-go at stage $( n - 1 )$ , already computed, and the optimal solutions are found considering first-order Kuhn–Tucker conditions; two cases arise, depending on whether the inventory level at the end of stage $( n - 2 )$ $\mathbf { i . e . , } x ( t _ { n - 1 } )$ , is positive or null. Therefore, two optimal solutions are found and two costs-to-go are determined, corresponding to the two cases. When considering the intermediate stage $( n - 3 )$ , two different problems must be stated according to the behaviour of the optimal solution at stage $( n - 2 )$ (either $x ( t _ { n - 1 } ) > 0$ or $x ( t _ { n - 1 } ) = 0 )$ which correspond to two different costs-to-go. For each of the two problems stated for stage $( n   -   3 )$ two different solutions are found, corresponding to whether $x ( t _ { n - 2 } )$ is positive or null (this means that four different cases are developed for stage $( n - 3 ) )$ . Generalising this approach to a generic intermediate stage of a subsequence, the result stated in the Theorem is proved.

The optimal values of the decision variables for the first stage of a subsequence are computed following the same reasoning line already described for the intermediate stage, since the first stage of the subsequence can be either stage $( n   -   2 )$ , or $( n   -   3 )$ or previous stages, depending on the length of the subsequence. As a matter of fact, the problems to be solved at each stage are the same for the intermediate and the first stage, while the solutions are different because they correspond to different cases of Kuhn–Tucker conditions.

**Theorem 2.** Consider a generic j-th subsequence, composed of $\rho = 1$ orders (with $\boldsymbol { o } = \boldsymbol { \sigma } _ { j + 1 } - \boldsymbol { \sigma } _ { j } )$ , the optimal solution at stage $( i - 1 ) = \sigma _ { j }$ is:

$$
T _ {i - 1} ^ {\circ} = \frac {Q _ {i} - x (t _ {i - 1})}{K}\tag{38}
$$

$$
\tau_ {i - 1} ^ {\circ} = t _ {i} ^ {*} - t _ {i - 1} - \frac {Q _ {i} - x (t _ {i - 1})}{K} - \frac {x (t _ {i - 1})}{2 \gamma}\tag{39}
$$

Sketch of the proof. The previous statement is proved considering the last stage of the subsequence, i.e., stage $( n - 1 )$ , which is both the first and the last stage (since the considered subsequence is composed of 1 order). First-order Kuhn–Tucker conditions are developed and the optimal values of the decision variables are found.

## 4 Solution of Problem 3

Once Problem 4 has been solved, in particular finding the feedback control law, Problem 3 still needs to be studied. As previously described and as it is clear in the statement of Problem 3, the optimal solution of Problem 4 provides some data characterizing Problem 3, related to $k ( t )$ . A major feature of the optimal solution of Problem 4 is the optimal behaviour of the production effort $k ( t )$ that turns out to be either null or equal to its maximum value K, as depicted in Fig. 5. The set of subsequences defined by (26) and identified when solving Problem 4 corresponds to a set of S time intervals during which production is active (and, correspondingly, S idle periods). For the sake of simplicity, quantities $\mu _ { j }$ and $\rho _ { j }$ are introduced and defined as follows:

$$
\mu_ {j} = t _ {\sigma_ {j}} + \tau_ {\sigma_ {j}} ^ {\circ} \quad j = 1, \dots , S\tag{40}
$$

$$
\rho_ {j} = t _ {\sigma_ {j + 1}} \quad j = 1, \dots , S\tag{41}
$$

It is straightforward that

$$
k (t) = \left\{ \begin{array}{l l} 0 & t \in (\rho_ {j - 1}, \mu_ {j} ] \\ K & t \in (\mu_ {j}, \rho_ {j} ] \end{array} \right. \quad j = 1, \dots , S\tag{42}
$$

where $\rho _ { 0 }   =   0$ . The time intervals $( \mu _ { j } , \rho _ { j } ] , j = 1 , \ldots , S$ , will be in the following denoted as production intervals.

![](images/page_167_chart_8.jpg)

Fig. 5. Plot of k(t) in the optimal solution of Problem 2

With the above assumptions and considerations, some important properties of the optimal solution of Problem 3 can now be derived, as provided in the following propositions.

**Proposition 4.** In the optimal solution of Problem 3, no material arrival occurs in the intervals in which $k ( t ) = 0 ,   i . e .$

$$
\delta_ {i} ^ {\circ} \notin (\rho_ {j - 1}, \mu_ {j} ] \quad i = 1, \dots , \Gamma \quad j = 1, \dots , S\tag{43}
$$

Proof. Suppose, ab absurdo, that $\delta _ { i } \in ( \rho _ { j - 1 } , \; \mu _ { j } ]$ in the optimal solution of Problem 3. It is straightforward that a solution with $\delta _ { i } \; = \; \mu _ { j }$ would be feasible (since no production is realized in $( \delta _ { i } , ~ \mu _ { j } ] )$ and it would be also characterized by the same order cost and by a lower inventory cost. This proves that any solution with $\delta _ { i } \in$ $( \rho _ { j - 1 } ,   \mu _ { j } ]$ cannot be optimal.

The above proposition states that it is never convenient to have material arrivals in the time intervals in which production is not active. This fact is actually quite intuitive since it can be easily argued that placing orders in such time intervals would only yield an increased inventory cost. This is actually the same reasoning line that leads to prove the following result.

**Proposition 5.** In the optimal solution of Problem 3, the raw materials arrived at time $\delta _ { i - 1 }$ are all consumed in the production process before the following arrival occurs at $\delta _ { i }$ . This means that

$$
\xi^ {\circ} (\delta_ {i} ^ {-}) = 0 \quad i = 1, \dots , \Gamma\tag{44}
$$

$$
\xi^ {\circ} (\delta_ {i} ^ {+}) = \Theta_ {i} \quad i = 1, \dots , \Gamma\tag{45}
$$

Proof. Suppose, ab absurdo, that in the optimal solution of Problem 3, the inventory level in the time instant $\delta _ { i }$ is positive. It is easy to verify that a solution in which the i-th order is placed in the time instant $\bar { \delta } _ { i } > \delta _ { i }$ (with $\bar { \boldsymbol { \varTheta } } _ { i }   =   \boldsymbol { \varTheta } _ { i } )$ and such that the inventory level in $\bar { \delta } _ { i }$ is equal to zero would be feasible and would guarantee a lower inventory cost (with the same order cost). This proves that any solution in which a generic order is placed when the inventory level is still positive cannot be optimal.

Proposition 4 implies that the inventory level $\xi ( t )$ keeps constant during the time intervals $( \rho _ { j - 1 } ,   \mu _ { j } ] , \; j = 1 , \ldots , S$ , thus yielding

$$
\xi (\mu_ {j}) = \xi (\rho_ {j - 1}) \quad j = 1 \dots , S\tag{46}
$$

Moreover, thanks to Proposition 5, it is possible to state that in the time instant in which the i-th material arrival occurs, the inventory level changes instantaneously from 0 to the ordered quantity $\theta _ { i }$ . A possible behaviour of $\xi ( t )$ is then depicted in Fig. 6.

In the following, some results will be provided concerning a generic production interval $j ,$ for which a cost $C _ { j }$ is considered, made of the fixed order cost and the inventory cost. Actually, the variable order cost (which has been considered in the definition of Problem 3) can be neglected when searching for some properties of the optimal solution of Problem 3. This is motivated by the fact that the variable order cost (obtained as the sum of the ordered quantities $\theta _ { i } ,   i   =   1 , \ldots , \varGamma$ , times a cost term $c _ { \nu } )$ does not depend on the problem decision variables. This fact is due to the following consideration. The decision variables $\theta _ { i } ,   i   =   1 , \ldots , \varGamma ,$ can be derived if the order time instants $\delta _ { i } ,   i = 1 , \ldots , \varGamma$ , are known. The quantity $\theta _ { i }$ to order at each time instant $\delta _ { i }$ must assure that the inventory level $\xi ( t )$ never becomes negative and that it becomes equal to 0 exactly in $\delta _ { i + 1 }$ , as stated in Proposition 5. Thus, supposing to have a null initial inventory level, it must be

![](images/page_169_chart_2.jpg)

Fig. 6. A possible pattern of $\xi ( t )$

$$
\left| \sum_ {j = 1} ^ {S} K (\rho_ {j} - \mu_ {j}) = \sum_ {i = 1} ^ {\Gamma} \Theta_ {i} \right|\tag{47}
$$

The variable order cost

$$
\left| \sum_ {i = 1} ^ {\Gamma} c _ {v} \Theta_ {i} \right|\tag{48}
$$

can be written as

$$
c _ {v} \sum_ {i = 1} ^ {\Gamma} \Theta_ {i} = c _ {v} K \sum_ {j = 1} ^ {S} (\rho_ {j} - \mu_ {j})\tag{49}
$$

thus, it depends only on problem data. For this reason, this cost term will be from now on neglected.

Consider a generic j-th production interval, with an initial inventory $\xi ( \mu _ { j } )$ and a final inventory $\xi ( \rho _ { j } )$ , as depicted in Fig. 7. From now on, we define as $n _ { j }$ the number of orders to be placed in the j-th interval and $\delta _ { j , i } , ~ i = 1 , \ldots , n _ { j }$ , the time instant in which the i-th order is placed in the j-th production interval. Of course, it must be

$$
\left| \sum_ {j = 1} ^ {S} n _ {j} = \Gamma \right|\tag{50}
$$

Analogously, the corresponding ordered quantities will be referred to as $\theta _ { j , i } , \; i =$ $1 , \ldots , n _ { j }$ . With these considerations, in a production interval $j ,$ there are $n _ { j } { + } 1$ reorder periods, whose length is denoted as $\mathcal { A } _ { j , i } , i = 1 , \ldots , n _ { j } + 1$ . In the following proposition, a property relevant to the values of these quantities in the optimal solution is reported.

![](images/page_170_chart_2.jpg)

Fig. 7. ξ(t) in a generic production interval j

**Proposition 6.** In the optimal solution of Problem 3, $i f n _ { j }$ orders $( n _ { j } > 1 )$ are placed within the j-th production interval, then the time intervals between two subsequent order deliveries inside the interval (except the first and the last one) have the same length. The reorder periods are obtained as a function of the initial and final inventory level, $\xi ( \mu _ { j } )$ and $\xi ( \rho _ { j } )$ , and of the number of orders $n _ { j } ,$

Proof. The generic cost $C _ { j }$ associated with the interval j can be written as

$$
C _ {j} = n _ {j} c _ {f} + H _ {\xi} \left[ \frac {1}{2} \varDelta_ {j, 1} \xi (\mu_ {j}) + \sum_ {i = 2} ^ {n _ {j}} \frac {1}{2} K \varDelta_ {j, i} ^ {2} + \frac {1}{2} K \varDelta_ {j, n _ {j} + 1} ^ {2} + \varDelta_ {j, n _ {j} + 1} \xi (\rho_ {j}) \right]\tag{51}
$$

where, thanks to Proposition $5 , \mathcal { A } _ { j , 1 }$ is given by

$$
\Delta_ {j, 1} = \frac {1}{K} \xi (\mu_ {j})\tag{52}
$$

Moreover, variables $\mathcal { A } _ { j , i }$ are related by the following expression

$$
\sum_ {i = 1} ^ {n _ {j} + 1} \Delta_ {j, i} = \rho_ {j} - \mu_ {j}\tag{53}
$$

which, considering (52), becomes

$$
\left| \frac {1}{K} \xi (\mu_ {j}) + \frac {1}{K} \sum_ {i = 2} ^ {n _ {j} + 1} \varDelta_ {j, i} = \rho_ {j} - \mu_ {j} \right|\tag{54}
$$

that can be written as

$$
h _ {j} = \frac {1}{K} \xi (\mu_ {j}) + \frac {1}{K} \sum_ {i = 2} ^ {n _ {j} + 1} \varDelta_ {j, i} - \rho_ {j} + \mu_ {j} = 0\tag{55}
$$

The problem concerning interval $j$ can be stated as follows, being $\mathcal { A } _ { j , i }$ $i =$ $2 , \ldots , n _ { j }   +   1$ the decision variables, while $\xi ( \rho _ { j } ) , \xi ( \mu _ { j } )$ and $n _ { j }$ are considered as known data

$$
\min _ {\Delta_ {j, i}, i = 2, \dots , n _ {j} + 1} C _ {j}
$$

where $C _ { j }$ is given by (51), subject to

$$
h _ {j} = 0\tag{56}
$$

$$
\Delta_ {j, i} > 0 \quad j = 2, \dots , n _ {j} + 1\tag{57}
$$

with $h _ { j }$ defined as in (55).

This problem is a quadratic programming problem, characterized by a quadratic objective function, $n _ { j }$ decision variables and one linear equality constraint. Considering Kuhn–Tucker conditions for this problem, one Lagrangian multiplier, i.e., λ, must be considered, leading to the following equations:

$$
\frac {\partial \mathcal {C} _ {j}}{\varDelta_ {j , i}} + \lambda \frac {\partial h _ {j}}{\varDelta_ {j , i}} = 0 \quad i = 2, \dots , n _ {j} + 1\tag{58}
$$

which become

$$
K \varDelta_ {j, i} + \lambda = 0 \quad \quad i = 2, \dots , n _ {j}\tag{59}
$$

$$
K \varDelta_ {j, n _ {j} + 1} + \xi (\rho_ {j}) + \lambda = 0\tag{60}
$$

These equations, together with the relation (54), let us obtain $\mathcal { A } _ { j , i } ,   i = 2 , \ldots , n _ { j } + 1$ as

$$
\varDelta_ {j, i} = \varDelta_ {j} = \frac {1}{K n _ {j}} \left[ K (\rho_ {j} - \mu_ {j}) + \xi (\rho_ {j}) - \xi (\mu_ {j}) \right] \quad i = 2, \dots , n _ {j}\tag{61}
$$

$$
\Delta_ {j, n _ {j} + 1} = \Delta_ {j} - \frac {1}{K} \xi (\rho_ {j})\tag{62}
$$

![](images/page_172_chart_2.jpg)

Fig. 8. The optimal behaviour of $\xi ( t )$ for the case $n _ { j } = 3$

The result proposed in Proposition 6 implies that, in a given production interval $j ,$ the reorder periods are equal, except the first and the last one. In the following, such intermediate reorder periods will be referred to as $\mathcal { A } _ { j } , j   =   1 , \ldots , S$ (without using $\mathcal { A } _ { j , i } )$ . Moreover, the ordered quantities are the same (an example is provided in Fig. 8 for the case of $n _ { j }   =   3 )$ . Therefore, also the ordered quantities can be simply indexed by $j$ (instead of using the pair $j , i )$ , and will be in the following referred to as $\theta _ { j }$ such that:

$$
\Theta_ {j} = \frac {1}{n _ {j}} \left[ K (\rho_ {j} - \mu_ {j}) + \xi (\rho_ {j}) - \xi (\mu_ {j}) \right]\tag{63}
$$

The statement of Proposition 6 does not consider the case in which $n _ { j } = 1$ , that is when only one order is placed in the j-th production interval. In this case, the reorder periods can be simply derived by remembering the result of Proposition 5 (implying that the inventory level goes to zero before reordering again). As also depicted in Fig. 9, the following relations hold:

$$
\Delta_ {j, 1} = \frac {\xi (\mu_ {j})}{K}\tag{64}
$$

$$
\Delta_ {j, 2} = \rho_ {j} - \mu_ {j} - \frac {\xi (\mu_ {j})}{K}\left. \right]\tag{65}
$$

$$
\Theta_ {j} = K (\rho_ {j} - \mu_ {j}) + \xi (\rho_ {j}) - \xi (\mu_ {j})\tag{66}
$$

The propositions previously reported define some significant properties of the optimal solution of Problem 3. Such properties help in rewriting Problem 3 in a simplified way. For doing this, it is necessary to introduce a binary variable indicating whether in a given production interval any orders are placed or not; to this end, we define $\omega _ { j } \in \{ 0 , 1 \}$ as follows:

$$
\omega_ {j} = \left\{ \begin{array}{l l} 0 & \text {if} \quad n _ {j} = 0 \\ 1 & \text {if} \quad n _ {j} > 0 \end{array} \right. \quad j = 1, \dots , S\tag{67}
$$

Before rewriting Problem 3, it is still necessary to express the inventory cost. Note that such a cost is the area defined by $\xi ( t )$ multiplied by the unitary cost $H _ { \xi }$

![](images/page_173_chart_2.jpg)

Fig. 9. The optimal behaviour of $\xi ( t )$ for the case $n _ { j } = 1$

Such an area is computed by exploiting the geometric properties of $\xi ( t )$ coming from the previous propositions. Two different expressions of the inventory cost in the j-th production interval can be written, depending on whether any orders are placed in a production interval or not. In the former case (corresponding to $\omega _ { j } = 1 )$ , the area defined by $\xi ( t )$ in the production interval j is:

$$
A _ {j} ^ {I} = \frac {1}{2 K} \left[ \xi (\mu_ {j}) \right] ^ {2} + \frac {1}{2} K n _ {j} \varDelta_ {j} ^ {2} - \frac {1}{2 K} \left[ \xi (\rho_ {j}) \right] ^ {2}\tag{68}
$$

On the contrary, if $\omega _ { j } = 0$ , the area defined by $\xi ( t )$ in the production interval j is:

$$
A _ {j} ^ {0} = \frac {1}{2} (\rho_ {j} - \mu_ {j}) \left[ \xi (\mu_ {j}) + \xi (\rho_ {j}) \right]\tag{69}
$$

Moreover, for completing the expression of the inventory cost, it is still necessary to add the term corresponding to a positive inventory level during idle intervals. This is the last term included in the cost function of the following problem which is the new version of Problem 3.

**Problem 5.** Given the initial conditions $\rho _ { 0 } = 0$ and $\xi ( 0 ) = 0$ , find

$$
\min_{\substack{\omega_{j},n_{j},A_{j},\xi (\rho_{j}),\xi (\mu_{j})\\ j = 1,\dots ,S}}c_{f}\sum_{j = 1}^{S}n_{j} + H_{\xi}\sum_{j = 1}^{S}\left[\omega_{j}\cdot A_{j}^{I} + (1 - \omega_{j})\cdot A_{j}^{O}\right] + H_{\xi}\sum_{j = 1}^{S - 1}\left[\xi (\rho_{j})(\mu_{j + 1} - \rho_{j})\right]
$$

where $A _ { j } ^ { 1 }$ is given by (68), ${ \boldsymbol { A } } _ { j } ^ { 0 }$ is given by (69), subject to

$$
\xi (\mu_ {j}) = \xi (\rho_ {j - 1}) \quad j = 1, \dots , S\tag{70}
$$

$$
\xi (\rho_ {j}) = \xi (\mu_ {j}) + K n _ {j} \varDelta_ {j} - K (\rho_ {j} - \mu_ {j}) \quad j = 1, \dots , S\tag{71}
$$

$$
\xi (\rho_ {j}) \geq 0 \quad j = 1, \dots , S\tag{72}
$$

$$
\xi (\mu_ {j}) \geq 0 \quad j = 1, \dots , S\tag{73}
$$

$$
\varDelta_ {j} \leq \rho_ {j} - \mu_ {j} \quad j = 1, \dots , S\tag{74}
$$

$$
\varDelta_ {j} \geq 0 \quad j = 1, \dots , S\tag{75}
$$

$$
M \omega_ {j} - n _ {j} \geq 0 \quad j = 1, \dots , S\tag{76}
$$

$$
\omega_ {j} - n _ {j} \leq 0 \quad j = 1, \dots , S\tag{77}
$$

$$
\omega_ {j} \in \{0, 1 \} \quad j = 1, \dots , S\tag{78}
$$

where M is a positive and sufficiently large number.

\-

In constraints (71), the values of the inventory level at the end of each production interval are defined. Note that such constraints hold both for the case in which orders are placed within the production interval and for the opposite case (in which, of course, $n _ { j } = 0 )$ .

Problem 5 is a nonlinear mixed-integer mathematical programming problem, which can be solved by nonlinear solvers included in mathematical programming software tools. The solution of Problem 5 provides decisions about how many orders must be forwarded to suppliers, the time instants corresponding to order deliveries and the ordered quantities. Actually, the provided solution is typically a local optimum.

Note that Problem 5, which is here considered as a subproblem within the op timization procedure defined for a node of a supply chain, is actually a general replenishment problem that significantly extends the classical Wagner-Within model. More specifically, in the model proposed here, demand is a time-varying deterministic quantity (as in Wagner-Within model), but the time instants in which orders are placed are asynchronous (and no time discretization has been realized). Moreover, in the present case, the inventory serves a production process characterized by a piecewise constant production effort (which can be also null in specified time intervals).

## 5 The Multi-Site Case

The optimization approach regarding a single node is extended to consider the interactions among different stages of the supply chain structure. In this section, two simple multi-site schemes will be analyzed, the former being related to a competitive case, the latter considering a cooperative structure.

The first multi-site structure we want to analyze is a simple case in which different production nodes can serve a customer (the simple case of two competitive nodes is reported in Fig. 10). In particular, the considered problem regards the definition of an optimization procedure in order to define the best production centre able to serve a given demand. It is assumed that each producer has to optimally realize a predefined job sequence, over a certain time horizon, and that, at a given time instant, a new request comes by a generic consumer, in terms of a required quantity and a required delivery time instant.

![](images/page_175_image_2.jpg)

Fig. 10. A simple competitive multi-site structure

In order to formalize the optimization problem concerning production and delivery of finite products to a consumer in a supply chain, some assumptions have been considered. First of all, the requests coming from consumers are processed one at a time and they are sequenced depending on a chronological order; moreover, each consumer request cannot be split, this means that it must be satisfied by only one producer. Furthermore, transportation operations are modelled in a very simplified way, thus each request corresponds to one transportation operation and transportation times between each producer and each consumer are known and constant.

The decision process through which a consumer chooses the best producer for satisfying its demand can be schematized as a sequence of some decision steps. First of all, the consumer makes a request $( Q , \pi ^ { * } )$ , where $\pi ^ { * }$ is the due date of the request and $Q$ is the required quantity of products. Then, each producer $p = 1 , \ldots , P$ (in the case shown in Fig. 10, it is $P = 2 )$ answers to the request following these steps:

• Producer p determines the required time instant for ending the production as $t _ { p } ^ { * } = \pi ^ { * } - t _ { p }$ , where $t _ { p }$ is the transportation time between the production site $p$ and the consumer;

• Producer p inserts $( t _ { p } ^ { * } , Q )$ in its job sequence;

Producer p applies the optimization procedure defined for single production nodes (Problem 2) and it obtains its optimal solution, determining its optimal delivering time $d t _ { p }$ and the production cost $C P _ { p }$ yielded by the insertion in the job sequence of the considered request;

• Producer p computes its transportation cost $C T _ { p } ;$

Producer p can thus determine the characteristics of the product delivery to the consumer and, specifically, the total cost $C _ { p }   =   C T _ { p }   +   C P _ { p }$ and the delivering time to the consumer $t c _ { p } ,$ , where $t c _ { p } = d t _ { p } + t _ { p }$

Once received this information by all the producers, the consumer chooses the best producer to which the required production can be assigned; its choice is realized by adequately weighing the price and the supply characteristics, in terms of delivery time.

A second example of multi-site structure consists in the connection of two production nodes belonging to two subsequent stages of the supply chain system. Note that, in this case, the production nodes operate in a cooperative framework. A sketch of this two-node framework is given in Fig. 11.

![](images/page_176_image_4.jpg)

Fig. 11. A simple cooperative multi-site structure

First of all, finite horizon time periods are defined and correspond to optimization horizons for both the nodes; such intervals are driven by the external demand which reaches Producer 2 in the form of the already defined finite sequence of asynchronous requests $( Q _ { i } , \pi _ { i } ^ { * } ) , \quad i = 1 , \ldots , N .$ As previously described, considering the transportation time, $\pi_{i}^{*}$ are transformed in $t _ { i } ^ { * }$ , as in the definition of Problem 2.

In particular, by solving Problem 2, Producer 2 finds the optimal closed-loop production policy, determining the optimal production effort $k ^ { o } ( t )$ , the optimal values of the idle times $\tau _ { i } ^ { o } , \quad i   =   0 , \ldots , N   -   1$ , and the optimal values of the production times $T _ { i } ^ { o } , ~ i = 0 , \ldots , N - 1$ . Then, by solving Problem 3, Producer 2 calculates the optimal raw material replenishment policy, computing the number of orders to be placed at each production interval, the reorder periods at each production interval, and the corresponding ordered quantities. This also leads to the determination of the time instants at which orders are placed. The replenishment policy is thus defined for Producer 2 and it corresponds to a finite sequence of asynchronous requests for Producer 1.

The way in which Producer 1 deals with the received requests is based on its internal optimization procedure (solution of Problem 2 and Problem 3) and on the following considerations. An early delivery by Producer 1 to Producer 2 would involve an increased inventory cost for Producer 2, whereas a tardy delivery by Producer 1 to Producer 2 would cause a higher cost relevant to the deviations form due-dates of the external demand. If the unitary costs defined by Producer 2 are known by Producer 1, and as far as a cooperative framework is considered, the cost relevant to deviations from due-dates is no more symmetric for Producer 1 and it can be computed on the basis of the unitary costs of Producer 2. More in detail, we suppose that the unitary raw material inventory cost and the unitary cost for deviations from due-dates are $H _ { \xi , 2 }$ and $\alpha _ { 2 }$ for Producer 2; then, two different unitary costs for deviations from due-dates are defined for Producer 1, respectively, for earliness and tardiness, defined as $\alpha _ { E , 1 }$ and $\alpha _ { T , 1 }$ . Thus, it will be $\alpha _ { E , 1 } = H _ { \xi , 2 }$ and $\alpha _ { T , 1 } = \alpha _ { 2 }$

In this case as well, transportation operations are very simply modelled as fixed delays. Moreover, it would be desirable that decisions taken by Producer 1 did not “perturb” too much the production policy of Producer 2. More specifically, it would be interesting to maintain the set of subsequences found by Producer 2 unchanged. As a matter of fact, by preserving the defined subsequences, Producer 2 could also admit early or tardy deliveries by Producer 1, since it is provided with control strategies, function of the system state and in particular of the current inventory level. If Producer 1 does not succeed in fulfilling the requests of Producer 2 by preserving the set of subsequences, Producer 2 needs to re-run the overall optimization procedure.

## 6 Conclusions

A hybrid model for a production node of a supply chain system is proposed in the paper. The node is represented by defining the dynamics of two inventories referred to raw materials and final products, respectively. On the basis of such a model, an optimization problem relevant to the minimization of order costs, inventory costs and costs due to deviations from the external demand has been stated. The decision variables refer to the process of raw material arrivals, the process of finite product deliveries and the production effort. The resulting optimization problem is a nonlinear functional optimization problem. A solution procedure based on the decomposition of the problem into two subproblems is proposed. The former subproblem refers to the determination of the optimal production effort and the optimal product departure process, whereas the latter subproblem corresponds to the determination of the optimal replenishment policy. Finally, the exploitation of the proposed solution procedure in two very simple multi-site structures is described.

Present and future research is devoted to the definition of more complex decentralized decisional structures in which production nodes equipped with the described optimization algorithm interact both in cooperative and in competitive frameworks.

## References

[1] Chopra S and Meindl P (2001) Supply chain management: strategy, planning, and operation. Prentice-Hall.

[2] Min H, Zhou G (2002) Supply chain modeling: past, present and future. Computers and Industrial Engineering 43:231–249.

[3] Tan KC (2001) A framework of supply chain management literature. European Journal of Purchasing and Supply Management 7:39–48.

[4] Gershwin SB (1994) Manufacturing Systems Engineering. Prentice-Hall.

[5] Tan B, Gershwin SB (2004) Production and Subcontracting Strategies for Manufacturers with Limited Capacity and Volatile Demand. Annals of Operations Research 125: 205–232.

[6] Hu JQ, Vakili P, Huang L (2004) Capacity and Production Managment in a Single Product Manufacturing System. Annals of Operations Research 125: 191–204.

[7] Blanchini F, Miani S, Ukovich W (2000) Control of production-distribution systems with unknown inputs and system failures. IEEE Transactions on Automatic Control 45: 1072–1081.

[8] Bauso D, Blanchini F, Pesenti R (2006) Robust control strategies for multi-inventory systems with average flowconstraints. Automatica 42: 1255–1266.

[9] Xu J, Hancock KL, (2004) Enterprise-Wide Freight Simulation in an Integrated Logistics and Transportation System. IEEE Transactions on Intelligent transportation Systems 5: 342–346.

[10] Schwartz JD, Wang W, Rivera DE, (2006) Simulation-based optimization of process control policies for inventory management in supply chains. Automatica 42: 1311–1320.

[11] Giglio G, Minciardi R, Sacone S, Siri S (2005) A hybrid model for optimal control of single nodes in supply chains. Proceedings of 16th IFAC World Congress.

[12] Giglio G, Minciardi R, Sacone S, Siri S (2006) Supply chain management and optimization. Proceedings of LT’06, International Workshop on Logistics and Transportation.

[13] Siri S (2006) Modelling, optimization and control of logistic systems. PhD Thesis, University of Genova, Italy.

[14] Giglio G, Minciardi R, Sacone S, Siri S (2007) Optimal control of single nodes in supply chains by a hybrid model. DIST Technical Report - June 2007.

[15] Giglio G, Minciardi R, Sacone S, Siri S (2007) Optimal replenishment policies in production nodes of supply chain models. Proceedings of the European Control Conference.

# Approximate Optimal Order Batch Sizes in a Parallel-aisle Warehouse

Yeming Gong1 and René de Koster2

1 RSM Erasmus University, The Netherlands ygong@rsm.nl

2 RSM Erasmus University, The Netherlands rkoster@rsm.nl

**Summary.** The past warehousing literature dealing with order picking and batching assumes batch sizes are given. However, selecting a suitable batch size can significantly enhance the system performance. This paper is one of the earliest to search optimal batch sizes in a general parallel-aisle warehouse with stochastic order arrivals. We employ a sample path optimization and perturbation analysis algorithm to search the optimal batch size for a warehousing service provider facing a stochastic demand, and a central finite difference algorithm to search the op timal batch sizes from the perspectives of customers and total systems. We show the existence of optimal batch sizes, and find past researches underestimate the optimal batch size.

**Key words:** Stochastic optimization, Sample path optimization, Order picking, Batch size

## 1 Introduction

Order picking – the process of retrieving products from storage (or buffer areas) in response to a specific customer request – is the most labor-intensive operation in warehouses with manual systems, and a very capital-intensive operation in warehouses with automated systems (Goetchalckx and Ashayeri, 1989; Tompkins et al., 2003). Managing order picking systems effectively and efficiently is a challenging process in many warehouses. Order picking efficiency can often be improved by order batching (Gademann and Van De Velde, 2005), which is a method to group a set of orders into a number of sub-sets, each of which can then be retrieved by a single picking tour (De Koster et al., 2007).

The earlier papers dealing with order batching problem usually assume the batch size is directly given. A natural question is: are these given batch sizes suitable? Considering setup time and unit service time for order picking, the total service time and batch size are not related linearly: the setup time will take a bigger proportion in the total service time for a small batch, while the unit service time will take a bigger proportion in the total service time for larger batches. Therefore it is an interesting question to explore the optimal batch size when orders arrive according to a stochastic process. A following research question is: how to find an optimal batch size if it exists? Most research involved in optimizing batch sizes, with the objective to minimize total service times assumes the order set is given. Gademann and Van de Velde (2005) have pointed out that the deterministic version of the batch problem with optimal routing is $\mathcal { N P } _ { - }$ hard when the batch size is larger than 2, in a parallel-aisle layout. It is tough or even infeasible to determine optimal batch sizes for the stochastic version of the problem. Few papers explore optimum batch sizes in a stochastic context. Chew and Tang (1999) assume orders arrive according to a Poisson process and approximate the travel time in a rectangular warehouse and use this approximate expression to minimize the total throughput time of the first order in a batch. They compare their results with simulation. Le-Duc and De Koster (2007) extend these results by determining the optimal batch size minimizing the throughput time of a random order in a two-block warehouse. All methods use approximation methods and do not directly optimize the batch size, as this is very cumbersome. In this paper we opt for a different approach, by efficient simulation optimization. Simulation optimization can help the search for an improved policy while allowing for complex features that are typically outside of the scope of analytical models. In this paper, we will employ SPO (sample path optimization), a simulation optimization technique with the advantage of high efficiency and convenience. However, SPO requires a technique to estimate the gradient of the objective function with respect to the batch size.

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">L. Bertazzi et al. (eds.), Innovations in Distribution Logistics, Lecture Notes</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">in Economics and Mathematical Systems 619, DOI: 10.1007/978-3-540-92944-4,</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">-c 2009 Springer-Verlag Berlin Heidelberg</span></small>

A large number of gradient estimation techniques exist, such as Infinitesimal Perturbation Analysis (IPA), Likelihood Ratios, Symmetric Difference, and Simultaneous Perturbation (Fu, 2002). IPA is mainly used to calculate a sample path derivative with respect to an input parameter in a discrete event simulation (Heidelberger et al., 1998). We will employ this technique since it is an “efficient gradient estimation technique” (Ho et al., 1979), which can “expedite the process of performing experiments on discrete event simulation models” (Johnson and Jackman, 1989). The implicit assumption of IPA is that the average of the change which results from the perturbation equals the change in expectation, and it yields an unbiased estimator. Convergence is an important issue for the implementation of IPA. Heidelberger et al. (1988) have studied the convergence properties of IPA sample path derivative, and derived the necessary and sufficient condition for the convergence. Applications of perturbation analysis have been reported in simulations of Markov chains (Glasserman, 1992), inventory models (Fu, 1994), supply chain problems (Gong and Yücesan, 2006), manufacturing systems (Glasserman, 1994), finance (Fu and Hu, 1997), and statistical process control (Fu and Hu, 1999). In some formulations in this paper, we will face complicated objective functions. In order to obtain optimal batch sizes, we need to compute the gradient of these objective functions. However, either their gradients are not available in explicit form or they are given by complicated expressions. We therefore resort to a finite difference method, which makes it possible to use arithmetic operations to determine the gradient.

In this paper, we consider the optimal order batch size problem with stochastic demand in a parallel-aisle warehouse (see Fig. 1), with cross aisles at the front and back of the aisles. The warehouse faces a demand with a given distribution. An order picker travels at a constant velocity with a S-shape routing policy, one of most common routing policies in practice. In order to improve picking efficiency, orders are batched.

The research objective in this paper is to minimize the operational costs by optimizing the order batch size, defined as the set of orders that are picked by one order picker in one route, and batch size q is the number of items in the batch, with constraint $q ^ { L B } \leq q \leq q ^ { U B }$ , where the upper bound $q ^ { U B }$ is determined by the capacity of pick devices (pallets or bins) and the lower bound $q ^ { L B }$ is specified by an additional condition like system stability. To achieve this research objective, we consider three major research questions and build corresponding models as follows.

First of all, we examine the operational cost from the perspective of a warehousing service provider and build the corresponding Model-1. This model focuses primarily on an internal objective by minimizing the average total service time, which is the sum of setup time and travel time. We exclude picking time as this is not influenced by the batching policy. Orders are picked in a FIFO sequence. Model-1 emphasizes the impact of order batching on performance of a warehousing service provider. Secondly,we examine the cost for customers and build a corresponding Model-2, which is taken from Chew and Tang (1999). The contribution in Model-2 is to provide an efficient finite difference algorithm. While using straightforward simulation takes much time to obtain a solution by enumeration, our method takes on average 6 seconds to get one solution. Finally,we consider the total cost for both the warehousing service provider and the customers by combining Model-1 and Model-2 into a new Model-3. The contribution of this research is twofold. First we show SPO and perturbation analysis algorithms are efficient in deriving optimal values. Second we combine the perspectives of both customers and a warehousing provider in one model and show it can also be solved by perturbation analysis and an SPO algorithm.

The remainder of the paper is organized as follows: in the following section, we search optimal batch sizes for warehousing service providers in a general stochastic parallel-aisle warehouse by sample path optimization and infinitesimal perturbation analysis techniques. Section 3 is devoted to an efficient finite difference algorithm to search optimal batch sizes for customers. In Sect. 4, we present a model with the objective of minimizing the total cost, and provide an efficient finite difference algorithm to search the optimal batch size. We conclude with final discussion, contribution summary and further research in Sect. 5.

## 2 Optimal Order Batch Sizes for Model-1

## 2.1 Model

Model-1’s objective is to minimize the total expected operation time of a warehousing service provider $E [ T _ { p } ( q , D ) ]$ , where $q$ is the decision variable, the subscript p indicates a warehousing service provider, and $D$ is the demand generated from a given distribution $f ( D ) .   E [ T _ { p } ( q , D ) ]$ is the product of the expected number of batches $E [ D / q ]$ and the expected operational time of one batch. Following [4], we do not consider picking time since the batching policy does not influence the total picking time for a given demand. But the batch size does influence the total setup time and the total expected travel time. Therefore, in our model the expected operational time of one batch is the sum of a setup time $\beta$ and an expected travel time $E [ L ( q ) / \nu ]$ , where $E [ L ( q ) ]$ is the expected travel distance and v is a constant travel velocity. $E [ L ( q ) ]$ depends on the warehouse layout and the routing method. We assume a rectangular, parallel-aisle layout, as sketched in Fig. 1 and an S-shape routing method (see De Koster et al., 2007). For this environment, Chew and Tang (1999) have found a closed form approximate expression for $E [ L ( q ) ]$ . We have

$$
\underline {{\text {Model} - 1 : \min _ {D \sim f (D) , 0 \leq q \leq D} E [ T _ {p} (q , D) ]}}
$$

$$
s. t. \quad E [ T _ {p} (q, D) ] = E [ L (q) / v + \beta ] E [ D / q ]
$$

## 2.2 Algorithm

This section demonstrates how to obtain the optimal batch size quantities in a parallel-aisle warehouse with stochastic demand. Our scheme is to use the simulation optimization algorithm by combining sample path optimization and perturbation analysis to examine optimal order batch sizes.

## Algorithm Description

To compute the optimal batch size values, we adopt a sample path optimization technique as main algorithm, where we use IPA (Infinitesimal Perturbation Analysis) to calculate the gradient value. We start with an arbitrary batch size $q ^ { 1 }$ . After randomly generating an instance of the demand, we construct and solve Model-1 in a deterministic fashion. Then, we compute gradient values by the decision tree from the perturbation analysis. The procedure is summarized in a pseudo-code format in the following procedure, where K denotes the total number of steps taken in a search path of the main algorithm, U represents the total number of steps in one inner cycle which is to provide a gradient estimation at one step of the main algorithm, $\alpha _ { k }$ represents the step size at the each iteration $k ,$ and $q ^ { k }$ represents the batch size at the $k ^ { t h }$ step. The choice of step size is important to guarantee convergence of the batch size. A proper choice will be explained further in Theorem $4 .$

Algorithm 1

(I) Initialization.

(I.1) Initialize K.

(I.2) Initialize U.

(I.3) Initialize $q ^ { 1 }$

(I.4) Initialize $\alpha _ { 1 } = \alpha / 1$ for a constant α.

(II) Set $k \gets 1$

Repeat.

Set $u \gets 1$

Repeat.

(II.1) A. Generate the demand $d _ { u } ^ { k }$ from $f ( D )$

(II.1) B. Compute the objective value of Model-1 in a deterministic fashion.

(II.1) C. Compute and accumulate gradients $d L _ { \mu } ^ { k } ,$

also record generated demand $d _ { u } ^ { k }$ and realized travel distance $L _ { u } ^ { k } .$

$$
u \leftarrow u + 1,
$$

Until $\scriptstyle { u = U . }$

(II.2) Compute the desired gradients $\begin{array} { r } { \frac { \partial E [ L ] } { \partial q } \vert _ { q = q ^ { k } } = \frac { 1 } { U } \sum _ { u = 1 } ^ { U } d L _ { u } ^ { k } , } \end{array}$

$\begin{array} { r } { E [ D ] ^ { k } = \frac { 1 } { U } \sum _ { u = 1 } ^ { U } d _ { u } ^ { k } , } \end{array}$ , and $\begin{array} { r } { E [ L ] ^ { k } = \frac { 1 } { U } \sum _ { u = 1 } ^ { U ^ { * } } L _ { u } ^ { k } } \end{array}$ at the $k \; s t e p .$

(II.3) Calculate the desired gradients $\begin{array} { r } { d T _ { q } ^ { k } = ( \frac { 1 } { \nu } \frac { \partial E [ L ] } { \partial q } | _ { q = q ^ { k } } + \beta ) \frac { E [ D ] ^ { k } } { q ^ { k } } } \end{array}$

$$
+ (\frac {1}{v} E [ L ] ^ {k} + \beta) (- \frac {E [ D ] ^ {k}}{(q ^ {k}) ^ {2}}).
$$

(II.4) Update the batch size by $q ^ { k + 1 } \gets \lfloor q ^ { k } - \alpha _ { k } d T _ { q } ^ { k } \rfloor$ , where $\alpha _ { k } = \alpha / k .$

$$
k \leftarrow k + 1
$$

Until k = K.

(III) Return the $\{ q ^ { k } \} _ { k = 1 } ^ { K }$ and the objective function value.

We explain the procedure as follows:

(I) Initialization. The algorithm starts with an arbitrary value for the batch size $q ^ { 1 }$ . K and U are given and can be determined by a pilot study to solve the following trade-off: while a small K cannot provide sufficient data, and output will have a big variance, a too large K is inefficient to improve the optimal value.

(II) The main loop in step (II) is an outer loop with K steps. Each step includes a U-step inner loop computation in step (II.1), IPA analysis in step (II.2), the desired gradient calculation in step (II.3), and the updating of batch sizes in step (II.4).

We first run an inner loop with U steps. At each step of the inner loop, we generate the demand from distribution $f ( D )$ , solve the problem of Model-1 in a deterministic fashion once the demand is observed, and calculate the perturbation value $d L _ { u } ^ { k }$ . Secondly, we conduct critical computation $\begin{array} { r } { \frac { \partial E [ L ] } { \partial q } \vert _ { q = q ^ { k } }   =   \frac { 1 } { U } \sum _ { u = 1 } ^ { ^ { L } } d L _ { u } ^ { k } } \end{array}$ , which is just the IPA technique. Thirdly, we compute the gradient of the expected travel time with respect to the batch size by $\begin{array} { r } { d T _ { q } ^ { k } = ( \frac { 1 } { \nu } \frac { \partial E [ L ] } { \partial q } | _ { q = q ^ { k } } + \beta ) \frac { E [ D ] ^ { k } } { q ^ { k } } + ( \frac { 1 } { \nu } E [ L ] ^ { k } + \beta ) ( - \frac { E [ D ] ^ { k } } { ( q ^ { k } ) ^ { 2 } } ) } \end{array}$ Finally, we update batch sizes $q ^ { k + 1 }$ by $q ^ { k + 1 } \xleftarrow { \cdot } \lfloor q ^ { k } - \alpha _ { k } d T _ { q } ^ { k } \rfloor$ at the $k ^ { t h }$ step. Also note that since the algorithm stops at $k = K$ , we do not need an extra stopping rule here.

(III) Return the $q ^ { k }$ and objective function value at each step. Then we can conduct the output analysis.

## Algorithm Justification

If an algorithm can converge and the objective function subject to minimization is convex, the algorithm can provide a global optimal value. In order to justify Algorithm 1, we build four theorems. Theorem 1 is to justify the convexity of our objective function. Theorem 2, 3, and 4 will show the convergence of Algorithm 1.

In order to examine the convexity of objective function $E [ T _ { p } ( q , D ) ]$ . We first establish Theorem 1 as follows.

**Theorem 1.** The objective function $E [ T _ { p } ( q , D ) ] = E [ L ( q ) / \nu + \beta ] E [ D / q ]$ is a convex function $o f q .$

Proof: For item locations with uniform distribution, Chew and Tang [4] have given approximate distance estimation for the S-shape routing policy. Based on their result, we have

$$
E \left[ \frac {L (q)}{v} + \beta \right] = \frac {M}{v} H \left[ 1 - \left(1 - \frac {1}{M}\right) ^ {q} \right] + 2 \frac {\omega}{v} \left[ M - \sum_ {i = 1} ^ {M - 1} \left(\frac {j}{m}\right) ^ {q} \right] + \frac {H}{2 v} + \beta .\tag{1}
$$

For a constant $\theta$ with $0 \: < \: \theta \: < \: 1 , \: f ( q ) \: = \: - \theta ^ { q }$ is a concave function of $q .$ So $E [ L ( q ) / \nu + \beta ]$ here is a concave function. $E [ D ] / q$ is nonincreasing convex function of $q .$ From Boyd and Vandenberghe (2004), the product $E [ L ( q ) / \nu + \beta ] E [ D / q ]$ of a concave function $E [ L ( q ) / \nu + \beta ]$ and a nonincreasing convex function $E [ D ] / q$ is convex. -

In this algorithm, it is critical to find an efficient gradient estimator. We use perturbation analysis to compute this gradient. Perturbation analysis is a powerful technique for the efficient performance analysis of dynamic systems. Its fundamental approach is to keep track of information along a perturbed path. The main principle behind perturbation analysis is that if a decision variable of a system is perturbed by a small amount, the sensitivity of the response of the system to that variable can be estimated by “tracing its pattern of propagation through the system” (Carson and Maria, 1997). This will be a function of “the fraction of the propagations that die before having a significant effect on the response of interest” (Carson and Maria, 1997). The fact that all derivatives can be derived from the same simulation run represents a significant advantage to IPA in terms of the efficiency. With the support of this technique, we have the Theorem 2.

**Theorem 2.** The gradient of expected travel time with respect to batch size can be computed by d $\begin{array} { r } { ^ { \prime } T _ { p } = ( \frac { 1 } { \nu } \frac { \partial E [ L ] } { \partial q } + \beta ) \frac { E [ D ] } { q } + ( \frac { E [ L ] } { \nu } + \beta ) ( - \frac { E [ D ] } { ( q ^ { k } ) ^ { 2 } } ) } \end{array}$ , where $\frac { \partial E [ L ] } { \partial q }$ can be calculated by the perturbation analysis and decision tree method.

Proof: From Model-1, we have

$$
\left. \frac {\partial E [ T _ {p} (q) ]}{\partial q} \right| _ {q = q ^ {k}} = (\frac {1}{v} \left. \frac {\partial E [ L ]}{\partial q} \right| _ {q = q ^ {k}} + \beta) \frac {E [ D ]}{q ^ {k}} + (\frac {E [ L ]}{v} + \beta) (- \frac {E [ D ]}{(q ^ {k}) ^ {2}}).\tag{2}
$$

![](images/page_185_image_2.jpg)

A batch with even aisles

![](images/page_185_image_4.jpg)

Perturbation pattern 1

![](images/page_185_image_6.jpg)

Perturbation pattern 2

![](images/page_185_image_8.jpg)

Perturbation pattern 3

![](images/page_185_image_10.jpg)

![](images/page_185_image_11.jpg)

A batch with odd aisles

Perturbation pattern 4

![](images/page_185_image_14.jpg)

Perturbation pattern 5

![](images/page_185_image_16.jpg)

![](images/page_185_image_17.jpg)

Perturbation pattern 6

Perturbation pattern 7

Fig. 1. Perturbation analysis for a batch in a parallel-aisle warehouse with S-shape routing policy

In this formula, the critical issue is to compute the gradient of the travel distance with respect to batch sizes. Gong and Yücesan [10] have provided an implementation framework and theoretical justification of SPO and IPA, and they compute the gradient by an analytical duality method. Different from them, we conduct direct perturbation analysis, and then derive a decision tree from perturbation patterns.

We conduct a perturbation analysis for a single batch with S-shape routing policy here. For a batch with batch size q, we give the system a perturbation, i.e., let the batch size increase by 1. In Fig. 1 the item with a cross “X” is the perturbed item. By comparing the distance before and after perturbation, we can compute the perturbation of distance.When the number of visited aisles is even, there are three perturbation patterns. (see perturbation patterns 1, 2, 3 in Fig. 1). When the number of visited aisles is odd, there are four perturbation patterns. (see perturbation patterns 4, 5, 6, 7 in Fig. 1).

![](images/page_186_image_3.jpg)

Fig. 2. Decision tree from perturbation analysis

In the following research,we use the notation below:

M = the number of aisles;

H = the length of aisles. We assume a bin containing one kind of item has one unit length;

ω = the cross distance between two consecutive aisles;

D = the mean of demand;

N<sub>v</sub> = the number of visited aisles;

E = the even number set;

Θ = the odd number set;

$\varPsi   =   \{ 1 , 2 , . . . , q \}$ the indices set of q items;

ξ<sub>i</sub> = the aisle position of item $i , \xi _ { i } = 1 , . . . , M ;$

η<sub>i</sub> = the location position of item $i , \eta _ { i } = 1 , . . . , H ;$

Ω = the position set covered by the routing when batch size is q. The position of an item $i \in \mathcal { H }$ is indicated by $( \xi _ { i } , \eta _ { i } )$

$\xi ^ { * } = m a x ( \xi _ { i } , i \in \varPsi )$ be the farthest aisle visited;

$\eta ^ { * } = m a x ( \eta _ { i } , \forall i , s . t . \xi _ { i } = \xi ^ { * } )$ be the farthest position at the farthest aisle visited.

By tracing its pattern of propagation through the system, we can build a decision tree for the gradient computation in Fig. 2. Theorem 2 follows from IPA analysis in Fig. 1 and the decision tree in Fig. 2. -

**Theorem 3.** If demand D has a density on $( 0 , \infty )$ and $E [ D ] < \infty ,$ , batch size $q \in \Re ^ { + }$ and $q < \infty ,$ , the gradients obtained by Theorem 2 are bounded with probability 1.

Proof: Generate the aisle position $\xi _ { q + 1 }$ and location position $\eta _ { q + 1 }$ of a perturbed item. For S-shape routing policy, from the decision tree in Fig. 2, the gradient can be computed as follows:

$$
\frac {\partial L}{\partial q} = \left\{ \begin{array}{l l} 2 [ \eta_ {q + 1} + \omega (\xi_ {q + 1} - \xi^ {*}) ], & \xi_ {q + 1} > \xi^ {*} \text {and} N _ {v} \in E \\ 2 \eta^ {*}, & \xi_ {q + 1} <   \xi^ {*}, (\xi_ {q + 1}, \eta_ {q + 1}) \notin \Omega_ {q} \text {and} N _ {v} \in E \\ 0, & \xi_ {q + 1} = \xi^ {*}, (\xi_ {q + 1}, \eta_ {q + 1}) \notin \Omega_ {q} \text {and} N _ {v} \in E \\ 2 [ H - \eta^ {*} + \omega (\xi_ {q + 1} - \xi^ {*}) ], & \xi_ {q + 1} > \xi^ {*} \text {and} N _ {v} \in \Theta \\ 2 (H - \eta^ {*}), & \xi_ {q + 1} <   \xi^ {*}, (\xi_ {q + 1}, \eta_ {q + 1}) \notin \Omega_ {q} \text {and} N _ {v} \in \Theta \\ 2 (\eta_ {q + 1} - \eta^ {*}), & \xi_ {q + 1} = \xi^ {*}, \eta_ {q + 1} > \eta^ {*} \text {and} N _ {v} \in \Theta \\ 0, & (\xi_ {q + 1}, \eta_ {q + 1}) \in \Omega_ {q} \text {and} N _ {v} \in \Theta . \end{array} \right.\tag{3}
$$

From (3), we have

$$
\frac {\partial L}{\partial q} \leq m a x \{2 [ \eta_ {q + 1} + \omega (\xi_ {q + 1} - \xi^ {*}) ], 2 \eta^ {*}, 2 [ H - \eta^ {*} + \omega (\xi_ {q + 1} - \xi^ {*}) ],
$$

$$
2 (H - \eta^ {*}), 2 (\eta_ {q + 1} - \eta^ {*}) \} \leq 2 H + 2 \omega (M - 1).\tag{4}
$$

The boundedness of gradient follows from (4).

**Theorem 4.** By the sample path optimization in Algorithm 1 for a proper choice of step size, the batch size $\{ q ^ { k } \} _ { k = 1 } ^ { \infty }$ converges with probability 1.

Proof: In order to ensure the convergence, a key issue is the selection of a suitable step size $\alpha _ { k }$ , where we have

Condition (1): A criterion for choosing $\alpha _ { k }$ is to let step size go to zero fast enough so that the algorithm can converge, but not so fast that it will induce a wrong value. One condition to meet that criterion is $\begin{array} { r } { \sum _ { k = 1 } ^ { \infty } \alpha _ { k } = \infty } \end{array}$ and $\begin{array} { r } { \sum _ { k = 1 } ^ { \infty } \alpha _ { k } ^ { 2 } < \infty } \end{array}$

For instance, $\alpha _ { k } = \alpha / k$ for some fixed $\alpha > 0$ satisfies Condition (1). The first part of this condition facilitates convergence by ensuring that the steps do not become too small too quickly. However, if the algorithm is to converge, the step sizes must eventually become small, as ensured by the second part of the condition.

For a convex objective function $E [ T _ { p } ( q ) ]$ , a bounded gradient (see Theorem 2 and Theorem 3), and a step size $\alpha _ { k }$ which satisfies the condition (1), according to Robbins and Monro (1951), we have a limit point of $\{ q ^ { k } \} _ { k = 1 } ^ { \infty }$ , which is stationary with probability 1. -

## 2.3 Results

We implement Algorithm 1 in Matlab. Experiments are conducted on a computer with 1.73GHz CPU and 516MB RAM. After acquiring characteristic information like warehouse size and generating the demand by a normal distribution $N ( \mu , \sigma ^ { 2 } )$ to specify the problem, the distance computation program can return batch sizes and objective values at each step to the main program. Then by the gradient computing algorithm, the main program can update the batch size until it converges. Here we adopt an initial step size $\alpha _ { 1 }   =   0 . 5$ by a pretest experiment. Since the objective function is convex, this convergence will lead to a global optimum.

Without loss of generality, the position of our depot is the first aisle and the first location. The probability to visit an aisle is equal for all aisles and uniformly distributed. We have aisle number $\xi _ { i }   \sim   U ( 1 , M ) , \forall i \in   \varPsi$ . The probability to visit a location in a visited aisle is also equal, i.e., location position $\eta _ { i } \sim U ( 1 , H ) , \forall i \in \mathbb { P }$ In order to verify the result from the simulation optimization, we compare it with the result of enumeration, where we enumerate all the possible batch size values from $q ^ { L B }$ to $q ^ { U B }$ . In combination with Monte Carlo simulation, the enumeration is conducted as follows. First, we generate a very large order number, and then generate the position of each item by given distributions $\xi _ { i } \; \sim \; U ( 1 , M ) , \forall i \; \in \; \varPsi$ and $\eta _ { i } \sim$ $U ( 1 , H ) , \forall i \in \varPsi$ . Then, for every value of $q ,$ we determine the batches of size $q$ in an FCFS sequence. Third we compute the routing length and corresponding warehouse operation time of each batch by the S-shape policy. For every batch size we compute the expected warehousing operation time and hence finally find the optimal batch size.

We present experiments in Table 1. We have conducted two groups of experiments: varying the aisle number M (experiments 1 to 5) and varying the aisle length H (experiments 6 to 10). The computation results include the items below:

$q ^ { E } { = }$ the optimal batch size obtained by enumeration;

$\widehat { q }   =$ the statistical estimation of batch size by the stochastic simulation algorithms, which includes the mean batch size $\overline { { q } }$ and half width (HW) of the 95% confidence interval (CI);

$R ( { \overline { { q } } } ) =$ the rounded integer value of the estimated batch size;

$\mathcal { A } _ { 1 } = | \overline { { q } } - q ^ { E } | / q ^ { E }$ , the direct bias of statistical estimation;

$\mathcal { A } _ { 2 } = | R ( \overline { { q } } ) - q ^ { E } | / q ^ { E }$ , the indirect bias of rounded statistical estimation;

We compute the average direct bias $\begin{array} { r } { \overline { { \mathcal { A } _ { 1 } } } { = } 1 / N \sum _ { n } | \overline { { q } } - q _ { n } ^ { E } | / q _ { n } ^ { E }   =   0 . 2 5 5 \% } \end{array}$ and the average indirect bias $\begin{array} { r } { \overline { { \mathcal { A } _ { 2 } } } { = } 1 / N \sum _ { n } | R ( \overline { { q } } ) - q _ { n } ^ { E } | / q _ { n } ^ { E } = 0 \% } \end{array}$ . The average direct bias of statistical estimation is less than $1 \%$ , and the average indirect bias of rounded statistical estimation is negligible.

Table 1. Experiment result for Model-1

| No. | M | H | ω | $q^{UB}$ | $q^{LB}$ | $q^E$ | $\widehat{q_1} = \overline{q} \pm HW$ | $R(\overline{q})$ | $\Delta_1$ | $\Delta_2$ |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 25 | 20 | 3 | 50 | 1 | 50 | 49.8694±0.0876 | 50 | 0.26% | 0 |
| 2 | 30 | 20 | 3 | 50 | 1 | 50 | 49.7793±0.0773 | 50 | 0.44% | 0 |
| 3 | 35 | 20 | 3 | 50 | 1 | 50 | 49.8895±0.0271 | 50 | 0.22% | 0 |
| 4 | 40 | 20 | 3 | 50 | 1 | 50 | 49.9391±0.0763 | 50 | 0.12% | 0 |
| 5 | 45 | 20 | 3 | 50 | 1 | 50 | 49.8394±0.0745 | 50 | 0.32% | 0 |
| 6 | 40 | 25 | 3 | 60 | 1 | 60 | 59.7696±0.0876 | 60 | 0.38% | 0 |
| 7 | 40 | 27 | 3 | 60 | 1 | 60 | 59.9196±0.0773 | 60 | 0.13% | 0 |
| 8 | 40 | 28 | 3 | 60 | 1 | 60 | 59.8195±0.0272 | 60 | 0.30% | 0 |
| 9 | 40 | 30 | 3 | 60 | 1 | 60 | 59.9093±0.0765 | 60 | 0.15% | 0 |
| 10 | 40 | 32 | 3 | 60 | 1 | 60 | 59.8597±0.0743 | 60 | 0.23% | 0 |

From the experiment, we observe that

the optimal batch size for Model-1 equals to the upper bound $q ^ { * } = q ^ { U B }$ which is robust in both groups of simulation experiments. We can understand this result from the limiting system behavior. By increasing the batch size, the travel and setup time per batch will converge to a constant.

$$
\begin{array}{c} \varliminf_ {q \to \infty} E [ \frac {L (q)}{v} + \beta ] = \lim _ {q \to \infty} \frac {M}{v} H [ 1 - (1 - \frac {1}{M}) ^ {q} ] + 2 \frac {\omega}{v} [ M - \sum_ {j = 1} ^ {M - 1} (\frac {j}{m}) ^ {q} ] + \frac {H}{2 v} + \beta \\ = \frac {2 M H + 4 M \omega + H}{2 v} + \beta . \end{array}\tag{5}
$$

However, with an increasing batch size $q ,$ the number of batches $E [ D ] / q$ will continue to decrease, and therefore the total operation time, which is the product of the two items, will also decrease. That is the reason why the optimal batch size will converge to its upper bound.

## 3 Optimal Order Batch Sizes for Model-2

## 3.1 Model

Model-1 in Sect. 2 considers the main operation time from the perspective of a warehousing service provider. It does not measure the time of customers and the service level. It is also necessary to examine the time spent by customers in a warehousing system. We therefore adopt the turnover time of a consumer’s order, which is from [4], as the objective to build the Model-2 as follows.

$$
\text {Model} - 2: \text {Min} \quad T _ {T O} (q) _ {q ^ {L B} \leq q \leq q ^ {U B}}
$$

$$
s. t. \quad T _ {T O} (q) = W _ {1} (q) + W _ {2} (q) + E [ S ]
$$

Chew and Tang [4] focus on the first order in a batch. However, their results can be generalized to a random order in a batch. In Model-2, the objective $T _ { T O } ( q )$ is the turnover time of a customer’s order, i.e., the duration an order stays in the system, when batch size is $q$ with $q ^ { L B }   \leq   q   \leq   q ^ { U B } .   T _ { T O } ( q )$ consists of three parts: expected batch time $W _ { 1 } ( q )$ , expected waiting time $W _ { 2 } ( q )$ and expected service time $E [ S ]$ . Let the order arrival rate be λ. The expected batch time $W _ { 1 } ( q )$ is given by Chew and Tang (1999) as $W _ { 1 } ( q )   =   ( q - 1 ) / \lambda$ . Expected waiting time $W _ { 2 } ( q )$ is approximately computed by the linear combination of expected waiting times of $M / M / 1 ,   M / D / 1$ and $D / M / 1$ . Expected service time $E [ S ]$ consists of travel time, picking and sorting time.

## 3.2 Algorithm

The essential problem in searching for the optimal batch size is the choice of the computation method. From Chew and Tang (1999), our objective function is a specially complicated function of $q ,$ and an analytical gradient computation method is infeasible. Perturbation analysis is also highly complicated in Model-2, especially for the perturbation analysis of $W _ { 2 }$ . Even if we had obtained the decision tree by perturbation analysis, its computation will not be efficient. Therefore we use the finite differences (FD) for our objective function. There are two FD approximations: forward FD and central FD. The forward difference derivative approximations consume less computer time, but they are usually not as precise as central difference method. Therefore we mainly use central FD as our gradient computation method.

We use finite difference optimization algorithm to examine order batch problem in a parallel-aisle warehouse, and demonstrates how to obtain the optimal batch size quantities. The procedure is summarized in a pseudo-code format in Algorithm $2 .$ where we start with a batch size $q ^ { 1 }$ , usually $q ^ { 1 } \stackrel { 2 } { = } q ^ { U B }$ , K denotes the total number of steps taken in a search path, $\alpha _ { k }$ represents the step size at the each iteration $k ,$ and $q ^ { k }$ represents the batch size at the $k ^ { t h }$ step.

Algorithm 2

(I) Initialization.

(I.1) Initialize $K .$

(I.2) Initialize $q ^ { 1 }$ to $q ^ { U B }$

(II) Set $k \gets 1$

Repeat.

(II.1) Compute $T _ { T O } ^ { k } ( q ^ { k } + h )$ and $T _ { T O } ^ { k } ( q ^ { k } - h )$ , when $k   >   I$

(II.2) Compute the desired gradients.

$\begin{array} { r } { d T _ { T O } ^ { k } = \frac { T _ { T O } ^ { k } ( q ^ { k } + h ) - T _ { T O } ^ { k } ( q ^ { k } ) } { h } , } \end{array}$ , when $k   =   I$

$\begin{array} { r } { d T _ { T O } ^ { k } = \frac { T _ { T O } ^ { k } ( q ^ { k } + h ) - T _ { T O } ^ { k } ( q ^ { k } - h ) } { 2 h } } \end{array}$ , when $k   >   I$

(II.3) Update the batch size, $\begin{array} { r } { \mathrm { , } q ^ { k + 1 } \leftarrow \lfloor q ^ { k } - \alpha _ { k } d T _ { T O } ^ { k } \rfloor \mathrm { . } } \end{array}$

k $\iota \gets k + 1$ ,

Until $k = K$

(III) Return the $\{ q ^ { k } \} _ { k = 1 } ^ { K }$ and the objective function value.

**Theorem 5.** By the finite difference algorithm 2 and a step size $\alpha _ { k }$ which can satisfy Condition (1) , the batch sizes $\{ q ^ { k } \} _ { k = 1 } ^ { \infty }$ <sup>in</sup> Model-2 can converge.

Proof: From Bertsekas (1999), for the finite difference algorithm with a step size which can satisfy Condition (1), if the objective function in Model-2 is convex, the batch size can converge. Chew and Tang (1999) have showed that $T _ { T O } ( q ) = W _ { 1 } ( q ) +$ $W _ { 2 } ( q ) + E [ S ]$ is a convex function of $q$ for $q ^ { L B } \leq q \leq q ^ { U B }$ , where $q ^ { L B }$ is determined by the system equilibrium condition since if the arrival rate $\lambda$ is too high the system will become unstable and $q ^ { U B }$ is specified by facility capability limitation. -

## 3.3 Results

Based on Chew and Tang (1999) formulation and our optimization algorithm, we implement the optimization procedure in Matlab. One run of simulation takes only 6 seconds on average. Let $\bar { q ^ { 1 } = q ^ { U B } }$ , for the number of aisle ranging from 25 to 45, we obtain the search paths indicated in Fig. 3. All the experiments converge in the last 500 steps. We compute the statistical estimation by the transient deletion technique.

![](images/page_191_chart_4.jpg)

Fig. 3. Search path by Algorithm 2

In order to verify the result from optimization algorithm 2, we compare the result with that by enumeration, where we traverse all possible batch size values from $q ^ { L B }$ to $q ^ { U B }$ . For all possible values of batch size $q ,$ we compute the expected objective values from Chew and Tang [4] and find the optimal batch size. We present the result in Fig. 4.

We present experiments in Table 2. The left part of Table 2 is the indices of experiments. The middle part of Table 2 is the experiment setting: $M , H , \omega , q ^ { L B }$ and $q ^ { \bar { U } \bar { B } }$ . We have conducted two groups of experiments: varying the aisle number M (experiments 1 to 5) and varying the aisle length H (experiments 6 to 10). The right part presents the computation results, which includes the items below:

q<sup>E</sup> = the optimal batch size obtained by enumeration;

$\widehat { q }   =$ the statistical estimation by Algorithm 2, which includes the mean batch size $\overline { { q } }$ and HW of the 95%CI;

R(q) = the rounded integer value of the estimated batch size;

![](images/page_192_chart_2.jpg)

Fig. 4. Turnover time versus batch sizes in Model-2

$\mathcal { A } _ { 1 }   =   | \overline { { q } } - q ^ { E } | / q ^ { E }$ , the direct bias of statistical estimation;

$\mathcal { A } _ { 2 }   =   | R ( \overline { { q } } ) - q ^ { E } | / q ^ { E }$ , the indirect bias of rounded statistical estimation;

We compute the average direct bias $\begin{array} { r } { \overline { { \mathcal { A } _ { 1 } } } { = } 1 / N \sum _ { n } | \overline { { q } } - q _ { n } ^ { E } | / q _ { n } ^ { E }   =   2 . 7 8 5 \% } \end{array}$ and the average indirect bias $\begin{array} { r } { \overline { { \mathcal { A } _ { 2 } } } = 1 / N \sum _ { n } | R ( \overline { { q } } ) - q _ { n } ^ { E } | / q _ { n } ^ { E } = 0 . 7 6 9 \% } \end{array}$ . The average direct bias of statistical estimation is less than 3%, and the average indirect bias of rounded statistical estimation is less than 1%.

Table 2. Experiment result for Model-2

| No. | M | H | $\omega$ | $q^{UB}$ | $q^{LB}$ | $q^E$ | $\widehat{q_1} = \overline{q} \pm HW$ | $R(\overline{q})$ | $\Delta_1$ | $\Delta_2$ |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 25 | 20 | 3 | 50 | 6 | 7 | 6.9129±0.0061 | 7 | 1.24% | 0 |
| 2 | 30 | 20 | 3 | 50 | 7 | 8 | 7.7847±0.0046 | 8 | 3.08% | 0 |
| 3 | 35 | 20 | 3 | 50 | 8 | 9 | 8.7647±0.0034 | 9 | 2.61% | 0 |
| 4 | 40 | 20 | 3 | 50 | 9 | 10 | 9.8098±0.0025 | 10 | 1.90% | 0 |
| 5 | 45 | 20 | 3 | 50 | 10 | 11 | 10.8911±0.0018 | 11 | 0.99% | 0 |
| 6 | 40 | 25 | 3 | 50 | 10 | 12 | 12.4991±0.00005 | 12 | 4.16% | 0 |
| 7 | 40 | 27 | 3 | 50 | 10 | 13 | 13.5003±0.00006 | 14 | 3.85% | 7.69% |
| 8 | 40 | 28 | 3 | 50 | 10 | 14 | 14.4994±0.00006 | 14 | 3.57% | 0 |
| 9 | 40 | 30 | 3 | 50 | 10 | 15 | 15.4996±0.00007 | 15 | 3.33% | 0 |
| 10 | 40 | 32 | 3 | 50 | 10 | 16 | 16.4998±0.00005 | 16 | 3.12% | 0 |

From the result we can observe that, the optimal batch size for customers is close to its lower bound and less than its upper bound $q ^ { L B } < q _ { 2 } ^ { * } < q ^ { U B }$ , which is robust in both groups of simulation experiments. This result is similar to results of Chew and Tang (1999).

## 4 Optimal Order Batch Sizes for the Total System

The objective functions of both Model-1 and Model-2 are unilateral. The result from Model-2 is similar to Chew and Tang (1999) and Le-Duc (2005), and this result possibly underestimates the positive effect of batch procedure. The result from Model-1 also possibly overestimates the positive effect of batch procedure. While a large batch size brings short-run minimal cost to warehouse service providers, it will also cause long throughput times for the customers, and may therefore harm the long-run interest of warehouse service providers. Considering both sides, we therefore build Model-3 and measure the total system cost.

## 4.1 Model

The objective in Model-2 is the turnover time for a single customer’s order while the objective in Model-1 is the total service time for the total customers. So we need to transform the data in Model-1, and compute the time spent by service provider on a single customer, that is $\begin{array} { r } { \overbrace { T _ { P } ( q ) } ^ { \mathrm { ~ } } = \frac { E [ L ( q ) ] / \nu ^ { \mathbf { 1 } } + \beta } { q } } \end{array}$ . Without loss of generality, we assume a single customer corresponds to a single order. Let $c _ { 1 }$ be the operation cost per unit time for service provider, and $c _ { 2 }$ be the waiting cost per unit time for customer. Then $c _ { 1 } \overline { { T _ { P } ( q ) } } + c _ { 2 } T _ { T O } ( q )$ is the total system cost $C ( q )$ for one customer. We have:

$$
\text {Model} - 3: \text {Min} \quad C (q) _ {q ^ {L B} \leq q \leq q ^ {U B}}
$$

$$
\begin{array}{c} s. t. \quad C (q) = c _ {1} \overline {{T _ {P} (q)}} + c _ {2} T _ {T O} (q) \\ \overline {{T _ {P} (q)}} = \frac {E [ L (q) ] / v + \beta}{q} \\ T _ {T O} (q) = W _ {1} (q) + W _ {2} (q) + E [ S ] \end{array}
$$

The ratio of $c _ { 1 }$ and $c _ { 2 }$ in Model-3 is used to measure the weight of both sides in the system. We define: the unit cost ratio $\begin{array} { r } { \gamma = \frac { c _ { 1 } } { c _ { 2 } } } \end{array}$

## 4.2 Algorithm

We mainly use central FD as gradient computation method since the objective function in Model-3 is a specially complicated function of $q .$ The procedure is summarized in a pseudo-code format in Algorithm 3, where we start with an initial batch size $q ^ { 1 }$ , for example $q ^ { 1 } ~ = ~ q ^ { U B }$ , K denotes the total number of steps taken in a searching path, $\alpha _ { k }$ represents the step size at the each iteration $k ,$ and $q ^ { k }$ represents the batch size at the $k ^ { t h }$ step.

<div class="docvortex-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Algorithm 3
(I) Initialization.
    (I.1) Initialize $K$.
    (I.2) Initialize $q^1$ to $q^{UB}$.
(II) Set $k \leftarrow 1$.
Repeat.
    (II.1) Compute $C^k(q^k + h)$ and $C^k(q^k - h)$, when $k &gt; 1$.
    (II.2) Compute the desired gradients.
    $dC^k = \frac{C^k(q^k + h) - C^k(q^k)}{h}$, when $k = 1$.
    $dC^k = \frac{C^k(q^k + h) - C^k(q^k - h)}{2h}$, when $k &gt; 1$.
    (II.3) Update the batch size, $q^{k+1} \leftarrow \lfloor q^k - \alpha_k dC^k \rfloor$.
    $k \leftarrow k + 1$,
Until $k = K$.
(III) Return the $\{q^k\}_{k=1}^K$ and the objective function value.
</div>

**Theorem 6.** By the finite difference algorithm 3 and a step size $\alpha _ { k }$ which can satisfy Condition (1) , the batch sizes $\{ q ^ { k } \} _ { k = 1 } ^ { \infty }$ <sup>in</sup> Model-3 can converge.

Proof: From [1], for the finite difference algorithm with a step size which can satisfy Condition (1), if the objective function in Model-3 is convex, the batch size can converge. In Sect. 2, we have proven $T _ { P } ( q )$ and therefore $c _ { 1 } \overline { { T _ { P } ( q ) } }$ are convex function. Chew and Tang [4] have showed that the objective function $T _ { T O } ( q )$ is a convex function of $q .$ So $C ( q ) = c _ { 1 } \overline { { T _ { P } ( q ) } } + c _ { 2 } T _ { T O } ( q )$ is a convex function of $q .$ The convexity ensures the algorithm will converge to a global optimum. -

## 4.3 Results

Based on the formulation in Model-3, we implement the optimization algorithm 3 in Matlab. The running time ranges from 13 seconds to 19 seconds. For the coefficient γ ranging from 30 to 70, we obtain the search paths in the Fig. 5. For all the experiments we conducted, we observe the search paths converge in the last 500 steps. We use the transient deletion technique to conduct the statistical estimation.

In order to verify the result from the finite difference optimization, we compare it with the result of enumeration, where we traverse all the batch size values from $q ^ { L B }$ to $q ^ { U B }$ . We compute the expected objective values for all possible values of $q$ and find the optimal batch size.

For the aisle numbers ranging from 25 to 45, we respectively compute their “total cost”, “part 1 cost” which is the cost of warehousing service providers, and “part 2 cost” which is the cost for the customers. The result is presented in Fig. 6 and summarized in Table 3. The first column of Table 3 is the experiment index. The second part is the experiment setting: we have conducted three groups of experiments: varying the aisle number M (experiments 1 to 5), the aisle length H (experiments 6 to 10) and the cost ratio $\gamma$ (experiments 11 to 15). The third part of Table 2 is the computational results by Algorithm 3 and enumeration, containing $q ^ { E } ,   \widehat { q } ,   R ( \overline { { q } } ) ,   \mathcal { A } _ { 1 }$ and $\varDelta _ { 2 }$

Table 3. Experiment result for Model-3

| No. | M | H | $\omega$ | $q^{UB}$ | $q^{LB}$ | $\gamma$ | $q^{E}$ | $\widehat{q_{1}} = \overline{q} \pm HW$ | $R(\overline{q})$ | $\Delta_{1}$ | $\Delta_{2}$ |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 25 | 20 | 3 | 50 | 6 | 20 | 12 | 12.2801±3.5136e-004 | 12 | 2.33% | 0 |
| 2 | 30 | 20 | 3 | 50 | 7 | 20 | 12 | 12.4999±1.1592e-005 | 12 | 4.17% | 0 |
| 3 | 35 | 20 | 3 | 50 | 8 | 20 | 12 | 12.5000±1.3900e-005 | 13 | 4.17% | 8.33% |
| 4 | 40 | 20 | 3 | 50 | 9 | 20 | 13 | 12.7900±9.0225e-004 | 13 | 1.62% | 0 |
| 5 | 45 | 20 | 3 | 50 | 10 | 20 | 13 | 13.4995±9.3120e-005 | 13 | 3.84% | 0 |
| 6 | 40 | 25 | 3 | 50 | 10 | 20 | 14 | 14.9999±1.8239e-005 | 14 | 3.57% | 0 |
| 7 | 40 | 27 | 3 | 50 | 10 | 20 | 15 | 15.4998±1.7737e-005 | 15 | 3.33% | 0 |
| 8 | 40 | 28 | 3 | 50 | 10 | 20 | 16 | 15.5001±2.3669e-005 | 16 | 3.12% | 0 |
| 9 | 40 | 30 | 3 | 50 | 10 | 20 | 16 | 16.9980±2.4165e-005 | 16 | 3.12% | 0 |
| 10 | 40 | 32 | 3 | 50 | 10 | 20 | 17 | 17.5000±2.5194e-006 | 18 | 2.94% | 5.88% |
| 11 | 40 | 20 | 3 | 50 | 10 | 30 | 15 | 15.4992±9.7966e-006 | 15 | 3.33% | 0 |
| 12 | 40 | 20 | 3 | 50 | 10 | 40 | 18 | 18.1962±6.0757e-004 | 18 | 1.09% | 0 |
| 13 | 40 | 20 | 3 | 50 | 10 | 50 | 20 | 20.4999±6.3132e-006 | 20 | 2.50% | 0 |
| 14 | 40 | 20 | 3 | 50 | 10 | 60 | 23 | 22.9373±1.3000e-003 | 23 | 0.27% | 0 |
| 15 | 40 | 20 | 3 | 50 | 10 | 70 | 25 | 25.2757±7.0235e-004 | 25 | 1.10% | 0 |

We compute the average direct bias $\begin{array} { r } { \overline { { \mathcal { A } _ { 1 } } } { = } 1 / N \sum _ { n } | \overline { { q } } - q _ { n } ^ { E } | / q _ { n } ^ { E }   =   2 . 7 0 0 \% } \end{array}$ and the average indirect bias $\begin{array} { r } { \overline { { \mathcal { A } _ { 2 } } } { = } 1 / N \sum _ { n } | R ( \overline { { q } } ) - q _ { n } ^ { E } | / q _ { n } ^ { E } = 0 . 9 4 7 \% } \end{array}$ . The average direct bias of statistical estimation is less than 3%, and the average indirect bias of rounded statistical estimation is less than 1%.

From the results, we can observe that the optimal batch size for the total system is less than the optimal batch size $q _ { 1 } ^ { * }$ in Model-1 and larger than $q _ { 2 } ^ { * }$ in Model-2. We have $q _ { 2 } ^ { * } \leq q _ { 3 } ^ { * } \leq q _ { 1 } ^ { * }$ , which is robust in all the experiments with a different number of aisles, different aisle length, and different cost ratios $\gamma .$ The result also shows that existing research underestimates the optimal batch size. This serious underestimation is due to the unilateral objective function, and it leads to an inferior performance of warehousing service providers. Our problem is a basic economic equilibrium problem with two sides of agents: a warehousing service supplier and consumers. From the perspectives of different agents, the optimal batch sizes are different.

![](images/page_196_chart_2.jpg)

Fig. 5. Search path by Algorithm 3

## 5 Concluding Remarks

This paper studies the optimal order batch size problem in a parallel-aisle warehouse with stochastic order arrivals. The contribution of this paper is twofold in both application and methodology.

While existing literature directly assumes the batch size value, this paper shows that an optimal batch size exists. A too large batch size will harm the throughput time of consumers, and a too small batch size will bring a negative impact to warehousing costs. Existing literature focusing on the customer perspective only claims a suitable batch size will be close to its lower bound. Our research shows an optimal batch size will be larger than its lower bound when the costs of warehousing service providers are considered.

Past literature has not provided an efficient method to search optimal batch sizes. This paper provides an IPA and SPO stochastic approximate optimal implementation scheme to search the batch sizes for the warehousing service providers in a general parallel-aisle warehouse setting. This paper also presents an efficient FD algorithm to search the optimal batch sizes for customers and the total system. The estimation biases of the proposed algorithms are satisfactory.

A further topic for research could be to investigate the optimal batch size with the different routing policies in a general parallel-aisle warehouse with stochastic order arrivals. This paper employs an S-shape routing method. It is also possible to research the optimal batch size with other heuristic routing policies like the midpoint routing policy and the largest gap routing policy, or the optimal routing policy.

![](images/page_197_chart_2.jpg)

Fig. 6. Cost vs. batch sizes in Model-3

The latter will probably be hard to solve.

**Acknowledgements** The authors would like to thank the referees for their constructive comments that have led to many improvements in the exposition of this paper.

## References

[1] Bertsekas D (1999) Nonlinear programming, Athena Scientific, Belmont, Massachusetts, USA

[2] Boyd S, Vandenberghe L (2004) Convex optimization. Cambridge University Press, UK

[3] Carson Y, Maria A (1997) Simulation optimization: Methods and applications. In: Andradótir S, Healy KJ, Withers DH, and Nelson BL (eds) Proceedings of the 1997 Winter Simulation Conference. Atlanta, Georgia

[4] Chew EP, Tang LC (1999) Travel time analysis for general item location assignment in a rectangular warehouse. European Journal of Operational Research 112:582–597

[5] De Koster R, Le-Duc T, Roodbergen KJ (2007) Design and control of warehouse order picking: A literature review. European Journal of Operational Research 182:481–501

[6] De Koster R, Van der Poort, ES and Wolters, M (1999) Efficient orderbatching methods in warehouses. International Journal of Production Research 37(7):1479–1504

[7] Gademann N, Van De Velde S (2005) Order batching to minimize total travel time in a parallel-aisle warehouse. IIE Transactions 37(1):63–75

[8] Glasserman, P (1992) Derivative Estimates from Simulation of Continuous-Time Markov Chains. Operations Research 40:292–308

[9] Goetschalckx M and Ashayeri J (1989) Classification and design of order picking systems. Logistics World, June, 99–106

[10] Gong Y, Yücesan E (2006) The Multi-Location Transshipment Problem with Positive Replenishment Lead Times. ERIM working paper

[11] Heidelberger P, Cao X-R, Zazanis MA, Suri R (1988) Convergence properties of infinitesimal perturbation analysis estimates. Management Science 34(11):1281–1302

[12] Ho YC, Eyler MA, and Chien TT (1979) A Gradient Technique for General Buffer Storage Design in a Serial Production Line. International Journal of Production Research 17:557–580

[13] Fu MC (1994) Sample Path Derivatives for (s, S) Inventory Systems. Operations Research 42:351–364

[14] Fu MC (2002) Optimization for Simulation: Theory vs Practice. INFORMS Journal on Computing 14(3):192–215

[15] Fu MC, Hu JQ (1997) Conditional Monte Carlo: Gradient Estimation and Optimization Applications. Kluwer, Boston

[16] Fu MC, Hu JQ (1999) Efficient Design and Sensitivity Analysis of Control Charts using Monte Carlo Simulation. Management Science 45:395–413

[17] Johnson ME, Jackman J (1989) Infinitesimal perturbation analysis: a tool for simulation. Journal of the Operational Research Society 40(3):243–254

[18] Robbins H, Monro S (1951) A stochastic approximation method. Annals of Mathematical Statistics 22:400–407

[19] Tompkins JA, White JA, Bozer YA, Frazelle EH and Tanchoco JMA (2003) Facilities planning, Wiley, NJ x

[20] Le-Duc T, de Koster R (2007) Travel time estimation and order batching in a 2-block warehouse. European Journal of Operational Research 176(1):374–388

# Supply Chain Optimization for the Liquefied Natural Gas Business

Roar Grønhaug<sup>1</sup> and Marielle Christiansen<sup>2</sup>

1 Department of Industrial Economics and Technology Management, Norwegian University of Science and Technology, Norway roar.gronhaug@iot.ntnu.no

2 Department of Industrial Economics and Technology Management, Norwegian University of Science and Technology, Norway marielle.christiansen@iot.ntnu.no

**Summary.** The importance of natural gas as an energy source is increasing. Natural gas has traditionally been transported in pipelines, but ships are more efficient for transportation over long distances. When the gas is cooled down to liquid state it is called liquefied natural gas (LNG). The LNG supply chain consists of exploration, extraction, liquefaction, transportation, storage and regasification. Maritime transportation is a vital part of the LNG supply chain, and LNG is transported in special designed ships, LNG tankers. The demand for LNG tankers has increased considerably as the entire LNG industry continues to see strong growth. Hence, there is a great potential and need for optimization based decision support to manage the LNG fleet, liquefaction plants, and regasification terminals in this business.

Here, we are studying the LNG supply chain in close cooperation with a worldwide actor within the LNG business. This actor is responsible for the LNG supply chain management except the exploration and extraction.

We describe the real planning problem and present both an arc-flow and a path-flow model of the problem. Both models are tested and compared on instances motivated from the realworld problem. It is a very complex problem, so only small instances can be solved to optimality by these solution approaches.

**Key words:** Maritime transportation, Inventory routing

## 1 Introduction

Worldwide, there are large reserves of natural gas. Several existing gas producers are increasing their production capacity and new sources are explored. However, in some of these areas there are no significant markets (for instance North Africa, West Africa, South America, The Caribbean, The Middle East, Indonesia, Malaysia and

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">L. Bertazzi et al. (eds.), Innovations in Distribution Logistics, Lecture Notes</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">in Economics and Mathematical Systems 619, DOI: 10.1007/978-3-540-92944-4,</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">-c 2009 Springer-Verlag Berlin Heidelberg</span></small>

Northwestern Australia). Some of the natural gas is liquefied at these locations for shipping to areas far away where usage of natural gas exceeds indigenous production. Such markets include Japan, Taiwan, Korea, Europe and the U.S. The transformation process from gas to liquefied natural gas (LNG) is done by cooling down the gas at atmospheric pressure at a temperature of $-260^{\circ}\mathrm{F}\left(-162^{\circ}\mathrm{C}\right)$ before loading it into special designed tank ships, LNG tankers. By liquefying the natural gas into LNG the volume is reduced by a factor of 610 [8]. The reduction in volume makes transportation and storage more efficient. In addition, LNG offers greater trade flexibility than pipeline transport, allowing cargoes of natural gas to be delivered where the need is greatest and the commercial terms are most competitive.

Natural gas as an energy source is of increasing importance as the world’s demand for natural gas is expected to increase by 70% between 2002 and 2025 [9]. Hence, the demand for LNG tankers is increasing. In 2007 there were 220 LNG tankers in operation, and 35 LNG tankers were scheduled for delivery in 2007. Furthermore, by 2015 the number of LNG tankers in operation will almost double to 400 [10]. As a consequence of the increasing market for LNG, the supply chain management has become more complex and the need for decision support has become even more evident. We consider a real tactical supply chain optimization problem for LNG including the production volumes, liquefaction, transportation, storage, regasification and sale volumes. Suez Energy International (SEI) is a global energy actor and is facing such a planning problem. The company is involved within most of the LNG supply chain except exploration and extraction, and is using a number of liquefaction plants and regasification terminals throughout the world. For the company’s activity, the LNG can be considered a single product. The natural gas is cooled down at the liquefaction plants, stored at given pick-up ports, and transported at sea by LNG tankers to inventories at delivery ports before regasification. Inventory storage capacities are given at all ports. The production and consumption volumes are variable at all terminals. The transportation at sea is carried out with SEI’s own heterogeneous fleet of LNG tankers. The hold at the LNG tanker is separated into several cargo tanks. It is assumed that an LNG tanker is always fully loaded when it leaves the pick-up port, but it is possible to unload a variable number of cargo tanks at each regasification terminal. In fact, the LNG is at boiling state in the cargo tanks. Thus, some of the LNG evaporates during a voyage. Hence the term boil-off. This gas is used as fuel. The planning problem is to maximize the profit by designing routes and schedules for the fleet, including determining the production and consumption volumes at all terminals, without exceeding the ship capacities and the inventory limits of the storages. We call this problem the LNG inventory routing problem (LNG-IRP).

Maritime transport optimization is a well established field of research within transportation planning with reviews in [12, 13, 5, 4]. Though the attention to maritime transportation has been limited compared to other modes of transportation, we have witnessed an accelerating amount of research in the literature during the last decade and the interest in these types of problems is increasing.

In maritime transportation, usually large quantities are loaded and unloaded at each port call (ship visit at port). Both the (un)loading and transportation are time consuming and expensive. Thus, the potential is great if the planning of the transportation and the inventory management at each end of a sailing leg is integrated. In practice, we can find several maritime supply chains where one of the actors has the responsibility for both the transportation and the inventory management. For instance, [3] studies such a problem for a company producing and consuming ammonia. Here the company both produces and consumes the product and is controlling the fleet of ships. Furthermore, [1] consider a maritime inventory routing problem with multiple chemical and oil products. These products have to be transported in separated compartments on board the ship and stored in separate storages at the ports. Moreover, [11] study a planning problem that integrates both the shipment planning of petroleum products from refineries to depots, and the production scheduling at the refineries. More maritime inventory routing problems are referred in [6].

However, no research on LNG-IRP is reported in the literature as far as we know. With increased focus on this type of problems in the industry, we expect several contributions in near future.

The purpose of this paper is to introduce a new type of problem within maritime transportation and provide two types of formulations for the same problem. Moreover, it will contribute to increased knowledge about the LNG supply chain from an OR point of view.

The rest of the paper is organized as follows: Sect. 2 gives some insights into the LNG industry and describes the real planning problem considered. The problem is formulated as an arc-flow model in Sect. 3, while Sect. 4 is devoted to the path-flow model. Computational results on small instances of the real planning problem are reported in Sect. 5. Finally, concluding remarks and future research follow in Sect. 6.

## 2 Description of a Real LNG Supply Chain Planning Problem

Suez Energy International (SEI) is a global energy actor. The company is a subsidiary of the international conglomerate Suez and together with its sister company, Suez Energy Europe (SEE) has the responsibilities of maintaining Suez’ energy operations. SEI are involved within most of the liquefied natural gas (LNG) supply chain except exploration, extraction, and transportation to end-customers. Hence, the company is involved in liquefaction, transportation, storage and regasification of LNG. In addition, the company can influence the amount produced at the liquefaction plants and sold at the regasification terminals. Figure 1 shows the LNG supply chain and highlights the considered parts of the chain.

SEI is engaged in LNG supply chain planning at all levels, ranging from strategic decisions as determining the fleet size and mix, acquisition of plants and terminals, long-term contracts, to operational planning like determining the speed of each LNG tanker. In this paper, we consider the tactical supply chain planning problem and the typical planning horizon spans two to four months.

At the liquefaction plants the natural gas is cooled down to liquid state. Then, from ports located close to the liquefaction plants, the LNG is transported in special purpose vessels to ports close to storages and regasification terminals. Here, the LNG is converted from the liquefied state to the gaseous state, ready to be moved to the final destination through the natural gas pipeline system.

![](images/page_202_image_2.jpg)

Fig. 1. The LNG supply chain

SEI controls two regasification terminals located in Zeebrugge, Belgium and Boston, USA. It has also 10% equity participation in a liquefaction plant located in Trinidad and Tobago. In addition, the company uses third-party facilities for pickup and deliveries in other parts of the world. SEI currently purchases and distributes approximately 8 million tons of LNG per year from Algeria, Quatar, Trinidad and Tobago. The LNG operations are continuously increasing. For instance, a sales and purchase contract for 2.5 million tons of LNG per year was signed with Yemen LNG in August 2005. This contractual supply is expected to begin in 2009, and has 20 years duration.

Due to the expected increase in activity, SEI sees the need for an advanced decision support tool to coordinate and manage the fleet, and the inventories at both liquefaction and regasification terminals. For that reason, inventory management considerations are included at all ports. A reality consisting of 10 liquefaction plants and 10 regasification terminals is not impossible to imagine in the future. The number of spot cargoes in the LNG business is still limited, but we will see an increase in this activity in the future. In order to limit the size of the model and the level of details, we have disregarded possible spot trade in this paper.

The production of LNG at the liquefaction plants is normally at a maximum level. However, it is possible to regulate the production within certain limits. At each plant there exists given capacities of the storages. Production costs are dependent on volume and plant.

At the other end of the supply chain, the gas is unloaded from the LNG tankers and stored in storages with specified capacities. SEI’s customers are governments, industrial corporations, the service industry, and residential users throughout the world. The sales contracts include fixed contracts where the agreed volume cannot be violated, contracts with lower and upper limits on quantities to deliver, and short term contracts which should be satisfied only if profitable. From this contract structure, we assume that for each port, we can specify upper and lower limits of demand for gas and an associated revenue per day. In reality, the consumption rate varies from day to day.

Extraction of natural gas, and hence the production of LNG, takes place all over the world. Natural gas is transported by either pipe lines or by ship to the customers. The main flows of natural gas and LNG in the world are shown in Fig. 2. Hence, the ports associated to the LNG liquefaction plants and regasification terminals are placed all over the world.

![](images/page_203_image_3.jpg)

Fig. 2. The main flows of natural gas and LNG in the world. Figure from [2]

The LNG is transported by a fleet of LNG tankers controlled by SEI or by the associated company Suez Energy Europe. This fleet consists currently of 6 LNG tankers which they either have ownership over, or have chartered on long-term agreements. However, this number of LNG tankers will increase with increased activity. The LNG tankers have different cost structure, load capacity and specific ship characteristics. The hold of an LNG tanker is separated into several cargo tanks. Since the LNG is at boiling state in the cargo tanks, some of the cargo evaporates each day. This is called boil-off. Each day, the amount of boil-off in each cargo tank is a constant rate of the cargo capacity in the tank. Usually, the boil-off is used as fuel. It is the cargo itself that keeps the tanks cool, so if a cargo tank runs empty, the temperature will gradually increase. It is costly and time consuming to recool the cargo tanks before loading. Thus, there should always be some LNG left in the cargo tanks to keep them cool until (re)loading starts. Then, only a safety level should be left in the cargo tanks. No boil-off is assumed for the active tanks during loading and unloading in a port, while boil-off is considered for the tanks not affected at delivery ports. The loading and unloading of a ship are assumed to take one time period (one day) independent of the quantity loaded.

Successive calls at liquefaction plants are not relevant to consider. Furthermore, we can disregard the safety level from the calculations if we reduce the tank capacities with an appropriate safety level. Hence, when we speak about an ‘empty cargo tank’, there is a safety level of cargo left in the tank. In an optimal plan, an LNG tanker always arrives at a pick-up port and starts loading in the moment all the cargo tanks are empty and departs from the port fully loaded. However, at the delivery ports it is possible to unload partially. This means that several regasification terminals might be called in sequence, and a maximum number of successive delivery ports is given. In practice, this number is two. Due to sloshing problems for some types of LNG tankers, it is assumed that it is impossible to unload partial cargo tanks. Thus, a number of full cargo tanks adjusted for future boil-off until the next call to a liquefaction plant, must be unloaded at each delivery port. Figure 3 shows four snapshots of a voyage for an LNG tanker containing four cargo tanks. In Fig. 3a), the LNG tanker leaves the liquefaction plant fully loaded and the storage there is in one of its extreme situation; empty. The LNG tanker sails to a regasification terminal, and it has to arrive this terminal before the storage is empty. In Fig. 3b), we see that some of the gas has evaporated while sailing. The LNG tanker can then unload one or several of its cargo tanks. In this example, all tanks have been unloaded in one regasification terminal. Then, the LNG tanker returns in Fig. 3d) to the same liquefaction plant and the LNG tanker is just empty when it arrives the port.

![](images/page_204_image_3.jpg)

Fig. 3. LNG tanker inventory

The sailing time from one port to another is calculated based on the speed of the LNG tanker and the distance, but does not depend on the load aboard. There might also be several paths between two ports with different time consumptions and costs. For instance, this gives the possibility to use the Suez Canal or to sail around Africa.

The berth capacity of the ports is limited. Thus, a maximum number of LNG tankers can visit each port in each time period. However, it is possible to wait outside a port before loading and unloading, and the maximum number of waiting days outside each port is given. Normal boil-off is assumed during such waiting days. In contrast, no boil-off is assumed for the time periods from the last port call in a ship route until the end of the planning horizon. There is no natural depot for the LNG tankers. The initial position of an LNG tanker may be at a port or a point at sea. Furthermore, the LNG taker might be empty or loaded, and there is a set of first port call candidates in its route. Since there is no depot for the LNG tankers, there is no requirement for a specified position for any ship at the end of the planning horizon. In fact, the LNG tanker will end their route in one of the ports in the planning problem.

The LNG tankers are very specialized tank ships without any other area of application. In the short-term, there is no option to change the fleet size. The ship costs consist of several components. The fixed costs are the time charter rates which exist for all ships, while the variable costs consist of port and canal fees, and bunker oil costs.

In contrast to pickup and delivery vehicle routing problems [7], the number of calls to a port is not known, the quantity loaded or unloaded at each call is unknown and finally, there exist no pickup and delivery pairs. The LNG-inventory routing problem (LNG-IRP) aims at maximizing the profit by designing ship routes and schedules for the fleet in the planning period. Furthermore, the problem consists of deciding the production volumes of LNG, and determining the level of demand fulfillment. Finally, feasible inventory levels at both port types and load aboard the LNG tankers regarding the ship capacity and boil-off must be ensured.

## 3 Arc-Flow Formulation

This section describes the arc-flow formulation of the LNG-IRP. First, in Sect. 3.1 we introduce the network and describe the ship routing and scheduling constraints for the problem. Then, in Sect. 3.2 we present the constraints representing the ship inventory management. Section 3.3 is devoted to the activities at the ports, including the port inventory management. Finally, the objective function is addressed in Sect. 3.4.

The notation is based on the use of lower-case letters to represent decision variables and indices, while capital letters represent sets, constants and any constant superscripts.

## 3.1 Ship Routing and Scheduling

In the mathematical description of the problem, let N be the set of physical ports indexed by i. This set consists of pick-up ports $N ^ { P }$ and delivery ports $N ^ { D }$ . Further, let $\mathcal { V } ,$ indexed by $\nu _ { \ast }$ represent the heterogeneous fleet of ships (LNG tankers) available for routing and scheduling. Then, the set ${ \cal N } _ { \nu } ^ { P D }$ denotes all ports feasible for ship v (except its origin and destination node). Furthermore, $( \mathcal { N } _ { \nu } , \mathcal { R } _ { \nu } )$ is the total network associated with a specific ship v. Here, $\mathcal { N } _ { \nu }   =   \mathcal { N } _ { \nu } ^ { P D } \cup \{ o ( \nu ) , d ( \nu ) \}$ is the set of ports that ship v can visit, and $o ( \nu )$ and $d ( \nu )$ are the (artificial) origin node and (artificial) destination node, respectively. The set $\mathcal { R } _ { \nu }$ contains all feasible arcs for ship v, which is a subset of $\{ i \in \mathcal { N } _ { \nu } \} \times \{ i \in \mathcal { N } _ { \nu } \}$ . This set will be calculated based on capacity, time and inventory constraints, and other restrictions such as those based on precedence of pick-up and delivery nodes. From these calculations, we can extract the sets $\mathcal { N } _ { \nu } ^ { P } =$ $\mathcal { N } ^ { P } \cap \mathcal { N } _ { v }$ and $\mathcal { N } _ { \nu } ^ { D } = \mathcal { N } ^ { D } \cap \mathcal { N } _ { \nu }$ consisting of pick-up and delivery nodes that ship v may call, respectively.

The length of the planning horizon is given by the parameter $T ^ { M X }$ . Moreover, $\mathcal { T }$ denotes the set of time periods, $\mathcal { T } = \left\{ 1 , 2 , \ldots , T ^ { \mathit { M X } } \right\}$ , which is indexed by t. Let the parameter $T _ { i j \nu }$ represent the sailing time on arc $( i , j )$ for ship v. Sailing on arc $( i , i )$ is considered waiting outside port i, $T _ { i i v } \: = \: 1$ . The maximum number of time periods a ship can wait outside a port before loading or unloading is denoted $T ^ { W }$ Cargo handling, i.e. loading and unloading, is assumed to take one time period. To ease the representation, the cargo handling at port i is assumed to take place during the first time period on the sailing on arc $( i , j ) , i \neq j .$ Each ship has a number of cargo tanks, $W _ { \nu } ^ { M X }$ , where the set of cargo tanks on each ship is given by $\mathcal { W } _ { \nu }$ and $w$ is the corresponding index.

The binary flow variable $x _ { i j \nu t } ,   ( i , j ) \in \mathcal { A } _ { \nu } ,   \nu \in \mathcal { V } ,   t \in \mathcal { T }$ serves two purposes; sailing between two ports and waiting outside a port. If the variable equals 1 and $i = j ,$ ship v waits one time period outside port i. On the other side, when $i \neq j$ and $x _ { i j v t } = 1$ , ship v either loads or unloads at port i in time period t before it immediately starts sailing toward port j. The decision to load or unload a cargo tank is handled by the binary variable $z _ { i w \nu t } ,   i \in \mathcal { N } _ { \nu } ^ { P D } ,   w \in \mathcal { W } _ { \nu } ,   v \in \mathcal { V } ,   t \in \mathcal { T }$ , which equals 1 if ship v decides to load or unload cargo tank w in port i during time period t. Furthermore, the binary variable $u _ { i \nu t } ,   i \in \mathcal { N } _ { \nu } ^ { P D } ,   \nu \in \mathcal { V } ,   t \in \mathcal { T }$ equals 1 if ship v loads or unloads any cargo tank in port i during time period t.

In order to increase the readability of the arc-flow model, we eliminate the possibility of several paths between two nodes. However, this can easily be included in the model by introducing an additional index for the paths on the flow variable.

Then, the routing and scheduling part of the arc-flow LNG-IRP formulation is as follows:

$$
\sum_ {i \in \mathcal {N} _ {v} ^ {P D}} x _ {j i v t} - \sum_ {i \in \mathcal {N} _ {v} ^ {P D} | t > T _ {i j v}} x _ {i j v (t - T _ {i j v})} = 0, \quad \forall j \in \mathcal {N} _ {v} ^ {P D}, v \in \mathcal {V}, t \in \mathcal {T},\tag{1}
$$

$$
\sum_ {j \in \mathcal {N} _ {v}} x _ {o (v) j v t} = 1,
$$

$$
\forall v \in \mathcal {V}, t = 1,\tag{2}
$$

$$
\sum_ {t \in \mathcal {T}} \sum_ {i \in \mathcal {N} _ {v}} x _ {i d (v) v t} = 1,
$$

$$
\forall v \in \mathcal {V}.\tag{3}
$$

Constraints (1)-(3) describe the flow on the route used by ship v. The first sailing from ship v’s origin node, o(v), is handled by constraints (2), while constraints (3) give the end conditions for ship v, i.e. the ship must end its route in the destination node d(v).

$$
\sum_ {j \in \mathcal {N} _ {v} | j \neq i} x _ {i j v t} - u _ {i v t} = 0,
$$

$$
\forall i \in \mathcal {N} _ {v} ^ {P D}, v \in \mathcal {V}, t \in \mathcal {T},\tag{4}
$$

$$
x _ {i i v t} u _ {i v t} = 0,
$$

$$
\forall i \in \mathcal {N} _ {v} ^ {P D}, v \in \mathcal {V}, t \in \mathcal {T},\tag{5}
$$

$$
\sum_ {\tau = t \mid \tau \leq T ^ {M X} - T ^ {W} - 2 \min _ {j} \{T _ {i j v} \}} ^ {t + T ^ {W} + 2 \min _ {j} \{T _ {i j v} \}} x _ {i i v \tau} \leq T ^ {W}, \quad \forall i \in \mathcal {N} _ {v} ^ {P D}, v \in \mathcal {V}, t \in \mathcal {T},\tag{6}
$$

$$
\begin{array}{c} x _ {i j v t} \left(\sum_ {w \in \mathcal {W} _ {v}} z _ {i w v t} + \sum_ {\tau = t | \tau \leq T ^ {M X} - T _ {i j v} w \in \mathcal {W} _ {v}} ^ {t + T ^ {W}} \sum_ {} z _ {j w v (\tau + T _ {i j v})} - W _ {v} ^ {M X}\right) = 0, \\ \forall i \neq j, i \in \mathcal {N} _ {v} ^ {D}, j \in \mathcal {N} _ {v} ^ {D}, (i, j) \in \mathcal {A} _ {v}, v \in \mathcal {V}, t \in \mathcal {T}. \end{array}\tag{7}
$$

In constraints (4) we describe the connection between the cargo handling and the sailing. If a ship starts sailing between two ports, it must either load or unload depending on the type of port. Moreover, constraints (5) state that a ship cannot wait outside a port, i.e. traverses on an arc (i, i), in the same time period it loads or unloads. Constraints (6) limit the number of waiting days outside port i for ship v. Furthermore, constraints (7) assure that if a ship calls two consecutive delivery ports, all cargo tanks must unload at these ports.

$$
z _ {i w v t} \in \{0, 1 \}, \quad \forall i \in \mathcal {N} _ {v} ^ {P D}, w \in \mathcal {W} _ {v}, v \in V, t \in \mathcal {T},\tag{8}
$$

$$
u _ {i v t} \in \{0, 1 \}, \quad \forall i \in \mathcal {N} _ {v} ^ {P D}, v \in \mathcal {V}, t \in \mathcal {T},\tag{9}
$$

$$
x _ {i j v t} \in \{0, 1 \}, \quad \forall (i, j) \in \mathcal {A} _ {v}, v \in V, t \in \mathcal {T}.\tag{10}
$$

Finally, the formulation involves binary requirements (8)-(10).

A possible route through the network is illustrated in Fig. 4. The ship starts from its origin node in time period 1. The ship is either at sea and spends one time period to reach pick-up port i or it waits outside port i in this time period. After the arrival at port i in time period 2 the ship loads its cargo tanks in this time period, before it sails to delivery port j. The sailing time between i and j is three time periods. When the ship has unloaded some of its cargo tanks in port j in time period 6, the ship starts sailing towards delivery port k in time period 7. Here, the ship unloads the rest of the cargo tanks and starts sailing towards port i. The ship arrives port i in time period 14, but waits one day outside the port, before the ship loads all its cargo tanks and sails towards the destination node.

![](images/page_208_chart_3.jpg)

Fig. 4. Illustration of a possible route through the network for ship v

## 3.2 Ship Inventory Management

In order to describe the ship inventory management part of the LNG-IRP, we need the following additional notation.

The capacity of cargo tank w on ship v is given by $L _ { w v }$ . There is no loading or unloading at the origin node $o ( \nu )$ , but all cargo tanks have an initial load at the beginning of the planning horizon, $L _ { w v } ^ { O }$ . Furthermore, the parameter $I _ { i } ,$ equals −1 if port i is a pick-up port, and 1 if the port is an delivery port. The boil-off parameter $B _ { w v } ^ { F } ,$ states the amount of cargo evaporating in each time period. A duty is a journey which starts when a ship either loads all its cargo tanks in a pick-up port or leaves the origin node, and the duty ends immediately before the ship starts loading at the next call at a pick-up port or when the ship reaches the destination node. We can for ship v calculate upper and lower bounds on the total sailing time including waiting for the duties with visiting delivery port i. These upper and lower bounds are denoted $T _ { i \nu } ^ { D M N }$ and $T _ { i \nu } ^ { D M X }$ , respectively.

The load in cargo tank w at ship v at the end of time period t is measured by the continuous variable $l _ { w v t } , w \in \mathcal { W } _ { v } , v \in \mathcal { V } , t \in \mathcal { T }$ . Note the initial condition $l _ { w v 0 } = L _ { w v } ^ { O }$ Finally, the continuous variable $q _ { i w \nu t } ,   i \in \mathcal { N } _ { \nu } ^ { P D } ,   w \in \mathcal { W } _ { \nu } ,   \nu \in \mathcal { V } ,   t \in \mathcal { T }$ measures the amount of cargo loaded into or unloaded from cargo tank w at ship v in time period t.

$$
\begin{array}{c} - l _ {w v t} + l _ {w v (t - 1)} + B _ {w v} ^ {F} \left(\sum_ {i \in \mathcal {N} _ {v} ^ {P D}} z _ {i w v t} + \sum_ {i \in \mathcal {N} _ {v}} \sum_ {\tau = 1} ^ {t - 1} x _ {i d (v) v \tau}\right) \\ - \sum_ {i \in \mathcal {N} _ {v} ^ {P D}} I _ {i} q _ {i w v t} = B _ {w v} ^ {F}, \forall w \in \mathcal {W} _ {v}, v \in \mathcal {V}, t \in \mathcal {T}, \end{array}\tag{11}
$$

$$
W _ {v} ^ {M X} u _ {i v t} - \sum_ {w \in \mathcal {W} _ {v}} z _ {i w v t} = 0, \quad \forall i \in \mathcal {N} _ {v} ^ {P}, v \in \mathcal {V}, t \in \mathcal {T},\tag{12}
$$

$$
q _ {i w v t} - L _ {w v} z _ {i w v t} = 0, \quad \forall i \in \mathcal {N} _ {v} ^ {P}, w \in \mathcal {W} _ {v}, v \in \mathcal {V}, t \in T,\tag{13}
$$

$$
u _ {i v t} - z _ {i w v t} \geq 0,
$$

$$
\forall i \in \mathcal {N} _ {v} ^ {D}, w \in \mathcal {W} _ {v}, v \in \mathcal {V}, t \in T,\tag{14}
$$

$$
u _ {i v t} - \sum_ {w \in \mathcal {W} _ {v}} z _ {i w v t} \leq 0, \quad \forall i \in \mathcal {N} _ {v} ^ {D}, v \in \mathcal {V}, t \in \mathcal {T},\tag{15}
$$

$$
q _ {i w v t} - \left(L _ {w v} - B _ {w v} ^ {F} T _ {i v} ^ {D M X}\right) z _ {i w v t} \geq 0, \quad \forall i \in \mathcal {N} _ {v} ^ {D}, w \in \mathcal {W} _ {v}, v \in \mathcal {V}, t \in \mathcal {T},\tag{16}
$$

$$
q _ {i w v t} - \left(L _ {w v} - B _ {w v} ^ {F} T _ {i v} ^ {D M N}\right) z _ {i w v t} \leq 0, \quad \forall i \in \mathcal {N} _ {v} ^ {D}, w \in \mathcal {W} _ {v}, v \in \mathcal {V}, t \in \mathcal {T},\tag{17}
$$

$$
0 \leq l _ {w v t} \leq L _ {w v}, \quad \forall w \in W _ {v}, v \in V, t \in \mathcal {T}.\tag{18}
$$

The inventory balance on the ships are handled by constraints (11), which calculate the volume of LNG in each cargo tank on each ship in every time period. The amount of LNG in a cargo tank on a ship decreases at sea at an amount $B _ { w v } ^ { F }$ in each time period, although there is no boil-off from a cargo tank that is being loaded or unloaded. In addition, there is no boil-off from the cargo tanks on a ship at the destination node. An illustration on how the variables and parameters affect the ship inventory is given in Fig. 5. Constraints (12)-(13) ensure that all cargo tanks are fully loaded at pick-up ports, when a loading starts. On the other hand, constraints (14)- (15) ensure that if a ship is unloading at least one cargo tank is unloaded, and vice versa. Moreover, constraints (16) give lower limits to the amount of LNG unloaded at the delivery ports, where the amount of cargo not delivered must be less or equal to the accumulated boil-off during the longest possible trip between two pick-up ports. The boil-off rate is usually a small percentage. Hence, constraints (16) allow only one unloading of a cargo tank before it is reloaded. Furthermore, constraints (16) in combination with constraints (7) limit the ships to sail to maximum two consecutive delivery ports. The upper limits on the unloading volumes at the delivery ports are given by (17). Finally, bounds on the ship inventory variable are described in constraints (18).

If a ship ends its route in an delivery port, the cargo tanks that have been unloaded should have sufficient LNG left aboard to reach a pick-up port. This amount is represented by the parameter $L _ { w v } ^ { E }$ . The constraints required for handling the end conditions for the delivery ports are as follows:

$$
x _ {i d (v) v t} z _ {i w v t} \left(l _ {w v t} - L _ {w v} ^ {E}\right) = 0, \quad \forall i \in \mathcal {N} _ {v} ^ {D}, w \in \mathcal {W} _ {v}, v \in \mathcal {V}, t \in \mathcal {T},\tag{19}
$$

![](images/page_210_image_2.jpg)

Fig. 5. Inventory balance for the ships

$$
\sum_ {\tau = t} ^ {t + T ^ {W}} x _ {i d (v) v \tau} \sum_ {j \in \mathcal {N} _ {v} ^ {D}} x _ {j i v (t - T _ {i j v})} \left(l _ {w v t} - L _ {w v} ^ {E}\right) = 0,
$$

$$
\forall i \in \mathcal {N} _ {\nu} ^ {D}, w \in \mathcal {W} _ {\nu}, v \in \mathcal {V}, t \in \mathcal {T}.\tag{20}
$$

Constraints (19) ensure that if there is an unloading immediately before the destination node, the cargo left in these cargo tanks at the unloading node should equal the parameter $L _ { w v } ^ { E }$ . Constraints (20) have similar purpose when a ship calls two consecutive delivery ports before the destination node. If a ship calls two consecutive delivery ports, all cargo tanks must have been unloaded when leaving the second delivery port. Thus, there is no need for including $\mathcal { Z } _ { i w v t } \mathrm { ~ \bf { O f } ~ } \mathcal { Z } _ { j w v t }$ in constraints (20).

## Linearization of Constraints

Constraints (19)–(20) are nonlinear when we relax the binary requirements of the variables. In this section we linearize those constraints.

$$
l _ {w v t} - L _ {w y} ^ {E} x _ {i d (v) v t} \geq 0, \quad \forall i \in \mathcal {N} _ {v} ^ {D}, w \in \mathcal {W} _ {v}, v \in \mathcal {V}, t \in \mathcal {T},\tag{21}
$$

$$
l _ {w v t} + L _ {w v} \left(x _ {i d (v) v t} + z _ {i w w t}\right) \leq 2 L _ {w v} + L _ {w w} ^ {E}, \quad \forall i \in \mathcal {N} _ {v} ^ {D}, w \in \mathcal {W} _ {v}, v \in \mathcal {V}, t \in \mathcal {T}.\tag{22}
$$

Constraints (21) assure that all ships should have at least $L _ { w v } ^ { E }$ of LNG aboard each cargo tank when they reach the destination node. Furthermore, constraints (22) are bounding when $x _ { i d ( \nu ) \nu t } z _ { i w \nu t }   =   1$ . When $x _ { i d ( \nu ) \nu t } z _ { i w \nu t }   =   1$ , i.e. when a ship unloads a cargo tank before sailing to the destination node, constraints (22) limits the cargo aboard that cargo tank to be less or equal than $L _ { w v }$ . Hence, constraints (21)-(22), can be regarded as linearized reformulations of constraints (19).

$$
l _ {w v \left(t + T _ {i d (v) v}\right)} + L _ {w v} \left(\sum_ {\tau = t} ^ {t + T ^ {W}} x _ {i d (v) v \tau} + \sum_ {j \in \mathcal {N} _ {v} ^ {D}} x _ {j i v t}\right) \leq 2 L _ {w v} + L _ {w v} ^ {E},
$$

$$
\forall i \in \mathcal {N} _ {v} ^ {D}, w \in \mathcal {W} _ {v}, v \in \mathcal {V}, t \in \mathcal {T}.\tag{23}
$$

When a ship unloads at two consecutive delivery ports before sailing to the des tination node, there should be exact $L _ { w v } ^ { E }$ of LNG left in the cargo tanks. Constraints (23) are bounding when a ship calls consecutive delivery ports before sailing to the destination node. Then, the cargo left in each cargo tank should be equal or less than $L _ { w v } ^ { E }$ . Hence, we can use constraints (23) in combination with constraints (21) to linearize constraints (20).

## 3.3 Port Operations and Inventory Management

Here, the constraints handling both the port operations and the inventory management at the ports are presented. We need to introduce the following additional parameters and variables:

The daily production and sales of LNG at the ports have to be within a given interval $\left[ \underline { { Y } } _ { i t } , \overline { { Y } } _ { i t } \right]$ , which can change from one time period to another. Furthermore, the inventory levels at the ports should be within the upper and lower limits $\left[ \underline { { S } } _ { i } , \overline { { S } } _ { i } \right]$ The maximum number of ships at a port in a time period is given by the parameter $N _ { i } ^ { C A P }$

The sales and production of LNG are given by the continuous variable $y _ { i t } ,   i \in \mathcal { N } ,$ $t \in \mathcal { T }$ , while the continuous variable $s _ { i t } ,   i \in \mathcal { N } ,   t \in \mathcal { T }$ represents the inventory level at the liquefaction plants and regasification terminals in the different time periods. Note that $s _ { i 0 }$ represents the initial inventory.

$$
s _ {i t} - s _ {i (t - 1)} - \sum_ {v \in \mathcal {V}} \sum_ {w \in \mathcal {W} _ {v}} I _ {i} q _ {i w v t} + I _ {i} y _ {i t} = 0, \quad \forall i \in \mathcal {N}, t \in \mathcal {T},\tag{24}
$$

$$
\sum_ {v \in \mathcal {V}} u _ {i v t} \leq N _ {i} ^ {C A P},
$$

$$
\forall i \in \mathcal {N}, t \in \mathcal {T},\tag{25}
$$

$$
\underline {{S}} _ {i} \leq s _ {i t} \leq \overline {{S}} _ {i},
$$

$$
\forall i \in \mathcal {N}, t \in \mathcal {T},\tag{26}
$$

$$
\underline {{Y}} _ {i t} \leq y _ {i t} \leq \overline {{Y}} _ {i t},
$$

$$
\forall i \in \mathcal {N}, t \in \mathcal {T}.\tag{27}
$$

The port inventory balances are given by constraints (24), and are further illustrated in Fig. 6. Constraints (25) ensure that the port capacity in the number of ships in each time period is not exceeded. The upper and lower bounds for the variables are given in constraints (26)-(27).

![](images/page_211_image_15.jpg)

![](images/page_211_image_16.jpg)

Regasification terminal

Liquefaction terminal

Fig. 6. Inventory balance at regasification and liquefaction terminals

## 3.4 Objective Function

Finally, we can present the objective function for the arc-flow LNG-IRP formulation. We need to introduce the following revenue and cost parameters.

The parameter $R E V _ { i t }$ represents the unit revenue in each time period for selling LNG to the customers at the delivery ports, while $C O S T _ { i t }$ is the unit cost from producing LNG at the pick-up ports. Finally, $C _ { i j v }$ is the transportation cost, i.e. the cost of traversing arc $( i , j )$ for ship v. The transportation cost parameter is a compound cost parameter, consisting of daily operating costs for ship v, port fees at port i, and any canal fees.

$$
\max \sum_ {i \in \mathcal {N} ^ {D}} \sum_ {t \in \mathcal {T}} R E V _ {i t} y _ {i t} - \sum_ {i \in \mathcal {N} ^ {P}} \sum_ {t \in \mathcal {T}} C O S T _ {i t} y _ {i t} - \sum_ {(i, j) \in \mathcal {A}, v \in \mathcal {V}} \sum_ {t \in \mathcal {T}} C _ {i j v} x _ {i j v t}\tag{28}
$$

The objective function (28) maximizes total profit of selling LNG to endcustomers while minimizing the costs of production and transportation.

## 4 Path-Flow Formulation

In the arc-flow formulation, the routes including arrivals times and load quantities are constructed based on the values on the variables, while these routes are enumerated a priori and feed into the path-flow formulation. The model is presented in Sect. 4.1, while the algorithm for enumerating the paths is described in Sect. 4.2.

## 4.1 The Model

In the path-flow formulation of the LNG-IRP, a route $r \in \mathcal { R } _ { v }$ contains the geographical route and the schedule with information about the arrival times for all port calls for ship v in the planning horizon. In addition, the route contains information about the quantities loaded and unloaded at the liquefaction plants and regasification terminals, respectively.

The parameter $Z _ { i v t r }$ equals 1 if ship v calls port i in time period t on route r and 0 otherwise, while the corresponding (un)loading volume is given by the parameter $Q _ { i v t r }$ . The cost of sailing route r for ship v is given by the parameter $C _ { \nu r }$ . The cost parameters are composed of ship operation cost, port fees, and canal fees.

The binary variable $\lambda _ { v r } ,   v \in \mathcal { V } ,   r \in \mathcal { R } _ { v }$ is the ship route variable, and equals 1 if ship v chooses to sail route r, and 0 otherwise.

Then, the path-flow formulation of the LNG-IRP can be modeled as follows:

$$
\max \sum_ {i \in \mathcal {N} ^ {D}} \sum_ {t \in \mathcal {T}} R E V _ {i t} y _ {i t} - \sum_ {i \in \mathcal {N} ^ {P}} \sum_ {t \in \mathcal {T}} C O S T _ {i t} y _ {i t} - \sum_ {v \in \mathcal {V}} \sum_ {r \in \mathcal {R} _ {v}} C _ {v r} \lambda_ {v r},\tag{29}
$$

subject to

$$
s _ {i t} - s _ {i (t - 1)} - \sum_ {v \in \mathcal {V}} \sum_ {r \in \mathcal {R} _ {v}} I _ {i} Q _ {i v t r} \lambda_ {v r} + I _ {i} y _ {i t} = 0, \quad \forall i \in \mathcal {N}, t \in \mathcal {T},\tag{30}
$$

$$
\sum_ {v \in \mathcal {V}} \sum_ {r \in \mathcal {R} _ {v}} Z _ {i v t r} \lambda_ {v r} \leq N _ {i} ^ {C A P},
$$

$$
\forall i \in \mathcal {N}, t \in \mathcal {T},\tag{31}
$$

$$
\underline {{S}} _ {i} \leq s _ {i t} \leq \overline {{S}} _ {i},
$$

$$
\forall i \in \mathcal {N}, t \in \mathcal {T},\tag{32}
$$

$$
\underline {{Y}} _ {i t} \leq y _ {i t} \leq \overline {{Y}} _ {i t},
$$

$$
\forall i \in \mathcal {N}, t \in \mathcal {T},\tag{33}
$$

$$
\sum_ {r \in \mathcal {R} _ {v}} \lambda_ {v r} = 1,
$$

$$
\forall v \in \mathcal {V},\tag{34}
$$

$$
\lambda_ {v r} \in \{0, 1 \},
$$

$$
\forall v \in \mathcal {V}, r \in \mathcal {R} _ {v}.\tag{35}
$$

The objective function (29) maximizes the profit from the LNG activities. The inventory balances are given in constraints (30), while the port capacity constraints are given by (31). The bounds in constraints (32)-(33) are identical to constraints (26)-(27). Constraints (34) are the convexity constraints, limiting the ships to sail exactly one route. Finally, the formulation involves binary requirements (35) on the ship route variables $\lambda _ { \nu r }$

## 4.2 Path Enumeration Algorithm

Here, we present an algorithm for complete enumeration of all possible paths, called routes, for the path-flow LNG-IRP formulation. By use of a recursive algorithm we can identify all possible routes with information regarding the geographical route, the arrival times and the number of cargo tanks loaded and unloaded at all ports. When a route has been found, the algorithm must identify all the duties within the routes. These duties are in fact distinct subpaths in the route. The algorithm must calculate the aggregated boil-off from each cargo tank during the duties in order to calculate the exact amount of cargo unloaded at the delivery ports. This can be expressed mathematically if we introduce some new notation. Let ${ \mathcal { A } } _ { \nu r } ,$ indexed by $d ,$ denote the set of duties for ship v on route r. The aggregated boil-off in cargo tank w on ship v on duty d on route r is given by $B _ { w v r d } ^ { F A } .$ . Furthermore, $X _ { i j \nu t r d } = 1$ if arc $( i , j )$ is traversed by ship v starting in time period t on duty d on route $r ,$ and 0 otherwise. Moreover, $Z _ { i w v t r d } ^ { \mathcal { A } } = 1$ if ship v loads or unloads cargo tank $w$ in time period t on duty d on route r, and 0 otherwise.

$$
\begin{array}{l} B _ {w v r d} ^ {F A} = B _ {w v} ^ {F} \left(\sum_ {(i, j) \in \mathcal {A} _ {v}} \sum_ {t \in \mathcal {T}} X _ {i j v t r d} T _ {i j v} - \sum_ {i \in \mathcal {N} _ {v} ^ {P D}} \sum_ {t \in \mathcal {T}} Z _ {i w v t r d} ^ {\varDelta}\right), \\ \forall w \in \mathcal {W} _ {v}, v \in \mathcal {V}, r \in \mathcal {R} _ {v}, d \in \varDelta_ {v r}, \\ Q _ {i v t r} = \left\{ \begin{array}{l} \sum_ {w \in \mathcal {W} _ {v}} \sum_ {d \in \varDelta_ {v r}} Z _ {i w v t r d} ^ {\varDelta} L _ {w v}, \forall i \in \mathcal {N} _ {v} ^ {P}, v \in \mathcal {V}, t \in \mathcal {T}, r \in \mathcal {R} _ {v}, \\ \sum_ {w \in \mathcal {W} _ {v}} \sum_ {d \in \varDelta_ {v r}} Z _ {i w v t r d} ^ {\varDelta} \left(L _ {w v} - B _ {w v r d} ^ {F A}\right), \forall i \in \mathcal {N} _ {v} ^ {D}, v \in \mathcal {V}, t \in \mathcal {T}, r \in \mathcal {R} _ {v}, \end{array} \right. \\ Z _ {i v t r} \geq Z _ {i w v t r d} ^ {\varDelta}, \forall i \in \mathcal {N} _ {v}, w \in \mathcal {W} _ {v}, v \in \mathcal {V}, t \in \mathcal {T}, r \in \mathcal {R} _ {v}, d \in \varDelta_ {v r}. \end{array}\tag{36}
$$

(37)

(38)

With equations (36)–(38) we can calculate the input from the path enumeration algorithm to the path-flow model. In equations (36) we calculate the aggregated boil-off during a duty. The aggregated boil-off is used as input when calculating the amount of cargo loaded and unloaded at the ports in equations (37). Finally, equations (38) gives the relation between the cargo tank (un)loading parameter on a duty and the ship call parameter.

![](images/page_214_image_6.jpg)

Fig. 7. Illustration of a possible route through the network for ship v and the corresponding cargo tank levels

Figure 7 illustrates a possible route through the network for a ship with two cargo tanks. The ship loads both its cargo tanks in time period 2. Then it unloads one cargo tank in time period 6 and the other one in time period 11. Some LNG is left in the cargo tanks for the boil-off after the tanks have been unloaded. This boil-off keeps the cargo tanks cool and is also used as fuel until the cargo tanks are reloaded in time period 15.

The pseudocode for the path enumeration algorithm is described in Algorithm 1 and Algorithm 2. Here, Algorithm 1 initializes the path enumeration algorithm, while the recursive part of the algorithm which searches for all paths is given in Algorithm 2. To illustrate how the algorithm works we use the example from Fig. 7. The path enumeration algorithm will first identify the complete route, then it will identify the three duties in the network. The first duty starts in the origin node and ends in port i in time period 2. The second one starts in time period 2 when the ship leaves port i, and ends in time period 15 when the ship once again will leave port i. Note that the waiting day outside port i in time period 14 is considered belonging to the second duty. Finally, the third duty both starts and ends in time period 15, as it covers the sailing from port i to the destination node $d ( \nu )$

<div class="docvortex-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Algorithm 1 initializePath
for all $v \in \mathcal{V}$ do
    $r = 0$, the route numbering starts from 0 for each ship
    $N^{LIST} = \emptyset$, the list of nodes in the route
    call createPath$(r, o(v), N^{LIST})$
end for
</div>

<div class="docvortex-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Algorithm 2 createPath(r, i, $N^{INLIST}$)
$N^{LIST} = N^{INLIST} \cup \{i\}$
for all $j|(i, j) \in \mathcal{A}_v$ do
    if $j \neq d(v)$ then
        call createPath(r, j, $N^{LIST}$)
    else
        $N^{LIST} = N^{LIST} \cup \{j\}$
        Identify all duties in $N^{LIST}$ and create the set $\Delta_{vr}$ and the tables $X_{ijvtrd}$, $Z_{ivtr}$, and $Z_{iwvtrd}^\Delta$
        Calculate the boil-off, $B_{wvrd}^{FA}$, in each duty with equations (36)
        Calculate the quantity loaded or unloaded, $Q_{ivtr}$, with equations (37)
        $r = r + 1$
    end if
end for
</div>

For instance, if the cargo tanks have a capacity of $^ { 7 5 , 0 0 0 } \mathrm { m } ^ { 3 }$ each and the boiloff is $1 1 5   \mathrm { ~ m } ^ { 3 }$ , we can calculate the aggregated boil-off and the amount of cargo unloaded at the ports. The aggregated boil-off for cargo tank 1 on the second duty is then calculated based on a 13 time period long duty, less one time period for loading and one for unloading: $B _ { 1 y r 2 } ^ { F A }   =   1 1 5   ( 1 3 - 2 )   =   1 2 6 5   \mathrm { ~ m } ^ { 3 }$ . Note that the loading in time period 15 belongs to the third duty. Then, if cargo tank 1 is unloaded at port j in time period $6 ,   7 3 ,   7 3 5 ~ \mathrm { m } ^ { 3 }$ will be unloaded there. Since the two cargo tanks are identical, the second tank will unload $^ { 7 3 , 7 3 5 } \mathrm { m } ^ { 3 }$ at port k in time period 11.

## 5 Computational Results

The purpose of the computational study is to evaluate the two proposed model formulations of the LNG-IRP, the arc-flow formulation presented in (1)–(28), and the path-flow formulation presented in (29)–(35). The models have been solved by use of XPRESS Optimizer v 17.1 on a computer with a 3 GHz processor and 8 GB RAM running on Rock Cluster v 4.2.1 operating system. Furthermore, the path enumeration algorithm presented in Sect. 4.2 has been programmed in C++ and solved on the same architecture.

We have created 21 instances motivated by the real planning problem faced by Suez Energy International. An overview of these instances is presented in Table 1. In this table the number of ships, cargo tanks, ports, and time periods are given for each instance. The number of pick-up and delivery ports are given in parenthesis behind the total number of ports. The number of ships ranges from 1 to 5 depending on the instance, while the number of ports is between 3 and 6. Keep in mind that each port may have ship calls several times during the planning period. Furthermore, the instances have 30, 45, or 60 time periods. To be able to test how the time horizon affect the solution time, some instances share most characteristics, but have different number of time periods. For instance, instance 1–3 have the same physical network and similar upper and lower bounds on production and sales, and 30, 45, and 60 time periods, respectively. The other instances can also be grouped similarly (4–6, 7–9, . . .).

The number of rows and columns for the instances for both formulations are presented in Table 2. Note that the number of integer columns for the path-flow formulation is the number of routes for the ships. This number gives some indication of the complexity of the problems, and how the instances escalate with the number of time periods. As we can see from the table, the path-flow formulation scales very poorly with respect to the number of time periods. Furthermore, for instances #9 and #15 we were not able to enumerate all routes as the optimizer ran out of memory during the enumeration process. For the other instances the number of routes spans from 426 for instance #10 to more than 1.5 million for instance #21.

In Table 3 the solution times for each instance are reported. For both formulations, the table reports the time to solve the linear relaxation, first integer solution, best integer solution, and the total solution time. All these solution times are measured starting from the moment the optimizer starts solving the problem, after the complete matrix has been fed into the solver. Maximum running time for the instances is 10 h. Thus, if the search is not completed within the time limit, the search is interrupted. In addition, the table reports the time needed for the path enumeration algorithm to enumerate all routes and feed them into the solver for the path-flow formulation.

The LNG-IRP is hard to solve. In general, both formulations solve the minor instances efficiently, while both formulations have problems with solving the instances with longer planning horizon to optimality. The path-flow formulation is the most efficient formulation with respect to total solution time for 7 of the instances, while the arc-flow performs better for 7 when we disregard 2 instances where we only have test results from the arc-flow formulation. The path-flow formulation suffers from its poor scaling capacity, which leads to large solution time even for the LP relaxation. For instance, solving the LP relaxation for instance #3 with the path-flow formulation is almost 2 h, while the corresponding solution time for the arc-flow formulation is 0 s. As a consequence of the long solution time for the path-flow formulation’s LP relaxation, the time to find the first integer solution is longer than for the arc-flow formulation for 11 of the instances, and faster for only 3 of the instances.

Table 1. Instance overview

| # | Ships | Tanks | Ports (P,D) | Time Periods |
| --- | --- | --- | --- | --- |
| 1 | 1 | 2 | 4(1,3) | 30 |
| 2 | 1 | 2 | 4(1,3) | 45 |
| 3 | 1 | 2 | 4(1,3) | 60 |
| 4 | 2 | 2 | 3(1,2) | 30 |
| 5 | 2 | 2 | 3(1,2) | 45 |
| 6 | 2 | 2 | 3(1,2) | 60 |
| 7 | 2 | 2 | 4(2,2) | 30 |
| 8 | 2 | 2 | 4(2,2) | 45 |
| 9 | 2 | 2 | 4(2,2) | 60 |
| 10 | 2 | 1 | 5(2,3) | 30 |
| 11 | 2 | 1 | 5(2,3) | 45 |
| 12 | 2 | 1 | 5(2,3) | 60 |
| 13 | 2 | 2 | 5(2,3) | 30 |
| 14 | 2 | 2 | 5(2,3) | 45 |
| 15 | 2 | 2 | 5(2,3) | 60 |
| 16 | 3 | 1 | 4(2,2) | 30 |
| 17 | 3 | 1 | 4(2,2) | 45 |
| 18 | 3 | 1 | 4(2,2) | 60 |
| 19 | 5 | 1 | 6(3,3) | 30 |
| 20 | 5 | 1 | 6(3,3) | 45 |
| 21 | 5 | 1 | 6(3,3) | 60 |

The solution values and the MIP-gaps are presented in Table 4. The MIP-gap is defined as |MIP\*-Bound\*| /Bound\*, where Bound\* is the best bound on the solution from the branch-and-bound procedure and MIP\* is the best (mixed) integer solution. For the instances that were not solved to optimality, the MIP-gaps are in the interval [2.9%, 42.9%]. One of the reasons for the large MIP-gaps is the poor linear relaxation for the LNG-IRP. If we define the LP-gap as the percentage deviation between the best MIP solution and the LP solution, |MIP\*-LP\*| /LP\*, the average LP-gap is 19, 4% for both model formulations. This indicates that for some of the instances where we did not manage to prove the optimal solution, the best integer solution found might be near optimal or even the optimal solution.

Table 2. Dimensions of the instances

<table><tr><td></td><td colspan="3">Arc-flow</td><td colspan="3">Path-flow</td></tr><tr><td>#</td><td>Rows</td><td>Columns</td><td>Int columns</td><td>Rows</td><td>Columns</td><td>Int columns</td></tr><tr><td>1</td><td>2,072</td><td>1,411</td><td>871</td><td>243</td><td>1,791</td><td>1,551</td></tr><tr><td>2</td><td>3,107</td><td>2,116</td><td>1,306</td><td>363</td><td>63,101</td><td>62,741</td></tr><tr><td>3</td><td>4,142</td><td>2,821</td><td>1,741</td><td>483</td><td>2,534,165</td><td>2,533,685</td></tr><tr><td>4</td><td>2,764</td><td>2 044</td><td>1,384</td><td>184</td><td>1,110</td><td>930</td></tr><tr><td>5</td><td>4,144</td><td>3,064</td><td>2,074</td><td>274</td><td>28 348</td><td>28,078</td></tr><tr><td>6</td><td>5,524</td><td>4,084</td><td>2,764</td><td>364</td><td>849,858</td><td>849,498</td></tr><tr><td>7</td><td>3,424</td><td>2,764</td><td>1,924</td><td>244</td><td>9,018</td><td>8,778</td></tr><tr><td>8</td><td>5,134</td><td>4 144</td><td>2,884</td><td>364</td><td>461,293</td><td>460,933</td></tr><tr><td>9</td><td>6,844</td><td>5,524</td><td>3,844</td><td>-</td><td>-</td><td>-</td></tr><tr><td>10</td><td>3,544</td><td>2,102</td><td>1,502</td><td>304</td><td>728</td><td>426</td></tr><tr><td>11</td><td>5,314</td><td>3,152</td><td>2,252</td><td>454</td><td>6,883</td><td>6,431</td></tr><tr><td>12</td><td>7,084</td><td>4,202</td><td>3,002</td><td>604</td><td>93,325</td><td>92,723</td></tr><tr><td>13</td><td>4,564</td><td>2 702</td><td>1,802</td><td>304</td><td>4,010</td><td>3,710</td></tr><tr><td>14</td><td>6,844</td><td>4,052</td><td>2,702</td><td>452</td><td>239 208</td><td>238,758</td></tr><tr><td>15</td><td>9,124</td><td>5,402</td><td>3,602</td><td>-</td><td>-</td><td>-</td></tr><tr><td>16</td><td>3,846</td><td>3,036</td><td>2,346</td><td>245</td><td>1,339</td><td>1,096</td></tr><tr><td>17</td><td>5,766</td><td>4,551</td><td>3,516</td><td>365</td><td>20,863</td><td>20,500</td></tr><tr><td>18</td><td>7 686</td><td>6,066</td><td>4,686</td><td>485</td><td>363,802</td><td>363,319</td></tr><tr><td>19</td><td>9,670</td><td>7,480</td><td>6,070</td><td>367</td><td>2 774</td><td>2,414</td></tr><tr><td>20</td><td>14,500</td><td>11,215</td><td>9,100</td><td>547</td><td>65,695</td><td>65,155</td></tr><tr><td>21</td><td>19,330</td><td>14,950</td><td>12,130</td><td>727</td><td>1,561,996</td><td>1,561,276</td></tr></table>

Looking at the quality of the first integer solutions found during branch-and-bound, we can see that for 11 of the instances the optimizer finds better solutions for the path-flow formulation than for the arc-flow formulation. Also the arc-flow formulation finds better integer solutions for 6 of the instances when we disregard instances #9 and #15. The path-flow formulation’s linear relaxations are tighter than the corresponding linear relaxations for the arc-flow formulation for all instances except instances #10 and #13. We would expect that the path-flow formulation would have best linear relaxation for all instances. However, when solving these instances without presolve applied, the conclusion alters. With the optimizer’s presolve turned off, the LP solutions for instances #10 and #13 are 2,433.7 for the arc-flow formulation and 2,403.1 for the path-flow formulation.

Table 3. Solution times. All measures in sec. LP – linear relaxation, MIP <sup>1</sup> - first MIP solution, MIP\* – best MIP solution, Total – total solution time, Enum = time to enumerate the routes

<table><tr><td></td><td colspan="4">Arc-flow</td><td colspan="5">Path-flow</td></tr><tr><td>#</td><td>LP</td><td>MIP1</td><td>MIP*</td><td>Total</td><td>LP</td><td>MIP1</td><td>MIP*</td><td>Total</td><td>Enum</td></tr><tr><td>1</td><td>0</td><td>0</td><td>1</td><td>2</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>2</td><td>0</td><td>6</td><td>6</td><td>63</td><td>5</td><td>12</td><td>12</td><td>27</td><td>1</td></tr><tr><td>3</td><td>0</td><td>31</td><td>7,548</td><td>7,548</td><td>7,131</td><td>8,992</td><td>23,540</td><td>36,000</td><td>56</td></tr><tr><td>4</td><td>0</td><td>0</td><td>2</td><td>120</td><td>0</td><td>0</td><td>0</td><td>1</td><td>0</td></tr><tr><td>5</td><td>0</td><td>3</td><td>7,105</td><td>36 000</td><td>1</td><td>6</td><td>186</td><td>423</td><td>0</td></tr><tr><td>6</td><td>0</td><td>6</td><td>23,706</td><td>36,000</td><td>140</td><td>378</td><td>32,096</td><td>36,000</td><td>19</td></tr><tr><td>7</td><td>0</td><td>1</td><td>1</td><td>1</td><td>0</td><td>0</td><td>1</td><td>43</td><td>0</td></tr><tr><td>8</td><td>0</td><td>1</td><td>3</td><td>4</td><td>27</td><td>43</td><td>180</td><td>1,761</td><td>8</td></tr><tr><td>9</td><td>0</td><td>155</td><td>454</td><td>456</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>10</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>11</td><td>0</td><td>0</td><td>3</td><td>15</td><td>0</td><td>4</td><td>196</td><td>973</td><td>0</td></tr><tr><td>12</td><td>0</td><td>7</td><td>27</td><td>56</td><td>15</td><td>70</td><td>33,605</td><td>36,000</td><td>2</td></tr><tr><td>13</td><td>0</td><td>0</td><td>21</td><td>22</td><td>0</td><td>0</td><td>1</td><td>5</td><td>0</td></tr><tr><td>14</td><td>0</td><td>0</td><td>2,693</td><td>3,797</td><td>67</td><td>237</td><td>1,162</td><td>36,000</td><td>4</td></tr><tr><td>15</td><td>2</td><td>63</td><td>33,093</td><td>36,000</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>16</td><td>0</td><td>1</td><td>42</td><td>55</td><td>0</td><td>0</td><td>13</td><td>14</td><td>0</td></tr><tr><td>17</td><td>0</td><td>0</td><td>225</td><td>9,217</td><td>0</td><td>0</td><td>206</td><td>13,625</td><td>0</td></tr><tr><td>18</td><td>0</td><td>0</td><td>3 354</td><td>36,000</td><td>35</td><td>223</td><td>35,896</td><td>36,000</td><td>7</td></tr><tr><td>19</td><td>0</td><td>1</td><td>17</td><td>172</td><td>0</td><td>0</td><td>3</td><td>39</td><td>0</td></tr><tr><td>20</td><td>0</td><td>11</td><td>7,476</td><td>36 000</td><td>3</td><td>13</td><td>3,074</td><td>36,000</td><td>1</td></tr><tr><td>21</td><td>1</td><td>41</td><td>12,214</td><td>36,000</td><td>321</td><td>8 724</td><td>20 492</td><td>36,000</td><td>32</td></tr></table>

## 6 Concluding Remarks

In this paper we have introduced a new type of optimization problems, the liquefied natural gas inventory routing problem, LNG-IRP. This problem deals with managing the supply chain for the liquefied natural gas (LNG) business at a tactical planning level. Here, one actor controls the supply chain from liquefaction to sales, where both the production and sales levels are variable and may change from day to day. Furthermore, ship routing and scheduling of specialized ships (LNG tankers) are important parts of this supply chain. The problem is more complicated than many other maritime inventory routing problems, as it deals with variable rates of production and consumption. Moreover, the ship routing and scheduling are also more complicated, as the ships’ cargo tanks should not run dry at sea, as they have to deal with a constant rate of boil-off. In addition, the ships load all their cargo tanks at the pick-up ports, and unload a discrete number of cargo tanks at the delivery ports.

Table 4. Solution values and MIP-gaps for the instances

<table><tr><td></td><td colspan="4">Arc-flow</td><td colspan="4">Path-flow</td></tr><tr><td>#</td><td>LP</td><td>MIP1</td><td>MIP*</td><td>MIP-gap(%)</td><td>LP</td><td>MIP1</td><td>MIP*</td><td>MIP-gap</td></tr><tr><td>1</td><td>1,036.9</td><td>807.0</td><td>887.0</td><td>0.0</td><td>1,024.7</td><td>887.0</td><td>887.0</td><td>0.0</td></tr><tr><td>2</td><td>1,504.8</td><td>1 314.7</td><td>1,314.7</td><td>0.0 %</td><td>1,470.4</td><td>1,314.7</td><td>1,314.7</td><td>0.0</td></tr><tr><td>3</td><td>1,940.0</td><td>1,354.7</td><td>1,533.0</td><td>0.0</td><td>1,896.6</td><td>1,133.8</td><td>1,331.5</td><td>28.8</td></tr><tr><td>4</td><td>782.7</td><td>490.7</td><td>681.0</td><td>0.0</td><td>760.9</td><td>537.0</td><td>681.0</td><td>0.0</td></tr><tr><td>5</td><td>1 082.1</td><td>507.8</td><td>940.8</td><td>2.9</td><td>1,044.6</td><td>688.5</td><td>940.8</td><td>0.0</td></tr><tr><td>6</td><td>1,375.3</td><td>429.2</td><td>1 122.6</td><td>15.2</td><td>1,326.8</td><td>804.2</td><td>1,095.3</td><td>16.9</td></tr><tr><td>7</td><td>1,313.6</td><td>992.1</td><td>1,018.6</td><td>0.0</td><td>1 262.5</td><td>905.0</td><td>1,018.6</td><td>0.0</td></tr><tr><td>8</td><td>1 838.2</td><td>1,142.2</td><td>1,492.6</td><td>0.0</td><td>1,761.3</td><td>1,166.2</td><td>1,492.6</td><td>0.0 %</td></tr><tr><td>9</td><td>2,346.9</td><td>1,243.8</td><td>1 784.2</td><td>0.0</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>10</td><td>2,329.7</td><td>2,170.0</td><td>2,170.0</td><td>0.0</td><td>2 396.1</td><td>2,002.0</td><td>2,170.0</td><td>0.0</td></tr><tr><td>11</td><td>3 371.3</td><td>2,231.9</td><td>2,544.8</td><td>0.0</td><td>3,350.2</td><td>1,996.8</td><td>2,544.8</td><td>0.0</td></tr><tr><td>12</td><td>3,944.5</td><td>2,247.8</td><td>2,920.3</td><td>0.0</td><td>3 892.7</td><td>2,403.2</td><td>2,745.6</td><td>26.6</td></tr><tr><td>13</td><td>2 394.5</td><td>1,742.5</td><td>2,170.0</td><td>0.0</td><td>2,396.2</td><td>2,068.3</td><td>2,170.0</td><td>0.0</td></tr><tr><td>14</td><td>3,462.3</td><td>1,659.0</td><td>2 591.0</td><td>0.0</td><td>3,352.6</td><td>2,259.9</td><td>2,591.0</td><td>15.2</td></tr><tr><td>15</td><td>4,421.3</td><td>1,997.1</td><td>2,882.3</td><td>18.8</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>16</td><td>1,290.5</td><td>867.1</td><td>1 118.0</td><td>0.0 %</td><td>1,287.3</td><td>1,085.7</td><td>1,118.0</td><td>0.0</td></tr><tr><td>17</td><td>1,778.4</td><td>1,291.3</td><td>1,435.4</td><td>0.0</td><td>1 771.2</td><td>1,291.3</td><td>1,435.4</td><td>0.0</td></tr><tr><td>18</td><td>2,244.9</td><td>1,243.0</td><td>1,579.7</td><td>16.6</td><td>2,228.2</td><td>953.2</td><td>1,579.7</td><td>27.6</td></tr><tr><td>19</td><td>1 910.9</td><td>1,530.8</td><td>1,697.6</td><td>0.0</td><td>1,909.4</td><td>1,180.8</td><td>1,697.6</td><td>0.0</td></tr><tr><td>20</td><td>2,498.4</td><td>947.4</td><td>2 032.5</td><td>6.0</td><td>2,483.1</td><td>1,304.0</td><td>2,011.3</td><td>16.0</td></tr><tr><td>21</td><td>3,026.6</td><td>910.3</td><td>2,062.3</td><td>25.1</td><td>2 995.7</td><td>1,090.4</td><td>1,684.5</td><td>42.9</td></tr></table>

We have proposed two formulations of the LNG-IRP; an arc-flow and a path-flow formulation. In the path-flow formulation, a path represents a possible geographical route and schedule for a ship during the entire planning horizon. In addition, the path handles the ship inventory management, the boil-off from the cargo tanks, and the amount of cargo loaded and unloaded at the pick-up and delivery ports. Moreover, we have presented an algorithm for complete enumeration of the columns in the path-flow model.

Both model formulations have been tested on instances motivated by a real plan ning problem. Both formulations provide good solutions to the test instances pre-sented, although none of them were able to solve the largest instances to optimum. From the limited number of instances, it is hard to conclude which formulation is superior. The path-flow formulation was able to solve more instances faster to optimum than the arc-flow formulation, while the arc-flow formulation finds the first integer solution faster than the path-flow formulation. Furthermore, the path-flow formulation suffers from poor scaling capabilities. Hence, the optimizer ran out of memory when we tried to enumerate the columns for two of the instances.

The LNG-IRP is hard to solve. Thus, none of the proposed formulations where able to verify the optimal solutions for all instances presented. To be able to solve these, and even larger instances, more research is required. Solution approaches based on both exact methods and heuristics may be appropriate for solving larger instances of the LNG-IRP. Within exact methods, column generation seems like a particularly interesting alternative since we will be able to work with a subset of the columns for the problems. Moreover, the LP-gap for the LNG-IRP is poor. Thus, development of valid inequalities might also be valuable.

## Acknowledgments

This work was carried out with financial support from the Research Council of Norway through the INSUMAR project (Integrated supply chain and maritime transportation planning), the OPTIMAR project (Optimization in Maritime transportation and logistics) and the DOMinant project (Discrete optimization methods in maritime and road-based transportation). We would also like to thank Chief Analyst Stephane Hecq and Senior LNG Analyst Dr. Geert Stremersch from the Suez Corporation for their involvement in the project.

## References

[1] F. Al-Khayyal and S.-J. Hwang. Inventory constrained maritime routing and scheduling for multi-commodity liquid bulk, part I: Applications and model. European Journal of Operational Research, 176:106–130, 2007.

[2] BP. BP Statistical Review of World Energy 2007. British Petroleum, 2007.

[3] M. Christiansen. Decomposition of a combined inventory and time constrained ship routing problem. Transportation Science, 33(1):3–14, 1999.

[4] M. Christiansen, K. Fagerholt, B. Nygreen, and D. Ronen. Maritime transportation. In C. Barnhart and G. Laporte, editors, Transportation, volume 14 of Handbooks in Operations Research and Management Science, pages 189–284. Elsevier Science, 2007.

[5] M. Christiansen, K. Fagerholt, and D. Ronen. Ship routing and scheduling, status and perspectives. Transportation Science, 38(1):1–18, 2004.

[6] Marielle Christiansen and Kjetil Fagerholt. Maritime inventory routing problems. Encyclopedia of Optimization, 2007. To appear. pp. 16.

[7] G. Desaulniers, J. Desrosiers, A. Erdmann, M.M. Solomon, and F. Soumis. VRP with pickup and delivery. In P. Toth and D. Vigo, editors, The Vehicle Routing Problem, volume 9 of SIAM Monographs on Discrete Mathematics and Applications, pages 225–242. SIAM, Philadelphia, PA, 2002.

[8] EIA. The Global Liquefied Natural Gas Market: Status and Outlook. Energy Information Administration, U.S. Department of Energy, 2003.

[9] EIA. International Energy Outlook 2005. Energy Information Administration, U.S. Department of Energy, 2005.

[10] IEA. Natural Gas Market Review 2007: Security in a globalising market to 2015. International Energy Agency, 2007.

[11] Jan A. Persson and Maud Göthe-Lundgren. Shipment planning at oil refineries using column generation and valid inequalities. European Journal of Operational Research, 163(3):631–652, 2005.

[12] David Ronen. Cargo ships routing and scheduling: Survey of models and problems. European Journal of Operational Research, 12(2):119–126, 1983.

[13] David Ronen. Ship scheduling: The last decade. European Journal of Operational Research, 71(3):325–333, 1993.

# Modeling The Pre-Auction Stage: The Truckload Case

Gianfranco Guastaroba<sup>1</sup>, Renata Mansini<sup>2</sup>, and M. Grazia Speranza<sup>3</sup>

1 University of Brescia, Department of Quantitative Methods, Italy guastaro@eco.unibs.it

2 University of Brescia, Department of Electronics for Automation, Italy rmansini@ing.unibs.it

3 University of Brescia, Department of Quantitative Methods, Italy speranza@eco.unibs.it

**Summary.** In transportation service procurement, shipper and carriers cost functions for serving a pair of origin-destination points, usually called lanes, are highly dependent on the opportunity to serve neighboring lanes. Traditional single-item auctions do not allow to capture this type of preferences. On the contrary, they are perfectly modeled in combinatorial auctions where bids on bundles of items are allowed. In transportation service procurement the management of a combinatorial auction can be seen as a three-stage process. Each stage involves several complex decision making problems. All such problems have relevant practical implications but only some of them have received attention in the literature. In the present paper we focus on the pre-auction stage for transportation procurement. In particular, we analyze the problem of a shipper who has to decide between undertaking and/or outsourcing (through an auction) his transportation requests. The problem has never been analyzed before. We propose two different models for the problem in the truckload case and provide their computational comparison on randomly generated instances.

**Key words:** Electronic auctions, Truckload problem, Shipper’s lane selection problem, Arc routing problems

## 1 Introduction

The worldwide use of the Internet has deeply modified the way commercial agreements in logistics are stipulated (see Cranic and Speranza [7]). As in traditional marketplaces, every agent that approaches an e-marketplace has to solve different complex problems, either in case one has to buy or to sell an item. Making the most profitable pricing decision is one of them (see Elmaghraby and Keskinocak [15]). A widely used price mechanism is the auction. Several auction protocols are known in the literature and used by the practitioners. Between them, the most suitable for the procurement of goods and services is the reverse auction, in which a buyer demands either a Request for Quotation (RFQ) or a Request for Proposal (RFP) for the item/s needed. The price is then determined by a competition between potential sellers. Electronic auctions, conducted over the Internet, have several benefits compared to the traditional ones such as lower transaction and participation costs and the access to possibly larger markets (see [26]). Despite most of the auctions involve the sale of multiple distinct items, research in auction theory has traditionally focused on single item auctions assuming that bidders have no preferences for sets of items. On the contrary, bidders often show preferences for bundles of items expressed either as complementary or substitution effects (see de Vries and Vohra [10]). Running single-item auctions for multiple distinct items, for example in parallel or in sequence, results in inefficient allocations when bidders show complementarity or substitution preferences (see, the well-known “exposure problem” in DeMartini et al. [11]). To correctly model such preferences on items researchers have proposed the use of combinatorial auctions, where bidders are allowed to bid on any combination of the items auctioned off.

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">L. Bertazzi et al. (eds.), Innovations in Distribution Logistics, Lecture Notes in Economics and Mathematical Systems 619, DOI: 10.1007/978-3-540-92944-4,</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">-c 2009 Springer-Verlag Berlin Heidelberg</span></small>

In different contexts, the potential benefits deriving from the use of combinatorial auctions are enormous. In the present paper, we consider the context of transportation procurement, so that the items auctioned off are transportation services. In this domain, buyer is a manufacturer, a distributor, a retailer and any other company that needs to move goods, while potential sellers are all the trucking companies. From now on, we will refer to the buyer as the shipper and to the sellers as the carriers. For sake of simplicity, we assume that the shipper is the auctioneer, while the carriers act as bidders of the procurement auction. Items being auctioned off are distinguishable pairs of origin-destination points, usually called lanes, to which the shipper associates the number of loads that have to be moved during the temporal horizon considered in the proposed agreement. Jara-Diaz [21] defines a lane as a one-way movement from an origin to a destination with the associated set of shipments for the period considered by the RFP.

E-procurement of transportation services is a typical application domain where agents participating to the procurement auction show complementarity or substitution preferences on service contracts (see Caplice [3]) and have to solve a complex decision problem. In fact, a carrier’s convenience to serve a lane depends not only on the number of loads the carrier hauls on that lane (economies of scale), but also on the number of loads he might carry on other neighboring lanes (economies of scope) (see Sheffi [36]). An important factor contributing to a carrier’s transportation costs is indeed the deadheading cost (also called repositioning cost) which can be defined as the cost incurred when moving an empty truck from its current position to the origin of a new lane (see Caplice and Sheffi [4] and Ergun et al. [17]). Thus, one of the main problems faced by a carrier is to find the right bid (the right bundles of lanes) and the corresponding price to submit as an auction bid. On the other side of the auction, there are shipper’s decision problems. A shipper that manages a fleet of vehicles may get substantial benefits from running an auction, in the case the fleet is not sufficient to fulfill all the required transportation services and the shipper has to outsource some of them, or in case the available fleet is sizable, but the auction might provide carriers able to achieve the same requests at a significant lower cost. We identify the problem faced by the shipper in deciding which lanes he can personally serve and which ones he has to outsource as the Shipper’s Lane Selection Problem (SLSP).

Several other complex problems can be encountered in the design and implementation of a combinatorial auction (see Abrache et al. [1] and Pekeč and Rothkopf [31]). Selecting the most suitable auction protocol (see Klemperer [23]), deciding the type of the auction (see Parkes [30] for a theoretical justification of the use of multi-round combinatorial auctions when bidders have hard valuation problems) and its bidding language (see Abrache et al.[1], Nisan [28] and [29], Sandholm [35] and Caplice and Sheffi [5] where the authors report the traditional practice in truckload transportation), managing uncertainty in shipper-carriers relationship and determining the winners of the auction (see again the chapter by Caplice and Sheffi [5]) are only some of the problems that an auctioneer has to solve when setting up a combinatorial auction. Several excellent surveys have been published on general combinatorial auctions. These include the papers by de Vries and Vohra [10], Pekeč and Rothkopf [31], Gavish [19], Kalagnanam and Parkes [22] and the volume edited by Cramton et al. [8].

The aim of this paper is twofold. We first provide a survey on the use of combinatorial auctions in transportation service procurement and detect open research areas. Secondly, we focus our analysis on one new problem, the Shipper’s Lane Selection Problem, and provide two alternative mathematical formulations for it. Though such models are easily adaptable for transportation service procurement in general, we concentrate on the procurement of transportation trucking services since it is the most relevant among all the transportation modes. Indeed, the Bureau of Transportation Statistics of the U.S. Department of Transportation (BTS [2]) reports that in 2002 trucks moved more than \$6.2 trillion and 7.8 billion tons of manufactured goods and raw materials. This is about 74.3% of the value shipped and 67.2% of the weight carried. In particular, we analyze the transportation services procurement assuming the shipper is requiring truckload transportation (TL) services.

The following sections of the paper are organized as follows. In Sect. 2 we analyze the stages composing the organization of a combinatorial auction process and describe the main decision making problems encountered in each phase. In particular, when analyzing the pre-auction stage, the Shipper’s Lane Selection Problem (SLSP) is introduced. In Sect. 3 the two mixed-integer linear programming formulations to model the SLSP for the truckload case are provided. Section 4 is devoted to an experimental comparison of the two models on random instances, while in Sect. 5 conclusions and future developments are drawn.

## 2 The Outline of an Auction Process

An auction process typically consists of several steps involving different actors and requiring the solution of different problems. Plummer [32] gives a description of the bidding process from the carrier’s perspective. The process starts with carriers responding to Requests for Quotation (RFQ) or Requests for Proposal (RFP) moved for by the shipper. Usually a carrier decides on which RFQ (or RFP) to bid by considering his fleet size and the current commitments in his network. In Caplice and Sheffi [5] the authors describe the complete combinatorial auction framework from a more general point of view. They identify three main stages that form an auction process:

Pre-auction stage: the shipper estimates his transportation service requests for the upcoming period. He then determines the carriers to be invited to the auction through a screening selection and decides what information carriers have to return back, the type of the service rate (e.g. flat rate per move, rate per mile), the service details (e.g. days of transit, capacity available) and the type of bid allowed (e.g. simple bids, combinatorial bids and possible constraints on allowed combinations).

Auction stage: the shipper communicates the freight network to the carriers. Carriers conduct their own analysis and determine their bidding strategy. Every bid consists in a bundle of lanes and in the rate (the price) the carrier asks to serve it. Then, carriers submit their bids.

Post-auction stage: the shipper receives bids and has to determine the winners of the auction. Once the winners have been determined, the shipper communicates to the participants the winning bids.

Each one of the described stages involves a complex decision problem in which operational research methods can represent valuable tools for decision makers. While the third stage is the most studied in the literature, very few contributions exist for the carriers’ bidding problem in the second stage and no attention at all has been reserved to the pre-auction stage.

Many efforts have been made in analyzing the post-auction stage in the transportation field. The first reported use of management science tools to determine the winners of an auction can be found in Moore et al. [27]. The authors describe how the optimization and simulation tools, developed in 1988 at Reynolds Metals Company to centralize interstate truckload freight operations, have resulted in improving on-time delivery of shipments and in a decrease of the annual freight costs by over \$7 million. The authors introduce a mixed integer programming model that globally minimizes transportation costs subject to several operational constraints such as upper bounds on the number of carriers to be selected and individual carriers’ capacity constraints. Their model allows simple bids with volume constraints and does not allow combinatorial bids. Moreover, due to the limited computational capabilities available, the model was not fully implemented in practice. Ledyard et al. [25] describe the iterative combinatorial auction implemented by Sear Logistics Services (SLS) in 1993. The authors report that SLS has been the first procurer of trucking services that used a combinatorial auction to reduce its costs, saving about a 13% over past procurement practices. Elmaghraby and Keskinocak [15] discuss the implementation of the combinatorial auction for procuring transportation services experienced by the Home Depot. The company decided to use a single-round combinatorial auction, eventually allowing for a second round only for a limited number of lanes and a selected group of carriers. The winner determination problem was solved using an integer programming based algorithm. They point out that several other companies use the same optimization tool to procure transportation services, included Walmart Stores, Compaq Computer Co., Staples Inc., and many others. de Vries and Vohra [10] mention Logistics.com Inc.’s use of combinatorial auctions to procure transportation services for K-Mart Corporation and Ford Motor Company. Caplice and Sheffi [4] report how shippers can use optimization-based techniques for transportation services procurement. While in [5] the same authors discuss three formulations of the winner determination problem, called “carrier assignment problem”, usually used in practice for the procurement of truckload transportation services. The first formulation allows only simple bids with no side constraints, the second one introduces both simple bids and combinatorial bids, and the last one is based on flexible combinatorial bids. In a typical procurement application, side constraints are often introduced to ensure additional conditions on a valid assignment are satisfied (see [9] and [16], see [5] for an illustration of the constraints most commonly used in the practice of truckload services).

In the auction stage, carriers have to determine their optimal bidding strategy, analyzing their internal costs structure determined by their own resources and by their existing commitments. Several researchers have pointed out the computational difficulties of the bid valuation and construction problem in a combinatorial auction (e.g., see Parkes [30]). Several practical cases have been described where the use of optimization tools in selecting bundles of lanes would have been greatly beneficial to carriers. See, for example, the difficulties in forming bundles experienced by bidders in the Sears Logistics Services TL combinatorial auction [25]. Caplice [3] introduces some heuristic algorithms that carriers can use to create open loop tours, closed loop tours, inbound-outbound reload packages, and short haul packages using potential savings estimates based on historical load volumes. In a simulation based study, Regan and Song [33] show that the use of combinatorial auctions is beneficial for carriers compared to traditional single-item auctions in terms of revenue. Regan and Song [34] propose a linear model in which the objective function to be minimized is the total empty movement costs subject to constraints that impose all loads for every commitment, new or pre-existing, have to be satisfied. Then, the authors suggest approximation methods to construct carrier’s optimal or near optimal bids with and without pre-existing commitments. Kwon et al. [24] propose a quadratic integer programming model for the carrier’s bid generation problem in which carriers employ vehicle routing-type models to identify packages of lanes based on the actual routes that a fleet of trucks will follow in practice. Some researchers have analyzed the use of advisors applied to electronic freight marketplaces (see [6] and [18]). In this context, advisors are software agents that assist carriers in making “profitable” bidding decisions, by processing the information available in the market, and realize its integration into the dynamic planning of transportation operations (see [1]).

Finally, the stage that has received less attention in the literature is the pre-auction stage. In such stage the shipper has to determine for which lanes it may be convenient to auction off the transportation service. If the shipper has a fleet of vehicles able to serve all his transportation requests, he might be interested to set up an auction to find out if there exist carriers able to offer the same transportation services at a significant lower cost. If, on the contrary, the fleet available is not enough to fulfill all the needs, the shipper has to determine which lanes to serve with his own fleet and which ones to outsource by an auction in order to serve all transportation requests at the minimum cost. We identify such problem as the Shipper’s Lane Selection Problem. To the best of our knowledge, this problem has never been analyzed in the literature up to now. In the following section we provide two alternative mathematical formulations for this problem in the truckload case.

## 3 Modeling the Shipper’s Lane Selection Problem: The Truckload Case

Let us consider a shipper who has a set of transportation requests (lanes) to be satisfied. Each lane consists in carrying a load from an origin straight to its destination (truckload (TL) case). For sake of simplicity, we suppose that every request has to be fulfilled only once in the life span of the agreement between the shipper and his customer. We assume that traveling costs are expressed as distances between two nodes and that satisfy the triangle inequality. We also assume that the shipper has a vehicle which can be used for the service. We assume, for sake of simplicity, that every carrier is allowed to submit bids only for single requests. Moreover, the shipper is able to estimate, for example by inferring from historical data, the bid price that carriers potentially participating to the auction will submit on each lane. Finally, implementing and running an electronic auction involves a fixed cost, no matter the number of carriers participating. The shipper main problem is to decide which lanes to serve directly and which ones to outsource by means of an auction. The objective is to optimize the trade-off between the travel costs of a direct service and the cost of paying carriers for the service plus the possible set-up cost of the auction. Let us formalize the problem.

Let L be a set of lanes, i.e. a set of transportation requests each one identified by an origin and a destination. Given a complete bi-directed graph $G = ( V , A )$ with node set V (including the depot), arc set A and lane set $L \subseteq A$ , the problem looks for a directed cycle starting and ending at the depot covering a subset of lanes while minimizing the direct traveling costs plus the sum of costs incurred by the shipper to auction off the lanes not served by his own vehicle, i.e. the sum of the estimated costs paid to the bidders for the requests auctioned off plus a fixed cost incurred for running the auction.

Let us define as $c _ { i j }$ the travel cost from node i to node $j , ( i , j ) \in A$ , and as $\widehat { c _ { i j } }$ the estimated cheapest price asked by a potential carrier for serving the lane $( i , j ) \in L .$ Finally, define as K the fixed cost incurred by the shipper when implementing and running the auction.

A feasible solution for the Shipper’s Lane Selection Problem is defined by a simple directed cycle starting and ending at the depot, covering a subset of lanes

$L ^ { \prime } \subseteq L$ . Since a same node may serve either as origin or as destination of different lanes, a feasible solution is always a simple cycle but it may be non elementary.

![](images/page_229_image_3.jpg)

Fig. 1. A non elementary optimal cycle

Figure 1 shows an example where the optimal solution for a problem with four nodes (including the depot) and three lanes (set $L   =   \{ ( 1 , 0 ) , ( 2 , 3 ) , ( 3 , 2 ) \} )$ is a non elementary cycle. The travel costs are all equal to 1, whereas the estimated cheapest price requested by potential carriers is equal to $1 - \epsilon ,   0 < \epsilon < 1$ , for each request and $K = 5$ . The optimal solution for the shipper is to serve all the lanes with his own vehicle by a non elementary cycle traversing arc (0, 2), then serving lanes $( 2 , 3 )$ and (3, 2) and moving to node 1 to serve lane (1,0), then returning to the depot. The total cost paid by the shipper is equal to 5. In this solution the selection of both arcs $( 2 , 3 )$ and (3, 2) forms a subtour (node 2 is visited more than once). In order to allow non elementary solutions, the mathematical formulation of the problem cannot use the generalized subtour elimination constraints (e.g. see Toth and Vigo [38]). We have to formulate constraints that allow subtours but eliminate those of them that are isolated from the depot.

Figure 2 shows an example where the optimal solution consists of a cycle which serves only a part of the available lanes while some others are auctioned off. The graph is the same as that used in Fig. 1 with the same set of lanes and the same travel costs. The estimated bid prices are the same as those used in the previous example but for that associated to lane (1, 0) which is set equal to $2 + \epsilon .$ Finally, we set $K   =   1$ . Then, an optimal solution is to traverse arc (0, 1), to fulfill lane $( 1 , 0 )$ returning to the depot and to auction off the remaining lanes. The solution is shown in Fig. 2, where the cross-hatched lines represent the lanes auctioned off. The total cost paid by the shipper is equal to $5 - 2 \epsilon$ . The cheapest cost the shipper should pay by satisfying all the transportation requests with his own vehicle is equal to 5. The cost incurred by the shipper auctioning off all the requests would be equal to $5 - \epsilon .$

![](images/page_230_image_3.jpg)

Fig. 2. An optimal solution with some lanes auctioned off

## 3.1 Models Formulation

As the decision maker has to determine a minimum cost cycle traversing an arc subset of a graph, the SLSP is similar to the problems belonging to the class of Arc Routing Problems (see the excellent surveys by Eiselt et al. [13, 14] and the book edited by Dror [12]). Since the objective to be minimized is a function not only of the travel cost associated to each arc but also of the costs associated to the auction, the SLSP is rather different from all the problems formerly addressed in the literature.

In the following, we present two integer programming formulations for the SLSP. The first model is new, whereas the second model derives from a well-known formulation for the capacitated arc routing problem.

Let $x _ { i j } ,   ( i , j ) \in A$ , be a binary variable that takes value 1 if arc $( i , j )$ is traversed by the shipper’s vehicle, and 0 otherwise. Let $l _ { i j } , ( i , j ) \in L$ , be a binary variable that takes value 1 if lane $( i , j )$ is auctioned off and 0 otherwise. Finally, let z be a binary variable that takes value 1 if at least one lane is auctioned off and 0 otherwise, and $u ^ { S } ,   S   \subseteq   V \backslash \{ 0 \} , S   \neq   \emptyset$ , be a binary variable which takes value 1 when at least one node in set S is visited by the optimal solution and 0 otherwise. $M _ { 1 }$ and $M _ { 2 }$ are large constant values which can be set equal to $| L |$ and $| V | ^ { 2 }$ , respectively.

A first formulation of the truckload Shipper’s Lane Selection Problem (SLSP1) can be as follows:

$$
(S L S P 1) \quad \min \sum_ {(i, j) \in A} c _ {i j} x _ {i j} + \sum_ {(i, j) \in L} \widehat {c} _ {i j} l _ {i j} + K z\tag{1}
$$

$$
x _ {i j} \geq (1 - l _ {i j}) \quad (i, j) \in L\tag{2}
$$

$$
\sum_ {(i, j) \in L} l _ {i j} \leq M _ {1} z\tag{3}
$$

$$
\sum_ {j \in V \backslash \{i \}} x _ {j i} = \sum_ {j \in V \backslash \{i \}} x _ {i j} \quad i \in V\tag{4}
$$

$$
\sum_ {i \in S} \sum_ {j \in S} x _ {i j} \leq M _ {2} u ^ {S} \quad S \subseteq V \backslash \{0 \}, S \neq \emptyset\tag{5}
$$

$$
\sum_ {i \notin S} \sum_ {j \in S} x _ {i j} \geq u ^ {S} \quad S \subseteq V \backslash \{0 \}, S \neq \emptyset\tag{6}
$$

$$
x _ {i j} \in \{0, 1 \} \quad (i, j) \in A\tag{7}
$$

$$
l _ {i j} \in \{0, 1 \} \quad (i, j) \in L\tag{8}
$$

$$
u ^ {S} \in \{0, 1 \} \quad S \subseteq V \backslash \{0 \}, S \neq \emptyset\tag{9}
$$

$$
z \in \{0, 1 \}.\tag{10}
$$

The objective function (1) minimizes the estimated total cost incurred by the shipper to serve all his lanes. The total cost is given by the sum of the transportation costs incurred by the shipper visiting customers with his own vehicle, plus the sum of the estimated cheapest prices for the requests auctioned off, plus the fixed cost paid to set up the auction.

For every request $( i , j ) \in L$ , constraint (2) forces variable $x _ { i j }$ to take value 1 if the request is not auctioned off, i.e. if $l _ { i j } = 0$ . Notice that if $l _ { i j } = 1$ then $x _ { i j }$ is free to take any value. However, the minimization of the objective function forces variable $x _ { i j }$ to take at optimum value 0 as the most convenient of the two. Constraint (3) imposes that if at least a request is auctioned off, i.e. $l _ { i j } \; = \; 1$ for some $( i , j )   \in   L$ , then the binary variable z will take value 1. One may notice that if $l _ { i j }   =   0$ for all $( i , j ) \in L$ then z is forced by the objective function to take value 0 as the most convenient of the two. Constraints (4) (in-degree and out-degree constraints) establish that at optimum the total number of selected arcs entering into node $i \in V$ must be equal to the total number of selected arcs leaving it. This ensures that the number of selected arcs entering into any subset S , $S \subseteq V \backslash \{ 0 \} , S \neq \emptyset$ , is equal to the number of selected arcs exiting it. The set of constraints (5) along with constraints (6) eliminate isolated subtours. Indeed, the following implications are true:

$$
\boxed {\sum_ {i \in S} \sum_ {j \in S} x _ {i j} > 0 \quad \Rightarrow \quad u ^ {S} = 1 \quad \Rightarrow \quad \sum_ {i \notin S} \sum_ {j \in S} x _ {i j} \geq 1.}
$$

Specifically, for each subset $S   \subseteq   V \backslash \{ 0 \}$ , constraint (5) forces binary variable $u ^ { S }$ to take value 1 if, at optimum, at least one arc between two nodes in S is selected. For each subset $S   \subseteq   V \backslash \{ 0 \}$ constraint (6) imposes that, at optimum, the number of arcs entering into S must be at least equal to the value taken by variable $u ^ { S }$ . This imposes that if at least one arc is selected between two nodes in $S   , \mathrm { i . e . }   u ^ { S } = 1$ , then at least one arc starting from a node not in S must enter into S . Moreover, if $\textstyle \sum _ { i \in S } \sum _ { j \in S } x _ { i j }   =   0$ then $u ^ { S }$ is free to take any value, and it will take value 0 as the most convenient one, forced by the objective function. Finally, constraints (7) – (10) define binary conditions.

![](images/page_232_image_2.jpg)

Fig. 3. Violated constraints. Subsets $S _ { 1 } , S _ { 2 }$ and $S _ { 3 }$

In Fig. 3 we show how constraints (5) – (6) eliminate isolated subtours referring to the data of the example shown in Fig. 1. In particular, we show how the solution represented in Fig. 3 violates the constraints. Let us consider all the subsets $S \subseteq$ $V \backslash \{ 0 \}$ with cardinality equal to 2. We have labeled them as $S _ { 1 } , S _ { 2 }$ and $S _ { 3 }$ and plotted in Fig. 3. One may notice that considering only subsets $S _ { 1 }$ and $S _ { 2 }$ the constraints are satisfied since there is no arc selected in the solution between the two nodes in $S _ { 1 }$ and in $S _ { 2 }$ , respectively. Let us consider subset $S _ { 3 }$ . In the depicted solution $x _ { 2 3 } = x _ { 3 2 } = 1$ then binary variable $u ^ { S _ { 3 } }$ is forced to take value 1 by constraint (5). By constraint (6) at least one arc must enter into subset $S _ { 3 }$ . Then, the current solution violates constraint (6). Finally, notice that all subsets with cardinality 1, and the unique subset with cardinality 3, do not violate any constraint.

Model (SLSP1) requires $\left| V \right|   * ( \left| V \right|   -   1 )$ binary variables $x _ { i j } , | L |$ binary variables $l _ { i j } .$ $2 ^ { | V | - 1 }   -   1$ binary variables $u ^ { S }$ and the binary variable $z .$ The total number of constraints is equal to $| L | + ( 2 ^ { | V | } - 2 ) + | V | + 1$ . Thus, even for the smallest instances, the number of variables and the number of constraints are very large and grow exponentially in the number of vertices.

An alternative mathematical formulation for the SLSP can be derived from the formulation of the Capacitated Arc Routing Problem (CARP) (see Golden and Wong [20]). The new mathematical formulation (SLSP2) is as follows:

$$
(\text {SLSP2}) \quad (1)
$$

$$
\sum_ {i \in S} \sum_ {j \in S} x _ {i j} \leq | S | - 1 + M _ {2} u ^ {S} \quad S \subseteq V \backslash \{0 \}, S \neq \emptyset\tag{11}
$$

$$
(2) - (4) \text {and} (7) - (1 0)
$$

$$
\sum_ {i \in S} \sum_ {j \notin S} x _ {i j} \geq 1 - w ^ {S} \quad S \subseteq V \backslash \{0 \}, S \neq \emptyset\tag{12}
$$

$$
u ^ {S} + w ^ {S} \leq 1 \quad S \subseteq V \backslash \{0 \}, S \neq \emptyset\tag{13}
$$

$$
w ^ {S} \in \{0, 1 \} \quad S \subseteq V \backslash \{0 \}, S \neq \emptyset .\tag{14}
$$

With respect to the (SLSP1) formulation, the model makes use of a new set of binary variables $w ^ { S }$ . The meaning of all the other variables is the same as in the previous formulation.

Constraints (13) ensure that, at optimum and for every node subset S , only one of the two binary variables $u ^ { S }$ and $w ^ { \overline { { S } } }$ can take value 1. Hence, if the number of arcs between nodes in a subset S is strictly greater than $| S | - 1$ S | − , then the variable $u ^ { S }$ is forced to take value 1 by constraint (11). If variable $u ^ { S }$ takes value 1, then constraint (13) forces variable $w ^ { S }$ to take value 0. Finally, from constraint (12), the number of arcs leaving set S must be greater than 1.

This model requires $2 ^ { | V | - 1 } - 1$ additional binary variables $w ^ { S }$ and has $2 ^ { | V | - 1 } - 1$ more constraints.

## 4 Experimental Analysis

In this section we compare the computational times required by the two models to optimally solve a set of random instances. The models have been solved with CPLEX 10.1. Experiments have been run on a PC with 2,992 Mhz Intel Pentium III processor and 2 Gb of RAM.

The benchmark problems have been generated starting from Solomon’s instances for the VRPTW (see [37]). In detail, we have considered the first 15 customer co-ordinates of 5 random instances (R102, R104, R106, R108, and R110). We have changed the position of the depot assuming it is located at the origin of the axes. The latter choice has been motivated by the fact that, by maintaining Solomon’s depot coordinates no optimal solution auctioned any lane off. Euclidean distances have been rounded to the nearest integer. To provide a different level of lanes density, for each Solomon’s instance considered we have generated three different sets $L ,$ each one characterized by a different number of transportation requests. This means 15 instances altogether. Lanes have been generated randomly, assuming a predefined average number of lanes for each node, excluding the depot. The first set L is composed by the minimum number of lanes needed to ensure that at least a request is incident to every node of the graph:

$$
| L | = \lceil (| V | - 1) / 2 \rceil .
$$

The second set of lanes has been generated assuming that the ratio $| L | / ( | V | - 1 )$ is equal to 1. One may notice that this means to generate, on average, two lanes incident to every node. Finally, the third set of lanes has been generated assuming that the ratio $| L | / ( | V |   -   1 )$ is equal to 2. Notice that this means to generate, on average, four lanes incident to every node. Given the number of nodes, equal to 14 without considering the depot, the cardinality of set L is equal to 7, 14 and 28, respectively.

For each lane $( i , j ) \in L$ the expected cheapest price $\hat { c } _ { i j }$ has been uniformly generated in the interval $[ \alpha * ( c _ { 0 i } + c _ { i j } + c _ { j 0 } ) , ( c _ { 0 i } + c _ { i j } + c _ { j 0 } ) ]$ , where $\alpha$ has been set equal to 0.2. Finally, the fixed cost K, paid whenever the auction is implemented, has been set equal to 70.

Table 1 provides the computational times required by the two models when solving the 15 test instances. The table is organized into five columns. The first column provides the cardinality of set L, i.e. the number of lanes randomly generated in the graph. The second column indicates the Solomon’s problem from which the nodes coordinates have been selected. The third column provides the number of lanes (#) auctioned off in the optimal solution. Finally the last two columns provide the computational times of the models. Time is expressed in seconds.

One may notice that the SLSP1 formulation, independently of the instance, finds the optimal solution in about 7/8 mins, whereas the SLSP2 model requires computational times that are highly correlated with the type of instance. The SLSP2 model is always faster than the SLSP1 when the average number of lanes incident to every node of the graph is greater or equal than 1, i.e. for $| L | \geq 1 4$ . Conversely, the SLSP1 model is highly faster when the number of requests is minimum $( | L | = 7 )$ and the optimal solution auctions some lanes off. The only exception is represented by instance R110 where the number of lanes auctioned off is zero.

Table 1. Computational times (in seconds)

<table><tr><td colspan="3">|L| Problem # SLSP1</td><td>SLSP2</td></tr><tr><td rowspan="5">7</td><td>R102</td><td>2 473.08</td><td>155829.37</td></tr><tr><td>R104</td><td>2 458.48</td><td>747.94</td></tr><tr><td>R106</td><td>2 481.66</td><td>24304.41</td></tr><tr><td>R108</td><td>2 463.35</td><td>1555.18</td></tr><tr><td>R110</td><td>0 451.36</td><td>110.39</td></tr><tr><td rowspan="5">14</td><td>R102</td><td>0 449.97</td><td>54.78</td></tr><tr><td>R104</td><td>2 451.52</td><td>51.39</td></tr><tr><td>R106</td><td>3 451.27</td><td>69.09</td></tr><tr><td>R108</td><td>0 447.97</td><td>49.30</td></tr><tr><td>R110</td><td>0 447.09</td><td>53.88</td></tr><tr><td rowspan="5">28</td><td>R102</td><td>6 449.09</td><td>52.94</td></tr><tr><td>R104</td><td>3 453.47</td><td>53.16</td></tr><tr><td>R106</td><td>2 449.32</td><td>54.09</td></tr><tr><td>R108</td><td>5 448.36</td><td>50.80</td></tr><tr><td>R110</td><td>3 453.58</td><td>52.63</td></tr></table>

## 5 Conclusions and Future Research

In this paper we have introduced the Shipper’s Lane Selection Problem. We have proposed two equivalent integer linear programming formulations and compared the computational times required by the two models to solve a set of randomly generated instances. Since the problem is new, several interesting issues can be considered for further developments. From the modeling point of view, to assume a shipper’s fleet composed by more than one vehicle, to consider the Less-Than-Truckload case and to allow more than one load per single lane are natural extensions. Moreover, as the problem cannot be solved in a reasonable amount of time with more than 16 customers, the design of effective and efficient heuristics seems to be a primary concern.

## References

[1] Abrache J, Crainic TG, Gendreau M (2004) Design issues for combinatorial auctions. Quarterly Journal of the Belgian, French and Italian Operations Research Societies 2(1):1–33.

[2] Bureau Transportation Statistics (2005) Trucks carry the most freight by weight and value. Available at: http://www.bts .gov/press releases/ 2005/bts003 05/html/bts003 05.html.

[3] Caplice C (1996), Optimization-based bidding: a new framework for shippercarrier relationship. PhD Thesis, Massachusetts Institute of Technology, Cambridge, MA.

[4] Caplice C, Sheffi Y (2003) Optimization-based procurement for transportation services. Journal of Business Logistics 24(2):109–128.

[5] Caplice C, Sheffi Y (2006) Combinatorial auctions for truckload transportation. In: Cramton P, Shoham Y, Steinberg R (eds) Combinatorial auctions. MIT Press, Cambridge, MA:539–571.

[6] Chang T-S, Crainic TG, Gendreau M (2002) Dynamic advisors for freight carriers for bidding in combinatorial auctions. In: Proceedings of the 5th international conference on electronic commerce research (ICECR-5), CD-ROM. Centre de Recherce sur le Transports, Montréal, Canada.

[7] Crainic TG, Speranza MG (2007) Logistics and the Internet. In: Don Taylor G (eds) Logistics engineering handbook. Taylor and Francis Group.

[8] Cramton P, Shoham Y, Steinberg R (2006) Combinatorial auctions. MIT Press, Cambridge, MA.

[9] Davenport AJ and Kalagnanam JR (2002) Price negotiations for procurement of direct inputs. In: Dietrich B, Vohra RV (eds) Mathematics of the Internet: e-auctions and markets. The IMA volumes in mathematics and its applications, Vol. 127. Springer, Berlin Heidelberg New York:27–44.

[10] de Vries S, Vohra RV (2003) Combinatorial auctions: a survey. INFORMS Journal on Computing 15(3):284–309.

[11] DeMartini C, Kwasnica AM, Ledyard JO, Porter DP (2005) A new and improved design for multi-object iterative auctions. Management Science 51(3):419–434.

[12] Dror M (2000) Arc routing: theory, solutions and applications. Kluwer Academic Publishers, Norwell, MA.

[13] Eiselt HA, Gendreau M, Laporte G (1995) Arc routing problems, part I: the chinese postman problem. Operations Research 43(2):231–242.

[14] Eiselt HA, Gendreau M, Laporte G (1995) Arc routing problems, part II: the rural postman problem. Operations Research 43(3):399–414.

[15] Elmaghraby W, Keskinocak P (2003) Combinatorial auctions in procurement. In: Billington C, Harrison T, Lee H, Neale J (eds) The practice of supply chain management. Kluwer Academic Publishers:245–258.

[16] Epstein R, Henr´ıquez L, Catalán J, Weinstraub GY, Mart´ınez C (2002) A combinatorial auction improves school meals in Chile. Interfaces 32(6):1–14.

[17] Ergun O, Kuyzu G, Savelsberg M (2007) Shipper collaboration. Computers & Operations Research 34(6):1551–1560.

[18] Figliozzi M, Mahmassani HS, Jaillet P (2002) Modeling online transportation market performance: carrier competition under asymmetric fleet assignment technology. In: Proceedings of the 5th international conference on electronic commerce research (ICECR-5), CD-ROM. Centre de Recherce sur le Transports, Montréal, Canada.

[19] Gavish B (2003) Combinatorial auctions mathematical formulations and open issues. International Journal of Information Technology & Decision Making 2(1):5–27.

[20] Golden BL, Wong RT (1981) Capacitated arc routing problems. Networks 11(3):305–315.

[21] Jara-Diaz SR (1988) Multioutput analysis of trucking operations using spatially disaggregated flows. Transportation Research Part B 22(3):159–171.

[22] Kalagnanam J, Parkes D (2003) Auctions, bidding and exchange design. In: Simchi-Levi D, Wu SD, Shen Z-J (eds) Handbook of quantitative supply chain analysis: modeling in the e-business era. Kluwer Academic Publishers:143–212.

[23] Klemperer P (1999) Auction theory: a guide to the literature. Journal of Economic Surveys 13(3):227–286.

[24] Kwon RH, Lee C-G, Ma Z (2007) A carrier’s optimal bid generation problem in combinatorial auctions for transportation procurement. Transportation Research Part E 43(2):173–191.

[25] Ledyard JO, Olson M, Porter D, Swanson JA, Torma DP (2002) The first use of a combined-value auction for transportation services. Interfaces 32(5):4–12.

[26] Lucking-Reley D (2000) Auctions on the Internet: what’s being auctioned, and how? The Journal of Industrial Economics 48(3):227–252.

[27] Moore EW, Warmke JM, Gorban LR (1991) The indispensable role of management science in centralizing freight operations at Reynolds Metals company. Interfaces 21(1):107–129.

[28] Nisan N (2000) Bidding and allocation in combinatorial auctions. In: Proceedings of the Second ACM Conference on Electronic Commerce. Minneapolis, MN:1–12.

[29] Nisan N (2006) Bidding languages for combinatorial auctions. In: Cramton P, Shoham Y, Steinberg R (eds) Combinatorial auctions. MIT Press, Cambridge, MA:215–232.

[30] Parkes DC (2000) Optimal auction design for agents with hard valuation problems. In: Moukas A, Sierra C, Ygge F (eds) Agent mediated electronic commerce II: towards next-generation agent-based electronic commerce systems. Springer, Berlin Heidelberg New York:206–219.

[31] Pekeč A and Rothkopf MH (2003) Combinatorial auction design. Management Science 49(11):1485–1503.

[32] Plummer C (2003) Bidder response to combinatorial auctions in truckload procurement. Master Thesis, Massachusetts Institute of Technology, Cambridge, MA.

[33] Regan A, Song J (2003) Combinatorial auctions for transportation service procurement: the carrier perspective. Transportation Research Record 1833:40–46.

[34] Regan A, Song J (2005) Approximation algorithms for the bid construction problem in combinatorial auctions for the procurement of freight transportation contracts. Transportation Research Part B 39(10):914–933.

[35] Sandholm T (2002) Algorithm for optimal winner determination in combinatorial auctions. Artificial Intelligence 135(1):1–54.

[36] Sheffi Y (2004) Combinatorial auctions in the procurement of transportation services. Interfaces 34(4):245–252.

[37] Solomon MM (1987) Algorithms for the vehicle routing and scheduling problems with time window constraints. Operations Research 35(2):254–265.

[38] Toth P, Vigo D (2002) The Vehicle Routing Problem. Volume 9 of SIAM Monographs on Discrete Mathematics and Applications, Philadelphia, PA.

# Applications of the Double Standard Model for Ambulance Location

Gilbert Laporte1, François V. Louveaux<sup>2</sup>, Frédéric Semet<sup>3,4</sup>, and Arnaud Thirion<sup>2</sup>

1 Canada Research Chair in Distribution Management, HEC, Canada gilbert@crt.umontreal.ca

2 Facultés Universitaires Notre-Dame de la Paix, Belgium francois.louveaux@fundp.ac.be, thirionarnaud@hotmail.com

3 LAMIH-ROI, Université de Valenciennes et du Hainaut-Cambrésis, France frederic.semet@univ-valenciennes.fr

4 GRIS, Département d’administration de la santé, Université de Montréal, Canada

**Summary.** This paper describes classical and advanced ambulance location models developed over the past 35 years. One of these models, called the Double Standard Model (DSM) maximizes double demand coverage with a fixed number of ambulances. A dynamic version of DSM was developed and tested on data from the Island of Montreal. The static version was successfully applied to data from Montreal, Austria and Wallonia.

**Key words:** Ambulance location and relocation, Double coverage, Dynamic model, Probabilistic model

## 1 Introduction

The design and provision of efficient and cost effective ambulance services is a problem faced by all major municipal and regional authorities throughout the world. This is an area in which operations researchers have traditionally had an important impact. Their role is likely to increase in coming years with the development of powerful metaheuristics and their interaction with geographic information systems and advanced telecommunication technologies. A central problem arising in ambulance fleet management is to decide where to locate ambulances in order to provide adequate population coverage. Since the early 1970s, there has been a steady evolution in the models and algorithms proposed for this type of problem. The aim of this paper is to report on some recent developments in the area of ambulance location.

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">L. Bertazzi et al. (eds.), Innovations in Distribution Logistics, Lecture Notes</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">in Economics and Mathematical Systems 619, DOI: 10.1007/978-3-540-92944-4,</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">-c 2009 Springer-Verlag Berlin Heidelberg</span></small>

Formally, ambulance location models are defined on a graph $G = ( V \cup W , A )$ where V is the a node set representing aggregated demand points, W is a set of potential ambulance location site, and $A = \{ ( i , j ) \in V   \times   W , i \neq j \}$ is an arc set. With each arc $( i , j )$ is associated a travel time $t _ { i j }$ . A demand point $i \in V$ is covered by site $j \in W$ if and only if $d _ { i } \leq r ,$ where $r$ is a preset coverage standard. Let $W _ { i } = \{ j \in W : t _ { i j } \leq r \}$ be the set of location site covering demand point i. Several objectives and constraints are possible. For example, one could determine the minimum number of ambulances needed to cover all demand, or maximize the demand covered with a given number of ambulances. More involved models aimed at covering some demand points several times have also been proposed. In addition, dynamic and probabilistic models have been put forward.

In the Location Set Covering Model (LCSM) (Toregas et al. [23]) the aim is to minimize the number of ambulances needed to cover all demand points. The model uses binary variable $x _ { j }$ equal to 1 if and only if an ambulance is located at $j ;$

$$
\text {(LSCM) Minimize} \sum_ {j \in W} x _ {j}\tag{1}
$$

$$
\text {subject to} \sum_ {j \in W _ {i}} x _ {j} \geq 1 (i \in V),\tag{2}
$$

$$
x _ {j} \in \{0, 1 \} (j \in W).\tag{3}
$$

In the Maximum Covering Location Problem (MCLP) (Church and ReVelle [4]) $p$ ambulances are given and the aim is to cover the largest possible demand $z ( p )$ Denote by $d _ { i }$ the demand at node $i \in V$ and let $y _ { i }$ be a binary variable equal to 1 if and only if i is covered by at least one ambulance:

$$
(\text {MCLP}) \text {Maximize} z (p) = \sum_ {i \in V} d _ {i} y _ {i}\tag{4}
$$

$$
\text {subject to} \sum_ {j \in W _ {i}} x _ {j} \geq y _ {i} (i \in V),\tag{5}
$$

$$
\sum_ {j \in W} x _ {j} = p\tag{6}
$$

$$
x _ {j} \in \{0, 1 \} (j \in W),\tag{7}
$$

$$
y _ {i} \in \{0, 1 \} (i \in V).\tag{8}
$$

In practice, one can repeatedly solve MCLP with increasing values of $p$ and select a solution offering a good compromise between $p$ and $z ( p )$ .

The main drawback of LCSM and MCLP is that once an ambulance has been dispatched to a site its coverage becomes lost. To remedy this situation, several classes of more sophisticated models have been proposed. In the first class, multiple coverage of each demand point is ensured. In the second class, the probability that an ambulance will be available at any moment is explicitly taken into account. A third class of models allow for ambulance relocation in real-time. In other words, ambulance location models have evolved from static to probabilistic to dynamic settings. For recent surveys of ambulance location models, see Marianov and ReVelle [17], Brotcorne et al. [3], Goldberg [14], and Cordeau et al. [5].

This study focuses on the Double Standard Model (DSM) of Gendreau et al. [10] which belongs to the first class and has also been extended to handle dynamic ambulance relocation (Gendreau et al. [11]). Applications to Canadian data are provided by these authors. This model has recently been applied to the Austrian and Belgian contexts, by Doerner et al. [8] and Thirion [22], respectively.

The remainder of this paper is organized as follows. Section 2 presents an overview of some advanced ambulance location models, with an emphasis on DSM. In Sect. 3, we summarize the applications of the DSM to the Canadian, Austrian and Belgian cases. Conclusions follow in Sect. 4.

## 2 Advanced Ambulance Location Models

Our review of advanced ambulance location models covers the three classes of extensions presented in the introduction but, for logical reasons, the probabilistic case is described immediately after the dynamic case.

## 2.1 Multi-Coverage Static Models

One of the first extensions of MCLP model has been the use of several vehicle types and the introduction of the requirement that each demand point should be covered with one vehicle of each type (Schilling et al. [20]). Daskin and Stern [6] have later proposed a hierarchical objective to first maximize the demand covered more than once, and then the demand covered exactly once. Hogan and ReVelle [15] consider only one vehicle type but have developed two Backup Coverage Problems called BACOP1 and BACOP2. In BACOP1 the number p of ambulances is sufficient to cover the demand at least once, and the objective is to maximize the total demand covered at least twice. In BACOP2 the objective is a convex linear combination of the demand covered once or at least twice.

The Double Standard Model (DSM) of Gendreau et al. [10] works with two coverage standards $r _ { 1 }$ and $r _ { 2 }$ , with $r _ { 1 } \quad < \quad r _ { 2 }$ , as specified by the United States

Emergency Medical Services Act of 1973. A proportion $\alpha$ of the demand must be covered within $r _ { 1 }$ , while the entire demand must be covered within $r _ { 2 }$ . In the DSM, the objective is to maximize the demand covered twice within $r _ { 1 }$ using $p$ ambulances, at most $p _ { j }$ of which are located at $j \in W$ , subject to the double coverage constraints. Let $W _ { i } ^ { 1 } \; \stackrel { \cdot } { = } \; \{ j   \in   W   :   t _ { i j }   \leq   r _ { 1 } \}$ and $W _ { i } ^ { 2 }   =   \{ j   \in   W   :   t _ { i j }   \leq   r _ { 2 } \}$ . The integer variable $x _ { j }$ denotes the number of ambulances located at $j \in W$ and the binary variable $y _ { j } ^ { k }$ is equal to 1 if and only if the demand at node $i   \in   V$ is covered k times $( k = 1 { \mathrm { ~ o r ~ } } 2 )$ within $r _ { 1 }$ . The formulation is then:

$$
\text {(DSM) Maximize} \sum_ {i \in V} d _ {i} y _ {i} ^ {2}\tag{9}
$$

sub

$$
\text {ject to} \quad \sum_ {j \in W _ {i} ^ {2}} x _ {j} \geq 1 \quad (i \in V).\tag{10}
$$

$$
\sum_ {i \in V} d _ {i} y _ {i} ^ {1} \geq \alpha \sum_ {i \in V} d _ {i}\tag{11}
$$

$$
\sum_ {j \in W _ {i} ^ {1}} x _ {j} \geq y _ {i} ^ {1} + y _ {i} ^ {2} \quad (i \in V),\tag{12}
$$

$$
y _ {i} ^ {2} \geq y _ {i} ^ {1} \quad (i \in V),\tag{13}
$$

$$
\sum_ {j \in W} x _ {j} = p\tag{14}
$$

$$
x _ {j} \leq p _ {j} (j \in W),\tag{15}
$$

$$
y _ {i} ^ {1} \in \{0, 1 \} \quad (i \in V),\tag{16}
$$

$$
y _ {i} ^ {2} \in \{0, 1 \} \quad (i \in V),\tag{17}
$$

$$
x _ {j} \geq 0 \text {and integer} \quad (j \in W).\tag{18}
$$

In this model, the objective function computes the demand covered twice within $r _ { 1 }$ time units. Constraints (10) mean that all demand is covered within $r _ { 2 }$ . The lefthand side of (12) represents the number of ambulances covering node i within $r _ { 1 }$ units, while the right-hand side is equal to 1 if i is covered once within $r _ { 1 }$ units, and equal to 2 if it is covered at least twice within $r _ { 1 }$ units. The combination of constraints (11) and (12) ensures that a proportion α of the demand is covered within $r _ { 1 }$ . Constraints (13) state that node i cannot be covered at least twice if it is not covered at least once.

## 2.2 Multi-Coverage Static Models

The only known dynamic ambulance relocation model is due to Gendreau et al. [11]). Their Dynamic Double Standard Model (DDSM) can be used to redeploy ambulances in real-time whenever a call is made. In addition to the DSM constraints, the DDSM includes the following requirements: 1) vehicles moved in successive redeployments cannot always be the same; 2) repeated round trips between the same two location sites must be avoided; 3) long trips between the initial and final location sites must be avoided.

The dynamic aspect of the redeployment model is captured by time-dependent constants $M _ { j l } ^ { t }$ equal to the cost of repositioning, at time t, ambulance l from its current site to site ${ \hat { j } } \in W$ . This includes the case where site j coincides with the current location of the ambulance, i.e., $M _ { j l } ^ { t } \; = \; 0$ . The constant $M _ { j l } ^ { t }$ captures some of the history of ambulance l. If it has been moved frequently prior to time t, then $M _ { j l } ^ { t }$ will be larger. If moving ambulance l to site j violates any of above constraints, then the move is simply disallowed. Binary variables $x _ { j l }$ are equal to 1 if and only if ambulance l is moved to site $j .$ The constraints of the DDSM are similar to those of the DSM, with the extra constraint that at most one deployment per ambulance is allowed. The objective at time t is:

$$
\left(\mathrm{DDSM} ^ {t}\right) \text {Maximize} \sum_ {i \in V} d _ {i} y _ {i} ^ {2} - \sum_ {j \in W} \sum_ {l = 1} ^ {p} M _ {j l} ^ {t} x _ {j l}\left. \right\}\tag{19}
$$

## 2.3 Probabilistic Models

Probabilistic models take into account the fact that ambulances are not always available to answer a call. Each ambulance has a probability q, called busy fraction, of being unavailable. It is computed as the ratio of the total time spent by all ambulances on all calls to the total ambulance time available. If $i \in V$ is covered by k ambulances, then the expected demand covered at that node is $E _ { i , k } = d _ { i } ( 1 - q ^ { k } )$ and the marginal contribution of the $k ^ { t h }$ ambulance is : $E _ { i , k } - E _ { i , k - 1 } = d _ { i } ( 1 - q ) q ^ { k - 1 }$

In the Maximum Expected Covering Location Model (MEXCLP) (Daskin [7]), up to p ambulances may be located in total, and more than one vehicle may be located at the same node. Let $y _ { i k }$ be a binary variable equal to 1 if and only if node $i \in V$ is covered by at least k ambulances. The model is as follows :

$$
\text {Maximize} \sum_ {i \in V} d _ {i} (1 - q) q ^ {k - 1} y _ {i k}\tag{20}
$$

$$
\text {subject to} \quad \sum_ {j \in W _ {i}} x _ {j} \geq \sum_ {k = 1} ^ {p} y _ {i k} \quad (i \in V),\tag{21}
$$

$$
\sum_ {j \in W} x _ {j} \leq p\tag{22}
$$

$$
x _ {j} \geq 0 \text {and integer} \quad (j \in W),\tag{23}
$$

$$
y _ {i k} \in \{0, 1 \} (i \in V, k = 1, \dots , p).\tag{24}
$$

The validity of this model stems from the fact that the marginal contribution of the $k ^ { t h }$ ambulance is concave in k. Therefore, if $y _ { i k } = 1$ , then $y _ { i h } = 1$ for $h \leq k$ . Since the objective is to be maximized, both (21) and (22) will be satisfied as equalities. It follows that the two sides of (21) will be equal to the number of ambulances covering node $i \in V$

A dynamic implementation of MEXCLP, called TIMEXCLP, in which travel speeds change dynamically over time has been developed by Repede and Bernardo [18], while Goldberg et al. [13] have worked with stochastic travel times. These authors have also developed a formula to compute the probability that a site will be covered at any time. A related model used to locate physicians’ cars in the Montreal region was recently developed by Gendreau, Laporte and Semet [12].

ReVelle and Hogan [19] have developed two versions of the Maximal Availabil ity Location Problem, called MALP I and MALP II, in which each demand point is covered with the probability α, given that an ambulance is unavailable with probability q. Further studies on the estimate of the busy fraction have been conducted by Batta et al. [2] and by Marianov and ReVelle [16]. Finally, Ball and Lin [1] have developed an extension of LSCM which contains a linear constraint on the number of ambulances required to achieve a given reliability level.

## 3 Applications of the Double Standard Model

The Double Standard Model has been applied by three groups of researchers. The data used in these studies originate from Montreal (Gendreau, Laporte and Semet [10], [11]), from the eight rural provinces of Austria (Doerner et al. [8]), and from part of Wallonia (Thirion [22]).

## 3.1 Application to Montreal

The first application of the Double Standard Model was made to the Island of Montreal data, using the population distribution of 1986 (Statistics Canada [21]). The demand points are defined by the centroids of the $| V | = 2 ^ { \circ } 5 2 1$ census tracts which range from two to $7   0 0 0$ inhabitants. The total population is $1 ^ { \circ } 7 5 8 ^ { \circ } 6 0 0$ . For this study, four sets W of potential location sites, with $| W | = 4 0 , 5 0$ , 60 and 70 were used, and the number p of ambulances was 25, 30, 35 or 40.

Because of its large scale, this instance was solved heuristically. An upper bound $\overline { { z } }$ on the objective function value of DSM was first computed by solving the linear relaxation of the integer program at the root of the search tree by means of CPLEX. A first heuristic called CPLEX2 was obtained by solving the integer linear program and stopping 1) at the optimum, or 2) after $1 0 0 ^ { \circ } 0 0 0$ branch-and-bound nodes, or 3) as soon as a feasible solution of value $\underline { { z } } \leq 0 . 9 9   \overline { { z } }$ was reached.

A second heuristic, called TABU, consisted of applying tabu search starting from a solution derived from the linear relaxation. Consider the values $\overline { { x } } _ { j }$ taken by the $x _ { j }$ variables in the continuous solution. If these values are integer, then the solution is feasible and optimal. Otherwise, $\left[ \overline { { x } } _ { j } \right]$ ambulances are allocated to each site j and $p$ $- \textstyle \sum _ { j \in W } \left[ { \overline { { x } } } _ { j } \right]$ additional ambulances are allocated to the sites $j$ for which $x _ { j } > 0$ . This initial solution may be feasible or infeasible. The solution space is then explored according to the usual tabu search rules. The basic move consists of relocating an ambulance to one of its five closest neighbour sites where it is still possible to locate an ambulance. However, a simple application of this move would often yield uncovered areas and for this reason the neighbour solution is obtained by moving not only a single ambulance, but a sequence of ambulances in order to maximize the objective function at each step of the sequence. More specifically, a move can be described as a set of r pairs $\left( j _ { t } , j _ { t } ^ { \prime } \right) \left( t = 1 , \ldots , r \right)$ , where an ambulance is moved from $j _ { t }$ to $j _ { t } ^ { \prime }$

The objective function used during the search is not the original objective function $z$ defined by (9), but a modified hierarchical objective:

$$
z ^ {\prime} = z + M _ {1} z _ {1} + M _ {2} z _ {2}
$$

where $M _ { 1 }$ and $M _ { 2 }$ are two weights satisfying $M _ { 1 } > M _ { 2 } > 1$ . The functions $z _ { 1 } , z _ { 2 }$ are defined as follows:

$$
z _ {1} = | \{i \in V: \sum_ {j \in W _ {i} ^ {2}} x _ {j} \geq 1 \} |\tag{25}
$$

and

$$
z _ {2} = \min \{\alpha , \sum_ {i \in V} d _ {i} y _ {i} ^ {1} / \sum_ {i \in V} d _ {i} \}.\tag{26}
$$

The tabu search algorithm stops after 1000 iterations without improvement, or whenever it has identified a feasible solution within 1% of z.

Table 1 compares lower bounds values obtained by TABU and CPLEX2 to $\overline { { z } }$ and gives the computation times in seconds needed to run these two heuristics on a Sun Sparcstation 1000. Both algorithms consistently yield near optimal solution. It can be seen that CPLEX is slightly better than TABU, but has more unstable computation times. The solution with 40 potential sites and 25 ambulances is depicted in Fig. 1.

The tabu search algorithm developed for the static double standard location problem was extended by Gendreau, Laporte and Semet [11] to the dynamic case. The same algorithm is applied at each instant t at which a call is made, with the modified objective function (19), resulting in a redeployment plan. Because it takes about around 3 min to run the algorithm, it is preferable to precompute solutions during the time elapsed between two consecutive calls. More, specifically, for each site j at which an ambulance is currently positioned, one can determine a relocation plan under the hypothesis the ambulance located at j would be the one dispatched to answer the next call. In order to speed up the solution process, several scenarios can be considered simultaneously by using parallel computing. When the next call occurs, the corresponding redeployment plan is implemented and new solutions are recomputed. There always exists a risk that a scenario cannot be computed in time for the next call, in which case no redeployment is implemented.

Table 1. DSM results for the Island of Montreal

<table><tr><td>m</td><td>p</td><td>TABU / $\overline{z}$ </td><td>CPLEX2 / $\overline{z}$ </td><td>TABU time (s)</td><td>CPLEX2 time (s)</td></tr><tr><td rowspan="4">40</td><td>25</td><td>0.995</td><td>0.995</td><td>282</td><td>349</td></tr><tr><td>30</td><td>0.997</td><td>0.998</td><td>227</td><td>205</td></tr><tr><td>35</td><td>0.992</td><td>0.995</td><td>259</td><td>330</td></tr><tr><td>40</td><td>0.999</td><td>1.000</td><td>188</td><td>157</td></tr><tr><td rowspan="4">50</td><td>25</td><td>0.992</td><td>0.993</td><td>692</td><td>2999</td></tr><tr><td>30</td><td>0.994</td><td>0.995</td><td>403</td><td>396</td></tr><tr><td>35</td><td>0.995</td><td>0.994</td><td>186</td><td>227</td></tr><tr><td>40</td><td>0.999</td><td>0.999</td><td>175</td><td>185</td></tr><tr><td rowspan="4">60</td><td>25</td><td>0.995</td><td>0.996</td><td>354</td><td>491</td></tr><tr><td>30</td><td>0.992</td><td>0.993</td><td>353</td><td>316</td></tr><tr><td>35</td><td>0.996</td><td>0.998</td><td>238</td><td>234</td></tr><tr><td>40</td><td>0.996</td><td>0.999</td><td>194</td><td>207</td></tr><tr><td rowspan="4">70</td><td>25</td><td>0.991</td><td>0.993</td><td>698</td><td>1855</td></tr><tr><td>30</td><td>0.994</td><td>0.996</td><td>333</td><td>331</td></tr><tr><td>35</td><td>0.995</td><td>0.996</td><td>270</td><td>225</td></tr><tr><td>40</td><td>0.998</td><td>0.999</td><td>201</td><td>221</td></tr></table>

In order to test the feasibility of this approach, the tabu search algorithm was run on a network of 16 Sun Ultra-1/140 workstations (spec int95:5.87; spec fp95:8.38; ram: 64M; Solaris 7 exploitation system) and PVM was used for the parallel implementation. Six simulated data sets derived Urgences Santé data in Montreal were used to run the tests. Each set corresponds to a 7 h period and contains an average of 130 calls served by an average of 54 ambulances. These calls were distributed into four categories: urgent calls requiring one ambulance : 80%; urgent calls requiring two or three ambulances : 3%; less urgent calls: 10%; pending calls : 7%. The covering radiuses were $r _ { 1 }   =   7$ min and $r _ { 2 }   =   1 5$ min. With the proposed system, all calls were covered within with $r _ { 2 }$ , and 98% of urgent calls were covered within $r _ { 1 }$ with an average of 3.5 min (the desired response time set by Urgences Santé for urgent calls is $7$ min 90% of the time). Less urgent calls were served within an average of 9 min. The algorithm was capable of precomputing in time a redeployment plan in 95% of all cases. The only case where this was not possible is when two calls arrived within less than 32 seconds of each other. Out of all calls, 62% required no relocation and 99.59% of all relocation involved at most five ambulances with an average of 2.08. Thirty-three scenarios extracted from the simulation data were solved exactly by CPLEX. On these scenarios the tabu search heuristic produces solutions within 2% of the optima.

![](images/page_246_image_2.jpg)

Fig. 1. DSM solution for the Island of Montreal. Number of ambulances located at a site (1 or 2)

## 3.2 Application to Austria

Doerner et al. [8] have applied a model derived from DSM to locate ambulances in Austria. In their model, constraint (10) and (11) are treated as soft constraints, and the fraction of the demand $w _ { i }$ covered per ambulance for each demand point i is bounded above by a constant $w _ { 0 }$ . This requirement is also treated as a soft constraint. The objective function to be maximized is therefore:

$$
z ^ {\prime} = z - M _ {1} z _ {1} - M _ {2} z _ {2} - M _ {3} z _ {3},
$$

where $z$ is defined by (9) and $M _ { 1 } ,   M _ { 2 } ,   M _ { 3 }$ are positive constants. The functions $z _ { 1 }$ , z2, z3 are defined as follows:

$$
z _ {1} = | \{i \in V: \sum_ {j \in W _ {i} ^ {2}} x _ {j} = 0 \} |\tag{27}
$$

$$
z _ {2} = \alpha - \min \{\alpha , \sum_ {i \in V} d _ {i} y _ {i} ^ {1} / \sum_ {i \in V} d _ {i} \}\tag{28}
$$

and

$$
z _ {3} = \sum_ {i \in V} \max \left\{0, d _ {i} / \sum_ {j \in W _ {i} ^ {2}} x _ {j} - w _ {0} \right\}\tag{29}
$$

The model was solved by the tabu search algorithm of Gendreau, Laporte and Semet [10], and also by an ant colony optimization (ACO) heuristic inspired from that of Doerner et al. [9]. Basically, several location plans are determined, and ambulances are located at the selected sites. If fewer than $p$ ambulances have been assigned though this process, the remaining ambulances are randomly assigned to the remaining sites. A measure of the attractiveness of the solution is computed and is used to assign a “pheromone value” to the solution. More specifically, the pheromone values $\tau _ { j s }$ are numbers associated to the decision of locating s ambulances at site $j .$ The pheromone values are periodically updated in order to influence the design of ulterior solutions. The higher the value of $\tau _ { j s }$ is, the more likely s ambulances will be located at site $j$ in future iterations. The authors have also applied a local search mechanism, similar to that of the tabu search algorithm of Gendreau, Laporte and Semet [10] in order to improve the successive solutions constructed by their ACO algorithm. The ACO algorithm generated solutions of similar quality to those produced by tabu search but required significantly more computation time.

Both algorithms were applied to locate 1’952 ambulances over 460 bases in all of Austria, except Vienna. In two cases where it was possible to compute an optimal solution with an exact algorithm, the optimum was found. Figure 2 depicts the best solution identified for the Province of Salzburg.

Doerner et al. [8] have clearly demonstrated the practicality of the Gendreau, Laporte and Semet tabu search algorithm [10] over a different data set and with a slightly modified model. In our opinion, the main advantage of this model lies in the assignment of a maximum demand to any ambulance. This feature seems to be absent from previous ambulance location models.

## 3.3 Application to Wallonia

Finally, Thirion [22] has recently applied and compared several ambulance location models to a zone comprising 247 communes in the provinces of Namur and Brabant Walloon in the French speaking part of Belgium. This zone is currently served by 46 ambulances, 25 of which are located on nine sites within the zone, and 21 are located on 12 sites outside the zone but can still answer calls inside the zone. The set W is made up of 259 sites comprising the 247 communes of the zone, and the 12 current location sites outside the zone which are considered to be fixed. Currently,

![](images/page_248_image_2.jpg)

Fig. 2. DSM solution for the Province of Salzburg. Number of ambulances located at a site (1 or 2)

126 communes (51.01%) are covered by an ambulance within 8 min, while five cannot be reached within 15 min. In 2005, 77.47% of the 19’197 calls made to the ambulance services could be reached within 8 min.

A straight application of the LCSM shows that 26 ambulances would be necessary to cover all demand points within 8 min, while successive applications of the MCLP show that only eight sites are necessary to cover 82.33% of all calls within 8 mins and 15 sites yield a 95.34% coverage.

The MEXCLP was also applied to these data. The busy fraction q was estimated as 17.79% in 2005. It was found with this model that 12 ambulances would be needed to cover 81.26% of all demand, taking into account the temporary unavailability of some ambulances. To obtain a 95% coverage, 28 ambulances would be needed. The data should be contrasted with those of the MCLP which ensures a zero busy fraction.

Finally, the DSM was also applied to the same data. It was found that 20 ambulances are necessary to cover 82.38% of all calls twice within eight min, and 30 ambulances are necessary to bring the proportion up to 95.22%. Optimally relocating the 25 ambulances currently located inside the zone while leaving the location of the 21 outside ambulances unchanged would yield a 91.31% double coverage of all calls, as opposed to the current proportion of 75.88%.

These results clearly show that the application of models such as the MEXCLP and the DSM, which are based on different principles, can yield a significant improvement in simple or double coverage by simply reallocating the available ambulances to different sites. Figure 3 shows the locations of the 25 ambulances of the zone in the current situation, and as suggested by the MEXCLP and DSM solutions.

## 4 Conclusions

We have described some classical and advanced ambulance location models developed over the past 35 years. One of these models, called the Double Standard Model (DSM), maximizes double coverage with a fixed number of ambulances. A dynamic version of the DSM was developed by Gendreau, Laporte and Semet [11]. The static and dynamic versions of the DSM were successfully tested on data from the Island of Montreal. A slightly modified version of the DSM was later applied to Austrian data. Recently, the application of DSM to Walloon data has shown that significant coverage improvements could be reached without increasing the number of ambulances now in use.

## Acknowledgments

This work was partly supported by the Canadian Natural Sciences and Engineering Council under grants 39682-05, by the FEDER program of the European Community, and by the Région Nord Pas de Calais, France. This support is gratefully acknowledged.

## References

[1] Ball MO, Lin FL (1993) A reliability model applied to emergency service vehicle location. Operations Research 41:18-36.

[2] Batta R, Dolan JM, Krishnamorthy NN (1989) The maximal expected covering location model revisited. Transportation Science 23:277-287.

[3] Brotcorne L, Laporte G, Semet F (2003) Ambulance location and relocation models. European Journal of Operational Research 147:451-463.

[4] Church RL, ReVelle CS (1974) The maximal covering location problem. Papers of the Regional Science Association 32:101-118.

[5] Cordeau JF, Laporte G, Potvin J-Y, Salvesbergh MWP (2007) Transportation on demand. In : Barnhart C, Laporte G (eds) Transportation, Handbooks

![](images/page_250_image_2.jpg)

Fig. 3. Location of 25 ambulances in the Namur and Brabant Walloon provinces : (a) current situation; (b) MEXCLP solution ; (c) DSM solution

in Operations Research and Management Science, Volume 14. Elsevier, Amsterdam.

[6] Daskin MS, Stern EH (1981) A hierarchical objective set covering model for emergency medical service vehicle deployment. Transportation Science 15:137-152.

[7] Daskin MS (1983) The maximal expected covering location model: formulation, properties, and heuristic solution. Transportation Science 17:48-70.

[8] Doerner KF, Gutjahr WJ, Hartl RF, Karall M, Reimann M (2005) Heuristic solution of an extended double-coverage ambulance location problem for Austria. Central European Journal of Operations Research 13:325-340.

[9] Doerner KF, Gutjahr WJ, Hartl RF, Strauss C, Stummer C (2006) Nature inspired metaheuristics in multiobjective activity crashing. Forthcoming in Omega.

[10] Gendreau M, Laporte G, Semet F (1997) Solving an ambulance location model by tabu search. Location Science 5:75-88.

[11] Gendreau M, Laporte G, Semet F (2001) A dynamic model and parallel tabu search heuristic for real-time ambulance relocation. Parallel Computing 27:1641-1653.

[12] Gendreau M, Laporte G, Semet F (2006) The maximal expected demand coverage relocation problem for emergency vehicles. Journal of the Operational Research Society 57:22-28.

[13] Goldberg JB, Dietrich R, Chen JM, Mitwasi MG, Valenzuela T, Criss E (1990) Validating and Applying a Model for Locating Emergency Medical Vehicles in Tucson, AZ. European Journal of Operational Research 49:308-324.

[14] Goldberg JB (2004) Operations research models for the deployment of emergency services vehicles, EMS Management Journal 1:20-39.

[15] Hogan K, ReVelle CS (1986) Concept and applications of backup coverage. Management Science 32:1434-1444.

[16] Marianov V, ReVelle CS (1994) The queuing probabilistic location set covering problem and some extensions. Socio-Economic Planning Sciences 28:167-178.

[17] Marianov V, ReVelle CS (1995) Siting emergency services. In: Drezner Z. (ed) Facility Location: A Survey of Applications and Methods. Springer-Verlag, New York.

[18] Repede JF, Bernardo JJ (1994) Developing and validating a decision support system for locating emergency medical vehicles in Louisville, Kentucky. European Journal of Operational Research 75:567-581.

[19] ReVelle CS, Hogan K (1989) The maximum availability location problem. Transportation Science 23:192-200.

[20] Schilling DA, Elzinga DJ, Cohon J, Chuch RL, ReVelle CS (1979) The TEAM/FLEET models for simultaneous facility and equipment sitting. Transportation Science 13:163-175.

[21] Statistics Canada (1991) GEO: fichier de conversion des codes postaux.

[22] Thirion A (2006) Modèles de localisation et de réallocation d’ambulances. Application aux communes en provinces de Namur et Brabant Wallon. M.Sc. Dissertation, Facultés Universitaires Notre-Dame de la Paix, Namur, Belgium.

[23] Toregas C, Swain R, ReVelle C.S., Bergman L. (1971) The location of emergency service facilities. Operations Research 19:1363–1373.

# A Pricing Algorithm for the Vehicle Routing Problem with Soft Time Windows

Federico Liberatore<sup>1</sup>, Giovanni Righini<sup>2</sup>, and Matteo Salani<sup>3</sup>

1 Dipartimento di Tecnologie dell’Informazione, Università degli Studi di Milano, Italy fliberatore@crema.unimi.it

2 Dipartimento di Tecnologie dell’Informazione, Università degli Studi di Milano, Italy righini@dti.unimi.it

3 TRANSP-OR, Ecole Politechnique F´ ´ edérale de Lausanne, Switzerland matteo.salani@epfl.ch

**Summary.** The Vehicle Routing Problem with Soft Time Windows consists in computing a minimum cost set of routes for a fleet of vehicles of limited capacity that must visit a given set of customers with known demand, with the additional feature that each customer expresses a preference about the time at which the visit should occur. If a vehicle serves the customer out of its specified time window, an additional cost is incurred. Here we consider the case with penalties linearly depending on the time windows violation. We present an exact optimization algorithm for the pricing problem which arises when the vehicle routing problem with soft time windows is solved by column generation. The algorithm exploits bi-directional and bounded dynamic programming with decremental state space relaxation.

**Key words:** Combinatorial optimization, Vehicle routing, Column generation, Dynamic programming, Time windows

## 1 Introduction

In distribution logistics it is common that customers impose constraints on the arrival and departure time of the vehicles visiting them for pick-up or delivery operations. Therefore any planning algorithm for optimally routing and scheduling a fleet of vehicles must comply with these restrictions. The scientific literature in logistics optimization is rich of references to the vehicle routing problem with time windows (VRPTW): for a recent survey the reader is referred to Cordeau et al. [5] and Kallehauge et al. [12].

Soft time windows do not represent constraints but rather preferences about the time at which visits should occur at customers’ locations: if a customer is visited out of his preferred time window, a penalty is incurred in terms of additional costs that are charged to the distributor/collector. The main advantage of routing with soft time windows is that a feasible plan may include more visits than in the case in which the same time windows are imposed as “hard” constraints; solutions implying a small violation of one or more time window constraints and that therefore would have been discarded as infeasible for the VRPTW, may be discovered in this way and hence more profitable plans can be produced. However the optimization algorithm must take into account the additional cost terms coming from the penalties; as illustrated in the remainder this implies a number of algorithmic problems that must be suitably addressed to make use of the mathematical optimization techniques developed so far for the VRPTW.

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">L. Bertazzi et al. (eds.), Innovations in Distribution Logistics, Lecture Notes</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">in Economics and Mathematical Systems 619, DOI: 10.1007/978-3-540-92944-4,</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">-c 2009 Springer-Verlag Berlin Heidelberg</span></small>

Several heuristic algorithms have been proposed for the vehicle routing problem with soft time windows (VRPSTW), starting with the early work by Sexton and Choi [14], which concerned the pick-up and delivery version of the problem; Koskosidis et al. [13] developed an optimization-based heuristic; Balakrishnan [1] developed several constructive heuristics, while Taillard et al. [15] and Chiang and Russell [4] presented tabu search heuristics; more recently Ibaraki et al. [9] studied acceleration techniques for local search algorithms in the case of multiple soft time windows.

In this paper we present an algorithm for the resource constraint elementary shortest path problem with soft time windows, which forms the basis to develop a branch-and-price algorithm for the exact optimization of the VRPSTW. Recent examples of branch-and-price algorithms for the VRPTW are those of Desaulniers et al. [6] and Jepsen et al. [11].

## 2 Problem Formulation

The VRPSTW is defined as follows: a graph $\mathcal { G } ( \mathcal { V } , \mathcal { A } )$ is given, where the vertex set V is made of a set N of N customers and two vertices, numbered 0 and $N + 1$ representing the depot, where V vehicles are located. Non-negative weights $t _ { i j }$ and $c _ { i j }$ are associated with each arc $( i , j ) \in \mathcal { A } ;$ they represent respectively the traveling time and the transportation cost on each arc $( i , j ) \in { \mathcal { A } } ;$ traveling times are given by shortest path lengths and therefore they satisfy the triangle inequality.

A positive integer demand $q _ { i }$ is associated with each vertex $i \in N$ and a capacity $Q$ is associated with each vehicle. A non-negative integer service time $\theta _ { i }$ and a time window $[ a _ { i } , b _ { i } ]$ , defined by two non-negative integers, are also associated with each vertex $i \in \mathcal { N } ;$ if the service at vertex i starts inside its time window $[ a _ { i } , b _ { i } ]$ no penalty is incurred; if a vehicle starts servicing the customer at vertex i before time $a _ { i }$ or after time $b _ { i }$ , then a linear penalty has to be paid, which is proportional to the anticipation or delay through non-negative coefficients $\alpha _ { i }$ and $\beta _ { i }$ respectively. Indicating with $T _ { i }$ the starting time of service at vertex i the penalty term $\pi _ { i } ( T _ { i } )$ is defined as follows:

$$
\pi_ {i} (T _ {i}) = \left\{ \begin{array}{l l} \alpha_ {i} (a _ {i} - T _ {i}) & \text {if} T _ {i} \leq a _ {i} \\ 0 & \text {if} a _ {i} \leq T _ {i} \leq b _ {i} \\ \beta_ {i} (T _ {i} - b _ {i}) & \text {if} T _ {i} \geq b _ {i}. \end{array} \right.
$$

However the vehicles are allowed to wait at no cost at any time along their routes.

Column generation algorithms for routing problems rely upon a set covering reformulation, as follows.

$$
\text {minimize} \sum_ {f \in \mathcal {F}} w _ {f} z _ {f}
$$

$$
\text {subject to} \sum_ {f \in \mathcal {F}} x _ {i f} z _ {f} \geq 1
$$

$$
\forall i \in \mathcal {N}\tag{1}
$$

$$
- \sum_ {f \in \mathcal {F}} z _ {f} \geq - V\tag{2}
$$

$$
z _ {f} \in \{0, 1 \}
$$

$$
\forall f \in \mathcal {F}\tag{3}
$$

where $\mathcal { F }$ is the set of feasible vehicle routes, $w _ { f }$ is the cost of route $f \in \mathcal { F }$ , that is the sum of the costs of the arcs in the route plus the penalties due to the soft time windows violations, and $x _ { i f }$ is the number of times route $f   \in   \mathcal { F }$ visits customer $i \in N .$ The linear relaxation of this set covering reformulation usually yields very tight lower bounds (see for instance Bramel and Simchi-Levi [3] and the references therein). However since in general $\mathcal { F }$ contains an exponential number of columns, only a subset $\mathcal { F } ^ { \prime }$ is kept in a restricted linear master problem (RLMP) and further feasible routes are generated by the iterated solution of a pricing problem. The pricing problem consists in finding routes with negative reduced cost or proving that none exists. The reduced cost of route $f \in \mathcal { F }$ is:

$$
\overline {{w}} _ {f} = w _ {f} - \sum_ {i \in \mathcal {N}} x _ {i f} \lambda_ {i} + \lambda_ {0}
$$

where $( \lambda , \lambda _ { 0 } )$ is the vector of non-negative dual variables corresponding to constraints (1) and (2) in the linear restricted master problem.

The capacity constraints as well as the penalties are taken into account in the pricing subproblem: in particular the former ones restrict the set $\mathcal { F }$ of feasible routes, while the latter ones contribute to determine the cost of each route.

Hence the pricing subproblem turns out to be a resource constrained shortest path problem with soft time windows. A vehicle must go from vertex 0 to vertex $N + 1$ , visiting a subset of the other vertices; no cycles are allowed. Because there are non-negative prizes λ associated with the vertices, negative cost cycles can occur. Therefore the requisite that the path must be elementary does not come for free from cost minimization but it must be explicitly enforced. The capacity constraint is taken into account as a resource constraint: each vehicle leaving the depot has $Q$ units of available resource and every time it visits a customer with demand $q _ { i }$ it consumes $q _ { i }$ units of resource. The objective is to minimize the cost, given by the sum of the costs of the arcs traversed plus the sum of the penalties for anticipation and delay, minus the sum of the prizes collected at the vertices visited.

The main difficulty in dealing with soft time windows in column generation algorithms is that the possibility of trading time vs. cost generates an infinite number of possible solutions of the pricing problem that do not dominate one another. In algorithmic terms this means that the pricing algorithm, usually a dynamic programming algorithm, must take into account an infinite number of Pareto-optimal states. The pricing subproblem turns out to be an elementary shortest path problem with continuous resources on a graph with negative-cost arcs. The resource constrained elementary shortest path problem (RCESPP) on graphs with negative cost cycles is strongly NP-hard (see Dror, [7]) and it has been recently investigated by Righini and Salani who proposed bi-directional bounded dynamic programming algorithms [17] and decremental state space relaxation [16]. Another recent contribution on the subject is due to Irnich [10]. Hereafter we extend this research stream and we show how it can be adapted to the case with soft time windows implying continuous resources. In particular we present experimental evaluations of the bi-directional search technique [17], coupled with decremental state space relaxation [16] [18], when dynamic programming labels represent in a compact way an infinite number of non-dominated states.

## 3 The Algorithm

The resource constrained elementary shortest path problem with soft time windows is solved to optimality by a bi-directional dynamic programming algorithm.

## 3.1 States, Labels and Extension

A state associated with vertex $i \in N$ represents a path from the depot 0 to i. Different states associated with the same vertex correspond to different feasible paths reaching that vertex.

When a vehicle reaches a vertex it can start the service immediately or it can wait and start the service at a later time in order to reduce costs in case of early arrival. Therefore from each feasible state an infinite number of feasible states can be generated. For this reason our dynamic programming algorithm must take into account an infinite number of non-dominated states and this is done by grouping them into labels. Each label corresponds to an infinite number of states associated with the same path.

A label associated with vertex $i \in N$ is a tuple $L _ { i }   =   ( S , i , r , C ( T _ { i } ) )$ , where S is a binary vector indicating the vertices visited along the path, i is the last reached vertex, r is the amount of capacity consumed up to i, C is the cost of the path, $T _ { i }$ is the time at which the service at vertex i begins. In each label the function $C ( T _ { i } )$ describes the trade-off between cost and time. This function is piecewise linear and convex, because it is the sum of piecewise linear and convex functions, like the one shown in Fig. 1, one for each visited vertex. Its domain ranges from earliest possible arrival time to infinity.

In bi-directional dynamic programming these states are called forward states and in the same way we define backward states, corresponding to paths from vertex i to the final depot $N + 1$ represented by labels $( S , i , r , C ( T _ { i } ) )$ , where $T _ { i }$ is the time at which the service at vertex i begins.

![](images/page_257_image_2.jpg)

Fig. 1. A soft time window at a generic vertex $i \in \mathcal { N } :$ a linear penalty $\pi _ { i }$ is incurred depending on the service starting time $T _ { i }$

Remark. To keep a perfect symmetry in the description of the algorithm, one could equivalently define $T _ { i }$ in backward labels as the time at which the service at vertex i terminates and consider backward time windows $[ a _ { i } + \theta _ { i } , b _ { i } + \theta _ { i } ]$ , specifying the range in which the service at vertex i should preferably terminate. In the exposition we preferred not to introduce backward time windows, in order not to make the notation unnecessarily complicated, and hence we refer to service starting time and to the original time windows both in forward and in backward labels.

The dynamic programming algorithm iteratively extends all feasible forward and backward labels to generate new forward and backward labels respectively. The extension of a forward label corresponds to appending an additional arc $( i , j )$ to a path from 0 to i, obtaining a path from $0$ to $j ,$ while the extension of a backward label corresponds to appending an additional arc $( j , i )$ to a path from i to $N + 1$ , obtaining a path from $j$ to $N + 1$

To avoid negative cost cycles a dummy resource is associated with each vertex $i \in N ;$ there is only one unit available for each dummy resource and it is consumed when the corresponding vertex is visited. The binary vector S , indicating the vertices already visited, is therefore a resource consumption vector related to the dummy resources. It is initialized at $0$ at vertex 0. Note that S does not keep any information about the order in which the vertices are visited. When a forward label $( S , i , r , C ( T _ { i } ) )$ is extended to a vertex $j ,$ a new forward label $( S ^ { \prime } , j , r ^ { \prime } , C ^ { \prime } ( T _ { j } ) )$ is generated and the update rule is:

$$
S _ {k} ^ {\prime} = \left\{ \begin{array}{l l} S _ {k} + 1 & \text {if} k = j \\ S _ {k} & \text {if} k \neq j. \end{array} \right.
$$

A label $( S , i , r , C ( T _ { i } ) )$ corresponds to an elementary path only if $S _ { k } \leq 1 \; \forall k \in \mathcal { N } .$

The resource consumption r indicates the amount of capacity used. When a vehicle leaves the depot 0 all the resource is available, that is $r = 0$ , and the extension

rule is:

$$
r ^ {\prime} = r + q _ {j}.
$$

A label $( S , i , r , C ( T _ { i } ) )$ is feasible only if $r \leq Q$

Finally the cost $C ( T _ { i } )$ is initialized with the function $C(T_0)=0\ \forall T_0 \geq 0$ at the depot 0. At each extension the cost depends on both traveling time and penalties and it is updated according to the formula:

$$
C ^ {\prime} (T _ {j}) = C (T _ {j} - (\theta_ {i} + t _ {i j})) - \lambda_ {i} / 2 + c _ {i j} - \lambda_ {j} / 2 + \pi_ {j} (T _ {j}),
$$

where $\lambda _ { i } = - \lambda _ { 0 }$ if $i = 0$ and $\lambda _ { j } = - \lambda _ { 0 } \; \mathrm { i f } \; j = N   +   1$ . In this expression the cost function of the predecessor is evaluated at $T _ { i } = T _ { j } - ( \theta _ { i } + t _ { i j } )$ , which is the latest time instant at which the service at vertex i should begin to allow starting the service at vertex j at time $T _ { j }$

Figure 2 shows an example of forward extension. In graphical terms, the cost function $C ( T _ { i } )$ is shifted to the right by the service time at vertex i, that is $\theta _ { i } ,$ plus the traveling time $t _ { i j }$ spent to reach vertex $j ,$ it is shifted up by the traveling cost $c _ { i j }$ minus the prizes $\lambda _ { i } / 2 + \lambda _ { j } / 2$ collected for visiting the vertices. Then it is summed to the penalty term $\pi _ { j }$ , which depends on the arrival time $T _ { j } .$ If $C ( T _ { i } )$ is piecewise linear and convex, then the resulting function $C ^ { \prime } ( T _ { j } )$ preserves both these properties. The number of segments in these piecewise linear functions is increased by at most two at every extension.

![](images/page_258_chart_9.jpg)

Fig. 2. Forward extension of a label of vertex i to vertex $j .$ The $C ^ { \prime } ( T _ { j } )$ function resulting from the extension is the sum of the $C ( T _ { i } )$ function of the extended label suitably shifted and the penalty function $\pi _ { j } ( T _ { j } )$

The extension rules for backward labels are symmetrical to those above. The cost function at the final depot is initialized as $C ( T _ { N + 1 } ) = 0 \; \forall T _ { N + 1 } \leq T ^ { m a x }$ , where $T ^ { m a x }$ is defined below.

## 3.2 Dominance Rules

In general the effectiveness of any dynamic programming algorithm heavily depends on the number of states generated. Hence it is essential to fathom feasible states which cannot lead to optimal solutions.

In our case this is done in two ways: first, by the deletion of parts of the linear functions in all labels and, second, by suitable dominance rules.

Consider a generic forward label like that represented in Fig. 3. Since all penalty functions have a positive penalty term for delays, the rightmost part of the function certainly has positive first derivative. Since waiting at no cost is allowed, all states in this part of the function are dominated by the states of the same label with smaller values of both time and cost. Therefore these dominated states can be replaced by states with the same cost of the dominating ones, as shown in Fig. 3. In graphical terms this means that the rightmost part of the piecewise linear function in each label is a horizontal unbounded segment, replacing all the segments with positive first derivative resulting from the last extension. A symmetric argument holds for backward labels, where a horizontal segment replaces the leftmost part of the piecewise linear functions with negative first derivative.

![](images/page_259_image_6.jpg)

Fig. 3. States on the ascending part of the piecewise linear function are dominated: the same value in time can be reached at a smaller cost

The second way to eliminate dominated states is by dominance tests, that are performed each time labels are extended. Let $L ^ { \prime } = ( S ^ { \prime } , i , r ^ { \prime } , C ^ { \prime } ( T _ { i } ^ { \prime } ) )$ and $L ^ { \prime \prime } \quad = \quad$ $( S ^ { \prime \prime } , i , r ^ { \prime \prime } , C ^ { \prime \prime } ( T _ { i } ^ { \prime \prime } ) )$ be two labels associated with vertex $i ;$ let $( S ^ { \prime } , i , r ^ { \prime } , C ^ { \prime } , T _ { i } ^ { \prime } )$ and $( S ^ { \prime \prime } , i , r ^ { \prime \prime } , C ^ { \prime \prime } , \dot { T _ { i } ^ { \prime \prime } } )$ be two states belonging to $L ^ { \prime }$ and $L ^ { \prime \prime }$ respectively, corresponding to two points on the piecewise linear functions $C ^ { \prime } ( T _ { i } ^ { \prime } )$ and $C ^ { \prime \prime } ( T _ { i } ^ { \prime \prime } )$ . Then the former state dominates the latter only if

$$
\begin{array}{l} S ^ {\prime} \leq S ^ {\prime \prime} \\ r ^ {\prime} \leq r ^ {\prime \prime} \\ C ^ {\prime} \leq C ^ {\prime \prime} \\ T _ {i} ^ {\prime} \leq T _ {i} ^ {\prime \prime} \end{array}
$$

and at least one of the inequalities is strict. When a dominance rule is applied to single states and the test succeeds, the effect is simply to delete one of the two states. In our case, where each label represents an infinite number of states, the effect of the dominance test is to delete some parts of the piecewise linear functions, as shown in Fig. 4. The states surviving the dominance test are those of minimum cost for each feasible value of the service starting time.

![](images/page_260_image_3.jpg)

Fig. 4. As an effect of the dominance test, some parts of the piecewise linear functions are deleted. Only the states drawn with heavy lines are non-dominated and survive the test

This holds for both forward and backward labels. As a consequence, the resulting piecewise linear functions may have gaps and are not convex in general, as the small example in Fig. 4 shows.

When a new label is generated, it is compared to all the labels currently associated with the same vertex and the dominance test is applied for each comparison. Let $L ^ { \prime }   =   ( S ^ { \prime } , i , r ^ { \prime } , C ^ { \prime } ( T _ { i } ) )$ and $L ^ { \prime \prime }   =   ( S ^ { \prime \prime } , i , r ^ { \prime \prime } , C ^ { \prime \prime } ( T _ { i } ) )$ be the labels of vertex i that are compared. Then if $S ^ { \prime } = S ^ { \prime \prime }$ and $r ^ { \prime } = r ^ { \prime \prime }$ then the two labels are merged into one, so that at most one piecewise linear function is stored for each feasible combination of $S$ , i and $r ;$ in this case the non-dominated states form a new piecewise linear function possibly with vertical gaps and concavities as the one formed by the points in heavy lines in Fig. 4. In the other case, for instance (w.l.o.g.) if $S ^ { \prime } \leq S ^ { \prime \prime }$ and $r ^ { \prime } \leq r ^ { \prime \prime }$ , then the dominated states in $C ^ { \prime \prime } ( T _ { i } )$ are deleted and hence the resulting piecewise linear function can have also horizontal gaps, as the black heavy lines in Fig. 4.

## 3.3 Profitable Time Windows

The combined effect of soft time windows and dual prizes induces profitable time windows in the pricing problem. Consider a vertex i with dual prize $\lambda _ { i } ,$ soft time window $[ a _ { i } , b _ { i } ]$ and penalty coefficients $\alpha _ { i }$ and $\beta _ { i }$ . Any visit to the vertex occurring out of the time window $[ a _ { i }   -   \lambda _ { i } / \alpha _ { i } , b _ { i }   +   \lambda _ { i } / \beta _ { i } ]$ is not profitable, because the penalty to be paid would be larger than the prize gained. Such a non-profitable visit can always be skipped from any path $\mathcal { P } .$ , yielding another path $\mathcal { P }$ not worse than $\mathcal { P } ,$ owing to the triangle inequality. We do not explicitly include these profitable time windows in our model as hard constraints, but we use this observation to detect unreachable vertices, as explained in the next paragraph. Owing to this observation we also define a maximum allowed arrival time $T ^ { m a x } = \operatorname* { m a x } _ { i \in \mathcal { N } } \{ b _ { i }   +   \lambda _ { i } / \beta _ { i }   +   t _ { i \; N + 1 } \}$ , which is the latest possible arrival time at the final depot for an optimal path.

## Unreachable Vertices

A vertex j is unreachable from a label $L = ( S , i , r , C ( T _ { i } ) )$ when its demand $q _ { j }$ cannot be fulfilled with the remaining capacity $Q - r$ or when its profitable time window would be violated by any visit starting from label L, that is $T _ { i }   +   \theta _ { i }   +   t _ { i j } > b _ { j }   +   \lambda _ { j } / \beta _ { j }$ for all feasible values of $T _ { i }$ . For the purpose of the dominance test, unreachable vertices can be counted as if they were already visited, exploiting an idea of Feillet et al. [8]. Indicating with $U ^ { \prime }$ and $U ^ { \prime \prime }$ the characteristic vectors of the sets of unreachable vertices in two labels $L ^ { \prime }$ and $L ^ { \prime \prime }$ , the condition

$$
S ^ {\prime} \leq S ^ {\prime \prime}
$$

in the dominance test is replaced by

$$
S ^ {\prime} + U ^ {\prime} \leq S ^ {\prime \prime} + U ^ {\prime \prime},
$$

which is a weaker and therefore more effective sufficient condition.

## Search Policy

Labels are extended according to the vertices they are associated with. The vertices are cyclically visited in increasing order of the starting time $a _ { i }$ of their soft time windows; for each vertex the algorithm extends all its labels that have not yet been extended. At each vertex all the labels not yet extended are sorted according to a hierarchical criterion: first they are sorted by increasing overall length of the path; in case of ties they are sorted by increasing amount of capacity consumed; in case of further tie, they are sorted by number of vertices visited.

## Joining Forward and Backward States

In our bi-directional dynamic programming algorithm forward and backward paths must be joined together to produce complete paths from vertex 0 to vertex $N + 1$ . Let $L ^ { f w } = ( S ^ { f w } , i , r ^ { f w } , C ^ { f w } ( T _ { i } ) )$ be a forward label and $L ^ { b w } = ( S ^ { b w } , j , r ^ { b w } , C ^ { b w } ( T _ { j } ) )$ be a backward label. The join between $L ^ { f w }$ and $L ^ { b w }$ is subject to feasibility conditions on the resources. In particular the feasibility test on dummy resources S imposes that a same vertex can not be visited by both paths:

$$
S _ {k} ^ {f w} + S _ {k} ^ {b w} \leq 1 \quad \forall k \in \mathcal {N}.
$$

Moreover the consumption of capacity in the overall resulting path can not exceed the overall amount of available capacity, that is:

$$
r ^ {f w} + r ^ {b w} \leq Q.
$$

If the join is feasible, then the cost of the resulting path can be obtained as the minimum of the function

$$
C (T) = C ^ {f w} (T) - \lambda_ {i} / 2 + c _ {i j} - \lambda_ {j} / 2 + C ^ {b w} (T + \theta_ {i} + t _ {i j}).
$$

This function may have several local minima, as shown in Fig. 5. However the detection of the global minimum takes time linear in the number of discontinuity points of the two piecewise linear functions, since it requires a merge operation between two sorted lists.

![](images/page_262_image_6.jpg)

Fig. 5. When a forward and a backward labels are joined, the two corresponding piecewise linear functions are summed up. The resulting piecewise linear function may have multiple local minima. All its points below 0 correspond to negative reduced cost routes

## Resource-Based Bounding

Since all forward and backward states generated by the bi-directional search algorithm are tentatively joined, it is crucial to reduce their number as much as possible. To this purpose we select a critical resource, whose consumption is monotone along the paths, and we do not extend states in which at least half of the available amount of that resource has already been consumed. We tried using r, T and |S | as critical resources. These choices are compared in the next section.

## Decremental State Space Relaxation

Decremental state space relaxation (DSSR) was independently introduced by Righini and Salani [16] and by Boland et al. [2] to reduce the number of states to be explored by dynamic programming. The basic idea is that the elementary path constraints are not imposed on all the vertices of the graph but rather on a subset of critical vertices. If the optimal solution of the pricing problem is not elementary, one or more vertices visited more than once are inserted into the critical vertex set and the dynamic programming algorithm is executed again. In this way at each iteration a lower bound for the pricing problem is computed. Computational experiments reported in [16] show that the number of vertices that must be defined as critical in order to obtain a feasible solution is usually only a small fraction of N and therefore the pricing problem is solved to proven optimality in a fraction of the computing time required by dynamic programming when multiple visits are forbidden at all vertices.

In our algorithm we map each label $( S , i , r , C ( T _ { i } ) )$ onto a new label $( \hat { S } , i , r , C ( T _ { i } ) )$ where $\hat { S }$ is the set of critical vertices, initially empty. This is done for both forward and backward labels. The dominance rule is then modified, replacing condition $S ^ { \prime }   \leq   S ^ { \prime \prime } \mathrm {  ~ b y ~ } \hat { S } ^ { \prime }   \leq   \hat { S } ^ { \prime \prime }$ . Also in this case the detection of unreachable critical vertices is useful to enhance the effect of dominance tests. Indicating with $\hat { U }$ the set of unreachable critical vertices, the dominance test is $\hat { S } ^ { \prime } + \hat { U } ^ { \prime } \leq \hat { S } ^ { \prime \prime } \stackrel { \sim } { + } \hat { U } ^ { \prime \prime }$

## DSSR Policies

In Boland et al. [2] several different policies to update the critical set were considered. A computational comparison between them is also reported in Righini and Salani [18]. In the algorithm for the VRPSTW, we used the policy called HMO according to the terminology of [2]: it consists in adding to the critical vertex set one vertex at each iteration, selecting one at random among those visited the largest number of times.

## Initialization of the critical vertex set

Also the initialization of the critical vertex set can be done in different ways. In Righini and Salani [18] several policies were compared. The aim is to identify a subset of vertices that have a high probability to belong to the final critical vertex set. Let us define $f _ { i j }$ to be a measure of the “cycling attractiveness” of a vertex i with respect to a vertex $j$ as the ratio of the prize $\lambda _ { i }$ over the duration of the cycle $i – j – \dot { i } \dot { . }$

$$
f _ {i j} = \lambda_ {i} / (\theta_ {i} + t _ {i j} + \theta_ {j} + t _ {j i}).
$$

Now we define an ordering of the vertices based on the following four criteria:

• Highest Cycling Attractiveness (HCA): order by max $\mathfrak { c } _ { j \in \mathcal { N } \backslash \{ i \} } \{ f _ { i j } \}$

• Total Cycling Attractiveness (TCA): order by $\begin{array} { r } { \sum _ { j \in \mathcal { N } \setminus \{ i \} } f _ { i j } . } \end{array}$

• Weighted Highest Cycling Attractiveness (WHCA): order by max $_ { j \in \mathcal { N } \backslash \{ i \} } \{ f _ { i j } ( b _ { i } -$ $\left. a _ { i } \right) \}$

• Weighted Total Cycling Attractiveness (WTCA): order by $\textstyle \sum _ { j \in \mathcal { N } \backslash \{ i \} } f _ { i j } ( b _ { i } - a _ { i } )$

In general these criteria give different results and none of them is reliable to reveal the necessary vertices to be put in the critical vertex set. Let us define $H C A _ { m } , T C A _ { m } ,$ $W H C A _ { m }$ and $W T C A _ { m }$ to be the sets containing the first m vertices according to each of the ordering criteria above. We use as an initial critical vertex set the one obtained from the intersection of these four sets. By a suitable choice of the value of m the initial critical vertex set can be set large with the aim of reducing the number of iterations (high m) or small to reduce the probability of inserting unnecessary vertices into it (low m). In our computational experiments we set $m = 8$

## 4 Experimental Results

For our experiments we used instances derived from the well-known Solomon’s VRPTW benchmark. In particular we considered the instances in the class random with 100 customers. The integer coefficients $\alpha _ { i }$ and $\beta _ { i }$ for each vertex were generated at random with uniform probability distribution in the range [1, 5]. The values of the $t _ { i j }$ data are the Euclidean distances rounded down to the nearest multiple of 0.1. The values of the $c _ { i j }$ data are given by $\theta _ { i } + t _ { i j }$ . The vehicles capacity was set to 200.

All tests were performed on a PC equipped with an Intel Core Duo T2500 2x1.0 GHz processor, with 1024 MB RAM. The algorithms were coded in C++. We used GLPK as a linear programming solver for the RLMP.

Tables 1, 2 and 3 report on the experimental comparison between the bidirectional bounded dynamic programming algorithm without DSSR and with DSSR, when the critical resource used for stopping the extension in both directions is respectively the amount of capacity used, the time elapsed and the number of vertices visited. For all algorithms we report the number of stored labels and the computing time. For the DSSR algorithms we also report the number of iterations and the number of critical vertices at the end.

A time-out of 15 min was imposed to all tests. A dash in the “Time” column indicates that the time-out was exceeded.

Table 1. Comparison between bi-directional bounded dynamic programming algorithms without and with DSSR, using capacity as a critical resource

<table><tr><td rowspan="2">Instance</td><td colspan="2">D.P.</td><td colspan="4">DSSR</td></tr><tr><td>Labels</td><td>Time</td><td>Labels</td><td>Iterations</td><td>Critical</td><td>Time</td></tr><tr><td>r101_100</td><td>3,636</td><td>0.30</td><td>1,218</td><td>1</td><td>0</td><td>0.13</td></tr><tr><td>r102_100</td><td>29,190</td><td>4.24</td><td>5,882</td><td>4</td><td>5</td><td>5.83</td></tr><tr><td>r103_100</td><td>70,654</td><td>18.08</td><td>8,351</td><td>5</td><td>7</td><td>14.19</td></tr><tr><td>r104_100</td><td>141,422</td><td>54.92</td><td>10,893</td><td>6</td><td>7</td><td>25.00</td></tr><tr><td>r105_100</td><td>9,248</td><td>0.94</td><td>2,357</td><td>4</td><td>3</td><td>1.47</td></tr><tr><td>r106_100</td><td>47,889</td><td>9.95</td><td>7,251</td><td>4</td><td>5</td><td>8.00</td></tr><tr><td>r107_100</td><td>93,888</td><td>26.47</td><td>8,755</td><td>4</td><td>5</td><td>12.78</td></tr><tr><td>r108_100</td><td>166,226</td><td>69.97</td><td>11,446</td><td>6</td><td>7</td><td>26.59</td></tr><tr><td>r109_100</td><td>26,092</td><td>3.91</td><td>5,498</td><td>5</td><td>4</td><td>5.98</td></tr><tr><td>r110_100</td><td>64,594</td><td>16.20</td><td>7,332</td><td>4</td><td>4</td><td>9.64</td></tr><tr><td>r111_100</td><td>80,498</td><td>21.22</td><td>9,431</td><td>5</td><td>6</td><td>19.11</td></tr><tr><td>r112_100</td><td>191,198</td><td>86.86</td><td>11,979</td><td>5</td><td>5</td><td>26.44</td></tr></table>

Table 2. Comparison between bi-directional bounded dynamic programming algorithms without and with DSSR, using time as a critical resource

<table><tr><td rowspan="2">Instance</td><td colspan="2">D.P.</td><td colspan="4">DSSR</td></tr><tr><td>Labels</td><td>Time</td><td>Labels</td><td>Iterations</td><td>Critical</td><td>Time</td></tr><tr><td>r101_100</td><td>1,935</td><td>0.09</td><td>724</td><td>1</td><td>0</td><td>0.06</td></tr><tr><td>r102_100</td><td>37,698</td><td>11.69</td><td>9,792</td><td>4</td><td>5</td><td>19.24</td></tr><tr><td>r103_100</td><td>219,389</td><td>311.25</td><td>20,219</td><td>5</td><td>7</td><td>83.36</td></tr><tr><td>r104_100</td><td>485,653</td><td>-</td><td>37,272</td><td>6</td><td>7</td><td>225.36</td></tr><tr><td>r105_100</td><td>6,667</td><td>0.69</td><td>2,060</td><td>4</td><td>3</td><td>1.34</td></tr><tr><td>r106_100</td><td>82,709</td><td>58.22</td><td>12,461</td><td>4</td><td>5</td><td>28.80</td></tr><tr><td>r107_100</td><td>308,385</td><td>549.99</td><td>20,847</td><td>4</td><td>5</td><td>68.24</td></tr><tr><td>r108_100</td><td>481,206</td><td>-</td><td>38,076</td><td>6</td><td>7</td><td>230.87</td></tr><tr><td>r109_100</td><td>28,577</td><td>6.67</td><td>5,587</td><td>5</td><td>4</td><td>9.84</td></tr><tr><td>r110_100</td><td>136,516</td><td>162.34</td><td>12,764</td><td>4</td><td>4</td><td>38.69</td></tr><tr><td>r111_100</td><td>161,772</td><td>135.19</td><td>18,773</td><td>5</td><td>6</td><td>74.61</td></tr><tr><td>r112_100</td><td>430,117</td><td>-</td><td>27,943</td><td>5</td><td>5</td><td>206.75</td></tr></table>

Table 3. Comparison between bi-directional bounded dynamic programming algorithms without and with DSSR, using the number of vertices visited as a critical resource

<table><tr><td rowspan="2">Instance</td><td colspan="2">D.P.</td><td colspan="4">DSSR</td></tr><tr><td>Labels</td><td>Time</td><td>Labels</td><td>Iterations</td><td>Critical</td><td>Time</td></tr><tr><td>r101_100</td><td>4,518</td><td>0.30</td><td>1,367</td><td>1</td><td>0</td><td>0.14</td></tr><tr><td>r102_100</td><td>373,100</td><td>-</td><td>26,470</td><td>4</td><td>5</td><td>101.81</td></tr><tr><td>r103_100</td><td>415,083</td><td>-</td><td>48,253</td><td>5</td><td>7</td><td>566.94</td></tr><tr><td>r104_100</td><td>521,151</td><td>-</td><td>249</td><td>6</td><td>7</td><td>-</td></tr><tr><td>r105_100</td><td>22,764</td><td>4.08</td><td>3,808</td><td>4</td><td>3</td><td>3.38</td></tr><tr><td>r106_100</td><td>468,522</td><td>-</td><td>32,710</td><td>4</td><td>5</td><td>186.64</td></tr><tr><td>r107_100</td><td>448,413</td><td>-</td><td>47,882</td><td>4</td><td>5</td><td>453.78</td></tr><tr><td>r108_100</td><td>558,889</td><td>-</td><td>66,627</td><td>6</td><td>7</td><td>-</td></tr><tr><td>r109_100</td><td>175,621</td><td>155.84</td><td>18,498</td><td>5</td><td>5</td><td>61.78</td></tr><tr><td>r110_100</td><td>304,154</td><td>-</td><td>25,526</td><td>4</td><td>4</td><td>120.25</td></tr><tr><td>r111_100</td><td>420,081</td><td>-</td><td>54,034</td><td>5</td><td>6</td><td>767.61</td></tr><tr><td>r112_100</td><td>521,833</td><td>-</td><td>59,536</td><td>5</td><td>5</td><td>-</td></tr></table>

A first observation that can be drawn from the three tables reported, is that DSSR yields a remarkable improvement. In the worst cases only 7 vertices among 100 needed to be considered as critical in order to obtain a feasible solution.

A second observation concerns the choice of the critical resource: for the benchmark instances considered here capacity was definitely the most useful critical resource. Bounding on the basis of the number of vertices visited was particularly ineffective since the limit is set to half of the vertices, that is 50, while the average number of vertices in optimal paths is between 6 and 7. It should be remarked that Righini and Salani [16] obtained their best results on the same data-set with hard time windows using the elapsed time as a critical resource. Hence the relaxation of the time windows constraints makes the problem definitely more difficult, owing to an increased number of feasible labels.

A third observation concerns multiple pricing. The time spent by a pricing algorithm in column generation may be excessive if only one column is added to the RLMP at each iteration. An important feature of the algorithm described here is that it allows multiple pricing, which has become a common practice in column generation algorithms. At each join operation multiple columns with negative reduced cost can be found and inserted into the RLMP.

Moreover, by a trivial modification of the dominance test, the algorithm can be easily transformed into a heuristic, to accelerate the pricing phase.

## 5 Conclusions

In this paper we have presented an exact pricing algorithm for the vehicle routing problem with soft time windows, an important optimization problem in distribution logistics, for which no exact optimization algorithm has been published so far at the best of our knowledge.

The pricing algorithm is based on bi-directional and bounded dynamic programming with decremental state space relaxation.

We have described how an infinite number of non-dominated states are represented in a compact way by means of piecewise linear functions, whose description is stored in the labels extended by the dynamic programming algorithm; we have also presented the corresponding dominance rules and other algorithmic details.

The outcome of our computational experiments shows that this technique yields significant improvements compared to classical dynamic programming algorithms.

The next step will be to develop a branch-and-price algorithm for the exact optimization of the VRPSTW, exploiting this effective pricing technique. For this purpose the main developments needed are: (1) accurate and fast heuristics to compute primal bounds; (2) heuristic pricing algorithms to further speed up the search for profitable columns; (3) branching strategies compatible with the structure of the pricing problem.

## Acknowledgments

We thank M.Grazia Speranza and the organizers and participants of the International

Workshop on Distribution Logistics 2006 (Brescia), where a preliminary version of this research was presented. We also acknowledge the support of ACSU – Associazione Cremasca Studi Universitari to the OptLab, where this research was done.

## References

[1] Balakrishnan N (1993) Simple heuristics for the vehicle routeing problem with soft time windows Journal of the Operational Research Society 44:279–287.

[2] Boland N, Dethridge J, Dumitrescu I (2006) Accelerated label setting algorithms for the elementary resource constrained shortest path problem Operations Research Letters 34:58–68.

[3] Bramel J, Simchi-Levi D (2001) Set-covering-based algorithms for the capacitated VRP. In: Toth P, Vigo D (eds) The vehicle routing problem. SIAM Monographs on Discrete Mathematics and Applications, Philadelphia.

[4] Chiang WC, Russell RA (2004) A metaheuristic for the vehicle-routeing problem with soft time windows Journal of the Operational Research Society 55:1298–1310.

[5] Cordeau JF, Desaulniers G, Desrosiers J, Solomon MM, Soumis F (2001) The VRP with time windows. In: Toth P, Vigo D (eds) The vehicle routing problem. SIAM Monographs on Discrete Mathematics and Applications, Philadelphia.

[6] Desaulniers G, Lessard F, Hadjar A (2006) Tabu search, generalized k-path inequalities, and partial elementarity for the vehicle routing problem with time windows. Les Cahiers du GERAD 45, GERAD, Canada.

[7] Dror M (1994) Note on the complexity of the shortest path models for column generation in VRPTW Operations Research 42:977–978.

[8] Feillet D, Dejax P, Gendreau M, Gueguen C (2004) An exact algorithm for the elementary shortest path problem with resource constraints: application to some vehicle routing problems Networks 44:216–229.

[9] Ibaraki T, Imahori S, Kubo M, Masuda T, Uno T, Yagiura M (2005) Effective local search algorithms for routing and scheduling problems with general timewindow constraints Transportation Science 39:206–232.

[10] Irnich S (2006) Resource extension functions: properties, inversion, and generalization to segments Technical report, RWTH Aachen University, Germany.

[11] Jepsen M, Petersen B, Spoorendonk S, Pisinger D (2006) A non-robust Branchand-Cut-and-Price algorithm for the Vehicle Routing Problem with Time Windows. Technical report 06-03, DIKU University of Copenhagen, Denmark.

[12] Kallehauge B, Larsen J, Madsen OBG, Solomon MM (2005) Vehicle routing problem with time windows. In: Desaulniers G, Desrosiers J, Solomon MM (eds) Column generation. Springer, New York.

[13] Koskosidis YA, Powell WB, Solomon MM (1992) An optimization based heuristic for vehicle routeing and scheduling with soft time window constraints Transportation Science 26:69–85.

[14] Sexton T, Choi Y (1986) Pickup and delivery of partial loads with soft time windows American Journal of Mathematical and Management Sciences 6:369–398.

[15] Taillard E, Badeau P, Gendreau M, Guertin F, Potvin JY (1997) A tabu search heuristic for the vehicle routing problem with soft time windows Transportation Science 31:170–186.

[16] Righini G, Salani M (2005) New dynamic programming algorithms for the resource-constrained elementary shortest path problem. Note del Polo - Ricerca 69, DTI, University of Milan, Italy. Accepted for publication on Networks.

[17] Righini G, Salani M (2006) Symmetry helps: bounded bi-directional dynamic programming for the elementary shortest path problem with resource constraints Discrete Optimization 3:255–273.

[18] Righini G, Salani M (2006) Dynamic programming for the orienteering problem with time windows. Note del Polo - Ricerca 91, DTI, University of Milan, Italy.

# Effective Algorithms for a Bounded Version of the Uncapacitated TPP

Renata Mansini<sup>1</sup> and Barbara Tocchella<sup>2</sup>

1 Department of Electronics for Automation, University of Brescia, Italy rmansini@ing.unibs.it

2 Department of Electronics for Automation, University of Brescia, Italy barbara.tocchella@ing.unibs.it

**Summary.** Let us consider a set of markets plus a depot and a set of products. Each product is made available at a given price in a subset of markets. The distance between each couple of markets and between each market and the depot is known. The Uncapacitated Traveling Purchaser Problem with Budget constraint (UTPP-B) looks for a simple cycle starting at and ending to the depot which visits a subset of markets at the minimum traveling cost while pur chasing all products at a global cost that does not exceed a defined budget threshold. Although the problem arises in several application domains very few contributions exist in the literature for the UTPP-B. We propose and compare two solution algorithms for the problem, an enhanced local search heuristic and a Variable Neighborhood Search (VNS) approach. UTPP benchmark instances with additional budget constraints are used for computational experi ments. Heuristic performances are compared to exact solution values provided in [13] while solving with a single-objective hierarchical approach a bi-objective UTPP.

**Key words:** Traveling purchaser problem, Budget constraint, Local search, Variable neighborhood search

## 1 Introduction

The Traveling Purchaser Problem (TPP), originally proposed by Ramesh [9] is a generalization of the Traveling Salesman Problem and can be stated as follows. Consider a set of markets $M : = \{ 1 , \ldots , m \}$ plus a depot (indexed 0) and a set of products $K : = \{ 1 , \ldots , n \}$ . A traveling cost between each couple of markets and between each market and the depot $c _ { i j } ,   \forall i , j   \in   M \cup \{ 0 \}$ , is given. Each product $k , k   \in   K ,$ can be purchased in a given cluster of markets $M _ { k } \subseteq M$ at a nonnegative price $f _ { k i }$ depending on the market $i , i \in M _ { k }$ . The problem objective is to find a cycle starting at the depot and purchasing each product while minimizing the sum of the traveling costs plus the purchasing costs. This problem is also known as uncapacitated TPP to distinguish it from the capacitated one. The latter is a generalization where for each product k a required amount $d _ { k }$ to be purchased is specified and a defined quantity $q _ { k i }$ is made available at market i, $i \in M _ { k }$ , where $0 < q _ { k i } \leq d _ { k }$ and $\textstyle \sum _ { i \in M _ { k } } q _ { k i } \geq d _ { k }$ for all $k \in K$ and $i \in M _ { k }$

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">L. Bertazzi et al. (eds.), Innovations in Distribution Logistics, Lecture Notes</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">in Economics and Mathematical Systems 619, DOI: 10.1007/978-3-540-92944-4,</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">-c 2009 Springer-Verlag Berlin Heidelberg</span></small>

In this paper we analyze a bounded version of the uncapacitated TPP where the purchasing costs are removed from the objective function and added to the problem constraints by specifying a threshold B (the budget) as upper bound on the total amount which can be spent to purchase products. The problem looks for a minimum traveling costs cycle such that the demand for all products is satisfied at a global purchasing cost which does not exceed the budget threshold B. We identify such problem as the uncapacitated TPP with budget constraint (UTPP-B). The introduction of this bounded version aims at avoiding the sum in the same objective function of two cost measures which may be extremely different in nature. This is indeed the main drawback of the TPP formulation which does not take into account how, in many practical applications, the traveling costs are represented as distances or traveling times whereas the purchasing costs are measured as currency. Moreover, a trade-off frequently characterizes these two objectives since reducing the purchasing cost may imply an increase in the distance traveled.

Whereas many contributions can be found on the UTPP in the literature, its bounded version UTPP-B, although its recognized practical relevance, has received a limited attention. The uncapacitated version of the TPP was originally introduced by Burstall [1] and Ramesh [9] and has found several applications in scheduling and routing contexts. The problem is known to be NP-hard in the strong sense, reducing to the Traveling Salesman Problem (TSP) when each market offers a product which is not provided by the remaining ones. It also contains the uncapacitated facility location problem and the set cover problem as special cases. Due to its computational hardness several heuristic procedures have been proposed to solve both the capacitated and the uncapacitated version of the problem (see, for instance, Golden et al. [3], Ong [7], Pearn and Chien [8], Voss [15], Renaud et al. [11] and Mansini et al. [6]). Branch and Bound exact algorithms have been studied by Singh and van Oudheusden [14] while recently Laporte et al. [5] have introduced a branch-and-cut procedure for the capacitated version of the problem which is able to solve problems with up to 200 markets and 150 products.

On the contrary, the bounded version UTPP-B is cited and analyzed in very few works. In Riera-Ledesma and Salazar-González [13] the authors have introduced the bi-objective TPP, i.e. a bi-criteria version of the TPP where minimizing the purchasing cost and the traveling distances are two separate objectives. The bi-objective is a generalization of the TPP whose solution provide insight into the trade-off between the two costs. The authors tackle the problem by generating the set of all supported and non-supported efficient points in the objective space. For each efficient point in the objective space a Pareto optimal solution in the decision space is computed by solving a single-objective problem while bounding the remaining cost function. In the case the single objective is represented by traveling costs while purchasing costs are bounded in the constraints the problem solved is the UTPP-B. The authors provide exact solutions by means of a Branch and Cut approach for instances with up to 100 markets and 200 different products. The uncapacitated TPP with budgetconstraint is also analyzed in Ravi and Salman [10] as an application of telecommunication network design. In this paper the authors introduce an algorithm for the bi-criteria version of the UTPP with metric distances based on the rounding of an LP relaxation solution whose worst-case ratio is poly-logarithmic. They also show that for a special case of the UTPP which models the ring-star network design problem with proportional costs a constant factor approximation algorithm exists.

In the present paper, we propose two solution algorithms for the UTPP-B. To the best of our knowledge these procedures represent the first heuristics proposed in the literature to solve this bounded version of the TPP. In particular, the first procedure is based on an enhanced local search scheme where a neighbor solution is obtained from the current one by removing l-consecutive markets and inserting as many markets as required to restore solution feasibility. The heuristic uses a neighborhood similar to that proposed in [12] with the addition of a simple tabu structure introduced to avoid cycling. We will refer to such algorithm as enhanced local search since with respect to a pure local search scheme it varies the neighborhood during the search. The procedure is very efficient and, in those instances where budget constraint is not too tight (i.e. not too close to the minimum purchasing cost), it is also able to provide very effective solutions. The second algorithm is based on a Variable Neighborhood Search scheme (see Hansen and Mladenović [4] and references therein) where a sequence of neighborhoods $N _ { q } ( \cdot )$ is introduced each one characterized by a different parameter q representing the number of markets randomly inserted in a current solution. This procedure has the merit to show how a simple and straightforward application of a VNS structure along with an effective local search can be enough to produce high quality solutions.

The paper is organized as follows. In Sect. 2, the mathematical formulation of the UTPP with budget constraint is described. The solution algorithms are introduced in Sect. 3, while Sect. 4 is devoted to computational results. We have tested the proposed algorithms on benchmark instances of the uncapacitated TPP to which a budget constraint has been added. More precisely, algorithms performance has been compared to the optimal solution value provided in [13], where the authors deal with the UTPP with budget constraint to compute Pareto optimal solutions of a bi-objective TPP. Finally, conclusions and future developments are drawn in Sect. 5.

## 2 Problem Formulation

The uncapacitated TPP-B can be formally defined on an undirected complete graph $G = ( V , E )$ , where $V : = \{ 0 \} \cup M$ is the vertex set with vertex 0 representing the depot and $E : = \{ ( i , j ) : i , j \in V , i < j \}$ is the edge set. The problem looks for a simple cycle in $G ,$ starting at and ending to vertex 0, which visits a subset of vertices at a minimum traveling cost while purchasing all products at a global purchasing cost which does not exceed the budget threshold B. To avoid explicit consideration of trivial cases we have assumed that none of the markets can provide each of the n products at the cheapest cost.

To formulate the uncapacitated version of the problem we have introduced the following three sets of decision variables:

$$
x _ {i j} := \left\{ \begin{array}{l l} 1 & \text {if edge (i,j) belongs to the optimal cycle} \\ 0 & \text {otherwise;} \end{array} \right. \forall (i, j) \in E,
$$

$$
y _ {i} := \left\{ \begin{array}{l l} 1 & \text {if market $i$ belongs to the optimal cycle} \\ 0 & \text {otherwise;} \end{array} \right. \quad \forall i \in V,
$$

$$
z _ {k i} = \left\{ \begin{array}{l l} 1 & \text {if product k is purchased at market i} \\ 0 & \text {otherwise;} \end{array} \right. \quad \forall k \in K, \forall i \in M _ {k}.
$$

For any $S \subset V ,$ we define as $E ( S ) \; : = \; \{ ( i , j ) \; \in \; E \; : \; i , j \; \in \; S , i \; < \; j \}$ and as $\delta ( S ) \; : = \; \{ ( i , j ) \; \in \; E \; : \; i \; \in \; S , j \; \in \; V \setminus S \}$ . Moreover, we indicate as $M ^ { * }$ , the set $M ^ { * } \; : = \; \{ 0 \} \; \cup \; \{ i \; \in \; M \; : \; \exists k \; \in \; K$ such that $i   \in   M _ { k }$ and $| M _ { k } | \; = \; 1 \}$ , representing the markets which necessarily have to make part of any feasible solution.

The uncapacitated TPP with budget-constraint can be formulated as follows:

$$
\begin{array}{c c c} \hline (U T P P - B) & \min & v := \sum_ {(i, j) \in E} c _ {i j} x _ {i j} \\ \hline \end{array}\tag{1}
$$

$$
\sum_ {(i, j) \in \delta (\{i \})} x _ {i j} = 2 y _ {i} \quad \forall i \in V\tag{2}
$$

$$
\sum_ {(i, j) \in \delta (S)} x _ {i j} \geq 2 y _ {t} \quad \forall S \subseteq M \text {and} \forall t \in S\tag{3}
$$

$$
\sum_ {k \in K} \sum_ {i \in M _ {k}} f _ {k i} z _ {k i} \leq B\tag{4}
$$

$$
\sum_ {i \in M _ {k}} z _ {k i} = 1 \quad \forall k \in K\tag{5}
$$

$$
z _ {k i} \leq y _ {i} \quad \forall k \in K \text {and} \forall i \in M _ {k}\tag{6}
$$

$$
y _ {i} = 1 \quad \forall i \in M ^ {*}\tag{7}
$$

$$
x _ {i j} \in \{0, 1 \} \quad \forall (i, j) \in E\tag{8}
$$

$$
y _ {i} \in \{0, 1 \} \quad \forall   i \in V \setminus M ^ {*}\tag{9}
$$

$$
z _ {k i} \in \{0, 1 \} \quad \forall k \in K \text {and} \forall i \in M _ {k}\tag{10}
$$

Objective function (1) establishes the minimization of the routing costs. The set of constraints (2) ensures that the degree of each market i in the solution $( y _ { i } = 1 )$ has to be equal to two, i.e. each selected market is visited only once. The inequalities (3) ensure connectivity. Constraint (4) imposes a budget threshold equal to B on the total purchasing costs. Equalities (5) guarantee that each product k is purchased, whereas for inequalities (6) it is not possible to purchase a product k at an unvisited market. Equalities (7) impose that all the markets belonging to set $M ^ { * }$ are necessarily selected in any feasible solution. Constraints (8)–(10) are binary conditions on the variables.

## 3 Solution Algorithms

In this section we describe the two algorithms proposed to solve the UTPP-B. Given a current solution s, we call external the markets which do not belong to it and define as Tabu the set of markets in s which are forbidden to exit the solution in the current iteration.

The first proposed algorithm is called EJEMO (EJEct and MOve). Its detailed description is provided in Fig. 1. EJEMO receives as input a feasible solution $s ^ { I }$ and provides as output a new, possibly improved, feasible solution $s ^ { E }$ . The algorithm consists in an enhanced local search procedure which moves from a current solution s to its neighbor $s ^ { \prime }$ by removing a chain of l markets and inserting as many markets as required to restore feasibility (procedure ChainEjection(s, l)). Inserted markets (set S ) become tabu for a maximum of $r _ { m a x }$ iterations during which they cannot be removed from the current solution. If the new solution $s ^ { \prime }$ has a better value with respect to s, the parameter l (initially set to its maximum value $l _ { m a x } )$ remains unchanged (internal while loop) and the algorithm moves from s to $s ^ { \prime }$ . Otherwise the parameter l is reduced and the search is restarted from s. When l reaches its minimum value $l _ { m i n }$ (for loop), the algorithm diversifies the search generating a new solution $s ^ { \prime \prime }$ by using the procedure Shaking(s, h). This procedure randomly inserts in the current solution s as many markets as necessary to increase its traveling costs by at least a predefined percentage h (initially set to its maximum value $h _ { m a x } )$ . The procedure aims at possibly escaping from a local minimum by leading the search towards unexplored regions of the solution space. After the insertion of the new markets, the heuristic starts again with l set to a new initial value $l _ { m a x }$ computed as a fixed percentage of the markets making part of the current solution, whereas the diversification parameter h is reduced by a constant percentage $h _ { 0 }$ . The algorithm’s stopping rule is given by $h = h _ { m i n }$ (main while loop).

Procedure ChainEjection(s, l) is a two-step routine. The first step tries to reduce the length of the current cycle s by removing the chain of l consecutive markets that yields the largest reduction in the traveling costs. At this aim the procedure finds the set $P ( s )$ of all possible paths with $l + 1$ edges belonging to the current solution s and which do not contain markets belonging to $M ^ { * }$ or markets which are tabu (since they have been inserted in one of the previous iterations). If P is void an aspiration rule is applied which allows to consider tabu markets for paths construction. For each path $p \in P ( s )$ , the procedure calculates the routing cost reduction produced by its removal and the path yielding the highest reduction is removed by directly joining its extreme vertices. The second step controls if the new cycle is feasible and, if not, it restores feasibility by consecutively applying, if necessary, two feasibility procedures (GetAll(s) and BudgetRestore(s)).

Fig. 1. Pseudo-code of EJEMO algorithm

<div class="docvortex-algorithm" style="white-space: pre-wrap; font-family:monospace;">
INPUT:
initial solution $s^I$.
OUTPUT:
final solution $s^E$.

MAIN LOOP:
$h := h_{max}, r := r_{max};$
$s^E := s^I, v(s^E) := v(s^I);$
$s := s^E, v(s) := v(s^E);$
while $(h &gt; h_{min})$ {
    for $( l := l_{max}; l &gt; l_{min}; l := l - 1 );$ {
        $s' := \text{ChainEjection}(s, l);$
        Let $S$ be the set of markets inserted to restore feasibility;
        if $r = 0$ then $\{ r := r_{max} \}$;
        Add markets in $S$ to Tabu with tabu tenure $r;$
        $r := r - 1;$
        while $( v(s') &lt; v(s) )$ {
            $s := s', v(s) := v(s');$
            $s' := \text{ChainEjection}(s, l);$
            let $S$ be the set of markets inserted to restore feasibility;
            if $r = 0$ then $\{ r := r_{max} \}$;
            Add markets in $S$ to Tabu with tabu tenure $r;$
            $r := r - 1;$
        } end while
        if $v(s) &lt; v(s^E)$ then $\{ s^E := s, v(s^E) := v(s) \}$;
    } end for
    $s'' := \text{Shaking}(s, h);$
    $s := s'', v(s) := v(s'') ;$
    $h := h - h_0;$
} end while
</div>

Procedure GetAll(s) receives as input a solution s which is infeasible with respect to products purchasing. It iteratively inserts external markets one after the other until all products result to be bought. Since the procedure aims at satisfying products demand while minimizing routing costs, the markets to enter the solution are selected and inserted according to cheapest insertion rule and without considering purchasing costs. All inserted markets become tabu with a tabu tenure value r depending on the iteration. Every $r _ { m a x }$ iterations the tabu tenure r reduces to zero and the set Tabu becomes void. This means that when entering a solution a market will remain tabu for a number of iterations equal to the current value of parameter r where $r$ is less than or equal to $r _ { m a x }$

The solution finally provided by GetAll(s) may not be feasible with respect to the budget threshold constraint. In such case the procedure BudgetRestore(s) is applied. As a first step, such procedure finds all the subsets of markets external to solution s with cardinality one and two such that, if singularly inserted in the current solution, guarantee the budget to be satisfied. Then, the subset which allows to get feasibility with the smallest increase in the traveling costs, is added to the current solution. Markets insertion is made by cheapest insertion rule. If no subset of cardinality less than or equal to two is enough to restore budget feasibility, the procedure iteratively inserts one by one the external markets, previously sorted according to a saving cost rule, until the budget constraint is satisfied. More precisely, when inserting one or two markets in a solution, the corresponding saving in the purchasing costs is exactly computed as the difference between the total purchasing costs before and after markets insertion. The markets inserted become tabu for a number of iterations equal to r as described above.

EJEMO is very quick and has the main advantage of depending on only two main parameters: the one establishing the length of the chain to be removed (parameter $l )$ and that controlling diversification and imposing a maximum number of restarts (parameter $h )$ . For parameter l we have also tested the variant of the algorithm in which l is initially set to its minimum value $l _ { m i n }$ and then increased up to $l _ { m a x }$ . Since this version has provided a worse performance we have abandoned it.

Finally, the idea of removing chains of markets is also used in the algorithm proposed in [12]. With respect to such local search heuristic in our case markets inserted into a solution become tabu with a predefined tabu tenure. The length of the tabu list is not constant but reduces at a constant rate from $r _ { m a x }$ to zero. As soon as tabu tenure is zero it is reset to its maximum value $r _ { m a x }$

The second proposed algorithm uses a modification of the previous heuristic as a local search to be applied within a Variable Neighborhood Search (VNS) scheme. Figure 2 shows the pseudo-code of the implemented algorithm.

In a Variable Neighborhood Search scheme a sequence of neighborhoods $N _ { q } ( \cdot )$ is introduced each one characterized by a different parameter $q .$ If intensification of the search is required, the initial value of $q$ is set to a minimum value so that the closest neighborhood is selected first. The parameter will be increased only if no solution improvement can be obtained. If diversification of the search is required, the initial value for $q$ is set to a maximum value and then decreased.

In our case the algorithm explores increasing neighborhoods of a current solution (the VNS parameter $q$ is initialized to its minimum value $q _ { m i n } )$ and moves from this solution to a new one restarting the whole procedure if and only if an objective function improvement has been obtained. The algorithm receives as input an initial solution $s ^ { I }$ and provides as output the possibly improved solution $s ^ { V N S }$ which is initialized to $s ^ { I }$ .

Fig. 2. Pseudo-code of Variable Neighborhood Search algorithm

<div class="docvortex-algorithm" style="white-space: pre-wrap; font-family:monospace;">
INPUT:
initial solution $s^I$.
OUTPUT:
final solution $s^{VNS}$.

MAIN LOOP:
$s^{VNS} := s^I; v(s^{VNS}) := v(s^I)$;
for ($q := q_{min}; q &lt;= q_{max}; q := q + q_{step}$) {
    $s' := \textbf{RandomIns}(s^{VNS}, q)$;
    for ($l := l_{max}; l &gt; l_{min}; l := l - 1$) {
        $s'' := \textbf{Improvement}(s', l)$;
        if ($v(s'') &lt; v(s')$) {
            $s' := s''$;
            $v(s') := v(s'')$;
            $l := l_{max}$;
        } end if
    } end for
    if ($v(s') &lt; v(s^{VNS})$) {
        $s^{VNS} := s', v(s^{VNS}) := v(s')$;
        $q := q_{min}$;
    } end if
} end for
</div>

Given $q$ and the solution $s ^ { V N S }$ , a new solution $s ^ { \prime }$ belonging to the neighborhood $N _ { q } ( \bar { s ^ { V N S } }   )$ is generated from $s ^ { V N S }$ by inserting $q$ external random markets (RandomIns $( s ^ { V N S } , q )$ procedure). Insertion is made according to the cheapest insertion rule. Then a local search procedure is applied to $s ^ { \prime }$ . The local search routine starts by setting the parameter l to its maximum value $l _ { m a x }$ (computed as a predefined percentage of the markets making part of the current solution). Then procedure Improvement() is called. As procedure ChainEjection() in $E J E M O .$ Improvement $( s ^ { \prime } , l )$ routine is based on the ejection of l consecutive markets from a solution $s ^ { \prime }$ . However, in this case, the chain to be ejected is not selected a priori as the one which yields the highest travel costs reduction, but the method iteratively evaluates each feasible solution which can be obtained by removing $l$ consecutive markets and by inserting as many external markets as necessary to restore the feasibility (through GetAll() and BudgetRestore() procedures). As far as an improving solution is obtained the evaluation of l-markets chains ejection is interrupted (first improvement rule), the algorithm moves to the new solution, while the parameter l is reset to a new maximum value $l _ { m a x }$ (depending on the number of markets in the current solution) and the local search is restarted. If no improvement is achieved, after evaluating all feasible solutions obtainable by the elimination of l consecutive markets, the parameter l is decreased by one unit and the procedure is repeated. When $l = l _ { m i n }$ the local search stops providing the best solution $s ^ { \prime }$ found. If this solution is better than the incumbent one $s ^ { V N S }$ , the algorithm moves to this new solution and the VNS procedure restarts with $q : = q _ { m i n }$ and $s ^ { V N S } \; : = \; s ^ { \prime }$ , otherwise the parameter $q$ is increased by a value $q _ { s t e p }$ . Parameter $q$ controls search intensification and diversification. When no better solutions can be found $q$ is increased allowing the search to explore farthest and possibly more promising regions of the solution space. The algorithm stops when $q$ takes its maximum value $q _ { m a x }$ . The proposed VNS is not as efficient as EJEMO algorithm but, on average, provides more effective solutions.

Both proposed solution algorithms receive as input an initial feasible solution $s ^ { I }$ consisting of two steps. In the first one a construction heuristic is applied: the markets are sorted according to a predefined rule and then added one by one to a cycle until all products have been purchased. In the second step, the previously obtained solution is improved by possibly reducing its traveling costs with a TSP-improving heuristic. If, at step one, the constructed solution results to be infeasible with respect to the budget threshold B, the BudgetRestore() routine is called. In the construction heuristic we have used the nearest neighborhood rule to select the market which has to be inserted next and we have started insertion with markets belonging to set $M ^ { * }$ . As TSP-improving heuristic we have applied GENIUS algorithm (see Gendrau et al. [2]).

## 4 Computational Results

Proposed algorithms have been coded in C and run on a PC Pentium with 3.5 GHz and 2 GB of RAM.

Since no instances for the TPP with budget constraint are available in the literature, we have used the Euclidean instances proposed by Laporte et al. [5] for the uncapacitated TPP (Class 3 instances). We have set the budget constraints equal to the optimal purchasing costs provided by Riera Ledesma and Salazar Gonzalez in [13] when solving the bi-objective formulation of the Uncapacitated TPP on the same set of instances. In this paper, the authors have developed an iterative procedure to determine the solutions efficient set of their bi-criteria problem in the objective space. For each efficient point in the objective space, a Pareto optimal solution in the decision space is computed. The first step of this general method determines, for each instance, two initial efficient points through a two phases procedure which optimizes hierarchically the two objective functions represented by the purchasing and the routing costs. More precisely, an efficient point is computed by first minimizing the purchasing costs over all markets and then by setting this value as a constraint in a problem which minimizes the routing costs. The other one is obtained by first solving the problem that looks for the cycle at minimum cost while purchasing all products and then by finding the minimum purchasing costs over the subset of selected markets.

For each efficient point obtained by solving a given instance of the bi-objective problem a corresponding instance for the UTTP-B is generated by setting its budget threshold B equal to the optimal purchasing costs of the efficient point. This means that for each instance of Class 3 two different instances for the UTPP-B are created. Notice that while the instance corresponding to the first efficient point will have a tight budget threshold (the optimal purchasing costs correspond to the minimum purchasing costs), this is not the case for that corresponding to the second one. It is immediate to see that the optimal solutions for these UTPP-B instances correspond to the optimal traveling costs of the corresponding efficient points. We will identify the instances corresponding to the first efficient point and characterized by a budget equal to the minimum purchasing costs as tight-budget instances, while we will refer to those instances associated to the second efficient point as untight-budget instances.

We recall that instances in Class 3 are characterized by integer coordinate vertices generated in a $[ 0 { , } 1 { , } 0 0 0 ] \times [ 0 { , } 1 { , } 0 0 0 ]$ square according to a uniform distribution and Euclidean distances. Each product k is associated with $| M _ { k } |$ randomly selected markets, where $| M _ { k } |$ is randomly generated in $[ 1 , | V | - 1 ]$ . Product prices are generated in the interval [1,500] according to a discrete uniform distribution. In [13] the authors provide optimal solutions (initial efficient points) for instances with $m = 50,100,150,200$ markets and $n \; = \; 5 0 { , } 1 0 0$ products. For each combination of m and n they solve five different instances made available on the web page http://webpages.ull.es/users/jjsalaza. This means that, for our problem, we have generated and solved 80 instances altogether, 40 of which are tight-budget instances and 40 untight-budget ones. Moreover, given the random nature of the proposed solution algorithms, each of them has been run 5 times (5 trials) over each instance. The following two tables provide the average, min and max percentage errors with respect to the optimal solution value out of these 5 trials for the 40 tight-budget instances (Table 1) and for the 40 untight-budget ones (Table 2), respectively.

Each table is divided into two parts, the first one provides the computational results for heuristic EJEMO whereas the second one those for the VNS procedure. The column headings in each table have the following meaning: symbol # identifies, given m and n, the instance solved; B provides the budget threshold (the optimal purchasing costs of the corresponding efficient point); opt gives the optimal solution value (optimal traveling costs); aver., min and max refers to the average, the minimum and the maximum percentage error of the heuristic solution value from the optimal one out of the 5 trials; finally, sec provides the average computational time in seconds out of the 5 trials.

For heuristic $E J E M O$ we have set the parameters $h_{max} \; = \; 35\%$ and $h _ { m i n }$ and $h _ { 0 }$ equal to 1%. The decision has been taken after trying different values for the maximum percentage $h _ { m a x }$ equal to 20%, 25%, 40%, and 50%, respectively. The maximum value for the tabu tenure $r _ { m a x }$ has been set to 4, while parameter $l _ { m a x }$ and

Table 1. Computational results: tight-budget instances

<table><tr><td rowspan="2">n</td><td rowspan="2">m #</td><td rowspan="2">B opt</td><td colspan="4">EJEMO</td><td colspan="4">VNS</td></tr><tr><td>aver.</td><td>min</td><td>max</td><td>sec</td><td>aver.</td><td>min</td><td>max</td><td>sec</td></tr><tr><td rowspan="5">50</td><td>50 1</td><td>76 3629</td><td>3.25</td><td>2.65</td><td>3.69</td><td>1.99</td><td>0.71</td><td>0.61</td><td>0.74</td><td>4.12</td></tr><tr><td>2</td><td>66 3511</td><td>5.74</td><td>3.59</td><td>9.83</td><td>1.88</td><td>1.12</td><td>0.00</td><td>3.25</td><td>4.23</td></tr><tr><td>3</td><td>70 3164</td><td>1.99</td><td>1.04</td><td>3.60</td><td>1.77</td><td>0.05</td><td>0.00</td><td>0.25</td><td>3.95</td></tr><tr><td>4</td><td>80 3439</td><td>1.19</td><td>0.55</td><td>1.48</td><td>1.81</td><td>0.00</td><td>0.00</td><td>0.00</td><td>1.87</td></tr><tr><td>5</td><td>72 4116</td><td>5.52</td><td>4.64</td><td>6.75</td><td>2.04</td><td>0.47</td><td>0.00</td><td>2.36</td><td>3.28</td></tr><tr><td rowspan="5"></td><td>100 1</td><td>151 4050</td><td>2.20</td><td>0.49</td><td>3.04</td><td>2.72</td><td>0.00</td><td>0.00</td><td>0.00</td><td>11.18</td></tr><tr><td>2</td><td>137 4442</td><td>6.66</td><td>5.11</td><td>7.99</td><td>2.75</td><td>0.10</td><td>0.00</td><td>0.18</td><td>9.74</td></tr><tr><td>3</td><td>134 4174</td><td>17.48</td><td>8.53</td><td>22.76</td><td>2.76</td><td>0.68</td><td>0.00</td><td>1.92</td><td>10.97</td></tr><tr><td>4</td><td>159 4117</td><td>2.79</td><td>1.51</td><td>3.84</td><td>2.82</td><td>0.00</td><td>0.00</td><td>0.00</td><td>6.46</td></tr><tr><td>5</td><td>145 4110</td><td>5.51</td><td>4.70</td><td>7.20</td><td>2.77</td><td>0.00</td><td>0.00</td><td>0.00</td><td>7.30</td></tr><tr><td rowspan="5"></td><td>150 1</td><td>224 4851</td><td>9.35</td><td>7.87</td><td>11.44</td><td>6.31</td><td>2.80</td><td>1.46</td><td>4.16</td><td>13.53</td></tr><tr><td>2</td><td>199 4434</td><td>8.21</td><td>4.53</td><td>13.01</td><td>5.46</td><td>1.16</td><td>0.59</td><td>1.65</td><td>14.73</td></tr><tr><td>3</td><td>193 4609</td><td>2.26</td><td>1.48</td><td>3.62</td><td>5.76</td><td>0.00</td><td>0.00</td><td>0.02</td><td>17.49</td></tr><tr><td>4</td><td>222 4692</td><td>2.22</td><td>2.22</td><td>2.22</td><td>5.93</td><td>0.00</td><td>0.00</td><td>0.00</td><td>19.67</td></tr><tr><td>5</td><td>215 5018</td><td>8.41</td><td>6.30</td><td>12.71</td><td>6.70</td><td>0.00</td><td>0.00</td><td>0.00</td><td>20.49</td></tr><tr><td rowspan="5"></td><td>200 1</td><td>299 4816</td><td>4.94</td><td>3.09</td><td>7.56</td><td>10.51</td><td>0.13</td><td>0.00</td><td>0.25</td><td>29.56</td></tr><tr><td>2</td><td>258 4564</td><td>5.67</td><td>3.22</td><td>9.14</td><td>9.21</td><td>0.52</td><td>0.00</td><td>2.61</td><td>29.91</td></tr><tr><td>3</td><td>262 4259</td><td>8.32</td><td>7.54</td><td>10.24</td><td>9.52</td><td>0.01</td><td>0.00</td><td>0.02</td><td>31.96</td></tr><tr><td>4</td><td>291 4684</td><td>1.96</td><td>1.96</td><td>1.96</td><td>10.48</td><td>0.00</td><td>0.00</td><td>0.00</td><td>22.88</td></tr><tr><td>5</td><td>282 5184</td><td>6.25</td><td>4.44</td><td>7.66</td><td>9.60</td><td>1.01</td><td>0.00</td><td>1.81</td><td>22.52</td></tr><tr><td rowspan="5">100</td><td>50 1</td><td>58 2930</td><td>5.24</td><td>3.38</td><td>6.83</td><td>15.33</td><td>0.00</td><td>0.00</td><td>0.00</td><td>32.47</td></tr><tr><td>2</td><td>53 3091</td><td>1.99</td><td>0.49</td><td>3.49</td><td>12.85</td><td>0.46</td><td>0.03</td><td>1.59</td><td>23.84</td></tr><tr><td>3</td><td>71 2977</td><td>2.57</td><td>0.97</td><td>6.18</td><td>13.93</td><td>0.19</td><td>0.00</td><td>0.37</td><td>33.75</td></tr><tr><td>4</td><td>62 3311</td><td>7.70</td><td>2.66</td><td>11.87</td><td>13.67</td><td>0.38</td><td>0.00</td><td>1.00</td><td>37.85</td></tr><tr><td>5</td><td>67 2890</td><td>1.42</td><td>1.31</td><td>1.63</td><td>13.27</td><td>0.00</td><td>0.00</td><td>0.00</td><td>21.59</td></tr><tr><td rowspan="5"></td><td>100 1</td><td>123 3842</td><td>5.23</td><td>0.96</td><td>9.24</td><td>4.09</td><td>0.03</td><td>0.03</td><td>0.03</td><td>137.36</td></tr><tr><td>2</td><td>121 3767</td><td>9.25</td><td>5.89</td><td>12.37</td><td>3.69</td><td>1.28</td><td>0.00</td><td>6.24</td><td>197.63</td></tr><tr><td>3</td><td>137 3725</td><td>7.21</td><td>4.62</td><td>9.96</td><td>4.22</td><td>0.23</td><td>0.00</td><td>0.62</td><td>142.59</td></tr><tr><td>4</td><td>121 3749</td><td>6.57</td><td>3.55</td><td>9.98</td><td>3.99</td><td>1.06</td><td>0.00</td><td>5.25</td><td>167.48</td></tr><tr><td>5</td><td>129 3893</td><td>2.17</td><td>1.64</td><td>2.80</td><td>3.30</td><td>0.11</td><td>0.00</td><td>0.28</td><td>141.94</td></tr><tr><td rowspan="5"></td><td>150 1</td><td>177 4312</td><td>10.63</td><td>4.17</td><td>13.01</td><td>4.28</td><td>0.93</td><td>0.00</td><td>4.66</td><td>324.90</td></tr><tr><td>2</td><td>188 4584</td><td>8.89</td><td>3.77</td><td>13.46</td><td>4.71</td><td>1.34</td><td>0.00</td><td>6.65</td><td>365.70</td></tr><tr><td>3</td><td>191 4724</td><td>8.82</td><td>5.86</td><td>12.47</td><td>4.67</td><td>1.36</td><td>0.28</td><td>2.46</td><td>251.93</td></tr><tr><td>4</td><td>189 4649</td><td>10.90</td><td>7.14</td><td>13.85</td><td>5.40</td><td>1.01</td><td>0.00</td><td>2.41</td><td>234.38</td></tr><tr><td>5</td><td>192 4502</td><td>7.01</td><td>2.95</td><td>10.35</td><td>4.77</td><td>0.75</td><td>0.33</td><td>0.71</td><td>264.40</td></tr><tr><td rowspan="5"></td><td>200 1</td><td>230 4124</td><td>7.49</td><td>4.92</td><td>10.14</td><td>2.79</td><td>0.00</td><td>0.00</td><td>0.00</td><td>253.17</td></tr><tr><td>2</td><td>261 5120</td><td>9.79</td><td>7.01</td><td>11.19</td><td>3.16</td><td>1.20</td><td>0.29</td><td>2.09</td><td>271.57</td></tr><tr><td>3</td><td>246 4660</td><td>8.51</td><td>4.59</td><td>10.52</td><td>2.86</td><td>1.06</td><td>0.00</td><td>1.59</td><td>272.74</td></tr><tr><td>4</td><td>245 4673</td><td>7.01</td><td>4.86</td><td>8.88</td><td>3.06</td><td>0.03</td><td>0.00</td><td>0.00</td><td>251.32</td></tr><tr><td>5</td><td>258 4699</td><td>6.01</td><td>2.43</td><td>9.45</td><td>3.13</td><td>0.44</td><td>0.00</td><td>0.87</td><td>336.05</td></tr><tr><td colspan="3">Average</td><td>6.11</td><td>3.72</td><td>8.44</td><td>5.75</td><td>0.52</td><td>0.09</td><td>1.40</td><td>101.21</td></tr></table>

Table 2. Computational results: untight-budget instances

<table><tr><td rowspan="2">n</td><td rowspan="2">m #</td><td rowspan="2" colspan="2">B opt</td><td colspan="3">EJEMO</td><td rowspan="2">sec</td><td colspan="3">VNS</td><td rowspan="2">sec</td></tr><tr><td>aver.</td><td>min</td><td>max</td><td>aver.</td><td>min</td><td>max</td></tr><tr><td rowspan="5">50</td><td>50 1</td><td>176</td><td>1684</td><td>0.00</td><td>0.00</td><td>0.00</td><td>1.99</td><td>0.00</td><td>0.00</td><td>0.00</td><td>1.00</td></tr><tr><td>2</td><td>143</td><td>935</td><td>0.00</td><td>0.00</td><td>0.00</td><td>1.88</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.66</td></tr><tr><td>3</td><td>158</td><td>1422</td><td>0.00</td><td>0.00</td><td>0.00</td><td>1.77</td><td>0.04</td><td>0.00</td><td>0.00</td><td>0.60</td></tr><tr><td>4</td><td>242</td><td>1228</td><td>0.00</td><td>0.00</td><td>0.00</td><td>1.81</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.53</td></tr><tr><td>5</td><td>269</td><td>1317</td><td>0.00</td><td>0.00</td><td>0.00</td><td>2.04</td><td>0.00</td><td>0.00</td><td>0.00</td><td>1.00</td></tr><tr><td rowspan="5"></td><td>100 1</td><td>277</td><td>2120</td><td>2.03</td><td>1.84</td><td>2.08</td><td>2.72</td><td>0.96</td><td>0.00</td><td>1.60</td><td>0.87</td></tr><tr><td>2</td><td>309</td><td>1854</td><td>0.00</td><td>0.00</td><td>0.00</td><td>2.75</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.88</td></tr><tr><td>3</td><td>238</td><td>1614</td><td>0.00</td><td>0.00</td><td>0.00</td><td>2.76</td><td>0.00</td><td>0.00</td><td>0.00</td><td>1.03</td></tr><tr><td>4</td><td>287</td><td>2822</td><td>0.35</td><td>0.00</td><td>0.89</td><td>2.82</td><td>0.00</td><td>0.00</td><td>0.00</td><td>1.47</td></tr><tr><td>5</td><td>263</td><td>2340</td><td>0.29</td><td>0.00</td><td>1.24</td><td>7.82</td><td>0.00</td><td>0.00</td><td>0.00</td><td>1.04</td></tr><tr><td rowspan="5"></td><td>150 1</td><td>394</td><td>2409</td><td>0.00</td><td>0.00</td><td>0.00</td><td>29.20</td><td>0.14</td><td>0.00</td><td>0.71</td><td>1.27</td></tr><tr><td>2</td><td>343</td><td>1815</td><td>0.00</td><td>0.00</td><td>0.00</td><td>5.22</td><td>0.00</td><td>0.00</td><td>0.00</td><td>1.52</td></tr><tr><td>3</td><td>443</td><td>1917</td><td>0.05</td><td>0.05</td><td>0.05</td><td>21.09</td><td>0.00</td><td>0.00</td><td>0.00</td><td>1.04</td></tr><tr><td>4</td><td>411</td><td>2143</td><td>0.00</td><td>0.00</td><td>0.00</td><td>1.71</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.92</td></tr><tr><td>5</td><td>362</td><td>2800</td><td>0.50</td><td>0.50</td><td>0.50</td><td>12.36</td><td>0.30</td><td>0.00</td><td>0.50</td><td>1.95</td></tr><tr><td rowspan="5"></td><td>200 1</td><td>446</td><td>2933</td><td>0.14</td><td>0.00</td><td>0.38</td><td>2.50</td><td>0.27</td><td>0.00</td><td>0.68</td><td>1.94</td></tr><tr><td>2</td><td>447</td><td>1989</td><td>0.03</td><td>0.00</td><td>0.05</td><td>23.44</td><td>0.17</td><td>0.00</td><td>0.85</td><td>2.04</td></tr><tr><td>3</td><td>466</td><td>1860</td><td>0.00</td><td>0.00</td><td>0.00</td><td>1.98</td><td>0.00</td><td>0.00</td><td>0.00</td><td>1.36</td></tr><tr><td>4</td><td>451</td><td>2414</td><td>0.00</td><td>0.00</td><td>0.00</td><td>16.87</td><td>0.00</td><td>0.00</td><td>0.00</td><td>4.75</td></tr><tr><td>5</td><td>478</td><td>3148</td><td>0.10</td><td>0.10</td><td>0.10</td><td>27.36</td><td>0.00</td><td>0.00</td><td>0.00</td><td>1.99</td></tr><tr><td rowspan="5">100</td><td>50 1</td><td>137</td><td>1335</td><td>0.18</td><td>0.00</td><td>0.30</td><td>13.17</td><td>0.00</td><td>0.00</td><td>0.00</td><td>2.63</td></tr><tr><td>2</td><td>186</td><td>832</td><td>0.12</td><td>0.12</td><td>0.12</td><td>11.39</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.77</td></tr><tr><td>3</td><td>156</td><td>1475</td><td>0.00</td><td>0.00</td><td>0.00</td><td>8.23</td><td>0.00</td><td>0.00</td><td>0.00</td><td>1.47</td></tr><tr><td>4</td><td>146</td><td>1586</td><td>1.56</td><td>1.07</td><td>2.40</td><td>6.07</td><td>0.34</td><td>0.00</td><td>0.57</td><td>4.62</td></tr><tr><td>5</td><td>111</td><td>2391</td><td>0.00</td><td>0.00</td><td>0.00</td><td>2.57</td><td>0.00</td><td>0.00</td><td>0.00</td><td>10.94</td></tr><tr><td rowspan="5"></td><td>100 1</td><td>211</td><td>1919</td><td>0.60</td><td>0.31</td><td>0.68</td><td>1.58</td><td>0.18</td><td>0.05</td><td>0.68</td><td>22.94</td></tr><tr><td>2</td><td>266</td><td>1662</td><td>1.13</td><td>0.60</td><td>1.26</td><td>3.20</td><td>0.18</td><td>0.18</td><td>0.18</td><td>7.14</td></tr><tr><td>3</td><td>239</td><td>1597</td><td>0.00</td><td>0.00</td><td>0.00</td><td>1.47</td><td>0.00</td><td>0.00</td><td>0.00</td><td>23.51</td></tr><tr><td>4</td><td>248</td><td>1406</td><td>2.39</td><td>0.21</td><td>3.84</td><td>1.51</td><td>0.00</td><td>0.00</td><td>0.00</td><td>2.60</td></tr><tr><td>5</td><td>249</td><td>2709</td><td>0.04</td><td>0.04</td><td>0.04</td><td>3.82</td><td>0.04</td><td>0.04</td><td>0.07</td><td>12.93</td></tr><tr><td rowspan="5"></td><td>150 1</td><td>380</td><td>1863</td><td>0.65</td><td>0.00</td><td>2.20</td><td>1.93</td><td>0.02</td><td>0.00</td><td>0.05</td><td>3.07</td></tr><tr><td>2</td><td>321</td><td>2505</td><td>0.01</td><td>0.00</td><td>0.04</td><td>2.17</td><td>0.00</td><td>0.00</td><td>0.00</td><td>21.88</td></tr><tr><td>3</td><td>421</td><td>1898</td><td>0.00</td><td>0.00</td><td>0.00</td><td>1.99</td><td>0.00</td><td>0.00</td><td>0.00</td><td>1.33</td></tr><tr><td>4</td><td>337</td><td>2292</td><td>0.02</td><td>0.00</td><td>0.09</td><td>3.82</td><td>0.00</td><td>0.00</td><td>0.00</td><td>29.81</td></tr><tr><td>5</td><td>339</td><td>2848</td><td>0.01</td><td>0.00</td><td>0.04</td><td>1.90</td><td>0.00</td><td>0.00</td><td>0.00</td><td>18.23</td></tr><tr><td rowspan="5"></td><td>200 1</td><td>408</td><td>1483</td><td>3.84</td><td>3.84</td><td>3.84</td><td>3.09</td><td>1.94</td><td>0.00</td><td>3.24</td><td>37.70</td></tr><tr><td>2</td><td>438</td><td>2683</td><td>0.63</td><td>0.48</td><td>0.78</td><td>1.22</td><td>0.23</td><td>0.11</td><td>0.26</td><td>29.58</td></tr><tr><td>3</td><td>485</td><td>2364</td><td>0.00</td><td>0.00</td><td>0.00</td><td>1.61</td><td>0.00</td><td>0.00</td><td>0.00</td><td>8.24</td></tr><tr><td>4</td><td>429</td><td>3024</td><td>0.11</td><td>0.03</td><td>0.20</td><td>2.25</td><td>0.01</td><td>0.00</td><td>0.03</td><td>14.27</td></tr><tr><td>5</td><td>470</td><td>2308</td><td>0.00</td><td>0.00</td><td>0.00</td><td>7.82</td><td>0.00</td><td>0.00</td><td>0.00</td><td>1.53</td></tr><tr><td>Average</td><td></td><td></td><td></td><td>0.37</td><td>0.23</td><td>0.53</td><td>6.27</td><td>0.12</td><td>0.01</td><td>0.24</td><td>7.08</td></tr></table>

$l _ { m i n }$ are equal to 10% and 1% of the number of the markets making part of the current solution, respectively.

For algorithm VNS we have easily set $q _ { m a x }   =   2 0$ and $q _ { m i n }   =   q _ { s t e p }   =   1$ as the best parameter values, whereas some testing has been required in order to choose the initial value for parameter l which is resulted to be more crucial. At this aim we have solved several instances with different values of parameter $l _ { m a x }$ . In Fig. 3 we report the average percentage errors with respect to the optimal solution value found by the VNS approach out of the 5 tight-budget instances (tight-budget line in the graph) and the 5 untight-budget instances (untight-budget line in the graph) with 100 markets and 100 products for five different values of the parameter $l _ { m a x }$ equal to 5, 10, 15, 20, and 25%, respectively. For this testing we have considered only one algorithm trial. We can notice how, in both the cases, the better algorithm performance can be obtained by setting $l _ { m a x }$ equal to $5 \%$ of the number of markets in the current solution. This result has been confirmed by other experiments carried out on instances with a different number of markets and products.

![](images/page_281_chart_4.jpg)

Fig. 3. Tuning of the parameter $l _ { m a x }$ over instances with 100 markets and 100 products

By comparing the two tables it is evident how tight-budget instances are the most difficult ones. In such instances EJEMO algorithm behaves rather poorly providing an average error equal to 6.11% out of the 40 solved instances (given the five trials). Moreover, it is never able to find the optimal solution value (cfr. column min in Table 1). Such bad performances are, on average, due to ChainEjection() procedure which fails to eject the right markets. Indeed, the simple selection rule used by such procedure to choose the chain of markets to be removed behaves acceptably good only when the number of good quality solutions is large enough as for untight-budget instances. On the contrary the Variable Neighborhood Search procedure yields an average error equal to 0.52% and finds the optimal solution value in 32 out of the 40 instances solved (considering the 5 trials). From the efficiency point of view, the computational time required by EJEMO is almost constant for all instances (its average value out of all instances is equal to 5.75 s), whereas the average computational time for the VNS algorithm grows quickly with the problem size reaching an average value of 276.97 s for instances with 100 markets and 200 products.

Both heuristics performance improves when untight-budget instances are taken into account. Table 2 shows that EJEMO provides an average percentage error out of all instances equal to 0.37% with a maximum error never larger than 3.84%. Moreover, given the five trials, it is able to find the optimal solution values in 27 out of 40 solved instances. The results obtained by the VNS approach are even better: this procedure yields an average percentage error equal to 0.12% out of the 40 solved instances and gets the optimal solution value (given the five trials) in all but three instances. The average computational times are close to 7 s for both the heuristics.

To conclude, if we consider tight-budget instances the ranking of the proposed algorithms in terms of solution values suggests VNS as a first choice followed by EJEMO. Nevertheless, if running time is of high relevance EJEMO may be used even if at a price of a lower performance. On the contrary for untight-budget instances procedure VNS is the dominant one providing solutions which are more effective and as efficient as those yielded by EJEMO.

## 5 Conclusions

In this paper we have analyzed a variant of the uncapacitated Traveling Purchasing Problem based on the minimization of the traveling costs while bounding the purchasing costs in the constraints. For this problem, which has found very little attention in the literature, we have introduced two different solution algorithms. The first one is an enhanced local search procedure which generates neighbor solution by ejecting chain of consecutive vertices from the current solution and is based on a simple tabu structure to avoid cycling (EJEMO algorithm). The second one is a straightforward implementation of a Variable Neighborhood Search scheme which uses a modification of the previous algorithm as local search routine.

Computational results on benchmark instances created for the problem have shown how EJEMO is an efficient and effective procedure when the solved instances are characterized by a large budget threshold (untight-budget instances). On the other side, the procedure may produce bad results when the number of good quality solutions is small as for the tight-budget instances.

On the contrary the VNS approach always provides effective solutions and in the case of untight-budget instances it is also efficient showing an average computational time equivalent to that of EJEMO.

As future developments we will study a dynamic version of the problem for the capacitated case. As a first step in this direction we will analyze the performance of the proposed heuristic algorithms as well as that of a new multi-start variant of the VNS approach when applied to the capacitated version of the problem. The best resulting approach will be used as solution algorithm for the dynamic routing problem.

## References

[1] Burstall M.R. (1966) A heuristic method for a job sequencing problem. Operational Research Quarterly 17: 291–304.

[2] Gendreau M., Hertz A., Laporte G. (1992) New insertion and postoptimization procedures for the Traveling Salesman Problem. Operations Research 40(6): 1086–1094.

[3] Golden B. L., Levy L., Dahl R. (1981) Two generalizations of the Traveling Salesman Problem. Omega 9: 439–445.

[4] Hansen, P., Mladenović N. (2001) Variable Neighborhood Search: principles and applications. European Journal of Operational Research 130: 449–467.

[5] Laporte G., Riera-Ledesma J., Salazar-Gonzàlez J.J. (2003) A branch-and-cut algorithm for the undirected Traveling Purchaser Problem. Operations Research 51(6): 940–951.

[6] Mansini R., Pelizzari M., Saccomandi R. (2005) An effective tabu search algorithm for the capacitated Traveling Purchaser Problem. Technical Report 2005-10-49, Dipartimento di Elettronica per l’Automazione, University of Brescia.

[7] Ong H.L. (1982) Approximate algorithms for the Traveling Purchaser Problem. Operations Research Letters 1: 201–205.

[8] Pearn W. L., Chien R. C. (1998) Improved solutions for the Traveling Purchaser Problem. Computers and Operations Research 25: 879–885.

[9] Ramesh T. (1981) Traveling purchaser problem. Operations Research 18: 78–91.

[10] Ravi R., Salman S. (1999) Approximation algorithms for the Traveling Purchaser Problem and its variants in network design. In: Proceedings of the 7th Annual European Symposium on Algorithms, Lecture Notes in Computer Science vol. 1643. Spriger, Berlin: 29–40.

[11] Renaud J., Boctor F. F., Laporte G. (2003) Heuristics for the traveling purchaser problem. Computers and Operations Research 30(4): 491–504.

[12] Riera-Ledesma J., Salazar-González J. J. (2005) A heuristic approach for the Traveling Purchaser Problem. European Journal of Operational Research 162(1): 142–152.

[13] Riera-Ledesma J., Salazar-González J. J. (2005) The Biobjective Traveling Purchaser Problem. European Journal of Operational Research 160: 599–613.

[14] Singh K. N., Van Oudheusden D. L. (1997) A branch and bound algorithm for the traveling purchaser problem. European Journal of Operational Research 97: 571–579.

[15] Voß S. (1996) Dynamic tabu search strategies for the traveling purchaser problem. Annals of Operations Research 63: 253–275.