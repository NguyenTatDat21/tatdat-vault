# Matheuristic algorithms for the parallel drone scheduling traveling salesman problem

**Mauro Dell’Amico** · **Roberto Montemanni** · **Stefano Novellani**

**Received: 21/05/2019 / Accepted: date**

**Abstract In a near future drones are likely to become a viable way of distributing parcels in a urban environment. In this paper we consider the parallel drone scheduling traveling salesman problem, where a set of customers requiring a delivery is split between a truck and a fleet of drones, with the aim of minimizing the total time required to service all the customers.**

**We present a set of matheuristic methods for the problem. The new approaches are validated via an experimental campaign on two sets of benchmarks available in the literature. It is shown that the approaches we propose perform very well on small/medium size instances. Solving a mixed integer linear programming model to optimality leads to the first optimality proof for all the instances with 20 customers considered, while the heuristics are shown to be fast and effective on the same dataset. When considering larger instances with 48 to 229 customers, the results are competitive with stateof-the-art methods and lead to 28 new best known solutions out of the 90 instances considered.**

**Keywords Traveling Salesman Problem · Drone-Assisted Deliveries · Mixed Integer Linear Programming · Heuristic Algorithms · Matheuristics**

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">M. Dell’Amico Department of Sciences and Methods for Engineering, University of Modena and Reggio Emilia, Via Amendola 2, 42122 Reggio Emilia, Italy</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">R. Montemanni Department of Sciences and Methods for Engineering, University of Modena and Reggio Emilia, Via Amendola 2, 42122 Reggio Emilia, Italy E-mail: roberto.montemanni@unimore.it</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">S. Novellani Department of Sciences and Methods for Engineering, University of Modena and Reggio Emilia, Via Amendola 2, 42122 Reggio Emilia, Italy</span></small>

## 1 Introduction

**E-commerce has experienced a boom in the last decades; indeed, the statistics portal Statista [7] shows an enormous increment in the e-commerce sales worldwide, whose value was already 1336 billion US dollars in 2014 and it is forecast to be of 4135 and 4878 billions in 2019 and 2020, respectively. The increase of on-line shopping has led to a high request of home delivery service. A recent Boston Consulting Group publication [27] shows that the amount of billions of founding dedicated to parcel and express delivery startups in 2016 was 20 times higher than the amount of 2014, only two years before. Another recent publication [16] reports that many e-commerce and parcel delivery companies are offering ever faster delivery, such as same-day and instant delivery. In fact, 20 to 25% of consumers are willing to pay more to receive their parcel on the same day, and 2% would require instant delivery. Those companies could offer this kind of deliveries because of the use of cutting-edge technology such as new apps and the use of different types of vehicles, for instance the use of aerial drones. In [16], the authors forecast that autonomous vehicles, including drones, will deliver about 80% of all parcels in the following ten years.**

**Food delivery has also been a booming industry in the last years and the fast and last mile delivery it requires it is now provided by bike couriers, but the same job could be done by drones in the future. Not only (cooked) food, but also delivery of other perishable goods such as groceries or medications could benefit from the use of drones; indeed the survey [16] reports that 27% and 26% of the respondents did not purchased groceries and medications, respectively, on-line because of too long delivery times. This shows a potential increase in those services if a faster mean like drones or autonomous vehicles were used. That is the direction where companies are going: for example UberEats is considering to launch food-delivery drones by 2021 [8].**

**On the other hand, one should not forget that drones are also used to allow and improve deliveries in remote areas or where the quality of infrastructure is poor. The first point is the case of mountainous areas such as in the Alps [6] or in small islands such as in North Sea [3], both performed by DHL; the second is the case of rural areas in China served by JD.com [5].**

**That said, the most relevant use of drones for parcel delivery is the one attempted by many companies such as Amazon [2], Alibaba [1], Alphabet [9], JD.com [4], etc, that consider to fly drones from a depot to customers or from a set of trucks that can launch and collect drones. By means of aerial drones, these companies can respond to the customers that require an ever fast delivery because of the advantages that aerial drones can offer: speed, flexibility, congestion avoidance, and the possibility to operate where other vehicles cannot.**

**Alongside the ferment in the industry, in the last years, researchers have started studying more and more the use of drones: if at the beginning the interest was mainly focused on the hardware aspects (battery endurance improvement, obstacles avoidance, on flight stability, etc.), the interest has moved** **to their operational use. At the beginning the focus was restricted to the military domain, but now, thanks to new possible applications, interest has raised also in the commercial sector, that includes, among the applications treated previously, the express parcel delivery.**

**Several problems that can arise in this field, among them we study a particular one that considers the parallel use of a truck and a set of drones. In the** Parallel Drone Scheduling Traveling Salesman Problem **(PDSTSP) a truck can leave the depot, serve a set of customers, and return to the depot, while the drones, in the meantime, can leave the depot, serve a customer, and return to the depot before serving other customers. Not all the customer can be served by the drones, either due to their location or the characteristic of their parcel. The objective of the problem is to minimize the completion time of the last vehicle returning to the depot, while serving all the customers.**

**In this paper we provide an simplified mixed integer linear programming (MILP) model for the PDSTSP and a set of matheuristic algorithms.**

**The paper is organized as follows: in Section 2 a brief literature review on related problems is provided. Section 3 provides a detailed problem description and a MILP formulation for the problem. In Section 4 the matheuristic methods we propose are described. Section 5 is about computational experiments and Section 6 concludes the paper.**

## 2 Literature review

**The PDSTSP is an NP-hard problem, being a generalization of two NP-hard problems, the Traveling Salesman Problem (TSP) and the Identical Parallel Machine Scheduling Problem [20].**

**In the recent survey [21], the authors treat deeply the problems that arise when drones are coupled with trucks for deliveries in the commercial sector: we head the interested reader to that survey. The survey classifies the PDSTSP in the class** Drones and vehicles performing independent tasks**, under the wider class called** Planning combined operations of drones with other vehicles**. While the vehicles perform independent tasks there is no need of synchronisation among them.**

**The PDSTSP was first introduced in [20]. They propose the first MILP formulation for the problem and simple greedy heuristics. In particular, they first partition the customers: all customers that can be visited by drones are set as to be visited by the drones in the initial solution and a TSP is solved to allocate the other customers to the truck. For the customers to be visited** by the drones, a parallel machine scheduling problem (denoted as $\mathrm { P | | C _ { \mathrm { m a x } } , }$ **using the notation by [12]) is solved to obtain the minimum makespan of the** partition. These two components needed to solve the TSP and the $\mathrm { P | | C _ { m a x } }$ **use both exact and heuristic methods. Several methods are used to solve the TSP. Among them a MILP solved to optimality (IP) and the savings heuristic (SAV). To solve the** $\mathrm { P | | C _ { m a x } }$ **they use a MILP solved to optimality (IP) and the long processing time first heuristic (LPT).**

**Another work aimed at solving the PDSTSP is the one presented in [18]. They present an improved formulation and an iterative two steps heuristic algorithm (Single-start two-stepH). They obtain the initial solution by building a giant TSP tour including all customers thanks to the nearest neighbour heuristic, where all customers are visited by the truck. The algorithm then tries to improve the solution: the sequence is separated into two parts, one for the truck and another for the drones. This split is performed by an elegant decoding procedure. The route of the truck is thus reoptimized heuristically, while the sequences of the drones are determined by using a longest processing time heuristic. They reiterate the procedure until the solution cannot be improved anymore. Eventually a multi-start mechanism is used (Multi-start two-stepH).**

**Two related problems, where a set of drones can serve in parallel the customers from a depot but there is no truck, are proposed in [11] and [25]. Drones can serve multiple customers, have a capacity and a maximum operation time, making the treated problem a generalization of the vehicle routing problem.**

**A problem where multiple drones, multiple trucks and multiple depots are considered is presented in [14]. This problem is a generalisation of the PDSTSP where drones can perform pickup after dropping parcels, customers can be visited twice in different time windows, and single and multiple depots instances are considered. The problem is called** PDSTSP Drop-Pickup**. A constraint programming approach is developed to tackle the problem.**

**A dynamic variant of the PDSTSP, called the** same-day delivery with heterogeneous fleets of drones and vehicles **is studied in [26]. In this problem requests arrive dynamically and can be accepted or not. In the case they are, they must be allocated to drones or truck maximizing the number of customers that are served. To solve the problem, the authors proposed an adaptive dynamic programming called parametric policy function approximation. Drone shipping versus truck delivery in a cross-docking system, with multiple products and multiple fleets, is finally considered in [24]. The authors want to define the operations of trucks and drones minimizing a bi-objective function that includes both cost and time.**

## 3 Problem description and mathematical fomulation

The PDSTSP can be represented on a complete directed graph $G = ( V , A )$ where the node set $V   =   \{ 0 , 1 , . . . , n \}$ **represents the depot (node 0) and the set of customers** $C   =   \{ 1 , . . . , n \} . \mathrm { ~ A ~ }$ **truck and a set U of |U| homogeneous drones are available to deliver parcels to the customers. The truck starts from the depot 0, visits a subset of the customers, and returns back to the depot. The drones operate back and forth trips from the depot to a single customer (one parcel per trip). Not all the customers can be served by a drone due to practical reasons like the weight of the parcel or an excessive distance of the** customer location from the depot. Let $\dot { C } ^ { U } \subseteq C$ **denotes the set of customers that can be served by drones. These customers are referred to as** drone-eligible **in the remainder of the paper. The travel time paid by the truck to go from** node i to node $j$ is denoted as $t _ { i j } ^ { T }$ **, while the time required by a drone to serve** a customer i (back and forth) is denoted as $t _ { i } ^ { U }$ **. The truck and the drones start from the depot at time 0, and the objective of the PDSTSP is to minimize the time required to complete all the deliveries and to have the truck and all the drones returned back to the depot. Since truck and drones work in parallel, the objective function translates into minimizing the maximum mission time among the vehicles.**

**The PDSTSP can be described in mathematical terms as a MILP model. In the remainder of the section we will propose a model that can be seen as a simplification of that originally appeared in [18]. The latter can be in turn interpreted as an improved version of the model proposed in [20] with subtour elimination constraints used in place of Miller-Tucker-Zemlin constraints [19].**

**The following variables are used in the model:**

$-   x _ { i j }   =   1$ **if node** $i \in V$ **is visited immediately before node** $j   \in   V$ **by the truck; 0 otherwise;**

$y _ { i } ^ { k } = 1$ if node $i \in C ^ { U }$ **is visited by drone** $k \in U ;$ **0 otherwise;**

**– α = time required to complete all the delivery missions.**

**The resulting model (P DS) reads as follows:**

**(P DS) min α**

**(1)**

$$
\text {s.t.} \alpha \geq \sum_ {i \in V} \sum_ {j \in V} t _ {i j} ^ {T} x _ {i j}\tag{2}
$$

$$
\alpha \geq \sum_ {i \in C ^ {U}} t _ {i} ^ {U} y _ {i} ^ {k}
$$

$$
\forall k \in U\tag{3}
$$

$$
\left| \sum_ {i \in V} x _ {i j} + \overbrace {\sum_ {k \in U} y _ {j} ^ {k}} ^ {\text {if} j \in C ^ {U}} = 1 \right|
$$

$$
\forall j \in C\tag{4}
$$

$$
\left| \sum_ {j \in V} x _ {i j} \overbrace {\sum_ {k \in U} y _ {i} ^ {k}} ^ {\text {if} i \in C ^ {U}} = 1 \right|
$$

$$
\forall i \in C\tag{5}
$$

$$
\sum_ {j \in V} x _ {j i} = \sum_ {h \in V} x _ {i h}
$$

$$
\forall i \in V\tag{6}
$$

$$
\sum_ {i \in S} \sum_ {j \in V \setminus S} x _ {i j} + \sum_ {i \in S} \sum_ {k \in U} y _ {i} ^ {k} \geq 1
$$

$$
\forall S \subseteq V, 0 \in S\tag{7}
$$

$$
x _ {i j} \in \{0, 1 \}
$$

$$
\forall i, j \in V\tag{8}
$$

$$
y _ {i} ^ {k} \in \{0, 1 \}
$$

$$
\forall i \in C ^ {U}, k \in U\tag{9}
$$

$$
\alpha \in \mathbb {R}\tag{10}
$$

**The objective function (1) minimizes the maximum working time among all the vehicles. The working time of the truck is considered in constraint (2)**

**while that of the drones is computed in (3). Constraints (4) and (5) state that each customer has to be visited either by the truck, or by one of the drones in case the customer is drone-eligible. Constraints (6) are classic flow conservation constraints for the truck tour. Inequalities (7) are connectivity constraints. Finally, constraints (8), (9) and (10) set the domain for each set of variables.**

## 3.1 Implementation details

**The model PDS presented in Section 3 has an exponential number of constraints (7) and in order to have competitive solution times, it has to be solved in a branch-and-cut fashion, where these inequalities are separated dynamically and added only if violated by the current solution. In this way, optimality can be proven with only a subset of them will being actually generated. In order to separate violated inequalities (7), a maximum flow problem [10] from** node 0 to each other node $i \in C$ is solved on a complete support graph con**structed as follows. The node set is V and arc capacities are given by the value of the x variables in the continuous solution under investigation, to which, for all** $i \in C .$ **also the value of the y variables involving node i are added to the arc (0, i). If the minimum cut** $( S , V \setminus S )$ **has a capacity strictly smaller than one, than this cut violates (7).**

**Another enhancement we implemented to speed up the computation times is to feed the MILP model with an initial solution representing a truck tour visiting all the customers (no drone is used). The tour is obtained by solving a classic TSP with the heuristic algorithm LKH (see [15] for a formal description of both the problem and the solving method).**

## 4 Matheuristic algorithms

**In this Section some heuristic methods, all relying on the MILP model discussed in Section 3, are described. The aim is to cover a spectrum of methods able to provide different trade-offs between the quality of the final solution and the computation time required to produce it.**

## 4.1 Fast heuristics

**A first simple heuristic called** $F a s t$ **in the sequel, is as follows. A TSP instance with the customers of the PDSTSP is solved by the heuristic algorithm LKH [15], obtaining a tour s such that customer** $s _ { i }$ **i**s in position i in the sequence. **The model PDS described in Section 3 is then solved with the following additional constraints:**

$$
x _ {s _ {i} s _ {j}} = 0 \quad i, j \in \{1, 2, \dots , | s | \}, i > j\tag{11}
$$

**Constraints (11) impose that the residual truck tour obtained after the assignment of a certain number of customers to the drones still respects the order imposed by the original tour s. Note that the selection of the customers assigned to the drone is delegated to the MILP itself.**

## Fast-2 heuristic

**The method can be seen as an iterative version of the method** Fast **above. The first step computes an initial sequence which visits all the customers, as in** Fast**. The sequence is then evolved by applying classic 2-opt [17] topological exchanges to the sequence. For each 2-opt move, the corresponding sequence s is used to run model PDS with the additional constraints (11) (as in** Fast**) in order to evaluate its cost. If a new improved solution is found, it becomes the reference one and the algorithm continues with the next 2-opt move. We stop when a loop of all possible 2-opt moves has been attempted without identifying improving solutions.**

## Fast-3 heuristic

**The method works according to the same logic of** Fast-2**, with the only remarkable difference that the changes to the reference sequence are carried out according to the logic of the classic 3-opt local search method [17].**

## 4.2 Random Restart Local Search (RRLS)

**This local search is more tailored to the characteristics of the PDSTSP with respect to those described in the previous sections. The idea is to optimize the truck tour with state-of-the-art heuristics as a TSP, and to delegate the MILP model PDS to adjust such a truck tour by inserting appropriate drone deliveries, with some controlled freedom in modifying the input truck route itself. An iterative mechanism can be derived by re-optimizing the truck tour once it has been modified by the MILP solver. Once a local minimum is reached, the truck tour is partially destroyed, and the process is started again in the hope of visiting a different region of the search space.**

**The method can be described through the following pseudocode:**

## 1. Bestcost = +∞

**2. A TSP instance with the customers of the PDSTSP is solved with algorithm LKH [15], obtaining a sequence of customers s such that customer** $s _ { i }$ **i**s in **position i in the sequence. (Note that at this stage the tour s covers all the customers, while during the execution of the algorithm this might not be always the case.)**

**3. The MILP model PDS described in Section 3 is then solved with the ad**ditional constraints (11) giving a solution Sol with cost $c ( S o l )$ Let z denote the sequence of customers visited by the truck in $S o l .$

4. If c(Sol) < Bestcost then Bestcost = c(Sol) and $B e s t s o l = S o l .$

**5. Algorithm LKH [15] is run on the customers contained in the sequence z to improve the truck tour, obtaining the optimized sequence s.**

**6. If** $s \equiv z$ **then we generate a new truck sequence s by randomly selecting** |z| customers, among which all that in $C \stackrel { - } { \setminus } C ^ { U }$ **. The tour is optimized by the algorithm LKH [15].**

**7. If the exit criterion is not met (this is typically a maximum computation time), go to step 3.**

## 4.2.1 Implementation strategy for large instances

**When attacking large instances, the computational time required to solve the model PDS, even when inequalities (11) are inserted, might be too long. For this reason, when** $| C | \; > \; 2 0$ **, we also add further constraints to the model PDS. In this way the time required to solve the MILP is reduced, making it possible to carry out more iterations of the heuristic in a given time limit. The drawback is that the constraints reduce the search space region explored by the MILP, potentially increasing the number of iterations required to converge. The trade-off is however in favour of the efficiency of the method, for large instances. Let us consider a customer j currently not inserted in truck sequence s. The following inequalities (12) and (13) forbid truck routes that invert the order of some of the customers with respect to the original sequence** $\mathcal { S } _ { \gamma }$ **after the insertion of customer j in the sequence.**

$$
\sum_ {1 \leq k <   i} x _ {j s _ {k}} \leq 1 - x _ {s _ {i j}} \quad \forall i \in \{2, \dots , | s | \}, j \notin s\tag{12}
$$

$$
x _ {j s _ {i}} \leq 1 - \sum_ {i <   k \leq | s |} x _ {s _ {k} j} \quad \forall i \in \{1, 2, \dots , | s | - 1 \}, j \notin s\tag{13}
$$

**Inequalities (14) strength the interaction between x and y variables in the case when nodes of the input truck sequence s are assigned to the drones.** They impose that $x _ { s _ { i } s _ { j } } , j > i$ **can be 1 only if all the nodes between i and j are moved to the drones.**

$$
x _ {s _ {i} s _ {j}} \leq \sum_ {m \in U} y _ {s _ {k}} ^ {m} \quad \forall i, j, k \in \{1, 2, \dots , | s | \}: i <   k <   j; j - i <   \delta\tag{14}
$$

**The parameter δ indicates the maximum distance over the sequence for which the constraints are added. For all the experiments presented in the paper we will have** $\delta = 2 0$ **. Note that inequalities (14) improve the quality of the linear relaxation of the enriched model, although they do not impose anything new to the optimal solution.**

**Further changes are introduced to the algorithm to make the MILP more tractable. In particular, the step 6 of the original RRLS algorithm is substituted by the following:**

**6\*. If** $s \equiv z$ **the**n (a) define a new random truck sequence containing all the **customers; (b) The tour is optimized by the LKH heuristic on an artificial** graph where the truck distances $t _ { i j } ^ { T }$ **are increased by a random factor, with a maximum of** $\gamma \%$ **(set to 80% in our experiments).**

**Having a giant tour covering all the customers makes the MILP easier to solve because the choices it has to do are restricted to which customers to assign to the drone(s).**

**A final modification to the original RRLS algorithm is done in step 3, where the solving process of the MILP model PDS is interrupted after** $\beta$ **seconds. We hope the solver has already found a heuristic solution at that stage and that the solver is only working on the lower bound to close its optimality gap. This appears to apply in our case, with** $\beta = 1 0$ **seconds. This value is kept for all the experiments presented in Section 5.3.**

## 5 Computational experiments

**The model discussed in Sections 3 and the heuristic approaches based on it have been tested on the benchmark sets introduced in [20] and [18], that contain instances with the number of customers in the range from 10 to 229. The methods have been implemented in ANSI C and all the MILPs have been solved with Gurobi 8.1 [13]. All the tests have been run on a computer equipped with an Intel(R) Xeon(R) E5-2620 v4 2.10GHz processor (a single thread was used during the testing), but in order to simplify the comparison with the work previously published, computation times are in some contexts normalized to appropriate reference machines, according to [22].**

**The experiments are organized based on the set of instances considered. In particular, for the studies presented in Sections 5.1 and 5.2 the instances proposed in [20] are considered, while for Section 5.3 the instances introduced in [18] are used. For each set, the most relevant methods among those we present will be run and the results compared with all those available in the state-of-the-art literature.**

**The interested reader can find extended results and solutions at** http://www.or.unimore.it/site/home/online-resources.html.

## 5.1 Instances with 10 customers

**The instances analysed in this section have been originally proposed by Murray and Chu in [20]. In these instances cartesian coordinates are given for both the depot and the customers. The speed of both the truck and the drones was fixed at 25 miles/hour. Distances were computed as Manhattan distances for the vehicle and as Euclidean distances for the drones. Different locations are implemented for the depot, given the same set of customers, and such location was selected as being either near the center of all customers, near the edge of the customer region, or at the origin of the cartesian axis. Customer** **locations were generated such that either 20%, 40%, 60%, or 80% of them were located within the drones range from the depot, with the drone having a flight endurance of 30 minutes. Finally, 10-20% of the customers were arbitrarily set as not drone-eligible because of excessive parcel weights. A total of 120 configurations with 10 customers were created and these instances were solved with a single truck and either one, two, or three drones, resulting in 360 test instances. In Table 1 we report the results obtained by the exact approach (Exact (IP)) and by the heuristic methods presented in [20] (we refer the interested reader to this paper for a description of the approaches), by the two heuristics described in Mbiadou Saleu et al. [18] (where the interested reader is addressed for the details of the methods), and by our exact approach, called PDS, described in Section 3. All the computation times reported are normalized to the Intel Core i7-860 2.80GHz processor used in [20] for an easier comparison, using a conversion factor of 1.258 for the computation time of the methods we developed and of 1.12042 for the times of the methods presented in [18]. These conversion factors are obtained according to [22].**

Table 1 Results of the algorithms on the instances with 10 customers from [20].

<table><tr><td rowspan="2">Method</td><td colspan="2">gap %</td><td rowspan="2">#opt</td><td colspan="2">time (sec)</td></tr><tr><td>avg</td><td>max</td><td>avg</td><td>max</td></tr><tr><td>IP/IP</td><td>0.12</td><td>10.13</td><td>299</td><td>2.49</td><td>29.97</td></tr><tr><td>IP/LPT</td><td>0.12</td><td>10.13</td><td>300</td><td>2.31</td><td>28.85</td></tr><tr><td>Savings/IP</td><td>1.57</td><td>20.68</td><td>209</td><td>0.24</td><td>8.26</td></tr><tr><td>Savings/LPT</td><td>1.58</td><td>20.68</td><td>209</td><td>0.00</td><td>0.01</td></tr><tr><td>Exact (IP)</td><td>0.00</td><td>0.00</td><td>360</td><td>0.32</td><td>2.02</td></tr><tr><td>Single-start two-stepH</td><td>0.12</td><td>8.51</td><td>278</td><td>0.19</td><td>0.36</td></tr><tr><td>Multi-start two-stepH</td><td>0.02</td><td>4.45</td><td>313</td><td>3.59</td><td>3.65</td></tr><tr><td>PDS</td><td>0.00</td><td>0.00</td><td>360</td><td>0.08</td><td>0.57</td></tr></table>

**For each method considered, the average and maximum (over the 360 instances) optimality gap with respect to optimal solutions (**gap **%) are presented together with the number of optimal solution retrieved (#** opt**) and theaverage and maximum computation times (**time (sec)**).**

**The analysis of Table 1 suggests that model PDS is the most efficient way to tackle the small-size instances considered here. In particular, it is interesting to observe how the model PDS we propose seems to outperform the MILP model discussed in [20] (**Exact (IP)**). We think this mainly depends on the use of subtour elimination constraints in place of Miller-Tucker-Zemlin constraints [19].**

## 5.2 Instances with 20 customers

**In this section we consider the 360 instances with 20 customers presented in [20] and generated with the same procedure described in Section 5.1 for the instances with 10 customers.**

**In Table 2 the results of the methods discussed in [20] are compared with those of the methods proposed in this paper (PDS, Fast, Fast-2, Fast-3 and**

**RRLS). Namely, we consider the direct solution of the model PDS, either with a maximum execution time of 180 seconds (truncated run), or up to completion. The results after 180 seconds are reported since 180 seconds is the maximum computation time allowed to solve the model discussed in [20] (**Exact (IP)**). As already done for Table 1, computation times are normalized to the Intel Core i7-860 2.80GHz processor used in [20] for an easier comparison, using a conversion factor of 1.258 obtained according to [22] for the computation time of the methods we developed.**

**On top of the information already provided in Table 1, we now also report some of the information internally perceived by the MILP solver at the end of truncated runs. Namely, we show the optimality gap (with respect to the lower bound produced by the solver itself) and number of optimal solutions certified (**gap **% and # opt).**

**Two observations can be done about the results presented in Table 2. The first is about the option of solving directly the model PDS: this is still a viable solution for these instances, since the solver is able to provide very low optimality gaps already in 180 seconds. Moreover, the solver run on PDS is able to prove optimality for all the instances in acceptable times (below two minutes on average, and with a maximum of approximately 8 hours for one instance that can be classified as an outlier). Note that for some instances an optimal solution has been reported in this paper for the first time. The second conclusion is about the use of the heuristic algorithms we propose. They all provide very low optimality gap in a few seconds. The computation time is inversely proportional to the quality, so a clear trade-off emerges.**

**In Table 3 the results obtained by the methods presented in [18] on the 360 instances with 20 customers introduced in [20] are compared with those of the of the relevant methods proposed in this paper (in bold). All the computation times have been normalized to the Intel core(TM) i5-6200 U 2.30Ghz processor used in [18] for an easier comparison, using a conversion factor of 1.035 obtained according to [22] for the computation time of the methods we developed.**

**For most of the methods (and anyway where explicitly indicated) the computation has been interrupted after 3 seconds, in order to fairly compare with the experiments of [18]. Note that the method RRLS is not considered here since it is not designed to run on such a shorter time scale. Note that the information available in [18] does not allow to have precise figures for the optimality gaps and the number of optimal solutions retrieved by the methods presented in that paper, since comparisons are there made against heuristic solutions, and not against optimal solutions, as we do. For this reason, only optimistic estimates from above can be provided for [18].**

**From Table 3 it emerges that solving the model PDS directly produces results comparable to (if not better than) those of the heuristic methods proposed in [18] on a short time scale of 3 seconds. Letting the solver run for longer computation times also guarantees an optimality proof, which is not possible with a purely heuristic algorithm. The results of the matheuristic approaches we propose appear more robust than those of the methods proposed in [18],** **having a substantially smaller maximum optimality gap on these benchmarks. On the other hand, it is interesting to observe how** Fast-2 **seems to perform better than** Fast-3 **on short runs like those considered here (3 seconds). This depends on the intrinsic characteristics of the methods.**

Table 2 Results of the algorithms on the instances with 20 customers from [20]. Comparison with the methods proposed in [20].

<table><tr><td rowspan="2">Method</td><td colspan="2"> $\overline{gap}$ %</td><td>#</td><td colspan="2">gap %</td><td>#</td><td colspan="2">time (sec)</td></tr><tr><td>avg</td><td>max</td><td>opt</td><td>avg</td><td>max</td><td>opt</td><td>avg</td><td>max</td></tr><tr><td>IP/IP</td><td>-</td><td>-</td><td>-</td><td>0.248</td><td>5.530</td><td>302</td><td>495.00</td><td>21510.61</td></tr><tr><td>IP/LPT</td><td>-</td><td>-</td><td>-</td><td>0.340</td><td>18.000</td><td>291</td><td>498.00</td><td>21521.31</td></tr><tr><td>Savings/IP</td><td>-</td><td>-</td><td>-</td><td>3.876</td><td>18.827</td><td>88</td><td>3.72</td><td>80.68</td></tr><tr><td>Savings/LPT</td><td>-</td><td>-</td><td>-</td><td>3.982</td><td>18.827</td><td>81</td><td>0.01</td><td>0.07</td></tr><tr><td>Exact (IP)</td><td></td><td></td><td>273</td><td>0.020</td><td>2.870</td><td>352</td><td>77.78</td><td>180.00</td></tr><tr><td>PDS (180 sec)</td><td>0.300</td><td>26.931</td><td>349</td><td>0.004</td><td>0.677</td><td>356</td><td>10.98</td><td>180.00</td></tr><tr><td>PDS (unlimited)</td><td>-</td><td>-</td><td>360</td><td>0.000</td><td>0.000</td><td>360</td><td>109.55</td><td>28698.71</td></tr><tr><td>Fast</td><td>-</td><td>-</td><td>-</td><td>0.834</td><td>7.932</td><td>225</td><td>0.03</td><td>1.11</td></tr><tr><td>Fast-2</td><td>-</td><td>-</td><td>-</td><td>0.260</td><td>6.513</td><td>309</td><td>0.12</td><td>4.52</td></tr><tr><td>Fast-3</td><td>-</td><td>-</td><td>-</td><td>0.046</td><td>4.077</td><td>342</td><td>1.03</td><td>21.51</td></tr><tr><td>RRLS (180 sec)</td><td>-</td><td>-</td><td>-</td><td>0.000</td><td>0.000</td><td>360</td><td>79.21</td><td>180.00</td></tr></table>

Table 3 Results of the algorithms on the instances with 20 customers from [20]. Comparison with the methods proposed in [18].

<table><tr><td rowspan="2">Method</td><td colspan="2"> $\overline{gap}$ %</td><td>#</td><td colspan="2">gap %</td><td>#</td><td colspan="2">time (sec)</td></tr><tr><td>avg</td><td>max</td><td>opt</td><td>avg</td><td>max</td><td>opt</td><td>avg</td><td>max</td></tr><tr><td>Single-start two-stepH</td><td>-</td><td>-</td><td>-</td><td>≥ 0.510</td><td>≥ 23.470</td><td>≤ 225</td><td>0.21</td><td>0.56</td></tr><tr><td>Multi-start two-stepH</td><td>-</td><td>-</td><td>-</td><td>≥ 0.150</td><td>≥ 23.470</td><td>≤ 337</td><td>3.07</td><td>3.32</td></tr><tr><td>PDS (3 sec)</td><td>2.161</td><td>41.722</td><td>279</td><td>0.256</td><td>27.337</td><td>332</td><td>0.96</td><td>3.00</td></tr><tr><td>PDS (unlimited)</td><td>0.000</td><td>0.000</td><td>360</td><td>0.000</td><td>0.000</td><td>360</td><td>97.78</td><td>25615.03</td></tr><tr><td>Fast</td><td>-</td><td>-</td><td>-</td><td>0.834</td><td>7.932</td><td>225</td><td>0.03</td><td>1.11</td></tr><tr><td>Fast-2 (3 sec)</td><td>-</td><td>-</td><td>-</td><td>0.300</td><td>7.652</td><td>304</td><td>0.21</td><td>2.69</td></tr><tr><td>Fast-3(3 sec)</td><td>-</td><td>-</td><td>-</td><td>0.435</td><td>7.242</td><td>283</td><td>0.32</td><td>3.00</td></tr></table>

## 5.3 Instances with 48-229 customers

**The instances considered in this section have been adapted to the P DST SP starting from classic TSPLIB instances [23] and represent challenging instances. They have been first introduced in [18]. The number in each instance name corresponds to the number of customers, ranging from 48 to 229. Manhattan distances are used for the truck and Euclidean distances for the drones. For each original T SP instance, several P DST SP were generated by modifying the following parameters: the position of the depot, which is either in the center of the customers, or in one corner of the customers’ region; the percentage of drone-eligible customers, ranging from 0% to 100%; the speed of the drones, which is expressed as a factor of the vehicle speed, with values ranging from 1 to 5; the number of drones, that are between 1 and 5. The tables are organized in blocks to highlights series of tests where a single construction parameter is modified from the reference instance (in the first row). We refer** **the interested reader to [18] for a detailed description of the instances, and for a procedure to generate them univocally.**

**Tables 4-9 report the results obtained, where each table refers to the instances derived from a single original TSPLIB problem. Each instance is charaterized by some** Instance settings**, namely the percentage of drone-eligible customers over the total (**el**), the drone speed (**sp**), the number of drones (**#**) and the depot location (**dp**). For each instance, we report the cost of the best known solution, which is obtained by the methods described in [18] with a maximum computation time of 300 seconds (on the machine adopted for their study), and the results of two relevant heuristics described in Section 4. Namely, we consider Fast and RRLS and for each of them we report the results obtained, the gaps with respect to the best known results presented in [18], and the computation times required to retrieve the reported solutions.**

Table 4 Results of the algorithms on the TSPLIB instance att48 from [18].

<table><tr><td colspan="4">Instance settings</td><td rowspan="2">Best known</td><td colspan="3">Fast</td><td colspan="3">RRLS</td></tr><tr><td>el</td><td>sp</td><td>#</td><td>dp</td><td>cost</td><td>gap %</td><td>sec</td><td>cost</td><td>gap %</td><td>sec</td></tr><tr><td>80</td><td>2</td><td>1</td><td>1</td><td>29954.00</td><td>31340.00</td><td>4.63</td><td>0.10</td><td>29954.00</td><td>0</td><td>20.73</td></tr><tr><td>80</td><td>2</td><td>1</td><td>2</td><td>33798.00</td><td>33798.00</td><td>0.00</td><td>0.10</td><td>33798.00</td><td>0</td><td>0.13</td></tr><tr><td>0</td><td>2</td><td>1</td><td>1</td><td>42136.00</td><td>42136.00</td><td>0.00</td><td>0.05</td><td>42136.00</td><td>0</td><td>0.03</td></tr><tr><td>20</td><td>2</td><td>1</td><td>1</td><td>38662.00</td><td>40082.00</td><td>3.67</td><td>0.07</td><td>38662.00</td><td>0</td><td>0.12</td></tr><tr><td>40</td><td>2</td><td>1</td><td>1</td><td>31592.00</td><td>35780.00</td><td>13.26</td><td>0.09</td><td>31592.00</td><td>0</td><td>95.60</td></tr><tr><td>60</td><td>2</td><td>1</td><td>1</td><td>30788.80</td><td>33310.00</td><td>8.19</td><td>0.11</td><td>30788.80</td><td>0</td><td>53.08</td></tr><tr><td>100</td><td>2</td><td>1</td><td>1</td><td>27784.00</td><td>28490.00</td><td>2.54</td><td>0.21</td><td>27784.00</td><td>0</td><td>141.98</td></tr><tr><td>80</td><td>1</td><td>1</td><td>1</td><td>33234.00</td><td>35226.00</td><td>5.99</td><td>0.18</td><td>33234.00</td><td>0</td><td>602.65</td></tr><tr><td>80</td><td>3</td><td>1</td><td>1</td><td>29142.00</td><td>30406.00</td><td>4.34</td><td>0.13</td><td>29142.00</td><td>0</td><td>330.17</td></tr><tr><td>80</td><td>4</td><td>1</td><td>1</td><td>28686.00</td><td>30010.00</td><td>4.62</td><td>0.11</td><td>28686.00</td><td>0</td><td>32.20</td></tr><tr><td>80</td><td>5</td><td>1</td><td>1</td><td>28610.00</td><td>29862.00</td><td>4.38</td><td>0.11</td><td>28610.00</td><td>0</td><td>4.69</td></tr><tr><td>80</td><td>2</td><td>2</td><td>1</td><td>28686.00</td><td>30010.00</td><td>4.62</td><td>0.13</td><td>28686.00</td><td>0</td><td>276.29</td></tr><tr><td>80</td><td>2</td><td>3</td><td>1</td><td>28610.00</td><td>29862.00</td><td>4.38</td><td>0.10</td><td>28610.00</td><td>0</td><td>155.78</td></tr><tr><td>80</td><td>2</td><td>4</td><td>1</td><td>28610.00</td><td>29862.00</td><td>4.38</td><td>0.08</td><td>28610.00</td><td>0</td><td>200.63</td></tr><tr><td>80</td><td>2</td><td>5</td><td>1</td><td>28610.00</td><td>29862.00</td><td>4.38</td><td>0.11</td><td>28610.00</td><td>0</td><td>371.02</td></tr><tr><td rowspan="3" colspan="5"></td><td>Max</td><td>13.26</td><td>0.21</td><td>Max</td><td>0.00</td><td>602.65</td></tr><tr><td>Min</td><td>0.00</td><td>0.05</td><td>Min</td><td>0.00</td><td>0.03</td></tr><tr><td>Avg</td><td>4.62</td><td>0.11</td><td>Avg</td><td>0.00</td><td>152.34</td></tr></table>

**Fast and RRLS have different purposes, and perform accordingly on these large instances. The method Fast is normally able to provide reasonably good solutions in a very short time, and could be useful within a purely online system. On the given instances the method is able to provide solutions with an average gap below 4.5%, with a computation time of maximum 5 seconds (around 1.2 second on average). Fast even improves the best known result for one particular instance. However, it has to be observed that it performs poorly on a few instances, with a gap approaching 40% for one instance. The method seems to have the worst performance on the instances where many drones are available and when the drone speed is high (in both cases the optimal solution is intuitively likely to diverge from the giant TSP substantially). In** **conclusion, the method is extremely fast, but does not always show robustness in its results.**

Table 5 Results of the algorithms on the TSPLIB instance berlin52 from [18].

<table><tr><td colspan="4">Instance settings</td><td rowspan="2">Best known</td><td colspan="3">Fast</td><td colspan="3">RRLS</td></tr><tr><td>el</td><td>sp</td><td>#</td><td>dp</td><td>cost</td><td>gap %</td><td>sec</td><td>cost</td><td>gap %</td><td>sec</td></tr><tr><td>80</td><td>2</td><td>1</td><td>1</td><td>6386.48</td><td>6640.00</td><td>3.97</td><td>0.15</td><td>6386.48</td><td>0</td><td>230.89</td></tr><tr><td>80</td><td>2</td><td>1</td><td>2</td><td>7830.00</td><td>7960.00</td><td>1.66</td><td>0.13</td><td>7830.00</td><td>0</td><td>0.19</td></tr><tr><td>0</td><td>2</td><td>1</td><td>1</td><td>9675.00</td><td>9675.00</td><td>0.00</td><td>0.04</td><td>9675.00</td><td>0</td><td>0.06</td></tr><tr><td>20</td><td>2</td><td>1</td><td>1</td><td>9350.00</td><td>9385.00</td><td>0.37</td><td>0.06</td><td>9350.00</td><td>0</td><td>887.51</td></tr><tr><td>40</td><td>2</td><td>1</td><td>1</td><td>8300.00</td><td>8635.00</td><td>4.04</td><td>0.11</td><td>8300.00</td><td>0</td><td>0.15</td></tr><tr><td>60</td><td>2</td><td>1</td><td>1</td><td>7410.00</td><td>7525.00</td><td>1.55</td><td>0.09</td><td>7410.00</td><td>0</td><td>845.44</td></tr><tr><td>100</td><td>2</td><td>1</td><td>1</td><td>6192.00</td><td>6285.40</td><td>1.51</td><td>0.32</td><td>6192.00</td><td>0</td><td>663.25</td></tr><tr><td>80</td><td>1</td><td>1</td><td>1</td><td>7450.00</td><td>7550.00</td><td>1.34</td><td>0.14</td><td>7450.00</td><td>0</td><td>800.35</td></tr><tr><td>80</td><td>3</td><td>1</td><td>1</td><td>5656.56</td><td>6060.00</td><td>7.13</td><td>0.21</td><td>5656.56</td><td>0</td><td>289.39</td></tr><tr><td>80</td><td>4</td><td>1</td><td>1</td><td>5290.65</td><td>5730.00</td><td>8.30</td><td>0.09</td><td>5290.65</td><td>0</td><td>36.74</td></tr><tr><td>80</td><td>5</td><td>1</td><td>1</td><td>5190.00</td><td>5730.00</td><td>10.40</td><td>0.14</td><td>5190.00</td><td>0</td><td>745.47</td></tr><tr><td>80</td><td>2</td><td>2</td><td>1</td><td>5299.81</td><td>5730.00</td><td>8.12</td><td>0.13</td><td>5290.65</td><td>-0.17</td><td>42.33</td></tr><tr><td>80</td><td>2</td><td>3</td><td>1</td><td>5190.00</td><td>5730.00</td><td>10.40</td><td>0.09</td><td>5190.00</td><td>0</td><td>96.99</td></tr><tr><td>80</td><td>2</td><td>4</td><td>1</td><td>5190.00</td><td>5730.00</td><td>10.40</td><td>0.10</td><td>5190.00</td><td>0</td><td>100.56</td></tr><tr><td>80</td><td>2</td><td>5</td><td>1</td><td>5190.00</td><td>5730.00</td><td>10.40</td><td>0.10</td><td>5190.00</td><td>0</td><td>348.83</td></tr><tr><td rowspan="3" colspan="5"></td><td>Max</td><td>10.40</td><td>0.32</td><td>Max</td><td>0.00</td><td>887.51</td></tr><tr><td>Min</td><td>0.00</td><td>0.04</td><td>Min</td><td>-0.17</td><td>0.06</td></tr><tr><td>Avg</td><td>5.31</td><td>0.13</td><td>Avg</td><td>-0.01</td><td>339.21</td></tr></table>

Table 6 Results of the algorithms on the TSPLIB instance eil101 from [18].

<table><tr><td colspan="4">Instance settings</td><td rowspan="2">Best known</td><td colspan="3">Fast</td><td colspan="3">RRLS</td></tr><tr><td>el</td><td>sp</td><td>#</td><td>dp</td><td>cost</td><td>gap %</td><td>sec</td><td>cost</td><td>gap %</td><td>sec</td></tr><tr><td>80</td><td>2</td><td>1</td><td>1</td><td>564.00</td><td>585.00</td><td>3.72</td><td>0.51</td><td>564.00</td><td>0</td><td>634.96</td></tr><tr><td>80</td><td>2</td><td>1</td><td>2</td><td>650.00</td><td>665.67</td><td>2.41</td><td>1.94</td><td>648.98</td><td>-0.16</td><td>40.79</td></tr><tr><td>0</td><td>2</td><td>1</td><td>1</td><td>819.00</td><td>819.00</td><td>0.00</td><td>0.19</td><td>819.00</td><td>0</td><td>0.21</td></tr><tr><td>20</td><td>2</td><td>1</td><td>1</td><td>738.00</td><td>767.00</td><td>3.93</td><td>0.29</td><td>736.00</td><td>-0.27</td><td>1.03</td></tr><tr><td>40</td><td>2</td><td>1</td><td>1</td><td>646.00</td><td>701.00</td><td>8.51</td><td>0.39</td><td>646.00</td><td>0</td><td>129.86</td></tr><tr><td>60</td><td>2</td><td>1</td><td>1</td><td>578.00</td><td>599.00</td><td>3.63</td><td>0.65</td><td>578.00</td><td>0</td><td>123.81</td></tr><tr><td>100</td><td>2</td><td>1</td><td>1</td><td>561.41</td><td>575.00</td><td>2.42</td><td>0.40</td><td>560.00</td><td>-0.25</td><td>166.95</td></tr><tr><td>80</td><td>1</td><td>1</td><td>1</td><td>650.00</td><td>667.00</td><td>2.62</td><td>0.45</td><td>650.00</td><td>0</td><td>255.72</td></tr><tr><td>80</td><td>3</td><td>1</td><td>1</td><td>504.00</td><td>530.50</td><td>5.26</td><td>0.43</td><td>504.00</td><td>0</td><td>107.39</td></tr><tr><td>80</td><td>4</td><td>1</td><td>1</td><td>456.00</td><td>495.00</td><td>8.55</td><td>0.44</td><td>456.00</td><td>0</td><td>1100.28</td></tr><tr><td>80</td><td>5</td><td>1</td><td>1</td><td>420.83</td><td>471.00</td><td>11.92</td><td>2.43</td><td>421.00</td><td>0.04</td><td>31.48</td></tr><tr><td>80</td><td>2</td><td>2</td><td>1</td><td>456.00</td><td>495.00</td><td>8.55</td><td>0.49</td><td>456.00</td><td>0</td><td>780.24</td></tr><tr><td>80</td><td>2</td><td>3</td><td>1</td><td>395.00</td><td>449.00</td><td>13.67</td><td>0.90</td><td>395.00</td><td>0</td><td>1154.43</td></tr><tr><td>80</td><td>2</td><td>4</td><td>1</td><td>346.68</td><td>445.00</td><td>28.36</td><td>0.38</td><td>346.00</td><td>-0.20</td><td>1113.50</td></tr><tr><td>80</td><td>2</td><td>5</td><td>1</td><td>319.74</td><td>445.00</td><td>39.18</td><td>0.39</td><td>318.00</td><td>-0.54</td><td>420.26</td></tr><tr><td rowspan="3" colspan="5"></td><td>Max</td><td>39.18</td><td>2.43</td><td>Max</td><td>0.04</td><td>1154.43</td></tr><tr><td>Min</td><td>0.00</td><td>0.19</td><td>Min</td><td>-0.54</td><td>0.21</td></tr><tr><td>Avg</td><td>9.52</td><td>0.69</td><td>Avg</td><td>-0.09</td><td>404.06</td></tr></table>

**The second method, RRLS, is intrinsically slower to converge than Fast and the algorithms presented in [18]. Therefore, a maximum computation time of 1200 seconds for each RRLS run is allowed, with the best solution found however on average within 405 seconds. This is longer than the 300 seconds allowed in [18] (on a slightly slower computer), but still acceptable even in a quasi-online system. In the allowed time, RRLS is able to provide solutions** **of quality comparable to those of [18], improving the best known solution for 28 of the 90 instances considered (and being worse in 11 cases). Note that a higher concentration of improvements is present for the larger instances. The results are also robust, with a gap always below 0.72%. It is finally not possible to clearly identify characteristics of the instances (blocks of the tables) on which the new algorithm performs better, since the improvements appear to be spread around each tables almost evenly.**

Table 7 Results of the algorithms on the TSPLIB instance gr120 from [18].

<table><tr><td colspan="4">Instance settings</td><td rowspan="2">Best known</td><td colspan="3">Fast</td><td colspan="3">RRLS</td></tr><tr><td>el</td><td>sp</td><td>#</td><td>dp</td><td>cost</td><td>gap %</td><td>sec</td><td>cost</td><td>gap %</td><td>sec</td></tr><tr><td>80</td><td>2</td><td>1</td><td>1</td><td>1414.00</td><td>1471.00</td><td>4.03</td><td>2.97</td><td>1420.76</td><td>0.48</td><td>451.92</td></tr><tr><td>80</td><td>2</td><td>1</td><td>2</td><td>1730.00</td><td>1752.00</td><td>1.27</td><td>1.22</td><td>1726.00</td><td>-0.23</td><td>568.94</td></tr><tr><td>0</td><td>2</td><td>1</td><td>1</td><td>2006.00</td><td>2006.00</td><td>0.00</td><td>0.31</td><td>2006.00</td><td>0</td><td>0.27</td></tr><tr><td>20</td><td>2</td><td>1</td><td>1</td><td>1736.00</td><td>1766.00</td><td>1.73</td><td>0.39</td><td>1736.00</td><td>0</td><td>5.69</td></tr><tr><td>40</td><td>2</td><td>1</td><td>1</td><td>1624.00</td><td>1680.00</td><td>3.45</td><td>0.57</td><td>1624.00</td><td>0</td><td>495.17</td></tr><tr><td>60</td><td>2</td><td>1</td><td>1</td><td>1494.00</td><td>1559.94</td><td>4.41</td><td>1.36</td><td>1494.00</td><td>0</td><td>74.57</td></tr><tr><td>100</td><td>2</td><td>1</td><td>1</td><td>1414.80</td><td>1461.00</td><td>3.27</td><td>0.93</td><td>1416.00</td><td>0.08</td><td>396.04</td></tr><tr><td>80</td><td>1</td><td>1</td><td>1</td><td>1592.00</td><td>1637.00</td><td>2.83</td><td>1.48</td><td>1592.00</td><td>0</td><td>1091.80</td></tr><tr><td>80</td><td>3</td><td>1</td><td>1</td><td>1289.27</td><td>1346.24</td><td>4.42</td><td>0.96</td><td>1291.00</td><td>0.13</td><td>136.85</td></tr><tr><td>80</td><td>4</td><td>1</td><td>1</td><td>1189.71</td><td>1251.00</td><td>5.15</td><td>2.07</td><td>1192.00</td><td>0.19</td><td>316.62</td></tr><tr><td>80</td><td>5</td><td>1</td><td>1</td><td>1112.00</td><td>1171.00</td><td>5.31</td><td>4.50</td><td>1114.00</td><td>0.18</td><td>257.38</td></tr><tr><td>80</td><td>2</td><td>2</td><td>1</td><td>1188.51</td><td>1251.00</td><td>5.26</td><td>2.29</td><td>1197.00</td><td>0.71</td><td>878.42</td></tr><tr><td>80</td><td>2</td><td>3</td><td>1</td><td>1044.65</td><td>1102.58</td><td>5.55</td><td>3.14</td><td>1050.00</td><td>0.51</td><td>1183.20</td></tr><tr><td>80</td><td>2</td><td>4</td><td>1</td><td>946.04</td><td>997.00</td><td>5.39</td><td>1.46</td><td>946.04</td><td>0</td><td>130.27</td></tr><tr><td>80</td><td>2</td><td>5</td><td>1</td><td>880.00</td><td>929.17</td><td>5.59</td><td>3.27</td><td>881.00</td><td>0.11</td><td>130.81</td></tr><tr><td rowspan="3" colspan="5"></td><td>Max</td><td>5.59</td><td>4.50</td><td>Max</td><td>0.71</td><td>1183.20</td></tr><tr><td>Min</td><td>0.00</td><td>0.31</td><td>Min</td><td>-0.23</td><td>0.27</td></tr><tr><td>Avg</td><td>3.84</td><td>1.79</td><td>Avg</td><td>0.15</td><td>407.86</td></tr></table>

Table 8 Results of the algorithms on the TSPLIB instance pr152 from [18].

<table><tr><td colspan="4">Instance settings</td><td rowspan="2">Best known</td><td colspan="3">Fast</td><td colspan="3">RRLS</td></tr><tr><td>el</td><td>sp</td><td>#</td><td>dp</td><td>cost</td><td>gap %</td><td>sec</td><td>cost</td><td>gap %</td><td>sec</td></tr><tr><td>80</td><td>2</td><td>1</td><td>1</td><td>76008.00</td><td>76820.00</td><td>1.07</td><td>1.55</td><td>76008.00</td><td>0</td><td>728.20</td></tr><tr><td>80</td><td>2</td><td>1</td><td>2</td><td>76556.00</td><td>77464.00</td><td>1.19</td><td>1.09</td><td>76556.00</td><td>0</td><td>452.24</td></tr><tr><td>0</td><td>2</td><td>1</td><td>1</td><td>86596.00</td><td>86596.00</td><td>0.00</td><td>0.83</td><td>86596.00</td><td>0</td><td>0.79</td></tr><tr><td>20</td><td>2</td><td>1</td><td>1</td><td>82504.00</td><td>82604.00</td><td>0.12</td><td>1.67</td><td>82504.00</td><td>0</td><td>7.05</td></tr><tr><td>40</td><td>2</td><td>1</td><td>1</td><td>77372.00</td><td>79088.00</td><td>2.22</td><td>1.45</td><td>77316.00</td><td>-0.07</td><td>105.52</td></tr><tr><td>60</td><td>2</td><td>1</td><td>1</td><td>76786.00</td><td>77678.00</td><td>1.16</td><td>2.86</td><td>76786.00</td><td>0</td><td>548.58</td></tr><tr><td>100</td><td>2</td><td>1</td><td>1</td><td>74468.00</td><td>74568.00</td><td>0.13</td><td>3.20</td><td>74302.00</td><td>-0.22</td><td>226.34</td></tr><tr><td>80</td><td>1</td><td>1</td><td>1</td><td>80164.00</td><td>80668.00</td><td>0.63</td><td>1.19</td><td>79952.00</td><td>-0.26</td><td>547.98</td></tr><tr><td>80</td><td>3</td><td>1</td><td>1</td><td>72936.00</td><td>73972.00</td><td>1.42</td><td>2.79</td><td>72936.00</td><td>0</td><td>113.24</td></tr><tr><td>80</td><td>4</td><td>1</td><td>1</td><td>70412.00</td><td>71286.65</td><td>1.24</td><td>5.08</td><td>70328.00</td><td>-0.12</td><td>846.80</td></tr><tr><td>80</td><td>5</td><td>1</td><td>1</td><td>67798.00</td><td>68812.00</td><td>1.50</td><td>1.17</td><td>67798.00</td><td>0</td><td>1158.65</td></tr><tr><td>80</td><td>2</td><td>2</td><td>1</td><td>70244.00</td><td>71316.90</td><td>1.53</td><td>2.22</td><td>70405.45</td><td>0.23</td><td>293.78</td></tr><tr><td>80</td><td>2</td><td>3</td><td>1</td><td>65062.10</td><td>66714.02</td><td>2.54</td><td>1.62</td><td>64720.30</td><td>-0.53</td><td>729.20</td></tr><tr><td>80</td><td>2</td><td>4</td><td>1</td><td>60027.40</td><td>63040.80</td><td>5.02</td><td>3.01</td><td>59772.00</td><td>-0.43</td><td>1172.29</td></tr><tr><td>80</td><td>2</td><td>5</td><td>1</td><td>56336.10</td><td>60599.05</td><td>7.57</td><td>3.99</td><td>56262.00</td><td>-0.13</td><td>1011.87</td></tr><tr><td rowspan="3" colspan="5"></td><td>Max</td><td>7.57</td><td>5.08</td><td>Max</td><td>0.23</td><td>1172.29</td></tr><tr><td>Min</td><td>0.00</td><td>0.83</td><td>Min</td><td>-0.53</td><td>0.79</td></tr><tr><td>Avg</td><td>1.82</td><td>2.25</td><td>Avg</td><td>-0.10</td><td>529.50</td></tr></table>

Table 9 Results of the algorithms on the TSPLIB instance gr229 from [18].

<table><tr><td colspan="4">Instance settings</td><td rowspan="2">Best known</td><td colspan="3">Fast</td><td colspan="3">RRLS</td></tr><tr><td>el</td><td>sp</td><td>#</td><td>dp</td><td>cost</td><td>gap %</td><td>sec</td><td>cost</td><td>gap %</td><td>sec</td></tr><tr><td>80</td><td>2</td><td>1</td><td>1</td><td>1794.84</td><td>1816.62</td><td>1.21</td><td>1.72</td><td>1785.86</td><td>-0.50</td><td>171.38</td></tr><tr><td>80</td><td>2</td><td>1</td><td>2</td><td>1913.74</td><td>1929.32</td><td>0.81</td><td>2.97</td><td>1911.58</td><td>-0.11</td><td>7.77</td></tr><tr><td>0</td><td>2</td><td>1</td><td>1</td><td>2020.16</td><td>2017.24</td><td>-0.14</td><td>0.73</td><td>2017.24</td><td>-0.14</td><td>0.63</td></tr><tr><td>20</td><td>2</td><td>1</td><td>1</td><td>1862.76</td><td>1889.14</td><td>1.42</td><td>1.96</td><td>1860.14</td><td>-0.14</td><td>1002.19</td></tr><tr><td>40</td><td>2</td><td>1</td><td>1</td><td>1828.02</td><td>1874.88</td><td>2.56</td><td>1.47</td><td>1827.02</td><td>-0.05</td><td>1144.65</td></tr><tr><td>60</td><td>2</td><td>1</td><td>1</td><td>1807.50</td><td>1831.66</td><td>1.34</td><td>3.33</td><td>1797.37</td><td>-0.56</td><td>955.35</td></tr><tr><td>100</td><td>2</td><td>1</td><td>1</td><td>1498.05</td><td>1498.01</td><td>0.00</td><td>3.44</td><td>1496.29</td><td>-0.12</td><td>139.43</td></tr><tr><td>80</td><td>1</td><td>1</td><td>1</td><td>1865.00</td><td>1893.90</td><td>1.55</td><td>1.68</td><td>1863.12</td><td>-0.10</td><td>734.09</td></tr><tr><td>80</td><td>3</td><td>1</td><td>1</td><td>1735.16</td><td>1756.24</td><td>1.21</td><td>1.34</td><td>1725.45</td><td>-0.56</td><td>816.30</td></tr><tr><td>80</td><td>4</td><td>1</td><td>1</td><td>1679.33</td><td>1702.09</td><td>1.36</td><td>2.36</td><td>1675.82</td><td>-0.21</td><td>988.52</td></tr><tr><td>80</td><td>5</td><td>1</td><td>1</td><td>1642.04</td><td>1658.02</td><td>0.97</td><td>1.36</td><td>1629.38</td><td>-0.77</td><td>687.03</td></tr><tr><td>80</td><td>2</td><td>2</td><td>1</td><td>1686.75</td><td>1701.18</td><td>0.86</td><td>2.78</td><td>1673.72</td><td>-0.77</td><td>699.95</td></tr><tr><td>80</td><td>2</td><td>3</td><td>1</td><td>1603.90</td><td>1621.82</td><td>1.12</td><td>3.58</td><td>1592.52</td><td>-0.71</td><td>430.77</td></tr><tr><td>80</td><td>2</td><td>4</td><td>1</td><td>1518.62</td><td>1560.61</td><td>2.77</td><td>1.80</td><td>1526.92</td><td>0.55</td><td>718.71</td></tr><tr><td>80</td><td>2</td><td>5</td><td>1</td><td>1483.68</td><td>1509.24</td><td>1.72</td><td>2.31</td><td>1467.76</td><td>-1.07</td><td>381.18</td></tr><tr><td rowspan="3" colspan="5"></td><td>Max</td><td>2.77</td><td>3.58</td><td>Max</td><td>0.55</td><td>1144.65</td></tr><tr><td>Min</td><td>-0.14</td><td>0.73</td><td>Min</td><td>-1.07</td><td>0.63</td></tr><tr><td>Avg</td><td>1.25</td><td>2.19</td><td>Avg</td><td>-0.35</td><td>591.86</td></tr></table>

**A general consideration about the results on these TSPLIB-derived instances is that properly optimized solutions appear to have very similar costs, denoting a search space landscape with several quasi-optimal solutions. This can be devised by the small differences in the cost of the solutions proposed by the different heuristics for several of the instances.**

## 6 Conclusions

**New methods mixing concepts from integer linear programming with heuristic ideas have been proposed for the Parallel Drone Scheduling Traveling Salesman Problem, a combinatorial optimisation problem arising when parcel delivery is carried out by an heterogeneous fleet of vehicles composed of one truck and a set of drones.**

**The new matheuristic methods have proven effective on the benchmark instances available from the literature. In particular, it is shown that high quality (often optimal) solutions can be retrieved for small/medium size instances very quickly. When considering larger instances, the most promising methods among those presented are able to provide competitive results with respect to state-of-the-art methods in a reasonable time. In particular, improved heuristic solutions are provided for 28 of the 90 instances of the most challenging benchmark currently available in the literature.**

**Acknowledgements The authors are very grateful to Ra¨ıssa G. Mbiadou Saleu and Dominique Feillet for the suggestions and the useful discussions.**

## References

1. Alibaba’s drones deliver packages to islands. [http://www.chinadaily.com.cn/business/2017-11/07/content\_34230012.htm](http://www.chinadaily.com.cn/business/2017-11/07/content_34230012.htm). Accessed: 2019-03-22

2. Amazon PrimeAir. [https://www.amazon.com/Amazon-Prime-Air/b?ie=UTF8&node=8037720011](https://www.amazon.com/Amazon-Prime-Air/b?ie=UTF8&node=8037720011). Accessed: 2019-03-22

3. Drone delivery: DHL ‘Parcelcopter’ flies to German isle. [https://www.reuters.com/article/us-deutsche-post-drones/drone-delivery-dhl-](https://www.reuters.com/article/us-deutsche-post-drones/drone-delivery-dhl-)parcelcopter-flies-to-german-isle-idUSKCN0HJ1ED20140924. Accessed: 2019-03-22

4. JD.com to build 150 drone launch facilities in China by 2020. [https://aircargoworld.com/allposts/jd-com-to-build-150-drone-launch-](https://aircargoworld.com/allposts/jd-com-to-build-150-drone-launch-)facilities-in-china-by-2020-video/. Accessed: 2019-03-22

5. JD.com a Drone Delivery Program Takes Flight in Rural China. [http://corporate.jd.com/whatIsNewDetail?contentCode=6IhXLeeSAFLjLLlyuZatDA](http://corporate.jd.com/whatIsNewDetail?contentCode=6IhXLeeSAFLjLLlyuZatDA).Accessed: 2019-03-22

6. Parcelcopter: DHL’s drone. [https://discover.dhl.com/business/business-ethics/parcelcopter-drone-](https://discover.dhl.com/business/business-ethics/parcelcopter-drone-)technology. Accessed: 2019-03-22

7. Retail e-commerce sales worldwide from 2014 to 2021. [https://www.statista.com/statistics/379046/worldwide-retail-e-commerce-](https://www.statista.com/statistics/379046/worldwide-retail-e-commerce-)sales/. Accessed: 2019-04-30

8. Uber Ambitiously Eyes 2021 for Food-Delivery Drones Launch. [https://www.wsj.com/articles/uber-ambitiously-eyes-2021-for-food-delivery-](https://www.wsj.com/articles/uber-ambitiously-eyes-%202021-for-food-delivery-)drones-launch-1540163425. Accessed: 2019-04-30

9. Wing - transforming the way goods are transported. [https://x.company/projects/wing/](https://x.company/projects/wing/). Accessed: 2019-03-22 10. Ford, L., Fulkerson, D.: Flows in Networks. Princeton University Press (1962)

11. Ghazzai, H., Kadri, A., Ghorbel, M.B., Menouar, H.: Optimal sequential and parallel uav scheduling for multi-event applications. In: 2018 IEEE 87th Vehicular Technology Conference (VTC Spring), pp. 1–6. IEEE (2018)

12. Graham, R., Lawler, E., Lenstra, J., Rinnooy Kan, A.: Optimization and approximation in deterministic sequencing and scheduling: a survey. Annals of Discrete Mathematics 5, 287–326 (1979)

13. Gurobi Optimization LLC: Gurobi optimizer reference manual. [http://www.gurobi.com](http://www.gurobi.com). Accessed: 2019-03-22

14. Ham, A.M.: Integrated scheduling of m-truck, m-drone, and m-depot constrained by time-window, drop-pickup, and m-visit using constraint programming. Transportation Research Part C: Emerging Technologies 91, 1–14 (2018)

15. Helsgaun, K.: An effective implementation of the lin-kernighan traveling salesman heuristic. European Journal of Operational Research 126(1), 106–130 (2000)

16. Joerss, M., Schroeder, J., Neuhaus, F., Klink, C., Mann, F.: Parcel delivery - the future of last mile. Travel, Transport and Logistics (2016)

17. Johnson, D., McGeoch, L.: The traveling salesman problem: A case study in local optimization. In: E. Aarts, J. Lenstra (eds.) Local Search in Combinatorial Optimization, pp. 215–310. John Wiley & Sons, New York, NY, USA (1997)

18. Mbiadou Saleu, R.G., Deroussi, L., Feillet, D., Grangeon, N., Quilliot, A.: An iterative two-step heuristic for the parallel drone scheduling traveling salesman problem. Networks 72(4), 459–474 (2018)

19. Miller, C., Tucker, A., Zemlin, R.: Integer programming formulations and traveling salesman problems. Journal of Association for Computing Machinery (7), 326–329 (1960)

20. Murray, C.C., Chu, A.G.: The flying sidekick traveling salesman problem: Optimization of drone-assisted parcel delivery. Transportation Research Part C: Emerging Technologies 54, 86–109 (2015)

21. Otto, A., Agatz, N., Campbell, J., Golden, B., Pesch, E.: Optimization approaches for civil applications of unmanned aerial vehicles (uavs) or aerial drones: A survey. Networks 72(4), 411–458 (2018)

22. Passmark Software: CPU Benchmarks. [https://www.cpubenchmark.net](https://www.cpubenchmark.net). Accessed: 2019-03-22 23. Reinelt, G.: TSPLIB – A Traveling Salesman Problem Library. ORSA Journal on Computing 3(4), 376–384 (1991)

24. Tavana, M., Khalili-Damghani, K., Santos-Arteaga, F.J., Zandi, M.H.: Drone shipping versus truck delivery in a cross-docking system with multiple fleets and products. Expert systems with applications 72, 93–107 (2017)

25. Torabbeigi, M., Lim, G.J., Kim, S.J.: Drone delivery schedule optimization considering the reliability of drones. In: 2018 International Conference on Unmanned Aircraft Systems (ICUAS), pp. 1048–1053. IEEE (2018)

26. Ulmer, M.W., Thomas, B.W.: Same-day delivery with heterogeneous fleets of drones and vehicles. Networks 72(4), 475–505 (2018)

27. Wolleswinkel, R., Lukic, V., Jap, W., Chan, R., Govers, J., Banerjee, S.: An onslaught of new rivals in parcel and express. Travel, Transport and Logistics (2018)