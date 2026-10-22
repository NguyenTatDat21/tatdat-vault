## Journal Pre-proof

Large Neighborhood and Hybrid Genetic Search for Inventory Routing Problems

Jingyi Zhao, Claudia Archetti, Tuan Anh Pham, Thibaut Vidal

PII: S0377-2217(25)00930-0 DOI: [https://doi.org/10.1016/j.ejor.2025.11.021](https://doi.org/10.1016/j.ejor.2025.11.021)Reference: EOR 19873

![](images/page_0_chart_4.jpg)

To appear in: European Journal of Operational Research

Received date: 27 May 2025

Accepted date: 14 November 2025

Please cite this article as: Jingyi Zhao, Claudia Archetti, Tuan Anh Pham, Thibaut Vidal, Large Neighborhood and Hybrid Genetic Search for Inventory Routing Problems, European Journal of Operational Research (2025), doi: [https://doi.org/10.1016/j.ejor.2025.11.021](https://doi.org/10.1016/j.ejor.2025.11.021)

This is a PDF of an article that has undergone enhancements after acceptance, such as the addition of a cover page and metadata, and formatting for readability. This version will undergo additional copyediting, typesetting and review before it is published in its final form. As such, this version is no longer the Accepted Manuscript, but it is not yet the definitive Version of Record; we are providing this early version to give early visibility of the article. Please note that Elsevier’s sharing policy for the Published Journal Article applies to this version, see: [https://www.elsevier.com/about/policies-and-standards/sharing#4-published-journal-article](https://www.elsevier.com/about/policies-and-standards/sharing#4-published-journal-article). Please also note that, during the production process, errors may be discovered which could affect the content, and all legal disclaimers that apply to the journal pertain.

© 2025 Published by Elsevier B.V.

## highlights

• Dynamic programming–based delivery-schedule improvement operator for the IRP.

• Jointly optimize inventory and distribution operations over multiple days.

• Embed the operator in a hybrid genetic search to optimize replenishment decisions.

• Extend the IRP to a stock-out-allowed model with penalized unmet demand.

• Achieve 365 new best solutions on 1,040 benchmarks and 191 on new large instances.

# Large Neighborhood and Hybrid Genetic Search for Inventory Routing Problems

Jingyi Zhao\*

Shenzhen Research Institute of Big Data, Shenzhen 518172, China, jingyi.z@u.nus.edu

Claudia Archetti

Department of Economics and Management, University of Brescia, Italy, claudia.archetti@unibs.it

Tuan Anh Pham

Faculty of DS&AI, College of Technology, National Economics University, ptanh@neu.edu.vn

Thibaut Vidal

CIRRELT & SCALE-AI Chair in Data-Driven Supply Chains, Department of Mathematical and Industrial Engineering, Polytechnique Montreal, Canada, thibaut.vidal@polymtl.ca

The inventory routing problem (IRP) focuses on jointly optimizing inventory and distribution operations from a supplier to retailers over multiple days. Compared to other problems from the vehicle routing family, the interrelations between inventory and routing decisions render IRP optimization more challenging and call for advanced solution techniques. A few studies have focused on developing large neighborhood search approaches for this class of problems, but this remains a research area with vast possibilities due to the challenges related to the integration of inventory and routing decisions. In this study, we advance this research area by developing a new large neighborhood search operator tailored for the IRP. Specifically, the operator optimally removes and reinserts all visits to a specific retailer while minimizing routing and inventory costs. We propose an efficient tailored dynamic programming algorithm that exploits preprocessing and acceleration strategies. The operator is used to build an effective local search routine, and included in a state of-the-art routing algorithm, i.e., Hybrid Genetic Search. Through extensive computational experiments, we demonstrate that the resulting heuristic algorithm leads to solutions of unmatched quality up to this date, especially on large-scale benchmark instances.

Key words : Inventory Routing Problem; Hybrid Genetic Search Algorithm; Large Neighborhood Search; Dynamic Programming.

## 1. Introduction

The use of large neighborhood search (LNS) techniques has permitted significant progress in the solution of various vehicle routing problems (VRPs) (see, e.g., Christiaens and Vanden Berghe 2020, Pacheco et al. 2023) and combinatorial optimization (CO) problems in general (Hendel 2022). Especially when multiple decisions are interrelated, classical local search neighborhoods often do not allow an efficient search space exploration, while larger neighborhoods can be instrumental in exploring structurally different solutions.

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">\*Corresponding author</span></small>

The Inventory Routing Problem (IRP), in particular, is a prototypical example of a problem involving multiple interrelated decisions. In its canonical form, the IRP requires jointly optimizing inventory and delivery routes from a supplier to geographically dispersed retailers over a planning horizon measured in days. This involves a complex set of decisions that include the daily selection of retailers receiving visits, their delivery quantities, the assignment of vehicles to these visits, and their ordering. Despite a few recent and promising works on the topic (see, e.g., Chitsaz et al. 2019, Diniz et al. 2020, Archetti et al. 2021, Skålnes et al. 2023), applications of LNS for this problem remain few and far. Many LNS designed for IRP fundamentally rely on mixed integer programming (see, e.g., Bouvier et al. 2024a), which can become time-consuming and not permit many iterations. For this reason, though extensive progress has been made on solution methods over the past decades, judging from the average gap and standard deviation of state-of-the-art methods, significant improvements are still possible on medium and larger-scale instances such as the ones introduced in Skålnes et al. (2024).

In this study, we contribute to advancing efficient large-neighborhood-based search techniques for the IRP. Our contribution is fourfold.

1. We propose a new large neighborhood operator that removes and reinserts all visits to a specific retailer while minimizing routing and inventory costs. While this may evoke the concepts used in ruin-and-recreate methods (Ropke and Pisinger 2006), the way we apply this strategy is fundamentally different. We demonstrate that, after preprocessing, the reinsertion can be done optimally using efficient dynamic programming and acceleration strategies specifically tailored to this case. Moreover, the speed of our method permits us to explore this large neighborhood fully for all retailers in random order until a local minimum is reached.

2. We integrate this LNS operator into the hybrid genetic search (HGS) of (Vidal et al. 2012, Vidal 2022), extending this method to solve IRPs. Specifically, the new operator replaces the neighborhood search operator originally used in Vidal et al. (2012) to choose the allowed visit-day combinations by inspection in the context of multi-period VRP. This is the first time an operator has been designed for an IRP that optimizes replenishment decisions across the entire planning horizon.

3. We extend the IRP to the Stock-Out Allowed (SOA) model by introducing a penalty term for stock-out. This variant has been rarely considered, but it is especially relevant when applying IRP solution techniques in a dynamic environment, e.g., as studied in (Greif et al. 2024), as this often requires the ability to evaluate infeasible solutions in some scenarios.

4. We conduct an extensive computational campaign to evaluate the neighborhood search efficiency and compare the adapted HGS’s performance with other state-of-the-art IRP algorithms. Most notably, the resulting method identifies 187 new best solutions out of 800 small data instances and 178 new best solutions in 240 large instances. Even more remarkable is its performance when applied to the new challenging IRP dataset proposed in Skålnes et al. (2024), where it finds 191 new benchmark solutions on 270 instances with a shorter average running time. These findings highlight the efficiency of the proposed enhanced HGS algorithm, thanks to the development of the new large neighborhood operator.

## 2. Related works

Large Neighborhood Search (LNS) is a fundamental component of heuristic algorithms and is regularly used in combinatorial optimization (CO), especially on large-scale problems of a size that defies exact algorithms. Broadly defined, a neighborhood search involves an iterative exploration of the solution space around an incumbent solution, i.e., a “neighborhood”, to find improved solutions. Typically, the search starts from an initial solution, and it ite by replacing the incumbent solution with any superior solution found (i.e., accepting ove” ), with mechanisms in place to allow controlled deterioration of the solution quality to escape local optima. The qualifiers “local” and “large” distinguish the scale of the neighborhood examined during each iteration. When the number of possible moves is polynomial, enabling efficient enumeration, the process is generally termed Local Search (LS). Conversely, when each iteration involves the exploration of a neighborhood with an exponential number of solutions, we typically refer to the process as an LNS. The neighborhood exploration methods might be different; they may be based on sampling or on efficient (possibly polynomial-time) search techniques tailored to the problem, often relying on combinatorial subproblems solvable in polynomial time.

Ahuja et al. (2002) reviews various large neighborhood search techniques, categorizing them into three main categories. The first category, variable-depth methods, employs heuristics to explore increasingly large (higher-order) neighborhoods. The heuristic of Lin and Kernighan (1973) is a seminal exampl as effectively harnesses pruning techniques to explore many solutions obtained by replacing a variable number of edges. Applications of this technique to various CO problems are demonstrated in Applegate et al. (2003) and Hendel (2022). The second category includes network flow-based improvement algorithms, which rely on solving network flow subproblems to explore large neighborhoods. Ejection chains (Thompson and Psaraftis 1993, Vidal 2017) and assignment-based neighborhoods (Toth and Tramontani 2008, Capua et al. 2018) are notable examples, leveraging shortest path and assignment problems to explore an exponential subset of solutions in polynomial time. The third category, neighborhoods induced by restrictions, exploits special cases of the original problem that admit polynomial-time solutions. For example, certain restrictions of the Traveling Salesman Problem (TSP) can be solved in polynomial time, leading to various classes of large neighborhoods that are broadly applicable to routing problems (Balas and Simonetti 2001, Pacheco et al. 2023). Additionally, complex CO problems can often be decomposed into several classes of decision variables, allowing for local searches on a subset of these variables. When combined with a move evaluation procedure that optimally determines the remaining variables, this approach can lead to effective searches in large neighborhoods (Vidal 2017, Toffolo et al. 2019). Collectively, these techniques have led to important breakthroughs for difficult problems.

The Inventory Routing Problem (IRP) is a foundational problem in supply chain optimization that has been extensively studied over the past decades, as highlighted in surveys by Andersson et al. (2010), Coelho et al. (2014) and Vidal et al. (2020). The IRP is a canonical problem designed to capture the challenges associated with the simultaneous optimization of both inventory replenishment strategies and routing plans, offering significant potential for cost reduction in supply chain operations.

The origins of the IRP trace back to the work of Bell et al. (1983), who introduced the concept for a gas delivery application. Their approach leveraged Lagrangian relaxation to decompose the problem across temporal and vehicle dimensio ater, Christiansen (1999) expanded the IRP’s application to maritime logistics, coining the term “inventory pickup and delivery problem.” Their approach used Dantzig-Wolfe decomposition and column-generation techniques. Further advancements in addressing the IRP were made by Carter et al. (1996) and Campbell and Savelsbergh (2004), who developed efficient heuristic methods by decomposing the IRP into an allocation problem and a routing problem.

Numerous metaheuristic strategies have since been proposed for the IRP. Examples include tabu search (Rusdiansyah and Tsao 2005), genetic algorithms (Abdelmaguid and Dessouky 2006), a greedy randomiz adaptive search procedure (Campbell and Savelsbergh 2004), adaptive large neighborhood search (LNS) (Coelho et al. 2012), and a variable neighborhood descent heuristic with stochastic neighborhood ordering (Alvarez et al. 2018), which combines routing-focused and joint routing-inventory operators. In addition, “matheuristics”, which integrate heuristic search with mathematical programming, have shown significant promise. Notable examples include hybrid methods by Archetti et al. (2012, 2017), Chitsaz et al. (2019), Archetti et al. (2021), Skålnes et al. (2023), Bouvier et al. (2024b) and Dinh et al. (2025). Among these, Skålnes et al. (2023) developed a matheuristic that is invoked on each primal solution identified by a branch-and-cut algorithm. Whenever the mathematical program discovers a new best upper bound, this method attempts to further improve it by applying mixed integer programming to a restricted problem, which involves removing and reinserting clusters of clients. This advanced approach successfully identified 741 best-known solutions out of 878 existing benchmark instances and proved the optimality of 458 of these solutions.

Research has also extended to various IRP variants. For instance, Gaur and Fisher (2004) addressed the periodic IRP, optimizing replenishment under cyclical demand, while other studies focused on cyclic (Gunawan et al. 2019, Vincent et al. 2021), multi-product (Ohmori and Yoshimoto 2021, Mahjoob et al. 2022), multi-depot (Guimarães et al. 2019), multi-attribute (Coelho et al. 2020), and bi-objective (Feng et al. 2025) IRPs. Strategic extensions integrating production decisions have also been explored (Adulyasak et al. 2014b) As noted by Andersson et al. (2010), early research predominantly relied on heuristics due to the problem’s complexity. However, subsequent works introduced exact algorithms, primarily branch-and-cut methods (Coelho and Laporte 2013a,b, Adulyasak et al. 2014a, Archetti et al. 2014, Coelho and Laporte 2014), with one notable exception employing branch-and-price (Desaulniers et al. 2016) Other contributions include VND methods (Larrain et al. 2017) and matheuristic framewor ( incent et al. 2025) that combine mathematical programming with metaheuristics to address larger-scale instances.

Despite their efficiency for small to medium-scale problems, these methods often struggle with scalability, particularly for instances involving more than 50 retailers or planning horizons exceeding three days. Addressing this gap, Skålnes et al. (2024) proposed challenging large-scale IRP instances to stimulate further research. Recently, Bouvier et al. (2024b) introduced a large neighborhood search procedure designed for very large IRPs involving an average of 30 commodities, 16 depots, and 600 retailers. However, the scale of the problems they address and the complexity of the underlying neighborhoods limit the procedure to only a handful of local search descents. This highlights the ongoing need for efficient neighborhood operators —both local and large— that can effectively tackle large-scale IRP instances.

## 3. Problem Statement

Our IRP is defined on a complete directed graph $\mathcal { G } = ( \mathcal { N } , \mathcal { A } )$ , where the node set $\mathcal { N }   =   \{ 0 , n   +   1 \}   \cup   \mathcal { N } ^ { \prime }$ includes the departure depot at node $0 ,$ the destination depot at node $n   +   1$ , and the retailer nodes $\mathcal { N } ^ { \prime }   =   \{ 1 , \ldots , n \}$ . The arc set $\mathcal { A }$ represents paths between nodes, with each arc $( i , j ) \in \mathcal { A }$ associated with a non-negative cost $c _ { i , j }$ . The planning horizon spans H days, denoted by $\mathcal { T }   =   \{ 1 , \ldots , H \}$ . Each retailer node $i \in \mathcal { N } ^ { \prime }$ has a per-day inventory holding cost $h _ { i } ,$ an initial inventory level $I _ { i } ^ { 0 }$ , and a maximum inventory level $U _ { i }$ . In the Stock-Out Allowed (SOA) model, $\rho h _ { i }$ represents the per-unit stock-out penalty for retailer $i ,$ with $\rho > 1$ . In contrast, in the No Stock-Out (NSO) model, the value of $\rho$ is set to infinity. Each day $t   \in   \mathcal { T } ,   d _ { 0 } ^ { t }$ units of product are made available at the supplier, and $d _ { i } ^ { t }$ units are consumed by retailer $i \in \mathcal { N } ^ { \prime }$ . A fleet K of K identical vehicles, each with capacity $Q ,$ provides the delivery service.

The IRP involves creating a distribution plan that minimizes the total cost. This plan specifies, for each day $t \in { \mathcal { T } } .$ , the delivery quantity to each retailer $i \in \mathcal { N } ^ { \prime }$ and the routes of vehicles for servicing the retailers on that day. The total cost encompasses the holding costs at both the supplier and retailers, the stock-out costs under the SOA model, and the transportation costs associated with the routes. In the IRP, allowing stock-outs is a realistic modeling approach that reflects many real-world scenarios. This no-backlogging setup is particularly suited to situations where unmet demand cannot or should not be fulfilled later. For example, in fast-moving consumer goods, customers typically turn to competitors if products are out of stock, meaning lost sales rather than deferred ones. Similarly, in retail, pharmaceuticals, or seasonal product delivery, stockouts represent immediate service failure, and backlogging is irrelevant or impractical. The penalty cost serves as a proxy for lost revenue, customer dissatisfaction, or contractual penalties, and it incentivizes timely and adequate deliveries. This modeling choice also simplifies the mathematical formulation by avoiding the complexity of backlog tracking while maintaining economic pressure to avoid stock-outs.

A mathematical formulation of the IRP under the SOA model is presented below, extending the formulation from Archetti et al. (2007) to nt for possible stock-outs. Let $I _ { i } ^ { t }$ represent the inventory level at retailer i at the end of the day t, and $B _ { i } ^ { t }$ the unsatisfied demand on that day. Also, $I _ { 0 } ^ { t }$ is the inventory level at the supplier at the end of the day t. Binary variable $z _ { i } ^ { k , t }$ is set to one if node $i \in \mathcal { N }$ is visited by vehicle $k \in \mathcal { K }$ on day $t \in \mathcal { T }$ . Continuous variable $q _ { i } ^ { k , t }$ denotes the quantity delivered to retailer $i \in \mathcal { N } ^ { \prime }$ on by vehicle $k .$ Binary variable $y _ { i , j } ^ { k , t }$ indicates whether vehicle k traverses arc $( i , j )   \in   \mathcal { A }$ on day t. Finally, $Q _ { i } ^ { k , t }$ is a continuous variable representing the load of vehicle k upon arrival at node reflecting the cumulative load at that point in the vehicle’s route. The objective is to minimize he total cost, which includes holding costs at the supplier $h _ { 0 } I _ { 0 } ^ { t }$ , holding costs at the retailers $\textstyle \sum _ { i \in \mathcal { N } ^ { \prime } } h _ { i } I _ { i } ^ { t }$ , penalty costs for stock-outs $\textstyle \sum _ { i \in \mathcal { N } ^ { \prime } } \rho h _ { i } B _ { i } ^ { t }$ , and transportation costs $\textstyle \sum _ { k \in \mathcal { K } } \sum _ { ( i , j ) \in \mathcal { A } } \widehat { c _ { i , j } } y _ { i , j } ^ { k , t }$ . The resulting mathematical formulation is:

$$
\min \sum_ {t \in \mathcal {T}} \left(h _ {0} I _ {0} ^ {t} + \sum_ {i \in \mathcal {N} ^ {\prime}} h _ {i} I _ {i} ^ {t} + \sum_ {i \in \mathcal {N} ^ {\prime}} \rho h _ {i} B _ {i} ^ {t} + \sum_ {k \in \mathcal {K}} \sum_ {(i, j) \in \mathcal {A}} c _ {i, j} y _ {i, j} ^ {k, t}\right)\tag{1}
$$

$$
\text {s.t.} \quad I _ {0} ^ {t} = I _ {0} ^ {t - 1} + d _ {0} ^ {t} - \sum_ {k \in \mathcal {K}} \sum_ {i \in \mathcal {N} ^ {\prime}} q _ {i} ^ {k, t}
$$

$$
\forall t \in \mathcal {T},\tag{2}
$$

$$
I _ {i} ^ {t} = I _ {i} ^ {t - 1} - d _ {i} ^ {t} + \sum_ {k \in \mathcal {K}} q _ {i} ^ {k, t} + B _ {i} ^ {t}
$$

$$
\forall i \in \mathcal {N} ^ {\prime}, t \in \mathcal {T},\tag{3}
$$

$$
\sum_ {k \in \mathcal {K}} q _ {i} ^ {k, t} + I _ {i} ^ {t - 1} \leq U _ {i}
$$

$$
\forall i \in \mathcal {N} ^ {\prime}, t \in \mathcal {T},\tag{4}
$$

$$
q _ {i} ^ {k, t} \leq U _ {i} z _ {i} ^ {k, t}
$$

$$
\forall i \in \mathcal {N} ^ {\prime}, k \in \mathcal {K}, t \in \mathcal {T},\tag{5}
$$

$$
\sum_ {i \in \mathcal {N} ^ {\prime}} q _ {i} ^ {k, t} \leq Q z _ {0} ^ {k, t}
$$

$$
\forall k \in \mathcal {K}, t \in \mathcal {T},\tag{6}
$$

$$
\sum_ {k \in \mathcal {K}} z _ {i} ^ {k, t} \leq 1
$$

$$
\forall i \in \mathcal {N} ^ {\prime}, t \in \mathcal {T},\tag{7}
$$

$$
\sum \quad y _ {i, j} ^ {k, t} = \quad \sum \quad y _ {j i} ^ {k, t} = z _ {i} ^ {k, t}
$$

$$
\forall i \in \mathcal {N} ^ {\prime}, k \in \mathcal {K}, t \in \mathcal {T},\tag{8}
$$

$$
\sum_ {j \in \mathcal {N} ^ {\prime} \cup \{n + 1 \}} y _ {0, j} ^ {k, t} = z _ {0} ^ {k, t} = \sum_ {j \in \mathcal {N} ^ {\prime} \cup \{0 \}} y _ {j, n + 1} ^ {k, t} = z _ {n + 1} ^ {k, t} = 1
$$

$$
\forall k \in \mathcal {K}, t \in \mathcal {T},\tag{9}
$$

$$
Q _ {0} ^ {k, t} = \sum_ {i \in \mathcal {N} ^ {\prime}} q _ {i} ^ {k, t}
$$

$$
k \in \mathcal {K}, t \in \mathcal {T},\tag{10}
$$

$$
Q _ {i} ^ {k, t} - q _ {i} ^ {k, t} \geq Q _ {j} ^ {k, t} - Q \left(1 - y _ {i, j} ^ {k, t}\right)
$$

$$
\forall (i, j) \in \mathcal {A}, k \in \mathcal {K}, t \in \mathcal {T},\tag{11}
$$

$$
Q _ {i} ^ {k, t}, q _ {i} ^ {k, t} \geq 0
$$

$$
\forall i \in \mathcal {N} ^ {\prime}, k \in \mathcal {K}, t \in \mathcal {T},\tag{12}
$$

$$
q _ {0} ^ {k, t} = q _ {n + 1} ^ {k, t} = 0
$$

$$
\forall k \in \mathcal {K}, t \in \mathcal {T},\tag{13}
$$

$$
z _ {i} ^ {k, t} \in \{0, 1 \}
$$

$$
\forall i \in \mathcal {N} ^ {\prime}, k \in \mathcal {K}, t \in \mathcal {T},\tag{14}
$$

$$
I _ {i} ^ {t} \geq 0, B _ {i} ^ {t} \geq 0
$$

$$
\forall i \in \mathcal {N} ^ {\prime}, t \in \mathcal {T},\tag{15}
$$

$$
y _ {i, j} ^ {k, t} \in \{0, 1 \}
$$

$$
\forall (i, j) \in \mathcal {A}, k \in \mathcal {K}, t \in \mathcal {T}.\tag{16}
$$

Constraints (2) define the inventory level supplier while constraints (3) determine the inventory level at retailer i at the end of the day t, where $B _ { i } ^ { t }$ represents the stock-out quantity. Constraints (4) ensure that the total quantity delivered to retailer i on day t by all vehicles $k \in \mathcal { K }$ , combined with the previous day’s inventory $I _ { i } ^ { t - 1 }$ , does not exceed the retailer’s inventory capacity $U _ { i }$ . This follows the maximum level policy, which allows flexibility in delivery quantities as long as post-delivery levels remain within maximum inventory limits. Constraints (5) ensure that the delivered quantity is zero if the vehicle does not visit the retailer $( z _ { i } ^ { k , t } = 0 )$ . Constraints (6) impose vehicle capacity limits, while constraints (7)–(13) model the routing constraints. Specifically, constraints (7) stipulate that each retailer can be visited no more than once per day. Constraints (8) regulate the flow through each node for each vehicle on each day. Constraints (9) require each vehicle to depart from and return to the depot, while constraints (10)–(13) ensure proper tracking of the vehicle load throughout its journey and prevent subtours.

Finally, Constraints (15), in conjunction with the objective function, ensure that $I _ { i } ^ { t }$ is set to zero when inventory is insufficient to meet demand and that $B _ { i } ^ { t }$ remains zero when there is no stock-out.

The following property holds and will play a role in the analysis of the complexity of the large neighborhood operators we introduce:

Property 1 (Archetti and Ljubić (2022)) When the input parameters $Q , U _ { i j }$ , and $d _ { i } ^ { t }$ are integer, there always exists an optimal solution in which the quantity variables $q _ { i } ^ { k , t }$ (and, consequently, the inventory and stock-out variables $I _ { i } ^ { t }$ and $B _ { i } ^ { t } )$ are integer-valued for all $i   \in   \mathcal { N } ,   k   \in   \mathcal { K } _ { j }$ , and $t \in \mathcal { T }$

## 4. A New Large Neighborhood Search Operator

This paper proposes a new, efficient neighborhood search operator for the Inventory Routing Problem (IRP), designed to be broadly applicable, regardless of the metaheuristic context. Specifically, given an incumbent solution and a selected retailer i, it removes all visits to it over the planning horizon and optimally selects new visit days, delivery quantities, and delivery locations among existing routes or new direct routes with a single visit, while accounting for all relevant costs.

Consequently, this move can also be viewed as a simultaneous reinsertion operator across multiple days, specifically designed for IRP. It is iteratively applied to all retailers in random order until a local minimum is reached. The closest comparable concept in the literature is the pattern improvement (PI) operator proposed in Vidal et al. (2012), which optimally selects a visit pattern over an extended planning horizon and insertion positions for the multi-period VRP. However, the operator introduced here for the IRP is significantly different, as it handles inventory level constraints, accounts for possible stock-outs, and solves an underlying combinatorial optimization problem to identify the best reinsertion configuration. As a result, it will be referred to as the delivery schedule (DS) operator throughout the remainder of this document. As will be shown, dynamic programming (DP) algorithms can be designed to find optimal reinsertion positions and quantities. The proposed method is versatile and can be adapted to different IRP variants, such as those with penalized stock-outs.

We note that the DS operator allows the insertion of a visit to a retailer into a route, even if this causes a violation of the capacity constraints. The capacity violation is penalized by multiplying the excess quantity by a penalty parameter ω. The insertion procedure, together with the definition of the quantity to be delivered and the corresponding cost, is detailed in Section 4.2.

Figure 1 illustrates how the DS operator works. One of the retailers (highlighted in blue in the figure) is selected to be removed from its original visit positions, as shown in the first row. After applying the DP algorithm explained below, new insertion positions are determined, as depicted in the second row. Note that the delivery quantities for each day have also been adjusted, leading to completely different inventory levels over the planning horizon. Importantly, while the initial situation is associated with a stock-out quantity equal to 2 in the third period, the move results in a solution with no stock-outs, as illustrated in the bars close to each plot.

## 4.1. Dynamic Programming Algorithm

After having removed a retailer i from all routes, the DS operator determines the best reinsertions in terms of days, routes, and quantities. The evaluation of the reinsertion cost in the IRP is quite challenging. Indeed, the cost depends on the inventory level, which in turn depends on the quantity delivered in former visits to the retailer. Our main contribution is the design of an efficient method to compute the reinsertion cost function. To do that, we first observe that, for each day t, the reinsertion cost function is a piecewise linear function in the inventory level $I _ { i } ^ { t }$ . Then, we develop a DP algorithm that iteratively computes an optimal replenishment strategy.

![](images/page_10_image_2.jpg)

Figure 1 Illustration of the DS neighborhood

The DP algorithm efficiently computes function $C _ { t } ( I _ { i } ^ { t } )$ , which represents the minimum cost associated with inventory level I for retailer i at time t, from t = 1 to t = H. The cost includes inventory cost or stock-out cost at the retailer, detour cost associated with the insertion of retailer i in the daily routes of day t (in case a positive quantity is delivered at time $t )$ , supplier’s holding costs (which is negative in case of positive quantity delivered), and penalties associated with vehicle capacity violations. Since the inventory level is represented at the end of the day, after deduction of the retailer demand quantity $d _ { i } ^ { t }$ on that day, and the inventory at the start of the day is upper limited to $U _ { i }$ due to capacity limits, we have $I _ { i } ^ { t } \in [ 0 , U _ { i } - d _ { i } ^ { t } ]$

Functions $C _ { t } ( I _ { i } ^ { t } )$ are piecewise linear, and it is possible to compute them recursively using $\mathrm { D P } ,$ from t − 1 to $t ,$ as illustrated in Figure 2. In practice, these functions will be efficiently represented as linked lists of function pieces, ordered by increasing inventory value, each of which is represented by the endpoints and slope. Moreover, due to Property 1, any segment that does not span an integer inventory value can be discarded throughout the algorithm. Thus, the complexity of the DP algorithm will depend on the number of pieces of this function, as analyzed in Section 4.4.

The cost function $C _ { t } ( I _ { i } ^ { t } )$ is computed in two steps for each t. First of all, we compute a delivery cost function $\hat { C } _ { t } ( \hat { I } _ { i } ^ { t } )$ considering inventory levels $\hat { I } _ { i } ^ { t } \in [ - d _ { i } ^ { t } , U _ { i } - d _ { i } ^ { t } ]$ that are possibly negative and trigger up to $d _ { i } ^ { t }$ units of stock-out at the current period t. Then, we include the related stock-out penalties to derive $C _ { t } ( I _ { i } ^ { t } )$ for $I _ { i } ^ { t } \in [ 0 , U _ { i } - d _ { i } ^ { t } ]$ . Function $\hat { C } _ { t } ( \hat { I } _ { i } ^ { t } )$ can be computed by taking the minimal cost out of two options:

![](images/page_11_image_2.jpg)

Figure 2 The evolution of the cost function Ct(I<sup>t</sup><sub>i</sub> )

(i) If no delivery is performed at time $t ,$ the inventory level can be obtained by $I _ { i } ^ { t - 1 } = \hat { I } _ { i } ^ { t } + d _ { i } ^ { t }$ for a given value of $\hat { I } _ { i } ^ { t }$ , thus the cost is:

$$
f _ {1} (\hat {I} _ {i} ^ {t}) = C _ {t - 1} (\hat {I} _ {i} ^ {t} + d _ {i} ^ {t}) + h _ {i} \hat {I} _ {i} ^ {t},\tag{17}
$$

where $h _ { i } \hat { I } _ { i } ^ { t }$ is the holding cost.

(ii) If a delivery is performed, we should select the quantity $q _ { i } ^ { t } > 0$ for which the cost associated with $\hat { I } _ { i } ^ { t }$ is minimized. Note that, for a given value of $\hat { I } _ { i } ^ { t }$ , once we determine the quantity $q _ { i } ^ { t }$ the inventory level $I _ { i } ^ { t - 1 }$ corresponds to $I _ { i } ^ { t - 1 } = \hat { I } _ { i } ^ { t } + d _ { i } ^ { t } - q _ { i } ^ { t }$ . Thus, the cost function associated with this case is:

$$
f_{2}(\hat{I}_{i}^{t}) = \min_{\substack{q_{i}^{t} > 0}}\bigg(C_{t - 1}(\hat{I}_{i}^{t} + d_{i}^{t} - q_{i}^{t}) + h_{i}\hat{I}_{i}^{t} + F_{t}(q_{i}^{t}) - h_{0}^{t}(H - t + 1)q_{i}^{t}\bigg),\tag{18}
$$

where $F_{t}(q_{i}^{t})   is a$ piecewise linear function calculating the necessary detour (and possible capacity penalty) costs to insert a visit to retailer i into a route on day t and deliver $q _ { i } ^ { t }$ units, and $h _ { 0 } ^ { t } ( H { \circleddash } t + 1 ) q _ { i } ^ { t }$ is the reduction in holding cost at the supplier for the remaining days. ore e a s on e pre-process ng M d t il th i of function $F _ { t } ( q _ { i } ^ { t } )$ are given in the next section.

Overall, the cost $\hat { C } _ { t } ( \hat { I } _ { i } ^ { t } )$ is calculated as:

$$
\hat {C} _ {t} (\hat {I} _ {i} ^ {t}) = \min \big (f _ {1} (\hat {I} _ {i} ^ {t}), f _ {2} (\hat {I} _ {i} ^ {t}) \big).\tag{19}
$$

Finally, we must derive function $C _ { t } ( I _ { i } ^ { t } )$ considering stock-out penalties. Note that, thanks to the way stock-out costs are defined $( \rho h _ { i }$ with $\rho > 1 )$ , it is always convenient to avoid any unnecessary stock-out leading to $I _ { i } ^ { t } > 0$ in any given day. Otherwise, when a stock-out occurs $( \mathrm { i . e . , ~ } \hat { I } _ { i } ^ { t } \leq 0$ in Equation (19)), a penalty of $\rho h _ { i }$ multiplied by the number of stock-out units $( - \hat { I } _ { i } ^ { t } )$ is incurred, and the additional holding cost term $h _ { i } \hat { I } _ { i } ^ { t }$ in Equation (19) should be removed accordingly. Therefore, we can calculate the function as:

$$
C _ {t} (I _ {i} ^ {t}) = \left\{ \begin{array}{l l} \min _ {\hat {I} _ {i} ^ {t} \in [ - d _ {i} ^ {t}, 0 ]} \left(\hat {C} _ {t} (\hat {I} _ {i} ^ {t}) - \rho h _ {i} \hat {I} _ {i} ^ {t} - h _ {i} \hat {I} _ {i} ^ {t}\right) & \text {if} I _ {i} ^ {t} = 0 \\ \hat {C} _ {t} (\hat {I} _ {i} ^ {t}) & \text {otherwise.} \end{array} \right.\tag{20}
$$

Observe that, when stock-outs are forbidden, we can take $C _ { t } ( I _ { i } ^ { t } )   =   \hat { C } _ { t } ( \hat { I } _ { i } ^ { t } )$ considering only cases where $\hat { I } _ { i } ^ { t } \geq 0$ . Moreover, backlogging (allowing negative inventory levels to be carried over and fulfilled in future periods) is not considered in the present paper, but the DS operator could accommodate backorders with minimal structural changes as explained in Appendix A.

Once the DP algorithm has reached day $H ,$ it determines the inventory level $I _ { i } ^ { H * }$ associated with the minimum cost $C _ { H } ( I _ { i } ^ { H } )$ . i.e., $I _ { i } ^ { H * } = \mathrm { a r g }$ min ${ } _ { I _ { i } ^ { H } } C _ { H } ( I _ { i } ^ { H } )$ . Finally, a backtracking procedure, starting from $I _ { i } ^ { H * }$ , determines the quantity $q _ { i } ^ { t }$ to be delivered to the retailer on each day t.

## 4.2. Preprocessing Functions $F _ { t } ( q _ { i } ^ { t } )$

Before executing the DP algorithm for a retailer $i ,$ we preprocess the functions $F _ { t } ( q _ { i } ^ { t } )$ for each day t, representing the minimum cost of inserting a visit to retailer i to deliver $q _ { i } ^ { t }$ units. This involves evaluating all existing routes on day to calculate their residual capacity and detour cost $( \kappa , \gamma )$ associated with a least-cost insertion. If fewer than K routes exist on day t, we also consider $t ,$ creating a new route for $i ,$ with a detour cost $\gamma = c _ { 0 i } + c _ { i 0 }$ and residual capacity $\kappa   =   Q$

In alignment with the penalty framework employed to diversify the search in Vidal et al. (2012), Vidal (2022), we allow penalized capacity violations in the routes, weighted by a penalty factor $\omega$ which remains fixed during each execution of the DS operator. Based on these definitions, we have $F_{t}(q_{i}^{t}) = \min_{k \in \mathcal{K}} \left( \gamma_{k} + \omega \max(0, q_{i}^{t} - \kappa_{k}) \right)$ . This function can be built in $O ( K \log ( K ) )$ time by ranking delivery options increasing order of detour cost, resulting in a list $( ( \kappa _ { 1 } , \gamma _ { 1 } ) , \ldots , ( \kappa _ { m } , \gamma _ { m } ) )$ of $m \leq K$ delivery options, and eliminating dominated options. An illustration of the resulting function is presented in Figure 3.

## 4.3. Practical Implementation

As discussed previously, each function $C _ { t } ( I _ { i } ^ { t } )$ and $F _ { t } ( q _ { i } ^ { t } )$ is piecewise linear and can be efficiently represented as a linked list of function pieces represented by their interval and slope. A practical implementation of the calculations of Equations (17–20) requires efficiently handling some primitive operations on these functions:

• Translation: Compute $g ( x ) = f ( x + a )$ where $a \in \mathfrak { R }$ is a constant. This operation occurs in Equations (17) and (18) and can be done in $O ( \Phi ( f ) )$ elementary operations by translating each segment, where $\Phi ( f )$ is the number of pieces of $f .$ It does not change the number of pieces of the resulting function.

![](images/page_13_image_2.jpg)

Figure 3 Illustration of a function $F _ { t } ( q _ { i } ^ { t } )$

• Sum with an affine function: Compute $g ( x ) = f ( x ) + a x { \mathrm { ~ w i t h ~ } } a \in \Re$ This operation occurs in Equations (17) and (18). It can be performed in $O ( \Phi ( f _ {   } ) )$ elementary operations by changing the slope of each segment of $f .$ The number of pieces of the function remains unchanged.

• Lower envelope: Compute $g ( x )   =   \operatorname* { m i n } ( f _ { 1 } ( x ) , \underline { { f _ { 2 } } } ( x ) )$ It occurs in Equation (19) and can be done in $O ( \Phi ( f _ { 1 } ) + \Phi ( f _ { 2 } ) )$ elementary operations by jointly sweeping through the segments of $f _ { 1 }$ and $f _ { 2 }$ and keeping track of the minimum, producing $O \big ( \Phi \big ( f _ { 1 } \big ) + \Phi \big ( f _ { 2 } \big ) \big )$ pieces.

• Infimal convolution: Compute $g(x) = \min_{y} \left( f_{1}(x - y) + f_{2}(y) \right)$ (see, e.g., Bauschke and Combettes 2017). This operation is more complex and occurs during the calculations of Equation (18). It can be done in $O ( \Phi ( f _ { 1 } ) \Phi ( f _ { 2 } ) )$ elementary operations by observing that $g ( x )$ is the lower envelope of the infimal convolutions $o f \textcircled{a} \Pi$ pairs of segments in $f _ { 1 }$ and $f _ { 2 }$ . Each such convolution can be geometrically calculated as the lower edges of a parallelogram, as illustrated in Figure 4. The resulting function $g$ can $have $O \big ( \Phi \big ( f _ { 1 } \big ) \times \Phi \big ( f _ { 2 } \big ) \big )$$ pieces.

## 4.4. Computational Complexity

Preprocessing the functions $F _ { t } ( q _ { i } ^ { t } )$ for all days requires $O ( H K \log ( K ) )$ time (Section 4.2). Next, the computational effort to resolve the DP recursion depends on the number of pieces in the $C _ { t } ( I _ { i } ^ { t } )$ functions. Since segments that do not contain integer values in the range $\{ 0 , \ldots , U _ { i } \}$ can be disregarded, the number of pieces is in $O ( U _ { i } )$ . The most computationally intensive operation in each recursion is the calculation of the infimal convolution between the functions $C _ { t - 1 }$ and $F _ { t }$ which have $O ( U _ { i } )$ and $O ( K )$ pieces, respectively. This convolution requires $O ( U _ { i } K )$ elementary operations. However, many of these are later discarded, either because they fall outside the valid inventory range or due to domination when retaining the lower-cost segments. As the convolution is performed for each of the H days, exploring the DS neighborhood for a single retailer $i ,$ including preprocessing, takes $O ( U _ { i } K H )$ time. This analysis assumes $\log ( K ) \leq U _ { i }$ , which typically holds in practice. Moreover, as demonstrated in our computational experiments in Section 6.2, the number of pieces in the function $C _ { t }$ remains far below their theoretical maximum in practice. For our problem instances, the complete evaluation of the DS neighborhood for any retailer i is typically completed in a hundred microseconds.

![](images/page_14_image_2.jpg)

Figure 4 An example of computation of the superposition of two piecewise linear functions.

## 5. Hybrid Genetic Search

The DS operator described above is integrated into the HGS framework initially introduced by Vidal et al. (2012), which we adapt to solve the IRP. While the DS operator can in principle be embedded within any metaheuristic, we selected HGS due to its flexibility, ability to effectively solve multi-perio problems with time constraints, and strong empirical performance across various VRP settings idal et al. 2013, 2014). In addition to its successful application in prior research, HGS has also demonstrated top-tier performance in recent benchmarking competitions, such as the DIMACS VRP Challenge and the EURO/NeurIPS Vehicle Routing Competition (Kool et al. 2022), where it formed the core of leading solution methods. These results further support the robustness of HGS as a general-purpose search framework for complex VRPs.

Figure 5 outlines the HGS-IRP framework, which follows the structure of the original HGS but includes several key adaptations. The solution is represented by a collection of giant tours—one per day—that encode customer sequences. Combined with delivery quantities, they define a complete IRP solution. The population includes both feasible and infeasible individuals, with penalized capacity violations encouraged to foster diversification.

After generating an initial population (Section 5.2), the algorithm iteratively applies selection and crossover (Section 5.3), followed by route decoding via the Split algorithm (Prins 2004). A local search phase (Section 5.4) then refines each offspring through (i) route improvement (RI) while keeping delivery quantities fixed, (ii) delivery schedule improvement (DSI) using the DS operator, and (iii) re-optimization of routes (RI). After educating the offspring, the algorithm inserts the resulting solution in the correct subpopulation according to its feasibility and possibly repairs it to additionally include the resulting solution in the feasible subpopulation. If the maximum size of any subpopulation is reached, a survivor selection process is triggered to reduce this subpopulation size (Section 5.5). Subsequently, the penalty parameter associated with capacity violations is adjusted. If the best solution does not improve within a predefined number of iterations, the population is diversified by introducing new solutions generated through the same procedure as in the initialization.

![](images/page_15_image_3.jpg)

Figure 5 High-level description of the HGS-IRP algorithm

## 5.1. Solution Representation.

Each individual in the genetic algorithm represents a solution. It contains, on each day, the sequence of visits to retailers without trip delimiters, i.e., represented as a “giant tour” (Prins 2004). This representation is advantageous since it is possible to optimally split this giant tour to create individual routes using a linear-time split algorithm (Vidal 2016). For the IRP, additional information is needed to completely represent solutions: the quantities delivered to each retailer on each day. Therefore, each solution includes, on each day, (i) a giant tour chromosome encoding the visit sequence and (ii) a quantity chromosome specifying the corresponding delivery quantities.

## 5.2. Generation of Initial Solutions

Each initial solution is constructed using a just-in-time delivery rule. Starting from day $t = 1$ a retailer is scheduled for a visit if its stock is insufficient to meet demand for the next period. The delivery quantity is determined by the order-up-to level (OU) policy, meaning the retailer’s inventory is replenished up to its maximum capacity $U _ { i }$ . Additionally, even if a retailer has sufficient inventory, there is a 30% probability of making a delivery anyway, still up to reaching level $U _ { i }$ This process continues until the final day H. Once the set of daily quantities are fixed, the visits are ordered randomly on each day, partitioned into vehicle routes using the Split algorithm, and the education operator (Section 5.4) is applied to refine the solution.

## 5.3. Selection and Crossover

Each parent is selected by a binary tournament within the union of the feasible and infeasible subpopulations. The crossover procedure begins by randomly shuffling the days and selecting two random indices $j _ { 1 }$ and $j _ { 2 }$ with uniform probability such that $j _ { 1 } < j _ { 2 }$ from this list. These indices divide the days into three sets.

For days with indices strictly below j<sub>1</sub>, a segment of deliveries is inherited from Parent 1. This segment is determined by selecting a random start and end position within the parent’s sequence for that day, as in the PIX crossover of Vidal et al. (2012). The corresponding deliveries, along with their respective delivery quantities, are transferred to the offspring. On days with indices within $\{ j _ { 1 } , \ldots , j _ { 2 } - \underline { { 1 } } \}$ no deliveries are inherited. Finally, for the remaining days, the entire delivery sequence from Parent 1 is copied to the offspring.

Once inheritance from Parent 1 is complete, missing deliveries are filled using Parent 2. Specifically, for days with indices strictly below $j _ { 2 } ,$ where no sequence or only a partial sequence was inherited from Parent 1, additional deliveries from Parent 2 are introduced. Each delivery is added at the end of the sequence only if it does not already appear on that day. The corresponding delivery quantities are also inherited, unless they would exceed the retailer’s inventory constraints, in which case the maximum feasible delivery quantity is selected.

After inheritance is finalized, the split algorithm is applied on each day to partition each giant tour into individual routes. The resulting solution is then refined through the local-search-based education process described in the next section.

## 5.4. Education

The local-search education procedure improves solutions by reorganizing the delivery schedule across all routes and days. This operation is applied to complete solutions. The process follows three sequential steps: RI-DSI-RI. The first and last steps, referred to as Route Improvement (RI), involve a standard local search procedure identical to that of Vidal et al. (2012), based on nine classic neighborhood operators, including Relocate and Swap (involving up to two consecutive nodes), as well as 2-Opt and $2-OPT ^{*}$ . These neighborhoods are explored in a randomized order, with any improving move immediately accepted until a local minimum is reached. For the Delivery Schedule Improvement (DSI) phase, as described in Section 4, we iterate over all retailers in random order to optimize their delivery schedules by reassigning visit days. This phase stops when a complete pass over all retailers results in no improvement in any retailer’s delivery plan.

## 5.5. Diversity Management

When a subpopulation reaches its maximum size, the algorithm employs a survivor selection process, similar to the method proposed in Vidal et $\mathrm{abL}(2012)$ , to determine which individuals are retained for the next generation. This mechanism aims to maintain diversity in visit patterns while preserving elite solutions based on cost. Consequently, discarded individuals are either clones or solutions that perform poorly in terms of both cost and contribution to population diversity.

To quantify diversity, a distance measure specific to the IRP setting is used. Given two individuals, $P _ { 1 }$ and $P _ { 2 }$ , their distance is computed as:

$$
\Delta (P _ {1}, P _ {2}) = \frac {1}{n} \sum_ {i = 1} ^ {n} \mathbb {1} (\pi_ {i} (P _ {1}) \neq \pi_ {i} (P _ {2}))\tag{21}
$$

where $\mathbf { 1 } ( \pi _ { i } ( P _ { 1 } ) \neq \pi _ { \underline { { i } } } ( P _ { 2 } ) )$ equals 1 if the set of delivery days $\pi _ { i } ( P _ { 1 } )$ assigned to retailer i in $P _ { 1 }$ differs from that in P<sub>2</sub>, and 0 otherwise.

As in Vidal et al. (2012), this distance measure is used to define a biased fitness function that influences selection probability, ensuring that the survivor selection process effectively maintains diversity while eliminating redundant or low-quality solutions.

## 6. Computational experiments

This section presents the computational experiments conducted to evaluate the performance of the HGS algorithm using the new DS operator for the IRP. We first focus on the classical IRP without stock-out, as it is a benchmark in the literature, and the results are detailed in Section 6.1. We then investigate the empirical behavior of the number of linear pieces in the cost-to-go functions $C _ { t } ,$ introduced in Section 4.4, to assess the practical computational complexity of the DS operator. The corresponding analysis and results are presented in Section 6.2. Finally, we evaluate the algorithm’s performance on the IRP with stock-out, providing further insights into the trade-offs between customer service levels and delivery costs in Section 6.3.

Benchmark Instances. We test the algorithm on established IRP benchmark instances, categorized into small and large instance datasets. The small dataset consists of well-known instances from (Archetti et al. 2007), while the large instances were introduced in Archetti et al. (2012).

Each instance in the small dataset is defined by three parameters: the planning horizon (H), the number of retailers (n), and the inventory cost level (C). The dataset is divided into four categories, covering two values of H (H = 3 and H = 6) and two levels of inventory cost: low inventory cost (LC) and high inventory cost (HC). The number of retailers n in each category ranges from 10 to 50. Each problem size includes five distinct instances. The number available vehicles K varies between 2 and 5, resulting in a total of 800 instances in th dataset. The large dataset introduced in Archetti et al. (2012) follows a similar struct ith $H = 6$ and $n \in \{ 5 0 , 1 0 0 , 2 0 0 \}$ The settings for C and K remain consistent with the smal instances. For each of the 24 possible parameter combinations (n, H, C, K), 10 randomly generated instances were created, leading to a total of 240 large instances. More recently, Skålnes et al. (2024) introduced a new set of IRP instances designed to be more challenging than the benchmark instances described above. We refer to the small and large datasets as benchmark instances, while we denote the instances from Skålnes et al. (2024) as SAHS instances (named as the initials of the authors). In Section 6.1, we evaluate the HGS algorithm on SAHS instances as well. These instances feature varying numbers of retailers (10 to 200), planning horizons of $\underline { { 6 } } \lrcorner \overline { { 9 } } ,$ or 12 periods, and multiple vehicle types with capacities of 8, 18, or 38 EUR-pallets. Unlike the benchmark dataset, which assumes constant retailer demand, SAHS instances incorporate variable demand over time to better simulate real-world conditions.

For the tests in Section 6.3, where stock-out is allowed, we used the small benchmark dataset and set the value of the stock-out penalty ρ as follows: 50, 100, 300, and 1,000,000, the latter being set to a large value to avoid stock-out. Thus, we obtained four instances for each original IRP instance.

Experimental Setup. All experiments were conducted on a server equipped with Intel(R) Xeon(R) Gold 6336Y CPUs running at 2.40 GHz. Each experiment was executed on a single CPU. The open-source code and instances are available at https://github.com/vidalt/HGS-IRP/,along with solution details for each instance.

The HGS algorithm terminates when any of the following stopping criteria are met: (i) a total of 100,000 iterations, (ii) 10,000 consecutive iterations without improvement, or (iii) a maximum runtime of 2,400 seconds for small-scale instances and 7,200 seconds for large-scale and SAHS instances. This configuration permits the use of a computational time, on large instances, commensurate to that used by the other methods.

## 6.1. Performance analysis on the IRP

Classical benchmark instances for the IRP do not permit stock-out. To accommodate this setting, we omit negative $\hat { I } _ { i } ^ { t }$ in the DP transition processes described in Section 4 while retaining the rest of the algorithm unchanged. We compare the performance of our algorithm, HGS-IRP, against the most recent heuristics in the literature as well as the best-performing method from the DIMACS 2022 Implementation Challenge on Vehicle Routing, which included a dedicated track on the IRP. All benchmark instances and reference solutions used in our experiments are sourced from https://or-brescia.unibs.it/instances and http: $/ / \mathrm { d } ]$ imacs.rutgers.edu/programs/ challenge/vrp/irp/, and are also provided in the Git repos or associated with this project. HGS-IRP is evaluated against three leading methods: the unifie decomposition matheuristic pro posed by Chitsaz et al. (2019) (denoted CCJ), the kernel search heuristic of Archetti et al. (2021) (KS), and the Branch-and-Heuristic approach developed by Skålnes et al. (2023) (BCHeu), which achieved first place in the DIMACS competition. This selection provides a comprehensive basis for performance comparison.

Results are summarized in Table 1 which reports average values for instances sharing the same values of n, H, and C, on the benchmark instances, small and large (the latter corresponding to the last two blocks). For each method, we report the solution value (Sol), the percentage gap (Gap) relative to the best known solution (BKS, shown in the last column), and the computational time in seconds (T(s)). The gap is computed as $\left( \frac{ Sol }{ BKS } - 1 \right) \times 100\%$ . To the best of our knowledge, the BKS values are compiled from all existing methods for the IRP under an ML-based inventory policy, including the best-performing solutions reported in the DIMACS 2022 Vehicle Routing Implementation hallenge. In contrast to these single-run results, we report the average results of our method over multiple runs, as this provides a more reliable performance estimator given the random nature of the algorithm. Specifically, we present the average solution value $\mathrm { ( A v g ) }$ , average gap $\mathrm { ( G a p _ { A } ) }$ to the best known solution (BKS), average CPU time (T(s)), the best solution (Best) among the 10 runs and its corresponding gap to the BKS (Gap<sub>B</sub>).

The proposed HGS-IRP algorithm exhibits strong performance in both solution quality and computational efficiency. It consistently produces solutions that are comparable to, or better than, those obtained by existing methods, all within reasonable computational times. Across all 1,040 tested instances, the maximum optimality gap relative to the BKS is only 0.29%, while the average gap is −0.15%, both of which outperform all benchmark algorithms. In terms of computational time, HGS-IRP is particularly efficient on large-scale instances, and it also maintains strong solution quality on smaller instances. As the problem size increases, both in number of periods (H) and customers (n), the advantages of HGS-IRP become more pronounced. On the small 3-day dataset (400 instances), HGS-IRP identifies 37 new best-known solutions, matches the existing BKS in 320 instances, and performs slightly worse in only 43 instances. For the small 6-day dataset, it finds 150 new best solutions and matches the BKS in 83 instances. Most notably, on the large 6-day dataset, HGS-IRP finds new best solutions in 178 out of 240 instances, representing a substantial improvement over the current state-of-the-art in solving large-scale IRP problems.

Table 1 Comparative analysis on medium-scale IRP instances

<table><tr><td rowspan="2">H</td><td rowspan="2">C</td><td rowspan="2">n</td><td colspan="3">CCJ</td><td colspan="3">KS</td><td colspan="3">BCHeu</td><td colspan="5">HGS-IRP</td><td rowspan="2">BKS</td></tr><tr><td>Sol</td><td>Gap(%)</td><td>T(s)</td><td>Sol</td><td>Gap(%)</td><td>T(s)</td><td>Sol</td><td>Gap(%)</td><td>T(s)</td><td>Avg</td><td> $Gap_A$ (%)</td><td>T(s)</td><td>Best</td><td> $Gap_B$ (%)</td></tr><tr><td rowspan="52">3</td><td rowspan="11">HC</td><td>5</td><td>2855.05</td><td>3.39</td><td>1.7</td><td>2761.47</td><td>0.00</td><td>5.9</td><td>2761.47</td><td>0.00</td><td>7200.0</td><td>2761.47</td><td>0.00</td><td>60.3</td><td>2761.47</td><td>0.00</td><td>2761.47</td></tr><tr><td>10</td><td>5013.81</td><td>3.24</td><td>4.3</td><td>4856.89</td><td>0.01</td><td>91.3</td><td>4856.50</td><td>0.00</td><td>7200.0</td><td>4856.50</td><td>0.00</td><td>104.3</td><td>4856.50</td><td>0.00</td><td>4856.50</td></tr><tr><td>15</td><td>5620.86</td><td>1.63</td><td>11.3</td><td>5534.01</td><td>0.06</td><td>114.9</td><td>5530.87</td><td>0.00</td><td>7200.0</td><td>5530.88</td><td>0.00</td><td>119.6</td><td>5530.87</td><td>0.00</td><td>5530.87</td></tr><tr><td>20</td><td>7191.44</td><td>1.39</td><td>25.3</td><td>7105.34</td><td>0.18</td><td>202.6</td><td>7093.86</td><td>0.02</td><td>7200.0</td><td>7092.57</td><td>0.00</td><td>127.0</td><td>7092.57</td><td>0.00</td><td>7092.57</td></tr><tr><td>25</td><td>8501.63</td><td>0.86</td><td>37.6</td><td>8438.19</td><td>0.10</td><td>324.3</td><td>8429.51</td><td>0.00</td><td>7200.0</td><td>8430.00</td><td>0.01</td><td>153.9</td><td>8429.50</td><td>0.00</td><td>8429.42</td></tr><tr><td>30</td><td>9699.83</td><td>0.40</td><td>64.1</td><td>9721.92</td><td>0.63</td><td>504.8</td><td>9665.34</td><td>0.04</td><td>7200.0</td><td>9660.65</td><td>0.00</td><td>207.5</td><td>9660.57</td><td>-0.01</td><td>9661.11</td></tr><tr><td>35</td><td>10210.21</td><td>0.39</td><td>85.2</td><td>10205.92</td><td>0.35</td><td>544.2</td><td>10172.89</td><td>0.02</td><td>7200.0</td><td>10171.15</td><td>0.01</td><td>259.5</td><td>10170.59</td><td>0.00</td><td>10170.59</td></tr><tr><td>40</td><td>10986.12</td><td>0.46</td><td>141.9</td><td>11012.14</td><td>0.70</td><td>614.7</td><td>10945.29</td><td>0.09</td><td>7200.0</td><td>10950.63</td><td>0.13</td><td>318.9</td><td>10935.93</td><td>0.00</td><td>10935.94</td></tr><tr><td>45</td><td>11998.55</td><td>0.27</td><td>179.9</td><td>12077.35</td><td>0.93</td><td>663.1</td><td>11999.87</td><td>0.28</td><td>7200.0</td><td>11976.60</td><td>0.09</td><td>313.1</td><td>11966.17</td><td>0.00</td><td>11966.14</td></tr><tr><td>50</td><td>13571.12</td><td>0.33</td><td>232.1</td><td>13692.82</td><td>1.23</td><td>1173.8</td><td>13546.34</td><td>0.15</td><td>7200.0</td><td>13528.67</td><td>0.02</td><td>453.9</td><td>13523.46</td><td>-0.02</td><td>13526.27</td></tr><tr><td>Avg</td><td>8564.86</td><td>0.85</td><td>78.3</td><td>8540.60</td><td>0.56</td><td>424.0</td><td>8500.19</td><td>0.08</td><td>7200.0</td><td>8495.91</td><td>0.03</td><td>211.8</td><td>8492.76</td><td>0.00</td><td>8493.09</td></tr><tr><td rowspan="11">LC</td><td>5</td><td>2180.27</td><td>4.81</td><td>1.7</td><td>2080.31</td><td>0.00</td><td>6.2</td><td>2080.31</td><td>0.00</td><td>7200.0</td><td>2080.32</td><td>0.00</td><td>60.4</td><td>2080.31</td><td>0.00</td><td>2080.31</td></tr><tr><td>10</td><td>3221.39</td><td>5.51</td><td>4.2</td><td>3053.18</td><td>0.00</td><td>89.3</td><td>3053.14</td><td>0.00</td><td>7200.0</td><td>3053.13</td><td>0.00</td><td>99.4</td><td>3053.13</td><td>0.00</td><td>3053.13</td></tr><tr><td>15</td><td>3200.77</td><td>2.66</td><td>10.3</td><td>3121.36</td><td>0.11</td><td>118.5</td><td>3118.09</td><td>0.01</td><td>7200.0</td><td>3117.85</td><td>0.00</td><td>107.6</td><td>3117.85</td><td>0.00</td><td>3117.85</td></tr><tr><td>20</td><td>3771.04</td><td>2.27</td><td>20.5</td><td>3702.66</td><td>0.41</td><td>225.8</td><td>3687.81</td><td>0.01</td><td>7200.0</td><td>3687.49</td><td>0.00</td><td>128.6</td><td>3687.48</td><td>0.00</td><td>3687.48</td></tr><tr><td>25</td><td>3994.91</td><td>1.49</td><td>60.6</td><td>3951.99</td><td>0.40</td><td>337.7</td><td>3937.48</td><td>0.03</td><td>7200.0</td><td>3938.14</td><td>0.04</td><td>149.6</td><td>3936.56</td><td>0.00</td><td>3936.37</td></tr><tr><td>30</td><td>3989.68</td><td>1.07</td><td>44.1</td><td>3978.59</td><td>0.78</td><td>482.1</td><td>3953.57</td><td>0.15</td><td>7200.0</td><td>3947.76</td><td>0.00</td><td>192.3</td><td>3947.63</td><td>0.00</td><td>3947.63</td></tr><tr><td>35</td><td>4237.04</td><td>0.94</td><td>58.1</td><td>4224.87</td><td>0.65</td><td>556.9</td><td>4198.92</td><td>0.03</td><td>7200.0</td><td>4197.83</td><td>0.01</td><td>207.2</td><td>4197.62</td><td>0.00</td><td>4197.58</td></tr><tr><td>40</td><td>4397.24</td><td>1.89</td><td>94.4</td><td>4377.20</td><td>1.43</td><td>619.9</td><td>4328.67</td><td>0.30</td><td>7200.0</td><td>4322.94</td><td>0.17</td><td>264.5</td><td>4315.28</td><td>-0.01</td><td>4315.63</td></tr><tr><td>45</td><td>4517.73</td><td>1.03</td><td>107.4</td><td>4576.23</td><td>2.33</td><td>698.3</td><td>4491.29</td><td>0.44</td><td>7200.0</td><td>4473.40</td><td>0.04</td><td>274.6</td><td>4471.83</td><td>0.00</td><td>4471.83</td></tr><tr><td>50</td><td>5296.46</td><td>1.16</td><td>152.7</td><td>5445.02</td><td>4.00</td><td>1098.2</td><td>5253.17</td><td>0.34</td><td>7200.0</td><td>5239.09</td><td>0.07</td><td>365.5</td><td>5232.78</td><td>-0.05</td><td>5235.53</td></tr><tr><td>Avg</td><td>3880.65</td><td>2.01</td><td>55.4</td><td>3851.14</td><td>1.23</td><td>423.3</td><td>3810.24</td><td>0.16</td><td>7200.0</td><td>3805.79</td><td>0.04</td><td>185.0</td><td>3798.08</td><td>-0.16</td><td>3804.33</td></tr><tr><td rowspan="11">HC</td><td>5</td><td>-</td><td>-</td><td>-</td><td>7371.68</td><td>0.00</td><td>95.6</td><td>7371.44</td><td>0.00</td><td>7200.0</td><td>7090.34</td><td>-3.81</td><td>394.3</td><td>7090.08</td><td>-3.82</td><td>7371.44</td></tr><tr><td>10</td><td>11760.57</td><td>7.54</td><td>13.1</td><td>10954.19</td><td>0.17</td><td>134.1</td><td>10936.89</td><td>0.01</td><td>7200.0</td><td>10940.78</td><td>0.05</td><td>828.9</td><td>10935.72</td><td>0.00</td><td>10935.67</td></tr><tr><td>15</td><td>13797.25</td><td>5.31</td><td>77.7</td><td>13156.04</td><td>0.42</td><td>198.5</td><td>13110.17</td><td>0.07</td><td>7200.0</td><td>13117.52</td><td>0.12</td><td>1042.8</td><td>13105.75</td><td>0.03</td><td>13101.33</td></tr><tr><td>20</td><td>16979.09</td><td>4.03</td><td>71.5</td><td>16420.79</td><td>0.61</td><td>503.7</td><td>16334.12</td><td>0.08</td><td>7200.0</td><td>16335.86</td><td>0.09</td><td>1358.5</td><td>16320.20</td><td>0.00</td><td>16320.60</td></tr><tr><td>25</td><td>19081.64</td><td>3.97</td><td>135.5</td><td>18498.31</td><td>0.79</td><td>694.3</td><td>18395.07</td><td>0.23</td><td>7200.0</td><td>18376.31</td><td>0.13</td><td>1590.9</td><td>18356.10</td><td>0.02</td><td>18353.33</td></tr><tr><td>30</td><td>21314.31</td><td>2.41</td><td>221.3</td><td>21034.43</td><td>1.06</td><td>687.2</td><td>20866.21</td><td>0.25</td><td>7200.0</td><td>20836.78</td><td>0.11</td><td>1766.2</td><td>20812.69</td><td>0.00</td><td>20813.61</td></tr><tr><td>35</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>22671.70</td><td>0.29</td><td>7200.0</td><td>22640.50</td><td>0.15</td><td>1888.2</td><td>22609.81</td><td>0.01</td><td>22606.89</td></tr><tr><td>40</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>24292.25</td><td>0.63</td><td>7200.0</td><td>23451.28</td><td>-2.86</td><td>1923.8</td><td>23400.59</td><td>-3.07</td><td>24141.23</td></tr><tr><td>45</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>26722.37</td><td>0.21</td><td>7200.0</td><td>25920.28</td><td>-2.80</td><td>2007.8</td><td>25880.87</td><td>-2.95</td><td>26667.58</td></tr><tr><td>50</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>30467.00</td><td>0.15</td><td>7200.0</td><td>29567.18</td><td>-2.81</td><td>2201.4</td><td>29515.75</td><td>-2.97</td><td>30420.51</td></tr><tr><td>Avg</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>19116.72</td><td>0.23</td><td>7200.0</td><td>18827.68</td><td>-1.16</td><td>1500.27</td><td>18802.75</td><td>-1.42</td><td>19073.22</td></tr><tr><td rowspan="11">LC</td><td>5</td><td>5794.88</td><td>5.78</td><td>5.8</td><td>5478.02</td><td>0.00</td><td>88.7</td><td>5477.99</td><td>0.00</td><td>7200.0</td><td>5478.03</td><td>0.00</td><td>428.7</td><td>5477.99</td><td>0.00</td><td>5477.99</td></tr><tr><td>10</td><td>8213.51</td><td>9.15</td><td>11.0</td><td>7548.02</td><td>0.31</td><td>130.0</td><td>7525.02</td><td>0.00</td><td>7200.0</td><td>7526.81</td><td>0.03</td><td>725.4</td><td>7525.61</td><td>0.01</td><td>7524.83</td></tr><tr><td>15</td><td>8469.11</td><td>7.79</td><td>27.2</td><td>7891.16</td><td>0.44</td><td>220.5</td><td>7863.14</td><td>0.08</td><td>7200.0</td><td>7869.35</td><td>0.16</td><td>897.9</td><td>7858.85</td><td>0.03</td><td>7856.69</td></tr><tr><td>20</td><td>10123.49</td><td>6.94</td><td>59.1</td><td>9558.74</td><td>0.97</td><td>641.7</td><td>9506.25</td><td>0.42</td><td>7200.0</td><td>9488.26</td><td>0.23</td><td>1260.5</td><td>9476.98</td><td>0.11</td><td>9466.51</td></tr><tr><td>25</td><td>10648.25</td><td>5.86</td><td>108.4</td><td>10227.55</td><td>1.68</td><td>723.7</td><td>10104.99</td><td>0.46</td><td>7200.0</td><td>10088.21</td><td>0.29</td><td>1525.1</td><td>10064.89</td><td>0.06</td><td>10058.85</td></tr><tr><td>30</td><td>10394.63</td><td>4.84</td><td>153.9</td><td>10222.89</td><td>3.10</td><td>619.1</td><td>9971.14</td><td>0.57</td><td>7200.0</td><td>9933.83</td><td>0.19</td><td>1735.6</td><td>9901.21</td><td>-0.14</td><td>9915.06</td></tr><tr><td>35</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>10915.93</td><td>0.79</td><td>7200.0</td><td>10843.66</td><td>0.12</td><td>1925.4</td><td>10817.43</td><td>-0.12</td><td>10830.43</td></tr><tr><td>40</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>11002.22</td><td>0.27</td><td>7200.0</td><td>10991.20</td><td>0.17</td><td>1985.1</td><td>10951.25</td><td>-0.20</td><td>10972.65</td></tr><tr><td>45</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>11579.88</td><td>0.46</td><td>7200.0</td><td>11544.00</td><td>0.15</td><td>2025.8</td><td>11510.08</td><td>-0.15</td><td>11527.10</td></tr><tr><td>50</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>13511.62</td><td>0.26</td><td>7200.0</td><td>13505.18</td><td>0.21</td><td>2262.0</td><td>13454.90</td><td>-0.16</td><td>13476.69</td></tr><tr><td>Avg</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>9745.82</td><td>0.36</td><td>7200.0</td><td>9726.85</td><td>0.17</td><td>1477.2</td><td>9703.92</td><td>-0.07</td><td>9710.68</td></tr><tr><td rowspan="4">LC</td><td>50</td><td>14336.56</td><td>4.96</td><td>394.5</td><td>14455.92</td><td>5.84</td><td>2589.5</td><td>13694.50</td><td>0.26</td><td>7200.0</td><td>13670.93</td><td>0.09</td><td>4512.1</td><td>13619.39</td><td>-0.29</td><td>13658.58</td></tr><tr><td>100</td><td>17630.85</td><td>4.50</td><td>1823.2</td><td>18421.73</td><td>9.18</td><td>2112.0</td><td>16890.54</td><td>0.11</td><td>7200.0</td><td>16805.40</td><td>-0.40</td><td>6391.5</td><td>16736.78</td><td>-0.80</td><td>16872.38</td></tr><tr><td>200</td><td>25142.35</td><td>4.12</td><td>8310.1</td><td>27786.21</td><td>15.07</td><td>828.3</td><td>24146.93</td><td>0.00</td><td>7200.0</td><td>24216.63</td><td>0.29</td><td>7140.9</td><td>24063.84</td><td>-0.34</td><td>24146.93</td></tr><tr><td>Avg</td><td>19036.59</td><td>4.45</td><td>3509.3</td><td>20221.29</td><td>10.95</td><td>1843.3</td><td>18243.99</td><td>0.10</td><td>7200.0</td><td>18230.99</td><td>0.03</td><td>6014.8</td><td>18140.00</td><td>-0.47</td><td>18225.96</td></tr><tr><td rowspan="4">HC</td><td>50</td><td>31283.24</td><td>2.15</td><td>642.5</td><td>31412.44</td><td>2.57</td><td>3081.1</td><td>30663.33</td><td>0.13</td><td>7200.0</td><td>30649.56</td><td>0.08</td><td>4323.8</td><td>30581.14</td><td>-0.14</td><td>30624.92</td></tr><tr><td>100</td><td>52530.23</td><td>1.30</td><td>2968.6</td><td>53591.81</td><td>3.35</td><td>2360.4</td><td>51865.07</td><td>0.02</td><td>7200.0</td><td>51888.67</td><td>0.06</td><td>5531.8</td><td>51740.12</td><td>-0.22</td><td>51856.76</td></tr><tr><td>200</td><td>96076.10</td><td>0.82</td><td>16435.8</td><td>99209.77</td><td>4.20</td><td>1507.6</td><td>95298.01</td><td>0.00</td><td>7200.0</td><td>95576.34</td><td>0.29</td><td>6927.1</td><td>95358.71</td><td>0.06</td><td>95298.01</td></tr><tr><td>Avg</td><td>59963.19</td><td>1.19</td><td>6682.3</td><td>61434.67</td><td>3.67</td><td>2316.4</td><td>59275.47</td><td>0.03</td><td>7200.0</td><td>59371.52</td><td>0.19</td><td>5594.2</td><td>59226.66</td><td>-0.06</td><td>59259.90</td></tr><tr><td colspan="2">Avg Gap</td><td></td><td colspan="2">2.84</td><td></td><td colspan="2">2.66</td><td></td><td colspan="2">0.17</td><td></td><td colspan="2">-0.15</td><td></td><td></td><td>-0.38</td><td></td></tr><tr><td colspan="2">Avg Time</td><td></td><td></td><td colspan="2">1509.1</td><td></td><td colspan="2">879.7</td><td></td><td colspan="2">7200.0</td><td></td><td colspan="2">1989.4</td><td></td><td></td><td></td></tr></table>

Result 1 HGS-IRP yields 768 best-known solutions, out of which 365 are new best solutions, across 1040 benchmark IRP instances. In detail, for small instances, HGS-IRP identifies 187 new best solutions out of 800 instances. For large instances, HGS-IRP finds 178 new best solutions out of 240 instances. This highlights the efficiency and effectiveness of HGS-IRP, especially in handling larger and more complex datasets, and demonstrates the effectiveness of the proposed DS operator, which is the only operator in charge of optimizing delivery schedules.

Table 2 Comparative analysis on large-scale IRP instances

<table><tr><td rowspan="2">n</td><td colspan="3">Construction</td><td colspan="3">Matheuristic</td><td colspan="4">Branch and Cut</td><td colspan="5">HGS-IRP</td><td rowspan="2">BKS</td></tr><tr><td>UB</td><td>Gap(%)</td><td>T(s)</td><td>UB</td><td>Gap(%)</td><td>T(s)</td><td>LB</td><td>UB</td><td>Gap(%)</td><td>T(s)</td><td>Avg</td><td> $Gap_A$ (%)</td><td>T(s)</td><td>Best</td><td> $Gap_B$ (%)</td></tr><tr><td>10</td><td>7502.74</td><td>40.08</td><td>0.0</td><td>5385.52</td><td>0.55</td><td>1748.8</td><td>5331.14</td><td>5356.03</td><td>0.00</td><td>5422.3</td><td>5369.76</td><td>0.26</td><td>4378.4</td><td>5356.81</td><td>0.01</td><td>5356.03</td></tr><tr><td>25</td><td>19431.74</td><td>40.37</td><td>0.0</td><td>15072.20</td><td>8.88</td><td>1800.0</td><td>13626.19</td><td>13842.88</td><td>0.00</td><td>7199.1</td><td>13886.24</td><td>0.31</td><td>7078.1</td><td>13819.07</td><td>-0.17</td><td>13842.88</td></tr><tr><td>50</td><td>42969.72</td><td>6.84</td><td>0.1</td><td>-</td><td>-</td><td>2400.0</td><td>28862.31</td><td>51389.61</td><td>27.78</td><td>7193.2</td><td>29945.03</td><td>-25.54</td><td>7390.6</td><td>29753.66</td><td>-26.02</td><td>40218.66</td></tr><tr><td>100</td><td>86098.23</td><td>0.38</td><td>0.7</td><td>-</td><td>-</td><td>2400.0</td><td>52307.74</td><td>172930.13</td><td>101.61</td><td>7193.8</td><td>58382.45</td><td>-31.94</td><td>7215.3</td><td>58121.23</td><td>-32.24</td><td>85775.08</td></tr><tr><td>200</td><td>154146.38</td><td>0.00</td><td>6.7</td><td>-</td><td>-</td><td>2400.0</td><td>76747.91</td><td>-</td><td>-</td><td>7217.9</td><td>106730.50</td><td>-30.76</td><td>11139.3</td><td>105188.88</td><td>-31.76</td><td>154146.38</td></tr></table>

Experiments on SAHS instances. We further evaluate HGS-IRP on the challenging IRP instances recently introduced by Skålnes et al. (2024). Table 2 presents the average results across instances of varying sizes. Skålnes et al. (2024) propose three approaches, and we report the corresponding results: (1) Construction heuristic, (2) Matheuristic, (3) Branch-and-Cut. Only the Branch-and-Cut method provides lower bounds (LB), in contrast to the constructive and matheuristic methods, which are primarily designed to generate feasible solutions and, therefore, only provide upper bounds (UB). Finally, BKS reports the best of the feasible solutions found by the three approaches (the minimum value in UB).

Result 2 The computational results demonstrate that, out of a total of 270 benchmark instances, the best-known solution is improved in 191 instances and matched in an additional 25 instances. Notably, within the same 2-hour time limit, substantially better solutions are obtained, yielding an average improvement of 18.21 over all instances compared to the BKS previously reported by Skålnes et al. (2024).

## 6.2. Empirical Behavior of the Number of Pieces in $C _ { t }$

In Section 4.4, we analyzed the theoretical complexity of computing the cost-to-go functions $C _ { t }$ The number of linea pieces in $C _ { t }$ is theoretically bounded by $O ( U _ { i } )$ , and the most expensive operation is the convolution of $C _ { t - 1 }$ and $F _ { t }$ , which takes $O ( U _ { i } K )$ time. When repeating across all H time steps of the dynamic program, the total complexity of evaluating the DS neighborhood for a single retailer becomes $O ( U _ { i } K H )$ . However, in practice, we observe that the number of pieces remains much smaller than this bound.

To evaluate this, we recorded the number of pieces in $C _ { t }$ for several test instances. The results are shown in Figure 6. These results were obtained on an instance from the small instance set, which includes 50 customers and high holding cost. Each day, up to $K = 5$ vehicles are available for deliveries, and the maximum inventory level $U _ { i }$ varies significantly across customers, ranging from 22 to 294. The planning horizon in this instance is H = 10 days. These parameters define the theoretical bounds on the number of linear pieces in $C _ { t } .$ , as discussed in Section 4.4, where the full evaluation of the DS neighborhood for one retailer requires $O ( U _ { i } K H )$ time. We began recording from iteration 1001 to 1020, after running 1000 iterations to allow the population to stabilize. During this period, measurements were taken only after crossover, and the results of the first application of the DS operator were recorded within the DSI loop during the local search. We collected the number of linear pieces in $C _ { t }$ for each of the 50 customers on 20 DSI calls, resulting in 1000 data points per day (50 customers $\times 2 0$ rounds) for the boxplot. We repeated the same procedure on four other instances with varying horizon lengths $( H \in \{ 6 , 1 0 , 1 2 \} )$ , and observed similar trends. Therefore, the behavior shown in Figure 6 shows consistent patterns across different time horizons. Although it may seem surprising at first, the number of pieces initially increases but then stabilizes or even decreases over time, as the algorithm retains only the most promising options and prunes the rest. Moreover, while the upper range tends to grow in later days, the median number of pieces remains low, and reductions are frequently observed. This suggests that the actual computational burden remains well controlled.

![](images/page_22_chart_3.jpg)

Figure 6 Boxplots of the number of pieces in $C _ { t }$ from Day 1 to Day 10. Each box represents the distribution across different instances. The box spans from the 25th to the 75th percentile, with the median shown as a horizontal line.

Two key design mechanisms in our algorithm explain this observation:

1. Range-based pruning: The function $C _ { t } ( I _ { i } ^ { t } )$ models the cost of ending day t with inventory level $I _ { i } ^ { t }$ . As established in Section $4 . 4 ,$ the feasible domain for $I _ { i } ^ { t }$ is $[ 0 , U _ { i } - d _ { i } ^ { t } ]$ , where $U _ { i }$ is the maximum inventory and $d _ { i } ^ { t }$ is the demand on day t. This domain applies to both transitions (17) and (18) in the DP recursion. Before performing convolutions or minimizations, we discard any segments of the piecewise linear functions that fall entirely outside this interval. Additionally, segments that do not cover any integer-valued inventory levels are also removed, as they contain no feasible solutions. These two steps significantly reduce the number of pieces carried forward at each stage.

2. Optimality-based merging: When merging cost functions from different transitions $( \mathbf { e . g . }$ delivery vs. no-delivery, different stock-out levels), we retain only the segment with the lowest cost over each interval. Dominated segments are discarded and they are frequently encountered in Equations (19) and (20). This operation further limits the total number of pieces and avoids redundant computations.

Together, these two mechanisms effectively limit the number of function segments. Despite the theoretical worst-case scenario, the number of linear segments in C<sub>t</sub> remains small over the planning horizon, leading to an efficient approach.

## 6.3. Performance of HGS-IRP on IRP with penalized stock-outs

In the stock-out-allowed setting, no standard benchmark instances are available. Therefore, we evaluate the performance of HGS-IRP on both the small and large benchmark IRP datasets described earlier. Specifically, we test four different values of the stock-out penalty parameter $\rho ;$ 50, 100, 300, and 1,000,000.

Figure 7 illustrates the trade-off observed on a representative instance when varying the penalty parameter $\rho .$ The x-axis shows the stock-out quantity, and the total quantity delivered to retailers is displayed on top of each column. The y-axis represents the sum of the routing and inventory costs, with routing costs shown in black and inventory costs shown as shaded segments. Each bar also reports the total quantity delivered to all customers, which decreases as the stock-out amount increases. The plot shows that lower values of $\rho$ result in higher stock-out quantities and reduced total cost. In particular, routing costs decrease consistently as stock-outs increase, as the algorithm avoids serving some retailers when the penalty is low. This leads to a shorter or less frequent delivery schedule. Conversely, as $\rho$ increases, the algorithm favors full delivery, reducing stock-outs but increasing overall cost due to more extensive routing and higher inventory levels. Note that multiple values of $\rho$ can yield the same best delivery decision. As a result, several distinct $\rho$ values may correspond to a single bar in the figure, with identical stock-out quantities and cost decompositions. It is observed that once $\rho$ exceeds 91, no stock-out events occur. Consequently, for $\rho \geq 9 2$ , all corresponding bars in the figure coincide with the first bar, as increasing the penalty further only reinforces stock-out avoidance but does not change the outcome.

![](images/page_24_chart_2.jpg)

Figure 7 Trade-off between stock-out amount and routing/inventory cost for a specific instance (15 customers and 5 vehicles) under varying stock-out penalties ρ, which varies from 1 to 300 in integer increments.

Table 3 also reports detailed results for all tested instances under the four values of $\rho .$ Instances are grouped by number of retailers, inventory cost type (HC and LC), and time horizon. For each configuration, we present the best solution value, the average solution value over 10 runs, and the corresponding computational time. These results confirm a general trend: higher $\rho$ values typically result in increased total cost and runtime. We additionally report the $\mathrm { g a p }$ (Gap) in average cost across $\rho$ values, using the $\rho = 1,000,000$ case as a benchmark which approximates the no-stock-out case. This highlights the impact of stock-out penalties on the overall cost structure. As expected, higher $\rho$ values yield higher total costs, as the routing plans adjust to avoid larger stock-out penalties. Under the HC (high holding cost) setting, cost differences across $\rho$ are smaller, since high holding and stock-out costs already discourage stock-outs. $\mathrm { B y }$ contrast, in the LC setting, small $\rho$ values produce relatively low routing-cost solutions, as stock-outs remain cheaper than replenishment. Overall, HGS-IRP maintains stable performance across the range of penalty settings, suggesting robustness in handling various stock-out scenarios.

## 7. Conclusions

In this paper, we have introduced a novel large neighborhood search operator for the Inventory Routing Problem (IRP). For any given retailer, the operator removes all visits across the planning horizon and computes an optimized delivery schedule —reselecting visit days and delivery quantities to jointly minimize routing and inventory costs. In contrast to existing search operators, which either apply local changes to the delivery schedule or incur high computational costs when considering broader modifications, this is the first operator specifically designed for the IRP that efficiently optimizes replenishment decisions over the entire planning horizon. The operator also handles stock-outs in a natural way, a feature that has received limited attention in the IRP literature despite being common in practical settings.

Table 3 Best results (Best), average results (Avg), average runtime in seconds (T(s)) on instances of varying sizes for different stock-out penalty settings.

<table><tbody><tr><td rowspan="2">Data Set n</td><td colspan="4">ρ=50</td><td colspan="4">ρ=100</td><td colspan="4">ρ=300</td><td colspan="3">ρ=1,000,000</td></tr><tr><td>Best Best</td><td>T(s)</td><td>Avg Avg</td><td>Gap(%)</td><td>Best Best</td><td>T(s)</td><td>Avg Avg</td><td>Gap(%)</td><td>Best Best</td><td>T(s)</td><td>Avg Avg</td><td>Gap(%)</td><td>Best Best</td><td>A T(s)</td><td>vg Avg</td></tr><tr><td>5</td><td>587.08</td><td>16.9</td><td>587.08</td><td>-71.78</td><td>948.97</td><td>24.8</td><td>948.97</td><td>-54.38</td><td>1674.99</td><td>48.9</td><td>1674.99</td><td>-19.48</td><td>2080.31</td><td>87.1</td><td>2080.31</td></tr><tr><td>10</td><td>1497.86</td><td>44.5</td><td>1497.86</td><td>-50.94</td><td>2264.81</td><td>59.7</td><td>2264.81</td><td>-25.82</td><td>2955.57</td><td>108.0</td><td>2955.57</td><td>-3.20</td><td>3053.13</td><td>139.0</td><td>3053.13</td></tr><tr><td>15</td><td>1921.61</td><td>68.7</td><td>1921.61</td><td>-38.37</td><td>2540.49</td><td>87.7</td><td>2540.49</td><td>-18.52</td><td>3031.66</td><td>130.9</td><td>3031.97</td><td>-2.75</td><td>3117.85</td><td>155.4</td><td>3117.85</td></tr><tr><td>20</td><td>2553.68</td><td>88.6</td><td>2553.68</td><td>-30.75</td><td>3212.50</td><td>121.1</td><td>3212.50</td><td>-12.88</td><td>3611.01</td><td>162.5</td><td>3611.01</td><td>-2.07</td><td>3687.48</td><td>184.5</td><td>3687.49</td></tr><tr><td>25</td><td>3124.38</td><td>115.2</td><td>3126.72</td><td>-20.64</td><td>3643.10</td><td>159.4</td><td>3643.22</td><td>-7.53</td><td>3909.73</td><td>211.2</td><td>3914.53</td><td>-0.64</td><td>3936.38</td><td>215.9</td><td>3939.80</td></tr><tr><td>LC</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>30</td><td>3353.37</td><td>149.2</td><td>3353.42</td><td>-15.05</td><td>3777.17</td><td>198.3</td><td>3777.38</td><td>-4.32</td><td>3920.38</td><td>253.3</td><td>3921.61</td><td>-0.66</td><td>3947.63</td><td>274.8</td><td>3947.74</td></tr><tr><td>H=3</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>35</td><td>3664.29</td><td>163.8</td><td>3668.62</td><td>-12.60</td><td>4088.36</td><td>239.6</td><td>4089.93</td><td>-2.57</td><td>4187.51</td><td>286.1</td><td>4187.64</td><td>-0.24</td><td>4197.61</td><td>297.4</td><td>4197.70</td></tr><tr><td>40</td><td>3782.98</td><td>205.9</td><td>3795.75</td><td>-12.20</td><td>4102.82</td><td>262.3</td><td>4107.49</td><td>-4.99</td><td>4271.98</td><td>339.1</td><td>4272.86</td><td>-1.17</td><td>4315.37</td><td>387.7</td><td>4323.25</td></tr><tr><td>45</td><td>4022.20</td><td>227.4</td><td>4028.15</td><td>-9.97</td><td>4293.90</td><td>293.0</td><td>4299.02</td><td>-3.92</td><td>4458.13</td><td>361.2</td><td>4463.54</td><td>-0.24</td><td>4471.83</td><td>386.8</td><td>4474.28</td></tr><tr><td>50</td><td>4676.77</td><td>262.4</td><td>4684.09</td><td>-10.59</td><td>5020.13</td><td>381.7</td><td>5033.01</td><td>-3.93</td><td>5181.11</td><td>485.6</td><td>5191.22</td><td>-0.91</td><td>5232.76</td><td>539.9</td><td>5239.03</td></tr><tr><td>Avg</td><td>2918.42</td><td>134.2</td><td>2921.70</td><td>-23.24</td><td>3389.23</td><td>182.8</td><td>3391.68</td><td>-10.89</td><td>3720.21</td><td>238.7</td><td>3722.49</td><td>-2.20</td><td>3804.04</td><td>266.8</td><td>3806.06</td></tr><tr><td>5</td><td>2114.42</td><td>84.3</td><td>2114.42</td><td>-64.15</td><td>3318.14</td><td>174.0</td><td>3318.15</td><td>-43.75</td><td>5192.22</td><td>372.3</td><td>5192.30</td><td>-11.98</td><td>5898.73</td><td>621.4</td><td>5898.77</td></tr><tr><td>10</td><td>3944.96</td><td>169.9</td><td>3944.96</td><td>-47.59</td><td>5732.51</td><td>324.8</td><td>5732.56</td><td>-23.84</td><td>7302.65</td><td>797.4</td><td>7304.50</td><td>-2.95</td><td>7524.83</td><td>1016.5</td><td>7526.86</td></tr><tr><td>15</td><td>5469.63</td><td>310.0</td><td>5469.87</td><td>-30.48</td><td>6937.18</td><td>618.4</td><td>6938.69</td><td>-11.82</td><td>7728.22</td><td>1028.9</td><td>7734.11</td><td>-1.71</td><td>7858.97</td><td>1189.9</td><td>7868.57</td></tr><tr><td>20</td><td>7038.84</td><td>470.3</td><td>7040.12</td><td>-25.78</td><td>8654.39</td><td>973.2</td><td>8660.29</td><td>-8.71</td><td>9370.41</td><td>1563.2</td><td>9390.04</td><td>-1.01</td><td>9475.69</td><td>1680.2</td><td>9486.06</td></tr><tr><td>25</td><td>8044.29</td><td>733.5</td><td>8048.87</td><td>-20.23</td><td>9382.32</td><td>1414.2</td><td>9402.07</td><td>-6.82</td><td>9983.37</td><td>1770.7</td><td>10006.16</td><td>-0.84</td><td>10063.19</td><td>1865.5</td><td>10090.52</td></tr><tr><td>LC</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>30</td><td>8635.57</td><td>1187.4</td><td>8644.47</td><td>-13.02</td><td>9628.74</td><td>1707.7</td><td>9646.79</td><td>-2.94</td><td>9902.33</td><td>2046.3</td><td>9932.44</td><td>-0.06</td><td>9910.42</td><td>2072.6</td><td>9938.70</td></tr><tr><td>H=6</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>35</td><td>9594.55</td><td>1470.9</td><td>9617.88</td><td>-11.37</td><td>10512.11</td><td>1937.7</td><td>10541.70</td><td>-2.86</td><td>10813.82</td><td>2142.5</td><td>10841.46</td><td>-0.09</td><td>10819.22</td><td>2182.5</td><td>10851.70</td></tr><tr><td>40</td><td>9695.89</td><td>1640.3</td><td>9750.94</td><td>-11.38</td><td>10597.52</td><td>2053.2</td><td>10634.63</td><td>-3.35</td><td>10940.88</td><td>2202.3</td><td>10988.62</td><td>-0.13</td><td>10953.99</td><td>2225.9</td><td>11003.23</td></tr><tr><td>45</td><td>10441.67</td><td>1951.6</td><td>10466.43</td><td>-9.36</td><td>11176.42</td><td>2138.1</td><td>11209.45</td><td>-2.92</td><td>11500.24</td><td>2248.4</td><td>11542.45</td><td>-0.04</td><td>11509.90</td><td>2262.3</td><td>11547.06</td></tr><tr><td>50</td><td>12418.36</td><td>2141.8</td><td>12474.57</td><td>-7.78</td><td>13171.02</td><td>2279.9</td><td>13224.56</td><td>-2.23</td><td>13420.02</td><td>2366.0</td><td>13484.94</td><td>-0.31</td><td>13460.64</td><td>2368.9</td><td>13526.78</td></tr><tr><td>Avg</td><td>7739.82</td><td>1016.0</td><td>7757.25</td><td>-20.63</td><td>8911.04</td><td>1362.1</td><td>8930.89</td><td>-8.62</td><td>9615.42</td><td>1653.8</td><td>9641.70</td><td>-1.35</td><td>9747.56</td><td>1748.6</td><td>9773.82</td></tr><tr><td>5</td><td>2635.88</td><td>63.7</td><td>2635.88</td><td>-4.55</td><td>2733.03</td><td>81.2</td><td>2733.48</td><td>-1.01</td><td>2754.16</td><td>83.1</td><td>2754.16</td><td>-0.26</td><td>2761.47</td><td>83.7</td><td>2761.47</td></tr><tr><td>10</td><td>4829.84</td><td>125.3</td><td>4830.24</td><td>-0.54</td><td>4846.23</td><td>139.8</td><td>4846.28</td><td>-0.21</td><td>4856.50</td><td>145.6</td><td>4856.56</td><td>0.00</td><td>4856.50</td><td>143.1</td><td>4856.58</td></tr><tr><td>15</td><td>5491.10</td><td>144.4</td><td>5491.72</td><td>-0.71</td><td>5509.68</td><td>159.7</td><td>5509.68</td><td>-0.38</td><td>5524.66</td><td>165.1</td><td>5524.72</td><td>-0.11</td><td>5530.87</td><td>170.2</td><td>5530.88</td></tr><tr><td>20</td><td>7066.76</td><td>170.8</td><td>7067.11</td><td>-0.36</td><td>7082.51</td><td>180.1</td><td>7082.51</td><td>-0.14</td><td>7090.65</td><td>183.2</td><td>7090.65</td><td>-0.03</td><td>7092.57</td><td>181.9</td><td>7092.57</td></tr><tr><td>25</td><td>8421.57</td><td>204.3</td><td>8421.96</td><td>-0.10</td><td>8428.26</td><td>215.7</td><td>8428.45</td><td>-0.02</td><td>8429.46</td><td>228.0</td><td>8429.98</td><td>0.00</td><td>8429.50</td><td>221.9</td><td>8429.97</td></tr><tr><td>HC</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>30</td><td>9656.95</td><td>270.2</td><td>9657.25</td><td>-0.04</td><td>9658.73</td><td>293.2</td><td>9658.84</td><td>-0.02</td><td>9660.57</td><td>301.5</td><td>9660.59</td><td>0.00</td><td>9660.57</td><td>295.7</td><td>9660.69</td></tr><tr><td>H=3</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>35</td><td>10166.57</td><td>348.7</td><td>10167.74</td><td>-0.03</td><td>10167.88</td><td>378.4</td><td>10168.28</td><td>-0.03</td><td>10170.59</td><td>369.8</td><td>10171.19</td><td>0.00</td><td>10170.63</td><td>360.3</td><td>10171.22</td></tr><tr><td>40</td><td>10919.59</td><td>408.2</td><td>10933.05</td><td>-0.17</td><td>10932.19</td><td>438.6</td><td>10952.13</td><td>0.01</td><td>10934.26</td><td>463.1</td><td>10953.13</td><td>0.02</td><td>10935.95</td><td>462.8</td><td>10951.37</td></tr><tr><td>45</td><td>11958.89</td><td>391.3</td><td>11964.93</td><td>-0.04</td><td>11961.90</td><td>419.3</td><td>11965.66</td><td>-0.04</td><td>11966.25</td><td>430.9</td><td>11977.74</td><td>0.06</td><td>11966.17</td><td>420.6</td><td>11970.11</td></tr><tr><td>50</td><td>13519.58</td><td>573.5</td><td>13529.78</td><td>-0.03</td><td>13522.07</td><td>635.8</td><td>13531.65</td><td>-0.02</td><td>13523.54</td><td>639.6</td><td>13530.39</td><td>-0.03</td><td>13523.45</td><td>609.7</td><td>13534.32</td></tr><tr><td>Avg</td><td>8466.67</td><td>270.0</td><td>8469.97</td><td>-0.31</td><td>8484.25</td><td>294.2</td><td>8487.70</td><td>-0.10</td><td>8491.06</td><td>301.0</td><td>8494.91</td><td>-0.01</td><td>8492.77</td><td>295.0</td><td>8495.92</td></tr><tr><td>5</td><td>7313.49</td><td>487.1</td><td>7313.82</td><td>-0.79</td><td>7352.60</td><td>570.9</td><td>7352.92</td><td>-0.26</td><td>7367.91</td><td>643.0</td><td>7368.72</td><td>-0.05</td><td>7371.85</td><td>601.3</td><td>7372.14</td></tr><tr><td>10</td><td>10849.74</td><td>911.9</td><td>10854.04</td><td>-0.80</td><td>10905.93</td><td>1041.9</td><td>10910.54</td><td>-0.28</td><td>10931.97</td><td>1069.5</td><td>10937.92</td><td>-0.03</td><td>10935.99</td><td>1060.2</td><td>10941.57</td></tr><tr><td>15</td><td>13066.26</td><td>1256.9</td><td>13074.88</td><td>-0.32</td><td>13104.46</td><td>1297.8</td><td>13116.45</td><td>-0.01</td><td>13106.68</td><td>1396.8</td><td>13117.23</td><td>0.00</td><td>13106.99</td><td>1323.3</td><td>13117.17</td></tr><tr><td>20</td><td>16307.98</td><td>1634.5</td><td>16321.56</td><td>-0.09</td><td>16319.36</td><td>1692.4</td><td>16335.14</td><td>-0.01</td><td>16321.38</td><td>1736.8</td><td>16336.75</td><td>0.00</td><td>16322.96</td><td>1688.1</td><td>16336.76</td></tr><tr><td>25</td><td>18320.33</td><td>1905.2</td><td>18350.60</td><td>-0.18</td><td>18340.80</td><td>1842.6</td><td>18370.67</td><td>-0.07</td><td>18358.87</td><td>1884.7</td><td>18382.77</td><td>0.00</td><td>18358.73</td><td>1865.3</td><td>18383.15</td></tr><tr><td>HC</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>30</td><td>20810.58</td><td>2016.5</td><td>20835.51</td><td>0.01</td><td>20810.16</td><td>2040.6</td><td>20837.67</td><td>0.02</td><td>20808.01</td><td>2088.0</td><td>20836.47</td><td>0.02</td><td>20805.62</td><td>2028.9</td><td>20833.26</td></tr><tr><td>H=6</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>35</td><td>22607.50</td><td>2103.9</td><td>22643.27</td><td>0.02</td><td>22607.88</td><td>2161.8</td><td>22644.03</td><td>0.02</td><td>22614.14</td><td>2149.1</td><td>22644.51</td><td>0.02</td><td>22606.38</td><td>2072.9</td><td>22639.84</td></tr><tr><td>40</td><td>24146.43</td><td>2029.4</td><td>24203.13</td><td>0.07</td><td>24144.45</td><td>2127.1</td><td>24227.38</td><td>0.17</td><td>24143.91</td><td>2111.3</td><td>24224.99</td><td>0.16</td><td>24147.37</td><td>2179.5</td><td>24186.13</td></tr><tr><td>45</td><td>27129.80</td><td>617.0</td><td>27129.80</td><td>0.22</td><td>27129.80</td><td>617.0</td><td>27129.80</td><td>0.22</td><td>27070.40</td><td>559.0</td><td>27165.30</td><td>0.35</td><td>27036.50</td><td>2400.0</td><td>27071.16</td></tr><tr><td>50</td><td>30397.51</td><td>2282.3</td><td>30491.50</td><td>0.10</td><td>30413.11</td><td>2277.1</td><td>30518.17</td><td>0.19</td><td>30425.21</td><td>2275.0</td><td>30497.33</td><td>0.12</td><td>30405.67</td><td>2361.1</td><td>30460.95</td></tr><tr><td>Avg</td><td>19094.96</td><td>1524.5</td><td>19121.81</td><td>-0.06</td><td>19112.85</td><td>1566.9</td><td>19144.28</td><td>0.05</td><td>19114.85</td><td>1591.3</td><td>19151.20</td><td>0.09</td><td>19109.81</td><td>1758.0</td><td>19134.21</td></tr><tr><td>50</td><td>30615.71</td><td>7200.0</td><td>30697.45</td><td>-0.05</td><td>30619.20</td><td>7200.0</td><td>30696.18</td><td>-0.06</td><td>30618.82</td><td>7200.0</td><td>30699.39</td><td>-0.05</td><td>30629.73</td><td>7200.0</td><td>30713.76</td></tr><tr><td>100</td><td>51806.43</td><td>7200.2</td><td>51970.67</td><td>-0.01</td><td>51806.30</td><td>7200.2</td><td>51959.48</td><td>-0.03</td><td>51803.57</td><td>7200.2</td><td>51953.48</td><td>-0.05</td><td>51803.26</td><td>7200.2</td><td>51976.93</td></tr><tr><td>HC</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>200</td><td>95497.49</td><td>7200.9</td><td>95754.60</td><td>0.00</td><td>95523.94</td><td>7201.0</td><td>95763.75</td><td>0.01</td><td>95534.84</td><td>7201.0</td><td>95753.63</td><td>0.00</td><td>95526.64</td><td>7201.0</td><td>95757.36</td></tr><tr><td>Avg</td><td>59306.54</td><td>7200.4</td><td>59474.24</td><td>-0.01</td><td>59316.48</td><td>7200.4</td><td>59473.14</td><td>-0.02</td><td>59319.08</td><td>7200.4</td><td>59468.83</td><td>-0.02</td><td>59319.88</td><td>7200.4</td><td>59482.68</td></tr><tr><td>50</td><td>12551.19</td><td>7200.0</td><td>12615.56</td><td>-8.06</td><td>13336.96</td><td>7200.0</td><td>13405.90</td><td>-2.30</td><td>13623.71</td><td>7200.0</td><td>13689.28</td><td>-0.23</td><td>13660.14</td><td>7200.0</td><td>13721.51</td></tr><tr><td>100</td><td>16341.00</td><td>7200.1</td><td>16444.51</td><td>-2.51</td><td>16656.30</td><td>7200.2</td><td>16754.31</td><td>-0.68</td><td>16783.32</td><td>7200.2</td><td>16867.82</td><td>0.00</td><td>16787.39</td><td>7200.2</td><td>16868.29</td></tr><tr><td>LC</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>200</td><td>23910.12</td><td>7200.9</td><td>24110.79</td><td>-1.11</td><td>24135.77</td><td>7200.9</td><td>24347.91</td><td>-0.14</td><td>24183.88</td><td>7201.0</td><td>24389.36</td><td>0.03</td><td>24176.11</td><td>7200.9</td><td>24382.03</td></tr><tr><td>Avg</td><td>17600.77</td><td>7200.4</td><td>17723.62</td><td>-3.28</td><td>18043.01</td><td>7200.4</td><td>18169.37</td><td>-0.84</td><td>18196.97</td><td>7200.4</td><td>18315.49</td><td>-0.05</td><td>18207.88</td><td>7200.4</td><td>18323.94</td></tr></tbody></table>

The operator is implemented through a dynamic programming (DP) procedure, using piecewiselinear functions and supported by preprocessing and acceleration techniques to ensure practical efficiency. It is designed to be metaheuristic-independent: it only requires an incumbent solution and can therefore be embedded as a large-scale neighborhood within various frameworks, such as Iterated Local Search (ILS), adaptive Large Neighborhood Search (LNS), or other metaheuristics. As demonstrated in our experiments, this design enables the calculation of reinsertion schedules within microseconds, making it useful for systematic solution refinement within metaheuristics. We integrated the operator into the Hybrid Genetic Search (HGS) framework, where it serves as the sole component responsible for modifying delivery schedules and quantities. The resulting HGS-IRP algorithm achieves state-of-the-art performance: it discovers new best-known solutions for 365 out of 1,040 benchmark instances and improves the best feasible solutions for 191 out of 270 challenging larger-scale IRP instances introduced in 2023.

The research perspectives stemming from this work are numerous. While the integration of the DS operator into HGS already yields good performance, the operator itself is generic and can be embedded into other methods more specifically tailored to the IRP. Moreover, it could be extended to richer IRP variants, such as those with time windows, heterogeneous fleets, multiple depots, or to the production routing problem, by adapting the eva luation function to incorporate the corresponding constraints and cost components. Moreover, this search strategy could be adapted to other deterministic IRP variants, as well as to more complex settings such as two-stage stochastic IRPs and dynamic IRPs, which are increasingly relevant in real-world applications. In these contexts, the operator could be adapted to solve sample average approximation-based deterministic approximations of stochastic problems, either as a standalone approach within a rolling horizon framework or as a generator of solutions for training imitation learning models, such as the one developed in Greif et (2024).

## Acknowledgments

The authors thank the three anonymous reviewers whose comments helped to improve and clarify this manuscript. They also thank Dr. Khalid Laaziri for his assistance in IT-related matters, including but not limited to resolving server issues and problems with Python and Matplotlib, and Dr. Brett Kraabel for help with writing. This work was supported by SCALE-AI through its Research Chairs program, the National Natural Science Foundation of China (72571234), and the SRIBD Grant (J00220250002).

## Declaration of Interest Statement

The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper.

## References

Abdelmaguid, T.F., M.M. Dessouky. 2006. A genetic algorithm approach to the integrated inventory distribution problem. International Journal of Production Research 44(21) 4445–4464.

Adulyasak, Y., J. Cordeau, R. Jans. 2014a. Formulations and branch-and-cut algorithms for multivehicle production and inventory routing problems. INFORMS Journal on Computing 26(1) 103–120.

Adulyasak, Y., J. Cordeau, R. Jans. 2014b. Optimization-based adaptive large neighborhood search for the production routing problem. Transportation Science 48(1) 20–45.

Ahuja, R.K., O. Ergun, J.B. Orlin, A.P. Punnen. 2002. A survey of very large-scale neighborhood search ¨ techniques. Discrete Applied Mathematics 123(1-3) 75–102.

Alvarez, A., P. Munari, R. Morabito. 2018. Iterated local search and simulated annealing algorithms for the inventory routing problem. International Transactions in Operational Research 25(6) 1785–1809.

Andersson, H., A. Hoff, M. Christiansen, G. Hasle, A. Løkketangen. 2010. Industrial aspects and literature survey: Combined inventory management and routing. Computers & operations research 37(9) 1515–1536.

Applegate, D., R.E. Bixby, V. Chvátal, W. Cook. 2003. A new bound on the traveling salesman problem. SIAM Journal on Computing 32(1) 1–8.

Archetti, C., L. Bertazzi, A. Hertz, M.G. Speranza. 2012. A hybrid heuristic for an inventory routing problem. INFORMS Journal on Computing 24(1) 101–116.

Archetti, C., L. Bertazzi, G. Laporte, M.G. Speranza. 2007. A branch-and-cut algorithm for a vendormanaged inventory-routing problem. Transportation science 41(3) 382–391.

Archetti, C., N. Bianchessi, S. Irnich, M. G. Speranza. 2014. Formulations for an inventory routing problem. International Transactions in Operational Research 21(3) 353–374.

Archetti, C., N. Boland, M. Grazia Speranza. 2017. A matheuristic for the multivehicle inventory routing problem. INFORMS Journal on Computing 29(3) 377–387.

Archetti, C., G. Guastaroba, D.L. Huerta-Muñoz, M.G. Speranza. 2021. A kernel search heuristic for the multivehicle inventory routing problem. International Transactions in Operational Research 28(6) 2984–3013.

Archetti, C., I. Ljubić. 2022. Comparison of formulations for the inventory routing problem. European Journal of Operational Research 303(3) 997–1008.

Balas, E., N. Simonetti. 2001. Linear time dynamic-programming algorithms for new classes of restricted TSPs: A computational study. INFORMS Journal on Computing 13(1) 56–75.

Bauschke, H.H., P.L. Combettes. 2017. Infimal Convolution. Springer International Publishing, Cham, 203–217.

Bell, W.J., L.M. Dalberto, M.L. Fisher, A.J. Greenfield, R. Jaikumar, P. Kedia, R.G. Mack, P.J. Prutzman. 1983. Improving the distribution of industrial gases with an on-line computerized routing and scheduling optimizer. Interfaces 13(6) 4–23.

Bouvier, L., G. Dalle, A. Parmentier, T. Vidal. 2024a. Solving a continent-scale inventory routing problem at renault. Transportation Science 58(1) 131–151.

Bouvier, L., G. Dalle, A. Parmentier, T. Vidal. 2024b. Solving a continent-scale inventory routing problem at Renault. Transportation Science 58(1) 131–151.

Campbell, A.M., M.W. Savelsbergh. 2004. A decomposition approach for the inventory-routing problem. Transportation science 38(4) 488–502.

Capua, R., Y. Frota, L.S. Ochi, T. Vidal. 2018. A study on exponential-size neighborhoods for the bin packing problem with conflicts. Journal of Heuristics 24(4) 667–695.

Carter, M.W., J.M. Farvolden, G. Laporte, J. Xu. 1996. Solving an integrated logistics problem arising in grocery distribution. INFOR: Information Systems and Operational Research 34(4) 290–306.

Chitsaz, M., J. Cordeau, R. Jans. 2019. A unified decomposition matheuristic for assembly, production, and inventory routing. INFORMS Journal on Computing 31(1) 134–152.

Christiaens, J., G. Vanden Berghe. 2020. Slack induction by string removals for vehicle routing problems. Transportation Science 54(2) 417–433.

Christiansen, M. 1999. Decomposition of a combined inventory and time constrained ship routing problem. Transportation science 33(1) 3–16.

Coelho, L., J. Cordeau, G. Laporte. . Thirty years of inventory routing. Transportation Science 48(1) 1–19.

Coelho, L. C., A. De Maio, D. Laganà. 2020. A variable mip neighborhood descent for the multi-attribute inventory routing problem. Transportation Research Part E: Logistics and Transportation Review 144 102137.

Coelho, L. C., G. Laporte. 2013a. A branch-and-cut algorithm for the multi-product multi-vehicle inventoryrouting problem. International Journal of Production Research 51(23-24) 7156–7169.

Coelho, L. C., G. Laporte. 2013b. The exact solution of several classes of inventory-routing problems. Computers & Operations Research 40(2) 558–565.

Coelho, L. C., G. Laporte. 2014. Improved solutions for inventory-routing problems through valid inequalities and input ordering. International Journal of Production Economics 155 391 – 397.

Coelho, L.C., J. Cordeau, G. Laporte. 2012. The inventory-routing problem with transshipment. Computers & Operations Research 39(11) 2537–2548.

Desaulniers, G., J. G. Rakke, L. C. Coelho. 2016. A branch-price-and-cut algorithm for the inventory routing problem. Transportation Science 50(3) 1060–1076.

Dinh, N. M., C. Archetti, L. Bertazzi. 2025. Matheuristic algorithms for the inventory routing problem with unsplit and split deliveries. Networks .

Diniz, P., R. Martinelli, M. Poggi. 2020. An efficient matheuristic for the inventory routing problem. Combinatorial Optimization: 6th International Symposium, ISCO 2020, Montreal, QC, Canada, May 4–6, 2020, Revised Selected Papers 6 . Springer, 273–285.

Feng, Yuqiang, Ada Che, Jieyu Lei. 2025. Bi-objective inventory routing problem with uncertain demand: a data-driven robust optimisation approach. International Journal of Production Research 63(11) 3885–3912.

Gaur, V., M.L. Fisher. 2004. A periodic inventory routing problem at a supermarket chain. Operations Research 52(6) 813–822.

Greif, T., L. Bouvier, C.M. Flath, A. Parmentier, S.U. Rohmer, T. Vidal. 2024. Combinatorial optimization and machine learning for dynamic inventory routing. arXiv preprint arXiv:2402.04463 .

Guimarães, T.A., L.C. Coelho, C.M. Schenekemberg, C.T. Scarpin. 2019. The two-echelon multi-depot inventory-routing problem. Computers & Operations Research 101 220–233.

Gunawan, A., F.Y. Vincent, A.T. Widjaja, P. Vansteenwegen. 2019. Simulated annealing for the multi-vehicle cyclic inventory routing problem. 2019 IEEE 15th International Conference on Automation Science and Engineering (CASE). IEEE, 691–696.

Hendel, G. 2022. Adaptive large neighborhood search for mixed integer programming. Mathematical Programming Computation 14(2) 185–221.

Kool, W., L. Bliek, D. Numeroso, Zhang, T. Catshoek, K. Tierney, T. Vidal, J. Gromicho. 2022. The EURO Meets NeurIPS 2022 vehicle routing competition. Proceedings of the NeurIPS 2022 Competitions Track, PMLR, vol. 220. 35–49.

Larrain, Homero, Leandro C Coelho, Alejandro Cataldo. 2017. A variable mip neighborhood descent algorithm for managing inventory and distribution of cash in automated teller machines. Computers & Operations Research 85 22–31.

Lin, S., B. Kernighan. 1973. An effective heuristic algorithm for the traveling salesman problem. Operations Research 21(2) 498–516.

Mahjoob, M., S.S. Fazeli, S. Milanlouei, L.S. Tavassoli, M. Mirmozaffari. 2022. A modified adaptive genetic algorithm for multi-product multi-period inventory routing problem. Sustainable Operations and Computers 3 1–9.

Ohmori, S., K. Yoshimoto. 2021. Multi-product multi-vehicle inventory routing problem with vehicle compatibility and site dependency: A case study in the restaurant chain industry. Uncertain Supply Chain Management 9(2) 351–362.

Pacheco, T., R. Martinelli, A. Subramanian, T.A. Toffolo, T. Vidal. 2023. Exponential-size neighborhoods for the pickup-and-delivery traveling salesman problem. Transportation Science 57(2) 463–481.

Prins, C. 2004. A simple and effective evolutionary algorithm for the vehicle routing problem. Computers & Operations Research 31(12) 1985–2002.

Ropke, S., D. Pisinger. 2006. An adaptive large neighborhood search heuristic for the pickup and delivery problem with time windows. Transportation science 40(4) 455–472.

Rusdiansyah, A., D. Tsao. 2005. An integrated model of the periodic delivery problems for vending-machine supply chains. Journal of Food Engineering 70(3) 421–434.

Skålnes, J., M.B. Ahmed, L.M. Hvattum, M. Stålhane. 2024. New benchmark instances for the inventory routing problem. European Journal of Operational Research 313(3) 992–1014.

Skålnes, J., S.T. Vadseth, H. Andersson, M. Stålhane. 2023. A branch-and-cut embedded matheuristic for the inventory routing problem. Computers & Operations Research 159 106353.

Thompson, P.M., H.N. Psaraftis. 1993. Cyclic transfer algorithms for multi-vehicle routing and scheduling problems. Operations Research 41(5) 935–946.

Toffolo, T.A.M., T. Vidal, T. Wauters. 2019. Heuristics for vehicle routing problems: Sequence or set optimization? Computers & Operations Research 105 118–131.

Toth, P., A. Tramontani. 2008. An integer linear programming local search for capacitated vehicle routing problems. B.L. Golden, S. Raghavan, E.A. Wasil, eds., The Vehicle Routing Problem: Latest Advances and New Challenges. Springer, New York, 275–295.

Vidal, T. 2016. Technical note: Split algorithm in O(n) for the capacitated vehicle routing problem. Computers & Operations Research 69 40–47.

Vidal, T. 2017. Node, edge, arc routing and turn penalties: Multiple problems – One neighborhood extension. Operations Research 65(4) 992–1010.

Vidal, T. 2022. Hybrid genetic search for the CVRP: Open-source implementation and SWAP\* neighborhood. Computers & Operations Research 140 105643.

Vidal, T., T.G. Crainic, M. Gendreau, N. Lahrichi, W. Rei. 2012. A hybrid genetic algorithm for multidepot and periodic vehicle routing problems. Operations Research 60(3) 611–624.

Vidal, T., T.G. Crainic, M. Gendreau, C. Prins. 2013. A hybrid genetic algorithm with adaptive diversity management for a large class of vehicle routing problems with time-windows. Computers & operations research 40(1) 475–489.

Vidal, T., T.G. Crainic, M. Gendreau, C. Prins. 2014. A unified solution framework for multi-attribute vehicle routing problems. European Journal of Operational Research 234(3) 658–673.

Vidal, T., G. Laporte, P. Matl. 2020. A concise guide to existing and emerging vehicle routing problem variants. European Journal of Operational Research 286 401–416.

Vincent, F Yu, Nabila Yuraisyah Salsabila, Aldy Gunawan, Nurhadi Siswanto. 2025. A three-stage matheuristic for the blood stochastic inventory routing problem. Transportation Research Part E: Logistics and Transportation Review 200 104143.

Vincent, F.Y., A.T. Widjaja, A. Gunawan, P. Vansteenwegen. 2021. The multi-vehicle cyclic inventory routing problem: Formulation and a metaheuristic approach. Computers & Industrial Engineering 157 107320.

## Appendix A: Considering Possible Backorders

The IRP formulation considered in this paper assumes lost sales: that is, unmet demand in a given period is not carried over and instead incurs an immediate penalty cost. This reflects many real-world applications, such as retail, vending machines, or seasonal products, where backlogging is either impractical or undesirable. Nevertheless, from an algorithmic perspective, supporting backorders requires only minimal modifications to the DS operator and no modification of HGS. In particular, this requires enlarging the DP state space and adapting the cost-update function.

State Space. In the current model, the inventory level at the start of each period $I _ { i } ^ { t }$ is restricted to the range $[ 0 , U _ { i } ]$ , where $U _ { i }$ is the retailer’s capacity. To allow backorders, this domain should be expanded to $[ - B _ { \mathrm { m a x } } , U _ { i } ]$ , where $B _ { \mathrm { m a x } }$ is the maximum backlog allowed for retailer i (e.g., the sum of all demands). This change increases the number of DP states and thus raises the computational complexity of the operator from $O ( U _ { i } K H )$ to $O ( ( U _ { i } + B _ { \operatorname* { m a x } } ) K H )$ per retailer.

Cost Function Modification. The rest of the DP structure, including the transition functions $f _ { 1 }$ and $f _ { 2 } ,$ remains unchanged. The only modification occurs in the final cost function update, where the stockout penalty is replaced by a per-period backlog cost. Specifically, we define:

$$
C _ {t} (I _ {i} ^ {t}) = \hat {C} _ {t} (I _ {i} ^ {t}) + p _ {i} \cdot \max (0, - I _ {i} ^ {t}),\tag{22}
$$

where $p _ { i }$ is the backlog penalty per unit per day for retailer $i ,$ and $\hat { C } _ { t }$ is the continuation cost computed recursively. The term max $\iota ( 0 , - I _ { i } ^ { t } )$ captures the amount of backlog at the start of period t.

Backtracking. In the backtracking phase, the delivery quantity $q _ { i } ^ { t }$ must satisfy both the current demand and any carried-over backlog. If $\underline { { I _ { i } ^ { t - 1 } } } \gtrless \underline { { 0 } } ,$ the algorithm will naturally allocate enough delivery in period t to reduce or clear the backlog. This behavior is seamlessly supported by the modified state space and cost function, requiring no further structural change. This simple extension allows the DS operator to balance routing, inventory holding, and backlog costs, making it applicable to contexts where backorders are acceptable or even necessary.