# The vehicle routing problem with drones and drone speed selection

Felix Tamke<sup>a,∗</sup>, Udo Buscher<sup>a</sup>

<sup>a</sup>Faculty of Business and Economics, TU Dresden, Dresden 01062, Germany

## Abstract

Joint parcel delivery by trucks and drones has enjoyed significant attention for some time, as the advantages of one delivery method offset the disadvantages of the other. This paper focuses on the vehicle routing problem with drones and drone speed selection (VRPD-DSS), which considers speed-dependent energy consumption and drone-charging in detail. For this purpose, we formulate a comprehensive mixed-integer problem that aims to minimize the operational costs consisting of fuel consumption costs of the trucks, labor costs for the drivers, and energy costs of the drones. The speed at which a drone performs a flight must be selected from a discrete set. We introduce preprocessing steps to eliminate dominated speeds for a flight to reduce the problem size and use valid inequalities to accelerate the solution process. The consideration of speed-dependent energy consumption leads to the fact that it is advisable to perform different flights at different speeds and not to consistently operate a drone at maximum speed. Instead, drone speed should be selected to balance drone range and speed of delivery. Our extensive computational study of a rural real-world setting shows that, by modeling energy consumption realistically, the savings in operational costs compared to truck-only delivery are significant but smaller than those identified in previously published work. Our analysis further reveals that the greatest savings stem from the fact that overall delivery time decreases compared to truck-only delivery, allowing costly truck-driver time to be reduced. The additional energy costs of the drone, however, are largely negligible.

Keywords: Vehicle routing problem, Drones, Energy consumption

## 1. Introduction

This paper introduces the vehicle routing problem with drones and drone speed selection (VRPD-DSS). The integration of drones into transportation systems for parcel delivery has attracted significant attention in recent years [9, 27, 28, 32, 37]. In contrast to delivery trucks, drones are not restricted to road networks and are, therefore, considered faster. However, they have several drawbacks. Drones have very limited capacities, e. g., in terms of the number of parcels or maximum payload, as well as limited range. Therefore, they are not well-suited as a stand-alone solution for delivery scenarios involving longer distances. One way to offset the disadvantages of drones is to combine trucks and drones into tandems [1, 10, 29, 48]. In these cases, a truck carries one or more drones atop its roof and operates as a kind of mobile warehouse for drones but it also makes deliveries to customers.

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">∗Corresponding author</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">Email addresses: felix.tamke@tu-dresden.de (Felix Tamke), udo.buscher@tu-dresden.de (Udo Buscher)</span></small>

Truck-drone tandems are considered a viable option for last-mile delivery, especially in rural areas [5, 19], where distances between customers are greater because the population density is lower. Thus, trucks have to travel long distances to make deliveries to remote customers, while drones can fly more-direct routes. However, direct drone delivery from a warehouse or store, as tested by various companies for urban and suburban areas, is usually not possible due to the long distances. Hence, the trucks are able to work as range extenders for the drones. Moreover, drones can usually operate in rural areas without interference from tall buildings or other obstacles. This allows for less-stringent regulations concerning their use. Another aspect to consider is a potential customer-delivery zone. Residences in rural areas are mostly stand-alone houses. This allows a drone to drop the package somewhere on the customer’s property, for example with a winch, which simplifies the delivery process.

One of the most important factors of drone use is their limited range. In the literature on truck-drone tandems, the range is often only an approximation based on a maximum distance or a time limit [27, 49]. However, both approaches are simplifications for the maximum energy consumption of a drone. The energy consumed by a drone depends on several factors. Zhang et al. [49] grouped these factors with respect to drone design, environment, drone dynamics, and delivery operations. These authors showed that, in particular, the total weight of the drone at takeoff, which consists of the payload plus drone and battery weight, and the airspeed have a major impact on energy consumption and, thus, on range. For a given drone configuration and just a single customer delivery per flight, the total weight at takeoff is fixed, and only the speed of the flight can be adjusted to vary the range.

However, in most optimization approaches for truck-drone tandems, the range is either independent of the speed, or the speed is the same for all flights. Thus, speed is not included in the decision-making process. In the context of the problem considered here, i.e., trucks and drones make deliveries, to the best of our knowledge, variable drone speeds affecting the range are presented only in [35] for a single truck with multiple drones. They introduced a heuristic approach in which drone speeds can be dynamically adjusted and demonstrated that significant time-savings can be achieved with variable drone speeds.

In contrast to [35], we present for the first time an exact approach for routing truck-drone tandems that takes into account speed-dependent energy consumption and other relevant aspects such as recharging. Here, considering drone speed as a continuous decision variable is not practical because the speed affects the energy expended in a nonlinear manner [49]. Therefore, we perform a discretization of the speed to obtain different discrete levels. The energy consumption for each discrete level can be determined in advance and, thus, a speed has to be selected for a flight. We call this new problem the vehicle routing problem with drones and drone speed selection and make the following additional contributions in this paper:

• We conduct numerical experiments on realistic instances for a rural scenario. The instances incorporate real-world routing between locations and realistic drone parameters. The results show that substantial cost-savings can be achieved by truck-drone tandems in comparison to traditional truck-only delivery for the given rural test instances. However, because of the more-realistic assumptions, the savings are not as high as those shown in other publications.

• We show in our experiments that the greatest savings can be achieved by shortening delivery times, while the power costs of the drones are almost negligible.

• We find that the speed selected in advance has a large impact on the costs of the VRPD when only a single speed is available. In contrast, the VRPD-DSS is independent of this pre-selected speed and achieves at least the minimal costs of all VRPDs but usually provides better solutions.

• We present and prove preprocessing methods to eliminate dominated speeds for drone flights and unnecessary variables to efficiently reduce the problem size without excluding optimal solutions.

The paper is structured as follows. A brief overview of the related literature is provided in Section 2. We then present the assumptions made to define the VRPD-DSS and explain the energy-consumption model used in this paper in detail in Section 3. A mixed-integer linear programming formulation for the VRPD-DSS is introduced in Section 4. Section 5.1 presents the newly developed preprocessing methods. Known and new valid inequalities to strengthen the model formulation are described in Section 5.2. The generation of the rural test instances and the results of our computational studies are reported in Section 6. Finally, we conclude the paper in Section 7.

## 2. Related literature

The literature on optimization problems associated with drones is growing rapidly as shown in recent surveys [9, 27, 28, 32, 37]. Therefore, we focus our brief review of the relevant literature mostly on the drone range concepts used and on problems where trucks and drones can perform deliveries. Macrina et al. [27] distinguished this class of problems from problem classes where only drones are able to make deliveries, either from stationary depots (drone delivery problem) or from mobile ground vehicles (carrier-vehicle problem with drones). We refer to the most recent surveys in Chung et al. [9], Macrina et al. [27], and Moshref-Javadi and Winkenbach [28] for a more detailed review of these problems.

Combined delivery by trucks and drones as tandems was introduced by Murray and Chu [29] as the flying sidekick traveling salesman problem (FSTSP) for a single truck with a single drone. They limited the range of the drone by a maximum time it can be airborne and presented a mixed-integer linear programming (MILP) model as well as a heuristic approach to solve the FSTSP. Agatz et al. [1] presented a variant where drones can perform loops, i.e., start and end a flight at the same node. They called this problem the traveling salesman problem with drones (TSPD) and introduced two heuristics. In contrast to [29], the drone range is limited by a maximum flight distance. In addition, they varied the speed of the drone in the computational experiments and showed that a faster drone leads to significantly reduced costs. However, the range is independent from the speed. Many additional heuristic algorithms, e.g., [6, 12, 22, 23, 34], and exact approaches, e.g., [3, 4, 14, 15, 36, 44], have been designed to solve these two basic problems or closely related variants. Currently, the best-known exact approach for a single tandem with one drone is a branch-and-price algorithm introduced in [36]. Unlike the other approaches, Jeong et al. [23] used an approximation of a simple energy-consumption function that takes into account the loaded weight. In a recent heuristic approach [6], the authors used a more detailed energy-consumption model that considers the parcel weight and a fixed speed.

A natural extension of the basic problems FSTSP and TSPD is to consider multiple drones for one truck, as in [7, 13, 30, 35], for example. Murray and Raj [30] introduced the multiple flying sidekicks traveling salesman problem (mFSTSP) and focused on the scheduling of launch and retrieval operations of multiple drones to deal with the small space on a delivery truck. They present an MILP model to solve small instances and a heuristic algorithm for larger instances. In addition, they investigated different approaches to drone endurance, including an energy-consumption model based on parcel weight and speed. However, the speed is not part of the decision-making process. In their computational experiments, they demonstrated that not using an actual energy-consumption model often leads to under-utilization of resources or infeasible solutions in terms of energy consumption. In a subsequent paper [35], the authors included the drone speed as a decision variable and called the resulting problem the mFSTSP with variable drone speeds. They introduced a heuristic approach to solve the problem and showed that variable drone speeds lead to substantial time-savings.

Another extension of the FSTSP and the TSPD arises from using multiple tandems with one or more drones per truck. This problem is introduced in Wang et al. [46] as the vehicle routing problem with drones (VRPD). As for the problem with one tandem, several heuristic algorithms, e.g. [11, 17, 24, 26, 38, 39, 45], and exact approaches, e.g. [16, 40, 43, 47], have been presented for the VRPD and several related problems. Several approaches consider time windows [16, 17], allow multiple visits to customers on the same flight [26, 47], or enable the launch and retrieval of drones at discrete points on an arc [39]. However, only the approach presented by Liu et al. [26] considers a range that is not limited by a maximum time or distance. Instead, they used an approximation of a drone’s energy consumption that depends on the loaded weight.

Different concepts for a drone’s range are also applied in problems without combined deliveries, e.g., in [8, 33, 18]. Cheng et al. [8] developed an exact algorithm for a drone delivery problem with multiple trips and with non-linear energy consumption based on the payload. Poikonen and Golden [33] studied a problem with one truck and multiple drones and proposed a heuristic algorithm. Drones are allowed to visit multiple customers on the same flight, but the truck cannot visit a node when a drone is in the air. The energy consumption used in their approach takes into account the loaded weight of the parcels. Two different drone speeds are tested in their computational experiments, but the speed has no impact on the expended energy. Dukkanci et al. [18] considered a problem where drones are first transported to launch points by trucks, serve a customer, and then return to the truck to start the next service. The trucks remain at the launch points and perform no deliveries, while the drones serve the customers. The authors determined the energy consumption explicitly and used the speed of the drones as continuous decision variables. To solve this problem, they reformulated the non-linear model into a second-order cone-programming problem.

In summary, to the best of our knowledge, there is currently no approach for the VRPD that takes into account the actual energy consumption of drones and incorporates drone speed into the decision-making process. Additionally, in contrast to battery-switching, recharging the battery while the drone is on the truck has not yet been included. Therefore, we adapt and extend one of the currently best exact approaches for the VRPD, as presented in [43], to address these relevant and important additional features.

## 3. Preliminary considerations

## 3.1. Assumptions on drone operations and truck-drone interaction

To model the VRPD-DSS, we make the following assumptions:

(a) A truck can be equipped with one or more drones. However, each drone is associated with one truck exclusively. Therefore, that drone may not be launched or received by any other truck. This is reasonable since the technological effort required to coordinate multiple drones on one truck is high.

(b) Trucks and drones do not have to use the same distance metric in a network because trucks are bound by the road network whereas drones are not.

(c) Each drone operation comprises three steps. First, it has to be launched from the truck. Next, the drone performs a delivery to exactly one customer, and then, it returns to its associated truck.

(d) A drone must be launched and retrieved at nodes of the given network, i.e., the depot or customer locations. A drone must not start and end a flight at the same customer location. In addition, a truck must not return to an already-visited customer to retrieve a drone. Likewise, trucks and drones may return to the depot only once.

(e) We consider service times at customer locations for truck as well as drone deliveries. We also take into account the time needed to prepare a launch. The time required to retrieve a drone is not considered since we assume that the drones operate autonomously.

(f) A drone can fly at different speeds. The speed for a flight can be selected from a discrete set of available speeds and is constant during the whole flight (steady flight). The speed of the truck is given and is not part of the decision-making process.

(g) A drone expends energy by flying and hovering. Its energy consumption while flying depends on the selected speed and the weight. Hovering occurs in two cases: first, if the drone has to wait at the retrieval location and, second, while it is serving a customer. Other operations like climb and descent are not taken into consideration. We assume that the amount of time not spent hovering or in steady flight is negligible.

(h) The energy that can be expended during flight and hovering is limited by the available energy of the drone battery. However, the battery can be charged at a constant rate when the drone is on top of the truck. It cannot be recharged while the drone is being prepared for a launch.

## 3.2. Energy-consumption model

An energy-consumption model for drone operations is essential in our study. We use the model presented in [41] for two reasons. First, multi-rotor drones are considered, corresponding to the technology currently used in truck-drone tandems. Second, the model provides different power functions for steady flight and hovering. Thus, we are able to distinguish between these two operations and can include the speed of a flight into energy considerations and decision-making. We use the octocopter presented in [41] in all our tests (see Table A.1 for parameters) because octocopters are capable of carrying heavier packages and, thereby, are suitable for truck-drone tandems.

A drone consumes energy when hovering and flying because it has to resist both gravity and drag forces. The latter are caused by the forward motion of the drone and the wind. However, we assume perfect ambient conditions such as no wind. All of a drone’s activities in the air are accomplished by adjusting the speed of each rotor. This leads to the required thrust and pitch to perform an operation, e.g., moving forward at a desired speed. The thrust of the individual rotors differs depending on the type of activity. On average, however, they are almost equal and, together, exactly balance gravity and drag forces. Therefore, the total required thrust T can be described as the sum

$$
T = F^{\mathrm{g}} + F^{\mathrm{d}}\tag{1}
$$

of gravity $F ^ { \mathrm { g } }$ and the total drag forces $F ^ { \mathrm { d } }$

As described in [41], it is convenient to divide the drone into three relevant components: drone body (db), battery (b), and a customer’s package (p). All three components $i \in DP =$ {db, b, p} have the same attributes: mass $m _ { i }$ , drag coefficient $c _ { i } ^ { \mathrm { d } }$ , and projected area $A _ { i }$ perpendicular to the direction of travel. Hence, gravity $F ^ { \mathrm { g } }$ is equal to

$$
F^{\mathrm{g}} = g\sum_{i\in DP}m_{i},\tag{2}
$$

where $g$ is the standard acceleration due to gravity. The total drag force $F ^ { \mathrm { d } }$ for steady flight with speed v can be estimated with the equation

$$
F ^ {\mathrm{d}} = \frac {1}{2} \rho v ^ {2} \sum_ {i \in D P} c _ {i} ^ {\mathrm{d}} A _ {i},\tag{3}
$$

where $\rho$ is the density of air.

For a drone with n rotors of diameter $D .$ , we are now able to calculate the theoretical minimum power required to hover as

$$
P ^ {\mathrm{H,min}} = \frac {T ^ {\frac {3}{2}}}{\sqrt {\frac {1}{2} \pi n D ^ {2} \rho}}.   6\tag{4}
$$

Note that for hovering, $v = 0$ and, therefore, $F ^ { \mathrm { d } } = 0$ and $T = F ^ { \mathrm { g } }$ . The theoretical minimum power for steady flight with speed v is given by

$$
P ^ {\mathrm{F,min}} = T \left(v \sin \alpha + v ^ {\mathrm{i}}\right)\tag{5}
$$

with pitch angle α and induced speed $v ^ { \mathrm { i } } ,$ . Pitch angle α is the tilt of the drone in the direction of travel and can be determined by

$$
\alpha = \arctan \left(\frac {F ^ {\mathrm{d}}}{F ^ {\mathrm{g}}}\right).\tag{6}
$$

The induced speed at the rotors $v ^ { \mathrm { i } }$ can be computed by solving the implicit equation

$$
v ^ {\mathrm{i}} - \frac {2 T}{\pi n D ^ {2} \rho \sqrt {(v \cos \alpha) ^ {2} + (v \sin \alpha + v ^ {\mathrm{i}}) ^ {2}}} = 0,\tag{7}
$$

which can easily be done numerically. Finally, we consider an overall power efficiency of the drone $\eta$ and also use a safety coefficient $\sigma .$ The latter is used to reflect circumstances not considered in the energy-consumption function, such as wind and temperature, and to prevent an underestimation of the power consumption. Hence, the expended power during hover $P ^ { \mathrm { H } }$ and forward flight $P ^ { \mathrm { F } }$ is expressed as

$$
P ^ {\mathrm{H}} = \frac {P ^ {\mathrm{H,min}}}{\eta} (1 + \sigma) \text {and} P ^ {\mathrm{F}} = \frac {P ^ {\mathrm{F,min}}}{\eta} (1 + \sigma).\tag{8}
$$

In our studies, we vary two parameters that are relevant for computing the energy consumption of a given drone configuration: speed $v$ and the mass of the package for a customer $m _ { \mathrm { p } }$ . Hence, we introduce the expended power for hovering and steady forward flight as functions $P ^ { \mathrm { H } } ( m _ { \mathrm { p } } )$ and $P ^ { \mathrm { F } } ( m _ { \mathrm { p } } , v )$ . Note that the drag coefficient $c _ { \mathrm { p } } ^ { d }$ and the projected area $A _ { \mathrm { p } } ^ { d }$ also change with different packages due to their different shapes. However, these effects are negligible compared to those of other two factors.

In the following, we analyze the trade-off between drone speed and energy consumed for the given model. Consider the examples shown in Figure 1 to better understand the relationship between package mass, speed, and corresponding expended power (1a) and energy consumption (1b, 1c) for the introduced model. We distinguish between two different energy-consumption scenarios. First, we take into account only the energy consumption for flying 1000 m (1b). Secondly, we assume that the drone flies 1000 m and then has to hover and wait for the truck, which arrives 180 s after the drone takes off (1c). This is a relevant scenario for truck-drone tandems and is required for synchronization. Since all flights are faster than 180 s, the drone must hover regardless of the speed. However, hovering time increases with increasing drone speed.

The expended power increases monotonously with the drone speed and is higher for larger package masses. In contrast, the energy consumption for steady flight initially decreases and then increases again with increasing speed; this is due to the trade-off between expended

![](images/page_7_chart_0.jpg)

(a) Expended power

![](images/page_7_chart_2.jpg)

(b) Energy consumption only flight

![](images/page_7_chart_4.jpg)

(c) Energy consumption flight and hover

Figure 1: Expended power, energy consumption to fly 1000 m, and energy consumption to fly 1000 m plus hovering up to 180 s are reached for different speeds and package masses $m _ { \mathrm { p } }$

power and flight duration. At low speeds, less power is expended, but the flight duration is longer. In the reverse case, exactly the opposite is true; higher speeds expend more power, but the flight is faster. As a result, the range of the drone depends significantly on the selected speed, and faster drone speeds are not automatically better. Additionally, if waiting for the truck and hovering were not necessary in general, we could determine an optimal speed for a given package mass $m _ { \mathrm { p } }$ and exclude all slower speeds. Speeds slower than the optimum speed cause higher energy consumption plus longer flight duration. However, hovering might be necessary for truck-drone tandems. If we include energy consumption for hovering, slower speeds usually have a smaller total energy consumption, as shown in Figure 1c.

Hence, faster drones may lead to faster deliveries but have a smaller range and higher energy consumption. The latter is especially important if the battery has to be recharged on the truck before the next flight and is not swapped. Therefore, it is essential to include the speed of the drones in the route-planning process of truck-drone tandems when their energy consumption is considered.

## 4. Mixed-integer linear programming formulation for the VRPD-DSS

## 4.1. Notation

## 4.1.1. Sets and parameters

We distinguish five different but partly overlapping sets of nodes. First, we denote the set of all customers by $C = \{ 1 , \ldots , c \}$ . Not all customers can be served by a drone due, for example, to weight restrictions or customer preferences. Therefore, we introduce subset ${ \bar { C } } \subseteq C$ as the set of all customers that can be served by a drone. Furthermore, we introduce nodes 0 and $c   +   1$ as start depot and end depot for the same physical location. We then define $N = \{ 0 \} \cup C \cup \{ c + 1 \}$ as the set of all nodes, $N _ { 0 } = N \backslash \{ c + 1 \}$ as the set of all departure nodes, and $N _ { + } = N \backslash \{ 0 \}$ as the set of all arrival nodes.

A homogeneous fleet of truck-drone tandems F is available to supply all customers. Each tandem $f \in F$ consists of a single truck f and a set of drones D. The distance from node $i \in N$ to node $j \in N$ for a truck is denoted by $\delta _ { i j } ^ { \mathrm { T } }$ and the corresponding travel time by $\tau _ { i j } ^ { \mathrm { T } }$ The distance between two nodes i and $j$ for the drone is represented by $\delta _ { i j } ^ { \mathrm { D } }$ . In contrast to a truck, a drone can travel at different speeds $v \in V .$ , where V is the set of possible speeds. We introduce $\tau _ { i j } ^ { \mathrm { D } , v } = \delta _ { i j } ^ { \mathrm { D } } / v$ as the travel time of a drone from node i to node $j$ at speed v. In addition to travel times, we consider service times $\tau _ { j } ^ { \mathrm { S , T } }$ and $\tau _ { j } ^ { \mathrm { S , D } }$ for truck and drone deliveries for each node $j \in N$ . The amount of time needed to prepare a launch is represented by $\tau ^ { \mathrm { L } }$ We also introduce the maximum amount of time a drone is allowed to hover before retrieval as $\tau ^ { \mathrm { M H } }$ and the maximum time a truck is allowed to remain stationary at a node as $\tau ^ { \mathrm { M S } }$ Both times can be limited to reflect more-realistic scenarios. The maximum duration of a route is denoted by M.

A drone flight is defined as triple $( i , j , k )$ with node $i \in N _ { 0 }$ as the launch node, $j \in \bar { C }$ as the customer node, and $k \in N _ { + }$ as the retrieval node. An operation $( i , j , k ) ^ { v }$ represents the execution of the flight $( i , j , k )$ with speed v. Assuming that both legs of the flight (i to j and $j$ to $k )$ are executed at the same speed v, we can determine the time $\tau _ { i j k } ^ { v }$ of an operation with

$$
\tau_ {i j k} ^ {v} = \tau_ {i j} ^ {\mathrm{D}, v} + \tau_ {j} ^ {\mathrm{S}, \mathrm{D}} + \tau_ {j k} ^ {\mathrm{D}, v}.\tag{9}
$$

The energy consumption of an operation can be computed in a similar manner. During the flight to the customer $j ,$ the drone must carry the package with mass $m _ { j }$ , whereas no package is transported on the way to retrieval node $k .$ We assume that the drone hovers at customer $j ^ { \prime } \mathfrak { g }$ s property to deliver the package and that the mass is constant $( m _ { j } )$ over the delivery time to take additional energy consumption, $\mathbf { e . g . }$ , for using the winch, into account. Therefore, the energy consumption for operation $( i , j , k ) ^ { v }$ corresponds to

$$
e _ {i j k} ^ {v} = \tau_ {i j} ^ {\mathrm{D}, v} \cdot P ^ {\mathrm{F}} (m _ {j}, v) + \tau_ {j} ^ {\mathrm{S}, \mathrm{D}} \cdot P ^ {\mathrm{H}} (m _ {j}) + \tau_ {j k} ^ {\mathrm{D}, v} \cdot P ^ {\mathrm{F}} (0, v).\tag{10}
$$

The battery of a drone has a nominal energy of $E$ . However, in order to increase its service life, a battery should usually not be fully discharged. Hence, we use  as the maximum depth of discharge (DoD) in percent. A DoD of 0% means the battery is fully charged, while at a DoD of 100%, the battery is empty. Therefore, the maximum available energy is $\epsilon E$ Furthermore, it can be recharged with a fixed charging rate of $P ^ { \mathrm { C } }$

$W _ { v }$ is the set of feasible drone operations for speed $v \in V$ . Each drone speed $v$ leads to a different set of feasible operations since the speed has a large impact on the range. The set of all feasible drone operations is $\begin{array} { r } { W = \bigcup _ { v \in V } W ^ { v } } \end{array}$ . An operation $( i , j , k ) ^ { v }$ is feasible only under three conditions: (i) all nodes have to be pairwise different; (ii) customer $j$ can be supplied by a drone, $\stackrel{\leftrightarrow}{ i.e., } j \in \bar{C};$ and (iii) the minimum energy consumption of operation $\left( i , j , k \right) ^ { v }$ does not exceed the maximum available energy $\epsilon E$ of the battery. In addition to the energy consumption $e _ { i j k } ^ { v }$ , we can take into account the minimum hovering time at retrieval node k as the truck could arrive after the drone, although it travels directly from i to $k .$ Thus, operation $( i , j , k ) ^ { v }$ is feasible for $i \in N _ { 0 } , j \in \bar { C } , k \in N _ { + } , i \neq j , i \neq k , j \neq k ,$ , if

$$
e _ {i j k} ^ {v} + \max (\tau_ {i k} ^ {\mathrm{T}} - \tau_ {i j k} ^ {v}, 0) \cdot P ^ {\mathrm{H}} (0) \leq \epsilon E.\tag{11}
$$

Finally, we define the cost parameters: (i) λ as fuel cost per distance unit traveled by a truck, (ii) $\beta$ as cost per time unit of working time of a truck driver, and (iii) $\gamma$ as cost per energy unit expended by the drone.

## 4.1.2. Decision variables

Several decision variables are required to describe the problem as an MILP:

$x _ { i j } ^ { f } = 1$ if truck $f \in F$ drives directly from node $i \in N _ { 0 }$ to node $j \in N _ { + }$ and, otherwise, 0.

$y _ { i j k } ^ { f d v } = 1$ if drone d of tandem $f \in F$ performs operation $( i , j , k ) ^ { v }$ and, otherwise, 0.

$q _ { i } ^ { f } = 1$ if node $i \in N$ is visited by truck $f \in F$ and, otherwise, 0.

• $b _ { i j } ^ { f } = 1$ if nodes $i , j \in C$ with $j > i$ are visited by truck $f \in F$ and, otherwise, 0.

$u _ { i } ^ { f } \in  { \mathbb { N } } _ { 0 }$ specifies the position of customer $i \in C$ on the route of truck $f \in F$

$p _ { i j } ^ { f } = 1$ if node $i \in N _ { 0 }$ precedes nodes $j \in N _ { + }$ in the tour of truck $f \in F$ and, otherwise, 0.

![](images/page_10_chart_0.jpg)

Figure 2: Relation between variables for resources time and energy

$z _ { l i k } ^ { f d } = 1$ if drone $d \in D$ of tandem $f \in F$ performs a flight with launch node $i \in N _ { 0 }$ and retrieval node $k \in N _ { + }$ and truck $f$ visits node $l \in C$ in between and, otherwise, 0.

$a t t _ { i } ^ { f } \in \mathbb { R } _ { + }$ represents the arrival time of truck $f \in F$ at node $i \in N$

$d t t _ { i } ^ { f } \in \mathbb { R } _ { + }$ represents the departure time of truck $f \in F$ from node $i \in N$

$a t d _ { i } ^ { f d } \in \mathbb { R } .$ + represents the arrival time of drone $d \in D$ of tandem $f \in F$ at node $i \in N$

$d t d _ { i } ^ { f d } \in \mathbb { R } _ { + }$ represents the departure time of drone $d \in D$ of tandem $f \in F$ from node $i \in N$

$h t d _ { i } ^ { f d } \in \mathbb { R } _ { + }$ represents the amount of time that drone $d \in D$ of tandem $f \in F$ hovers at node $i \in N$

$l t d _ { i } ^ { f d } \in \mathbb { R } _ { + }$ represents the amount of time that is used for drone d $\in \textit { D }$ of tandem $f \in F$ to be loaded at node $i \in N$

$r _ { i } ^ { f d } \in [ ( 1 - \epsilon ) E , E ]$ represents the residual energy of drone $d \in D$ of tandem $f \in F$ when arriving at node $i \in N$ or at reunion with truck $f$ if i is a retrieval node.

$w _ { i j } ^ { f d } \in [ 0 , 1 ]$ represents the share of travel time $\tau _ { i j } ^ { \mathrm { T } }$ on arc $( i , j )$ that is used by drone $\dot { d \in D }$ of tandem $f \in F$ for recharging.

$t e c ^ { f d } \in \mathbb { R } _ { + }$ represents the total energy consumption of drone d of tandem $f .$

The relationship between time variables of trucks and drones as well as energy-related variables of drones is shown in Figure 2. Note that we omit the indices for truck and drone as we consider only one vehicle of each type in this example. Both vehicles leave node i at the same time $( d t t _ { i } = d t d _ { i } )$ . The drone performs operation $( i , j , k ) ^ { v }$ and arrives at retrieval node k at time $a t d _ { k } = d t d _ { i } + \tau _ { i j k } ^ { v }$ . Its residual energy decreases from $r _ { i }$ to $r _ { i } - e _ { i j k } ^ { v }$ on arrival at node $k .$ The truck arrives at node $k$ at $\it a t t _ { k } = \it d t _ { i } + \tau _ { i k } ^ { \mathrm { T } } > \it a t d _ { k }$ . Thus, the drone must hover for $h t d _ { k } = a t t _ { k } - a t d _ { k }$ time units. The residual energy of the drone at its reunion with the truck at node k is $r _ { k } = r _ { i } - e _ { i j k } ^ { v } - h t d _ { k } P ^ { \mathrm { H } } ( 0 )$ . After the arrival of the truck, customer k is served by the driver. The drone is recharged on the truck for $l t d _ { k } = \tau _ { k } ^ { \mathrm { S , T } }$ time units during the service to customer k. Finally, the truck departs from customer location k at time $d t _ { k } = a t t _ { k } + \tau _ { k } ^ { \mathrm { S } }$ and travels to node l. The drone is recharged during the complete travel time $\tau _ { k l } ^ { \mathrm { T } } ~ ( w _ { k l } = 1 )$ while atop the truck, and its residual energy is $r _ { l } = \tau _ { k l } ^ { \mathrm { T } } P ^ { \mathrm { C } }$ when the tandem reaches node l.

## 4.2. Model

The VRPD-DSS can be formulated as an MILP with the notation and decision variables introduced above. To facilitate understanding, the objective function and the various groups of constraints are presented in several sections.

## 4.2.1. Objective function

The objective function

$$
\min \lambda \sum_ {f \in F} \sum_ {i \in C} \sum_ {j \in N _ {+}} \delta_ {i j} ^ {\mathrm{T}} x _ {i j} ^ {f} + \beta \sum_ {f \in F} a t t _ {c + 1} ^ {f} + \gamma \sum_ {f \in F} \sum_ {d \in D} t e c ^ {f d}\tag{12}
$$

minimizes the total operational costs. The first term of (12) corresponds to the fuelconsumption costs of the total distance traveled by all trucks. The second term represents the total working-time costs of all drivers, and the total energy costs of all drones are determined by the last term.

## 4.2.2. Complete demand satisfaction

Constraints

$$
\sum_ {f \in F} \left(q _ {j} ^ {f} + \sum_ {i \in N _ {0}} \sum_ {k \in N _ {+}} \sum_ {d \in D} \sum_ {v \in V} y _ {i j k} ^ {f d v}\right) = 1 \quad \forall j \in C\tag{13}
$$

guarantee that all packages must be delivered and ensure that each customer is visited only once by truck or drone.

## 4.2.3. Truck routing

We introduce constraints

$$
\left| \sum_ {i \in N _ {0}} x _ {i j} ^ {f} = q _ {j} ^ {f} \quad \forall j \in N _ {+}, f \in F \right|\tag{14}
$$

$$
\sum_ {j \in N _ {+}} x _ {i j} ^ {f} = q _ {i} ^ {f} \quad \forall i \in N _ {0}, f \in F\tag{15}
$$

$$
u _ {i} ^ {f} - u _ {j} ^ {f} + c \cdot x _ {i j} ^ {f} + (c - 2) \cdot x _ {j i} ^ {f} \leq c - 1 \quad \forall i, j \in C, f \in F\tag{16}
$$

$$
c \cdot p _ {i j} ^ {f} - (c - 1) \leq u _ {j} ^ {f} - u _ {i} ^ {f} \quad \forall i, j \in C, f \in F\tag{17}
$$

$$
p _ {0, i} ^ {f} = q _ {i} ^ {f} \quad \forall i \in C, f \in F
$$

$$
p _ {i, c + 1} ^ {f} = q _ {i} ^ {f} \quad \forall i \in C, f \in F\tag{18}
$$

(19)

to ensure feasible truck routes. Constraints (14) and (15) preserve the flow of a vehicle $f .$ Inequalities (16) are lifted Miller–Tucker–Zemlin subtour elimination constraints. However, their primary purpose is not to prevent subtours but to correctly determine variables u. Variables u are used in constraints (17) to set precedence variables $p .$ If $p _ { i j } ^ { f } = 1$ , then node $j$ is visited after node i by truck f and $u _ { j } ^ { f }$ is larger than $u _ { i } ^ { f } + 1$ . Equations (18) and (19) guarantee that the depot precedes (node 0) and succeeds (node $c + 1 )$ customer i on the route of truck f if and only if customer i is visited by truck $f .$

Additionally, we ensure that either $p _ { i j } ^ { f }$ or $p _ { j i } ^ { f }$ equals 1 if and only if both nodes i and $j$ are visited by the truck. Hence, we impose $\tilde{p}_{ij}^{f} + \tilde{p}_{ji}^{f} = q_{i}^{f} \cdot q_{j}^{f} \forall i,j \in C, j > i$ . As the right-hand side of this inequality is nonlinear, we use variables $b _ { i j } ^ { f }$ and the following inequalities to linearize this relationship:

$$
p _ {i j} ^ {f} + p _ {j i} ^ {f} = b _ {i j} ^ {f} \quad \forall i, j \in C, j > i, f \in F\tag{20}
$$

$$
q _ {i} ^ {f} \leq b _ {i j} ^ {f} \quad \forall i, j \in C, j > i, f \in F\tag{21}
$$

$$
q _ {j} ^ {f} \leq b _ {i j} ^ {f} \quad \forall i, j \in C, j > i, f \in F\tag{22}
$$

$$
q _ {i} ^ {f} + q _ {j} ^ {f} \leq 1 + b _ {i j} ^ {f} \quad \forall i, j \in C, j > i, f \in F\tag{23}
$$

## 4.2.4. Coordination of drone actions

A drone can perform various actions. Considering our assumptions, it can

• start or end a flight at a node,

• be airborne while the truck visits a node,

• recharge while the truck is traveling from one node to another,

• recharge at a node, or

• idle on the truck either at a node or on an arc.

However, it can never perform multiple activities at the same time, and its actions must be coordinated with the activities of its truck. Since times when the drone is idle do not need to be modeled separately and recharging at a node is included in the energy-consumption constraints in Section 4.2.6, we need to introduce only constraints

$$
\left| \sum_ {i \in N _ {0}} \sum_ {j \in C} \sum_ {v \in V} y _ {i j k} ^ {f d v} \leq q _ {k} ^ {f} \quad \forall k \in N _ {+}, f \in F, d \in D \right|\tag{24}
$$

$$
w _ {i k} ^ {f d} \leq x _ {i k} ^ {f} \quad \forall i, k \in N, f \in F, d \in D\tag{25}
$$

$$
z _ {l i k} ^ {f d} \geq p _ {i l} ^ {f} + p _ {l k} ^ {f} + \sum_ {j \in C} \sum_ {v \in V} y _ {i j k} ^ {f d v} - 2 \quad \forall l \in C, i \in N _ {0}, k \in N _ {+}, f \in F, d \in D\tag{26}
$$

to model the coordination of the remaining activities. Constraints (24) assure that the retrieval node of a drone flight has to be visited by the truck. Constraints (25) guarantee that a charging activity of drone d on arc $( i , k )$ may occur only if truck f travels from i to k. Constraints (26) determine whether drone d is in the air at node l while the truck is visiting l. Thus, these constraints determine whether a drone is available to start an activity at node l or not. Consider Figure 3 for a better understanding. Truck $f$ visits customer l between nodes i and $k ;$ therefore, $p _ { i l } ^ { f } = 1$ and $p _ { l k } ^ { f } = 1$ . At the same time, drone d starts a flight with any speed v at node $i ,$ visits a customer $j ,$ and is retrieved by the truck at k. Thus, drone d is in the air at node l and constraints (26) enforce $z _ { l i k } ^ { f d } = 1$

![](images/page_13_image_1.jpg)

Figure 3: Visualization of constraints (26) that determine if drone d of tandem $f$ is in air at node l.

Now, multiple actions that take place simultaneously can be prevented with

$$
\sum_ {n \in N _ {+}} w _ {l m} ^ {f d} + \sum_ {v \in V} \sum_ {m \in C} \sum_ {n \in N _ {+}} y _ {l m n} ^ {f d v} \leq q _ {l} ^ {f} - \sum_ {i \in N _ {0}} \sum_ {k \in N _ {+}} z _ {l i k} ^ {f d} \quad \forall l \in C, f \in F, d \in D.\tag{27}
$$

Constraints (27) guarantee that drone d can either be charged on an arc leaving node l or can start an operation from node l. However, these actions are possible only if node l is visited by truck f and drone d is not already in the air at node l.

## 4.2.5. Temporal synchronization between trucks and drones

We introduce constraints

$$
a t t _ {k} ^ {f} \geq d t t _ {i} ^ {f} + \tau_ {i k} ^ {\mathrm{T}} \cdot x _ {i k} ^ {f} - M _ {i} \left(1 - x _ {i k} ^ {f}\right) \quad \forall i \in N _ {0}, k \in N _ {+}, f \in F\tag{28}
$$

$$
a t d _ {k} ^ {f d} \geq d t d _ {i} ^ {f d} + \sum_ {v \in V} \sum_ {j \in C} \tau_ {i j k} ^ {v} y _ {i j k} ^ {f d v} - M _ {i} \left(1 - \sum_ {v \in V} \sum_ {j \in C} y _ {i j k} ^ {f d v}\right)\tag{29}
$$

$$
\forall f \in F, d \in D, i \in N _ {0}, k \in N _ {+}
$$

$$
a t d _ {k} ^ {f d} \leq d t d _ {i} ^ {f d} + \sum_ {v \in V} \sum_ {j \in C} \tau_ {i j k} ^ {v} y _ {i j k} ^ {f d v} + M _ {i} \left(1 - \sum_ {v \in V} \sum_ {j \in C} y _ {i j k} ^ {f d v}\right)\tag{30}
$$

$$
\forall f \in F, d \in D, i \in N _ {0}, k \in N_{+}
$$

$$
h t d _ {i} ^ {f d} \geq a t t _ {i} ^ {f} - a t d _ {i} ^ {f d} \quad \forall i \in C, f \in F, d \in D\tag{31}
$$

$$
h t d _ {i} ^ {f d} \leq q _ {i} ^ {f} \tau_ {i} ^ {\mathrm{MH}} \quad \forall i \in C, f \in F, d \in D\tag{32}
$$

$$
l t d _ {i} ^ {f d} \leq q _ {i} ^ {f} \tau_ {i} ^ {\mathrm{MS}} \quad \forall i \in C, f \in F, d \in D\tag{33}
$$

to synchronize the activities of trucks and their associated drones with respect to time. Constraints (28) bound the arrival time $a t t _ { k } ^ { f }$ of truck f at node k if truck f travels directly from node i to node $j ,$ where $M _ { i } = M - \tilde { \tau _ { i , c + 1 } ^ { \mathrm { T } } }$ is the latest possible departure time from node i. Constraints (29) and (30) set the arrival time $a t d _ { k } ^ { f d }$ of drone d belonging to tandem $f$ at reunification node k if it performs operation $\left( i , j , k \right) ^ { v }$ . Hover time $h t d _ { k } ^ { f d }$ of drone d at node k is defined by constraints (31). In case drone d arrives before its corresponding truck $f$ at node i $\left( a t d _ { i } ^ { f d } < a t t _ { i } ^ { f } \right)$ , it is equal to the difference between the truck arrival time $a t t _ { i } ^ { f }$ and the drone arrival time $a t d _ { i } ^ { f d } ;$ otherwise, it is 0. Inequalities (32) and (33) can be used to limit the maximum time a drone is allowed to hover at node i and the maximum time a drone can be recharged at customer node i. They also ensure that drone d of tandem $f$ can only hover or be recharged at customer i if truck f visits customer i.

Constraints

$$
d t t _ {i} ^ {f} \geq a t t _ {i} ^ {f} + \tau_ {i} ^ {\mathrm{S,T}} \quad \forall i \in N, f \in F\tag{34}
$$

$$
d t t _ {i} ^ {f} \geq d t d _ {i} ^ {f d} \quad \forall i \in N, f \in F, d \in D\tag{35}
$$

$$
d t t _ {i} ^ {f} \leq a t t _ {i} ^ {f} + \tau^ {\mathrm{MS}} \quad \forall i \in C, f \in F\tag{36}
$$

$$
d t d _ {i} ^ {f d} \geq a t d _ {i} ^ {f d} + h t d _ {i} ^ {f d} + l t d _ {i} ^ {f d} + \tau^ {\mathrm{L}} \sum_ {j \in C ^ {\prime}} \sum_ {k \in N _ {+}} \sum_ {v \in V} y _ {i j k} ^ {f d v} \quad \forall i \in N, f \in F, d \in D\tag{37}
$$

set the departure times of trucks and drones. The earliest departure time of truck f from node i is determined by constraints (34) and (35). In addition, constraints (36) limit the maximum time a truck can remain stationary at a node. The departure time of a drone is determined with constraints (37). Drone d must not depart from node i before it has finished hovering and loading and is prepared for launch if it starts an operation at node i. Thus, all truck- and drone-related activities at a node must be completed before the truck can leave that node.

## 4.2.6. Energy consumption of drones

The total energy consumption $t e c ^ { f d }$ of drone d belonging to tandem f is determined by constraints

$$
t e c ^ {f d} = \sum_ {i \in N _ {0}} \sum_ {j \in C} \sum_ {k \in N _ {+}} \sum_ {v \in V} e _ {i j k} ^ {v} y _ {i j k} ^ {f d v} + P ^ {\mathrm{H}} (0) \sum_ {i \in C} h t d _ {i} ^ {f d} \quad \forall f \in F, d \in D\tag{38}
$$

and is equal to the energy expended for all flights plus the energy expended for hovering. The residual energy of a drone is computed by constraints

$$
\begin{array}{c} r _ {k} ^ {f d} \leq r _ {i} ^ {f d} + l t d _ {i} ^ {f d} P ^ {\mathrm{C}} - \sum_ {v \in V} \sum_ {j \in C} e _ {i j k} ^ {v} y _ {i j k} ^ {f d v} - h t d _ {k} ^ {f d} P ^ {\mathrm{H}} (0) + E \left(1 - \sum_ {v \in V} \sum_ {j \in C} y _ {i j k} ^ {f d v}\right) \\ \forall f \in F, d \in D, i \in N _ {0}, k \in N _ {+} \end{array}\tag{39}
$$

$$
r _ {i} ^ {f d} + l t d _ {i} ^ {f d} P ^ {\mathrm{C}} \leq E \quad \forall i \in N _ {0}, f \in F, d \in D
$$

$$
r _ {j} ^ {f d} \leq r _ {i} ^ {f d} + l t d _ {i} ^ {f d} P ^ {\mathrm{C}} + \tau_ {i j} ^ {\mathrm{T}} P ^ {\mathrm{C}} w _ {i j} ^ {f d} + E \left(1 - x _ {i j} ^ {f}\right) \quad \forall i \in N _ {0}, j \in N _ {+}, f \in F, d \in D.\tag{40}
$$

(41)

Constraints (39) restrict the residual energy of drone d when reuniting with truck f at node k if a flight is performed between nodes i and k. The residual energy at reunification is the residual energy at departure from node i minus the expended energy. The residual energy at departure from node i consists of the residual energy at arrival $\mid r _ { i } ^ { f d }$ plus the recharged energy while stationary at node i. The expended energy comprises the energy $e _ { i j k } ^ { v }$ for performing operation $( i , j , k ) ^ { v }$ and the energy needed for hovering at reunification node k. Constraints (40) limit the residual energy at departure to the maximum value E since this is not guaranteed by constraints (39). Finally, constraints (41) represent the reloading of drone d while traveling on truck f from node i to node j. However, this is valid only if truck f uses arc $( i , j )$

## 5. Model strengthening

## 5.1. Preprocessing

## 5.1.1. Elimination of dominated drone operations

Identifying drone speeds that will never be used in an optimal solution for a flight $( i , j , k )$ and eliminating them can substantially reduce the number of possible drone operations. Consequently, the number of variables in our model is also reduced, thereby improving the performance. In general, we have to consider the different resources time and energy consumption. An operation is referred to as dominated by another operation for the same flight if is not beneficial with respect to time or to energy consumption.

General dominance rules.

Proposition 1. For flight $( i , j , k ) \in P$ , operation $( i , j , k ) ^ { v }$ is dominated by operation $( i , j , k ) ^ { s }$ with $s > v$ and $v , s \in V , \; i f$

$$
e _ {i j k} ^ {s} + \left(\tau_ {i j k} ^ {v} - \tau_ {i j k} ^ {s}\right) P ^ {H} (0) \leq e _ {i j k} ^ {v}.\tag{42}
$$

Proof. Operation $( i , j , k ) ^ { s }$ is faster than operation $( i , j , k ) ^ { v }$ because $\tau _ { i j k } ^ { s } \; < \; \tau _ { i j k } ^ { v }$ if $s \; > \; v$ However, since the truck can arrive after the drone, we can state only that operation $( i , j , k ) ^ { s }$ is always at least as good as operation $( i , j , k ) ^ { v }$ with respect to time.

The energy consumption of operation $(i,j,k)^v   is   e_{ijk}^v$ . Since the truck can arrive after the drone, we also have to consider the maximum additional hover time $\left( \tau _ { i j k } ^ { v } - \tau _ { i j k } ^ { s } \right)$ to reach the same point in time with operation $( i , j , k ) ^ { s }$ as with operation $( i , j , k \dot { ) } ^ { v }$ . After that, the energy expended by hovering is the same for both speeds. Therefore, the maximum energy consumption of operation $( i , j , k ) ^ { s }$ to reach the same point in time as operation $( i , j , k ) ^ { v }$ is

$$
e _ {i j k} ^ {s} + \left(\tau_ {i j k} ^ {v} - \tau_ {i j k} ^ {s}\right) P ^ {\mathrm{H}} (0).\tag{43}
$$

Thus, operation $( i , j , k ) ^ { s }$ dominates operation $( i , j , k ) ^ { v }$ , if (42) is true.

However, due to the drone power-usage models for flight and hover mode introduced in Section 3.2, it is unlikely that the dominance rule in Proposition 1 applies. This also highlights the trade-off between energy consumption and execution time. Nevertheless, we are able to construct two special cases to eliminate dominated operations. In the following, we first show how a slower operation can dominate a faster one. Secondly, we demonstrate the reverse case, where faster operations are superior to slower operations.

Elimination of operations with faster speeds.

Proposition 2. For flight $( i , j , k ) \in P ,$ operation $( i , j , k ) ^ { s }$ is dominated by operation $( i , j , k ) ^ { v }$ with $s > v$ and $v , s \in V$ if

$$
\tau_ {i j k} ^ {v} \leq \tau_ {i k} ^ {T} \wedge e _ {i j k} ^ {v} \leq e _ {i j k} ^ {s} + \left(\tau_ {i j k} ^ {v} - \tau_ {i j k} ^ {s}\right) \cdot P ^ {H} (0).\tag{44}
$$

Proof. As stated above, operation $( i , j , k ) ^ { s }$ is always at least as good with respect to time as $( i , j , k ) ^ { v }$ . However, if $\tau _ { i j k } ^ { v } \leq \tau _ { i k } ^ { \mathrm { T } }$ , then there is no benefit in using the faster speed s. Thus, both operations are equal with respect to time. Now, we can eliminate operation $( i , j , k ) ^ { s }$ if the energy consumption is at least as high as the energy consumption of the slower operation $( i , j , k ) ^ { v }$ . Analogous to the general case, the energy consumption of operation $( i , j , k ) ^ { v }$ is $e _ { i j k } ^ { v }$ , and the energy consumption of operation $( i , j , k ) ^ { s }$ to reach the same point in time as operation $( i , j , k ) ^ { v }$ can be determined with (43). Thus, operation $( i , j , k ) ^ { s }$ is dominated by operation $( i , j , k ) ^ { v }$ , if (44) is true. □

Elimination of operations with slower speeds.

Proposition 3. For flight $( i , j , k ) \in P$ , operation $( i , j , k ) ^ { v }$ is dominated by operation $( i , j , k ) ^ { s }$ with $s > v$ and $v , s \in V { \it ~ i f }$

$$
\neg \exists l \in C, l \neq j \text {s.t.} e _ {i j k} ^ {v} + \max \left(\tau_ {i l} ^ {T} + \tau_ {l} ^ {S, T} + \tau_ {l k} ^ {T} - \tau_ {i j k} ^ {v}, 0\right) \cdot P ^ {H} (0) \leq \epsilon E\tag{45}
$$

$$
\wedge \neg \exists l \in C, l \neq j \text {s.t.} e _ {i j k} ^ {s} + \max \left(\tau_ {i l} ^ {T} + \tau_ {l} ^ {S, T} + \tau_ {l k} ^ {T} - \tau_ {i j k} ^ {s}, 0\right) \cdot P ^ {H} (0) \leq \epsilon E\tag{46}
$$

$$
\wedge \tau_ {i j k} ^ {v} > \tau_ {i k} ^ {T} \wedge e _ {i j k} ^ {s} + \max \left(\tau_ {i k} ^ {T} - \tau_ {i j k} ^ {s}, 0\right) \cdot P ^ {H} (0) \leq e _ {i j k} ^ {v}.\tag{47}
$$

Proof. Conditions (45) and (46) ensure that operations $( i , j , k ) ^ { v }$ and $( i , j , k ) ^ { s }$ require a direct trip of the truck from the launch node i to the retrieval node k. Here, a direct trip is necessary if the truck cannot serve a customer $l \in C$ between i and k since this detour via l would increase the hover time of the drone at $k ,$ resulting in energy consumption that is too high. Taking this special case into account, the amount of hover time is known as the truck travels directly from the launch to the retrieval node. Therefore, we are able to determine the expended energy, including hovering, exactly. In addition, we assume that the drone always arrives after the truck if operation $( i , j , k ) ^ { v }$ is performed $\left( \tau _ { i j k } ^ { v } > \tau _ { i k } ^ { \mathrm { T } } \right)$ ; hence, it never needs to hover. This also means that, in contrast to the general rule, if the drone performs operation $( i , j , k ) ^ { s }$ , it can always be retrieved by the truck before reaching the same point in time as operation $( i , j , k ) ^ { v }$ Thus, the maximum additional hover time is max $\left( \tau _ { i k } ^ { \mathrm { T } } - \tau _ { i j k } ^ { s } , 0 \right)$ and operation $( i , j , k ) ^ { s }$ dominates operation $( i , j , k ) ^ { v }$ if conditions $(45) - (47)$ hold true.

## 5.1.2. Elimination of variables z

Different modeling approaches for the VRPD prohibit, in different ways, the launch of a drone when it is already in flight. We introduce variables $z _ { l i k } ^ { f d }$ to check whether drone d of tandem $f$ performs a flight from i to k and is, therefore, not available at node l. This leads to a large number of variables for larger instances. However, we can eliminate several unnecessary variables to reduce the problem size without excluding any optimal solutions.

Proposition 4. Variables $z _ { l i k } ^ { f d }$ for three pairwise different nodes $l \in C , i \in N _ { 0 } , k \in N _ { + }$ can be eliminated for all $f \in F , d \in D$ if there is no drone operation with launch node i and retrieval node k or

$$
\neg \exists (i, j, k) ^ {v} \in W _ {v}, v \in V, l \neq j \text {s.t.} e _ {i j k} ^ {v} + \max \left(\tau_ {i l} ^ {T} + \tau_ {l} ^ {S, T} + \tau_ {l k} ^ {T} - \tau_ {i j k} ^ {v}, 0\right) \cdot P ^ {H} (0) \leq \epsilon E.\tag{48}
$$

Proof. Following the definition of the variables, it is obvious that $z _ { l i k } ^ { f d }$ can be eliminated if there is no drone operation with launch node i and retrieval node k. Condition (48) states that there is no feasible operation with launch node i and retrieval node k if the truck performs a detour via node l, since the energy consumption of the operation plus the additional energy consumption while hovering at node k exceeds the drone’s available energy. Thus, the truck cannot visit node l between i and k if a drone performs any operation with launch node i and retrieval node k and variables $z _ { l i k } ^ { f d }$ can be eliminated. □

## 5.2. Valid inequalities

Most of the valid inequalities used in this paper are similar to the valid inequalities introduced in [43]. Since they are explained in detail there, we refer to that work for a more detailed discussion.

## 5.2.1. Lower bounds on arrival and departure times

The lower bounds on arrival times at nodes and departure times from nodes are modified in comparison to [43] to include the additional aspects considered in this paper. However, the operating principle is similar. The following inequalities set lower bounds on the completion time of a truck $f$ and a drone d belonging to $f ;$

$$
a t t _ {c + 1} ^ {f} \geq \sum_ {i \in N _ {0}} \sum_ {j \in N _ {+}} \left(\tau_ {i j} ^ {\mathrm{T}} + \tau_ {j} ^ {\mathrm{S,T}}\right) x _ {i j} ^ {f} \quad \forall f \in F\tag{49}
$$

$$
atd_{c + 1}^{fd}\geq \sum_{i\in N_{0}}\sum_{j\in C}\sum_{k\in N_{+}}\sum_{v\in V}\left(\tau^{\mathrm{L}} + \tau_{ijk}^{v}\right)y_{ijk}^{fdv} + \sum_{i\in N}\left[htd_{i}^{fd} + ltd_{i}^{fd}\right] + \sum_{i\in N_{0}}\sum_{j\in N_{+}}w_{ij}^{fd}\tau_{ij}^{\mathrm{T}}\tag{50}
$$

$$
\forall f \in F, d \in D
$$

$$
a t t _ {c + 1} ^ {f} \geq d t t _ {i} ^ {f} + \sum_ {k \in N _ {+}} \left[ \left(\tau_ {i k} ^ {\mathrm{T}} + \tau_ {k} ^ {\mathrm{S,T}} + \tau_ {k, c + 1} ^ {\mathrm{T}}\right) x _ {i k} ^ {f} \right] \quad \forall i \in C, f \in F.\tag{51}
$$

The first two consider the total active time of the vehicles. The active time of a truck consists of travel and service times (49). In addition to these, hovering and recharging times at nodes and on arcs must also be taken into consideration for drones (50). In contrast to the first two inequalities, inequalities (51) determine the completion time based on the minimum travel time from a customer i via another node k back to the depot. If truck $f$ travels directly from i to $k .$ then the earliest arrival time at the depot is the departure time at node i, plus the travel time from i to $k ,$ the service time at node $k ,$ and the travel time from node k to the depot.

$$
\left| \begin{array}{l l} a t t _ {k} ^ {f} \geq \sum_ {i \in N _ {0}} \left(\tau_ {0, i} ^ {\mathrm{T}} + \tau_ {i} ^ {\mathrm{S,T}} + \tau_ {i k} ^ {\mathrm{T}}\right) x _ {i k} ^ {f} & \forall k \in C, f \in F \end{array} \right|\tag{52}
$$

$$
d t d _ {k} ^ {f d} \geq \sum_ {i \in N _ {0}} \sum_ {j \in C} \sum_ {v \in V} \left(\tau_ {0, i} ^ {\mathrm{T}} + \tau^ {\mathrm{L}} + \tau_ {i j k} ^ {v}\right) y _ {i j k} ^ {f d v} + h t d _ {k} ^ {f d} + l t d _ {k} ^ {f d} \quad \forall k \in C, f \in F, d \in D.\tag{53}
$$

Inequalities (52) establish lower bounds on the arrival time at a customer k. As in (51), the detour via another node is considered, but now the truck starts at the depot and travels directly to detour node i. Inequalities (53) set lower bounds on the departure time of drone d associated with truck $f$ at node k. Drone d travels atop truck $f$ from the depot to detour node i and performs an operation with retrieval node $k$

## 5.2.2. Problem-specific cuts

In addition to the lower bounds on arrival and departure times, we use the VRPD-specific cuts introduced in [43]:

$$
\sum_ {i \in C} \sum_ {f \in F} q _ {i} ^ {f} \geq \frac {| C | - | D | \cdot | F |}{| D | + 1}\tag{54}
$$

$$
x _ {i k} ^ {f} \leq p _ {i k} ^ {f} \quad \forall i \in N _ {0}, k \in N _ {+}, f \in F\tag{55}
$$

$$
\left| \sum_ {j \in C} \sum_ {v \in V} y _ {i j k} ^ {f d v} \leq p _ {i k} ^ {f} \quad \forall i \in N _ {0}, k \in N _ {+}, f \in F, d \in D \right|\tag{56}
$$

$$
x _ {0 c + 1} ^ {f} + q _ {j} ^ {f} \leq 1 \quad \forall j \in C f \in F.\tag{57}
$$

First, we set a lower bound on the number of customers that can be visited by all trucks with inequality (54). Inequalities (55) state that, if truck f travels directly from node i to node $k ,$ then i has to precede k in the route of $f .$ Inequalities (56) ensure that, if drone d performs any flight with launch node i and retrieval node k, then i must be visited before k by truck $f .$ Inequalities (57) prohibit the artificial trip between the two depot nodes 0 and c + 1 if any customer is visited by the truck.

Furthermore, we use the extended subtour elimination constraints (ESECs)

$$
\left| \begin{array}{l} \sum_ {f \in F} \left[ \sum_ {i \in S} \sum_ {j \in S} x _ {i j} ^ {f} + \sum_ {i \in \bar {S}} \sum_ {j \in S} \sum_ {k \in S} \sum_ {d \in D} \sum_ {v \in V} y _ {i j k} ^ {f d v} \right. \\ \left. + \sum_ {i \in S} \sum_ {j \in S} \sum_ {k \in \bar {S}} \sum_ {d \in D} \sum_ {v \in V} y _ {i j k} ^ {f d v} + \sum_ {i \in S} \sum_ {j \in S} \sum_ {k \in S} \sum_ {d \in D} \sum_ {v \in V} y _ {i j k} ^ {f d v} \right] \leq | S | - 1 \quad \forall S \subseteq C, | C | \geq 2 \end{array} \right|\tag{58}
$$

introduced in [43] as well. Since there is an exponential number of ESECs, we cannot add them at the beginning but, rather, have to detect violated cuts during the optimization. Therefore, we use the separation algorithm presented in [43].

Finally, we introduce the following new cuts, which have been proven to be useful:

$$
\left| \sum_ {j \in C} \sum_ {v \in V} y _ {i j k} ^ {f d v} \leq \sum_ {l \in C} z _ {l i k} ^ {f d} + x _ {i k} ^ {f} \quad \forall i \in N _ {0}, k \in N _ {+}, f \in F, d \in D \right|\tag{59}
$$

$$
r _ {i} ^ {f d} + l t d _ {i} ^ {f d} P ^ {\mathrm{C}} - (1 - \epsilon) E \geq \sum_ {v \in V} \sum_ {j \in \bar {C}} \sum_ {k \in N _ {+}} e _ {i j k} ^ {v} y _ {i j k} ^ {f d v} \quad \forall i \in C, f \in F, d \in D\tag{60}
$$

$$
t e c ^ {f d} = \sum_ {i \in N _ {0}} \sum_ {j \in N _ {+}} w _ {i j} ^ {f d} \tau_ {i j} ^ {\mathrm{T}} P ^ {\mathrm{C}} + \sum_ {i \in C} l t d _ {i} ^ {f d} P ^ {\mathrm{C}} + \left(r _ {0} ^ {f d} - r _ {c + 1} ^ {f d}\right) \quad \forall f \in F, d \in D.\tag{61}
$$

Inequalities (59) state that, if drone d of tandem f performs any operation with launch node i and retrieval node $k ,$ then it has to be in the air at any node l visited by truck f between i and $k ,$ or truck f has to travel directly from i to k. Inequalities (60) set a lower bound on the available energy, consisting of the residual energy on arrival and the recharged energy while stationary, at node i. The available energy must be sufficient for a drone operation starting at node i. Finally, equations (61) represent a second variant to determine the total energy consumption of a drone. Constraints (38) take into account the energy used for flying and hovering. In contrast, equations (61) consider the energy that is used to recharge the battery of a drone. However, the battery need not be fully charged at the end of the tour. Therefore, we have to additionally consider the difference between the residual energy at the beginning and at the end to determine the drone’s total energy consumption.

## 6. Computational studies

The algorithm is implemented in $\mathrm { C } \#$ with .NET Framework 4.6.1 and Gurobi 9.0 is used as the MILP solver. All tests are performed on a Windows Server 2012 R2 with Intel(R) Xeon(R) CPU E5-4627 v2 3.3 GHz processors with 32 cores and 768GB RAM. We use 12 cores to solve each instance, and the memory consumption is very low. As in [43], extended subtour elimination constraints (58) are not added at every node of the branch-and-bound tree. Here, they are added at every 100th node.

## 6.1. Generation of real-world rural-area test instances

We generate test instances that represent a real-world, rural-area based scenario for the use of truck-drone tandems to test our approach and gain managerial insights. All instances are created with Python 3.7 and are available at [42].

Depot and customer locations. The basis of all test instances is an rectangular-shaped area approximately 20 km by 30 km located in Minnehaha County, South Dakota, USA. We have selected approximately 700 possible customer locations and a UPS Customer Center in Sioux Falls as the depot. The map in Figure 4 shows the distribution of the selected customer locations (dots) and the depot (triangle). To create a single instance, we randomly select |C| customers out of all customer locations.

![](images/page_20_image_0.jpg)

Figure 4: Distribution of all possible customers (dots) and the depot (triangle in the lower right corner)

Specifications of drone model and battery. As in the examples in Section 3.2, we use the octocopter model presented in [41]. We assume an overall power efficiency of the drone $\eta = 0 . 7$ and a safety coefficient $\sigma = 0 . 2$ . Similar to [38], we assume that all drones can transport packages weighing up to 5 kg. In addition, we use an existing lithium polymer (LiPo) battery from Grepow Inc. to power the drone [21]. Since large drones have higher energy consumption, they also require large batteries. The LiPo battery selected for our experiments weighs six kilograms and consists of 12 cells with a total nominal voltage of 44.4 V and a nominal capacity of 22 000 mA h. Thus, it has a nominal energy of $E = 9 7 6 . 8   \mathrm { W   h } { = }$ 3516.48 kJ. In addition, we set the maximum DoD $\epsilon = 0 . 8 0$ . Finally, we assume a charge rate of 1 C, which means that the battery can be completely charged in one hour and $P ^ { \mathrm { C } } =$ 3516.48 kJ/h.

Selection of drone customers. A customer $j \in C$ can only be supplied by a drone if the mass of the package $m _ { j }$ is lass than the payload of the drone. We assume that 90% of all packages are below the drone’s payload and range from 0.05 kg to 5 kg. The other 10% range from 5 kg to 50 kg. Hence, with probability $p \in [ 0 , 1 )$ , we draw $m _ { j }$ from interval [0.05, 5] if $p \leq 0 . 9$ and from interval (5, 50) otherwise. However, a package may not be eligible for drone delivery even though its weight is below the payload. This can occur, for example, if a customer is not willing to be supplied by a drone, which may well be the case when a new technology is introduced. In our computational studies, we assume that 75% of all customers allow drone delivery of their packages.

Distances, travel times, and time parameters. We use openrouteservice.org [31] to obtain actual road network distances and travel times between all locations. The beeline distances for drone flights are determined with GeoPy [20]. Both are free-to-use Python packages. The maximum route duration $M$ is eight hours. For each customer $j \in C ,$ we set the service time of a truck delivery $\tau _ { j } ^ { \mathrm { S , T } }$ at 120 seconds and the service time of drone delivery $\tau _ { j } ^ { \mathrm { S , D } }$ at 90 seconds. For depot nodes 0 and $c   + 1$ the times are fixed at zero. The time needed to prepare the launch of a drone $\tau ^ { \mathrm { L } }$ is 60 seconds. Unless otherwise noted, the maximum time a truck is allowed to remain stationary at a node $\tau ^ { \mathrm { M S } }$ and the maximum time a drone is allowed to hover at retrieval $\tau _ { j } ^ { \mathrm { M H } }$ i1 are set high enough that they are not constraining.

<table><tr><td rowspan="2">Instance</td><td rowspan="2"> $|C|$ </td><td colspan="5"> $|W|$  for  $|V| = 1$ </td><td colspan="3"> $|W|$  for  $|V| = 5$ </td></tr><tr><td>8</td><td>10</td><td>12</td><td>14</td><td>16</td><td>No OE</td><td>OE</td><td> $\Delta W [\%]$ </td></tr><tr><td>SF_20_1</td><td>13</td><td>51</td><td>80</td><td>86</td><td>59</td><td>29</td><td>305</td><td>224</td><td>-26.56</td></tr><tr><td>SF_20_2</td><td>15</td><td>52</td><td>81</td><td>81</td><td>65</td><td>37</td><td>316</td><td>223</td><td>-29.43</td></tr><tr><td>SF_20_3</td><td>11</td><td>299</td><td>397</td><td>384</td><td>298</td><td>198</td><td>1576</td><td>1249</td><td>-20.75</td></tr><tr><td>SF_20_4</td><td>15</td><td>78</td><td>122</td><td>129</td><td>99</td><td>69</td><td>497</td><td>409</td><td>-17.71</td></tr><tr><td>SF_20_5</td><td>15</td><td>176</td><td>248</td><td>254</td><td>207</td><td>147</td><td>1032</td><td>909</td><td>-11.92</td></tr><tr><td>SF_20_6</td><td>12</td><td>84</td><td>134</td><td>135</td><td>96</td><td>54</td><td>503</td><td>355</td><td>-29.42</td></tr><tr><td>SF_20_7</td><td>14</td><td>101</td><td>173</td><td>170</td><td>110</td><td>61</td><td>615</td><td>489</td><td>-20.49</td></tr><tr><td>SF_20_8</td><td>12</td><td>81</td><td>131</td><td>123</td><td>91</td><td>46</td><td>472</td><td>332</td><td>-29.66</td></tr><tr><td>SF_20_9</td><td>13</td><td>83</td><td>131</td><td>125</td><td>94</td><td>70</td><td>503</td><td>376</td><td>-25.25</td></tr><tr><td>SF_20_10</td><td>14</td><td>129</td><td>208</td><td>195</td><td>133</td><td>74</td><td>739</td><td>593</td><td>-19.76</td></tr><tr><td>Avg.</td><td>13.30</td><td>113.40</td><td>170.50</td><td>168.20</td><td>125.20</td><td>78.50</td><td>655.80</td><td>515.90</td><td>-23.10</td></tr></table>

Table 1: Characteristics of instances with 20 customers

Costs. We consider fuel costs of the trucks, wages of the truck drivers, and energy costs of the drones as described in the objective function (12). These costs differ between different truck-types, regions, and companies and vary over time. The costs per distance unit traveled by truck λ in our experiments are based on a typical $\mathrm { P 7 0 }$ UPS truck. We assume a fuel consumption of 11 mpg (0.214 l/km) for rural areas [25] and a diesel price of $\S 0 . 7 6 / 1$ . Thus, distance cost parameter λ is approximately \$0.16/km. Furthermore, we assume that a driver costs approximately $\beta = \S 2 0 / \mathrm { h }$ and the electricity rate $\gamma =   \mathrm { \textperthousand \textperthousand \textperthousand \textperthousand \textperthousand \textperthousand \textperthousand \textperthousand \textpertharpoons \textpertharpoons \textpertharpoons \textpertharpoons \textpertharpoons \textpertharpoons \textpertharpoons \textpertharpoons \textpertharpoons \textpertharpoons \textpertharpoons \textpertharpoons \textpertharpoons \textpertharpoons \textpertharpoons \textpertharpoons \textpertharpoons \textpertharpoons \textpertharpoons \textpertharpoons \textpertharpoons \textpertharpoons \textpertharpoons \textpertharpoons \textpertharpoons \textpertharpoons \textpertharpoons \textpertharpoons \textpertharpoons \textpertharpoons \textpertharpoons \textpertharpoons \textpertharpoons \textpertharpoons \textpertharpoons \textpertharpoons \textpertharpoons \textpertharpoons \textpertharpoons \textpertharpoons \textpertharpoons \textpertharpoons \textpertharpoons \textpertharpoons \textpertharpoons \textpertharpoons \textpertharpoons \textpertharpoons \textpertharpoons \textpertharpoons \textpertharpoons \textpertharpoons \textpertharpoons \textper  \textper  \textper  \textper  \textper  \textper  \textper  \textper  \textper  \textper  \textper  \textper  \textper  \textper  \textper  \textper  \textper  \textper  \textper  \textper  \textper  \textper  \textper  \textper  \textper  \textper  \textper  \textper  \textper  \textper  \textper  \textper  \textper  \textper  \textper  \textper  \textper  \textper  \textper  \textper  \textper  \textper  \textper  \textper  \textper  \textper  \textper  \textper  \textper  \textper  \textper  \textper  \textper  \textper  \textper  \textper  \textper  \textper  \textper  \text�  \text�  \text�  \text�  \text�  \text�  \text�  \text�  \text�  \text�  \text�  \text�  \text�  \text�  \text�  \text�  \text�  \text�  \text�  \text�  \text�  \text�  \text�  \text�  \text�  \text�  \text�  \text�  \text�  \text�  \text�  \text�  \text�  \text�  \text�  \text�  \text�  \text�  \text�  \text�  \text�  \text�  \text�  \text�  \text�  \text�  \text�  \text�  \text�  \text�  \text�  \text�  \text�  \text�  \text�  \text�  \text�  \text�  \text�  \text�  \text�  \text�  \text�  \text�  \text�  \text�  \text�  \text�  \text�  \text�  \text�  \text�  \text�  \text�  \text�  \text�  \text�  \text�  \text�  \text�  \text�  \text�  \text�  \text�  \text�  \text�  \text�  \text�  \text�  \text�  \text�  \text�  \text�  \text�  \text�  \text�  \text�  \text�  \text�  \text�  \text�  \text�  \text�  \text�  \text�  \text�  \text�  \text�  \text�  \text�  \text�  \text�  \text�  \text�  \text�  \text�  \text�  \text�  \text�  \text�  \text�  \text�  \text�  \text�  \text�  \text�  \text�  \text�  \text�  \text�  \text�  \text�  \text�  \text�  \text�  \text�  \text�  \text�  \text�  \text�  \text�  \text�  \text�  \text�  \text�  \text�  \text�  \text�  \text�  \text�  \text�  \text�  \text�  \text�  \text�  \text�  \text�  \text�  \text�  \text�  \text�  \text�  \text�  \text�  \text�  \text�  \text�  \text�  \text�  \text�  \text�  \text�  \text�  \text�  \text�  \text�  \text�  \text�  \text�  \text�  \text�  \text�  \text�  \text�  \text�  \text�  \text�  \text�  \text�  \text�  \text�  \text�  \text�  \text�  \text�  \text�  \text�  \text�  \text�  \text�  \text�  \text�  \text�  \text�  \text�  \text�  \text�  \text�  \text�  \text�  \text�  \text�  \text�  \text�  \text�  \text$ (\$0.025/kJ).

## 6.2. Results for small instances

We use 10 small instances with 20 customers to assess the following:

1) the impact of our preprocessing methods on the runtime,

2) the influence of varying drone speeds on the costs in the VRPD, and

3) the benefits of speed selection in comparison to a single fixed speed.

We have chosen five possible drone speeds ranging from $8   \mathrm { m } / \mathrm { s }$ to 16 m/s in steps of $2   \mathrm { m } / \mathrm { s } .$ Therefore, we have five VRPDs with $| V | = 1$ and one VRPD-DSS with $V = \{ 8 , 1 0 , 1 2 , 1 4 , 1 6 \}$ Table 1 shows the characteristics of each of the 20 customer instances. It includes the number of customers that are available for drone deliveries $| \bar { C } |$ and the number of operations $| W |$ for each VRPD with $| V | = 1$ and for the VRPD-DSS with $| V | = 5$ . For the VRPD-DSS, we also show the number of operations without the elimination of dominated drone operations (No

OE), with operation elimination (OE), and the percentage of dominated operations that can be eliminated (∆W).

## 6.2.1. Performance improvements through preprocessing

The average results of all 10 instances for each set of speeds are presented in Table 2. We solve each instance with two algorithm configurations. First, we apply only the model plus the cuts introduced in Section 5.2 (Model + Cuts). The second configuration includes our preprocessing methods (PP + Model + Cuts). We perform five runs per instance to deal with the performance variability in the MILP solution process. The number of nonzero matrix elements (#NZ) following presolve performed by Gurobi is used to represent the size of a problem. In addition, we use the run-time to optimality in seconds (Time) as the performance indicator and show the optimal costs (Costs). Finally, the relative change ∆ between the two configurations for #NZ and Time is displayed as a percentage.

<table><tr><td rowspan="2">|D|</td><td rowspan="2">V</td><td colspan="3">Model + Cuts</td><td colspan="3">PP + Model + Cuts</td><td colspan="2">Δ[%]</td></tr><tr><td>#NZ</td><td>Time [s]</td><td>Costs [$]</td><td>#NZ</td><td>Time [s]</td><td>Costs [$]</td><td>#NZ</td><td>Time</td></tr><tr><td rowspan="5">1</td><td>8</td><td>45731.68</td><td>536.79</td><td>107.11</td><td>24979.10</td><td>174.12</td><td>107.11</td><td>-45.38</td><td>-67.56</td></tr><tr><td>10</td><td>47185.30</td><td>589.10</td><td>104.09</td><td>26646.70</td><td>144.95</td><td>104.09</td><td>-43.53</td><td>-75.39</td></tr><tr><td>12</td><td>49132.62</td><td>589.61</td><td>102.39</td><td>26061.90</td><td>169.71</td><td>102.39</td><td>-46.96</td><td>-71.22</td></tr><tr><td>14</td><td>43792.16</td><td>156.12</td><td>103.33</td><td>24289.40</td><td>39.43</td><td>103.33</td><td>-44.53</td><td>-74.74</td></tr><tr><td>16</td><td>35659.88</td><td>44.24</td><td>104.44</td><td>22263.70</td><td>11.69</td><td>104.44</td><td>-37.57</td><td>-73.57</td></tr><tr><td></td><td>8,10,12,14,16</td><td>65508.24</td><td>589.35</td><td>101.80</td><td>32409.70</td><td>211.42</td><td>101.80</td><td>-50.53</td><td>-64.13</td></tr><tr><td rowspan="5">2</td><td>8</td><td>65352.20</td><td>315.40</td><td>104.10</td><td>34540.30</td><td>81.62</td><td>104.10</td><td>-47.15</td><td>-74.12</td></tr><tr><td>10</td><td>89139.50</td><td>595.93</td><td>99.96</td><td>37114.60</td><td>145.78</td><td>99.96</td><td>-58.36</td><td>-75.54</td></tr><tr><td>12</td><td>86646.60</td><td>276.35</td><td>97.70</td><td>36017.00</td><td>56.02</td><td>97.70</td><td>-58.43</td><td>-79.73</td></tr><tr><td>14</td><td>71697.10</td><td>91.34</td><td>99.07</td><td>32967.90</td><td>22.92</td><td>99.07</td><td>-54.02</td><td>-74.91</td></tr><tr><td>16</td><td>51544.70</td><td>28.33</td><td>100.74</td><td>29663.60</td><td>7.76</td><td>100.74</td><td>-42.45</td><td>-72.61</td></tr><tr><td></td><td>8,10,12,14,16</td><td>131450.60</td><td>698.27</td><td>96.97</td><td>48416.50</td><td>332.00</td><td>96.97</td><td>-63.17</td><td>-52.45</td></tr></table>

Table 2: Average results for different drone speeds for instances with 20 customers

The results show that the number of nonzero elements in the constraint matrix can be reduced significantly by the preprocessing steps. However, optimal solutions are not excluded since costs are the same with and without preprocessing for all instances. The problem size reduction is larger for the VRPD-DSS than for a single-speed VRPD. In the VRPD, only unnecessary variables z can be eliminated, while in the case of the VRPD-DSS, dominated drone operations are also removed. On average, 23.10 % of the drone operations are removed by applying our dominance rules, as shown in Table 1. Table 2 also highlights that a reduced problem size leads to significantly faster run times. However, in contrast to the problem size reductions, the run-time reductions are smaller for the VRPD-DSS than for the single VRPDs. These results demonstrate that our preprocessing methods introduced in Section 5.1 are highly effective for the considered test instances and therefore, will be used in all further tests.

## 6.2.2. Impact of different drone speeds for the VRPD

Table 1 clearly shows that the number of feasible drone operations is heavily dependent on the selected speed. The number of operations first increases with drone speed and, then, it decreases again. Thus, flying faster than a certain threshold reduces the range of a drone due to the nonlinear energy-consumption function (see Figure 1b). For the chosen drone model, using a speed of $1 0   \mathrm { m / s }$ leads to the largest number of operations on average. However, in some instances, a speed of $1 2   \mathrm { m / s }$ generates the most feasible operations.

Nevertheless, the results in Table 2 demonstrate that more feasible operations do not necessarily lead to lower costs. On average across all 10 instances, the lowest costs considering a single-speed problem can be obtained for both one and two drones with a drone speed of $1 2   \mathrm { m / s }$ . A faster drone is, therefore, not necessarily advantageous and can result in higher costs. This supports the findings in [35]. Although using a speed of $1 2   \mathrm { m / s }$ leads to the lowest costs on average, this does not apply to each individual instance. Figure 5 shows the costs for each speed for all 20 customer instances separated by the number of available drones. In some instances, there is almost no difference between two or more speeds $\scriptstyle { \left( \mathrm { e . g . } \right. }$ $\mathtt { S F _ { - } } 2 0 \mathtt { _ { - } } 5 \mathtt { ) }$ , whereas in other instances, the difference between best and second-best speed is fairly high $\left(  e.g.,   \mathtt{SF}_{-}20_{-}6 \right)$ . Moreover, the speed that results in the lowest costs for an instance can depend on the number of drones available. For example, with instance $\mathtt { S F \_ 2 0 \_ 4 }$ $1 6   \mathrm { m / s }$ leads to minimal cost with one drone, while with two drones, $1 2   \mathrm { m / s }$ is the best choice. In general, it can be summarily stated that the speed selected in advance for the VRPD can have a significant impact on the costs. To address this issue, drone speed should be included in the decision-making process, such as in the VRPD-DSS. In addition, although performing all flights at speed of $1 6   \mathrm { m / s }$ leads to substantially fewer operations than a speed of $8   \mathrm { m } / \mathrm { s } ,$ the average costs are lower. This further illustrates the trade-off between the ability to serve more customers with drones by flying slower, and the savings that can be achieved through shorter delivery times by flying faster.

## 6.2.3. VRPD vs. VRPD-DSS

The optimal solution of the VRPD-DSS is always at least as good as the best solution of all VRPDs with a single speed. In addition, the costs of the VRPD-DSS are often lower because using different speeds is beneficial in terms of energy consumption or delivery time. However, the cost deviations between the VRPD and VRPD-DSS vary. Table 3 shows the minimum, average, and maximum percentage costs deviation (∆Costs) of all 10 instances for each VRPD compared to the VRPD-DSS. In addition, the total number of operations $\left( \#  OP  \right)$ at each speed used in all 10 optimal solutions of the VRPD-DSS is given.

Of course, the average costs of the VRPD with speed $1 2   \mathrm { m / s }$ deviate the least from the optimal solution of the VRPD-DSS since it has the lowest costs, on average, of all VRPDs. They are, on average, 0.59 % (one drone) and 0.78 % (two drones) worse than the optimal costs of the VRPD-DSS. For two instances in the case of a single drone and for one instance when two drones are available, the costs are the same, i.e., all flights are performed at $1 2   \mathrm { m / s }$ although other speeds are available. In contrast, the deviation is over 1 % in some instances. All other speeds lead to higher cost deviations on average and in the best and worst cases.

As a result, most flights in the speed selection problem are performed at a speed of $1 2   \mathrm { m / s }$ for both one and two drones. The slowest speed, $8   \mathrm { m } / \mathrm { s } ,$ is never used in any solution, and the fastest speed, $1 6   \mathrm { m } / \mathrm { s } ,$ is never selected if the tandem has only one drone. We also observe that the deviations between the VRPDs and the VRPD-DSS are larger with two drones. Thus, it is especially important to consider different drone speeds when multiple drones are available.

![](images/page_24_chart_0.jpg)

Figure 5: Costs for each 20 customer instance and varying speeds

## 6.3. Results for larger instances

In our further studies, we use larger instances with 30, 40, and 50 customers to gain insights into the benefits of truck-drone tandems under the realistic circumstances presented in this paper. In contrast to the small instances, we limit the maximum time a truck can stop at a node to $\tau ^ { \mathrm { M S } }$ four minutes, which is twice the service time for a customer visited by a truck. Moreover, the maximum hover time at a retrieval node $\tau ^ { \mathrm { M H } }$ is restricted to two minutes. Preliminary tests on 20 customer instances have shown that these values improve computational performance compared to the unrestricted case but increase costs only slightly.

<table><tr><td rowspan="3">V</td><td colspan="4"> $|D| = 1$ </td><td colspan="4"> $|D| = 2$ </td></tr><tr><td colspan="3"> $\Delta \text{Costs} [\%]$ </td><td rowspan="2">#OP</td><td colspan="3"> $\Delta \text{Costs} [\%]$ </td><td rowspan="2">#OP</td></tr><tr><td>Min</td><td>Avg</td><td>Max</td><td>Min</td><td>Avg</td><td>Max</td></tr><tr><td>8</td><td>2.46</td><td>5.20</td><td>10.60</td><td>0</td><td>3.45</td><td>7.34</td><td>11.71</td><td>0</td></tr><tr><td>10</td><td>0.35</td><td>2.23</td><td>8.01</td><td>6</td><td>1.32</td><td>3.07</td><td>8.37</td><td>10</td></tr><tr><td>12</td><td>0.01</td><td>0.59</td><td>1.78</td><td>22</td><td>0.00</td><td>0.78</td><td>1.89</td><td>29</td></tr><tr><td>14</td><td>0.04</td><td>1.46</td><td>7.45</td><td>8</td><td>0.01</td><td>2.08</td><td>8.57</td><td>8</td></tr><tr><td>16</td><td>0.34</td><td>2.54</td><td>8.68</td><td>0</td><td>0.04</td><td>3.79</td><td>9.00</td><td>7</td></tr></table>

Table 3: Comparison of solutions with a single speed and solutions with speed selection for 20 customers

## 6.3.1. The MILP solver as a heuristic

We focus on using the MILP solver as a heuristic rather than as an exact approach in the tests with larger instances. Today, state-of-the-art solvers contain powerful primal heuristics to find good feasible solutions quickly [2]. To test Gurobi’s ability to provide good solutions quickly, we conduct two different experiments.

In the first experiment (Experiment 1), we set the Gurobi parameter MIPFocus to 1 and Heuristics to 0.75. The former modifies the high-level solution strategy to focus on finding good feasible solutions, while the latter lets Gurobi spend even more time on primal heuristics. Using this setting, we perform five runs with different seed values for each instance and limit the maximum time per run to one hour. In the second experiment (Experiment 2), we attempt to achieve a good lower bound. For this purpose, we use the default values of MIPFocus and Heuristics and provide the best found solution in the first experiment as the starting solution. In addition, we increase the maximum run time to eight hours but perform only a single run per instance. Detailed results for both experiments are shown in Table A.2 in the appendix.

Table 4 displays the average over all 10 instances per instance class <u>of: t</u>he average objective function value at termination over all five runs of Experiment 1 (Obj); the coefficient of variation (CV), i.e., the ratio of the standard deviation to the mean, of the objective function value as a percentage; the objective function value of the best known solution (BKS); the optimality <u>gap</u> of B<u>KS</u> at termination (Gap) as a percentage; and the relative percentage deviation RPD = Obj − BKS /BKS · 100 at different points in time. Note that BKS corresponds to the objective function value at the termination of Experiment 2.

The results show that it is difficult to prove optimality with the given approach for VRPD-DSS instances with just 30 customers, and it becomes more difficult as the number of customers and drones increases. However, the solver is able to consistently provide good solutions in a reasonable amount of time. Similar to the optimality gap, the coefficient of variation of the objective function value increases with a growing number of customers and drones. This means that the spread of the objective function values at the end of Experiment 1 increases and the consistency decreases noticeably. Nevertheless, we consider an average coefficient of variation of 1 % as a small and acceptable spread. In addition to consistency, we assess Gurobi as providing good-quality solutions for the given instances. For instances with 30 and 40 customers, the av<u>erage</u> RPD is less than one percent within 600 s. After one hour of run time, the average RPD is between 0.13 % and 1.50 % for all instance sizes and only greater than 1 % for 50 customers and two drones per tandem. Note that the best known solution is almost always identical to the best solution found in Experiment 1 (RPD<sup>∗</sup> in Table A.2 is almost always 0). Thus, the best solution of an instance in Experiment 1 can very rarely be improved in eight hours in Experiment 2.

<table><tr><td rowspan="2">|C|</td><td rowspan="2">|D|</td><td rowspan="2"> $\overline{\text{Obj}}$ </td><td rowspan="2">CV [%]</td><td rowspan="2">BKS</td><td rowspan="2">Gap [%]</td><td colspan="6"> $\overline{\text{RPD}}$  [%]</td></tr><tr><td>60 s</td><td>120 s</td><td>300 s</td><td>600 s</td><td>1800 s</td><td>3600 s</td></tr><tr><td rowspan="2">30</td><td>1</td><td>116.39</td><td>0.06</td><td>116.23</td><td>2.64</td><td>0.47</td><td>0.33</td><td>0.27</td><td>0.13</td><td>0.13</td><td>0.13</td></tr><tr><td>2</td><td>108.81</td><td>0.27</td><td>108.44</td><td>4.09</td><td>2.39</td><td>1.49</td><td>0.93</td><td>0.71</td><td>0.47</td><td>0.33</td></tr><tr><td rowspan="2">40</td><td>1</td><td>129.23</td><td>0.25</td><td>128.95</td><td>7.43</td><td>1.75</td><td>1.20</td><td>0.85</td><td>0.61</td><td>0.28</td><td>0.22</td></tr><tr><td>2</td><td>119.30</td><td>0.37</td><td>118.79</td><td>12.06</td><td>6.97</td><td>2.92</td><td>1.23</td><td>0.97</td><td>0.58</td><td>0.43</td></tr><tr><td rowspan="2">50</td><td>1</td><td>149.01</td><td>0.50</td><td>148.29</td><td>9.30</td><td>7.18</td><td>4.18</td><td>2.07</td><td>1.55</td><td>0.76</td><td>0.49</td></tr><tr><td>2</td><td>138.08</td><td>1.00</td><td>136.04</td><td>15.37</td><td>21.95</td><td>15.11</td><td>5.35</td><td>3.01</td><td>1.91</td><td>1.50</td></tr></table>

Table 4: Aggregated results for experiments with larger instances

<table><tr><td rowspan="2">|C|</td><td rowspan="2">|D|</td><td colspan="2">Truck</td><td colspan="3">Drone</td><td colspan="4">Costs [$]</td><td rowspan="2">ΔTO [%]</td></tr><tr><td>Time [min]</td><td>Dist [km]</td><td>#OP</td><td>Dist [km]</td><td>#CC</td><td>Wages</td><td>Fuel</td><td>Power</td><td>Total</td></tr><tr><td rowspan="2">30</td><td>1</td><td>270.73</td><td>160.76</td><td>5.90</td><td>37.15</td><td>2.92</td><td>90.25</td><td>25.72</td><td>0.26</td><td>116.23</td><td>-12.56</td></tr><tr><td>2</td><td>250.42</td><td>153.26</td><td>4.90</td><td>32.36</td><td>2.52</td><td>83.48</td><td>24.52</td><td>0.45</td><td>108.44</td><td>-18.36</td></tr><tr><td rowspan="2">40</td><td>1</td><td>304.29</td><td>170.06</td><td>8.00</td><td>43.68</td><td>3.48</td><td>101.44</td><td>27.21</td><td>0.31</td><td>128.95</td><td>-14.68</td></tr><tr><td>2</td><td>277.51</td><td>160.96</td><td>6.60</td><td>37.27</td><td>2.96</td><td>92.51</td><td>25.76</td><td>0.52</td><td>118.79</td><td>-21.41</td></tr><tr><td rowspan="2">50</td><td>1</td><td>352.78</td><td>189.52</td><td>10.50</td><td>50.03</td><td>4.12</td><td>117.60</td><td>30.33</td><td>0.36</td><td>148.29</td><td>-14.75</td></tr><tr><td>2</td><td>321.69</td><td>176.18</td><td>8.15</td><td>43.33</td><td>3.48</td><td>107.24</td><td>28.19</td><td>0.61</td><td>136.04</td><td>-21.89</td></tr></table>

Table 5: Aggregated information on solutions for tandems with one and two drones.

## 6.3.2. Benefits of truck-drone tandems

Finally, we analyze the benefits and cost-savings of truck-drone tandems for the VRPD-DSS compared to traditional truck-only delivery (TO). We use the best solution for each instance obtained in the experiments to determine potential savings. Detailed information on the results are provided in the appendix. Table A.3 presents information on the instances and truck-only delivery, while Table A.4 and Table A.5 show detailed results for tandems with one and two drones, respectively.

Table 5 displays the average solution information for different numbers of customers and drones. It includes the operating time of trucks (Time); the distance traveled by trucks (Dist); the number of operations per drone (#OP); the distance covered per drone (Dist); the number of charge cycles per drone (#CC); the different cost components, i.e., wages, fuel, and power; the total costs (Total); and finally, the relative change in the total costs compared to truck-only delivery (∆TO) as percentages.

The results show that significant cost-savings can be achieved by using truck-drone tandems and that savings increase with an additional drone. However, the benefit of the second drone is less than the benefit of the first drone. As expected, the total number of drone operations and the total distance traveled by all drones increase when two drones are used instead of one drone per tandem. Thus, more customers are served by drones, which results in lower costs. However, the workload per drone decreases, which may result in longer life spans of drones and batteries. Furthermore, savings increase with the number of customers, i.e., with higher customer density, since higher customer density leads to more feasible drone operations (see |W| in Table A.3). Yet the increase from 40 to 50 customers is very small, so perhaps there is a saturation effect that limits the positive impact of customer density on savings, or the heuristic solutions for instances with 50 customers have poorer quality.

Finally, Figure 6 presents a more detailed insight into the cost components and savings. First, we observe that wages account for the largest share of the costs. Fuel costs are less than a quarter of the total operational costs, while power costs are almost negligible. Note that, although power costs have little impact on the total costs, proper consideration of the energy consumption is critical for feasibility, and including drone operations also reduces wages and fuel costs. Moreover, the average reduction in wages is greater than the average reduction in fuel costs. For example, for instances with 30 customers, the use of tandems with a single drone can reduce wages by 13.7 %, while fuel costs can be reduced only by 9.5 %. Hence, the application of drones can reduce working hours more than the traveled distance of trucks. This highlights expedited delivery through parallelization of services as one of the key benefits of truck-drone tandems. Therefore, it is advisable to include some element of time in the evaluation of truck-drone tandems when comparing them to traditional truck-only delivery.

## 7. Conclusion and future research

In this paper, combined parcel delivery by trucks and drones is studied, where the speed of a drone flight can be selected from a discrete set of different speeds. We call this problem the vehicle routing problem with drones and drone speed selection, and the following trade-off in speed selection is considered: On one hand, a faster speed shortens delivery times; on the other, it leads to increased energy consumption and, thereby, to a shorter range. We introduce an MILP for this problem, as well as preprocessing methods to eliminate dominated drone speeds and unnecessary variables, and valid inequalities to further strengthen the formulation. We test our approach on instances that closely resemble a real-world scenario in a rural area. The results clearly demonstrate the effectiveness of the preprocessing methods. We also show that, if only a single speed is available for each drone flight, increasing the speed above a threshold does not usually lead to lower costs. However, this threshold differs between instances. Therefore, from a cost perspective, it is always beneficial to consider multiple speeds. The results further indicate that a general solver such as Gurobi can consistently provide high-quality solutions for larger instances of the VRPD-DSS with up to 50 customers. Finally, our results show that truck-drone tandems can achieve significant savings compared to truck-only delivery for the rural scenario considered here. In addition, truck-driver wages account for the largest share of costs but can also be reduced the most by using tandems. In contrast, electricity costs for the drones are almost negligible. However, considering the energy consumption of drones with different speeds is crucial for the feasibility of solutions.

![](images/page_28_chart_0.jpg)

Figure 6: Cost structure of different delivery systems and average savings of a tandem with one drone (T-1D) and two drones (T-2D) compared to truck-only delivery (TO)

There are many potential avenues for future research. For example, heuristic algorithms can be developed for the VRPD-DSS, and the solutions obtained with the exact approach presented here can be used to evaluate the algorithms. In addition, VRPD-DSS heuristics can be compared to heuristics for the mFSTSP-VDS to investigate the effects of discrete speed levels instead of continuous drone-speed decision variables. Other exact approaches could also be developed to consider continuous drone speeds. A further interesting area of research could be the incorporation of external circumstances such as weather in order to derive more-robust routing decisions.

## References

[1] N. Agatz, P. Bouman, and M. Schmidt. Optimization approaches for the traveling salesman problem with drone. Transportation Science, 52(4):965–981, 2018.

[2] T. Berthold. Measuring the impact of primal heuristics. Operations Research Letters, 41(6):611–614, 2013. ISSN 0167-6377.

[3] M. Boccia, A. Masone, A. Sforza, and C. Sterle. A column-and-row generation approach for the flying sidekick travelling salesman problem. Transportation Research Part C: Emerging Technologies, 124: 102913, 2021. ISSN 0968-090X.

[4] P. Bouman, N. Agatz, and M. Schmidt. Dynamic programming approaches for the traveling salesman problem with drone. Networks, 72(4):528–542, 2018.

[5] N. Boysen, S. Fedtke, and S. Schwerdfeger. Last-mile delivery concepts: a survey from an operational research perspective. Or Spectrum, 43(1):1–58, 2021.

[6] G. Campuzano, E. Lalla-Ruiz, and M. Mes. A multi-start vns algorithm for the tsp-d with energy constraints. In International Conference on Computational Logistics, pages 393–409. Springer, 2021.

[7] S. Cavani, M. Iori, and R. Roberti. Exact methods for the traveling salesman problem with multiple drones. Transportation Research Part C: Emerging Technologies, 130:103280, 2021. ISSN 0968-090X.

[8] C. Cheng, Y. Adulyasak, and L.-M. Rousseau. Drone routing with energy function: Formulation and exact algorithm. Transportation Research Part B: Methodological, 139:364–387, 2020. ISSN 0191-2615.

[9] S. H. Chung, B. Sah, and J. Lee. Optimization for drone and drone-truck combined operations: A review of the state of the art and future directions. Computers & Operations Research, 123:105004, 2020.

[10] Daimler AG. The Mercedes-Benz Vision Van. For a highly efficient logistics concept, 2019. URL [https://www.daimler.com/innovation/specials/vision-van/en/](https://www.daimler.com/innovation/specials/vision-van/en/).

[11] R. Daknama and E. Kraus. Vehicle routing with drones. arXiv preprint arXiv:1705.06431, 2017. URL [https://arxiv.org/abs/1705.06431](https://arxiv.org/abs/1705.06431).

[12] J. C. de Freitas and P. H. V. Penna. A variable neighborhood search for flying sidekick traveling salesman problem. International Transactions in Operational Research, 27(1):267–290, 2020.

[13] M. Dell’Amico, R. Montemanni, and S. Novellani. Modeling the flying sidekick traveling salesman problem with multiple drones. Networks, 2021.

[14] M. Dell’Amico, R. Montemanni, and S. Novellani. Exact models for the flying sidekick traveling salesman problem. International Transactions in Operational Research, n/a(n/a), 2021.

[15] M. Dell’Amico, R. Montemanni, and S. Novellani. Algorithms based on branch and bound for the flying sidekick traveling salesman problem. Omega, 104:102493, 2021. ISSN 0305-0483.

[16] L. Di Puglia Pugliese and F. Guerriero. Last-mile deliveries by using drones and classical vehicles. In International Conference on Optimization and Decision Science, pages 557–565. Springer, 2017.

[17] L. Di Puglia Pugliese, G. Macrina, and F. Guerriero. Trucks and drones cooperation in the last-mile delivery process. Networks, 2020.

[18] O. Dukkanci, B. Y. Kara, and T. Bektaş. Minimizing energy and cost in range-limited drone deliveries with speed optimization. Transportation Research Part C: Emerging Technologies, 125:102985, 2021.

[19] F. Gaba and M. Winkenbach. A systems-level technology policy analysis of the truck-and-drone cooperative delivery vehicle system. Technical Report 2020-mitscale-ctl-03, MIT Global Supply Chain and Logistics Excellence Network, 2020.

[20] GeoPy. Documentation, 2019. URL [https://geopy.readthedocs.io/en/stable/](https://geopy.readthedocs.io/en/stable/).

[21] Grepow Inc. Tattu uav drone battery, 2019. URL [https://www.grepow.com/page/uav-battery.html#2](https://www.grepow.com/page/uav-battery.html#2).

[22] Q. M. Ha, Y. Deville, Q. D. Pham, and M. H. Hà. A hybrid genetic algorithm for the traveling salesman problem with drone. Journal of Heuristics, 26(2):219–247, 2020.

[23] H. Y. Jeong, B. D. Song, and S. Lee. Truck-drone hybrid delivery routing: Payload-energy dependency and no-fly zones. International Journal of Production Economics, 214:220–233, 2019. ISSN 0925-5273.

[24] P. Kitjacharoenchai, M. Ventresca, M. Moshref-Javadi, S. Lee, J. M. Tanchoco, and P. A. Brunese. Multiple traveling salesman problem with drones: Mathematical model and heuristic approach. Computers & Industrial Engineering, 129:14 – 30, 2019.

[25] M. Lammert and K. Walkowicz. Thirty-six month evaluation of ups diesel hybrid-electric delivery vans. Technical Report NREL/TP-5400-53503, National Renewable Energy Laboratory, 2012.

[26] Y. Liu, Z. Liu, J. Shi, G. Wu, and W. Pedrycz. Two-echelon routing problem for parcel delivery by cooperated truck and drone. IEEE Transactions on Systems, Man, and Cybernetics: Systems, pages 1–16, 2020. doi: 10.1109/TSMC.2020.2968839.

[27] G. Macrina, L. Di Puglia Pugliese, F. Guerriero, and G. Laporte. Drone-aided routing: A literature review. Transportation Research Part C: Emerging Technologies, 120:102762, 2020.

[28] M. Moshref-Javadi and M. Winkenbach. Applications and research avenues for drone-based models in logistics: A classification and review. Expert Systems with Applications, 177:114854, 2021.

[29] C. C. Murray and A. G. Chu. The flying sidekick traveling salesman problem: Optimization of drone-assisted parcel delivery. Transportation Research Part C: Emerging Technologies, 54:86–109, 2015.

[30] C. C. Murray and R. Raj. The multiple flying sidekicks traveling salesman problem: Parcel delivery with multiple drones. Transportation Research Part C: Emerging Technologies, 110:368–398, 2020.

[31] openrouteservice.org. openrouteservice, 2019. URL [https://openrouteservice.org/](https://openrouteservice.org/).

[32] A. Otto, N. Agatz, J. Campbell, B. Golden, and E. Pesch. Optimization approaches for civil applications of unmanned aerial vehicles (UAVs) or aerial drones: A survey. Networks, 72(4):411–458, 2018.

[33] S. Poikonen and B. Golden. Multi-visit drone routing problem. Computers & Operations Research, 113: 104802, 2020. ISSN 0305-0548.

[34] S. Poikonen, B. Golden, and E. A. Wasil. A branch-and-bound approach to the traveling salesman problem with a drone. INFORMS Journal on Computing, 31(2):335–346, 2019.

[35] R. Raj and C. Murray. The multiple flying sidekicks traveling salesman problem with variable drone speeds. Transportation Research Part C: Emerging Technologies, 120:102813, 2020.

[36] R. Roberti and M. Ruthmair. Exact methods for the traveling salesman problem with drone. Transportation Science, 55(2):315–335, 2021.

[37] D. Rojas Viloria, E. L. Solano-Charris, A. Muñoz-Villamizar, and J. R. Montoya-Torres. Unmanned aerial vehicles/drones in vehicle routing problems: a literature review. International Transactions in Operational Research, 28(4):1626–1657, 2021.

[38] D. Sacramento, D. Pisinger, and S. Ropke. An adaptive large neighborhood search metaheuristic for the vehicle routing problem with drones. Transportation Research Part C: Emerging Technologies, 102: 289–315, 2019.

[39] D. Schermer, M. Moeini, and O. Wendt. A hybrid vns/tabu search algorithm for solving the vehicle routing problem with drones and en route operations. Computers & Operations Research, 109:134–158, 2019.

[40] D. Schermer, M. Moeini, and O. Wendt. A matheuristic for the vehicle routing problem with drones and its variants. Transportation Research Part C: Emerging Technologies, 106:166–204, 2019. ISSN 0968-090X.

[41] J. K. Stolaroff, C. Samaras, E. R. O’Neill, A. Lubers, A. S. Mitchell, and D. Ceperley. Energy use and life cycle greenhouse gas emissions of drones for commercial package delivery. Nature communications, 9 (1):409, 2018.

[42] F. Tamke. VRPD-DSS, Nov 2021. URL [https://github.com/FelTam/VRPD-DSS](https://github.com/FelTam/VRPD-DSS).

[43] F. Tamke and U. Buscher. A branch-and-cut algorithm for the vehicle routing problem with drones. Transportation Research Part B: Methodological, 144:174–203, 2021.

[44] S. A. Vásquez, G. Angulo, and M. A. Klapp. An exact solution method for the tsp with drone based on decomposition. Computers & Operations Research, 127:105127, 2021. ISSN 0305-0548.

[45] D. Wang, P. Hu, J. Du, P. Zhou, T. Deng, and M. Hu. Routing and scheduling for hybrid truck-drone collaborative parcel delivery with independent and truck-carried drones. IEEE Internet of Things Journal, 6(6):10483–10495, 2019.

[46] X. Wang, S. Poikonen, and B. Golden. The vehicle routing problem with drones: Several worst-case results. Optimization Letters, 11(4):679–697, 2017.

[47] Z. Wang and J.-B. Sheu. Vehicle routing problem with drones. Transportation research part B: methodological, 122:350–364, 2019.

[48] Workhorse. Horsefly drone delivery, 2015. URL [https://workhorse.com/horsefly.html](https://workhorse.com/horsefly.html).

[49] J. Zhang, J. F. Campbell, D. C. Sweeney II, and A. C. Hupman. Energy consumption models for delivery drones: A comparison and assessment. Transportation Research Part D: Transport and Environment, 90:102668, 2021.

## Appendix A. Tables

| n | number rotors | 8 |
| --- | --- | --- |
| D | diameter of rotor | 0.432 m |
| $m_{\mathrm{db}}$ | mass drone frame | 10 kg |
| $m_{\mathrm{b}}$ | mass battery | 6 kg |
| $c_{\mathrm{db}}$ | drag coefficient drone body | 1.49 |
| $c_{\mathrm{b}}$ | drag coefficient battery | 1.00 |
| $c_{\mathrm{p}}$ | drag coefficient package | 2.20 |
| $A_{\mathrm{db}}$ | projected area drone body | 0.224 m2 |
| $A_{\mathrm{b}}$ | projected area battery | 0.015 m2 |
| $A_{\mathrm{p}}$ | projected area package | 0.0929 m2 |
| g | standard acceleration due to gravity | 9.81 m/s2 |
| ρ | density of air | 1.2250 kg/m3 |

Table A.1: Parameters of the octocopter energy model as in [41]

<table><tr><td rowspan="2"> $|C|$ </td><td rowspan="2">Instance</td><td colspan="7"> $|D|=1$ </td><td colspan="7"> $|D|=2$ </td></tr><tr><td> $\overline{Obj}$ </td><td> $Obj^{*}$ </td><td>CV</td><td>BKS</td><td>Gap</td><td> $\overline{RPD}$ </td><td>RPD*</td><td> $\overline{Obj}$ </td><td> $Obj^{*}$ </td><td>CV</td><td>BKS</td><td>Gap</td><td> $\overline{RPD}$ </td><td>RPD*</td></tr><tr><td rowspan="10">30</td><td>SF_30_1</td><td>108.51</td><td>108.51</td><td>0.00</td><td>108.51</td><td>2.16</td><td>0.00</td><td>0.00</td><td>104.82</td><td>104.53</td><td>0.35</td><td>104.53</td><td>5.15</td><td>0.28</td><td>0.00</td></tr><tr><td>SF_30_2</td><td>122.89</td><td>122.33</td><td>0.23</td><td>122.33</td><td>0.00</td><td>0.46</td><td>0.00</td><td>115.91</td><td>115.86</td><td>0.09</td><td>115.01</td><td>0.00</td><td>0.78</td><td>0.74</td></tr><tr><td>SF_30_3</td><td>119.95</td><td>119.78</td><td>0.17</td><td>119.78</td><td>4.43</td><td>0.14</td><td>0.00</td><td>112.05</td><td>110.90</td><td>0.60</td><td>110.90</td><td>6.72</td><td>1.04</td><td>0.00</td></tr><tr><td>SF_30_4</td><td>122.51</td><td>122.42</td><td>0.06</td><td>121.95</td><td>4.96</td><td>0.46</td><td>0.39</td><td>110.22</td><td>110.22</td><td>0.00</td><td>110.22</td><td>5.95</td><td>0.00</td><td>0.00</td></tr><tr><td>SF_30_5</td><td>117.20</td><td>117.20</td><td>0.00</td><td>117.20</td><td>0.00</td><td>0.00</td><td>0.00</td><td>109.42</td><td>109.09</td><td>0.61</td><td>109.09</td><td>1.39</td><td>0.30</td><td>0.00</td></tr><tr><td>SF_30_6</td><td>119.68</td><td>119.67</td><td>0.00</td><td>119.67</td><td>1.52</td><td>0.01</td><td>0.00</td><td>111.30</td><td>111.15</td><td>0.26</td><td>111.15</td><td>2.48</td><td>0.13</td><td>0.00</td></tr><tr><td>SF_30_7</td><td>113.36</td><td>113.36</td><td>0.00</td><td>113.36</td><td>4.70</td><td>0.00</td><td>0.00</td><td>105.62</td><td>105.56</td><td>0.11</td><td>105.56</td><td>6.33</td><td>0.06</td><td>0.00</td></tr><tr><td>SF_30_8</td><td>104.96</td><td>104.96</td><td>0.00</td><td>104.96</td><td>2.71</td><td>0.00</td><td>0.00</td><td>98.58</td><td>98.08</td><td>0.41</td><td>98.08</td><td>3.45</td><td>0.51</td><td>0.00</td></tr><tr><td>SF_30_9</td><td>104.39</td><td>104.39</td><td>0.00</td><td>104.39</td><td>2.12</td><td>0.00</td><td>0.00</td><td>98.97</td><td>98.96</td><td>0.01</td><td>98.96</td><td>3.86</td><td>0.01</td><td>0.00</td></tr><tr><td>SF_30_10</td><td>130.42</td><td>130.14</td><td>0.11</td><td>130.14</td><td>3.79</td><td>0.22</td><td>0.00</td><td>121.18</td><td>120.94</td><td>0.24</td><td>120.94</td><td>5.60</td><td>0.20</td><td>0.00</td></tr><tr><td colspan="2">Avg</td><td>116.39</td><td>116.28</td><td>0.06</td><td>116.23</td><td>2.64</td><td>0.13</td><td>0.04</td><td>108.81</td><td>108.53</td><td>0.27</td><td>108.44</td><td>4.09</td><td>0.33</td><td>0.07</td></tr><tr><td rowspan="10">40</td><td>SF_40_1</td><td>127.71</td><td>127.71</td><td>0.00</td><td>127.71</td><td>7.74</td><td>0.00</td><td>0.00</td><td>119.85</td><td>119.15</td><td>0.42</td><td>119.15</td><td>12.32</td><td>0.59</td><td>0.00</td></tr><tr><td>SF_40_2</td><td>126.90</td><td>126.63</td><td>0.28</td><td>126.63</td><td>6.08</td><td>0.21</td><td>0.00</td><td>117.70</td><td>117.63</td><td>0.09</td><td>117.63</td><td>8.43</td><td>0.06</td><td>0.00</td></tr><tr><td>SF_40_3</td><td>132.23</td><td>132.23</td><td>0.00</td><td>132.23</td><td>6.74</td><td>0.00</td><td>0.00</td><td>122.76</td><td>122.76</td><td>0.00</td><td>122.76</td><td>7.85</td><td>0.00</td><td>0.00</td></tr><tr><td>SF_40_4</td><td>119.02</td><td>118.29</td><td>0.38</td><td>118.29</td><td>7.97</td><td>0.62</td><td>0.00</td><td>109.38</td><td>108.83</td><td>0.43</td><td>108.83</td><td>18.51</td><td>0.51</td><td>0.00</td></tr><tr><td>SF_40_5</td><td>127.12</td><td>127.12</td><td>0.00</td><td>127.12</td><td>5.72</td><td>0.00</td><td>0.00</td><td>116.87</td><td>116.48</td><td>0.28</td><td>116.48</td><td>11.28</td><td>0.33</td><td>0.00</td></tr><tr><td>SF_40_6</td><td>131.04</td><td>130.44</td><td>0.56</td><td>130.44</td><td>8.33</td><td>0.46</td><td>0.00</td><td>121.57</td><td>120.04</td><td>0.89</td><td>120.04</td><td>12.82</td><td>1.27</td><td>0.00</td></tr><tr><td>SF_40_7</td><td>134.06</td><td>133.90</td><td>0.24</td><td>133.90</td><td>8.68</td><td>0.12</td><td>0.00</td><td>125.34</td><td>124.70</td><td>0.33</td><td>124.70</td><td>12.21</td><td>0.51</td><td>0.00</td></tr><tr><td>SF_40_8</td><td>128.36</td><td>127.99</td><td>0.26</td><td>127.99</td><td>6.21</td><td>0.29</td><td>0.00</td><td>118.94</td><td>118.42</td><td>0.38</td><td>118.42</td><td>13.72</td><td>0.44</td><td>0.00</td></tr><tr><td>SF_40_9</td><td>134.37</td><td>134.20</td><td>0.26</td><td>134.20</td><td>8.92</td><td>0.13</td><td>0.00</td><td>121.97</td><td>121.41</td><td>0.68</td><td>121.41</td><td>14.23</td><td>0.46</td><td>0.00</td></tr><tr><td>SF_40_10</td><td>131.52</td><td>131.02</td><td>0.55</td><td>131.02</td><td>7.89</td><td>0.38</td><td>0.00</td><td>118.57</td><td>118.44</td><td>0.23</td><td>118.44</td><td>9.22</td><td>0.11</td><td>0.00</td></tr><tr><td colspan="2">Avg</td><td>129.23</td><td>128.95</td><td>0.25</td><td>128.95</td><td>7.43</td><td>0.22</td><td>0.00</td><td>119.30</td><td>118.79</td><td>0.37</td><td>118.79</td><td>12.06</td><td>0.43</td><td>0.00</td></tr><tr><td rowspan="10">50</td><td>SF_50_1</td><td>151.61</td><td>150.63</td><td>0.34</td><td>150.63</td><td>12.91</td><td>0.65</td><td>0.00</td><td>135.10</td><td>133.91</td><td>1.05</td><td>133.91</td><td>14.91</td><td>0.89</td><td>0.00</td></tr><tr><td>SF_50_2</td><td>154.33</td><td>153.62</td><td>0.38</td><td>153.62</td><td>9.06</td><td>0.46</td><td>0.00</td><td>143.82</td><td>143.11</td><td>0.53</td><td>143.11</td><td>19.36</td><td>0.50</td><td>0.00</td></tr><tr><td>SF_50_3</td><td>147.26</td><td>145.66</td><td>1.24</td><td>145.66</td><td>8.01</td><td>1.10</td><td>0.00</td><td>141.81</td><td>134.83</td><td>2.74</td><td>134.83</td><td>15.53</td><td>5.18</td><td>0.00</td></tr><tr><td>SF_50_4</td><td>150.35</td><td>150.18</td><td>0.23</td><td>150.18</td><td>8.76</td><td>0.11</td><td>0.00</td><td>137.67</td><td>137.13</td><td>0.43</td><td>137.13</td><td>11.88</td><td>0.39</td><td>0.00</td></tr><tr><td>SF_50_5</td><td>147.10</td><td>146.02</td><td>0.97</td><td>146.02</td><td>8.90</td><td>0.74</td><td>0.00</td><td>136.86</td><td>134.99</td><td>1.31</td><td>134.99</td><td>17.54</td><td>1.39</td><td>0.00</td></tr><tr><td>SF_50_6</td><td>147.32</td><td>146.94</td><td>0.15</td><td>146.94</td><td>8.35</td><td>0.26</td><td>0.00</td><td>135.97</td><td>134.42</td><td>0.77</td><td>133.71</td><td>13.28</td><td>0.53</td><td>0.00</td></tr><tr><td>SF_50_7</td><td>162.37</td><td>161.46</td><td>0.66</td><td>161.46</td><td>8.50</td><td>0.56</td><td>0.00</td><td>151.34</td><td>149.99</td><td>0.49</td><td>149.99</td><td>11.70</td><td>0.90</td><td>0.00</td></tr><tr><td>SF_50_8</td><td>143.42</td><td>142.36</td><td>0.81</td><td>142.36</td><td>7.91</td><td>0.74</td><td>0.00</td><td>131.78</td><td>130.77</td><td>0.49</td><td>130.77</td><td>15.03</td><td>0.77</td><td>0.00</td></tr><tr><td>SF_50_9</td><td>139.75</td><td>139.75</td><td>0.00</td><td>139.75</td><td>9.55</td><td>0.00</td><td>0.00</td><td>130.28</td><td>127.69</td><td>1.37</td><td>127.69</td><td>16.58</td><td>2.03</td><td>0.00</td></tr><tr><td>SF_50_10</td><td>146.61</td><td>146.28</td><td>0.26</td><td>146.28</td><td>11.02</td><td>0.23</td><td>0.00</td><td>135.91</td><td>134.24</td><td>0.82</td><td>134.24</td><td>17.84</td><td>1.24</td><td>0.00</td></tr><tr><td colspan="2">Avg</td><td>149.01</td><td>148.29</td><td>0.50</td><td>148.29</td><td>9.30</td><td>0.49</td><td>0.00</td><td>138.05</td><td>136.11</td><td>1.00</td><td>136.04</td><td>15.37</td><td>1.50</td><td>0.05</td></tr></table>

Obj - Average obj ective function value at termination ( Experiment 1 )

Obj ∗ - Best obj ect ive funct ion value at terminat ion ( Exp eriment 1 )

CV - Coefficient of variation

B K S - Best known solution , corresponds to the obj ective function value at termination ( Experiment 2 )

Gap - Optimality gap of BK S at termination in percent ( Experiment 2 )

RP D - Relative percent age deviation of Obj with respect to BK S

RP D ∗ - Relative percent age deviation of Obj ∗ with respect to B K S

Table A . 2 : Det ailed result s for MILP solver as heurist ic for exp eriment s wit h larger inst ances

<table><tr><td rowspan="2">|C|</td><td rowspan="2">Instance</td><td rowspan="2">|C|</td><td rowspan="2">|W|</td><td colspan="2">Truck</td><td colspan="3">Costs [$]</td></tr><tr><td>Time [min]</td><td>Dist [km]</td><td>Wages</td><td>Fuel</td><td>Total</td></tr><tr><td rowspan="10">30</td><td>SF_30_1</td><td>22</td><td>5789</td><td>290.03</td><td>153.15</td><td>96.69</td><td>24.50</td><td>121.19</td></tr><tr><td>SF_30_2</td><td>18</td><td>1393</td><td>330.72</td><td>187.26</td><td>110.25</td><td>29.96</td><td>140.21</td></tr><tr><td>SF_30_3</td><td>19</td><td>1466</td><td>315.10</td><td>178.29</td><td>105.04</td><td>28.53</td><td>133.57</td></tr><tr><td>SF_30_4</td><td>23</td><td>1236</td><td>337.82</td><td>184.52</td><td>112.61</td><td>29.52</td><td>142.14</td></tr><tr><td>SF_30_5</td><td>21</td><td>1938</td><td>327.00</td><td>190.07</td><td>109.01</td><td>30.41</td><td>139.42</td></tr><tr><td>SF_30_6</td><td>18</td><td>1588</td><td>324.42</td><td>183.67</td><td>108.15</td><td>29.39</td><td>137.54</td></tr><tr><td>SF_30_7</td><td>20</td><td>2714</td><td>306.67</td><td>176.89</td><td>102.23</td><td>28.30</td><td>130.53</td></tr><tr><td>SF_30_8</td><td>18</td><td>3901</td><td>281.42</td><td>163.23</td><td>93.81</td><td>26.12</td><td>119.93</td></tr><tr><td>SF_30_9</td><td>20</td><td>4023</td><td>280.03</td><td>158.53</td><td>93.35</td><td>25.37</td><td>118.72</td></tr><tr><td>SF_30_10</td><td>19</td><td>1594</td><td>343.77</td><td>200.57</td><td>114.60</td><td>32.09</td><td>146.69</td></tr><tr><td>Avg</td><td></td><td>19.8</td><td>2564.2</td><td>313.70</td><td>177.62</td><td>104.57</td><td>28.42</td><td>132.99</td></tr><tr><td rowspan="10">40</td><td>SF_40_1</td><td>26</td><td>7012</td><td>351.95</td><td>193.77</td><td>117.33</td><td>31.00</td><td>148.33</td></tr><tr><td>SF_40_2</td><td>29</td><td>6291</td><td>351.08</td><td>184.20</td><td>117.04</td><td>29.47</td><td>146.51</td></tr><tr><td>SF_40_3</td><td>25</td><td>6055</td><td>359.02</td><td>199.14</td><td>119.68</td><td>31.86</td><td>151.54</td></tr><tr><td>SF_40_4</td><td>28</td><td>8452</td><td>337.88</td><td>171.67</td><td>112.64</td><td>27.47</td><td>140.10</td></tr><tr><td>SF_40_5</td><td>26</td><td>5026</td><td>363.95</td><td>197.57</td><td>121.33</td><td>31.61</td><td>152.94</td></tr><tr><td>SF_40_6</td><td>25</td><td>4796</td><td>375.78</td><td>202.95</td><td>125.27</td><td>32.47</td><td>157.74</td></tr><tr><td>SF_40_7</td><td>22</td><td>5642</td><td>370.98</td><td>190.17</td><td>123.67</td><td>30.43</td><td>154.10</td></tr><tr><td>SF_40_8</td><td>29</td><td>7113</td><td>367.85</td><td>187.38</td><td>122.63</td><td>29.98</td><td>152.61</td></tr><tr><td>SF_40_9</td><td>37</td><td>7139</td><td>377.13</td><td>203.96</td><td>125.72</td><td>32.63</td><td>158.35</td></tr><tr><td>SF_40_10</td><td>27</td><td>5144</td><td>358.42</td><td>186.91</td><td>119.48</td><td>29.91</td><td>149.39</td></tr><tr><td>Avg</td><td></td><td>27.4</td><td>6267.0</td><td>361.40</td><td>191.77</td><td>120.48</td><td>30.68</td><td>151.16</td></tr><tr><td rowspan="10">50</td><td>SF_50_1</td><td>29</td><td>9792</td><td>407.40</td><td>211.05</td><td>135.81</td><td>33.77</td><td>169.58</td></tr><tr><td>SF_50_2</td><td>41</td><td>10169</td><td>455.78</td><td>230.59</td><td>151.94</td><td>36.89</td><td>188.83</td></tr><tr><td>SF_50_3</td><td>33</td><td>11278</td><td>412.35</td><td>213.13</td><td>137.46</td><td>34.10</td><td>171.56</td></tr><tr><td>SF_50_4</td><td>33</td><td>10573</td><td>416.78</td><td>213.74</td><td>138.94</td><td>34.20</td><td>173.14</td></tr><tr><td>SF_50_5</td><td>34</td><td>16652</td><td>414.42</td><td>213.56</td><td>138.15</td><td>34.17</td><td>172.32</td></tr><tr><td>SF_50_6</td><td>36</td><td>18007</td><td>401.65</td><td>205.79</td><td>133.89</td><td>32.93</td><td>166.82</td></tr><tr><td>SF_50_7</td><td>31</td><td>7793</td><td>453.87</td><td>229.16</td><td>151.30</td><td>36.67</td><td>187.97</td></tr><tr><td>SF_50_8</td><td>29</td><td>9707</td><td>406.98</td><td>212.18</td><td>135.67</td><td>33.95</td><td>169.62</td></tr><tr><td>SF_50_9</td><td>31</td><td>19755</td><td>406.72</td><td>199.94</td><td>135.58</td><td>31.99</td><td>167.57</td></tr><tr><td>SF_50_10</td><td>36</td><td>15933</td><td>419.12</td><td>207.15</td><td>139.72</td><td>33.14</td><td>172.86</td></tr><tr><td>Avg</td><td></td><td>33.3</td><td>12965.9</td><td>419.51</td><td>213.63</td><td>139.85</td><td>34.18</td><td>174.03</td></tr></table>

Table A.3: Information on instances and detailed results for truck usage and costs for truck-only delivery.

<table><tr><td rowspan="2">|C|</td><td rowspan="2">Instance</td><td colspan="2">Truck</td><td colspan="3">Drone</td><td colspan="4">Costs[$]</td><td colspan="3">ΔTO [%]</td></tr><tr><td>Time [min]</td><td>Dist [km]</td><td>#OP</td><td>Dist [km]</td><td>#CC</td><td>Wages</td><td>Fuel</td><td>Power</td><td>Total</td><td>Wages</td><td>Fuel</td><td>Total</td></tr><tr><td rowspan="10">30</td><td>SF_30_1</td><td>254.97</td><td>145.46</td><td>6.00</td><td>32.72</td><td>2.70</td><td>85.00</td><td>23.27</td><td>0.24</td><td>108.51</td><td>-12.09</td><td>-5.02</td><td>-10.46</td></tr><tr><td>SF_30_2</td><td>285.51</td><td>168.06</td><td>6.00</td><td>37.31</td><td>2.97</td><td>95.18</td><td>26.89</td><td>0.26</td><td>122.33</td><td>-13.67</td><td>-10.25</td><td>-12.75</td></tr><tr><td>SF_30_3</td><td>278.23</td><td>167.54</td><td>5.00</td><td>32.58</td><td>2.58</td><td>92.75</td><td>26.81</td><td>0.23</td><td>119.78</td><td>-11.70</td><td>-6.03</td><td>-10.32</td></tr><tr><td>SF_30_4</td><td>288.59</td><td>159.08</td><td>5.00</td><td>43.41</td><td>3.37</td><td>96.20</td><td>25.45</td><td>0.30</td><td>121.95</td><td>-14.57</td><td>-13.79</td><td>-14.20</td></tr><tr><td>SF_30_5</td><td>274.23</td><td>159.48</td><td>6.00</td><td>36.31</td><td>3.04</td><td>91.42</td><td>25.52</td><td>0.27</td><td>117.20</td><td>-16.14</td><td>-16.08</td><td>-15.94</td></tr><tr><td>SF_30_6</td><td>279.59</td><td>163.71</td><td>6.00</td><td>39.93</td><td>3.12</td><td>93.20</td><td>26.19</td><td>0.27</td><td>119.67</td><td>-13.82</td><td>-10.89</td><td>-12.99</td></tr><tr><td>SF_30_7</td><td>261.63</td><td>161.68</td><td>7.00</td><td>41.20</td><td>3.15</td><td>87.22</td><td>25.87</td><td>0.28</td><td>113.36</td><td>-14.68</td><td>-8.59</td><td>-13.15</td></tr><tr><td>SF_30_8</td><td>243.97</td><td>146.39</td><td>6.00</td><td>29.32</td><td>2.32</td><td>81.33</td><td>23.42</td><td>0.20</td><td>104.96</td><td>-13.30</td><td>-10.34</td><td>-12.48</td></tr><tr><td>SF_30_9</td><td>240.87</td><td>149.09</td><td>6.00</td><td>34.41</td><td>2.71</td><td>80.30</td><td>23.86</td><td>0.24</td><td>104.39</td><td>-13.98</td><td>-5.95</td><td>-12.07</td></tr><tr><td>SF_30_10</td><td>299.70</td><td>187.15</td><td>6.00</td><td>44.30</td><td>3.28</td><td>99.91</td><td>29.94</td><td>0.29</td><td>130.14</td><td>-12.82</td><td>-6.70</td><td>-11.28</td></tr><tr><td>Avg</td><td></td><td>270.73</td><td>160.76</td><td>5.90</td><td>37.15</td><td>2.92</td><td>90.25</td><td>25.72</td><td>0.26</td><td>116.23</td><td>-13.68</td><td>-9.36</td><td>-12.56</td></tr><tr><td rowspan="10">40</td><td>SF_40_1</td><td>301.64</td><td>167.78</td><td>9.00</td><td>42.17</td><td>3.54</td><td>100.56</td><td>26.84</td><td>0.31</td><td>127.71</td><td>-14.29</td><td>-13.42</td><td>-13.90</td></tr><tr><td>SF_40_2</td><td>300.20</td><td>164.11</td><td>8.00</td><td>42.09</td><td>3.46</td><td>100.07</td><td>26.26</td><td>0.30</td><td>126.63</td><td>-14.50</td><td>-10.89</td><td>-13.57</td></tr><tr><td>SF_40_3</td><td>310.97</td><td>176.87</td><td>7.00</td><td>39.47</td><td>2.97</td><td>103.67</td><td>28.30</td><td>0.26</td><td>132.23</td><td>-13.38</td><td>-11.17</td><td>-12.74</td></tr><tr><td>SF_40_4</td><td>280.11</td><td>153.82</td><td>8.00</td><td>39.60</td><td>3.40</td><td>93.38</td><td>24.61</td><td>0.30</td><td>118.29</td><td>-17.10</td><td>-10.41</td><td>-15.57</td></tr><tr><td>SF_40_5</td><td>298.85</td><td>170.02</td><td>8.00</td><td>41.18</td><td>3.33</td><td>99.62</td><td>27.20</td><td>0.29</td><td>127.12</td><td>-17.89</td><td>-13.95</td><td>-16.88</td></tr><tr><td>SF_40_6</td><td>307.60</td><td>172.33</td><td>7.00</td><td>46.97</td><td>3.67</td><td>102.54</td><td>27.57</td><td>0.32</td><td>130.44</td><td>-18.14</td><td>-15.09</td><td>-17.31</td></tr><tr><td>SF_40_7</td><td>316.63</td><td>175.07</td><td>7.00</td><td>49.53</td><td>3.83</td><td>105.55</td><td>28.01</td><td>0.34</td><td>133.90</td><td>-14.65</td><td>-7.95</td><td>-13.11</td></tr><tr><td>SF_40_8</td><td>301.53</td><td>169.67</td><td>9.00</td><td>46.79</td><td>3.64</td><td>100.52</td><td>27.15</td><td>0.32</td><td>127.99</td><td>-18.03</td><td>-9.44</td><td>-16.13</td></tr><tr><td>SF_40_9</td><td>315.48</td><td>179.51</td><td>8.00</td><td>44.42</td><td>3.49</td><td>105.17</td><td>28.72</td><td>0.31</td><td>134.20</td><td>-16.35</td><td>-11.98</td><td>-15.25</td></tr><tr><td>SF_40_10</td><td>309.85</td><td>171.45</td><td>9.00</td><td>44.56</td><td>3.43</td><td>103.29</td><td>27.43</td><td>0.30</td><td>131.02</td><td>-13.55</td><td>-8.29</td><td>-12.30</td></tr><tr><td>Avg</td><td></td><td>304.29</td><td>170.06</td><td>8.00</td><td>43.68</td><td>3.48</td><td>101.44</td><td>27.21</td><td>0.31</td><td>128.95</td><td>-15.79</td><td>-11.26</td><td>-14.68</td></tr><tr><td rowspan="10">50</td><td>SF_50_1</td><td>356.03</td><td>197.39</td><td>10.00</td><td>49.44</td><td>4.15</td><td>118.68</td><td>31.58</td><td>0.36</td><td>150.63</td><td>-12.61</td><td>-6.49</td><td>-11.17</td></tr><tr><td>SF_50_2</td><td>367.72</td><td>191.66</td><td>9.00</td><td>53.40</td><td>4.18</td><td>122.58</td><td>30.67</td><td>0.37</td><td>153.62</td><td>-19.32</td><td>-16.86</td><td>-18.65</td></tr><tr><td>SF_50_3</td><td>348.02</td><td>182.93</td><td>11.00</td><td>52.00</td><td>4.24</td><td>116.01</td><td>29.27</td><td>0.37</td><td>145.66</td><td>-15.60</td><td>-14.16</td><td>-15.10</td></tr><tr><td>SF_50_4</td><td>356.84</td><td>192.77</td><td>11.00</td><td>53.63</td><td>4.31</td><td>118.95</td><td>30.84</td><td>0.38</td><td>150.18</td><td>-14.39</td><td>-9.82</td><td>-13.26</td></tr><tr><td>SF_50_5</td><td>348.54</td><td>184.23</td><td>10.00</td><td>49.66</td><td>3.99</td><td>116.19</td><td>29.48</td><td>0.35</td><td>146.02</td><td>-15.90</td><td>-13.73</td><td>-15.26</td></tr><tr><td>SF_50_6</td><td>349.67</td><td>187.73</td><td>10.00</td><td>46.47</td><td>3.86</td><td>116.56</td><td>30.04</td><td>0.34</td><td>146.94</td><td>-12.94</td><td>-8.78</td><td>-11.92</td></tr><tr><td>SF_50_7</td><td>383.20</td><td>208.28</td><td>11.00</td><td>53.96</td><td>4.41</td><td>127.74</td><td>33.33</td><td>0.39</td><td>161.46</td><td>-15.57</td><td>-9.11</td><td>-14.10</td></tr><tr><td>SF_50_8</td><td>336.55</td><td>186.18</td><td>10.00</td><td>49.22</td><td>4.30</td><td>112.19</td><td>29.79</td><td>0.38</td><td>142.36</td><td>-17.31</td><td>-12.25</td><td>-16.07</td></tr><tr><td>SF_50_9</td><td>333.30</td><td>176.90</td><td>11.00</td><td>45.44</td><td>3.82</td><td>111.11</td><td>28.30</td><td>0.34</td><td>139.75</td><td>-18.05</td><td>-11.53</td><td>-16.60</td></tr><tr><td>SF_50_10</td><td>347.95</td><td>187.16</td><td>12.00</td><td>47.09</td><td>3.91</td><td>115.99</td><td>29.95</td><td>0.34</td><td>146.28</td><td>-16.98</td><td>-9.63</td><td>-15.38</td></tr><tr><td>Avg</td><td></td><td>352.78</td><td>189.52</td><td>10.50</td><td>50.03</td><td>4.12</td><td>117.60</td><td>30.33</td><td>0.36</td><td>148.29</td><td>-15.87</td><td>-11.24</td><td>-14.75</td></tr><tr><td rowspan="10">30</td><td>SF_30_1</td><td>245.28</td><td>139.65</td><td>5.00</td><td>29.18</td><td>2.36</td><td>81.77</td><td>22.34</td><td>0.42</td><td>104.53</td><td>-15.43</td><td>-8.82</td><td>-13.75</td></tr><tr><td>SF_30_2</td><td>266.55</td><td>160.80</td><td>4.50</td><td>31.24</td><td>2.42</td><td>88.86</td><td>25.73</td><td>0.43</td><td>115.01</td><td>-19.40</td><td>-14.12</td><td>-17.97</td></tr><tr><td>SF_30_3</td><td>259.20</td><td>150.09</td><td>4.50</td><td>35.85</td><td>2.73</td><td>86.41</td><td>24.01</td><td>0.48</td><td>110.90</td><td>-17.74</td><td>-15.84</td><td>-16.97</td></tr><tr><td>SF_30_4</td><td>256.93</td><td>150.56</td><td>4.50</td><td>32.89</td><td>2.73</td><td>85.65</td><td>24.09</td><td>0.48</td><td>110.22</td><td>-23.94</td><td>-18.39</td><td>-22.46</td></tr><tr><td>SF_30_5</td><td>251.92</td><td>154.17</td><td>4.50</td><td>32.37</td><td>2.52</td><td>83.98</td><td>24.67</td><td>0.44</td><td>109.09</td><td>-22.96</td><td>-18.88</td><td>-21.75</td></tr><tr><td>SF_30_6</td><td>254.83</td><td>160.57</td><td>5.50</td><td>37.92</td><td>2.89</td><td>84.95</td><td>25.69</td><td>0.51</td><td>111.15</td><td>-21.45</td><td>-12.59</td><td>-19.19</td></tr><tr><td>SF_30_7</td><td>240.90</td><td>155.17</td><td>5.00</td><td>32.22</td><td>2.44</td><td>80.31</td><td>24.83</td><td>0.43</td><td>105.56</td><td>-21.44</td><td>-12.26</td><td>-19.13</td></tr><tr><td>SF_30_8</td><td>224.10</td><td>143.60</td><td>5.50</td><td>28.71</td><td>2.25</td><td>74.71</td><td>22.98</td><td>0.40</td><td>98.08</td><td>-20.36</td><td>-12.02</td><td>-18.22</td></tr><tr><td>SF_30_9</td><td>226.10</td><td>144.94</td><td>5.50</td><td>28.53</td><td>2.25</td><td>75.37</td><td>23.19</td><td>0.40</td><td>98.96</td><td>-19.26</td><td>-8.59</td><td>-16.64</td></tr><tr><td>SF_30_10</td><td>278.35</td><td>173.06</td><td>4.50</td><td>34.70</td><td>2.62</td><td>92.79</td><td>27.69</td><td>0.46</td><td>120.94</td><td>-19.03</td><td>-13.71</td><td>-17.55</td></tr><tr><td>Avg</td><td></td><td>250.42</td><td>153.26</td><td>4.90</td><td>32.36</td><td>2.52</td><td>83.48</td><td>24.52</td><td>0.45</td><td>108.44</td><td>-20.10</td><td>-13.52</td><td>-18.36</td></tr><tr><td rowspan="10">40</td><td>SF_40_1</td><td>279.58</td><td>158.84</td><td>6.50</td><td>38.19</td><td>3.04</td><td>93.20</td><td>25.42</td><td>0.53</td><td>119.15</td><td>-20.57</td><td>-18.00</td><td>-19.67</td></tr><tr><td>SF_40_2</td><td>273.50</td><td>161.93</td><td>8.00</td><td>37.25</td><td>3.11</td><td>91.18</td><td>25.91</td><td>0.55</td><td>117.63</td><td>-22.10</td><td>-12.08</td><td>-19.71</td></tr><tr><td>SF_40_3</td><td>285.22</td><td>170.34</td><td>6.00</td><td>29.94</td><td>2.40</td><td>95.08</td><td>27.25</td><td>0.42</td><td>122.76</td><td>-20.55</td><td>-14.47</td><td>-18.99</td></tr><tr><td>SF_40_4</td><td>257.80</td><td>140.10</td><td>6.00</td><td>34.85</td><td>2.70</td><td>85.94</td><td>22.42</td><td>0.47</td><td>108.83</td><td>-23.70</td><td>-18.38</td><td>-22.32</td></tr><tr><td>SF_40_5</td><td>269.82</td><td>162.64</td><td>6.50</td><td>36.70</td><td>2.91</td><td>89.95</td><td>26.02</td><td>0.51</td><td>116.48</td><td>-25.86</td><td>-17.68</td><td>-23.84</td></tr><tr><td>SF_40_6</td><td>279.72</td><td>164.11</td><td>6.00</td><td>39.21</td><td>3.06</td><td>93.25</td><td>26.26</td><td>0.54</td><td>120.04</td><td>-25.56</td><td>-19.13</td><td>-23.90</td></tr><tr><td>SF_40_7</td><td>292.78</td><td>165.86</td><td>6.50</td><td>39.65</td><td>3.17</td><td>97.60</td><td>26.54</td><td>0.56</td><td>124.70</td><td>-21.08</td><td>-12.78</td><td>-19.08</td></tr><tr><td>SF_40_8</td><td>276.57</td><td>160.56</td><td>7.00</td><td>39.34</td><td>3.05</td><td>92.20</td><td>25.69</td><td>0.54</td><td>118.42</td><td>-24.92</td><td>-14.51</td><td>-22.53</td></tr><tr><td>SF_40_9</td><td>282.51</td><td>166.69</td><td>7.00</td><td>39.64</td><td>3.20</td><td>94.18</td><td>26.67</td><td>0.56</td><td>121.41</td><td>-25.09</td><td>-18.27</td><td>-23.33</td></tr><tr><td>SF_40_10</td><td>277.64</td><td>158.55</td><td>6.50</td><td>37.88</td><td>2.93</td><td>92.56</td><td>25.37</td><td>0.52</td><td>118.44</td><td>-22.53</td><td>-15.18</td><td>-20.72</td></tr><tr><td>Avg</td><td></td><td>277.51</td><td>160.96</td><td>6.60</td><td>37.27</td><td>2.96</td><td>92.51</td><td>25.76</td><td>0.52</td><td>118.79</td><td>-23.20</td><td>-16.05</td><td>-21.41</td></tr><tr><td rowspan="10">50</td><td>SF_50_1</td><td>317.33</td><td>172.32</td><td>6.50</td><td>41.43</td><td>3.16</td><td>105.78</td><td>27.57</td><td>0.55</td><td>133.91</td><td>-22.11</td><td>-18.36</td><td>-21.03</td></tr><tr><td>SF_50_2</td><td>338.44</td><td>185.44</td><td>8.00</td><td>45.45</td><td>3.53</td><td>112.82</td><td>29.67</td><td>0.62</td><td>143.11</td><td>-24.98</td><td>-20.20</td><td>-23.70</td></tr><tr><td>SF_50_3</td><td>320.17</td><td>171.51</td><td>9.00</td><td>46.13</td><td>3.71</td><td>106.73</td><td>27.44</td><td>0.65</td><td>134.83</td><td>-23.74</td><td>-19.93</td><td>-22.61</td></tr><tr><td>SF_50_3</td><td>324.07</td><td>177.92</td><td>7.50</td><td>44.85</td><td>3.60</td><td>108.03</td><td>28.47</td><td>0.63</td><td>137.13</td><td>-22.25</td><td>-16.75</td><td>-20.80</td></tr><tr><td>SF_50_5</td><td>319.27</td><td>174.94</td><td>8.00</td><td>39.97</td><td>3.23</td><td>106.43</td><td>27.99</td><td>0.57</td><td>134.99</td><td>-22.96</td><td>-18.09</td><td>-21.66</td></tr><tr><td>SF_50_6</td><td>313.15</td><td>179.69</td><td>8.50</td><td>40.57</td><td>3.26</td><td>104.39</td><td>28.75</td><td>0.57</td><td>133.71</td><td>-22.03</td><td>-12.69</td><td>-19.85</td></tr><tr><td>SF_50_7</td><td>352.63</td><td>198.73</td><td>8.50</td><td>45.71</td><td>3.66</td><td>117.55</td><td>31.80</td><td>0.64</td><td>149.99</td><td>-22.31</td><td>-13.28</td><td>-20.21</td></tr><tr><td>SF_50_8</td><td>307.89</td><td>171.80</td><td>8.50</td><td>44.53</td><td>3.66</td><td>102.64</td><td>27.49</td><td>0.64</td><td>130.77</td><td>-24.35</td><td>-19.03</td><td>-22.90</td></tr><tr><td>SF_50_9</td><td>304.77</td><td>159.27</td><td>8.00</td><td>42.20</td><td>3.47</td><td>101.60</td><td>25.48</td><td>0.61</td><td>127.69</td><td>-25.06</td><td>-20.35</td><td>-23.80</td></tr><tr><td>SF_50_10</td><td>319.18</td><td>170.19</td><td>9.00</td><td>42.41</td><td>3.49</td><td>106.40</td><td>27.23</td><td>0.61</td><td>134.24</td><td>-23.85</td><td>-17.83</td><td>-22.34</td></tr><tr><td>Avg</td><td></td><td>321.69</td><td>176.18</td><td>8.15</td><td>43.33</td><td>3.48</td><td>107.24</td><td>28.19</td><td>0.61</td><td>136.04</td><td>-23.36</td><td>-17.65</td><td>-21.89</td></tr></table>

Table A . 4 : Detailed information on truck and drone usage and costs for tandems with one drone .