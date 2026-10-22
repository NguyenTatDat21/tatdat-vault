# On the Min-cost Traveling Salesman Problem with Drone

Quang Minh Ha

quang.ha@uclouvain.be

ICTEAM, Université catholique de Louvain, Belgium

Yves Deville

yves.deville@uclouvain.be

ICTEAM, Université catholique de Louvain, Belgium

Quang Dung Pham

dungpq@soict.hust.edu.vn

SoICT, Hanoi University of Science and Technology, Vietnam

Minh Hoàng Hà

minhhoang.ha@vnu.edu.vn

University of Engineering and Technology, Vietnam National University, Vietnam

## Abstract

Over the past few years, unmanned aerial vehicles (UAV), also known as drones, have been adopted as part of a new logistic method in the commercial sector called "last-mile delivery". In this novel approach, they are deployed alongside trucks to deliver goods to customers to improve the quality of service and reduce the transportation cost. This approach gives rise to a new variant of the traveling salesman problem (TSP), called TSP with drone (TSP-D). A variant of this problem that aims to minimize the time at which truck and drone finish the service (or, in other words, to maximize the quality of service) was studied in the work of Murray and Chu (2015). In contrast, this paper considers a new variant of TSP-D in which the objective is to minimize operational costs including total transportation cost and one created by waste time a vehicle has to wait for the other. The problem is first formulated mathematically. Then, two algorithms are proposed for the solution. The first algorithm (TSP-LS) was adapted from the approach proposed by Murray and Chu (2015), in which an optimal TSP solution is converted to a feasible TSP-D solution by local searches. The second algorithm, a Greedy Randomized Adaptive Search Procedure (GRASP), is based on a new split procedure that optimally splits any TSP tour into a TSP-D solution. After a TSP-D solution has been generated, it is then improved through local search operators. Numerical results obtained on various instances of both objective functions with different sizes and characteristics are presented. The results show that GRASP outperforms TSP-LS in terms of solution quality under an acceptable running time.

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">∗Corresponding author</span></small>

Keywords: Traveling Salesman Problem with Drone, Minimize operational cost, Integer programming, Heuristic, GRASP

## 1. Introduction

Companies always tend to look for the most cost-efficient methods to distribute goods across logistic networks [1]. Traditionally, trucks have been used to handle these tasks and the corresponding transportation problem is modelled as a traveling salesman problem (TSP). However, a new distribution method has recently arisen in which small unmanned aerial vehicles (UAV), also known as drones, are deployed to support parcel delivery. On the one hand, there are four advantages of using a drone for delivery: (1) it can be operated without a human pilot, (2) it avoids the congestion of traditional road networks by flying over them, (3) it is faster than trucks, and (4) it has much lower transportation costs per kilometre [2]. On the other hand, because the drones are powered by batteries, their flight distance and lifting power are limited, meaning they are restricted in both maximum travel distance and parcel size. In contrast, a truck has the advantage of long range travel capability.

It can carry large and heavy cargo with a diversity of size, but it is also heavy, slow and has much higher transportation cost.

Consequently, the advantages of truck offset the disadvantages of drones and — similarly — the advantages of drones offset the disadvantages of trucks. These complementary capabilities are the foundation of a novel method named "last mile delivery with drone" [3], in which the truck transports the drone close to the customer locations, allowing the drone to service customers while remaining within its flight range, effectively increasing the usability and making the schedule more flexible for both drones and trucks. Specifically, a truck departs from the depot carrying the drone and all the customer parcels. As the truck makes deliveries, the drone is launched from the truck to service a nearby customer with a parcel. While the drone is in service, the truck continues its route to further customer locations. The drone then returns to the truck at a location different from its launch point.

From the application perspective, a number of remarkable events have occurred since 2013, when Amazon CEO Jeff Bezos first announced Amazon’s plans for drone delivery [4], termed "a big surprise." Recently, Google has been awarded a patent that outlines its drone delivery method [5]. In detail, rather than trying to land, the drone will fly above the target, slowly lowering packages on a tether. More interestingly, it will be able to communicate with humans using voice messages during the delivery process. Google initiated this important drone delivery project, called Wing, in 2014, and it is expected to launch in 2017 [6]. A similar Amazon project called Amazon Prime Air ambitiously plans to deliver packages by drone within 30 minutes [7]. Other companies worldwide have also been testing delivery services using drones. In April 2016, Australia Post successfully tested drones for delivering small packages. That project is reportedly headed towards a full customer trial later this year [8]. In May 2016, a Japanese company—Rakuten— launched a service named "Sora Kaku" that "delivers golf equipment, snacks, beverages and other items to players at pickup points on the golf course" [9]. In medical applications, Matternet, a California-based startup, has been testing drone deliveries of medical supplies and specimens (such as blood samples) in many countries since 2011. According to their CEO: it is "much more cost-, energyand time-efficient to send [a blood sample] via drone, rather than send it in a two-ton car down the highway with a person inside to bring it to a different lab for testing," [10]. Additionally, a Silicon Valley start-up named Zipline International began using drones to deliver medicine in Rwanda starting in July, 2016 [11].

We are aware of several publications in the literature that have investigated the routing problem related to the truck-drone combination for delivery. Murray and Chu [12] introduced the problem, calling it the "Flying Sidekick Traveling Salesman Problem" (FSTSP). A mixed integer liner programming (MILP) formulation and a heuristic are proposed. Basically, their heuristic is based on a "Truck First, Drone Second" idea, in which they first construct a route for the truck by solving a TSP problem and, then, repeatedly run a relocation procedure to reduce the objective value. In detail, the relocation procedure iteratively checks each node from the TSP tour and tries to consider whether it is suitable for use as a drone node. The change is applied immediately when this is true, and the current node is never checked again. Otherwise, the node is relocated to other positions in an effort to improving the objective value. The relocation procedure for TSP-D is designed in a "best improvement" fashion; it evaluates all the possible moves and executes the best one. The proposed methods are tested on only small-sized instances with up to 10 customers.

Agatz et al. [13], study a slightly different problem—called the "Traveling Salesman Problem with Drone" (TSP-D), in which the drone has to follow the same road network as the truck. Moreover, in TSP-D, the drone may be launched and return to the same location, while this is forbidden in the FSTSP. This problem is also modelled as a MILP formulation and solved by a "Truck First, Drone Second" heuristic in which drone route construction is based on either local search or dynamic programming. More recently, Ponza [14] extended the work of Murray and Chu [12] in his master’s thesis to solve the

FSTSP, proposing an enhancement to the MILP model and solving the problem by a heuristic method based on Simulated Annealing.

Additionally, Wang et al. [15], in a recent research, introduced a more general problem that copes with multiple trucks and drones with the goal of minimizing the completion time. The authors named the problem "The vehicle routing problem with drone" (VRP-D) and conducted the analysis on several worst-case scenarios, from which they propose bounds on the best possible savings in time when using drones and trucks instead of trucks alone.

All the works mentioned above aim to minimize the time at which the truck and the drone complete the route and return to the depot, which can improve the quality of service [16]. However, in every logistics activities, operational costs also play an important role in the overall business cost (see [17] and [18]). Hence, minimizing these costs by using a more cost-efficient approach is a vital objective of every company involved in transport and logistics activities. Recently, an objective function that minimizes the transportation cost was studied by Mathew et al. [19] for a related problem called the Heterogeneous Delivery Problem (HDP). However, unlike in [12], [20] and [14], the problem is modelled on a directed physical street network where a truck cannot achieve direct delivery to the customer. Instead, from the endpoint of an arc, the truck can launch a drone that will service the customers. In this way, the problem can be favourably transformed to a Generalized Traveling Salesman Problem (GTSP) [21]. The authors use the Nood-Bean Transformation available in Matlab to reduce a GTSP to a TSP, which is then solved by a heuristic proposed in the study. To the best of our knowledge, the min-cost objective function has not been studied for TSP-D when the problem is defined in a more realistic way—similarly to [12], [20], and [14]. Consequently, this gap in the literature provides a strong motivation for studying TSP-D with the min-cost objective function.

This paper studies a new variant of TSP-D following the hypotheses of the FSTSP proposed in the work of [12]. In FSTSP, the objective is to minimize the delivery completion time, or in other word the time coming back to the depot, of both truck and drone. In the new variant that we call min-cost TSP-D, the objective is to minimize the total operational cost of the system including two distinguished parts. The first part is the transportation cost of truck and drone while the second part relates to the waste time a vehicle has to wait for the other whenever drone is launched. In the following, we denote the FSTSP as min-time TSP-D to avoid confusion.

In this paper, we propose a MILP model and two heuristics to solve the min-cost TSP-D: a Greedy Randomized Adaptive Search Procedure (GRASP) and a heuristic adapted from the work of [12] called TSP-LS. In detail, the contributions of this paper are as follows:

\- We introduce a new variant of TSP-D called min-cost TSP-D, in which the objective is to minimize the operational costs.

\- We propose a model together with a MILP formulation for the problem which is an extended version of the model proposed in [12] for min-time TSP-D.

\- We develop two heuristics for min-cost TSP-D: TSP-LS and GRASP. which contain a new split procedure and local search operators. We also adapt our solution methods to solve the min-time problem studied in [12].

\- We introduce various sets of instances with different numbers of customers and a variety of options to test the problem.

\- We conduct various experiments to test our heuristics on the min-cost as well as min-time problems. We also compare solutions of both objec tives. The computational results show that GRASP outperforms TSP-LS in terms of quality of solutions with an acceptable running time. TSP-LS delivers solution of lower quality, but very quickly.

This article is structured as follows: Section 1 provides the introduction. Section 2 describes the problem and the model. The MILP formulation is introduced in Section 3. We describe our two heuristics in Sections 4 and 5. Section 6 presents the experiments, including instance generations and settings. We discuss the computational results in Section 7. Finally, Section 8 concludes the work and provides suggestions for future research.

## 2. Problem definition

In this section, we provide a description of the problem and discuss a model for the min-cost TSP-D in a step-by-step manner. Here, we consider a list of customers to whom a truck and a drone will deliver parcels. To make a delivery, the drone is launched from the truck and later rejoins the truck at another location. Each customer is visited only once and is serviced by either the truck or the drone. Both vehicles must start from and return to the depot. When a customer is serviced by the truck, this is called a **truck delivery**, while when a customer is serviced by the drone, this is called a **drone delivery**. This is represented as a 3-tuple $\langle i , j , k \rangle$ , where i is a launch node, j is a drone node (a customer who will be serviced by the drone), and k is a rendezvous node, as listed below:

• Node i is a launch node at which the truck launches the drone. The launching operation must be carried out at a customer location or the depot. The time required to launch the drone is denoted as $s _ { L }$

• Node j is a node serviced by the drone, called a "drone node". We also note that not every node in the graph is a drone node. Because some customers might demand delivery a product with size and weight larger than the capacity of the drone.

• Node k is a customer location where the drone rejoins the truck. At node $k ,$ the two vehicles meet again; therefore, we call it "rendezvous node". While waiting for the drone to return from a delivery, the truck can make other truck deliveries. The time required to retrieve the drone and prepare for the next drone delivery is denoted as $s _ { R }$ . Moreover, the two vehicles can wait for each other at the rendezvous point.

Moreover, the drone has an "endurance", which can be measured as the maximum time the drone can operate without recharging. A tuple $\langle i , j , k \rangle$ is called feasible if the drone has sufficient power to launch from $i ,$ deliver to $j$ and rejoin the truck at k. The drone can be launched from the depot but must subsequently rejoin the truck at a customer location. Finally, the drone’s last rendezvous with the truck can occur at the depot.

When not actively involved in a **drone delivery**, the drone is carried by the truck. We also assume that the drone is in constant flight when waiting for the truck. Furthermore, the truck and the drone have their own transportation costs per unit of distance. In practice, the drone’s cost is much lower than the truck’s cost because it weighs much less than the truck, hence, consuming much less energy. In addition, it is not run by gasoline but by batteries. We also assume that the truck provides new fresh batteries for the drone (or recharges its batteries completely) before each drone delivery begins. When a vehicle has to wait for each other, a penalty is created and added to the transportation cost to form the total operational cost of the system. The waiting costs of truck and drone are calculated by:

$$
\text {waiting cost} _ {\text {truck}} = \alpha \times \text {waiting time}
$$

$$
\text {waiting cost} _ {\text {drone}} = \beta \times \text {waiting time}
$$

where α and $\beta$ are the waiting fees of truck and drone per unit of time, respectively.

The objective of the min-cost TSP-D is to minimize the total operational cost of the system which includes the travel cost of truck and drone as well as their waiting costs. Because the problem reduces to a TSP when the drone’s endurance is null, it is NP-Hard. Examples of TSP and min-cost TSP-D optimal solutions on the same instance in which the unitary transportation cost of the truck is 25 times more expensive than that of the drone are shown in Figure 1.

![](images/page_8_image_2.jpg)

(b) Optimal min-cost TSP-D tour

![](images/page_8_image_4.jpg)

Figure 1: Optimal solution: TSP vs. min-cost TSP-D. TSP Objective = 1500, min-cost TSP-D Objective = 1000.82. The solid arcs are truck’s path. The dash arcs are drone’s path

We now develop the model for the problem. We first define basic notations relating to the graph, sequence and subsequence. Then, we formally define drone delivery and the solution representation as well as the associated constraints and objective.

## 2.1. The min-cost TSP-D problem

The min-cost TSP-D is defined on a graph $G = \bigl ( V , A \bigr ) ,   V = \bigl \{ 0 , 1 , \cdots , n , n   +$ 1}, where 0 and n + 1 both represent the same depot but are duplicated to represent the starting and returning points. The set of customers is $N =$ $\{ 1 , \cdots , n \}$ . Let $V _ { D } \; \subseteq \; N$ denote the set of customers that can be served by drone. Let $d _ { i j }$ and $d _ { i j } ^ { \prime }$ be the distances from node i to node j travelled by the truck and the drone, respectively. We also denote $\tau _ { i j } , \tau _ { i j } ^ { \prime }$ the travel time of truck and drone from i to $j .$ Furthermore, $C _ { 1 }$ and $C _ { 2 }$ are the transportation costs of the truck and drone, respectively, per unit of distance.

Given a sequence $s   =   \left\langle s _ { 1 } , s _ { 2 } , \cdots , s _ { t } \right\rangle$ , where $s _ { i } \in V , i = 1 \ldots t ,$ we denote the following:

$V ( s ) \subseteq V$ the list of nodes of s

$p o s ( i , s )$ the position of node $i \in V$ in s

\- next<sub>s</sub>(i), prev<sub>s</sub>(i) the next node and previous node of i in s

$f i r s t ( s ) ,   l a s t ( s )$ the first node and last node of s

\- s[i] the $i ^ { t h }$ node in s

$s i z e ( s )$ the number of nodes in s

$s u b ( i , j , s )$ , where $\forall i , j \in s , p o s { \big ( } i , s { \big ) } < p o s { \big ( } j , s { \big ) }$ , the subsequence of s from node i to node j

$A ( s ) = \{ ( i , n e x t _ { s } ( i ) ) | i \in V ( s ) \setminus l a s t ( s ) \}$ the set of arcs in s

$d _ { i \rightarrow k }$ the distance traveled by truck from i to k in the truck tour

$t _ { i \rightarrow k }$ the time traveled by truck from i to k in the truck tour

$t _ { i j k } ^ { \prime }$ the time traveled by drone from i to j to k in a drone delivery

$d _ { i \rightarrow k } ^ { - j }$ the distance traveled by truck from i to k in the truck tour with j removed (j is between i and k)

As mentioned above, we define a **drone delivery** as a 3-tuple $\langle i , j , k \rangle \enspace :$ $i , j , k \in V , i \neq j , j \neq k , k \neq i , \tau _ { i j } ^ { \prime } + \tau _ { j k } ^ { \prime } \leq \epsilon ,$ where e is a constant denoting the drone’s endurance. We also denote P as the set of all possible drone deliveries on the graph $G = \left( V , A \right)$ that satisfies the endurance constraint as follows:

$$
\mathbb {P} = \{\langle i, j, k \rangle : i, k \in V, j \in V _ {D}, i \neq j, j \neq k, k \neq i, \tau_ {i j} ^ {\prime} + \tau_ {j k} ^ {\prime} \leq \epsilon \}.
$$

## 2.2. Solution representation

A **min-cost TSP-D solution**, denoted as sol, is represented by two components:

\- A truck tour, denoted as $T D ,$ is a sequence $\left\langle e _ { 0 } , e _ { 1 } , \cdots , e _ { k } \right\rangle$ , where $e _ { 0 } =$ $e _ { k } = 0 , e _ { i } \in V ,   e _ { i } \neq$ e  j and $i \neq j .$

\- A set of drone deliveries DD such that $D D \subseteq \mathbb { P } ,$

which can also be written as

$$
\text {sol} = (T D, D D).
$$

## 2.3. Constraints

A solution (TD, DD) of the min-cost TSP-D must satisfy the following constraints:

(A) Each customer must be serviced by either the truck or the drone:

$$
\forall e \in N: e \in T D \text {or} \exists \langle i, e, k \rangle \in D D.
$$

By definition, during a truck tour, a customer cannot be visited twice by the truck. The above constraint does not prevent a customer from being serviced by both the truck and the drone nor from being serviced twice by the drone.

(B) A customer is never serviced twice by the drone:

$$
\forall \langle i, j, k \rangle , \langle i ^ {\prime}, j ^ {\prime}, k ^ {\prime} \rangle \in D D: j \neq j ^ {\prime}.
$$

(C) Drone deliveries must be compatible with the truck tour:

$$
\forall \langle i, j, k \rangle \in D D: j \notin T D, i \in T D, k \in T D, p o s (i, T D) <   p o s (k, T D).
$$

This constraint implies that a customer cannot be serviced by both the truck and drone.

(D) No interference between drone deliveries:

$$
\forall \langle i, \cdot , k \rangle \in D D, \forall e \in \operatorname{sub} (i, k, T D), \forall \langle i ^ {\prime}, j ^ {\prime}, k ^ {\prime} \rangle \in D D: e \neq i ^ {\prime}.
$$

The above constraint means that when the drone is launched from the truck for a drone delivery, it cannot be relaunched before the rendezvous from that delivery. As a consequence, we cannot have any other rendezvous during that period either.

## 2.4. Objective

Regarding the costs, the following notations are used:

$- \; c o s t \big ( i , j , k \big ) \; = \; C _ { 2 } \big ( d _ { i j } ^ { \prime } + d _ { j k } ^ { \prime } \big )$ , where $\langle i , j , k \rangle \; \in \; \mathbb { P }$ [cost of drone delivery $\langle i , j , k \rangle ]$

$\begin{array} { r } { \mathrm { ~ - ~ } c o s t _ { W } ^ { T } \big ( i , j , k \big ) = \alpha \times m a x \big ( 0 , \big ( t _ { i \rightarrow k } - t _ { i j k } ^ { \prime } \big ) \big ) } \end{array}$ , where $\langle i , j , k \rangle \in \mathbb { P }$ [waiting cost of truck at k]

$- \; cost_{W}^{D}\big(i,j,k\big) = \beta \times max\big(0,\big(t_{ijk}^{\prime} - t_{i \rightarrow k}\big)\big)$ , where $\langle i , j , k \rangle \in \mathbb { P }$ [waiting cost of drone at k]

$-\ cost (TD)=\sum_{(i,j)\in A(TD)}C_{1}.d_{ij}$ [cost of a truck tour TD]

$- \; c o s t \big ( D D \big ) = \sum _ { \langle i , j , k \rangle \in D D } c o s t \big ( i , j , k \big )$ [total cost of all drone deliveries in DD]

$-\ cost_{W}(DD)=\sum_{\langle i,j,k\rangle\in DD}cost_{W}^{T}(i,j,k)+cost_{W}^{D}(i,j,k)$ [total waiting cost]

$- ~ c o s t \big ( T D , D D \big ) = c o s t \big ( T D \big ) + c o s t \big ( D D \big ) + c o s t _ { W } \big ( D D \big )$ [cost of a solution]

$- \; c o s t \big ( s u b \big ( i , k , s \big ) \big )$ the total cost for both truck and drone and their waiting cost (if any) in a subsequence $s \in T D$

**The objective** is to minimize the total operational cost:

$$
\min \operatorname{cost} (T D, D D).
$$

## 3. Mixed Integer Linear Programming Formulation

The min-cost TSP-D defined in the previous section is represented here in a MILP formulation. This formulation is an extension from the one proposed by [12]. We extend it by proposing constraints where waiting time is captured in order to calculate the waiting cost of two vehicles. We first define two subsets of $V ,   V _ { L } = \left\{ 0 , 1 , \cdots , n \right\}$ and $V _ { R } = \left\{ 1 , 2 , \cdots , n + 1 \right\}$ to distinguish the nodes that from where the drone can be launched from and the one it returns to.

## Variables

Let $x _ { i j } \; \in \; \{ 0 , 1 \}$ equal one if the truck goes from node i to node $j$ with $i   \in   V _ { L }$ and $j   \in   V _ { R } ,   i   \neq   j .$ Let $y _ { i j k }   \in   \{ 0 , 1 \}$ **e**qual one if $\langle i , j , k \rangle$ is a drone delivery. We can denote $p _ { i j } \in \{ 0 , 1 \}$ as equalling one if node $i \in N$ is visited before node $j \in N ,   j \neq i ,$ in the truck’s path. We also set $p _ { 0 j } = 1$ for all $j \in N$ to indicate that the truck always starts the tour from the depot. As in standard TSP subtour elimination constraints, we denote $0 \leq u _ { i } \leq n + 1$ as the position of the node $i ,   i \in V$ in the truck’s path.

To handle the waiting time, let $t _ { i }   \geq   0 , t _ { i } ^ { \prime }   \geq   0 , i   \in   V _ { R }$ denote the arrival time of truck and drone at node $i ,   r _ { i }   \geq   0 , r _ { i } ^ { \prime }   \geq   0 , i   \in   V _ { R }$ the leaving time of truck and drone at node i. We also denote $w _ { i } \geq 0 , w _ { i } ^ { \prime } \geq 0 , i \in V _ { R }$ the waiting time of truck and drone at node i respectively. Finally, we have $t _ { 0 } = 0 , t _ { 0 } ^ { \prime } =$ $0 , r _ { 0 } = 0 , r _ { 0 } ^ { \prime } = 0$ the earliest time of truck and drone starting from depot 0 and $w _ { 0 } = 0 , w _ { 0 } ^ { \prime } = 0$ the waiting time at the starting depot.

**The MILP formulation** is as follows:

$$
\begin{array}{c}\text{\rm{Min}} C_{1}\sum_{i\in V_{L}}\sum_{\substack{j\in V_{R}\\ i\neq j}}d_{ij}x_{ij} + C_{2}\sum_{i\in V_{L}}\sum_{\substack{j\in N\\ i\neq j}}\sum_{\substack{k\in V_{R}\\ \langle i,j,k\rangle \in \mathbb{P}}} (d^{\prime}_{ij} + d^{\prime}_{jk})y_{ijk}\\ \\ +\alpha \sum_{i\in V}w_{i} + \beta \sum_{i\in V}w^{\prime}_{i} \end{array}\tag{1}
$$

$$
\left|\sum_{\substack{i\in V_{L}\\ i\neq j}}x_{ij} + \sum_{\substack{i\in V_{L}\\ i\neq j}}\sum_{\substack{k\in V_{R}\\ \langle i,j,k\rangle \in \mathbb{P}}}y_{ijk} = 1\quad \forall j\in N\right|\tag{2}
$$

$$
\sum_ {j \in V _ {R}} x _ {0 j} = 1\tag{3}
$$

$$
\sum_ {i \in V _ {L}} x _ {i, n + 1} = 1\tag{4}
$$

$$
u _ {i} - u _ {j} + 1 \leq (n + 2) (1 - x _ {i j}) \quad \forall i \in V _ {L}, j \in \{V _ {R}: i \neq j \}\tag{5}
$$

$$
\sum_{\substack{i\in V_{L}\\ i\neq j}}x_{ij} = \sum_{\substack{k\in V_{R}\\ k\neq j}}x_{jk}\quad \forall j\in N\tag{6}
$$

$$
2y_{ijk}\leq \sum_{\substack{h\in V_{L}\\ h\neq i}}x_{hi} + \sum_{\substack{l\in N\\ l\neq k}}x_{lk}\tag{7}
$$

$$
\forall i \in N, j \in \{N: i \neq j \}, k \in \{V _ {R}: \langle i, j, k \rangle \in \mathbb {P} \}
$$

$$
y_{0jk}\leq \sum_{\substack{h\in V_{L}\\ h\neq k\\ h\neq j}}x_{hk}\quad j\in N,k\in \{V_{R}:\langle 0,j,k\rangle \in \mathbb{P}\}\tag{8}
$$

$$
u_{k} - u_{i}\geq 1 - (n + 2)(1 - \sum_{\substack{j\in N\\ \langle i,j,k\rangle \in \mathbb{P}}}y_{ijk})\tag{9}
$$

$$
\forall i \in V _ {L}, k \in \{V _ {R}: k \neq i \}
$$

$$
\sum_{\substack{j\in N\\ j\neq i}}\sum_{\substack{k\in V_{R}\\ \langle i,j,k\rangle \in \mathbb{P}}}y_{ijk}\leq 1\quad \forall i\in V_{L}\tag{10}
$$

$$
\sum_{\substack{i\in V_{L}\\ i\neq k}}\sum_{\substack{j\in N\\ \langle i,j,k\rangle \in \mathbb{P}}}y_{ijk}\leq 1\quad \forall k\in V_{R}\tag{11}
$$

$$
u_{i} - u_{j}\geq 1 - (n + 2)p_{ij} - M(2 - \sum_{\substack{h\in V_{L}\\ h\neq i}}x_{hi} - \sum_{\substack{k\in N\\ k\neq j}}x_{kj})\tag{12}
$$

$$
\forall i \in N, j \in \{V _ {R}: j \neq i \}
$$

$$
u_{i} - u_{j}\leq -1 + (n + 2)(1 - p_{ij}) + M(2 - \sum_{\substack{h\in V_{L}\\ h\neq i}}x_{hi} - \sum_{\substack{k\in N\\ k\neq j}}x_{kj})\tag{13}
$$

$$
\forall i \in N, j \in \{V _ {R}: j \neq i \}
$$

$$
u_{0} - u_{j}\geq 1 - (n + 2)p_{0j} - M(1 - \sum_{\substack{k\in V_{L}\\ k\neq j}}x_{kj})\quad \forall j\in V_{R}\tag{14}
$$

$$
u_{0} - u_{j}\leq -1 + (n + 2)(1 - p_{0j}) + M(1 - \sum_{\substack{k\in V_{L}\\ k\neq j}}x_{kj})\quad \forall j\in V_{R}\tag{15}
$$

$$
u_{l}\geq u_{k} - M\Bigg(3 - \sum_{\substack{j\in N\\ j\neq l\\ \langle i,j,k\rangle \in \mathbb{P}}}y_{ijk} - \sum_{\substack{m\in N\\ m\neq i\\ m\neq k\\ m\neq l}}\sum_{\substack{n\in V_{R}\\ n\neq i\\ n\neq k\\ \langle l,m,n\rangle \in \mathbb{P}}}y_{lmn} - p_{il}\Bigg)\tag{16}
$$

$$
\forall i \in V _ {L}, k \in \{V _ {R}: k \neq i \}, l \in \{N: l \neq i, l \neq k \}.
$$

$$
t _ {k} \geq r _ {i} + \tau_ {i k} - M (1 - x _ {i k}) \quad \forall i \in V _ {L}, k \in V _ {R}, i \neq j\tag{17}
$$

$$
t _ {k} \leq r _ {i} + \tau_ {i k} + M (1 - x _ {i k}) \quad \forall i \in V _ {L}, k \in V _ {R}, i \neq j\tag{18}
$$

$$
t_{j}^{\prime}\geq r_{i} + \tau_{ij}^{\prime} - M(1 - \sum_{\substack{k\in V_{R}\\ \langle i,j,k\rangle \in \mathbb{P}}}y_{ijk})\quad \forall j\in V_{D},i\in V_{L},j\neq i\tag{19}
$$

$$
t_{j}^{\prime}\leq r_{i} + \tau_{ij}^{\prime} + M(1 - \sum_{\substack{k\in V_{R}\\ \langle i,j,k\rangle \in \mathbb{P}}}y_{ijk})\quad \forall j\in V_{D},i\in V_{L},j\neq i\tag{20}
$$

$$
t_{k}^{\prime}\geq r_{j}^{\prime} + \tau_{jk}^{\prime} - M(1 - \sum_{\substack{i\in V_{L}\\ \langle i,j,k\rangle \in \mathbb{P}}}y_{ijk})\quad \forall j\in V_{D},k\in V_{R},j\neq k\tag{21}
$$

$$
t_{k}^{\prime}\leq r_{j}^{\prime} + \tau_{jk}^{\prime} + M(1 - \sum_{\substack{i\in V_{L}\\ \langle i,j,k\rangle \in \mathbb{P}}}y_{ijk})\quad \forall j\in V_{D},k\in V_{R},j\neq k\tag{22}
$$

$$
t_{j}^{\prime}\geq r_{j}^{\prime} - M(1 - \sum_{\substack{i\in V_{L}\\ i\neq j}}\sum_{\substack{k\in V_{R}\\ \langle i,j,k\rangle \in \mathbb{P}}}y_{ijk})\quad \forall j\in N\tag{23}
$$

$$
t_{j}^{\prime}\leq r_{j}^{\prime} + M(1 - \sum_{\substack{i\in V_{L}\\ i\neq j}}\sum_{\substack{k\in V_{R}\\ \langle i,j,k\rangle \in \mathbb{P}}}y_{ijk})\quad \forall j\in N\tag{24}
$$

$$
\left| \begin{array}{c}r_{k}\geq t_{k} + s_{L}(\sum_{\substack{l\in N\\ l\neq k}}\sum_{\substack{m\in V_{R}\\ m\neq l\\ m\neq k\\ \langle k,l,m\rangle \in \mathbb{P}}}y_{klm}) + s_{R}(\sum_{\substack{i\in V_{L}\\ i\neq k}}\sum_{\substack{j\in N\\ \langle i,j,k\rangle \in \mathbb{P}}}y_{ijk})\\ -M(1 - \sum_{\substack{i\in V_{L}\\ i\neq k}}\sum_{\substack{j\in N\\ \langle i,j,k\rangle \in \mathbb{P}}}y_{ijk})\quad \forall k\in V_{R} \end{array} \right|\tag{25}
$$

$$
\begin{array}{c}r^{\prime}_{k}\geq t^{\prime}_{k} + s_{L}(\sum_{\substack{l\in N\\ l\neq k}}\sum_{\substack{m\in V_{R}\\ m\neq l\\ m\neq k\\ \langle k,l,m\rangle \in \mathbb{P}}}y_{klm}) + s_{R}(\sum_{\substack{i\in V_{L}\\ i\neq k}}\sum_{\substack{j\in N\\ \langle i,j,k\rangle \in \mathbb{P}}}y_{ijk})\\ -M(1 - \sum_{\substack{i\in V_{L}\\ i\neq k}}\sum_{\substack{j\in N\\ \langle i,j,k\rangle \in \mathbb{P}}}y_{ijk})\quad \forall k\in V_{R} \end{array}\tag{26}
$$

$$
r_{k}^{\prime} - (r_{j}^{\prime} - \tau_{ij}^{\prime}) - s_{L}(\sum_{\substack{l\in N\\ l\neq i\\ l\neq j\\ l\neq k}}\sum_{\substack{m\in V_{R}\\ m\neq k\\ m\neq i\\ m\neq l\\ \langle k,l,m\rangle \in \mathbb{P}}}y_{klm})\leq \epsilon +M(1 - y_{ijk})\tag{27}
$$

$$
\forall k \in V _ {R}, j \in C, j \neq k, i \in V _ {R}, \langle i, j, k \rangle \in \mathbb {P}
$$

$$
w _ {k} \geq 0 \quad \forall k \in V _ {R}\tag{28}
$$

$$
w _ {k} ^ {\prime} \geq 0 \quad \forall k \in V _ {R}\tag{29}
$$

$$
w _ {k} \geq t _ {k} ^ {\prime} - t _ {k} \quad \forall k \in V _ {R}\tag{30}
$$

$$
w _ {k} ^ {\prime} \geq t _ {k} - t _ {k} ^ {\prime} \quad \forall k \in V _ {R}\tag{31}
$$

$$
w _ {0} = 0\tag{32}
$$

$$
w _ {0} ^ {\prime} = 0\tag{33}
$$

$$
r _ {i} = r _ {i} ^ {\prime} \quad \forall i \in V\tag{34}
$$

$$
t _ {0} = 0\tag{35}
$$

$$
t _ {0} ^ {\prime} = 0\tag{36}
$$

$$
r _ {0} = 0\tag{37}
$$

$$
r _ {0} ^ {\prime} = 0\tag{38}
$$

$$
x _ {i j} \in \{0, 1 \} \quad \forall i \in V _ {L}, j \in V _ {R}, j \neq i\tag{39}
$$

$$
\left| \begin{array}{l} y _ {i j k} \in \{0, 1 \} \quad \forall i \in V _ {L}, j \in N, k \in V _ {R}, i \neq j, j \neq k, i \neq k, \langle i, j, k \rangle \in \mathbb {P} \end{array} \right.\tag{40}
$$

$$
p _ {i j} \in \{0, 1 \} \quad \forall i, j \in N, i \neq j\tag{41}
$$

$$
p _ {0 j} = 1 \quad \forall j \in N\tag{42}
$$

$$
0 \leq u _ {i} \leq n + 1 \quad \forall i \in V\tag{43}
$$

$$
t _ {i} \geq 0 \quad \forall i \in V\tag{44}
$$

$$
t _ {i} ^ {\prime} \geq 0 \quad \forall i \in V\tag{45}
$$

$$
r _ {i} \geq 0 \quad \forall i \in V\tag{46}
$$

$$
r _ {i} ^ {\prime} \geq 0 \quad \forall i \in V\tag{47}
$$

The objective is to minimize the operational costs. We now explain the constraints. The letter in parenthesis at the end of each bullet item, if any, denotes the association between a MILP constraint and a constraint described in the model:

• Constraint 2 guarantees that each node is visited once by either a truck or a drone. **(A)**

• Constraints 3 and 4 state that the truck must start from and return to the depot. **(Modelling** TD)

• Constraint 5 is a subtour elimination constraint. **(Modelling** TD)

• Constraint 6 indicates that if the truck visits j then it must depart from j. **(Modelling** TD)

• Constraint 7 associates a drone delivery with the truck route. In detail, if we have a drone delivery $\langle i , j , k \rangle$ , then there must be a truck route between i and k. **(C)**

• Constraint 8 indicates that if the drone is launched from the depot, then the truck must visit k to collect it. **(C)**

• Constraint 9 ensures that if there is a drone delivery for $\langle i , j , k \rangle$ , then the truck must visit i before k. **(C)**

• Constraints 10 and 11 state that each node in $V _ { L }$ or $V _ { R }$ can either launch the drone or retrieve it at most once, respectively. **(B)**

• Constraints 12, 13, 14 and 15 ensure that if i is visited before j in the truck route, then its ordering constraint must be maintained. **(D)**

• Constraint $1 6 ,$ if we have two drone deliveries $\langle i , j , k \rangle$ and $\langle l , m , n \rangle$ and i is visited before l, then l must be visited after k. This constraint avoids the problem of launching a drone between i and k. **(D)**

• Finally, constraints 17 to 38 ensure that waiting time and endurance is correctly handled. **(E)**

## 4. A Greedy Randomized Adaptive Search Procedure (GRASP) for TSP-D

This section presents a Greedy Randomized Adaptive Search Procedure (GRASP) [22] to solve the min-cost TSP-D. We also adapt our split procedure to solve the min-time TSP-D. In the construction step, we propose a split algorithm that builds a min-cost TSP-D solution from a TSP solution. In the local search step, new operators adapted from the traditional ones are introduced for the min-cost TSP-D. The general outline of our GRASP is shown in Algorithm 1. More specifically, in each iteration, it first generates a TSP tour using a TSP construction heuristic (line 7). In this paper, we use three heuristics to generate giant tours as follows:

• k-nearest neighbour: This heuristic is inspired from the well-known nearest neighbour algorithm for solving the TSP. It starts from the depot, repeatedly visits the node v which is randomly chosen among k closest unvisited nodes.

• k-cheapest insertion: The approach is to start with a subtour, i.e., a small tour with a subset of nodes, and then extend this tour by repeatedly inserting the remaining nodes until no more node can be added. The unvisited node v to be inserted and its insertion location between two consecutive nodes $( i , j )$ of the tour are selected so that this combination gives the least Insertion Costs (IC). This cost is calculated by:

$$
IC = d _ {i v} + d _ {v j} - d _ {i j}\tag{48}
$$

To create the randomness for the heuristic, at each insertion step we randomly choose a pair of an unvisited node and its insertion location among k pairs which provides the best insertion costs. The starting subtour includes only the depot.

• random insertion: This heuristic works similarly to the k-nearest neighbour but it iteratively chooses a random node v among all unvisited nodes.

```matlab
Algorithm 1: Greedy Randomized Adaptive Search Procedure (GRASP)
for min-cost TSP-D
    Result: bestSolution
1 bestSolution = null ;
2 bestObjectiveValue = T ;
3 randomGenerator = initialize TSP tour random generator ;
4 iteration = 0 ;
5 while iteration < nTSP do
6     iteration = iteration + 1 ;
7     tour = generate a random TSP tour using randomGenerator ;
8     (P,V,T) = Split_Algorithm_Step1(tour) ;
9     tspdSolution = Split_Algorithm_Step2(P, V, T) ;
10     tspdSolution = Local_Search(tspdSolution) ;
11     if f(tspdSolution) < bestObjectiveValue then
12         bestSolution = tspdSolution ;
13         bestObjectiveValue = f(tspdSolution) ;
14 return bestSolution ;
```

In the next step, we construct a min-cost TSP-D solution using the split algorithm (line 8 and 9) and then improve it by local search (line 10). The best solution found is also recorded during the processing of the tours (lines 11 to 13). The algorithm stops after $n _ { T S P }$ iterations. The detailed implementation of the split algorithm is described in Algorithms 2 and 3.

## 4.1. A Split Algorithm for min-cost TSP-D

Given a TSP tour, the split procedure algorithm selects nodes to be visited by the drone to obtain a solution for the min-cost TSP-D, assuming that the relative order of the nodes is fixed. Other split procedures are now used widely in state-of-the-art metaheuristics such as [23], [24], [25], [26] to solve many variants of VRPs. We start from a given TSP tour $s = \left( s _ { 0 } , s _ { 1 } , \cdots s _ { n + 1 } \right)$ and must convert this tour into a feasible min-cost TSP-D solution. This is accomplished by removing nodes from the truck tour and substituting drone deliveries for those nodes. There are two main steps in the split algorithm: auxiliary graph construction and solution extraction. The pseudo code for these is listed in $\mathrm { A l - }$ gorithms $2$ and $^ { 3 , }$ respectively. The most important step of the split algorithm is the construction of the auxiliary graph, in which each subsequence of nodes $( s _ { i } , \dots s _ { k } )$ can be turned into a drone delivery such that $s _ { i }$ is the launch node, $s _ { k }$ is the rendezvous node and $s _ { j } ,$ where $p o s \big ( s _ { i } , s \big )   <   p o s \big ( s _ { j } , s \big )   <   p o s \big ( s _ { k } , s \big )$ , is the drone node. We now describe the split algorithm in detail.

<div class="docvortex-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Algorithm 2: Split_Algorithm_Step1(s): Building the auxiliary graph and finding shortest path
Data: TSP tour s
Result: P stores the shortest path from the auxiliary graph, V is the cost of that shortest path, and T is a list of the possible drone deliveries and costs
$arcs = \varnothing$;
T = \varnothing ;
/* Auxiliary graph construction - Arcs */
foreach i in s \ last(s) do
    $k = pos(i, s) + 1$;
    $arcs = arcs \cup (i, k, cost(i, k, s))$
foreach i in s \ { last(s), s[pos(last(s), s) - 1] } do
    foreach k in s : $pos(k, s) \geq pos(i, s) + 2$ do
        minValue = $\infty$ ;
        minIndex = $\infty$ ;
        foreach j in s : $pos(i, s) &lt; pos(j, s) &lt; pos(k, s)$ do
            if $\langle i, j, k \rangle \in \mathbb{P}$ then
                cost = $cost(sub(i, k, s)) + C_1 \left( d_{prev_s(j)next_s(j)} - d_{prev_s(j),j} - d_{j,next_s(j)} \right) + cost(i, j, k) + cost_W^T(i, j, k) + cost_W^D(i, j, k)$ ;
                if cost &lt; minValue then
                    minValue = cost ;
                    minIndex = pos(j, s) ;
            arcs = arcs $\cup \{(i, k, minValue)\}$ ;
        if minIndex $\neq \top$ then
            T = T $\cup \{(i, s[minIndex], k, minValue)\}$ ;
/* Finding the shortest path */
V[0] = 0 ;
P[0] = 0 ;
foreach k in s \ { 0 } do
    foreach (i, k, cost) $\in$ arcs do
        if V[k] &gt; V[i] + cost then
            V[k] = V[i] + cost ;
            P[k] = i ;
return (P, V, T) ;
</div>

Building the auxiliary graph and finding shortest path. In Algorithm 2, we construct an auxiliary weighted graph $H = \left( V ^ { \prime } , A ^ { \prime } \right)$ based on the TSP tour s of the graph $G = \left( V , A \right)$ . We have $V ^ { \prime } = V$ and an arc $( i , j ) \in A ^ { \prime }$ that represents a subroute from i to $j ,$ where pos $\left( i , s \right) < p o s { \left( j , s \right) }$

If i and j are adjacent nodes in $s ,$ then the cost $c _ { i j }$ of arc $( i , j ) \; \in \; A ^ { \prime }$ is calculated directly as follows:

$$
c _ {i j} = C _ {1} d _ {i j}.\tag{49}
$$

However, when i and k are not adjacent and a node j exists between i and k such that $\langle i , j , k \rangle \in \mathbb { P } ,$ , then

$$
\begin{array}{c} c _ {i k} = \min _ {\langle i, j, k \rangle \in \mathbb {P}} c o s t (s u b (i, k, s)) + C _ {1} \Big (d _ {p r e v _ {s} (j), n e x t _ {s} (j)} - d _ {p r e v _ {s} (j), j} - d _ {j, n e x t _ {s} (j)} \Big) \\ \qquad \qquad \qquad + c o s t (i, j, k) + c o s t _ {W} ^ {T} (i, j, k) + c o s t _ {W} ^ {D} (i, j, k). \end{array}\tag{50}
$$

If i and k are not adjacent and no node j exists between i and k such that $\langle i , j , k \rangle$ could be a **drone delivery**, then

$$
c _ {i k} = + \infty .\tag{51}
$$

The arc’s cost calculation is shown in lines 1 to 19 in Algorithm 2. Moreover, in lines 18 and 19, we store the list of possible **drone deliveries** T. This list will be used in the extraction step.

The auxiliary graph is used to compute the cost $v _ { k }$ of the shortest path from the depot to node k. Because the graph H is a directed acyclic graph, these values can be computed easily using a dynamic programming approach. Moreover, an arc $( i , k )$ in the shortest path that does not belong to the initial TSP tour means that a drone delivery can be made where i is the launch node, k is the rendezvous node, and the delivery node is a node between i and k in the TSP tour. This computation ensures that no interference occurs between the chosen drone deliveries. We therefore obtain the best solution from the TSP tour while respecting the relative order of the nodes.

In detail, given $v _ { 0 }   =   0 ,$ , the value $v _ { k }$ of each node $k   \in   V ^ { \prime } \setminus \{ 0 \}$ is then

calculated by

$$
v _ {k} = \min \{v _ {i} + c _ {i k}: (i, k) \in A ^ {\prime} \} \quad \forall k = 1, 2, \dots , n + 1.\tag{52}
$$

We also store the shortest path from 0 to $n + 1$ in $P ( j )$ , where $j = 1 \ldots n + 1 ;$ j is the node, and the value $P ( j )$ is the previous node of j. These steps are described in lines 21 to 27 in Algorithm 2. An auxiliary graph for Figure 1 is shown in Figure 2

![](images/page_23_image_6.jpg)

Figure 2: Auxiliary graph for TSP tour in Figure 1

The cost computation for each arc in the graph H can be done in $\mathcal { O } ( n ^ { 2 } )$ Since H is acyclic by construction, to search for a shortest path, a breadth-first search (BFS) algorithm for directed acyclic graphs can be used, with an $\mathcal { O } ( | A | )$ complexity where $| A |$ is the number of arcs in the graph. Because the number of arcs in H is proportional to $n ^ { 2 } .$ Thus, the search for a shortest path in graph H can be done in $\mathcal { O } ( n ^ { 2 } )$ . Several Split procedures in the literature work in a similar manner (see [27], [28] for example). Therefore, we get the complexity of the Algorithm 2 in $\mathcal { O } ( n ^ { 4 } )$ .

Extracting min-cost TSP-D solution. Given $P \big ( j \big ) , j = 1 \ldots n + 1$ defined as above and a list of possible **drone deliveries** T, we now extract the min-cost TSP-D solution in Algorithm 3. In the first step, given $P ,$ we construct a sequence of nodes $S _ { a }   =   0 , n _ { 1 } , \cdots , n   +   1$ representing the path from 0 to $\mathfrak { n } + 1$ in the auxiliary graph (lines 2 to 9). Each two consecutive nodes in $S _ { a }$ are a subroute of the complete solution. However, they might include a **drone delivery**; consequently, we need to determine which node might be the drone node in the subroute, which is computed in T.

The second step is to construct a min-cost TSP-D solution. To do that, we first initialize two empty sets: a set of drone deliveries $S _ { d }$ and a set representing the truck’s tour sequence $S _ { t }$ (lines 11 and 12). We now build these sets one at a time.

For drone delivery extractions, we consider each pair of adjacent positions i and $i + 1$ in $P _ { n e w }$ and determine the number of in-between nodes. If there is at least one $j$ node between the i and $i + 1$ positions in the $\mathrm { T S P }$ tour, we will choose the drone delivery in T with the minimum value, taking its drone node j as the result (lines 14 to 17).

To extract the truck’s tour (line 19 to 26), we start from the depot 0 in $S _ { a }$ Each pair $i , i + 1 \in S _ { a }$ is considered as a subroute in the min-cost TSP-D solution by taking the nodes from i to $i + 1$ in the $\mathrm { T S P }$ solution. However, in cases where i and $i + 1$ are launch and rendezvous nodes of a **drone delivery**, respectively, $\langle i , j , i + 1 \rangle$ , j must not be considered in the truck’s tour.

```txt
Algorithm 3: Split_Algorithm_Step2(P,V,T): Extract_TSPD_Solution
    Data: P stores the path in the auxiliary graph, V is the cost of the path in P, T is the list of drone deliveries + costs, and tspTour is the truck-only TSP tour
    Result: tspdSolution
1 /* Construct the sequence of nodes representing the path stored in P */
2 j = n + 1 ;
3 i = ∞ ;
4 Sa = ⟨j⟩ ;
5 while i ≠ 0 do
6     i = P[j] ;
7     Sa = Sa::⟨i⟩ ;
8     j = i ;
9 Sa = Sa.reverse() ;
10 /* Create a min-cost TSP-D solution from Sa */
11 Sd = ⟨⟩ ;
12 St = ⟨⟩ ;
13 /* Drone deliveries */
14 for i = 0; i < Sa.size - 1; i++ do
15     if between Sa[i] and Sa[i + 1] in tspTour, there is at least one node then
16     n_drone = obtain the associated drone node in tuples T ;
17     Sd = Sd ∪ ⟨Sa[i], n_drone, Sa[i + 1]⟩ ;
18 /* Truck tour */
19 currentNode = 0 ;
20 while Algeria ≠ n + 1 do
21     if Algeria is a launch node of a tuple t in Sd then
22     St = St :: ⟨all the nodes from the Algeria to the return node of t in tspTour except the drone node⟩ ;
23     Algeria = the return node of t ;
24     else
25     St = St :: ⟨currentNode⟩ ;
26     Algeria = tspTour[indexOf(currentPosition) + 1] ;
27 tspdSolution = (St, Sd) ;
28 return tspdSolution ;
```

415 Split procedure adaptation for min-time TSP-D. To deal with the min-time problem, we change the way the arc’s costs are computed in the auxiliary graph as follows: If i and j are adjacent nodes in s, then the cost $c _ { i j }$ is calculated by:

$$
c _ {i j} = \tau_ {i j}\tag{53}
$$

When i and k are not adjacent and a node j exists between i and k such that $\langle i , j , k \rangle \in \mathbb { P }$ , then

$$
c _ {i k} = \min _ {\langle i, j, k \rangle \in \mathbb {P}} (m a x (t i m e _ {T} (i \to k), t i m e _ {D} (i, j) + t i m e _ {D} (j, k)) + s _ {R} + s _ {L}).\tag{54}
$$

where ti $n e _ { T } ( i   \rightarrow   k )$ is the travel time of truck from launch point i to rendezvous point j and $t i m e _ { D } ( i , j )$ is the travel time of drone from i to j. Eventually, this modification results in a change of Algorithm 2, specifically, line 13 to 15 as follows:

<div class="docvortex-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Algorithm 4: Split_Algorithm_Step1(s): Min-time adaptation

1 ...
2 timeDrone = time_D(i, j) + time_D(j, k);
3 timeTruck = time_T(i → k);
4 if max(timeTruck, timeDrone) + s_R + s_L &lt; minValue then
5    $\text{minValue} = \text{max(timeTruck, timeDrone)} + s_R + s_L$;
6    ...
</div>

## 4.2. Local search operators

Two of our local search operators are inspired from the traditional move operators Two-exchange and Relocation [29]. In addition, given the charac teristics of the problem, we also develop two new move operators, namely, "drone relocation", which is a modified version of the classical relocation operator, and "drone removal", which relates to the removal of a drone node. In detail, from a min-cost TSP-D solution (TD, DD), we denote the following:

$- \; N _ { T } \big ( T D , D D \big )   =   \big \{ e   :   e   \in   T D , \big \langle e , \cdot , \cdot \big \rangle   \notin   D D , \big \langle \cdot , \cdot , e \big \rangle   \notin   D D \big \}$ is the set of **truck-only nodes** in the solution (TD, DD) that are not associated with any drone delivery

$- \; N _ { D } \big ( T D , D D \big ) \: = \: \big \{ e \: : \: \big \langle \cdot , e , \cdot \big \rangle \; \in \; D D \big \}$ is the set of **drone nodes** in the solution (TD, DD)

We now describe each operator.

Relocation: This is the traditional relocation operator with two differences:

(1) We consider only truck-only nodes; (2) we only relocate into a new position in the truck’s tour. An example is shown in Figure 3. In detail, we denote

$$
\text {relocate} _ {T} ((T D, D D), a, b), a \in N _ {T} ((T D, D D)), b \in T D, b \neq a, b \neq 0\tag{55}
$$

as the operator that—in effect—relocates node a before node b in the truck tour.

Drone relocation: The original idea of this operator is that it can change a truck node to a drone node or relocate an existing drone node so that it has different launch and rendezvous locations. The details are as follows: (1) We consider both truck-only and drone nodes; (2) each of these nodes is then relocated as a drone node in a different position in the truck’s tour. This move operator results in a neighbourhood that might contain more **drone deliveries**; hence, it has more possibilities to reduce the cost. An example is shown in Figure 4. More precisely, we denote

$$
\text {relocate} _ {D} ((T D, D D), a, i, k)\tag{56}
$$

$$
a \in N _ {T} ((T D, D D)) \cup N _ {D} ((T D, D D)), i, k \in T D \setminus \{a \}, i \neq k,
$$

$$
p o s (i, T D) <   p o s (k, T D), \langle i, a, k \rangle \in \mathbb {P}
$$

as the operator procedure, where a is the node to be relocated and i and k are two nodes in TD. There are two possibilities for effects: (1) If a is a truckonly node, this move creates a new drone delivery $\langle i , a , k \rangle$ in DD and removes a from TD; (2) if a is a drone node, the move changes the drone delivery $\left\langle \cdot , a , \cdot \right\rangle \in D D \; \mathrm { t o } \; \left\langle i , a , k \right\rangle$

Drone removal: In this move operator, we choose a drone node $j \in N _ { D }$ and replace the drone delivery by a truck delivery. An example is shown in Figure 5. In detail, we denote

$$
\text {remove} _ {D} ((T D, D D), j, k), j \notin T D, \langle \cdot , j, \cdot \rangle \in D D, k \in T D, k \neq \{0 \}\tag{57}
$$

as the operator procedure, where $j$ is the drone node to be removed and k is a node in TD such that j will be inserted before k. As a result, we have a new solution in which the number of nodes in TD has been increased by one and DD’s cardinality has been decreased by one.

Two-exchange: We exchange the position of two nodes. There are three possibilities: (1) When the exchanged nodes are both drone nodes, we make the change in the drone delivery list; (2) when the exchanged nodes are both truck nodes, we first exchange their positions in the truck sequence and then apply changes in the drone delivery list; and (3) when the exchanged nodes are a truck node and a drone node, we remove the old tuple and create a new one with the exchanged node. Next, we update the truck sequence and apply the changes to the tuples if the truck node is associated with any drone delivery. An example is shown in Figure 6. In detail, we denote

$$
\text {two\_exchange} ((T D, D D), a, b), a, b \in V \setminus \{0, n + 1 \}, a \neq b\tag{58}
$$

as the operator procedure, where a and b are the two nodes to be exchanged. We then swap their positions. The three swap possibilities are as follows: (1) a drone node with a node in TD; (2) two drone nodes; and (3) two nodes in TD.

To ensure the feasibility of resulting solutions, we only accept the moves which satisfy the constraints of the problem. And finally, our local search operators are easily adapted to deal with the min-time objective. They work on the travel time instead of the travel cost of each arc. Whenever there is a need to update a travel time of a drone delivery, we need to take the greater value between travel times of drone and truck instead of the summation. The mechanism of the rest of the local search then stays untouched.

![](images/page_29_image_0.jpg)

Figure 3: A truck relocation move operator : relocate<sub>T</sub>((TD, DD), 1, 2)

![](images/page_29_image_2.jpg)

Figure 4: A drone relocation move operator : relocate<sub>D</sub>((TD, DD), 1, 5, 4)

![](images/page_29_image_4.jpg)

Figure 5: A drone removal move operator : remove<sub>D</sub>((TD, DD), 2)

## 485 5. TSP-LS heuristic

The TSP-LS algorithm is adapted from the work of [12] to solve the mincost TSP-D. The differences between min-time FSTSP and the adapted mincost TSP-LS are at the calculation of cost savings (Algorithm 6), the cost of relocating a truck node to another position (Algorithm 7) and the cost of inserting a node as a drone node between two nodes in the truck tour (Algorithm 8). These changes are not only about the unit of measurement (time vs. cost) but also the waiting cost of two vehicles. We now describe the algorithm in details.

![](images/page_30_image_4.jpg)

Figure 6: A two-exchange move operator in which a drone node is exchanged with a truck node: two\_exchange((TD, DD), 3, 2)

The algorithm starts by calculating a TSP tour and then repeatedly re locates customers until no more improvement can be reached. The outline is shown in Algorithm 5. Lines 1–8 define the global variables, which are $C u s t o m e r s   =   [ 1 , 2 , \cdots , n ]$ , the sequence of truck nodes—truckRoute, and an indexed list truckSubRoutes of smaller sequences that represent the subroutes in truckRoute. The distinct combination of elements in truckSubRoutes must be equal to truckRoute. We define $i ^ { * } , j ^ { * } , k ^ { * }$ , where $j ^ { * }$ is the best candidate for relocation and $i ^ { * }$ and $k ^ { * }$ denote the positions between which $j ^ { * }$ will be inserted. We also store maxSavings which is the cost improvement value of this relocation. The two Boolean variables isDroneNode and Stop respectively determine whether a node in a subroute is a drone node and whether TSP-LS should terminate. These global variables are updated during the iterations, and the heuristic terminates when no more positive maxSavings can be achieved (maxSavings = 0).

```matlab
Algorithm 5: TSP-LS heuristic
Data: truck-only sequence truckRoute
Result: TSP-D solution sol
Customers = N ;
truckRoute = solveTSP(N);
truckSubRoutes = {truckRoute};
sol = (truckRoute, Ø);
i* = -1;
j* = -1;
k* = -1;
maxSavings = 0;
isDroneNode = null;
Stop = false;
repeat
    foreach j ∈ Customers do
        savings = calcSavings(j) ;
        foreach subroute in truckSubRoutes do
            if drone(subroute, sol) then
                (isDroneNode, maxSavings, i*, j*, k*) =
                    relocateAsTruck(j, subroutine, savings);
            else
                (isDroneNode, maxSavings, i*, j*, k*) =
                    relocateAsDrone(j, subroutine, savings);
    if maxSavings > 0 then
        (sol, truckRoute, truckSubRoutes, Customers) =
            applyChanges(isDroneNode, i*, j*, k*,
                sol, truckRoute, truckSubRoutes, Customers);
        maxSavings = 0 ;
    else
        Stop = true;
until Stop;
```

For an additional notation used in Algorithm 5, line 15, given a solution (TD, DD), we denote drone $\left( s , \left( T D , D D \right) \right) \in \left\{ T r u e , F a l s e \right\}$ as True if the subsequence s in TD is associated with a drone:

$$
\text {drone} (s, (T D, D D)) = \left\{ \begin{array}{l l} \text {True} & \text {if} \exists j \in V (s), j \neq \text {first} (s), \\ & j \neq \text {last} (s): \langle \text {first} (s), j, \text {last} (s) \rangle \in D D; \\ \text {False} & \text {if} \forall j \in V (s), j \neq \text {first} (s), \\ & j \neq \text {last} (s): \langle \text {first} (s), j, \text {last} (s) \rangle \notin D D. \end{array} \right.
$$

In detail, each iteration has two steps: (1) Consider each customer in Customers to determine the best candidate for relocation along with its new position and the cost savings. (2) If the candidate relocation can improve the current solution, then relocate the customer by updating truckRoute and truckSubRoutes and remove it from Customers so that it will not be considered in future iterations; otherwise (when the candidate relocation cannot improve the current solution), the relocation terminates. We now explain each step and its implementations in Algorithms 5, 6, 7, 8, 9.

Step 1 of the iteration is presented from lines 12 to 18 in Algorithm 5. It first considers each customer $j$ (line 12) and then calculates the cost savings by removing $j$ from its current position (line 13). The calculation is shown in Algorithm 6. Next, line 14 considers each subroute in truckSubRoute as a possible target for the relocation of j. When the current considered subroute is a **drone delivery** (line 15), we then try to relocate $j$ into this subroute as a truck node (line 16); otherwise, we try to relocate $j$ as a drone node to create a new **drone delivery** (line 18). The relocation analyses of $j$ as a truck node or a drone node are presented in Algorithms 7 and $8 ,$ respectively.

<div class="docvortex-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Algorithm 6: calcSavings(j)
    Data: $j$ : a customer currently assigned to the truck
    Result: Solution
$i = prev_{truckRoute}(j)$;
$k = next_{truckRoute}(j)$;
$savings = (d_{i,j} + d_{j,k} - d_{i,k})C_1$;
if $j$ is associated with a drone delivery in subroutine $s$ then
    $i = first(s)$;
    $k = last(s)$;
    $w = \alpha \times max(0, t_{i \to k} - \tau_{ij} - \tau_{jk} + \tau_{ik} - t'_{ijk})$;
    $w' = \beta \times max(0, t'_{ijk} - (t_{i \to k} - \tau_{ij} - \tau_{jk} + \tau_{ik}))$;
    $savings = savings + w + w'$
return savings;
</div>

In Algorithm 7, we aim to find the best position in subroute s to insert the current customer under consideration j by checking each pair of adjacent nodes i and k in s (line 3). After that, if the cost of inserting j in this position is less than the current savings, then relocating j here results in some savings (line 5). Furthermore, because this subroute has a **drone delivery**, we need to check whether inserting j into it still lies within the drone’s power limit so that the truck can still pick up the drone (line 6). Finally, if the cost saved is below the best known maxSavings, we apply the changes to this location by updating the values of isDroneNode, $i ^ { * } , j ^ { * } , k ^ { * }$ and maxSavings (lines 7 to 10).

<div class="docvortex-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Algorithm 7: relocateAsTruck(j, subroute, savings)—Calculates the cost of relocating the customer $j$ into a different position in the truck's route
Data:
$j$: current customer under consideration
$s$: current subroute under consideration
$savings$: savings that occur if $j$ is removed from its current position
Result: Updated $i^*, j^*, k^*$, isDroneNode
$a = \text{first}(s)$;
$b = \text{last}(s)$;
foreach $(i, k) \in A(s)$ do
    $\Delta = (d_{i,j} + d_{j,k} - d_{i,k})C_1$;
    if $\Delta &lt; savings$ then
        if the drone is still feasible to fly then
            if $savings - \Delta &gt; maxSavings$ then
                isDroneNode = False;
                $j^* = j; i^* = i; k^* = k$;
                $maxSavings = savings - \Delta$;
return (isDroneNode, maxSavings, $i^*, j^*, k^*$);
</div>

In Algorithm 8, we consider the relocation of a customer j in a subroute s that does not have **drone delivery**. The objective is simple: try to make j be come the drone node of this subroute to reduce the cost. Hence, we consider each pair of i and k in s, where i precedes k (line 1, 2), and check whether $\langle i , j , k \rangle$ could be a viable **drone delivery** (line 3). We then calculate the cost of this change in lines 4–6. Next, we check whether the relocation is better than the best known maxSavings in line 7. Finally, we update the relocation information in lines 8–10 as in Algorithm 7

<div class="docvortex-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Algorithm 8: relocateAsDrone(j, subroute, savings) - Calculates the cost of relocating customer $j$ as a drone node
Data:
$j$: current considered customer
$s$: current considered subroutine
$savings$: current savings if $j$ is removed from its position
Result: Updated $i^*, j^*, k^*$, isDroneNode
for $i = 0$ to size(s) - 2 do
    for $k = i + 1$ to size(s) - 1 do
        if $\langle s[i], j, s[k] \rangle \in \mathbb{P}$ then
            $w_k =$ waiting cost of truck at $k$ if $j$ is drone node ;
            $w'_k =$ waiting cost of drone at $k$ if $j$ is drone node ;
            $\Delta = (d'_{s[i],j} + d'_{j,s[k]})C_2 + w_k + w'_k$ ;
            if $savings - \Delta &gt; maxSavings$ then
                isDroneNode = True;
                $j^* = j; i^* = s[i]; k^* = s[k]$;
                $maxSavings = savings - \Delta$;
return (isDroneNode, maxSavings, $i^*, j^*, k^*$);
</div>

In step 2 of the iteration in Algorithm 9, when any cost reduction $\mathbf { e x } -$ ists (maxSavings $\neq 0 )$ , we apply the changes based on the current values of $i ^ { * } , j ^ { * } , k ^ { * } ,$ , andisDroneNode. If isDroneNode = True, we relocate $j ^ { * }$ between $i ^ { * }$ and $k ^ { * }$ as a drone node, forming a drone delivery (line 1 to 5). Otherwise, $j ^ { * }$ is inserted as a normal truck node (line 6 to 8). More specifically, these changes take place on the truckRoute and truckSubRoutes. Returning to Algorithm 5, after the changes have been applied in line 18, we reset the value of maxSavings to 0 to prepare for the next iteration. Moreover, the algorithm terminates when maxSavings = 0 (line 21).

<div class="docvortex-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Algorithm 9: applyChanges function
    Data: isDroneNode, $i^*$, $j^*$, $k^*$, sol, truckRoute, truckSubRoutes, Customers
    Result: Updated truckRoute, truckSubRoutes, t
if isDroneNode == True then
    The Drone is now assigned to $i^* \to j^* \to k^*$;
    Remove $j^*$ from truckRoute and truckSubRoutes;
    Append a new truck subroutine that starts at $i^*$ and ends at $k^*$;
    Remove $i^*$, $j^*$, $k^*$ from Customers;
else
    Remove $j^*$ from its current truck subroutine;
    Insert $j^*$ between $i^*$ and $k^*$ in the new truck subroutine ;
Update sol using truckRoute and truckSubRoutes ;
return (sol, truckRoute, truckSubRoutes, Customers);
</div>

## 6. Experiment setup

For the experiments, we generate customer locations randomly on a plane. We consider graphs with 10, 50 and 100 customers. These customers are created in squares with three different areas: 100 $k m ^ { 2 } ,$ 500 $k m ^ { 2 }$ and $1 0 0 0 \; k m ^ { 2 }$ An instance of the TSP-D is characterised by: customer locations, total area of the plane, drone endurance, depot location as well as speed, distance types, travelling cost and time of each vehicle, drone launch time and retrieve time. In total, 65 instances are generated; their characteristics are partially shown in Table 1:

| Instances | # of Customers | Area (km<sup>2</sup>) | Density | Distance (km) | \|P\| |
| --- | --- | --- | --- | --- | --- |
| A1 to A5 | 10 | 100 | 1 | 7.43 | 595 |
| B1 to B10 | 50 | 100 | 0.5 | 7.13 | 73053 |
| C1 to C10 | 50 | 500 | 0.1 | 15.45 | 10005 |
| D1 to D10 | 50 | 1000 | 0.05 | 22.19 | 2932 |
| E1 to E10 | 100 | 100 | 1 | 7.14 | 590144 |
| F1 to F10 | 100 | 500 | 0.2 | 15.21 | 81263 |
| G1 to G10 | 100 | 1000 | 0.1 | 21.59 | 24666 |

Table 1: Instances of min-cost TSP-D

The numbers in this table represent the average values over each class of instances. Three first columns "Instances", "# of Customers", and "Area" are self-explained. Column "Density" represents the number of customers generated in an area unit while column "Distance" indicates the average Euclidean distance among customers. And finally, column "|P|" implies the number of possible drone deliveries.

For all instances, the speeds of drone and truck are both set to 40 km/h. Moreover, $d _ { i j }$ is calculated using Manhattan distance, while $d _ { i j } ^ { \prime }$ is in Euclidean distance. The objective here is to partially simulate the fact that the truck has to travel through a road network (which is longer) and the drone can fly directly from an origin to a destination. The drone’s endurance e is set to 20 minutes of flight time. The truck’s cost $C _ { 1 }$ is by default set to 25 times the drone’s cost $C _ { 2 } .$ . Depot location is at the bottom left of the square. To simulate the real situation where not all packages can be delivered by drone, in all instances, only 80 % of customers can be served by drone. Waiting penalty coefficients α and $\beta$ are set to 10. And finally, the launch time $s _ { L }$ and retrieve time $s _ { R }$ are all set to 1 minute, as in [12].

For the results, we denote $\gamma , T ,$ and $\rho$ as the objective value, running time in seconds and performance ratio, respectively, defined as follows:

$$
\rho = \frac{\text{value}}{\text{referenceValue}}\times 100,\tag{59}
$$

where value is the objective value obtained by the considering algorithm and re f erenceValue is the objective value obtained by a reference algorithm. We will specify these algorithms for each experiment. Because we are dealing with a minimization problem, a ratio $\rho$ less than 100 % means that the considered algorithm provides a better solution than the reference algorithm. Furthermore, we denote σ the relative standard deviation percentage in multiple runs. The objective value, running time and performance ratio on average are denoted as $\gamma _ { a v g } , T _ { a v g } ,$ and $\rho _ { a v g }$ . In addition, the geometric mean, which is more appropriate than the arithmetic mean when analysing normalized performance numbers, is used to calculate the values of $\rho _ { a v g } , T _ { a v g }$ (see [30] for more information).

CPLEX 12.6.2 is used whenever the MILP formulation needs to be solved, and optimal TSP tours are obtained with the state-of-the-art Concorde solver [31]. The values of k in k-nearest neighbour and k-cheapest insertion heuristics are chosen randomly between {2, 3} to give the best results. Also by experiment, the value of parameter $n _ { T S P }$ of GRASP is set to 2000 in all tests. And finally, all instances and detailed results are available at [http://research.haquangminh.com/tspd/index](http://research.haquangminh.com/tspd/index).

## 7. Results

In this section, we present and analyse the computational results obtained by the proposed methods. The algorithms are implemented in C++ and run on an Intel Core i7-6700 @ 3.4 GHz processor. Different experiments have been carried out to evaluate the performance of the proposed methods and analyse the impact of parameters: explore the performance of GRASP on different TSP-tour construction heuristics in min-cost TSP-D, compare min-cost TSP-D solutions provided by the proposed heuristics and optimal solutions computed from the MILP formulation (if possible), compare min-cost TSP-D solutions with TSP solutions $( \mathbf { i . e . } ,$ no drone delivery), compare GRASP with TSP-LS on min-cost TSP-D instances, analyse the impact of the drone/truck cost ratio in min-cost TSP-D, and verify heuristics’ performance under mintime objective as well as the trade-off between two objectives.

## 7.1. Performance of GRASP on different TSP-tour construction heuristics in the mincost TSP-D

In this subsection, we evaluate the performance of GRASP under three proposed TSP construction heuristics in the min-cost TSP-D. We also analyse the impact of the local search operators on the behaviour of GRASP. For each instance set labeled from B to $\mathbf { G } _ { r }$ we select 3 instances. Then each combination of instance and TSP construction heuristic will be run 10 times. With 18 instances, 3 heuristics, 2 local search settings (enable/disable), we have in total: $1 8 \times 3 \times 1 0 \times 2 = 1 0 8 0$ tests. We use TSP optimal solutions (obtained by Concorde) as reference re f erenceValue to calculate the performance ratios $\rho .$

The columns $\rho _ { a v g } ^ { t s p }$ represent the performance ratio on average of TSP solutions obtained by TSP tour generation heuristics. The columns $\rho _ { a v g } ^ { w i t h L S } ,   \rho _ { a v g } ^ { n o L S }$ respectively report the performance ratio on average of GRASP with and without local search. The results are presented in Table 2.

<table><tbody><tr><td>Instance</td><td colspan="5">k-nearest neighbour</td><td colspan="5">k-cheapest insertion</td><td colspan="5">random insertion</td></tr><tr><td></td><td>ρ<sup>w</sup><sub>av</sub><sup>i</sup><sub>g</sub><sup>thLS</sup></td><td>σ</td><td>T<sub>avg</sub></td><td>ρ<sup>t</sup><sub>a</sub><sup>s</sup><sub>v</sub><sup>p</sup><sub>g</sub></td><td>ρ<sup>n</sup><sub>av</sub><sup>o</sup><sub>g</sub><sup>LS</sup></td><td>ρ<sup>w</sup><sub>av</sub><sup>i</sup><sub>g</sub><sup>thLS</sup></td><td>σ</td><td>T<sub>avg</sub></td><td>ρ<sup>t</sup><sub>a</sub><sup>s</sup><sub>v</sub><sup>p</sup><sub>g</sub></td><td>ρ<sup>n</sup><sub>av</sub><sup>o</sup><sub>g</sub><sup>LS</sup></td><td>ρ<sup>w</sup><sub>av</sub><sup>i</sup><sub>g</sub><sup>thLS</sup></td><td>σ</td><td>T<sub>avg</sub></td><td>ρ<sup>t</sup><sub>a</sub><sup>s</sup><sub>v</sub><sup>p</sup><sub>g</sub></td><td>ρ<sup>n</sup><sub>av</sub><sup>o</sup><sub>g</sub><sup>LS</sup></td></tr><tr><td>B1</td><td>66.33</td><td>1.26</td><td>8.57</td><td>142.12</td><td>82.55</td><td>66.80</td><td>0.27</td><td>6.94</td><td>117.31</td><td>77.20</td><td>69.92</td><td>1.44</td><td>66.70</td><td>409.23</td><td>187.15</td></tr><tr><td>B2</td><td>74.33</td><td>0.66</td><td>8.66</td><td>146.05</td><td>82.25</td><td>75.72</td><td>1.45</td><td>4.56</td><td>115.86</td><td>82.79</td><td>75.80</td><td>1.19</td><td>58.83</td><td>420.47</td><td>191.41</td></tr><tr><td>B3</td><td>71.62</td><td>1.22</td><td>9.90</td><td>137.05</td><td>85.11</td><td>75.17</td><td>0.10</td><td>6.09</td><td>117.38</td><td>86.03</td><td>73.80</td><td>1.49</td><td>57.38</td><td>438.95</td><td>209.62</td></tr><tr><td>C1</td><td>71.11</td><td>1.01</td><td>7.09</td><td>143.08</td><td>82.05</td><td>76.66</td><td>1.42</td><td>6.23</td><td>120.74</td><td>85.74</td><td>75.44</td><td>1.37</td><td>43.12</td><td>462.91</td><td>345.88</td></tr><tr><td>C2</td><td>72.66</td><td>0.91</td><td>8.69</td><td>150.82</td><td>81.78</td><td>78.72</td><td>0.83</td><td>6.54</td><td>122.71</td><td>84.65</td><td>75.80</td><td>0.74</td><td>52.65</td><td>498.46</td><td>363.96</td></tr><tr><td>C3</td><td>81.09</td><td>1.58</td><td>5.44</td><td>147.67</td><td>89.66</td><td>83.52</td><td>0.41</td><td>4.67</td><td>115.72</td><td>87.64</td><td>82.46</td><td>1.30</td><td>43.32</td><td>521.19</td><td>389.58</td></tr><tr><td>D1</td><td>77.63</td><td>0.79</td><td>6.97</td><td>146.24</td><td>92.73</td><td>81.16</td><td>0.30</td><td>4.85</td><td>118.39</td><td>89.14</td><td>79.36</td><td>1.30</td><td>58.33</td><td>469.68</td><td>364.12</td></tr><tr><td>D2</td><td>72.69</td><td>0.81</td><td>6.32</td><td>140.80</td><td>91.17</td><td>72.73</td><td>0.84</td><td>6.08</td><td>115.21</td><td>81.73</td><td>75.11</td><td>1.06</td><td>51.61</td><td>459.79</td><td>355.26</td></tr><tr><td>D3</td><td>74.75</td><td>0.74</td><td>5.85</td><td>144.54</td><td>88.93</td><td>85.51</td><td>0.47</td><td>4.27</td><td>123.19</td><td>90.78</td><td>78.04</td><td>1.47</td><td>52.83</td><td>519.60</td><td>388.39</td></tr><tr><td>E1</td><td>70.40</td><td>1.21</td><td>85.40</td><td>137.31</td><td>84.81</td><td>69.69</td><td>0.65</td><td>37.35</td><td>107.67</td><td>76.71</td><td>78.07</td><td>2.12</td><td>605.80</td><td>554.25</td><td>286.11</td></tr><tr><td>E2</td><td>70.64</td><td>1.13</td><td>82.52</td><td>135.61</td><td>85.71</td><td>67.16</td><td>0.46</td><td>41.68</td><td>112.61</td><td>74.89</td><td>79.31</td><td>1.79</td><td>605.82</td><td>560.64</td><td>278.69</td></tr><tr><td>E3</td><td>71.29</td><td>0.64</td><td>85.59</td><td>135.23</td><td>85.79</td><td>70.70</td><td>0.60</td><td>37.46</td><td>108.42</td><td>76.58</td><td>78.93</td><td>1.91</td><td>605.99</td><td>561.45</td><td>283.99</td></tr><tr><td>F1</td><td>75.12</td><td>1.27</td><td>67.42</td><td>144.97</td><td>94.16</td><td>78.12</td><td>0.56</td><td>51.06</td><td>115.20</td><td>84.60</td><td>86.37</td><td>1.27</td><td>604.38</td><td>614.22</td><td>512.49</td></tr><tr><td>F2</td><td>74.62</td><td>1.40</td><td>81.67</td><td>148.48</td><td>93.44</td><td>77.08</td><td>1.19</td><td>73.21</td><td>120.45</td><td>86.02</td><td>82.57</td><td>2.44</td><td>604.33</td><td>647.65</td><td>529.60</td></tr><tr><td>F3</td><td>76.44</td><td>1.27</td><td>80.90</td><td>137.19</td><td>93.56</td><td>79.26</td><td>0.91</td><td>63.74</td><td>120.15</td><td>87.27</td><td>85.02</td><td>2.41</td><td>604.39</td><td>662.81</td><td>527.52</td></tr><tr><td>G1</td><td>78.18</td><td>1.81</td><td>69.73</td><td>149.72</td><td>95.99</td><td>81.37</td><td>0.87</td><td>64.65</td><td>125.09</td><td>89.75</td><td>87.29</td><td>1.51</td><td>604.16</td><td>682.44</td><td>570.93</td></tr><tr><td>G2</td><td>78.28</td><td>1.36</td><td>90.76</td><td>148.37</td><td>97.76</td><td>81.96</td><td>0.73</td><td>84.38</td><td>118.48</td><td>89.63</td><td>88.66</td><td>0.83</td><td>604.18</td><td>749.13</td><td>623.78</td></tr><tr><td>G3</td><td>74.19</td><td>1.04</td><td>89.86</td><td>146.62</td><td>95.86</td><td>72.22</td><td>0.99</td><td>84.66</td><td>120.03</td><td>82.26</td><td>81.75</td><td>2.18</td><td>604.20</td><td>662.59</td><td>556.53</td></tr><tr><td>Mean</td><td>73.88</td><td></td><td>24.44</td><td>143.35</td><td>88.92</td><td>76.12</td><td></td><td>17.72</td><td>117.39</td><td>83.94</td><td>79.50</td><td></td><td>179.69</td><td>541.23</td><td>362.85</td></tr></tbody></table>

Table 2: Performance of GRASP on TSP-tour construction heuristics in min-cost TSP-D

In overall, GRASP with k-nearest neighbour provided the best performance in terms of solution quality, followed by k-cheapest insertion and then random insertion. It is well-known that greedy algorithms such as nearest neighbour and cheapest insertion give better solutions for the TSP than totally random insertion algorithm does (as confirmed again by the columns "ρtspavg" the use of good TSP tours is an important factor to improve the quality of our GRASP. However, although k-cheapest insertion in general gives better TSP tours than k-nearest neighbour, TSP-D solutions obtained from k-nearest neighbour are better than ones obtained from k-cheapest insertion. The reason could be due to our local search operators which seems to work better with k-nearest neighbour. In GRASP with k-cheapest insertion, the local search op erators in general converge more prematurely. And as a result, GRASP with k-cheapest insertion stops earlier than GRASP with k-nearest neighbour. In addition, we carried out some additional tests and found that, in general, using optimal TSP tours does not provide best solutions for the min-cost TSP-D.

Furthermore, all three heuristics provided stable results with most of standard deviations σ less than 2 %. More precisely, GRASPs with k-nearest neighbour and k-cheapest insertion are more stable than GRASP using random insertion heuristic. From these analyses, we decide to use k-nearest neighbour heuristic to generate TSP tours for GRASP in the next experiments.

## 7.2. Comparison with min-cost TSP-D optimal solutions

In this section, to validate the MILP formulation, we report the results obtained by CPLEX. We also wish to observe the possibility that finds optimal solutions of two approximate approaches GRASP and TSP-LS. The preliminary experiments show that the MILP formulation cannot solve to optimality instances with more than 10 nodes under a time limit of 1 hour. Therefore, in this subsection, we use only the 10-customer instances to compare the solutions obtained by GRASP, TSP-LS and ordinary TSP with the optimal solutions of the min-cost TSP-D computed through the MILP formulation. The re f erenceValue used to compute the ratio $\rho$ is the optimal min-cost TSP-D solution. For each instance, GRASP is repeatedly run 10 times and we record the number of times (in Column opt) it can reach the optimality. The comparison results reported in Table 3 show that GRASP can find all optimal solutions consuming much less computation time than the MILP formulation. On the other hand, although TSP-LS is faster, it can only find one optimal solution. It is clear that GRASP outperforms TSP-LS in terms of solution quality. In details, GRASP shows a stable performance with standard deviation of 0 (which reported in Column σ) and can reach to optimality in all cases. From the column "TSP", we observe that using the drone allows to save more than 20 % and up to 53 % of operational costs. Next, we focus on analysing the performance of GRASP and TSP-LS on the larger instances.

<table><tbody><tr><td rowspan="2">Instance</td><td colspan="2">TSP</td><td colspan="2">MILP formulation</td><td colspan="5">GRASP</td><td colspan="3">TSP-LS</td></tr><tr><td>γ</td><td>ρ</td><td>γ</td><td>T</td><td>γ<sub>avg</sub></td><td>T<sub>avg</sub></td><td>ρ<sub>avg</sub></td><td>σ</td><td>opt</td><td>γ</td><td>T</td><td>ρ</td></tr><tr><td>A1</td><td>1007.33</td><td>153.01</td><td>658.322</td><td>46.64</td><td>658.322</td><td>0.84</td><td>100</td><td>0</td><td>10</td><td>810.244</td><td>0.013</td><td>123.07</td></tr><tr><td>A2</td><td>955.876</td><td>140.58</td><td>679.932</td><td>144.51</td><td>679.932</td><td>1.06</td><td>100</td><td>0</td><td>10</td><td>777.119</td><td>0.006</td><td>114.29</td></tr><tr><td>A3</td><td>985.679</td><td>120.31</td><td>819.251</td><td>133.30</td><td>819.251</td><td>0.78</td><td>100</td><td>0</td><td>10</td><td>819.251</td><td>0.005</td><td>100</td></tr><tr><td>A4</td><td>944.645</td><td>126.22</td><td>748.405</td><td>41.31</td><td>748.405</td><td>1.70</td><td>100</td><td>0</td><td>10</td><td>834.89</td><td>0.007</td><td>111.55</td></tr><tr><td>A5</td><td>985.679</td><td>121.60</td><td>810.567</td><td>57.18</td><td>810.567</td><td>1.63</td><td>100</td><td>0</td><td>10</td><td>853.728</td><td>0.005</td><td>105.32</td></tr></tbody></table>

Table 3: Comparison with the min-cost TSP-D optimal solution.

## 7.3. Performance of heuristics on the larger instances in the min-cost TSP-D

In this subsection, we aim to analyse the performance of GRASP and TSP-LS on the larger min-cost TSP-D instances—those with 50 and 100 customers. Two methods TSP-LS and GRASP are tested and obtained solutions are compared with ones of the ordinary TSP. The re f erenceValue used to compute the ratio $\rho$ is the objective value of the TSP optimal solution. For each instance, we also report the average waiting times of truck and drone as well as the average latest time at which either the truck or the drone return to the depot (Column $w _ { a v g } , w _ { a v g } ^ { \prime }$ and $t _ { a v g } )$ . These values are measured in minutes. Again, for each instance, GRASP is repeatedly run 10 times. Tables 4 and 5 show the results for the instances with 50 and 100 customers, respectively.

As can be observed, GRASP outperforms TSP-LS in terms of solution quality. In terms of running time, GRASP runs slower. However, considering that it never runs in more than 4 minutes, while performs up to 7 % better than TSP-LS in terms of $\rho _ { a v g } ,$ this trade-off is worthy.

In all cases, GRASP finds the best solutions. Regardless of slower speed, its average computational time is acceptable on even 100-customer instances (about 2.5 minutes averagely). Furthermore, its relative standard deviation percentage – reported in Column σ – is less than 3% in all instances, proving the stability of the algorithm. The results obtained once again prove the effectiveness of using the drone for delivery. GRASP gives solutions with a cost saving of more than 25 % compared with the TSP optimal solutions, which do not use any drone delivery.

Regarding the waiting times, one can observe that in min-cost TSP-D solutions, truck has to wait for drone most of the time among all instances $( w _ { a v g } > w _ { a v g } ^ { \prime } )$ . In details, while drone’s waiting times are only a couple of minutes, truck’s waiting times make up approximately 25.95% and 26.20% of the delivery completion time $( t _ { a v g } )$ regarding to geometric mean in 50-customer and 100-customer instances, respectively. This could be due to the fact that truck’s transportation cost is much larger than drone’s transportation cost (25 times larger), the min-cost TSP-D solutions tend to select drone deliveries in which flying distance of drone is quite longer than traveling distance of truck.

<table><tbody><tr><td rowspan="2">N = 50</td><td colspan="8">GRASP</td><td colspan="2">TSP-LS</td></tr><tr><td>γ<sub>best</sub></td><td>γ<sub>avg</sub></td><td>ρ<sub>avg</sub></td><td>T<sub>avg</sub></td><td>σ</td><td>wavg</td><td>w<sup>0</sup><sub>avg</sub></td><td>t<sub>avg</sub></td><td>ρ<sub>avg</sub></td><td>T<sub>avg</sub></td></tr><tr><td>B1</td><td>1372.82</td><td>1413.24</td><td>66.59</td><td>16.30</td><td>1.34</td><td>70.48</td><td>0.56</td><td>192.52</td><td>78.62</td><td>0.40</td></tr><tr><td>B2</td><td>1491.30</td><td>1513.98</td><td>73.42</td><td>15.67</td><td>0.48</td><td>36.13</td><td>1.00</td><td>162.78</td><td>77.42</td><td>0.34</td></tr><tr><td>B3</td><td>1503.78</td><td>1521.67</td><td>72.06</td><td>16.70</td><td>0.68</td><td>44.11</td><td>1.57</td><td>165.46</td><td>81.44</td><td>0.28</td></tr><tr><td>B4</td><td>1396.17</td><td>1426.20</td><td>65.33</td><td>15.92</td><td>0.98</td><td>66.97</td><td>0.13</td><td>190.45</td><td>79.38</td><td>1.01</td></tr><tr><td>B5</td><td>1457.91</td><td>1500.90</td><td>71.52</td><td>18.73</td><td>1.51</td><td>53.38</td><td>1.94</td><td>178.12</td><td>81.28</td><td>0.39</td></tr><tr><td>B6</td><td>1316.08</td><td>1353.76</td><td>63.87</td><td>15.94</td><td>1.04</td><td>81.87</td><td>0.57</td><td>198.83</td><td>75.51</td><td>0.30</td></tr><tr><td>B7</td><td>1370.05</td><td>1399.71</td><td>65.90</td><td>14.27</td><td>0.83</td><td>63.16</td><td>1.46</td><td>183.53</td><td>78.69</td><td>0.30</td></tr><tr><td>B8</td><td>1484.93</td><td>1517.23</td><td>73.24</td><td>15.23</td><td>0.95</td><td>60.04</td><td>0.41</td><td>184.35</td><td>83.03</td><td>0.28</td></tr><tr><td>B9</td><td>1442.09</td><td>1468.86</td><td>70.27</td><td>17.05</td><td>0.94</td><td>43.65</td><td>3.87</td><td>168.32</td><td>79.19</td><td>0.31</td></tr><tr><td>B10</td><td>1392.54</td><td>1429.57</td><td>67.94</td><td>15.19</td><td>1.04</td><td>54.40</td><td>0.08</td><td>174.44</td><td>75.62</td><td>0.33</td></tr><tr><td>C1</td><td>2870.41</td><td>2935.87</td><td>71.70</td><td>12.62</td><td>0.88</td><td>112.76</td><td>2.47</td><td>318.15</td><td>79.52</td><td>0.12</td></tr><tr><td>C2</td><td>2804.47</td><td>2868.67</td><td>72.97</td><td>15.74</td><td>0.75</td><td>88.56</td><td>2.43</td><td>293.69</td><td>78.67</td><td>0.12</td></tr><tr><td>C3</td><td>3087.55</td><td>3185.09</td><td>81.87</td><td>9.73</td><td>1.07</td><td>56.35</td><td>4.03</td><td>272.77</td><td>83.06</td><td>0.14</td></tr><tr><td>C4</td><td>2844.10</td><td>2916.86</td><td>70.97</td><td>11.78</td><td>0.70</td><td>91.54</td><td>1.37</td><td>297.05</td><td>82.39</td><td>0.16</td></tr><tr><td>C5</td><td>3323.92</td><td>3367.34</td><td>80.54</td><td>11.40</td><td>0.57</td><td>58.89</td><td>4.72</td><td>286.26</td><td>89.21</td><td>0.09</td></tr><tr><td>C6</td><td>3433.99</td><td>3472.39</td><td>79.79</td><td>11.24</td><td>0.65</td><td>68.47</td><td>3.43</td><td>301.24</td><td>86.71</td><td>0.12</td></tr><tr><td>C7</td><td>3001.13</td><td>3047.71</td><td>71.92</td><td>12.86</td><td>0.64</td><td>105.33</td><td>0.58</td><td>317.15</td><td>80.75</td><td>0.11</td></tr><tr><td>C8</td><td>3481.17</td><td>3557.99</td><td>82.21</td><td>13.07</td><td>1.02</td><td>71.66</td><td>3.02</td><td>312.14</td><td>86.84</td><td>0.10</td></tr><tr><td>C9</td><td>3267.23</td><td>3306.38</td><td>75.35</td><td>11.56</td><td>0.40</td><td>85.48</td><td>0.46</td><td>311.73</td><td>80.09</td><td>0.27</td></tr><tr><td>C10</td><td>3291.20</td><td>3356.29</td><td>78.34</td><td>13.77</td><td>0.84</td><td>74.47</td><td>1.29</td><td>304.23</td><td>82.22</td><td>0.14</td></tr><tr><td>D1</td><td>4159.39</td><td>4389.24</td><td>76.86</td><td>12.87</td><td>1.61</td><td>93.40</td><td>1.61</td><td>382.41</td><td>89.35</td><td>0.10</td></tr><tr><td>D2</td><td>4275.46</td><td>4334.40</td><td>72.32</td><td>11.67</td><td>0.52</td><td>106.81</td><td>2.42</td><td>392.96</td><td>76.75</td><td>0.06</td></tr><tr><td>D3</td><td>4085.71</td><td>4191.08</td><td>75.25</td><td>11.06</td><td>1.01</td><td>92.96</td><td>1.59</td><td>368.91</td><td>82.21</td><td>0.07</td></tr><tr><td>D4</td><td>4612.46</td><td>4714.62</td><td>77.14</td><td>12.74</td><td>0.80</td><td>91.33</td><td>1.96</td><td>399.14</td><td>80.52</td><td>0.11</td></tr><tr><td>D5</td><td>4717.67</td><td>4793.39</td><td>80.26</td><td>11.70</td><td>0.79</td><td>77.54</td><td>0.97</td><td>390.97</td><td>82.89</td><td>0.06</td></tr><tr><td>D6</td><td>4405.02</td><td>4485.87</td><td>78.64</td><td>11.73</td><td>0.79</td><td>78.61</td><td>2.87</td><td>373.53</td><td>85.93</td><td>0.06</td></tr><tr><td>D7</td><td>4749.57</td><td>4796.23</td><td>82.77</td><td>15.06</td><td>0.46</td><td>68.48</td><td>7.74</td><td>384.65</td><td>86.69</td><td>0.07</td></tr><tr><td>D8</td><td>4143.03</td><td>4287.87</td><td>77.71</td><td>11.99</td><td>1.56</td><td>90.75</td><td>1.05</td><td>374.24</td><td>87.62</td><td>0.06</td></tr><tr><td>D9</td><td>4653.73</td><td>4688.16</td><td>76.11</td><td>13.39</td><td>0.50</td><td>86.84</td><td>4.82</td><td>392.72</td><td>86.34</td><td>0.17</td></tr><tr><td>D10</td><td>4260.60</td><td>4301.83</td><td>75.33</td><td>11.96</td><td>0.41</td><td>91.95</td><td>5.98</td><td>375.94</td><td>78.89</td><td>0.08</td></tr><tr><td>Mean</td><td></td><td></td><td>74.09</td><td>13.46</td><td></td><td></td><td></td><td></td><td>81.80</td><td>0.15</td></tr><tr><td rowspan="2">N = 100</td><td colspan="8">GRASP</td><td colspan="2">TSP-LS</td></tr><tr><td>γ<sub>best</sub></td><td>γ<sub>avg</sub></td><td>ρ<sub>avg</sub></td><td>T<sub>avg</sub></td><td>σ</td><td>wavg</td><td>w<sup>0</sup><sub>avg</sub></td><td>t<sub>avg</sub></td><td>ρ<sub>avg</sub></td><td>T<sub>avg</sub></td></tr><tr><td>E1</td><td>2206.53</td><td>2255.99</td><td>70.64</td><td>137.02</td><td>0.96</td><td>81.22</td><td>1.75</td><td>293.35</td><td>76.22</td><td>5.52</td></tr><tr><td>E2</td><td>2210.61</td><td>2273.09</td><td>70.53</td><td>136.68</td><td>1.08</td><td>77.09</td><td>2.21</td><td>288.01</td><td>76.26</td><td>5.90</td></tr><tr><td>E3</td><td>2248.16</td><td>2312.76</td><td>71.43</td><td>148.62</td><td>1.09</td><td>77.57</td><td>1.71</td><td>287.39</td><td>72.41</td><td>6.09</td></tr><tr><td>E4</td><td>2179.06</td><td>2223.97</td><td>70.35</td><td>178.37</td><td>0.90</td><td>75.97</td><td>1.69</td><td>282.29</td><td>78.14</td><td>6.02</td></tr><tr><td>E5</td><td>2286.16</td><td>2360.30</td><td>73.58</td><td>172.10</td><td>1.31</td><td>60.15</td><td>2.26</td><td>269.52</td><td>77.85</td><td>6.17</td></tr><tr><td>E6</td><td>2244.62</td><td>2313.86</td><td>71.89</td><td>195.51</td><td>1.05</td><td>74.50</td><td>1.87</td><td>286.99</td><td>78.14</td><td>5.89</td></tr><tr><td>E7</td><td>2249.09</td><td>2313.67</td><td>71.94</td><td>190.84</td><td>0.90</td><td>67.23</td><td>2.28</td><td>279.10</td><td>82.33</td><td>6.32</td></tr><tr><td>E8</td><td>2220.88</td><td>2272.55</td><td>70.66</td><td>189.24</td><td>0.79</td><td>71.45</td><td>1.40</td><td>280.26</td><td>72.37</td><td>6.64</td></tr><tr><td>E9</td><td>2279.91</td><td>2326.29</td><td>72.33</td><td>172.03</td><td>0.83</td><td>67.60</td><td>1.72</td><td>277.53</td><td>74.74</td><td>5.72</td></tr><tr><td>E10</td><td>2324.74</td><td>2384.52</td><td>74.30</td><td>204.74</td><td>0.96</td><td>64.16</td><td>1.94</td><td>277.90</td><td>77.23</td><td>4.98</td></tr><tr><td>F1</td><td>4569.83</td><td>4648.20</td><td>76.20</td><td>111.07</td><td>0.85</td><td>109.53</td><td>6.36</td><td>443.43</td><td>83.13</td><td>1.23</td></tr><tr><td>F2</td><td>4186.76</td><td>4318.78</td><td>74.74</td><td>143.07</td><td>1.47</td><td>138.73</td><td>2.39</td><td>459.57</td><td>80.43</td><td>1.19</td></tr><tr><td>F3</td><td>4414.38</td><td>4563.64</td><td>76.57</td><td>146.75</td><td>1.31</td><td>119.39</td><td>6.88</td><td>454.68</td><td>81.77</td><td>1.46</td></tr><tr><td>F4</td><td>4499.09</td><td>4600.27</td><td>79.53</td><td>128.53</td><td>1.25</td><td>123.85</td><td>3.15</td><td>456.31</td><td>80.99</td><td>1.38</td></tr><tr><td>F5</td><td>4381.37</td><td>4597.32</td><td>76.34</td><td>159.76</td><td>1.66</td><td>129.97</td><td>1.88</td><td>464.85</td><td>80.65</td><td>1.13</td></tr><tr><td>F6</td><td>4032.90</td><td>4171.80</td><td>74.54</td><td>157.70</td><td>1.53</td><td>130.63</td><td>3.55</td><td>442.99</td><td>79.74</td><td>1.06</td></tr><tr><td>F7</td><td>4076.31</td><td>4213.52</td><td>72.64</td><td>170.14</td><td>1.62</td><td>159.33</td><td>1.44</td><td>478.18</td><td>74.39</td><td>1.29</td></tr><tr><td>F8</td><td>4491.20</td><td>4597.90</td><td>75.37</td><td>165.96</td><td>0.98</td><td>126.90</td><td>4.52</td><td>464.09</td><td>82.89</td><td>1.31</td></tr><tr><td>F9</td><td>4388.91</td><td>4463.39</td><td>75.24</td><td>153.04</td><td>0.90</td><td>124.91</td><td>3.43</td><td>455.09</td><td>83.62</td><td>1.52</td></tr><tr><td>F10</td><td>4173.64</td><td>4567.84</td><td>76.48</td><td>153.99</td><td>2.31</td><td>118.52</td><td>3.07</td><td>451.57</td><td>80.48</td><td>1.51</td></tr><tr><td>G1</td><td>5947.97</td><td>6148.50</td><td>77.05</td><td>116.24</td><td>1.61</td><td>163.73</td><td>3.72</td><td>589.97</td><td>79.66</td><td>0.65</td></tr><tr><td>G2</td><td>5882.97</td><td>5987.64</td><td>79.70</td><td>158.00</td><td>0.76</td><td>118.74</td><td>5.14</td><td>532.92</td><td>81.70</td><td>0.52</td></tr><tr><td>G3</td><td>6074.57</td><td>6138.94</td><td>74.64</td><td>169.26</td><td>0.80</td><td>163.40</td><td>2.78</td><td>585.57</td><td>78.02</td><td>1.03</td></tr><tr><td>G4</td><td>6458.96</td><td>6632.14</td><td>82.34</td><td>143.47</td><td>1.16</td><td>135.84</td><td>5.02</td><td>588.44</td><td>85.79</td><td>0.90</td></tr><tr><td>G5</td><td>6198.95</td><td>6329.25</td><td>80.46</td><td>155.52</td><td>0.73</td><td>127.68</td><td>4.00</td><td>563.97</td><td>82.04</td><td>0.58</td></tr><tr><td>G6</td><td>6049.34</td><td>6343.26</td><td>77.02</td><td>177.07</td><td>1.69</td><td>149.52</td><td>6.42</td><td>589.69</td><td>81.67</td><td>0.64</td></tr><tr><td>G7</td><td>5889.08</td><td>6023.11</td><td>75.66</td><td>171.24</td><td>0.88</td><td>141.96</td><td>4.50</td><td>557.86</td><td>75.98</td><td>0.81</td></tr><tr><td>G8</td><td>5599.55</td><td>5871.96</td><td>71.99</td><td>156.90</td><td>1.87</td><td>159.24</td><td>6.95</td><td>570.88</td><td>80.03</td><td>0.86</td></tr><tr><td>G9</td><td>6050.80</td><td>6254.50</td><td>74.29</td><td>184.69</td><td>1.48</td><td>174.62</td><td>2.73</td><td>609.20</td><td>80.87</td><td>0.89</td></tr><tr><td>G10</td><td>6249.69</td><td>6534.13</td><td>79.63</td><td>162.11</td><td>1.97</td><td>124.85</td><td>6.79</td><td>572.85</td><td>83.47</td><td>0.78</td></tr><tr><td>Mean</td><td></td><td></td><td>74.87</td><td>158.77</td><td></td><td></td><td></td><td></td><td>79.36</td><td>1.79</td></tr></tbody></table>

Table 4: Performance of heuristics on 50-customer instances in the min-cost $T S P { \text-- } D$

## 7.4. Impact of cost ratio in the min-cost TSP-D

In this experiment, we explore the impact of the drone/truck cost ratio on the objective values of the min-cost TSP-D solutions provided by the GRASP and TSP-LS algorithms. By default, this parameter is set to 1:25; therefore, we added two more ratios, 1:10 and 1:50. Table 6 shows the geometric mean values of $\rho _ { a v g }$ for the two heuristics. The re f erenceValue used to compute the ratio $\rho$ is the objective value of the TSP optimal solution. Again, for each instance, GRASP is repeatedly run 10 times.

Logically, the value of $\rho _ { a v g }$ should decrease as the ratio increases. However, it does not reduce proportionally. More specifically, for GRASP, when the ratio changes from 1:10 to 1:25, the mean of $\rho _ { a v g }$ decreases by approximately 5% for the 50-customer instances and approximately 6% for the 100-customer instances. In contrast, as the ratio changes from 1:25 to 1:50, the mean of $\rho _ { a v g }$ decreases by only approximately 3% in both cases. The same phenomenon is observed for TSP-LS. Consequently, when constructing distribution networks for drone/truck combinations, overestimating the transportation cost of the drone does not always improve significantly the results. This means that the efficiency of investment in improving the cost ratio should be carefully considered because such an investment may prove more expensive than the savings in operational costs.

Varying the cost ratio does not significantly impact the relative performance between the heuristics. The GRASP still outperforms the TSP-LS in all cases in terms of solution quality but is slower in terms of running time.

<table><tr><td rowspan="2">Cost ratio</td><td colspan="2">N = 50</td><td colspan="2">N=100</td></tr><tr><td>GRASP</td><td>TSP-LS</td><td>GRASP</td><td>TSP-LS</td></tr><tr><td>1:10</td><td>79.41</td><td>84.94</td><td>80.63</td><td>82.92</td></tr><tr><td>1:25</td><td>74.09</td><td>81.80</td><td>74.86</td><td>79.36</td></tr><tr><td>1:50</td><td>71.93</td><td>80.70</td><td>72.53</td><td>78.05</td></tr></table>

Table 6: Performance of heuristics with different cost-ratio settings in min-cost TSP-D.

## 7.5. Performance of heuristics with min-time objective

In this section, we analyse the performance of proposed algorithms under min-time objective. We first compare the solutions provided by GRASP with the best ones found by [12] on 10-customer instances. We then evaluate the performance of these two heuristics on the larger instances proposed in Section 6.

## 7.5.1. Performance on small instances

We now compare the performance of GRASP with Murray et al. - the best recorded results found in [12] on small size instances of 10 customers spreading in a region of 8-mile square. These results have been selected from different approaches proposed in [12] including MILP formulation with Gurobi solver and FSTSP heuristic with different TSP tour constructions (IP, Savings, Nearest Neighbor, and Sweep). The detailed results are presented in Table 7. The best found solutions are appeared in bold. Column e represents the drone’s endurance in minutes, while column "TSP" contains the optimal TSP solution values.

In overall, GRASP performs better than the methods presented in [12]. Among 72 instances, GRASP provides solutions worse than those of Murray et al. in only three instances while improves the results of Murray et al. in 20 instances. These results demonstrate the performance of our algorithm to solve not only min-cost TSP-D but also min-time TSP-D.

| Instance | e | TSP | Murray et al. | GRASP | Instance | e | TSP | Murray et al. | GRASP |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 37v1 | 20 | 57.446 | 56.468 | 56.468 | 40v7 | 20 | 60.455 | 49.996 | 49.470 |
| 37v1 | 40 | 57.446 | 50.573 | 50.573 | 40v7 | 40 | 60.455 | 49.204 | 49.233 |
| 37v2 | 20 | 54.184 | 53.207 | 53.207 | 40v8 | 20 | 73.255 | 62.796 | 62.270 |
| 37v2 | 40 | 54.184 | 47.311 | 47.311 | 40v8 | 40 | 73.255 | 62.270 | 62.033 |
| 37v3 | 20 | 54.664 | 53.687 | 53.687 | 40v9 | 20 | 54.517 | 42.799 | 42.533 |
| 37v3 | 40 | 54.664 | 53.687 | 53.687 | 40v9 | 40 | 54.517 | 42.799 | 42.533 |
| 37v4 | 20 | 67.464 | 67.464 | 67.464 | 40v10 | 20 | 54.055 | 43.076 | 43.076 |
| 37v4 | 40 | 67.464 | 66.487 | 66.487 | 40v10 | 40 | 54.055 | 43.076 | 43.076 |
| 37v5 | 20 | 58.022 | 50.551 | 47.457 | 40v11 | 20 | 60.455 | 49.204 | 49.204 |
| 37v5 | 40 | 58.022 | 45.835 | 45.835 | 40v11 | 40 | 60.455 | 49.204 | 49.204 |
| 37v6 | 20 | 54.184 | 45.176 | 45.145 | 40v12 | 20 | 73.255 | 62.004 | 62.004 |
| 37v6 | 40 | 54.184 | 45.863 | 44.602 | 40v12 | 40 | 73.255 | 62.004 | 62.004 |
| 37v7 | 20 | 54.664 | 49.581 | 49.581 | 43v1 | 20 | 69.586 | 69.586 | 69.586 |
| 37v7 | 40 | 54.664 | 46.621 | 46.754 | 43v1 | 40 | 69.586 | 55.493 | 55.493 |
| 37v8 | 20 | 67.464 | 62.381 | 62.381 | 43v2 | 20 | 72.146 | 72.146 | 72.146 |
| 37v8 | 40 | 67.464 | 59.776 | 59.614 | 43v2 | 40 | 72.146 | 58.053 | 58.053 |
| 37v9 | 20 | 58.022 | 45.985 | 42.585 | 43v3 | 20 | 77.344 | 77.344 | 77.344 |
| 37v9 | 40 | 58.022 | 42.416 | 42.416 | 43v3 | 40 | 77.344 | 69.175 | 69.175 |
| 37v10 | 20 | 54.184 | 42.416 | 41.908 | 43v4 | 20 | 90.144 | 90.144 | 90.144 |
| 37v10 | 40 | 54.184 | 41.729 | 40.908 | 43v4 | 40 | 90.144 | 82.700 | 82.700 |
| 37v11 | 20 | 54.664 | 42.896 | 42.896 | 43v5 | 20 | 69.586 | 55.493 | 53.053 |
| 37v11 | 40 | 54.664 | 42.896 | 42.896 | 43v5 | 40 | 69.586 | 53.447 | 52.093 |
| 37v12 | 20 | 67.464 | 56.696 | 56.696 | 43v6 | 20 | 72.146 | 58.053 | 55.209 |
| 37v12 | 40 | 67.464 | 55.696 | 55.696 | 43v6 | 40 | 72.146 | 52.329 | 52.329 |
| 40v1 | 20 | 54.517 | 49.430 | 49.430 | 43v7 | 20 | 77.344 | 64.409 | 64.409 |
| 40v1 | 40 | 54.517 | 46.886 | 46.886 | 43v7 | 40 | 77.344 | 60.743 | 60.886 |
| 40v2 | 20 | 54.055 | 50.708 | 50.708 | 43v8 | 20 | 90.144 | 77.209 | 77.209 |
| 40v2 | 40 | 54.055 | 46.423 | 46.423 | 43v8 | 40 | 90.144 | 73.967 | 73.727 |
| 40v3 | 20 | 60.455 | 56.102 | 56.102 | 43v9 | 20 | 69.586 | 49.049 | 46.931 |
| 40v3 | 40 | 60.455 | 53.933 | 53.933 | 43v9 | 40 | 69.586 | 47.250 | 46.931 |
| 40v4 | 20 | 73.255 | 69.902 | 69.902 | 43v10 | 20 | 72.146 | 47.935 | 47.935 |
| 40v4 | 40 | 73.255 | 68.397 | 67.917 | 43v10 | 40 | 72.146 | 47.935 | 47.935 |
| 40v5 | 20 | 54.517 | 43.533 | 43.533 | 43v11 | 20 | 77.344 | 57.382 | 56.395 |
| 40v5 | 40 | 54.517 | 43.533 | 43.533 | 43v11 | 40 | 77.344 | 56.395 | 56.395 |
| 40v6 | 20 | 54.055 | 44.076 | 44.076 | 43v12 | 20 | 90.144 | 69.195 | 69.195 |
| 40v6 | 40 | 54.055 | 44.076 | 44.076 | 43v12 | 40 | 90.144 | 69.195 | 69.195 |

Table 7: Comparison between GRASP and the best solutions found by [12]

## 7.5.2. Performance on larger instances

Since larger instances of the min-time TSP-D are not available in the literature, we use the instances proposed in this work to analyse further the performance of GRASP and TSP-LS under min-time objective. Moreover, we vary the drone’s speed among three values 25 km/h, 40 km/h and 55 km/h as in [12]. Again, GRASP is repeatedly run 10 times for each combination of instance and drone’s speed. Some preliminary experiments show that, on many min-time TSP-D instances, solutions provided by GRASP were worse than ones provided by TSP-LS and even ordinary TSP. Upon further investigation, we found out that very few drone deliveries were used and min-time TSP solutions were not far from TSP solutions. As a result, TSP-LS which con structs optimal TSP tours and then improves them with local search operators could perform better than GRASP. In this experiment, we use an additional setting of GRASP that we call GRASP+: only one iteration with an optimal TSP tour is performed.

The results are shown in Table 8. The columns and their descriptions are similar to Tables 4 and 5 in Section 7.3 except that the re f erenceValue used to compute the ratio $\rho$ is the objective value of the TSP optimal solution regarding to traveling time (instead of transportation cost in the previous section). In addition, the average objective value of GRASP+ is reported in minutes in Column γ<sub>avg</sub>.

As can be observed, GRASP has better performance than TSP-LS on 50- customer instances, but performs slightly worse than TSP-LS on 100-customer instances regarding to solution quality. Its solutions are even worse than those of optimal TSP on the instances of class $\mathrm { { } ^ { \prime } E ^ { \prime } }$ . This phenomenon could be due to high launch and retrieve times of drone (totally 2 minutes while the average traveling time of truck between two customers is only about 30 seconds - See Table 1) leading to the low frequency of using drone in min-time TSP-D solutions. This also leads to an observation that, on the instances generated in wider regions, more drone deliveries are used and more savings in objective values of the min-time TSP-D are created. For example, the instances of type "E" have averagely 590,144 possibilities of drone deliveries and 100 customers, but only less than 6 drone deliveries are used (as showed in Table 10 of the next section). But on the instances of types $\mathrm { { } ^ { \prime } F ^ { \prime } }$ and $\mathbf { G }$ , the number of average used drone deliveries increases to 16 and 19, respectively. GRASP is still much slower than TSP-LS due to its higher-level characteristic, but similarly to Section 7.3, its running time is acceptable, slightly more than a minute in terms of geometric mean.

In overall, GRASP+ performs better than TSP-LS on all instance classes in terms of solution quality. Regarding the running time, GRASP+ also runs much faster with the average running time less than 0.1 second. These demonstrate the performance of our Split and local search operators.

In terms of waiting times (Columns $w _ { a v g }$ and $| w _ { a v g } ^ { \prime } \rangle ,$ , we can observe an opposite phenomenon with respect to Section 7.3. Unlike min-cost TSP-D solutions where truck has to wait for drone most of the time $( w _ { a v g }   >   w _ { a v g } ^ { \prime } )$ min-time solutions tend to choose drone deliveries in which drone has to wait for truck $( w _ { a v g } < w _ { a v g } ^ { \prime } )$

<table><tbody><tr><td rowspan="2">Instances</td><td colspan="5">GRASP+</td><td colspan="2">GRASP</td><td colspan="2">TSP-LS</td></tr><tr><td>γ<sub>avg</sub></td><td>ρ<sub>avg</sub></td><td>T<sub>avg</sub></td><td>wavg</td><td>w<sup>0</sup><sub>avg</sub></td><td>ρ<sub>avg</sub></td><td>T<sub>avg</sub></td><td>ρ<sub>avg</sub></td><td>T<sub>avg</sub></td></tr><tr><td>B</td><td>121.2</td><td>95.88</td><td>0.01</td><td>2.51</td><td>21.64</td><td>96.16</td><td>25.64</td><td>97.56</td><td>0.22</td></tr><tr><td>C</td><td>232.8</td><td>92.80</td><td>0.01</td><td>4.93</td><td>28.08</td><td>93.40</td><td>21.09</td><td>94.28</td><td>0.10</td></tr><tr><td>D</td><td>323.4</td><td>92.49</td><td>0.01</td><td>9.14</td><td>29.14</td><td>92.84</td><td>22.33</td><td>94.08</td><td>0.08</td></tr><tr><td>E</td><td>190.2</td><td>98.86</td><td>0.04</td><td>0.14</td><td>30.77</td><td>101.79</td><td>275.08</td><td>98.88</td><td>1.62</td></tr><tr><td>F</td><td>334.8</td><td>94.49</td><td>0.03</td><td>2.97</td><td>52.84</td><td>97.86</td><td>151.60</td><td>96.88</td><td>0.44</td></tr><tr><td>G</td><td>449.4</td><td>92.90</td><td>0.02</td><td>6.34</td><td>51.15</td><td>96.91</td><td>142.16</td><td>95.13</td><td>0.33</td></tr><tr><td>Mean</td><td></td><td>94.54</td><td>0.01</td><td></td><td></td><td>96.45</td><td>64.44</td><td>96.12</td><td>0.27</td></tr></tbody></table>

Table 8: Performance of heuristics of min-time TSP-D

## 7.6. Comparison between min-cost and min-time objectives

In this experiment, we compare the TSP-D under two objectives in terms of performance ratios and the frequency of using drones given the results from Sections 7.3 and 7.5.2. The experimental results are presented in Tables 9 and 10.

In Table 9, Columns $\rho _ { m i n - t i m e } ^ { t i m e }$ and $\rho _ { m i n - t i m e } ^ { c o s t }$ represent the performance ratios of two objective values, i.e. delivery completion time and operational cost, of the best solutions found in min-time TSP-D problems. Similarly, Columns $\rho _ { m i n - c o s t } ^ { t i m e }$ and $\rho _ { m i n - c o s t } ^ { c o s t }$ are delivery completion time and operational cost of the best solution found in min-cost TSP-D problems. Again, the value in performance ratio is the optimal TSP solution calculated in time and $\mathtt { c o s t } ,$ depending on the objective type. In overall, min-time TSP-D solutions not only reduce the delivery completion time but also the operational cost compared to corresponding optimal TSP solutions. In contrast, min-cost TSP-D solutions increase the completion time compared to optimal TSP solutions by up to 56.25 % and 43.55 % for 50 and 100-customer instances. However, min-cost TSP-D solutions can save averagely 30 % of the operational cost compared to 20 % of min-time TSP-D solutions. This proves the importance of the new min-cost objective function in the class of transportation problems with drone.

| Instances | ρ<sup>t</sup><sub>m</sub><sup>im</sup><sub>in</sub><sup>e</sup>-time | ρ<sup>c</sup><sub>m</sub><sup>o</sup><sub>i</sub><sup>s</sup><sub>n</sub><sup>t</sup>-time | ρ<sup>t</sup><sub>m</sub><sup>im</sup><sub>in</sub><sup>e</sup>-cost | ρ<sup>c</sup><sub>m</sub><sup>o</sup><sub>i</sub><sup>s</sup><sub>n</sub><sup>t</sup>-cost |
| --- | --- | --- | --- | --- |
| B | 91.83 | 80.60 | 156.25 | 62.10 |
| C | 86.37 | 76.89 | 115.35 | 69.20 |
| D | 81.82 | 77.29 | 108.31 | 71.34 |
| E | 97.31 | 90.27 | 143.55 | 68.59 |
| F | 90.88 | 81.31 | 128.44 | 69.88 |
| G | 85.63 | 77.07 | 111.15 | 68.65 |
| Mean | 88.83 | 80.44 | 125.99 | 68.23 |

Table 9: Trade-off between min-cost and min-time in terms of performance ratio

In Table 10, we observe the number of times the drone is used in both min-cost TSP-D solutions (Column "Min-Cost") and min-time TSP-D solutions (Columns "Min-Time 25", "Min-Time 40" and "Min-Time 55" representing the cases where the drone speed is set respectively to 25 km/h, 40 km/h and 55 km/h). The results show that min-cost solutions tend to use the drone to service up to 40% of the customers whereas min-time solutions only use the drone to service up to 22% of the customers. This is because, as analysed above, using drone likely helps to reduce the transportation cost but this is not the case for the delivery completion time. Additionally, increasing drone speed leads to higher frequency of using drones.

<table><tbody><tr><td rowspan="2">Instances</td><td colspan="4">Number of drone uses</td></tr><tr><td>Min-Cost</td><td>Min-Time 25</td><td>Min-Time 40</td><td>Min-Time 55</td></tr><tr><td>B</td><td>20.27</td><td>4.70</td><td>6.96</td><td>8.04</td></tr><tr><td>C</td><td>18.19</td><td>4.43</td><td>9.46</td><td>11.27</td></tr><tr><td>D</td><td>17.89</td><td>3.10</td><td>10.20</td><td>12.47</td></tr><tr><td>E</td><td>39.95</td><td>5.30</td><td>5.77</td><td>5.83</td></tr><tr><td>F</td><td>36.77</td><td>9.57</td><td>15.97</td><td>18.58</td></tr><tr><td>G</td><td>36.44</td><td>8.73</td><td>18.66</td><td>21.90</td></tr></tbody></table>

Table 10: The frequency of using drone in two objective functions

## 8. Conclusion

This paper presents a new variant of the Traveling Salesman Problem with Drone (TSP-D) whose objective is to minimize the total operational costs including the transportation cost and the waiting penalties. We propose a model, a mixed integer linear programming formulation and two heuristic methods—GRASP and TSP-LS—to solve the problem. The MILP formula tion is an extension of the mathematical model propose in [12]; TSP-LS is adapted from an existing heuristic, while GRASP is based on our new split algorithm and local search operators. Numerous experiments conducted on a variety of instances of both objective functions show the performance of our GRASP algorithm. Overall, it outperforms TSP-LS in terms of solution quality in an acceptable running time. The results also demonstrate the important role of the new objective function in the new class of vehicle routing problems with drone. Future researches could aim for proposing more efficient metaheuristics which based on our split procedure. The extension of the proposed methods to solve problems with multiple vehicles and multiple drones could be also an interesting research direction.

## Acknowledgement

This research is funded by Vietnam National Foundation for Science and Technology Development (NAFOSTED) under grant number FWO.102.2013.04.

The authors thank Professor Chase C. Murray for his kind support by sending us the instances and detailed results of the min-time TSP-D problem.

## References

## References

[1] A. E. Rizzoli, R. Montemanni, E. Lucibello, L. M. Gambardella, Ant colony optimization for real-world vehicle routing problems, Swarm Intelligence 1 (2) (2007) 135–151.

[2] M. WOHLSEN, [The next big thing you missed: Amazon’s delivery drones could work—they just need trucks](http://www.wired.com/2014/06/the-next-big-thing-you-missed-delivery-drones-launched-from-trucks-are-the-future-of-shipping/) (oct 2014).

URL [http://www.wired.com/2014/06/the-next-big-thing-you-missed-delivery-drones-launched-from-trucks-are-the-future-of-shipping/](http://www.wired.com/2014/06/the-next-big-thing-you-missed-delivery-drones-launched-from-trucks-are-the-future-of-shipping/)

[3] S. Banker, [Amazon and drones – here is why it will work](http://www.forbes.com/sites/stevebanker/2013/12/19/amazon-drones-here-is-why-it-will-work/) (dec 2013). URL [http://www.forbes.com/sites/stevebanker/2013/12/19/amazon-drones-here-is-why-it-will-work/](http://www.forbes.com/sites/stevebanker/2013/12/19/amazon-drones-here-is-why-it-will-work/)

[4] C. News, [Amazon unveils futuristic plan: Delivery by drone](http://www.cbsnews.com/news/amazon-unveils-futuristic-plan-delivery-by-drone/) (dec 2013). URL [http://www.cbsnews.com/news/amazon-unveils-futuristic-plan-delivery-by-drone/](http://www.cbsnews.com/news/amazon-unveils-futuristic-plan-delivery-by-drone/)

[5] M. Murphy, [This is how google wants its drones to deliver stuff to you](http://qz.com/670670/this-is-how-google-wants-its-drones-to-deliver-stuff-to-you/) (apr 2016). URL [http://qz.com/670670/this-is-how-google-wants-its-drones-to-deliver-stuff-to-you/](http://qz.com/670670/this-is-how-google-wants-its-drones-to-deliver-stuff-to-you/)

[6] M. Grothaus, [This is how google’s project wing drone delivery service could work](http://www.fastcompany.com/3055961/fast-feed/this-is-how-googles-project-wing-drone-delivery-service-could-work) (jan 2016). URL [http://www.fastcompany.com/3055961/fast-feed/this-is-how-googles-project-wing-drone-delivery-service-could-work](http://www.fastcompany.com/3055961/fast-feed/this-is-how-googles-project-wing-drone-delivery-service-could-work)

[7] D. Pogue, [Exclusive: Amazon reveals details about its crazy drone delivery program](https://www.yahoo.com/tech/exclusive-amazon-reveals-details-about-1343951725436982.html) (jan 2016). URL [https://www.yahoo.com/tech/exclusive-amazon-reveals-details-about-1343951725436982.html](https://www.yahoo.com/tech/exclusive-amazon-reveals-details-about-1343951725436982.html)

[8] A. Cuthbertson, [Australia post to launch drone delivery service](http://www.newsweek.com/australia-post-drone-delivery-service-drones-449442) (apr 2016). URL [http://www.newsweek.com/australia-post-drone-delivery-service-drones-449442](http://www.newsweek.com/australia-post-drone-delivery-service-drones-449442)

[9] C. News, [Japanese company launches drone delivery service on the golf course](http://www.ctvnews.ca/sci-tech/japanese-company-launches-drone-delivery-service-on-the-golf-course-1.2875191) (apr 2016). URL [http://www.ctvnews.ca/sci-tech/japanese-company-launches-drone-delivery-service-on-the-golf-course-1.2875191](http://www.ctvnews.ca/sci-tech/japanese-company-launches-drone-delivery-service-on-the-golf-course-1.2875191)

[10] S. French, [Drone delivery is already here and it works](http://www.marketwatch.com/story/drone-delivery-is-already-here-and-it-works-2015-11-30) (dec 2015). URL [http://www.marketwatch.com/story/drone-delivery-is-already-here-and-it-works-2015-11-30](http://www.marketwatch.com/story/drone-delivery-is-already-here-and-it-works-2015-11-30)

[11] A. Toor, [This startup is using drones to deliver medicine in rwanda](http://www.theverge.com/2016/4/5/11367274/zipline-drone-delivery-rwanda-medicine-blood) (apr 2016). URL [http://www.theverge.com/2016/4/5/11367274/zipline-drone-delivery-rwanda-medicine-blood](http://www.theverge.com/2016/4/5/11367274/zipline-drone-delivery-rwanda-medicine-blood)

[12] C. C. Murray, A. G. Chu, The flying sidekick traveling salesman problem: Optimization of drone-assisted parcel delivery, Transportation Research Part C: Emerging Technologies 54 (2015) 86–109.

[13] N. Agatz, P. Bouman, M. Schmidt, Optimization approaches for the traveling salesman problem with drone.

[14] A. Ponza, Optimization of drone-assisted parcel delivery.

[15] X. Wang, S. Poikonen, B. Golden, The vehicle routing problem with drones: several worst-case results, Optimization Letters (2016) 1–19.

[16] L. K. Nozick, M. A. Turnquist, Inventory, transportation, service quality and the location of distribution centers, European Journal of Operational Research 129 (2) (2001) 362–371.

[17] K. R. Dawn Russell, John J. Coyle, E. A. Thomchick, [The real impact of high transportation costs](http://www.supplychainquarterly.com/topics/Logistics/20140311-the-real-impact-of-high-transportation-costs/) (jan 2014). URL [http://www.supplychainquarterly.com/topics/Logistics/20140311-the-real-impact-of-high-transportation-costs/](http://www.supplychainquarterly.com/topics/Logistics/20140311-the-real-impact-of-high-transportation-costs/)

[18] A. Robinson, [Logistics and transportation expenses: Understanding their role in the cost of doing business](http://cerasis.com/2014/02/14/transportation-expenses/) (feb 2014). URL [http://cerasis.com/2014/02/14/transportation-expenses/](http://cerasis.com/2014/02/14/transportation-expenses/)

[19] N. Mathew, S. L. Smith, S. L. Waslander, Planning paths for package delivery in heterogeneous multirobot teams, Automation Science and Engi neering, IEEE Transactions on 12 (4) (2015) 1298–1308.

[20] N. Agatz, P. Bouman, M. Schmidt, Optimization approaches for the traveling salesman problem with drone, Tech. rep. (2015).

[21] G. Gutin, A. P. Punnen, The traveling salesman problem and its variations, Vol. 12, Springer Science & Business Media, 2006.

[22] M. Gendreau, J.-Y. Potvin, Handbook of metaheuristics, Vol. 2, Springer, 2010.

[23] C. Prins, N. Labadi, M. Reghioui, Tour splitting algorithms for vehicle routing problems, International Journal of Production Research 47 (2) (2009) 507–535.

[24] T. Vidal, T. G. Crainic, M. Gendreau, C. Prins, [A hybrid genetic algorithm with adaptive diversity management for a large class of vehicle routing problems with time-windows](http://dx.doi.org/10.1016/j.cor.2012.07.018), Computers & OR 40 (1) (2013) 475–489. [doi:10.1016/j.cor.2012.07.018](http://dx.doi.org/10.1016/j.cor.2012.07.018).

930 URL [http://dx.doi.org/10.1016/j.cor.2012.07.018](http://dx.doi.org/10.1016/j.cor.2012.07.018)

[25] T. Vidal, T. G. Crainic, M. Gendreau, C. Prins, [A unified solution framework for multi-attribute vehicle routing problems](http://dx.doi.org/10.1016/j.ejor.2013.09.045), European Journal of Operational Research 234 (3) (2014) 658–673. [doi:10.1016/j.ejor.2013. 09.045](http://dx.doi.org/10.1016/j.ejor.2013.09.045).

5 URL [http://dx.doi.org/10.1016/j.ejor.2013.09.045](http://dx.doi.org/10.1016/j.ejor.2013.09.045)

[26] D. Cattaruzza, N. Absi, D. Feillet, T. Vidal, A memetic algorithm for the multi trip vehicle routing problem, European Journal of Operational Research 236 (3) (2014) 833–848.

[27] C. Prins, A simple and effective evolutionary algorithm for the vehicle routing problem, Computers & Operations Research 31 (12) (2004) 1985–2002.

[28] C. Prins, A grasp× evolutionary local search hybrid for the vehicle routing problem, in: Bio-inspired algorithms for the vehicle routing problem, Springer, 2009, pp. 35–53.

945 [29] G. A. Kindervater, M. W. Savelsbergh, Vehicle routing: handling edge exchanges, Local search in combinatorial optimization (1997) 337–360.

[30] P. J. Fleming, J. J. Wallace, How not to lie with statistics: the correct way to summarize benchmark results, Communications of the ACM 29 (3) (1986) 218–221.

950 [31] D. Applegate, R. Bixby, V. Chvatal, W. Cook, Concorde tsp solver (2006).