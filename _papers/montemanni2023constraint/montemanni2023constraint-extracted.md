# Constraint Programming models for the parallel drone scheduling vehicle routing problem

**Roberto Montemanni**<sup>∗</sup>**, Mauro Dell’Amico**

Department of Sciences and Methods for Engineering, University of Modena and Reggio Emilia, Via Amendola 2, 42122 Reggio Emilia, Italy

## Abstract

**Drones are currently seen as a viable way for improving the distribution of parcels in urban and rural environments, while working in coordination with traditional vehicles like trucks. In this paper we consider the parallel drone scheduling vehicle routing problem, where the service of a set of customers requiring a delivery is split between a fleet of trucks and a fleet of drones. We consider two variations of the problem. In the first one the problem is more theoretical, and the target is the minimization of the time required to complete the service and have all the vehicles back to the depot. In the second variant more realistic constraints involving operating costs, capacity limitation and workload balance, are considered, and the target is to minimize the total operational costs. We propose several constraint programming models to deal with the two problems. An experimental champaign on the instances previously adopted in the literature is presented to validate the new solving methods. The results show that on top of being a viable way to solve problems to optimality, the models can also be used to derive effective heuristic solutions and highquality lower bounds for the optimal cost, if the execution is interrupted after its natural end.**

Keywords: **Parallel Drone Scheduling Vehicle Routing Problems, Constraint Programming, Drones, Optimization**

## 1. Introduction

**In the last few years, drone technology has seen investments for billion of dollars, due to its potentials. Forbes [4] defined such a phenomenon the “Drone Explosion”. Drones can be applied to many sectors, among which logistics, surveillance and disaster relief [13]. The most prominent application is probably logistics related to e-commerce, which has experienced an exponential growing** **in the last decades (Statista, [18]). In [19], the authors forecast that autonomous vehicles will deliver about 80% of all parcels in the following ten years. Several advantages associated with the use of aerial drones can be identified: they do not have to stick to the road network but can fly approximately straight line. Moreover, they are not affected by road traffic congestions. The technology might lead to innovative solutions of interest for the companies (operational costs reduction), for the customers (faster deliveries) and for the whole society (sustainability). In this work we will focus on operational delivery strategies with a mixed fleet using both trucks and drones.**

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">∗Corresponding author</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">Email addresses: roberto.montemanni@unimore.it (Roberto Montemanni), mauro.dellamico@unimore.it (Mauro Dell’Amico)</span></small>

**The seminal work of Murray and Chu [10] pioneered a new routing problem in which a truck and a drone collaborate to make deliveries. From an operations research perspective, the authors present two new prototypical variants expanding from the traditional Traveling Salesman Problem (TSP) called the Flying Sidekick TSP (FSTSP) and the Parallel Drone Scheduling TSP (PDSTSP). In both cases a truck and drones collaborate to deliver parcels, the difference being however that in the former model drones can be launched and collected from the truck during its tour, while in the latter one drones are operated directly from the central depot, while the truck executes a traditional delivery tour. In the remainder of the paper we will focus on the latter problem, addressing the interested reader, for example, to [2] for full details and some solution strategies for the FSTSP.**

**More formally, in the PDSTSP there is a truck that can leave the depot, serve a set of customers, and return to the depot, and a set of drones, each of which in the meantime can leave the depot, serve a customer, and return to the depot before serving other customers. Not all the customer can be served by the drones, either due to their location or the characteristic of their parcel. The objective of the problem is to minimize the completion time of the last vehicle returning to the depot (or a cost function related to this), while serving all the customers.**

**A first Mixed Integer Linear Programming (MILP) model for the PDSTSP and some simple heuristic methods are proposed in [10]. A more refined mixed integer programming model and the first metaheuristic method, based on a two steps strategy, embedding a dynamic programming-based component, are discussed in [6]. A similar two steps approach, but based on matheuristics concepts is presented in [1]. A hybrid ant colony optimization metaheuristic is discussed in [3]. In [8] a constraint programming approach is discussed, which is able to solve to optimality all the benchmark instances previously adopted in the literature for both exact and heuristic methods. An improved variable neighbour search metaheuristic is discussed in [5]. More recently, in [12] another exact approach based on branch-and-cut was proposed, together with some new benchmark problems.**

**Several PDSTSP variants are also introduced and studied in the literature. We refer the interested reader to [13] and [14] for a complete survey. In the following we review only the extensions of the original problem relevant to the present study, where multiple trucks are employed out of a same depot, and more realistic constraints involving load balancing, capacity and costs are eventually** **considered.**

**The recent work [7] discusses the** Parallel Drone Scheduling Multiple Traveling Salesman Problem **what we will here refer to as the MT-PDSVRP (** Min-Time Parallel Drone Scheduling Vehicle Routing Problem**), which is a straightforward extension of the PDSTSP where multiple trucks are employed and the target is to minimize the time required to complete the delivery to the last customer serviced and go back to the depot. The authors propose a hybrid metaheuristic algorithm along the line of the method previously introduced in [6], a mixed integer linear model and a branch-and-cut approach working on such a model. What is basically the same problem is also introduced at the same time in [16], where the authors propose three mixed integer linear programming models, one of which is arc-based and the other two are set covering-based, together with a branch-and-price approach based on one of the set covering-based models. A heuristic version of the branch-and-cut method is also discussed, targeting larger instances. A more realistic variation of the PDSTSP, which we will refer to as the MC-PDSVRP (**Min-Cost Parallel Drone Scheduling Vehicle Routing Problem**) is introduced in [11]. In this version of the problem concepts such as capacity, load balancing and decoupling of costs and times are taken into account. A formal definition of the problem will be provided in Section 3. The authors propose a mixed integer linear programming model and a ruin&recreate metaheuristic for the problem.**

**In this paper we aim to explore the potential of constraint programming on PDSVRPs, in the hope of exploiting the recent advances of solvers in dealing with TSP and VRP problems and we present tailored models for the different PDSVRP considered. Experimental results show that several best-known upper and lower bounds can be obtained by the new models.**

**The rest of the paper is organized as follows. Section 2 is devoted to the the MT-PDSTSP. The problem is formally defined and two Constraint Programming models are presented. Symmetrically, in Section 3 the MC-PDSVRP is discussed, again presenting Constraint Programming models. Experimental results for both the models are discussed in Section 4, while Section 5 contains some conclusions and ideas for future work.**

## 2. The Min-Time Parallel Drone Scheduling Vehicle Routing Problem

**The MT-PDSVRP can be represented on a complete directed graph** $G \; = \; ( V , A )$ **, where the node set** $V = \{ 0 , 1 , . . . , n \}$ **represents the depot (node 0) and a set of customers** $C = \{ 1 , . . . , n \}$ **to be serviced. A set T of homogeneous trucks and a set D of homogeneous drones are available to deliver parcels to the customers. Each truck starts from the depot 0, visits a subset of the customers, and returns back to the depot, operating a single route. The drones operate back and forth trips from the depot to customers, delivering one parcel per trip and operating multiple routes if necessary. Not all the customers can be served by a drone, due to the weight of the parcel, an excessive distance of the customer location from the depot, or eventual terrain obstacles such as hills or areas with** high-rise buildings. Let $C ^ { D } \subseteq C$ **d**enotes the set of customers that can be served **by drones. These customers are referred to as** drone-eligible **in the remainder of the paper. The travel time incurred by a truck to go from node i to node j is** denoted as $t _ { i j } ^ { T } ,$ **while the time required by a drone to serve a customer i (back** and forth) is denoted as $t _ { i } ^ { U }$ **. The trucks and the drones start from the depot at time 0, and the objective of the MT-PDSVRP is to minimize the time required to complete all the deliveries and to have all the trucks and all the drones back at the depot. Note that since truck and drones work in parallel, the objective function translates into minimizing the time required by the vehicle of the fleet with the longest total operational time.**

**An example of a solution of the MT-PDSVRP for a small instance is provided in Figure 1.**

![](images/page_3_image_2.jpg)

![](images/page_3_image_3.jpg)

Figure 1: An example of an instance is provided on the left; we assume that two trucks and two drones are available (travel times are omitted for the sake of simplicity). A solution of the MT-PDSVRP is provided on the right. The black and blue arcs represent the tour of the two truck. The first visits nodes 2 and 3 before going back to the depot, the second visits nodes 6 and 7 and goes back to the depot. The dashed red arcs depict the missions of the first drone (that serves nodes 1 and 8), while the dashed green arcs depict the missions of the second drone (that serves nodes 4 and 5).

## 2.1. Constraint programming models

**We propose two alternative models that exploit different functions made available by modern Constraint Programming solvers to model the problem. In the first model the truck tours are represented as separated non-overlapping entities, while in the second they are modelled similarly to the classic giant tour representation [9].**

## 2.1.1. MT-3IDX: A model based on separated truck tours

**The variables of the model that will be referred to as MT-3IDX are as follows. The binary variable** $z _ { k i j }$ **, with** $k \in T$ **and** $i , j \in V$ **takes value 1 (or equivalently**

True**) if node i is visited right before node** $j$ **in the tour of truck** $k ,$ **and value 0 (or equivalently** False) otherwise. The binary variable $x _ { d i }$ **,** with $d \in D$ and $i \in C ^ { D }$ takes value 1 is the customer i is visited by the drone $d ,$ **and value 0 otherwise. Finally, the variable α is a continuous variable introduced to implement the min max objective function. The model is as follows.**

$$
M T - 3 I D X: \quad \min \alpha\tag{1}
$$

$$
\text {s.t.} \quad \operatorname{Circuit} (z _ {k i j}; i, j \in V; i \neq 0 \lor j \neq 0)
$$

$$
k \in T\tag{2}
$$

$$
\sum_ {d \in D} x _ {d i} + \sum_ {k \in T} \neg z _ {k i i} = 1
$$

$$
i \in C ^ {D}\tag{3}
$$

$$
\sum_ {k \in T} \sum_ {i i n V} \neg z _ {k i j} = 1
$$

$$
j \in C \setminus C ^ {D}\tag{4}
$$

$$
\alpha \geq \sum_ {i \in V} \sum_ {j \in V, i \neq j} t _ {i j} ^ {T} z _ {k i j}
$$

$$
k \in T\tag{5}
$$

$$
\alpha \geq \sum_ {i \in C ^ {D}} t _ {i} ^ {D} x _ {d i}
$$

$$
d \in D\tag{6}
$$

$$
z _ {k i j} \in \{0; 1 \}
$$

$$
k \in T; i, j \in V\tag{7}
$$

$$
x _ {d i} \in \{0; 1 \}
$$

$$
d \in D, i \in C ^ {D}\tag{8}
$$

**The objective function (1) minimizes** $\alpha ,$ **that will be assigned the time taken by the latest vehicle to complete its tasks. Constrains (2) assures that the z variables associated to each truck k take values in such a way to form a valid tour, eventually with self-loops for the variables associated to customers visited by the drones. This is imposed through the use of the “**Circuit**” statement. In the logic of such a command, if a customer i is not visited by the a truck k then** $z _ { k i i }$ is set to 1. Constrains (3) imposes that if a customer $i \in C ^ { D }$ **is not visited by any truck, then one of the drones in D must visit it. Note that the negation operator** $a _ {  一  }$ **is used, and that if** $z _ { k i i } = 1 \; \forall k \in T$ **, then customer i is not visited** by any truck. Constraints (4) imposes that if a customer $i \in C \setminus C ^ { D }$ **then one truck in** $T$ **must visit it. Inequality (5) constraints α to be at least as large as the length of the tour of each truck. Constrains (6) set α to be at least as large as the time spent by each drone d to execute the tasks assigned to it. Finally, constrains (7) and (8) define the variables domain.**

**This model presents the drawback of having many variables, and these variables also have to be constrained to take mutually-consistent values. This might affect the quality of the lower bounds provided by the relaxations of the model.**

## 2.1.2. MT-2IDX: A model based on a giant truck tour

**In this section we present a model with less variables than that discussed in Section 3.1.1. This is achieved by exploiting the** $^ { \mathrm { { \small ~  ~ } } } M u l t i p l e C i r c u i t$ **statement present in modern Constraint Programming tools [15].**

**The meaning of variables x remain the same as in Section 3.1.1, while z variables are substituted by a new set of variable** $y _ { i j }$ **, with** $i , j \in V$ **, that when** $i \neq j$ **takes value 1 if node i is visited right before node** $j$ **in one of the truck** **tours, and value 0 otherwise. When** $i = j ,   y _ { i i }$ **takes value 1 if node i is visited by a drone, 0 otherwise. A new set of continuous variables** $\gamma _ { i } ,   i \in V$ **i**s introduced **to count the operating time of each truck** $k   \in   T$ **. The resulting model is as follows.**

$$
M T - 2 I D X: \quad \min \alpha\tag{9}
$$

$$
\text {s.t.} \quad \text {MultipleCircuit} (y _ {i j}, i, j \in V; i \neq 0 \lor j \neq 0)\tag{10}
$$

$$
\sum y _ {0 j} \leq | T |\tag{11}
$$

$$
j \in V \backslash \{0 \}
$$

$$
\sum_ {d \in D} x _ {d i} + \neg y _ {i i} = 1
$$

$$
i \in C\tag{12}
$$

$$
\gamma_ {0} = 0\tag{13}
$$

$$
y _ {i j} \implies \gamma_ {j} = \gamma_ {i} + t _ {i j} ^ {T}
$$

$$
i \in V; j \in V \setminus \{0 \}\tag{14}
$$

$$
y _ {i 0} \implies \alpha \geq \gamma_ {i} + t _ {i 0} ^ {T}
$$

$$
i \in V \setminus \{0 \}\tag{15}
$$

$$
\alpha \geq \sum_ {j \in C ^ {D}} t _ {j} ^ {D} x _ {d j}
$$

$$
d \in D\tag{16}
$$

$$
y _ {i j} \in \{0; 1 \}
$$

$$
i, j \in V\tag{17}
$$

$$
x _ {d i} \in \{0; 1 \}
$$

$$
\gamma_ {i} \geq 0
$$

$$
d \in D, i \in C ^ {D}\tag{18}
$$

$$
i \in V\tag{19}
$$

**The objective function (9) minimizes α, that will be assigned the time taken by the latest vehicle to complete its tasks. Constrains (10) assures that the y variables take values in such a way to form a set of valid truck tours, and eventually self-loops for the variables associated to customers visited by the drones. This is imposed through the use of the** $^ { \mathrm { { \small ~  ~ } } } M u l t i p l e C i r c u i t$ **statement. Constrain (12) states that the number of truck tours (outgoing arcs from the** depot 0) is limited to $| T |$ **.** Constrains (11) imposes that if each customer $i \in C$ must be visited either by a truck $( y _ { i i } \; = \; 0 )$ or by one of the drones in D. **Constraint (13) initializes to 0 the time counter at the depot. Constraints (14) increase the operational time of each truck (by setting the time each customer i is visited). Inequalities (15) force α to be at least as large as the last return time of a truck to the depot. Constrains (16) counts the total operating time of each drone d and imposes that α must be greater than it. Finally, constrains (17), (18) and (19) define the domain of the variables.**

**With respect to the model discussed in 3.1.1, MT-2IDX has the advantage of having a few less variables, but on the other hand it requires more complex constraints to account for the length of each single truck tour.**

## 3. The Min-Cost Parallel Drone Scheduling Vehicle Routing Problem

**The MC-PDSVRP is a modification of the MT-PDSVRP described in Section 2, where more realistic components are considered, leading to a model with** **more complex objective function and more constraints.. In particular, the following elements are added to concepts already analyzed for the MT-PDSVRP** and have to be taken into account: A transportation cost $c _ { i j } ^ { T }$ **is incurred by a** truck to travel on the edge $( i , j ) \in E$ , while $c _ { i } ^ { D }$ **is the transportation costs in**curred by each drone to complete a mission to customer $i \in \bar { C ^ { D } }$ **. These costs are used to define a new objective function to be minimized. The delivery request from each customer** $i   \in   C$ **i**s associated with a parcel weight $w _ { i }$ **. Each truck** has to respect some capacity constraints, being limited to transport at most $Q ^ { T }$ units of weight in its route. Finally, there are upper bounds $\tau ^ { \hat { T } }$ and $\tau ^ { D }$ **on the maximum working time for each truck and drone, respectively. Note that these latter constraints are normally used to introduce load-balancing concepts into the optimization.**

## 3.1. Constraint programming models

**Analogously to what seen in Section 2.1 for the MT-PDSVRP, two models will be presented.**

## 3.1.1. MC-3IDX: A model based on separated truck tours

**The variables used in this model are the same used for the model MT-3IDX in Section 2.1.1.**

$$
MC - 3IDX: \quad \min \sum_{k\in T}\sum_{i\in V}\sum_{j\in V,j\neq i}c_{ij}^{T}z_{kij} + \sum_{k\in D}\sum_{i\in V}c_{i}^{D}x_{ki}\tag{20}
$$

$$
\text {s.t.} \quad \operatorname{Circuit} (z _ {k i j}; i, j \in V)
$$

$$
k \in T\tag{21}
$$

$$
\sum_ {d \in D} x _ {d j} + \sum_ {k \in T} \sum_ {i} \neg z _ {k i j} = 1
$$

$$
j \in C ^ {D}\tag{22}
$$

$$
\sum_ {k \in T} \sum_ {\textit {i i n V}} \neg z _ {k i j} = 1
$$

$$
j \in C \setminus C ^ {D}\tag{23}
$$

$$
\sum_ {i \in V} \sum_ {j \in V, i \neq j} t _ {i j} ^ {T} z _ {k i j} \leq \tau^ {T}
$$

$$
k \in T\tag{24}
$$

$$
\sum_ {j \in C ^ {D}} t _ {j} ^ {D} x _ {d j} \leq \tau^ {D}
$$

$$
d \in D\tag{25}
$$

$$
\sum_ {j \in C} w _ {j} z _ {k i j} \leq Q ^ {T}
$$

$$
k \in T\tag{26}
$$

$$
z _ {k i j} \in \{0; 1 \}
$$

$$
k \in T, i, j \in V\tag{27}
$$

$$
x _ {d i} \in \{0; 1 \}
$$

$$
d \in D, i \in C ^ {D}\tag{28}
$$

**The objective function (20) minimizes the total cost, given by sum of the costs of each truck and drone, incurred to service all the customers. Constrains (21) assures that the z variables associated to each truck k take values in such a way to form a valid tour, eventually self-loops for the variables associated to customers visited by the drones. Constraints (22) imposes that if a customer** $i   \in   C ^ { D }$ **is not visited by any truck, then one of the drones in D must visit** it. Constraints (23) imposes that if a customer $i \in C \setminus C ^ { D }$ **then one truck in** $T$ **must visit it. Inequalities (24) make sure that each truck does not exceed its maximum working time. Inequalities (25) are the constraints on maximum working time for the drones. Constraints (26) model the capacity constraints for the trucks. Finally, constraints (27) and (28) define the variables domain.**

## 3.1.2. MC-2IDX: A model based on a giant truck tour

**The variables used in this model are the same used for the model MT-2IDX** in Section 2.1.2, with the addition of the new set of continuous variables $\beta _ { i }$ $i \in V$ which is introduced to count the weight carried by each truck $k \in T$

$$
M C - 2 I D X: \quad \min \sum_ {i \in V} \sum_ {j \in V, j \neq i} c _ {i j} ^ {T} y _ {i j} + \sum_ {d \in D} \sum_ {i \in V} c _ {i} ^ {D} x _ {d i}\tag{29}
$$

$$
\text {MultipleCircuit} (y _ {i j}, i, j \in V; i \neq 0 \lor j \neq 0)\tag{30}
$$

$$
\sum_ {d \in D} x _ {d i} + \neg y _ {i i} = 1
$$

$$
i \in C\tag{31}
$$

$$
\sum_ {j \in V \setminus \{0 \}} y _ {0 j} \leq | T |\tag{32}
$$

$$
\sum t _ {j} ^ {D} x _ {d j} \leq \tau^ {D}
$$

$$
d \in D\tag{33}
$$

$$
j \in C ^ {D}
$$

$$
\beta_ {0} = 0\tag{34}
$$

$$
y _ {i j} \implies \beta_ {j} = \beta_ {i} + w _ {j}
$$

$$
i \in V; j \in V \setminus \{0 \}\tag{35}
$$

$$
\beta_ {i} \leq Q ^ {T}
$$

$$
i \in V \setminus \{0 \}\tag{36}
$$

$$
\gamma_ {0} = 0\tag{37}
$$

$$
y _ {i j} \implies \gamma_ {j} = \gamma_ {i} + t _ {i j} ^ {T}
$$

$$
i \in V; j \in V \setminus \{0 \}\tag{38}
$$

$$
y _ {i 0} \implies \gamma_ {i} + t _ {i 0} ^ {T} \leq \tau^ {T}
$$

$$
i \in V \setminus \{0 \}\tag{39}
$$

$$
y _ {i j} \in \{0; 1 \}
$$

$$
i, j \in V\tag{40}
$$

$$
x _ {d i} \in \{0; 1 \}
$$

$$
d \in D, i \in C ^ {D}\tag{41}
$$

$$
\beta_ {i}, \gamma_ {i} \geq 0
$$

$$
| i \in V |\tag{42}
$$

**The objective function (29) minimizes the total cost, given by sum of the costs of each truck and drone, incurred to service all the customers. Constrains (30) assures that the** $y$ **variables take values in such a way to form a set of valid truck tours, and eventually self-loops for the variables associated to customers visited by the drones. Constrains (31) imposes that if each customer** $i \in C$ **must be visited either by a truck** $( y _ { i i } = 0 )$ **or by one of the drones in D. Constrain (32) states that the number of truck tours (outgoing arcs from the depot 0) is limited to |T |. Constrains (33) limits the total operating time of each drone d** to the maximum allowed value $\tau ^ { D }$ **. Constraint (34) initializes to 0 the weight counter at the depot. Constraints (35) increase the weight transported by each** **truck. Inequalities (36) impose that the incremental weight** $\beta _ { i }$ **at each customer** $i   \in   V$ **can never exceed the maximum capacity** $Q ^ { T }$ **of each truck. Constraint (37) initializes to 0 the time counter at the depot. Constraints (38) increase the operational time of each truck (by setting the time each customer i is visited).** Inequalities (39) impose that the incremental time $\gamma _ { i }$ at each customer $i \in V$ plus the time required to the truck to $\mathbf { g } \mathbf { o }$ **back to the depot, can never exceed** the maximum operating time $\tau ^ { T }$ **of each truck. Finally, constrains (40), (41) and (42) define the variables domain.**

## 4. Computational experiments

**The constraint programming models described in Sections 2 and 3 have been implemented in Python 3.9 and solved via the CP-SAT solver of Google OR-Tools 9.5.2237 [15]. The experiments have been run on a laptop computer equipped with 32 GB of RAM and an Intel Core i7 12700F CPU with 12 cores (8 with a maximum frequency of 4.9 GHz and 4 with a maximum frequency of 3.6 GHz).**

**The outcome of the experimental champaign we run is discussed in the remainder of this section, and is organized according to the different problems attacked. All the tables present the information of the instances and for each method considered the given maximum computation time (in the label of the columns), although the hardware is different in each paper. For each instance/method combination, the cost of the best heuristic solution retrieved, and eventually the lower bound found. A dash means no result was retrieved in the given time (or, for some of the methods we compare with, the experiment was not attempted). Every time one of the new models we propose improve a best-known bound, the relative entry is in bold. Analogously, every time one of the new models we propose does not match or improve a best-known bound, the relative entry is in italic. Finally, proven exact solutions, retrieved by any method, are marked with an asterisk in the tables. All the new best-known solutions retrieved are available upon request to the authors.**

## 4.1. MT-PDSVRP

**The results are subdivided based on the source of the instances in the following subsections.**

## 4.1.1. Instances from Mbiadou Saleu et al. $\slash \gamma$

**A first set of benchmarks for the MT-PDSVRP was created in [7] starting from classic instances for the** Capacitated Vehicle Routing Problem**. A total of 20 instances with a number of customers ranging between 50 and 199 has been obtained. We refer the interested reader to [7] for full details about the elements of the new instances and the complete sources for the instances. The results are summarized in Table 1, where the results are those obtained by a branch and cut (BC) approach running on a MILP model and of the best of nine variations of a hybrid metaheuristc approach (HM). The BC solver is run on a computer** **with an Intel Xeon CPU E5-2670 CPU with 2x8 cores running at 2.6 GHz and 62.5 GB of RAM, with a maximum computation time of 10800 seconds, while the HM variations have been run on a computer with an Intel core i5-6200U CPU running at 2.4 GHz and 8 GB of RAM, with a maximum computation time of 1000 for each variation.**

Table 1: MT-PDSVRP - Instances originated from CVRPLIB in Mbiadou Saleu et al. [7].

<table><tr><td colspan="3">Instances</td><td colspan="3">Mbiadou Saleu et al. [7]</td><td colspan="2">MT-3IDX(10800 sec)</td><td colspan="2">MT-2IDX(10800 sec)</td></tr><tr><td rowspan="2">Name</td><td rowspan="2">|T|</td><td rowspan="2">|D|</td><td colspan="2">BC (10800 sec)</td><td rowspan="2">HM (9x1000 sec)</td><td rowspan="2">UB</td><td rowspan="2">UB</td><td rowspan="2">UB</td><td rowspan="2">UB</td></tr><tr><td>LB</td><td>UB</td></tr><tr><td>CMT1</td><td>3</td><td>2</td><td>145.87</td><td>188.00</td><td>166.00</td><td>158.27</td><td>168.00</td><td>103.25</td><td>174.00</td></tr><tr><td>CMT2</td><td>5</td><td>5</td><td>101.66</td><td>3630.86</td><td>130.23</td><td>108.00</td><td>158.00</td><td>65.33</td><td>144.00</td></tr><tr><td>CMT3</td><td>4</td><td>4</td><td>161.07</td><td>4537.11</td><td>184.00</td><td>165.98</td><td>222.00</td><td>98.07</td><td>210.00</td></tr><tr><td>CMT4</td><td>6</td><td>6</td><td>-</td><td>-</td><td>160.38</td><td>125.39</td><td>288.00</td><td>72.73</td><td>180.00</td></tr><tr><td>CMT5</td><td>9</td><td>8</td><td>-</td><td>-</td><td>138.00</td><td>82.84</td><td>312.00</td><td>55.67</td><td>158.00</td></tr><tr><td>E-n51-k5</td><td>3</td><td>2</td><td>145.87</td><td>188.00</td><td>168.00</td><td>159.34</td><td>166.00</td><td>103.22</td><td>174.00</td></tr><tr><td>E-n76-k8</td><td>4</td><td>4</td><td>127.05</td><td>2975.51</td><td>154.00</td><td>132.49</td><td>180.00</td><td>81.13</td><td>164.00</td></tr><tr><td>E-n101-k8</td><td>4</td><td>4</td><td>161.07</td><td>4537.11</td><td>184.00</td><td>165.64</td><td>244.00</td><td>98.03</td><td>224.00</td></tr><tr><td>M-n151-k12</td><td>6</td><td>6</td><td>-</td><td>-</td><td>154.00</td><td>126.57</td><td>270.00</td><td>72.78</td><td>188.00</td></tr><tr><td>M-n200-k16</td><td>8</td><td>8</td><td>-</td><td>-</td><td>144.00</td><td>95.21</td><td>302.00</td><td>59.19</td><td>166.00</td></tr><tr><td>P-n51-k10</td><td>5</td><td>5</td><td>81.35</td><td>230.00</td><td>111.07</td><td>90.13</td><td>118.00</td><td>52.60</td><td>124.00</td></tr><tr><td>P-n55-k7</td><td>4</td><td>3</td><td>101.49</td><td>308.00</td><td>126.00</td><td>111.00</td><td>136.00</td><td>70.40</td><td>130.00</td></tr><tr><td>P-n60-k10</td><td>5</td><td>5</td><td>84.30</td><td>246.00</td><td>114.00</td><td>95.00</td><td>124.00</td><td>54.89</td><td>120.00</td></tr><tr><td>P-n65-k10</td><td>5</td><td>5</td><td>94.66</td><td>580.00</td><td>126.00</td><td>105.41</td><td>144.00</td><td>61.46</td><td>138.00</td></tr><tr><td>P-n70-k10</td><td>5</td><td>5</td><td>99.42</td><td>3166.25</td><td>128.00</td><td>108.00</td><td>164.00</td><td>64.34</td><td>150.00</td></tr><tr><td>P-n76-k5</td><td>3</td><td>2</td><td>181.36</td><td>280.00</td><td>200.00</td><td>189.91</td><td>206.00</td><td>129.06</td><td>214.00</td></tr><tr><td>P-n101-k4</td><td>2</td><td>2</td><td>321.80</td><td>4725.47</td><td>342.00</td><td>329.90</td><td>340.00</td><td>198.00</td><td>362.00</td></tr><tr><td>X-n110-k13</td><td>7</td><td>6</td><td>-</td><td>-</td><td>1864.00</td><td>1365.68</td><td>2702.00</td><td>766.70</td><td>2048.00</td></tr><tr><td>X-n115-k10</td><td>5</td><td>5</td><td>-</td><td>-</td><td>2258.00</td><td>1850.38</td><td>2920.00</td><td>1031.21</td><td>2488.00</td></tr><tr><td>X-n139-k10</td><td>5</td><td>5</td><td>-</td><td>-</td><td>2492.00</td><td>-</td><td>-</td><td>1118.67</td><td>2744.00</td></tr></table>

**The results presented in Table 1 indicate that the new CP-based approaches are competitive with state-of-the-art results. In particular, new improved lower bounds were provided for all the instances considered, and 2 new best-known heuristic solutions were also retrieved. The comparison between the CP models indicate that the model MT-3IDX discussed in Section 2.1.1, and characterized by the set of variables z with 3 indices, performs better. In particular, it provides substantially tighter lower bounds. However, this model is not capable of handling the last instance, which by its nature allows a large number of possible drone missions, that is in turns reflected on a large number of z variables. In this case the model MT-2IDX, with its smaller memory footprint, is the only viable option to have a good lower bound. It is interesting also to observe that the quality of the heuristic solutions produced by the CP methods is always high, although not always matching the state-of-the-art provided by the nine purely heuristic methods summarized in column HM.**

## 4.1.2. Instances from Raj et al. [16]

**A second set of instances for the MT-PDSTSP was originated from TSPLIB [17] in [16], by defining the missing elements according to what done previously in [6] for the PDSTSP. Only the instances with more than one truck are reported** **here, since those with one truck boil down the problem to a PDSTSP, and all the optimal solutions can be found in [8]. The number of customers range between 48 and 229. Full details about the instances can be found in [16]. Three methods are considered for comparison purposes: an arc-based MILP model; a branch and price (BP) method based on a set covering MILP model, and a mathheuristic method (MH) based on the same latter model. All the experiments for these methods were run on a computer equipped with an Intel i7-6700 CPU (with 8 cores running at 4 GHz) and 16 GB of RAM, with 3600 seconds for MILP and MH, and 2400 seconds for BC. The CP-based solvers we propose are run for a maximum time of 3600 seconds. The results are summarized in Tables 2 and 3.**

Table 2: MT-PDSVRP - Instances with 2 trucks originated from TSPLIB in Raj et al. [16].

<table><tr><td colspan="3">Instances</td><td colspan="3">Raj et al. [16]</td><td colspan="2">MT-3IDX(3600 s)</td><td colspan="2">MT-2IDX(3600 s)</td></tr><tr><td>Name</td><td> $|T|$ </td><td> $|D|$ </td><td>MILP (3600 s)UB</td><td>BP (2400 s)UB</td><td>MH (3600 s)UB</td><td>LB</td><td>UB</td><td>LB</td><td>UB</td></tr><tr><td>att48_0_80</td><td>2</td><td>2</td><td>18206.00</td><td>17032.00</td><td>17056.00</td><td>16940.18</td><td> $16940.18^*$ </td><td>9785.69</td><td>17288.00</td></tr><tr><td>att48_0_80</td><td>2</td><td>4</td><td>16730.00</td><td>16500.00</td><td>16500.00</td><td>16500.00</td><td> $16500.00^*$ </td><td>6562.48</td><td>16564.00</td></tr><tr><td>att48_0_80</td><td>2</td><td>6</td><td>16500.00</td><td>16500.00</td><td>16500.00</td><td>16500.00</td><td> $16500.00^*$ </td><td>4980.66</td><td>16500.00</td></tr><tr><td>berlin52_0_80</td><td>2</td><td>2</td><td>3328.20</td><td>3415.00</td><td>3415.00</td><td>3285.00</td><td> $3285.00^*$ </td><td>2240.63</td><td>3480.00</td></tr><tr><td>berlin52_0_80</td><td>2</td><td>4</td><td> $2995.00^*$ </td><td>2995.00</td><td>2995.00</td><td>2995.00</td><td> $2995.00^*$ </td><td>1498.57</td><td>2995.00</td></tr><tr><td>berlin52_0_80</td><td>2</td><td>6</td><td> $2995.00^*$ </td><td>2995.00</td><td>2995.00</td><td>2995.00</td><td> $2995.00^*$ </td><td>1141.20</td><td>2995.00</td></tr><tr><td>eil101_0_80</td><td>2</td><td>2</td><td>392.00</td><td>316.00</td><td>305.40</td><td>293.00</td><td> $293.00^*$ </td><td>197.44</td><td>331.00</td></tr><tr><td>eil101_0_80</td><td>2</td><td>4</td><td>408.00</td><td>266.80</td><td>253.70</td><td>232.84</td><td>248.00</td><td>131.60</td><td>283.00</td></tr><tr><td>eil101_0_80</td><td>2</td><td>6</td><td>320.00</td><td>219.00</td><td>215.30</td><td>198.00</td><td>212.00</td><td>99.15</td><td>272.00</td></tr><tr><td>gr120_0_80</td><td>2</td><td>2</td><td>1145.00</td><td>806.30</td><td>764.00</td><td>703.50</td><td>735.00</td><td>478.18</td><td>866.00</td></tr><tr><td>gr120_0_80</td><td>2</td><td>4</td><td>1092.00</td><td>676.00</td><td>646.00</td><td>590.54</td><td>676.00</td><td>318.78</td><td>777.00</td></tr><tr><td>gr120_0_80</td><td>2</td><td>6</td><td>1082.00</td><td>769.00</td><td>581.20</td><td>518.00</td><td>549.00</td><td>239.10</td><td>688.00</td></tr><tr><td>pr152_0_80</td><td>2</td><td>2</td><td>122961.00</td><td>55477.00</td><td>48967.00</td><td>38873.80</td><td>41371.00</td><td>18792.17</td><td>46897.00</td></tr><tr><td>pr152_0_80</td><td>2</td><td>4</td><td>-</td><td>54980.00</td><td>52353.00</td><td>33593.10</td><td>41295.58</td><td>12533.75</td><td>44059.00</td></tr><tr><td>pr152_0_80</td><td>2</td><td>6</td><td>-</td><td>50855.40</td><td>50854.40</td><td>31020.74</td><td>37413.00</td><td>9503.63</td><td>43573.00</td></tr><tr><td>gr229_0_80</td><td>2</td><td>2</td><td>-</td><td>1403.70</td><td>1403.70</td><td>881.91</td><td>1064.97</td><td>0.00</td><td>-</td></tr><tr><td>gr229_0_80</td><td>2</td><td>4</td><td>-</td><td>1346.20</td><td>1346.20</td><td>818.33</td><td>1064.97</td><td>0.00</td><td>-</td></tr><tr><td>gr229_0_80</td><td>2</td><td>6</td><td>-</td><td>1327.60</td><td>1327.60</td><td>776.98</td><td>1056.10</td><td>0.00</td><td>-</td></tr></table>

\* Optimality proven.

**The results of Table 2 indicates that the CP model MT-3IDX is very suitable on these instances, being able to provide all the state-of-the-art lower bounds and all the best-known heuristic solutions except one, in both cases with many substantial improvements over previously known best results. It is remarkable also that five instances are closed here for the first time. The performance of the model MT-2IDX appear less brilliant, in particular on the larger instances considered, on which no solution or meaningful bound was produced in the given time.**

**The results of Table 3 confirm the previous impressions. Only, in this case the CP model MT-3IDX otperforms the other methods less strongly. This indicates that its performance degrade when the number of trucks considered increases: On a few instances it found sub-optimal heuristic solutions, although it remarkably provided an optimality proof for the first instance. Note that** **the model MT-2IDX is now able to produce two new state-of-the-art heuristic solutions, indicating that this latter method might be indicated for problems with more trucks available.**

Table 3: MT-PDSVRP - Instances with 3 trucks originated from TSPLIB in Raj et al. [16].

<table><tr><td colspan="3">Instances</td><td colspan="3">Raj et al. [16]</td><td colspan="2">MT-3IDX(3600 s)</td><td colspan="2">MT-2IDX(3600 s)</td></tr><tr><td>Name</td><td>|T|</td><td>|D|</td><td>MILP (3600 s)UB</td><td>BP (2400 s)UB</td><td>MH (3600 s)UB</td><td>LB</td><td>UB</td><td>LB</td><td>UB</td></tr><tr><td>att48_0_80</td><td>3</td><td>2</td><td>19824.00</td><td>15218.00</td><td>14062.00</td><td>13452.00</td><td> $13452.00^*$ </td><td>7811.15</td><td>14652.00</td></tr><tr><td>att48_0_80</td><td>3</td><td>4</td><td>17194.00</td><td>13394.00</td><td>14652.00</td><td>10605.21</td><td>13394.00</td><td>5690.68</td><td>13394.00</td></tr><tr><td>att48_0_80</td><td>3</td><td>6</td><td>16226.00</td><td>13756.00</td><td>13394.00</td><td>10369.78</td><td>13394.00</td><td>4441.85</td><td>13394.00</td></tr><tr><td>berlin52_0_80</td><td>3</td><td>2</td><td>3205.00</td><td>3403.10</td><td>2995.00</td><td>2471.35</td><td>2935.00</td><td>1777.81</td><td>2995.00</td></tr><tr><td>berlin52_0_80</td><td>3</td><td>4</td><td>2665.00</td><td>2635.00</td><td>2625.00</td><td>2013.82</td><td>2625.00</td><td>1285.27</td><td>2925.00</td></tr><tr><td>berlin52_0_80</td><td>3</td><td>6</td><td>2625.00</td><td>2625.00</td><td>2625.00</td><td>2132.20</td><td>2625.00</td><td>1015.52</td><td>2925.00</td></tr><tr><td>eil101_0_80</td><td>3</td><td>2</td><td>-</td><td>260.00</td><td>235.00</td><td>209.00</td><td>252.00</td><td>157.04</td><td>278.00</td></tr><tr><td>eil101_0_80</td><td>3</td><td>4</td><td>-</td><td>221.00</td><td>200.10</td><td>177.00</td><td>198.00</td><td>112.23</td><td>227.00</td></tr><tr><td>eil101_0_80</td><td>3</td><td>6</td><td>-</td><td>228.00</td><td>181.00</td><td>155.20</td><td>218.00</td><td>87.91</td><td>204.00</td></tr><tr><td>gr120_0_80</td><td>3</td><td>2</td><td>-</td><td>611.00</td><td>597.00</td><td>509.50</td><td>688.00</td><td>381.29</td><td>734.00</td></tr><tr><td>gr120_0_80</td><td>3</td><td>4</td><td>-</td><td>536.00</td><td>528.00</td><td>444.00</td><td>688.00</td><td>272.58</td><td>601.00</td></tr><tr><td>gr120_0_80</td><td>3</td><td>6</td><td>-</td><td>590.90</td><td>527.20</td><td>397.50</td><td>526.00</td><td>212.84</td><td>547.00</td></tr><tr><td>pr152_0_80</td><td>3</td><td>2</td><td>-</td><td>48135.00</td><td>48135.00</td><td>25154.41</td><td>38395.00</td><td>15033.25</td><td>36443.00</td></tr><tr><td>pr152_0_80</td><td>3</td><td>4</td><td>-</td><td>43024.00</td><td>43024.00</td><td>21913.95</td><td>36940.00</td><td>10799.23</td><td>37183.00</td></tr><tr><td>pr152_0_80</td><td>3</td><td>6</td><td>-</td><td>46403.00</td><td>46403.00</td><td>20584.69</td><td>36940.00</td><td>8526.30</td><td>36281.00</td></tr><tr><td>gr229_0_80</td><td>3</td><td>2</td><td>-</td><td>1145.40</td><td>1145.40</td><td>579.62</td><td>981.59</td><td>0.00</td><td>-</td></tr><tr><td>gr229_0_80</td><td>3</td><td>4</td><td>-</td><td>1132.30</td><td>1132.30</td><td>561.47</td><td>969.92</td><td>0.00</td><td>-</td></tr><tr><td>gr229_0_80</td><td>3</td><td>6</td><td>-</td><td>1130.00</td><td>1130.00</td><td>517.37</td><td>1004.89</td><td>0.00</td><td>-</td></tr></table>

\* Optimality proven.

## 4.2. MC-PDSVRP

**The instances considered in this section are those originally proposed in Nguyen et al. [11]. They are based on several statistical data shared by logistics service providers and common practices, so although being generated as random, they can be considered as realistic. The numbers of customers considered are 30, 50, 100, 200 and 400 (the first element of the name of each instance reflects this information). We refer the reader to [11] for the full details of the instances ranging from the number of trucks and drones, to loading capacities, speeds, battery endurance for the drones, etc.**

**The results of our experiments are summarized in Tables 4, 5, 6, 7 and 8, divided according the size of the instances. On top of the CP models discussed in Section 3.1, that are run for a maximum of 1800 seconds, the methods considered in the comparison are those presented in [11], namely a MILP model and** Ruin and Recreate **heuristic algorithm (RR). The experiments for the latter methods were run on a computer equipped with an AMD Ryzen 3700X CPU running at 4.0 GHz and 16 GB of RAM, with a time limit of 3600 seconds. Note that the RR method was run 30 times, and the best result is reported here.**

**The results reported in Tables 4 and 5 suggest that the MILP model is the most viable method to solve these small problems with 30 and 50 customers: several instances are solved to optimality within the given time. However, on** **some of the instances with 50 customers, MILP is not able to provide any solution. The RR heuristic also obtains remarkably good results, always matching or improving the best known figures. We believe that taking the best of 30 runs was an important factor in these results, because this allows a good random exploration of the search space. The CP models perform reasonably well on these instances in terms of heuristic solution found, and are able to provide good lower bounds (no lower bound was provided in previous publications). It is worth noticing that the model MC-2IDX seems to perform better than MC-3 IDX on these** Minimum Cost **instances, especially on the instances with 50 customers. This revert what was observed in Section 4.1 for the** Minimum Time **instances, and can be explained by the completely different objective function between the two problems considered, and their general characteristics.**

Table 4: MC-PDSVRP - Instances with 30 customers from Nguyen et al. [11].

<table><tr><td rowspan="2">Instances</td><td colspan="2">Nguyen et al. [11]</td><td colspan="2">MC-3IDX(1800 sec)</td><td colspan="2">MC-2IDX(1800 sec)</td></tr><tr><td>MILP (3600 sec)UB</td><td>RR (30x3600 sec)UB</td><td>LB</td><td>UB</td><td>LB</td><td>UB</td></tr><tr><td>30-r-0-c</td><td>128.67*</td><td>128.67</td><td>101.69</td><td>128.67</td><td>103.11</td><td>128.67</td></tr><tr><td>30-r-0-e</td><td>300.85</td><td>300.85</td><td>104.85</td><td>300.85</td><td>150.61</td><td>300.85</td></tr><tr><td>30-r-0-r</td><td>199.76</td><td>199.76</td><td>110.71</td><td>199.76</td><td>125.00</td><td>199.76</td></tr><tr><td>30-r-1-c</td><td>58.30*</td><td>58.30</td><td>58.30</td><td>58.30*</td><td>58.30</td><td>58.30*</td></tr><tr><td>30-r-1-e</td><td>243.11</td><td>243.11</td><td>117.48</td><td>243.11</td><td>148.43</td><td>243.11</td></tr><tr><td>30-r-1-r</td><td>164.75</td><td>164.75</td><td>106.82</td><td>164.75</td><td>116.50</td><td>164.75</td></tr><tr><td>30-r-2-c</td><td>91.57*</td><td>91.57</td><td>69.04</td><td>91.57</td><td>80.43</td><td>91.57</td></tr><tr><td>30-r-2-e</td><td>235.25</td><td>235.25</td><td>111.62</td><td>235.25</td><td>151.10</td><td>235.25</td></tr><tr><td>30-r-2-r</td><td>211.26</td><td>211.26</td><td>101.11</td><td>211.26</td><td>135.88</td><td>211.26</td></tr><tr><td>30-c-0-c</td><td>82.15*</td><td>82.15</td><td>60.08</td><td>82.15</td><td>82.15</td><td>82.15*</td></tr><tr><td>30-c-0-e</td><td>150.44*</td><td>150.44</td><td>103.78</td><td>150.44</td><td>110.23</td><td>150.44</td></tr><tr><td>30-c-0-r</td><td>112.72*</td><td>112.72</td><td>83.08</td><td>112.72</td><td>91.44</td><td>112.72</td></tr><tr><td>30-c-1-c</td><td>39.98*</td><td>39.98</td><td>39.98</td><td>39.98*</td><td>39.98</td><td>39.98*</td></tr><tr><td>30-c-1-e</td><td>172.49</td><td>172.49</td><td>97.03</td><td>172.49</td><td>83.94</td><td>172.49</td></tr><tr><td>30-c-1-r</td><td>61.28*</td><td>61.28</td><td>61.28</td><td>61.28*</td><td>61.28</td><td>61.28*</td></tr><tr><td>30-c-2-c</td><td>77.00*</td><td>77.00</td><td>77.00</td><td>77.00*</td><td>77.00</td><td>77.00*</td></tr><tr><td>30-c-2-e</td><td>166.82</td><td>166.82</td><td>98.49</td><td>166.82</td><td>95.89</td><td>166.82</td></tr><tr><td>30-c-2-r</td><td>88.81*</td><td>88.81</td><td>59.65</td><td>88.81</td><td>80.22</td><td>88.81</td></tr><tr><td>30-rc-0-c</td><td>81.06*</td><td>81.06</td><td>81.06</td><td>81.06*</td><td>74.47</td><td>81.06</td></tr><tr><td>30-rc-0-e</td><td>181.89</td><td>181.89</td><td>111.08</td><td>181.89</td><td>115.78</td><td>181.89</td></tr><tr><td>30-rc-0-r</td><td>146.73</td><td>146.73</td><td>88.40</td><td>146.73</td><td>98.85</td><td>146.73</td></tr><tr><td>30-rc-1-c</td><td>56.48*</td><td>56.48</td><td>56.48</td><td>56.48*</td><td>56.48</td><td>56.48*</td></tr><tr><td>30-rc-1-e</td><td>176.57</td><td>176.57</td><td>115.70</td><td>176.57</td><td>118.09</td><td>176.57</td></tr><tr><td>30-rc-1-r</td><td>97.91*</td><td>97.91</td><td>97.91</td><td>97.91*</td><td>71.96</td><td>97.91</td></tr><tr><td>30-rc-2-c</td><td>77.00*</td><td>77.00</td><td>63.74</td><td>77.00</td><td>77.00</td><td>77.00*</td></tr><tr><td>30-rc-2-e</td><td>187.18</td><td>187.18</td><td>71.50</td><td>187.18</td><td>104.96</td><td>187.18</td></tr><tr><td>30-rc-2-r</td><td>94.21*</td><td>94.21</td><td>77.67</td><td>94.21</td><td>86.67</td><td>94.21</td></tr></table>

\* Optimality proven.

**The results summarized in Tables 6, 7 and 8 do not include the results of the MILP model, since these larger instances with 100, 200 and 400 customers were out of reach for it. The RR heuristic produce good quality solutions, as we are able to certify here with the first lower bounds ever produced on these instances. On the other hand, the relatively small gaps between upper and lower bounds**

Table 5: MC-PDSVRP - Instances with 50 customers from Nguyen et al. [11].

<table><tr><td rowspan="2">Instances</td><td colspan="2">Nguyen et al. [11]</td><td colspan="2">MC-3IDX(1800 sec)</td><td colspan="2">MC-2IDX(1800 sec)</td></tr><tr><td>MILP (3600 sec)UB</td><td>RR (30x3600 sec)UB</td><td>LB</td><td>UB</td><td>LB</td><td>UB</td></tr><tr><td>50-r-0-c</td><td>161.13*</td><td>161.13</td><td>110.62</td><td>161.13</td><td>131.27</td><td>161.56</td></tr><tr><td>50-r-0-e</td><td>-</td><td>310.50</td><td>129.68</td><td>310.50</td><td>151.57</td><td>310.50</td></tr><tr><td>50-r-0-r</td><td>-</td><td>246.53</td><td>110.02</td><td>246.53</td><td>137.85</td><td>246.53</td></tr><tr><td>50-r-1-c</td><td>177.21</td><td>177.21</td><td>103.69</td><td>177.21</td><td>135.27</td><td>177.21</td></tr><tr><td>50-r-1-e</td><td>216.97</td><td>216.97</td><td>129.97</td><td>216.97</td><td>153.12</td><td>216.97</td></tr><tr><td>50-r-1-r</td><td>-</td><td>228.11</td><td>116.45</td><td>228.11</td><td>148.57</td><td>228.11</td></tr><tr><td>50-r-2-c</td><td>182.09</td><td>181.49</td><td>108.59</td><td>182.62</td><td>145.83</td><td>182.62</td></tr><tr><td>50-r-2-e</td><td>-</td><td>375.05</td><td>127.88</td><td>375.05</td><td>153.27</td><td>375.05</td></tr><tr><td>50-r-2-r</td><td>-</td><td>313.32</td><td>109.95</td><td>313.32</td><td>162.11</td><td>313.32</td></tr><tr><td>50-c-0-c</td><td>89.04</td><td>89.04</td><td>47.73</td><td>89.04</td><td>78.64</td><td>89.04</td></tr><tr><td>50-c-0-e</td><td>183.26</td><td>182.91</td><td>78.01</td><td>182.91</td><td>105.82</td><td>182.91</td></tr><tr><td>50-c-0-r</td><td>112.17</td><td>112.17</td><td>85.09</td><td>112.17</td><td>89.09</td><td>112.17</td></tr><tr><td>50-c-1-c</td><td>81.76*</td><td>81.76</td><td>39.38</td><td>81.76</td><td>75.97</td><td>81.76</td></tr><tr><td>50-c-1-e</td><td>133.57</td><td>133.57</td><td>81.44</td><td>133.57</td><td>92.35</td><td>133.57</td></tr><tr><td>50-c-1-r</td><td>149.24</td><td>148.86</td><td>56.78</td><td>149.06</td><td>83.95</td><td>149.06</td></tr><tr><td>50-c-2-c</td><td>77.16*</td><td>77.16</td><td>54.26</td><td>77.16</td><td>75.31</td><td>77.16</td></tr><tr><td>50-c-2-e</td><td>214.25</td><td>214.25</td><td>74.24</td><td>214.66</td><td>112.86</td><td>214.66</td></tr><tr><td>50-c-2-r</td><td>136.60</td><td>136.51</td><td>67.30</td><td>136.51</td><td>90.66</td><td>136.51</td></tr><tr><td>50-rc-0-c</td><td>116.80*</td><td>116.80</td><td>70.01</td><td>116.80</td><td>107.92</td><td>116.80</td></tr><tr><td>50-rc-0-e</td><td>-</td><td>242.02</td><td>74.24</td><td>242.02</td><td>124.28</td><td>242.02</td></tr><tr><td>50-rc-0-r</td><td>217.87</td><td>217.87</td><td>95.88</td><td>217.87</td><td>109.28</td><td>217.87</td></tr><tr><td>50-rc-1-c</td><td>110.44*</td><td>110.44</td><td>82.98</td><td>110.44</td><td>104.16</td><td>110.44</td></tr><tr><td>50-rc-1-e</td><td>201.62</td><td>201.62</td><td>112.97</td><td>201.62</td><td>124.27</td><td>201.62</td></tr><tr><td>50-rc-1-r</td><td>173.16</td><td>173.16</td><td>90.57</td><td>173.61</td><td>116.16</td><td>173.61</td></tr><tr><td>50-rc-2-c</td><td>129.82</td><td>129.65</td><td>64.33</td><td>129.82</td><td>104.74</td><td>129.65</td></tr><tr><td>50-rc-2-e</td><td>-</td><td>383.49</td><td>109.51</td><td>383.49</td><td>129.50</td><td>383.49</td></tr><tr><td>50-rc-2-r</td><td>197.20</td><td>186.31</td><td>108.11</td><td>196.97</td><td>108.82</td><td>186.31</td></tr></table>

\* Optimality proven.

Table 6: MC-PDSVRP - Instances with 100 customers from Nguyen et al. [11].

<table><tr><td rowspan="2">Instances</td><td colspan="2">Nguyen et al. [11]</td><td colspan="2">MC-3IDX(1800 sec)</td><td colspan="2">MC-2IDX(1800 sec)</td></tr><tr><td>MILP (3600 sec)UB</td><td>RR (30x3600 sec)UB</td><td>LB</td><td>UB</td><td>LB</td><td>UB</td></tr><tr><td>100-r-0-c</td><td>-</td><td>272.77</td><td>143.76</td><td>-</td><td>222.27</td><td>277.90</td></tr><tr><td>100-r-0-e</td><td>-</td><td>506.07</td><td>206.21</td><td>-</td><td>250.30</td><td>-</td></tr><tr><td>100-r-0-r</td><td>-</td><td>325.29</td><td>140.62</td><td>-</td><td>226.44</td><td>-</td></tr><tr><td>100-r-1-c</td><td>-</td><td>302.46</td><td>167.13</td><td>-</td><td>240.03</td><td>-</td></tr><tr><td>100-r-1-e</td><td>-</td><td>470.06</td><td>198.41</td><td>-</td><td>251.18</td><td>-</td></tr><tr><td>100-r-1-r</td><td>-</td><td>350.97</td><td>179.63</td><td>-</td><td>230.43</td><td>-</td></tr><tr><td>100-r-2-c</td><td>-</td><td>284.77</td><td>169.39</td><td>288.00</td><td>232.12</td><td>-</td></tr><tr><td>100-r-2-e</td><td>-</td><td>435.91</td><td>208.16</td><td>-</td><td>265.24</td><td>-</td></tr><tr><td>100-r-2-r</td><td>-</td><td>320.98</td><td>162.92</td><td>361.47</td><td>226.69</td><td>-</td></tr><tr><td>100-c-0-c</td><td>-</td><td>218.59</td><td>92.16</td><td>221.59</td><td>170.73</td><td>-</td></tr><tr><td>100-c-0-e</td><td>-</td><td>315.84</td><td>93.02</td><td>-</td><td>175.48</td><td>-</td></tr><tr><td>100-c-0-r</td><td>-</td><td>252.39</td><td>81.02</td><td>276.95</td><td>161.81</td><td>-</td></tr><tr><td>100-c-1-c</td><td>-</td><td>154.61</td><td>87.41</td><td>179.75</td><td>112.94</td><td>-</td></tr><tr><td>100-c-1-e</td><td>-</td><td>222.15</td><td>103.33</td><td>236.44</td><td>119.22</td><td>-</td></tr><tr><td>100-c-1-r</td><td>-</td><td>110.95</td><td>64.71</td><td>110.95</td><td>98.77</td><td>110.95</td></tr><tr><td>100-c-2-c</td><td>-</td><td>108.35</td><td>73.34</td><td>108.35</td><td>95.81</td><td>-</td></tr><tr><td>100-c-2-e</td><td>-</td><td>118.71</td><td>70.71</td><td>132.28</td><td>103.69</td><td>-</td></tr><tr><td>100-c-2-r</td><td>-</td><td>86.28</td><td>49.08</td><td>102.47</td><td>86.00</td><td>88.01</td></tr><tr><td>100-rc-0-c</td><td>-</td><td>252.37</td><td>128.09</td><td>254.03</td><td>199.69</td><td>-</td></tr><tr><td>100-rc-0-e</td><td>-</td><td>472.95</td><td>168.08</td><td>-</td><td>233.41</td><td>-</td></tr><tr><td>100-rc-0-r</td><td>-</td><td>337.61</td><td>157.65</td><td>339.09</td><td>205.28</td><td>-</td></tr><tr><td>100-rc-1-c</td><td>-</td><td>276.78</td><td>152.69</td><td>305.51</td><td>209.72</td><td>-</td></tr><tr><td>100-rc-1-e</td><td>-</td><td>432.44</td><td>190.81</td><td>490.66</td><td>246.80</td><td>-</td></tr><tr><td>100-rc-1-r</td><td>-</td><td>423.33</td><td>163.48</td><td>426.76</td><td>220.13</td><td>-</td></tr><tr><td>100-rc-2-c</td><td>-</td><td>260.45</td><td>125.31</td><td>286.73</td><td>198.66</td><td>-</td></tr><tr><td>100-rc-2-e</td><td>-</td><td>358.24</td><td>174.37</td><td>406.12</td><td>228.51</td><td>-</td></tr><tr><td>100-rc-2-r</td><td>-</td><td>331.97</td><td>138.87</td><td>345.25</td><td>207.27</td><td>-</td></tr></table>

**on some of the instances, also suggest that the quality provided by the CP models are good. In details, MC-2IDX scales up very well while MC-3IDX is not able to produce significant bounds, due to the very large number of z variables necessary to model the problem. Unfortunately these good performance of the model MC-2IDX in terms of lower bounds does not get reflected on the quality of the heuristic solutions: very often the method is not capable of producing any feasible solution at all in the given computation time.**

## 5. Conclusions

**In this paper we have discussed some different Constraint Programming models to describe two versions of the Parallel Drone Scheduling Vehicle Routing Problem that were recently proposed in the literature.**

**Experimental results suggest that solving these models can lead to many improved state-of-the-art results. In particular, the new models seem to provide the new reference for producing high quality lower bounds on the optimal solution costs, but they are also able to produce several new best-known heuristic solutions, and even to close for the first time several of the instances considered.**

Table 7: MC-PDSVRP - Instances with 200 customers from Nguyen et al. [11].

<table><tr><td rowspan="2">Instances</td><td colspan="2">Nguyen et al. [11]</td><td colspan="2">MC-3IDX(1800 sec)</td><td colspan="2">MC-2IDX(1800 sec)</td></tr><tr><td>MILP (3600 sec)UB</td><td>RR (30x3600 sec)UB</td><td>LB</td><td>UB</td><td>LB</td><td>UB</td></tr><tr><td>200-r-0-c</td><td>-</td><td>430.42</td><td>134.99</td><td>-</td><td>353.51</td><td>-</td></tr><tr><td>200-r-0-e</td><td>-</td><td>728.00</td><td>0.00</td><td>-</td><td>368.88</td><td>-</td></tr><tr><td>200-r-0-r</td><td>-</td><td>528.29</td><td>102.71</td><td>-</td><td>355.73</td><td>-</td></tr><tr><td>200-r-1-c</td><td>-</td><td>434.66</td><td>228.69</td><td>-</td><td>348.04</td><td>-</td></tr><tr><td>200-r-1-e</td><td>-</td><td>601.06</td><td>0.13</td><td>-</td><td>369.88</td><td>-</td></tr><tr><td>200-r-1-r</td><td>-</td><td>481.83</td><td>128.30</td><td>-</td><td>349.86</td><td>-</td></tr><tr><td>200-r-2-c</td><td>-</td><td>446.15</td><td>0.00</td><td>-</td><td>357.04</td><td>-</td></tr><tr><td>200-r-2-e</td><td>-</td><td>606.05</td><td>0.00</td><td>-</td><td>374.19</td><td>-</td></tr><tr><td>200-r-2-r</td><td>-</td><td>497.72</td><td>0.00</td><td>-</td><td>350.49</td><td>-</td></tr><tr><td>200-c-0-c</td><td>-</td><td>234.40</td><td>0.00</td><td>-</td><td>184.05</td><td>-</td></tr><tr><td>200-c-0-e</td><td>-</td><td>442.74</td><td>0.00</td><td>-</td><td>189.35</td><td>-</td></tr><tr><td>200-c-0-r</td><td>-</td><td>270.76</td><td>0.00</td><td>-</td><td>173.94</td><td>-</td></tr><tr><td>200-c-1-c</td><td>-</td><td>225.55</td><td>78.21</td><td>-</td><td>186.77</td><td>-</td></tr><tr><td>200-c-1-e</td><td>-</td><td>461.57</td><td>0.00</td><td>-</td><td>211.23</td><td>-</td></tr><tr><td>200-c-1-r</td><td>-</td><td>239.91</td><td>0.00</td><td>-</td><td>198.22</td><td>-</td></tr><tr><td>200-c-2-c</td><td>-</td><td>263.26</td><td>0.00</td><td>-</td><td>193.47</td><td>-</td></tr><tr><td>200-c-2-e</td><td>-</td><td>486.05</td><td>0.00</td><td>-</td><td>212.55</td><td>-</td></tr><tr><td>200-c-2-r</td><td>-</td><td>322.61</td><td>0.00</td><td>-</td><td>189.90</td><td>-</td></tr><tr><td>200-rc-0-c</td><td>-</td><td>354.23</td><td>0.00</td><td>-</td><td>280.87</td><td>-</td></tr><tr><td>200-rc-0-e</td><td>-</td><td>575.94</td><td>0.00</td><td>-</td><td>297.83</td><td>-</td></tr><tr><td>200-rc-0-r</td><td>-</td><td>484.66</td><td>0.00</td><td>-</td><td>293.68</td><td>-</td></tr><tr><td>200-rc-1-c</td><td>-</td><td>370.01</td><td>0.00</td><td>-</td><td>280.68</td><td>-</td></tr><tr><td>200-rc-1-e</td><td>-</td><td>591.58</td><td>0.00</td><td>-</td><td>296.25</td><td>-</td></tr><tr><td>200-rc-1-r</td><td>-</td><td>411.34</td><td>0.00</td><td>-</td><td>267.01</td><td>-</td></tr><tr><td>200-rc-2-c</td><td>-</td><td>372.30</td><td>0.00</td><td>-</td><td>299.35</td><td>-</td></tr><tr><td>200-rc-2-e</td><td>-</td><td>534.45</td><td>0.00</td><td>-</td><td>330.13</td><td>-</td></tr><tr><td>200-rc-2-r</td><td>-</td><td>432.17</td><td>0.00</td><td>-</td><td>299.16</td><td>-</td></tr></table>

**In our opinion the flourishing literature on specialization of Parallel Drone Scheduling Vehicle Routing Problems, aiming at introducing more and more realistic aspects could be greatly benefit from our contributions, given the high flexibility provided by Constraint Programming, and the assumption that the results we have obtained here could be replicated. This is material for future work.**

## Acknowledgements

The authors are grateful to Prof. Hoàng Ha Minh for the useful discussions **and suggestions.**

## Declaration of competing interest

**The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper.**

Table 8: MC-PDSVRP - Instances with 400 customers from Nguyen et al. [11].

<table><tr><td rowspan="2">Instances</td><td colspan="2">Nguyen et al. [11]</td><td colspan="2">MC-3IDX(1800 sec)</td><td colspan="2">MC-2IDX(1800 sec)</td></tr><tr><td>MILP (3600 sec)UB</td><td>RR (30x3600 sec)UB</td><td>LB</td><td>UB</td><td>LB</td><td>UB</td></tr><tr><td>400-r-0-c</td><td>-</td><td>604.94</td><td>0.00</td><td>-</td><td>500.91</td><td>-</td></tr><tr><td>400-r-0-e</td><td>-</td><td>801.45</td><td>0.00</td><td>-</td><td>518.74</td><td>-</td></tr><tr><td>400-r-0-r</td><td>-</td><td>626.46</td><td>0.00</td><td>-</td><td>518.62</td><td>-</td></tr><tr><td>400-r-1-c</td><td>-</td><td>578.77</td><td>0.00</td><td>-</td><td>487.76</td><td>-</td></tr><tr><td>400-r-1-e</td><td>-</td><td>772.30</td><td>0.00</td><td>-</td><td>445.80</td><td>-</td></tr><tr><td>400-r-1-r</td><td>-</td><td>584.07</td><td>0.00</td><td>-</td><td>477.13</td><td>-</td></tr><tr><td>400-r-2-c</td><td>-</td><td>587.88</td><td>0.00</td><td>-</td><td>483.98</td><td>-</td></tr><tr><td>400-r-2-e</td><td>-</td><td>771.16</td><td>0.00</td><td>-</td><td>510.02</td><td>-</td></tr><tr><td>400-r-2-r</td><td>-</td><td>692.91</td><td>0.00</td><td>-</td><td>454.20</td><td>-</td></tr><tr><td>400-c-0-c</td><td>-</td><td>271.82</td><td>0.00</td><td>-</td><td>207.27</td><td>-</td></tr><tr><td>400-c-0-e</td><td>-</td><td>378.98</td><td>0.00</td><td>-</td><td>253.55</td><td>-</td></tr><tr><td>400-c-0-r</td><td>-</td><td>403.85</td><td>0.00</td><td>-</td><td>248.69</td><td>-</td></tr><tr><td>400-c-1-c</td><td>-</td><td>187.20</td><td>0.00</td><td>-</td><td>136.34</td><td>-</td></tr><tr><td>400-c-1-e</td><td>-</td><td>249.01</td><td>0.00</td><td>-</td><td>142.46</td><td>-</td></tr><tr><td>400-c-1-r</td><td>-</td><td>219.23</td><td>0.00</td><td>-</td><td>146.12</td><td>-</td></tr><tr><td>400-c-2-c</td><td>-</td><td>152.79</td><td>0.00</td><td>-</td><td>141.57</td><td>-</td></tr><tr><td>400-c-2-e</td><td>-</td><td>245.54</td><td>0.00</td><td>-</td><td>145.22</td><td>-</td></tr><tr><td>400-c-2-r</td><td>-</td><td>231.89</td><td>0.00</td><td>-</td><td>154.86</td><td>-</td></tr><tr><td>400-rc-0-c</td><td>-</td><td>497.90</td><td>0.00</td><td>-</td><td>420.36</td><td>-</td></tr><tr><td>400-rc-0-e</td><td>-</td><td>700.96</td><td>0.00</td><td>-</td><td>456.69</td><td>-</td></tr><tr><td>400-rc-0-r</td><td>-</td><td>604.38</td><td>0.00</td><td>-</td><td>437.29</td><td>-</td></tr><tr><td>400-rc-1-c</td><td>-</td><td>518.40</td><td>0.00</td><td>-</td><td>395.26</td><td>-</td></tr><tr><td>400-rc-1-e</td><td>-</td><td>784.02</td><td>0.00</td><td>-</td><td>424.46</td><td>-</td></tr><tr><td>400-rc-1-r</td><td>-</td><td>531.44</td><td>0.00</td><td>-</td><td>396.43</td><td>-</td></tr><tr><td>400-rc-2-c</td><td>-</td><td>510.64</td><td>0.00</td><td>-</td><td>424.09</td><td>-</td></tr><tr><td>400-rc-2-e</td><td>-</td><td>723.63</td><td>0.00</td><td>-</td><td>449.39</td><td>-</td></tr><tr><td>400-rc-2-r</td><td>-</td><td>625.31</td><td>0.00</td><td>-</td><td>448.43</td><td>-</td></tr></table>

## References

[1] M. Dell’Amico, R. Montemanni, and S. Novellani. Matheuristic algorithms for the parallel drone scheduling traveling salesman problem. Annals of Operations Research, 289:211–226, 2020.

[2] M. Dell’Amico, R. Montemanni, and S. Novellani. Algorithms based on branch and bound for the flying sidekick traveling salesman problem. Omega, 104:102493, 2021.

[3] Q. T. Dinh, D. D. Do, and M. H. Há. Ants can solve the parallel drone scheduling traveling salesman problem. In Proceedings of the Genetic and Evolutionary Computation Conference (GECCO), pages 14–21, 2021.

[4] Forbes. Drone explosion: \$5B investment in 2 years, 129 startups, 170 new craft. [https://www.forbes.com/sites/johnkoetsier/2022/02/07/drone-innovation-check-up-5b-inves](https://www.forbes.com/sites/johnkoetsier/2022/02/07/drone-innovation-check-up-5b-investment-129-companies-170-craft/)2022. [Accessed: 2023-02-05].

[5] D. Lei and X. Chen. An improved variable neighborhood search for parallel drone scheduling traveling salesman problem. Applied Soft Computing, 127:109416, 2022.

[6] R. G. Mbiadou Saleu, D. Deroussi, L. qnd Feillet, N. Grangeon, and A. Quilliot. An iterative two-step heuristic for the parallel drone scheduling traveling salesman problem. Networks, 72(4):459–474, 2018.

[7] R. G. Mbiadou Saleu, D. Deroussi, L. qnd Feillet, N. Grangeon, and A. Quilliot. The parallel drone scheduling problem with multiple drones and vehicles. European Journal of Operational Research, 300:571–589, 2022.

[8] R. Montemanni and M. Dell’Amico. Solving the parallel drone scheduling traveling salesman problem via constraint programming. Algorithms, 16(1):40, 2023.

[9] R. Montemanni and L.M. Gambardella. An ant colony system for team orienteering problems with time windows. Foundations of Computing and Decision Sciences, 34(4):287–306, 2009.

[10] C. C. Murray and A. G. Chu. The flying sidekick traveling salesman problem: Optimization of drone-assisted parcel delivery. Transportation Research Part C: Emerging Technologies, 54:86–109, 2015.

[11] M. A. Nguyen, G. T.-H. Dang, M. H. Há, and M.-T. Pham. The min-cost parallel drone scheduling vehicle routing problem. European Journal of Operational Research, 299:910–930, 2022.

[12] M. A. Nguyen, H. L. Luong, M. H. Hà, and H. B. Ban. An efficient branchand-cut algorithm for the parallel drone scheduling traveling salesman problem. 4OR, 2022.

[13] A. Otto, N. Agatz, J. Campbell, B. Golden, and E. Pesch. Optimization approaches for civil applications of unmanned aerial vehicles (uavs) or aerial drones: A survey. Networks, 72(4):411–458, 2018.

[14] J. Pasha, Z. Elmi, S. Purkayastha, A. M. Fathollahi-Fard, Y.-E. Ge, Y.-Y. Lau, and M. A. Dulebenets. The drone scheduling problem: A systematic state-of-the-art review. IEEE Transactions on Intelligent Transportation Systems, 23(9):14224–14247, 2022.

[15] L. Perron and V. Furnon. Google OR-Tools, 2023. https://developers.google.com/optimization/ [Accessed: 2023-03-03].

[16] R. Raj, D. Lee, S. Lee, J. Walteros, and C. Murray. A Branch-and-Price Approach for the Parallel Drone Scheduling Vehicle Routing Problem. SSRN Electronic Journal, 2021.

[17] G. Reinelt. TSPLIB – A Traveling Salesman Problem Library. ORSA Journal on Computing, 3(4):376–384, 1991.

[18] Statista. E-commerce. [https://www.statista.com/markets/413/e-commerce/](https://www.statista.com/markets/413/e-commerce/),2022. [Accessed: 2023-02-05].

[19] R. Wolleswinkel, V. Lukic, W. Jap, R. Chan, J. Govers, and S. Banerjee. An onslaught of new rivals in parcel and express, volume Travel, Transport and Logistics. Boston Consulting Group, 2018.