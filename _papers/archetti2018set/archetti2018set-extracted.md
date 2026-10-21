# Innovative Applications of O.R. The Set Orienteering Problem

Claudia Archetti a,∗, Francesco Carrabs b, Raffaele Cerulli b

![](data:image/jpeg;base64,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)

a Department of Economics and Management, University of Brescia, C.da S. Chiara 50, Brescia, Italy

b Department of Mathematics, University of Salerno, Via Giovanni Paolo II 132, Fisciano, Italy

## a r t i c l e i n f o

Article history: Received 1 June 2017 Accepted 8 November 2017 Available online 7 December 2017

Keywords: Routing Orienteering problem Matheuristic

## a b s t r a c t

In this paper, we study the Set Orienteering Problem which is a generalization of the Orienteering Problem where customers are grouped in clusters and a profit is associated with each cluster. The profit of a cluster is collected only if at least one customer from the cluster is visited. A single vehicle is available to collect the profit and the objective is to find the vehicle route that maximizes the profit collected and such that the route duration does not exceed a given threshold. We propose a mathematical formulation of the problem and a matheuristic algorithm. Computational tests are made on instances derived from benchmark instances for the Generalized Traveling Salesman Problem with up 1084 vertices. Results show that the matheuristic produces robust and high-quality solutions in a short computing time.

© 2017 Elsevier B.V. All rights reserved.

## 1. Introduction

Routing problems with profits received significant attention in recent years, as witnessed by the large literature surveyed in three recent papers, i.e., Archetti, Speranza, and Vigo (2014), Gunawan, Lau, and Vansteenwegen (2016) for routing problems with profits where the profit is associated with nodes of a graph, and Archetti and Speranza (2014) for problems where the profit is associated with arcs or edges of a graph. As witnessed by these three surveys, the literature on ‘node’ routing problems, i.e., the first of the two classes mentioned above, is much wider than the one on arc routing problems. In particular, among all node routing problems with profits studied in the literature, the most widely known is undoubtedly the Orienteering Problem (OP) where a profit is associated with each customer and the objective is to find a single vehicle tour maximizing the profit collected from visited customers and such that the duration of the tour does not exceed a maximum time limit. The profit of each customer can be collected at most once. The problem was first introduced in Tsiligirides (1984) and many variants of the problem have been studied, as described in Archetti et al. (2014), Gunawan et al. (2016). One of the most recent variants is the one presented in Angelelli, Archetti, and Vindigni (2014) where customers are grouped in clusters, a profit is associated with each cluster and it is collected only if all customers belonging to the cluster are visited. The authors called this problem the Clustered Orienteering Problem (COP). They present a mathematical formulation and two solution algorithms. They also describe practical applications related to the distribution of mass products where customers are retailers belonging to different supply chains.

In this paper, we are interested in a variant of the OP which shows some analogies with the one studied in Angelelli et al. (2014). In particular, we study the problem where customers are grouped in clusters. A profit is associated with each cluster and is collected only if at least one customer from the cluster is visited. The objective is to find the vehicle route that maximizes the collected profit and such that the corresponding duration does not exceed a given threshold. We call this problem the Set Orienteering Problem (SOP). The SOP finds application in mass distribution products, as for the COP, where a different distribution plan is sought. In particular, consider the case where customers belong to different supply chains and the carrier stipulates contracts with chains. Then, instead of having to serve all retailers belonging to the chain with which the contract has been stipulated, as happens in the COP, in the SOP the carrier may choose to serve only one customer from the chain (and, implicitly, serving the entire quantity demanded by the chain). This way, the carrier may be able to offer a better price for the service. The inner distribution among all retailers in the chain will be then organized internally. Thus, the SOP presents an alternative to the distribution strategy applied in the COP which may be advantageous both for the carrier and for the chains. Another application arises when customers are clustered in areas and the service to each area is made by delivering the entire quantity required by all customers in the area to a single customer, the one that is visited. This happens also when private customers group together to reach large quantity orders, and thus hopefully a lower price. Typically, in this case, the delivery is made to a single location.

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">∗ Corresponding author.</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">E-mail addresses: [claudia.archetti@unibs.it,](mailto:claudia.archetti@unibs.it) [archetti@eco.unibs.it](mailto:archetti@eco.unibs.it) (C. Archetti), [fcarrabs@unisa.it](mailto:fcarrabs@unisa.it) (F. Carrabs), [raffaele@unisa.it](mailto:raffaele@unisa.it) (R. Cerulli).</span></small>

The contribution of this paper can be summarized as follows. We introduce the SOP, present a formal description and a mathematical formulation. We then propose a matheuristic algorithm for its solution which is tested on instances derived from benchmark instances for the Generalized Traveling Salesman Problem (GTSP) with up to 1084 vertices. In particular, we first show the performance of the algorithm on small instances by comparing the results obtained from the matheuristic with optimal solutions. In addition, we test the performance of the matheuristic on large instances for which the optimal solution is known. We then present an exhaustive study of the contribution of the MILP embedded in the matheuristic. The results show that the contribution of the MILP is more evident on large instances. Moreover, even if the MILP makes the overall algorithm slower, computing times remain reasonable even on the largest instances.

The paper is organized as follows. A formal description of the problem together with a mathematical formulation are pre-sented in Section 2. The matheuristic algorithm is described in Section 3 while computational results are presented in Section 4. Finally, conclusions are drawn in Section 5.

## 2. Problem description and formulation

As the SOP is a generalization of the OP, we first provide a formal description of the OP.

The OP is defined on a complete directed graph $G = ( V , A )$ where $V = \{ 0 \} \cup C .$ Vertex 0 represents the depot from which the vehicle starts and ends its tour. C is the set of customers. A profit $p _ { i }$ is associated with each customer i ∈ C and is collected if and only if customer i is visited by the vehicle. Moreover, a cost $c _ { i j }$ is associated with each arc $( i , j )   \in   A .$ The objective is to find the tour that maximizes the collected profit and such that the associated cost (or duration) does not exceed a maximum value $T _ { m a x }$

In this paper we study a variant of the OP which we call the Set Orienteering Problem (SOP). In the SOP, customers in C are grouped in clusters $C _ { g }$ with $g = 1 , \ldots , l$ such that $\textstyle \bigcup _ { g = 1 } ^ { l } C _ { g } = C$ and $C _ { g } \cap C _ { h } =$ ∅, $\forall C _ { g } , C _ { h } \in \dot { \mathcal { P } }$ where $\mathcal { P } = \{ C _ { 1 } , \dots , C _ { l } \}$ is the set of clusters. A profit p<sub>g</sub> is associated with each cluster and is collected if and only if at least a customer $i \in C _ { \mathtt { g } }$ is visited in the tour. The profit of each cluster can be collected at most once. As in the OP, the objective is to find the tour that maximizes the collected profit and such that the associated cost does not exceed $T _ { m a x } .$ In the following, we assume that costs $c _ { i j }$ satisfy the triangle inequality. In this case, as shown in Laporte and Norbert (1983), an optimal solution always exists where one vertex per cluster at most is visited. This property is used in the solution method presented in Section 3.

In order to present a mathematical formulation for the SOP, we need the following notation. For any subset of vertices $S \subset V ,$ we define $\delta ^ { + } ( S ) = \left\{ ( i , j ) \in A : i \in S , j \notin S \right\}$ and $\delta ^ { - } ( S ) = \left\{ ( i , j ) \in A \right.$ $i \notin S , j \in S \}$ . For the ease of presentation, in the following we will use the notation $\delta ^ { + } ( i )$ and $\delta ^ { - } ( i )$ when $S = \{ i \}$ . The decision variables are the following:

• y<sub>i</sub> = binary variable equal to 1 if vertex i ∈ V is visited by the vehicle, and 0 otherwise,

$x _ { i j } =$ binary variable equal to 1 if arc $( i , j )   \in   A$ is traversed by the vehicle, and 0 otherwise,

$z _ { g } = \mathrm { b i n a r y }$ variable equal to 1 if the profit of cluster $C _ { g }$ is collected and 0 otherwise.

The mathematical programming formulation of the SOP is the following:

$$
\max \sum_ {j \in \mathcal {P}} p _ {g} z _ {g}\tag{1}
$$

$$
\text {s.t.} \quad \sum_ {(i, j) \in \delta^ {+} (i)} x _ {i j} = y _ {i} \quad i \in V,\tag{2}
$$

$$
\sum_ {(j, i) \in \delta^ {-} (i)} x _ {j i} = y _ {i} \quad i \in V,\tag{3}
$$

$$
\sum_ {(i, j) \in \delta^ {+} (S)} x _ {i j} \geq y _ {h} \quad S \subseteq V \setminus \{0 \}, h \in S,\tag{4}
$$

$$
\sum_ {(i, j) \in A} c _ {i j} x _ {i j} \leq T _ {\max},\tag{5}
$$

$$
z _ {g} \leq \sum_ {i \in C _ {g}} y _ {i} \quad C _ {g} \in \mathcal {P},\tag{6}
$$

$$
y _ {i} \in \{0, 1 \} \quad i \in V,\tag{7}
$$

$$
z _ {g} \in \{0, 1 \} \quad C _ {g} \in \mathcal {P},\tag{8}
$$

$$
x _ {i j} \in \{0, 1 \} \quad (i, j) \in A.\tag{9}
$$

The objective function (1) maximizes the collected profit. Constraints (2) and (3) ensure that one arc enters and one arc leaves each visited vertex. Subtours are eliminated through (4). Constraint (5) is the maximum duration constraint on the route while (6) imposes that the profit of cluster $C _ { g }$ is collected only if at least one customer $i   \in   C _ { g }$ is visited in the tour. Finally, $( 7 )  –  ( 9 )$ are variable definitions.

Note that formulation (1)–(9) has an exponential number of subtour elimination constraints (4). A formulation with a polynomial number of constraints is obtained by introducing arc flow variables $u _ { i j } ,$ representing the amount of flow crossing the edge (i, $j ) ,$ and substituting (4) with the following constraints:

$$
\sum_ {j \in V} u _ {j i} - \sum_ {j \in V} u _ {i j} = y _ {i} \quad i \in V \backslash \{0 \},\tag{10}
$$

$$
u _ {i j} \leq (n - 1) x _ {i j} (i, j) \in A,\tag{11}
$$

$$
y _ {0} = 1\tag{12}
$$

$$
u _ {i j} \geq 0 (i, j) \in A,\tag{13}
$$

where $n = | V |$ . We note that this formulation of subtour elimination constraints has been proposed in Gavish and Graves (1978) for the Traveling Salesman Problem (TSP) and its performance has been recently assessed in Öncan, Altinel, and Laporte (2009).

## 3. A matheuristic for the SOP

In this section, we describe the heuristic algorithm we have designed for the solution of the SOP. It is a matheuristic algorithm which is composed by the following two phases:

1. Phase 1: construction of an initial solution.

2. Phase 2: Tabu search.

It is a matheuristic algorithm as the tabu search makes use of a MILP formulation when it struggles in finding a new non-tabu feasible solution. In the following we refer to the algorithm as MASOP – a MAtheuristic for the SOP.

We now describe in details the two phases. We define the following notation. Given a tour T, we denote as $C ( T ) \subseteq { \mathcal { P } }$ the set of clusters visited in T, i.e., the set of clusters for which at least one vertex is visited in T, while $p ( T )$ and $c ( T )$ are the profit and the cost associated with T, respectively. T is a feasible tour if and only if $c ( T )   \leq   T _ { m a x } .$ Moreover, given a vertex $i   \in   V \{ 0 \}$ , let C(i) be the cluster to which i belongs. On the other hand, given a cluster $C _ { g } ,$ let $V ( C _ { g } )$ be the set of all vertices belonging to $C _ { g } .$

## 3.1. Phase 1: construction of an initial solution

MASOP constructs an initial feasible solution through a simple greedy algorithm which inserts clusters in the tour as long as this is feasible. In particular, it starts with a path T visiting vertex 0 only. Let u be the last vertex visited in T and let $C _ { f }$ be the cluster in ${ \mathcal { P } } \backslash C ( T )$ with the highest profit, $\mathrm { i . e . , } C _ { f } = a r g m a x _ { C _ { g } \in \mathcal { P } \backslash C ( T ) } \{ p _ { g } \}$ . Then, the procedure attaches at the end of T the vertex v ∈ $C _ { f }$ such that $c _ { u v } + c _ { v 0 }$ is minimum, if $c ( T ) + c _ { u v } + c _ { v 0 } \leq T _ { m a x } .$ If no such vertex exists, the procedure considers the cluster with the second highest profit and iterates. If no vertex can be feasibly inserted in T, the procedure stops and u is linked with 0. This way, T becomes a tour.

Once a feasible solution is constructed as described above, before starting Phase 2, MASOP applies the following procedure which is aimed at improving the cost associated with tour T. The idea is to maintain the same set C(T) of clusters visited, and thus the same associated profit p(T), while reducing cost c(T). The procedure consists of two steps.

In the first step, the procedure determines, for each cluster of C(T), which vertex has to be visited in order to obtain the minimum cost tour provided that the clusters in C(T) are visited according to the sequence defined in T. This problem can be solved in polynomial time by solving a shortest path problem as shown in Hu and Raidl (2008), Pop, Matei, and Sabo (2010), Coutinho, do Nascimento, Pessoa, and Subramanian (2016). Note that the problem can be solved as a shortest path thanks to the fact that the triangle inequality holds, as shown in Hu and Raidl (2008). Once the first step is terminated, we apply the second step which aims at optimizing the sequence of visiting the vertices included in T. In particular, let V(T) be the set of vertices visited in T. The second step consists in applying the Lin–Kernighan algorithm (Lin & Kernighan, 1973) for the solution of the Traveling Saleman Problem to the set V(T). The procedure iterates between the first and the second step as long as an improvement is found. The sketch of the procedure is shown in Algorithm 1. We call the procedure Tour Improvement.

<div class="docvortex-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Algorithm 1 Tour Improvement.
Input: Tour $T$.
Output: Tour $T_{best}$.
$T_{best} \leftarrow T$.
$T \leftarrow$ Solve Shortest Path ($T$).
$T \leftarrow$ Solve Lin–Kernighan ($V(T)$).
if ($c(T_{best}) &gt; c(T)$)
    $T_{best} \leftarrow T$. Return to 4.
else
    STOP.
Return $T_{best}$.
</div>

## 3.2. Phase 2: Tabu search

Phase 2 aims at improving the initial solution constructed in Phase 1 through a tabu search which is composed by the following procedures:

• ExploreNeighborhood(T, TL): this procedure explores the neighborhood of the solution represented by T on the basis of the tabu list TL and is explained in Section 3.2.1.

• MIPMove(T ): this function explores a different neighborhood which is based on the solution of a MILP. No tabu list is considered. It is called when function ExploreNeighborhood(T, TL) does not find any feasible non-tabu solution. MIPMove(T ) is described in Section 3.2.2.

• Shake(T): this is a diversification procedure which destroys the current solution T by removing a number of clusters visited in T at random. It is described in Section 3.2.3. It uses two operators: SoftShake(T) and HardShake(T).

A sketch of the tabu search algorithm is provided in Algorithm 2.

<div class="docvortex-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Algorithm 2 Tabu search.
Input: Tour $T.$ Provided by Phase 1
Output: Tour $T_{best}$.
$T_{best} \leftarrow T$.
numIterations $\leftarrow 0$; MIPInvocable $\leftarrow$ true.
while numIterations $\leq$ maxIterations do
    numIterations + +.
    ShakeInvocable $\leftarrow$ true.
    $T' \leftarrow$ ExploreNeighborhood($T, TL$).
    if $T' \neq null$ then
        if $p(T') &gt; p(T)$ then
            numIterations --.
        end if
        $T \leftarrow T'$.
        Update $TL$.
        MIPInvocable $\leftarrow$ true.
        if numIterations%$\alpha = 0$ then
            $T \leftarrow$ Tour Improvement ($T$).
        end if
        if $p(T) &gt; p(T_{best})$ then
            $T_{best} \leftarrow$ Tour Improvement ($T$).
            numIterations $\leftarrow 0$.
        end if
    else
        if (MIPInvocable = true) then
            $T' \leftarrow$ MIPMove($T$).
            if $p(T') &gt; p(T)$ then
                $T \leftarrow T'$.
                ShakeInvocable $\leftarrow$ false; MIPInvocable $\leftarrow$ false.
                if $p(T') &gt; p(T_{best})$ then
                    $T_{best} \leftarrow$ Tour Improvement ($T'$).
                    numIterations $\leftarrow 0$.
                end if
            end if
        end if
        if (ShakeInvocable = true) then
            MIPInvocable $\leftarrow$ true.
            if $p(T) \geq p(T_{best}) - \beta * p(T_{best})$ then
                $T \leftarrow$ SoftShake($T$).
            else
                $T \leftarrow$ HardShake($T$).
            end if
        end if
    end if
end while
Return $T_{best}$.
</div>

The tabu search is started with the initial feasible solution provided by Phase 1 (line 1). The main loop of the algorithm is in lines 5–44. The algorithm continues until a maximum number of iterations without improvement is reached (line 5). The counter of iterations without improvement is set to 0 any time a new best solution is found (lines 21 and 31) and is decreased by 1 any time the new solution improves the current one (line 11).

The main loop works as follows. First, the ExploreNeighborhood(T, TL) procedure is called (line 8). If it succeeds in finding a non-tabu feasible solution, then the move is implemented (line 13) and the tabu list is updated (line 14). The neighborhood is entirely explored and the best move is implemented. In addition, every α iterations the Tour Improvement procedure (Algorithm 1) is applied to the current tour T (line $1 7 ) .$ If ExploreNeighborhood(T, TL) fails in finding a new non-tabu feasible solution, then MIPMove(T ) is invoked (line 25) only if MIPInvocable = true. MIPInvocable is a binary variable that checks whether the MIPMove(T ) procedure has already been applied to the current tour T (in this case MIPInvocabl $e = f a l s e )$ or not (MIPInvocable = true). A similar role has variable ShakeInvocable for the Shake(T) function. If MIPMove(T ) improves the current solution, then both MIPInvocable and ShakeInvocable are set to false as the idea is to first direct the search to the improvement of the new solution just found (line 28). Finally, there is the shaking phase which is invoked only if ShakeInvocable = true, i.e., when ExploreNeighborhood(T, TL) fails in finding a new non-tabu solution and MIPMove(T ) does not improve the current solution. Then, if the profit of the current tour T is not lower than $\beta$ times the profit of the best tour, SoftShake(T) is applied. Otherwise, the algorithm applies HardShake(T) (line 37).

We now explain the three main procedures ExploreNeighborhood(T, TL), MIPMove(T ) and Shake(T) in detail.

## 3.2.1. Procedure ExploreNeighborhood(T, TL)

Given the current solution represented by tour T, the neighborhood of T, which we call N(T), is defined by the following moves:

• Insert. For all clusters $C _ { g } \in { \mathcal { P } } { \backslash } C ( T )$ , the operator evaluates the insertion of $C _ { g }$ in T. The insertion works as follows. Let $<$ $v _ { 1 } , \ldots , v _ { k } >$ be the sequence of vertices visited in T, where $\begin{array} { r } { v _ { 1 } = v _ { k } = 0 . } \end{array}$ Starting from $\nu _ { 1 }$ the operator determines the vertex $i \in C _ { \mathtt { g } }$ for which $c _ { v _ { 1 } i } + c _ { i v _ { 2 } }$ is minimum. The insertion is evaluated for all insertion points, i.e., for all $\nu _ { j }$ with $j = 1 , \ldots , k$ − 1 and the best one is retained only if it leads to a new cost not greater than $T _ { m a x }$

• Swap. For each pair of clusters $C _ { g } \in { \mathcal { P } } \setminus C ( T )$ and $C _ { h }   \in   \mathsf { C } ( T ) ,$ the operator evaluates the exchange of them, i.e., inserting $C _ { g }$ in T and removing $C _ { h } .$ The procedure is done by first evaluating the removal of $C _ { h }$ and then evaluating the insertion of $C _ { g }$ as done by the operator Insert. The removal of $C _ { h }$ is done by simply joining the predecessor of the vertex in $C _ { h }$ visited in T with its successor.

An iteration of the tabu search consists in evaluating all the neighbor solutions in N(T). Infeasible solutions are discarded and the best non-tabu solution is chosen as the new solution, thus becoming the current solution at the next iteration. Solutions are evaluated through a hierarchical objective function where the first objective consists of the profit associated with the solution and the second is the associated cost. Thus, the best solution in terms of total profit is chosen. In case of ties, the solution with the lowest cost is chosen.

The tabu list is defined as follows. When a cluster is removed (inserted) from the current solution T, then it is tabu to reinsert (remove) it for a number of iterations equal to

## rand(lλ)

(14)

where rand(lλ) is a function that returns a random integer number in $( 0 , \; \lceil l \lambda \rceil ] , \; l = | \mathcal { P } |$ and λ is a positive parameter. Moreover, each time a new best solution is found, procedure Tour Improvement is called to reduce the cost c(T). Tour Improvement is also called every α iterations of the tabu search and applied on the current solution, independently of the fact that this is a new best solution or not.

## 3.2.2. Procedure MIPMove(T )

MIPMove(T ) is called if ExploreNeighborhood(T, TL) fails in finding a new feasible non-tabu solution. The idea is to apply a move with a broader range of possible changes to the current solution T and, thus, a higher probability of finding a new feasible solution. No tabu list is considered. It works as follows.

First, a set of clusters visited in T is removed from T. The number $\delta$ of removed clusters is chosen randomly in [5%|T|; 15%|T|]. This interval gives the possibility of exploring a larger neighborhood than ExploreNeighborhood(T, TL) without destroying the current solution T. In order to choose the clusters to be removed, clusters in T are ordered on the basis of a non-decreasing value of the ratio

$$
\left| p _ {g} \right|
$$

$$
r s _ {g}
$$

where $r s _ { g }$ is the removal saving obtained by removing the vertex $\pmb { \nu } \in \mathsf { C } _ { \mathtt { S } } \cap T$ from T (i.e., joining its predecessor with its successor). If $r s _ { \mathrm { g } } = 0$ then we fix it to 1. This last situation occurs when $\nu \in C _ { \mathtt { g } }$ is on the segment connecting its predecessor and its successor in T. The subset composed by the first $\delta ^ { * } 1 . 5$ clusters of the ordered list is considered and then δ clusters are chosen randomly from this subset. This way, a tour T on the remaining clusters is found. By multiplying the parameter δ by 1.5, we avoid to always select the first δ clusters from the sorted list and we introduce randomness in this selection.

Then, a MILP is solved to insert non-visited clusters in $T .$ Let us define $D = \mathcal { P } \backslash C ( T ^ { \prime } )$ as the set of clusters not visited in $T ^ { \prime }$ and  be the set of all subsets of D composed by one or two clusters. Moreover, let < $v _ { 1 } , \ldots , v _ { k } >$ be the sequence of vertices visited in $T ,$ with $\begin{array} { r } { \nu _ { 1 } = \nu _ { k } = 0 . } \end{array}$ . For each set $\gamma \in \Gamma$ , we compute the cost of inserting γ between $\nu _ { i }$ and $v _ { i + 1 } ,   i = 1 , \ldots , k - 1$ , which we denote $\Delta _ { \gamma i \cdot }$ Cost $\Delta _ { \gamma i }$ is computed as follows. In case γ is formed by a single cluster $C _ { g } ,$ then $\Delta _ { \gamma i }$ corresponds to the length of the shortest path visiting, in sequence, $\nu _ { i }   -   { \mathfrak { a } }$ vertex in $C _ { g }   -   v _ { i + 1 }$ . In case $\gamma$ is formed by two clusters $C _ { g }$ and $C _ { h } ,$ then $\Delta _ { \gamma i }$ corresponds to the minimum between the length of the shortest paths $\nu _ { i } - \mathfrak { a }$ vertex in $C _ { g } \mathrm { ~ - ~ } \mathbf { a }$ vertex in $C _ { h } \mathrm { ~ - ~ } \nu _ { i + 1 }$ and $\nu _ { i } \mathrm { - ~ } \mathfrak { a }$ vertex in $C _ { h }   -   { \tt d }$ vertex in $C _ { \mathrm { g } } \mathrm { ~ - ~ }$ $\nu _ { i + 1 }$ . Note that we do not consider subsets of clusters of cardinality greater than 2 as this would be computationally too expensive. Finally, let $a _ { \gamma g } = 1$ if set $\gamma \in \Gamma$ contains cluster $C _ { g }   \in   D ,$ 0 otherwise. The following MILP is then solved:

$$
\left| \max \sum_ {\gamma \in \Gamma} \sum_ {i = 1} ^ {k - 1} p (\gamma) w _ {\gamma i} \right|\tag{15}
$$

$$
\text {s.t.} \sum_ {\gamma \in \Gamma} \sum_ {i = 1} ^ {k - 1} a _ {\gamma g} w _ {\gamma i} \leq 1 \quad C _ {g} \in D,\tag{16}
$$

$$
\sum_ {\gamma \in \Gamma} w _ {\gamma i} \leq 1 \quad i = 1, \dots , k - 1,\tag{17}
$$

$$
\left| c (T ^ {\prime}) + \sum_ {\gamma \in \Gamma} \sum_ {i = 1} ^ {k - 1} \Delta_ {\gamma i} w _ {\gamma i} \leq T _ {m a x}, \right.\tag{18}
$$

$$
w _ {\gamma i} \in \{0, 1 \} \quad \quad \gamma \in \Gamma , \quad k = 1, \dots , k - 1\tag{19}
$$

where $w _ { \gamma i }$ is a binary variable which takes value 1 if set γ is inserted after vertex $v _ { i } ,$ 0 otherwise. The objective function (15) aims at maximizing the profit of the clusters inserted. Constraints (16) state that each cluster can be inserted at most once while (17) establish that at most one element from  can be inserted between two consecutive vertices $\nu _ { i }$ and $\nu _ { i + 1 }$ . Finally, (18) is the maximum duration constraint.

The solution of (15)–(19) provides a new tour $T ^ { \prime \prime } .$ If $p ( T ^ { \prime \prime } )   >   p ( T )$ then the procedure is iterated. A sketch of MIPMove(T ) is provided in Algorithm 3.

<div class="docvortex-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Algorithm 3 MIPMove(T).
Input: Tour $T$.
Output: Tour $T''$.
$T' \leftarrow$ remove $\delta$ clusters from $T$.
$T'' \leftarrow$ solve (15)-(19) on $T'$.
if $p(T'') &gt; p(T)$ then
    $T \leftarrow$ Tour Improvement ($T''$).
    Return to line 3.
end if
Return $T$.
</div>

3.2.3. Procedure Shake(T)

Shake(T) aims at destroying the current solution and directing the search to a different part of the solution space. It removes at random a certain number of clusters from T. The only difference between SoftShake(T) and HardShake(T) is the number of clusters removed. In particular, in SoftShake(T) this number is chosen randomly in [5%|T|, 15%|T|] while in HardShake(T) it is in [30%|T|, 40%|T|].

## 4. Computational tests

In this section, we present the computational results of the tests we made in order to evaluate the performance of MASOP. The algorithm was coded in C++ on an OSX platform (Imac late 2012), running on an Intel Core i7 2.8 GHz processor with 16 GB of RAM. The mathematical formulations were solved using the ILOG Concert Technology library and CPLEX 12.6.

In the following section, we describe how we generated the instances for the SOP while computational results are illustrated in Section 4.2.

## 4.1. Test instances

As the SOP has not been studied previously in the literature, no benchmark instances exist. Thus, we generated them by adapting instances for the Generalized Traveling Salesman Problem (GTSP) proposed in Fischetti, Salazar Gonzàlez, and Toth (1997). The GTSP is the problem where customers are divided in cluster and the objective is to find the shortest cycle visiting at least one customer per cycle. In particular, among all instances proposed in Fischetti et al. (1997), we select the instances for which the distance is defined as the Euclidean distance between customers’ coordinates. These instances have a number of vertices ranging from 52 to 1084 and a number of clusters equal to ∼ 20% of the number of vertices. They are 51 in total. Concerning the number of customers, we classify the instances in two groups: small instances with up to 198 customers and large instances with at least 200 customers. We adapted these instances to the SOP as follows. We maintain the data related to customers locations. As no depot is defined in the GTSP, we defined the depot as follows. We took the first node in the node list and set it to be the depot. Thus, we removed it from the cluster it was inserted into in the GTSP instance and we inserted it in cluster 0 which contains the depot only. Then, we needed to generate the profits $p _ { g }$ for $C _ { g } \in \mathcal { P }$ and $T _ { m a x } .$ We generated them as follows.

$p _ { g } ;$ we used two rules. The first rule sets the profit of each cluster $C _ { g }$ equal to $| C _ { g } | .$ The second rule sets the profit of a node j equal to $1 + ( 7 1 4 1 j + 7 3 ) m o d ( 1 0 0 )$ in order to obtain pseudorandom profits. The profit of a cluster in then obtained by summing up the profit of all the nodes belonging to it. The same rules are used in Angelelli et al. (2014) for the clustered OP. In the following we call $g _ { 1 }$ the first rule and $g _ { 2 }$ the second rule.

$T _ { m a x } ;$ we set it to ωGTSP∗ where $G T S P ^ { * }$ is the cost of the best known solution value of the GTSP (taken from Fischetti et al., 1997) and ω has been set to 0.4, 0.6, 0.8.

Thus, in total we had 306 instances which form the Set 1 instances. In addition, we generated a second set of instances, which we called Set 2, starting from the same instances and following the same procedure described above. However, we changed the clusters defined in the GTSP instances as follows. We maintain the same number of clusters defined in the GTSP instances and assigned the customers at random to clusters. The value of $G T S P ^ { * }$ is not available for these new instances so we kept the one used for instances of Set 1.

## 4.2. Computational results

We performed preliminary tests, by considering all the instances of Set 1, in order to fine-tune the parameters used in MA-SOP. The resulting values are the following:

• MaxIterations = 500: it corresponds to the maximum number of iterations without improvement. It determines the stopping condition of the tabu search.

$\lambda = 0 .$ 1: it determines the tabu length.

• α = 5: it is related to the frequency of applying the Tour Improvement procedure.

• β = 8%: it establishes whether SoftShake(T) or HardShake(T) is applied.

We now present the results of our tests. In the following, all computing times are expressed in seconds. We made two kind of experiments. The first one is aimed at verifying the efficacy of MA-SOP by comparing the value of the solutions it provides with the optimal solutions obtained (i) by solving the mathematical formulation for the SOP presented in Section 2 and (ii) by considering the special case when ω = 1 for which the value of the optimal solution corresponds to the sum of the profit of all clusters. Regarding the mathematical formulation, we used inequalities (10)– (13) to model subtour elimination constraints. The formulation was solved through CPLEX 12.6. The maximum CPU time was set to 9 hours. Only small size instances were tested as no optimal solutions is obtained for larger ones.

Results are shown in Tables 1 and 2. In Table 1, the first block of rows is related to instances of Set 1 while the second block is related to instances of Set 2. The table is organized as follows. The first four columns report data on the instances: the name of the instance, the total number of vertices (n), the value of ω and the kind of profit. The following two columns refer to the computation of the optimal solution: value of the optimal solution and the computational time taken by CPLEX to compute it. Finally, the last three columns are related to MASOP solutions: solution value, computational time and percentage gap with respect to the optimal solution. From Table 1 it is possible to notice that MASOP always finds the optimal solution of Set 1 instances while it fails to find the optimal solution on three instances of Set 2 with a maximum gap of 8.11%. The computational time spent by MASOP to solve these instances is always lower than 15 seconds.

To further investigate the effectiveness of MASOP on large instances too, we carried out computational tests on Set 1 instances by using $\omega = 1$ , i.e. $T _ { m a x }$ is equal to the cost of the best known GTSP solution. This means that there is at least a tour that can visit all the clusters without violating the threshold $T _ { m a x }$ and then the optimal profit coincides with the sum of the profits of all the clusters. In other words, we apply MASOP to solve the GTSP. Obviously we do not expect to obtain results equal to the specific metaheuristics created “ad hoc” for this problem but the gap between the optimal solution values and the ones found by MASOP allow us to have an idea about the effectiveness of our algorithm even on large instances.

Comparison with optimal solutions on small instances with ω < 1.

<table><tr><td rowspan="2"></td><td rowspan="2">Instance</td><td rowspan="2">n</td><td rowspan="2"> $\omega$ </td><td rowspan="2"> $p_g$ </td><td colspan="2">MIP</td><td colspan="2">MASOP</td><td rowspan="2">Gap (%)</td></tr><tr><td>Opt</td><td>Time</td><td>Sol</td><td>Time</td></tr><tr><td rowspan="20">Set 1</td><td>11berlin52</td><td>52</td><td>0.4</td><td> $g_1$ </td><td>37</td><td>47.07</td><td>37</td><td>1.75</td><td>0.00</td></tr><tr><td>11berlin52</td><td>52</td><td>0.4</td><td> $g_2$ </td><td>1829</td><td>65.96</td><td>1829</td><td>1.70</td><td>0.00</td></tr><tr><td>11berlin52</td><td>52</td><td>0.6</td><td> $g_1$ </td><td>43</td><td>777.88</td><td>43</td><td>2.40</td><td>0.00</td></tr><tr><td>11berlin52</td><td>52</td><td>0.6</td><td> $g_2$ </td><td>2190</td><td>1532.91</td><td>2190</td><td>2.64</td><td>0.00</td></tr><tr><td>11berlin52</td><td>52</td><td>0.8</td><td> $g_1$ </td><td>47</td><td>2648.04</td><td>47</td><td>7.17</td><td>0.00</td></tr><tr><td>11berlin52</td><td>52</td><td>0.8</td><td> $g_2$ </td><td>2384</td><td>3833.50</td><td>2384</td><td>6.61</td><td>0.00</td></tr><tr><td>11eil51</td><td>51</td><td>0.4</td><td> $g_1$ </td><td>24</td><td>39.72</td><td>24</td><td>1.85</td><td>0.00</td></tr><tr><td>11eil51</td><td>51</td><td>0.4</td><td> $g_2$ </td><td>1279</td><td>40.13</td><td>1279</td><td>1.97</td><td>0.00</td></tr><tr><td>11eil51</td><td>51</td><td>0.6</td><td> $g_1$ </td><td>39</td><td>34.64</td><td>39</td><td>5.13</td><td>0.00</td></tr><tr><td>11eil51</td><td>51</td><td>0.6</td><td> $g_2$ </td><td>1911</td><td>204.65</td><td>1911</td><td>4.74</td><td>0.00</td></tr><tr><td>11eil51</td><td>51</td><td>0.8</td><td> $g_1$ </td><td>43</td><td>1586.67</td><td>43</td><td>2.30</td><td>0.00</td></tr><tr><td>11eil51</td><td>51</td><td>0.8</td><td> $g_2$ </td><td>2114</td><td>1520.67</td><td>2114</td><td>1.93</td><td>0.00</td></tr><tr><td>14st70</td><td>70</td><td>0.4</td><td> $g_1$ </td><td>33</td><td>9666.29</td><td>33</td><td>4.43</td><td>0.00</td></tr><tr><td>14st70</td><td>70</td><td>0.4</td><td> $g_2$ </td><td>1672</td><td>4396.77</td><td>1672</td><td>4.35</td><td>0.00</td></tr><tr><td>14st70</td><td>70</td><td>0.8</td><td> $g_1$ </td><td>65</td><td>18227.23</td><td>65</td><td>8.80</td><td>0.00</td></tr><tr><td>14st70</td><td>70</td><td>0.8</td><td> $g_2$ </td><td>3355</td><td>30851.18</td><td>3355</td><td>7.89</td><td>0.00</td></tr><tr><td>16eil76</td><td>76</td><td>0.4</td><td> $g_1$ </td><td>40</td><td>4987.09</td><td>40</td><td>3.88</td><td>0.00</td></tr><tr><td>16eil76</td><td>76</td><td>0.4</td><td> $g_2$ </td><td>2223</td><td>4939.08</td><td>2223</td><td>4.73</td><td>0.00</td></tr><tr><td>16eil76</td><td>76</td><td>0.6</td><td> $g_1$ </td><td>59</td><td>29565.85</td><td>59</td><td>2.40</td><td>0.00</td></tr><tr><td>16eil76</td><td>76</td><td>0.6</td><td> $g_2$ </td><td>3119</td><td>21127.41</td><td>3119</td><td>6.28</td><td>0.00</td></tr><tr><td rowspan="22">Set 2</td><td>11berlin52_RND</td><td>52</td><td>0.4</td><td> $g_1$ </td><td>50</td><td>43.20</td><td>50</td><td>6.33</td><td>0.00</td></tr><tr><td>11berlin52_RND</td><td>52</td><td>0.4</td><td> $g_2$ </td><td>2584</td><td>60.84</td><td>2584</td><td>6.11</td><td>0.00</td></tr><tr><td>11berlin52_RND</td><td>52</td><td>0.6</td><td> $g_1$ </td><td>51</td><td>1.52</td><td>51</td><td>6.73</td><td>0.00</td></tr><tr><td>11berlin52_RND</td><td>52</td><td>0.6</td><td> $g_2$ </td><td>2608</td><td>1.14</td><td>2608</td><td>6.63</td><td>0.00</td></tr><tr><td>11eil51_RND</td><td>51</td><td>0.4</td><td> $g_1$ </td><td>37</td><td>9.12</td><td>34</td><td>0.82</td><td>8.11</td></tr><tr><td>11eil51_RND</td><td>51</td><td>0.4</td><td> $g_2$ </td><td>1929</td><td>7.44</td><td>1929</td><td>1.30</td><td>0.00</td></tr><tr><td>11eil51_RND</td><td>51</td><td>0.6</td><td> $g_1$ </td><td>50</td><td>6.28</td><td>50</td><td>5.27</td><td>0.00</td></tr><tr><td>11eil51_RND</td><td>51</td><td>0.6</td><td> $g_2$ </td><td>2575</td><td>54.73</td><td>2575</td><td>5.25</td><td>0.00</td></tr><tr><td>14st70_RND</td><td>70</td><td>0.4</td><td> $g_1$ </td><td>56</td><td>5316.83</td><td>56</td><td>5.60</td><td>0.00</td></tr><tr><td>16eil76_RND</td><td>76</td><td>0.4</td><td> $g_1$ </td><td>51</td><td>2498.79</td><td>51</td><td>4.00</td><td>0.00</td></tr><tr><td>16eil76_RND</td><td>76</td><td>0.6</td><td> $g_1$ </td><td>74</td><td>993.13</td><td>69</td><td>0.86</td><td>6.76</td></tr><tr><td>16eil76_RND</td><td>76</td><td>0.6</td><td> $g_2$ </td><td>3728</td><td>1737.65</td><td>3713</td><td>5.76</td><td>0.40</td></tr><tr><td>16pr76_RND</td><td>76</td><td>0.4</td><td> $g_1$ </td><td>70</td><td>6536.81</td><td>70</td><td>3.09</td><td>0.00</td></tr><tr><td>16pr76_RND</td><td>76</td><td>0.4</td><td> $g_2$ </td><td>3550</td><td>5806.05</td><td>3550</td><td>7.39</td><td>0.00</td></tr><tr><td>16pr76_RND</td><td>76</td><td>0.6</td><td> $g_1$ </td><td>74</td><td>1370.58</td><td>74</td><td>12.57</td><td>0.00</td></tr><tr><td>20kroE100_RND</td><td>100</td><td>0.4</td><td> $g_2$ </td><td>4614</td><td>7865.33</td><td>4614</td><td>8.83</td><td>0.00</td></tr><tr><td>20rat99_RND</td><td>99</td><td>0.4</td><td> $g_1$ </td><td>73</td><td>3103.25</td><td>73</td><td>2.34</td><td>0.00</td></tr><tr><td>20rat99_RND</td><td>99</td><td>0.4</td><td> $g_2$ </td><td>3624</td><td>4408.47</td><td>3624</td><td>2.15</td><td>0.00</td></tr><tr><td>21lin105_RND</td><td>105</td><td>0.6</td><td> $g_1$ </td><td>104</td><td>2085.34</td><td>104</td><td>11.11</td><td>0.00</td></tr><tr><td>21lin105_RND</td><td>105</td><td>0.6</td><td> $g_2$ </td><td>5228</td><td>2034.79</td><td>5228</td><td>11.85</td><td>0.00</td></tr><tr><td>22pr107_RND</td><td>107</td><td>0.6</td><td> $g_1$ </td><td>106</td><td>1021.05</td><td>106</td><td>12.53</td><td>0.00</td></tr><tr><td>22pr107_RND</td><td>107</td><td>0.6</td><td> $g_2$ </td><td>5363</td><td>2145.44</td><td>5363</td><td>11.89</td><td>0.00</td></tr></table>

Results are shown in Table 2 where the first block of rows is related to the small instances while the second block is related to the large instances. The first two columns report the name of the instance and the total number of vertices. The next 8 columns are divided in two blocks, related to the profit rules g<sub>1</sub> and g<sub>2</sub>, reporting: the optimal solution value (Opt), the MASOP solution value (Sol), MASOP computational time (Time) and percentage gap with respect to the optimal solution (Gap). On small instances with profit g<sub>1</sub>, the percentage gap is lower than 3% on 19 out of 27 instances while the peak is equal to 5.1% and occurs on the instance 20rat99. Anyway, this is the only case for which the gap is higher than 5% while the average gap is equal to 2.15%. Surprisingly, the results are much better on the large instances. Indeed, the gap is always lower than 3% and the peak is equal to 2.23% (45tsp225). It is worth noting that, in these instances, the gap is lower than 1% on 17 out of 24 times and that the average gap is 0.81%. In our opinion, this situation occurs because on the large instances it is more difficult to find an optimal solution for the Generalized TSP and then the best known solution, provided in literature for these instances, is not the optimal one. For this reason, the value of T<sub>max</sub> is less restrictive on the large instances with respect to the small instances. As a consequence, the operators of MASOP are more effective thanks to the less binding duration constraint imposed during the construction or the modification of the tour.

We observed a similar behavior on the instances with profit type g<sub>2</sub>. In particular, on the small instances, the percentage gap is lower than 3% on 21 out of 27 instances while the gap is higher than 5% only in two cases with a peak equal to 5.79% on instance 11eil51. Again, better results are obtained by MASOP on the large instances where the gap is always lower than 2% and in 18 out of 24 cases it is lower than 1%. The peak is equal to 1.85% and occurs on instance 115rat575 and the average gap is equal to 0.59%.

Regarding the computational time, MASOP solves the small instances in less than 37 seconds with an average time equal to around 12 seconds for both profit rules g<sub>1</sub> and g<sub>2</sub>. On large instances, the computational time significantly increases with an average time equal to 154 seconds for $g _ { 1 }$ and 182 seconds for g<sub>2</sub>. Moreover, we observed a peak equal to 837 and 992 seconds for g<sub>1</sub> and g<sub>2</sub>, respectively.

According to the results reported in Tables 1 and 2, we can conclude that MASOP provides robust and reliable results related to high quality solutions. Finally, we did not carry out the computational tests with ω = 1 for the Set 2 because MASOP found solutions where all the clusters are visited in 100 out of 102 instances with ω = 0.8.

Table 2

Comparison with optimal solutions on small and large instances with ω = 1.

<table><tr><td rowspan="3"></td><td rowspan="3">Instance</td><td rowspan="3">n</td><td colspan="4"> $g_1$ </td><td colspan="4"> $g_2$ </td></tr><tr><td rowspan="2">Opt</td><td colspan="2">MASOP</td><td rowspan="2">Gap (%)</td><td rowspan="2">Opt</td><td colspan="2">MASOP</td><td rowspan="2">Gap (%)</td></tr><tr><td>Sol</td><td>Time</td><td>Sol</td><td>Time</td></tr><tr><td rowspan="27"></td><td>11berlin52</td><td>52</td><td>51</td><td>50</td><td>8.54</td><td>1.96</td><td>2608</td><td>2580</td><td>8.54</td><td>1.07</td></tr><tr><td>11eil51</td><td>51</td><td>50</td><td>48</td><td>7.03</td><td>4.00</td><td>2575</td><td>2426</td><td>6.93</td><td>5.79</td></tr><tr><td>14st70</td><td>70</td><td>69</td><td>68</td><td>8.02</td><td>1.45</td><td>3513</td><td>3488</td><td>8.25</td><td>0.71</td></tr><tr><td>16eil76</td><td>76</td><td>75</td><td>74</td><td>8.17</td><td>1.33</td><td>3800</td><td>3780</td><td>8.23</td><td>0.53</td></tr><tr><td>16pr76</td><td>76</td><td>75</td><td>74</td><td>8.57</td><td>1.33</td><td>3800</td><td>3765</td><td>10.58</td><td>0.92</td></tr><tr><td>20kroA100</td><td>100</td><td>99</td><td>96</td><td>10.53</td><td>3.03</td><td>5008</td><td>4868</td><td>11.48</td><td>2.80</td></tr><tr><td>20kroB100</td><td>100</td><td>99</td><td>98</td><td>13.40</td><td>1.01</td><td>5008</td><td>4916</td><td>10.73</td><td>1.84</td></tr><tr><td>20kroC100</td><td>100</td><td>99</td><td>97</td><td>10.80</td><td>2.02</td><td>5008</td><td>4882</td><td>11.23</td><td>2.52</td></tr><tr><td>20kroD100</td><td>100</td><td>99</td><td>96</td><td>10.30</td><td>3.03</td><td>5008</td><td>4838</td><td>8.86</td><td>3.39</td></tr><tr><td>20kroE100</td><td>100</td><td>99</td><td>96</td><td>9.14</td><td>3.03</td><td>5008</td><td>4887</td><td>9.95</td><td>2.42</td></tr><tr><td>20rat99</td><td>99</td><td>98</td><td>93</td><td>7.57</td><td>5.10</td><td>5007</td><td>4721</td><td>8.09</td><td>5.71</td></tr><tr><td>20rd100</td><td>100</td><td>99</td><td>97</td><td>10.38</td><td>2.02</td><td>5008</td><td>4929</td><td>9.60</td><td>1.58</td></tr><tr><td>21eil101</td><td>101</td><td>100</td><td>97</td><td>8.81</td><td>3.00</td><td>5050</td><td>4953</td><td>20.10</td><td>1.92</td></tr><tr><td>21lin105</td><td>105</td><td>104</td><td>102</td><td>8.05</td><td>1.92</td><td>5228</td><td>5157</td><td>8.38</td><td>1.36</td></tr><tr><td>22pr107</td><td>107</td><td>106</td><td>101</td><td>8.62</td><td>4.72</td><td>5363</td><td>5109</td><td>8.28</td><td>4.74</td></tr><tr><td>25pr124</td><td>124</td><td>123</td><td>121</td><td>11.30</td><td>1.63</td><td>6232</td><td>6173</td><td>11.92</td><td>0.95</td></tr><tr><td>26bier127</td><td>127</td><td>126</td><td>125</td><td>15.97</td><td>0.79</td><td>6333</td><td>6314</td><td>16.25</td><td>0.30</td></tr><tr><td>26ch130</td><td>130</td><td>129</td><td>127</td><td>10.21</td><td>1.55</td><td>6503</td><td>6412</td><td>9.73</td><td>1.40</td></tr><tr><td>28pr136</td><td>136</td><td>135</td><td>134</td><td>10.24</td><td>0.74</td><td>6850</td><td>6841</td><td>12.24</td><td>0.13</td></tr><tr><td>29pr144</td><td>144</td><td>143</td><td>141</td><td>17.35</td><td>1.40</td><td>7242</td><td>7195</td><td>22.01</td><td>0.65</td></tr><tr><td>30ch150</td><td>150</td><td>149</td><td>144</td><td>9.59</td><td>3.36</td><td>7533</td><td>7315</td><td>12.32</td><td>2.89</td></tr><tr><td>30kroA150</td><td>150</td><td>149</td><td>145</td><td>11.29</td><td>2.68</td><td>7533</td><td>7361</td><td>13.76</td><td>2.28</td></tr><tr><td>30kroB150</td><td>150</td><td>149</td><td>148</td><td>15.25</td><td>0.67</td><td>7533</td><td>7445</td><td>15.14</td><td>1.17</td></tr><tr><td>31pr152</td><td>152</td><td>151</td><td>147</td><td>18.22</td><td>2.65</td><td>7658</td><td>7422</td><td>17.77</td><td>3.08</td></tr><tr><td>32u159</td><td>159</td><td>158</td><td>157</td><td>15.51</td><td>0.63</td><td>8037</td><td>7991</td><td>22.87</td><td>0.57</td></tr><tr><td>39rat195</td><td>195</td><td>194</td><td>189</td><td>13.04</td><td>2.58</td><td>9863</td><td>9558</td><td>11.02</td><td>3.09</td></tr><tr><td>40d198</td><td>198</td><td>197</td><td>196</td><td>36.76</td><td>0.51</td><td>9997</td><td>9934</td><td>25.74</td><td>0.63</td></tr><tr><td>AVG</td><td></td><td></td><td></td><td></td><td>11.95</td><td>2.15</td><td></td><td></td><td>12.59</td><td>2.02</td></tr><tr><td rowspan="24">Large</td><td>40kroa200</td><td>200</td><td>199</td><td>198</td><td>22.75</td><td>0.50</td><td>10,058</td><td>10,010</td><td>24.54</td><td>0.48</td></tr><tr><td>40krob200</td><td>200</td><td>199</td><td>198</td><td>19.86</td><td>0.50</td><td>10,058</td><td>9990</td><td>28.58</td><td>0.68</td></tr><tr><td>45ts225</td><td>225</td><td>224</td><td>221</td><td>34.67</td><td>1.34</td><td>11,308</td><td>11,187</td><td>26.18</td><td>1.07</td></tr><tr><td>45tsp225</td><td>225</td><td>224</td><td>219</td><td>16.70</td><td>2.23</td><td>11,308</td><td>11,103</td><td>16.44</td><td>1.81</td></tr><tr><td>46pr226</td><td>226</td><td>225</td><td>224</td><td>26.94</td><td>0.44</td><td>11,375</td><td>11,368</td><td>26.44</td><td>0.06</td></tr><tr><td>53gil262</td><td>262</td><td>261</td><td>258</td><td>27.20</td><td>1.15</td><td>13,193</td><td>13,050</td><td>25.92</td><td>1.08</td></tr><tr><td>53pr264</td><td>264</td><td>263</td><td>262</td><td>34.02</td><td>0.38</td><td>13,302</td><td>13,277</td><td>36.94</td><td>0.19</td></tr><tr><td>56a280</td><td>280</td><td>279</td><td>273</td><td>33.52</td><td>2.15</td><td>14,178</td><td>13,971</td><td>37.03</td><td>1.46</td></tr><tr><td>60pr299</td><td>299</td><td>298</td><td>296</td><td>31.34</td><td>0.67</td><td>15,107</td><td>15,005</td><td>36.75</td><td>0.68</td></tr><tr><td>64lin318</td><td>318</td><td>317</td><td>315</td><td>43.42</td><td>0.63</td><td>16,037</td><td>16,013</td><td>77.26</td><td>0.15</td></tr><tr><td>80rd400</td><td>400</td><td>399</td><td>397</td><td>76.68</td><td>0.50</td><td>20,158</td><td>20,055</td><td>48.06</td><td>0.51</td></tr><tr><td>84fl417</td><td>417</td><td>416</td><td>415</td><td>103.55</td><td>0.24</td><td>21,048</td><td>21,030</td><td>114.65</td><td>0.09</td></tr><tr><td>88pr439</td><td>439</td><td>438</td><td>437</td><td>157.96</td><td>0.23</td><td>22,177</td><td>22,110</td><td>132.76</td><td>0.30</td></tr><tr><td>89pcb442</td><td>442</td><td>441</td><td>440</td><td>129.54</td><td>0.23</td><td>22,323</td><td>22,300</td><td>94.98</td><td>0.10</td></tr><tr><td>99d493</td><td>493</td><td>492</td><td>490</td><td>120.84</td><td>0.41</td><td>24,862</td><td>24,827</td><td>153.07</td><td>0.14</td></tr><tr><td>115rat575</td><td>575</td><td>574</td><td>562</td><td>91.23</td><td>2.09</td><td>29,033</td><td>28,497</td><td>65.91</td><td>1.85</td></tr><tr><td>115u574</td><td>574</td><td>573</td><td>571</td><td>204.52</td><td>0.35</td><td>28,957</td><td>28,888</td><td>212.74</td><td>0.24</td></tr><tr><td>131p654</td><td>654</td><td>653</td><td>652</td><td>356.02</td><td>0.15</td><td>32,997</td><td>32,991</td><td>360.06</td><td>0.02</td></tr><tr><td>132d657</td><td>657</td><td>656</td><td>649</td><td>126.14</td><td>1.07</td><td>33,188</td><td>32,974</td><td>155.92</td><td>0.64</td></tr><tr><td>145u724</td><td>724</td><td>723</td><td>716</td><td>99.60</td><td>0.97</td><td>36,532</td><td>36,288</td><td>116.69</td><td>0.67</td></tr><tr><td>157rat783</td><td>783</td><td>782</td><td>767</td><td>279.23</td><td>1.92</td><td>39,517</td><td>38,953</td><td>145.54</td><td>1.43</td></tr><tr><td>201pr1002</td><td>1002</td><td>1001</td><td>994</td><td>304.91</td><td>0.70</td><td>50,583</td><td>50,453</td><td>992.74</td><td>0.26</td></tr><tr><td>212u1060</td><td>1060</td><td>1059</td><td>1057</td><td>873.47</td><td>0.19</td><td>53,548</td><td>53,450</td><td>798.51</td><td>0.18</td></tr><tr><td>217vm1084</td><td>1084</td><td>1083</td><td>1078</td><td>489.48</td><td>0.46</td><td>54,712</td><td>54,642</td><td>655.52</td><td>0.13</td></tr><tr><td>AVG</td><td></td><td></td><td></td><td></td><td>154.32</td><td>0.81</td><td></td><td></td><td>182.63</td><td>0.59</td></tr></table>

Next we move to larger instances, with ω < 1, for which no optimal solution is available. The aim of this second set of experiments is to show the effectiveness of the different procedures embedded in MASOP. In particular, we aim at showing the effectiveness of the tabu search in improving the initial solution and, more specifically, the effectiveness of Procedure MIPMove(T ). In order to do that, we run two versions of MASOP: the complete version as described in Section 3 and a version where Procedure MIPMove(T ) is removed.

We call this second version HSOP for Heuristic for the SOP. In fact, this algorithm is no more a matheuristic algorithm and is a standard heuristic.

Results are shown in Table 3. The table is divided in two blocks of rows related to instances of Sets 1 and 2. We report average results on the instances clustered according to their number of customers, the value of ω and the rule used to generate profits. We report average results over instances belonging to the same cluster. The first three columns of the table report: the class of instances according to the number of customers, the kind of profits and the value of ω. Next, we report the average value of the initial solution, the average value of the best solution found by either MA-

Solution values for MASOP and HSOP.

<table><tr><td rowspan="2" colspan="2">Size</td><td rowspan="2"> $p_g$ </td><td rowspan="2">ω</td><td rowspan="2"> $T_S$ </td><td rowspan="2"> $T_B$ </td><td rowspan="2"> $T_B vs T_S$ </td><td colspan="3">HSOP</td><td rowspan="2"></td><td colspan="3">MASOP</td></tr><tr><td>#best</td><td>profit</td><td>Gap%</td><td>#best</td><td>profit</td><td>Gap%</td></tr><tr><td rowspan="19">Set 1</td><td rowspan="8">Small</td><td rowspan="3"> $g_1$ </td><td>0.4</td><td>35.78</td><td>53.33</td><td>32.91%</td><td>27/27</td><td>53.33</td><td>0.00%</td><td></td><td>27/27</td><td>53.33</td><td>0.00%</td></tr><tr><td>0.6</td><td>45.21</td><td>80.70</td><td>43.98%</td><td>25/27</td><td>80.62</td><td>0.10%</td><td></td><td>27/27</td><td>80.70</td><td>0.00%</td></tr><tr><td>0.8</td><td>53.96</td><td>99.55</td><td>45.80%</td><td>26/27</td><td>99.55</td><td>0.00%</td><td></td><td>26/27</td><td>99.51</td><td>0.04%</td></tr><tr><td>avg</td><td colspan="3"></td><td>40.89%</td><td colspan="2">26/27</td><td>0.03%</td><td colspan="3">26.6/27</td><td>0.01%</td></tr><tr><td rowspan="3"> $g_2$ </td><td>0.4</td><td>2011.14</td><td>2681.66</td><td>25.00%</td><td>27/27</td><td>2681.66</td><td>0.00%</td><td></td><td>26/27</td><td>2681.22</td><td>0.02%</td></tr><tr><td>0.6</td><td>2395.74</td><td>4059.70</td><td>40.99%</td><td>27/27</td><td>4059.70</td><td>0.00%</td><td></td><td>27/27</td><td>4059.70</td><td>0.00%</td></tr><tr><td>0.8</td><td>2911.96</td><td>5037.37</td><td>42.19%</td><td>26/27</td><td>5037.37</td><td>0.00%</td><td></td><td>26/27</td><td>5034.03</td><td>0.07%</td></tr><tr><td>avg</td><td colspan="3"></td><td>36.06%</td><td colspan="2">26.6/27</td><td>0.00%</td><td colspan="3">26.3/27</td><td>0.03%</td></tr><tr><td>avg</td><td></td><td colspan="3"></td><td>38.48%</td><td colspan="2">26.3/27</td><td>0.02%</td><td colspan="3">26.5/27</td><td>0.02%</td></tr><tr><td rowspan="8">Large</td><td rowspan="3"> $g_1$ </td><td>0.4</td><td>81.58</td><td>245.83</td><td>66.81%</td><td>19/24</td><td>245.83</td><td>0.00%</td><td></td><td>21/24</td><td>244.66</td><td>0.48%</td></tr><tr><td>0.6</td><td>111.33</td><td>361.62</td><td>69.21%</td><td>13/24</td><td>361.33</td><td>0.08%</td><td></td><td>20/24</td><td>361.62</td><td>0.00%</td></tr><tr><td>0.8</td><td>126.54</td><td>447.66</td><td>71.73%</td><td>16/24</td><td>446.25</td><td>0.31%</td><td></td><td>19/24</td><td>447.66</td><td>0.00%</td></tr><tr><td>avg</td><td colspan="3"></td><td>69.25%</td><td colspan="2">16/24</td><td>0.13%</td><td></td><td>20/24</td><td></td><td>0.16%</td></tr><tr><td rowspan="3"> $g_2$ </td><td>0.4</td><td>4046.12</td><td>12482.95</td><td>67.59%</td><td>15/24</td><td>12469.00</td><td>0.11%</td><td></td><td>21/24</td><td>12482.95</td><td>0.00%</td></tr><tr><td>0.6</td><td>5365.70</td><td>18433.33</td><td>70.89%</td><td>12/24</td><td>18394.29</td><td>0.21%</td><td></td><td>20/24</td><td>18433.33</td><td>0.00%</td></tr><tr><td>0.8</td><td>6744.45</td><td>22797.41</td><td>70.42%</td><td>14/24</td><td>22797.41</td><td>0.00%</td><td></td><td>17/24</td><td>22768.25</td><td>0.13%</td></tr><tr><td>avg</td><td colspan="3"></td><td>69.63%</td><td colspan="2">13.6/24</td><td>0.11%</td><td colspan="3">19.3/24</td><td>0.04%</td></tr><tr><td>avg</td><td></td><td colspan="3"></td><td>69.44%</td><td colspan="2">14.8/24</td><td>0.12%</td><td colspan="3">19.6/24</td><td>0.10%</td></tr><tr><td></td><td></td><td colspan="3"></td><td>53.96%</td><td colspan="2">20.5/24</td><td>0.07%</td><td colspan="3">23/24</td><td>0.06%</td></tr><tr><td rowspan="19">Set 2</td><td rowspan="8">Small</td><td rowspan="3"> $g_1$ </td><td>0.4</td><td>56.35</td><td>95.59</td><td>41.05%</td><td>26/27</td><td>95.59</td><td>0.00%</td><td></td><td>25/27</td><td>95.59</td><td>0.00%</td></tr><tr><td>0.6</td><td>69.46</td><td>112.48</td><td>38.25%</td><td>24/27</td><td>112.48</td><td>0.00%</td><td></td><td>25/27</td><td>112.18</td><td>0.27%</td></tr><tr><td>0.8</td><td>80.64</td><td>115.70</td><td>30.30%</td><td>27/27</td><td>115.70</td><td>0.00%</td><td></td><td>27/27</td><td>115.70</td><td>0.00%</td></tr><tr><td>avg</td><td colspan="3"></td><td>36.53%</td><td colspan="2">25.6/27</td><td>0.00%</td><td colspan="3">25.6/27</td><td>0.09%</td></tr><tr><td rowspan="3"> $g_2$ </td><td>0.4</td><td>2923.74</td><td>4825.74</td><td>39.41%</td><td>23/27</td><td>4811.18</td><td>0.30%</td><td></td><td>26/27</td><td>4825.74</td><td>0.00%</td></tr><tr><td>0.6</td><td>3625.48</td><td>5700.03</td><td>36.40%</td><td>24/27</td><td>5700.03</td><td>0.00%</td><td></td><td>25/27</td><td>5699.51</td><td>0.01%</td></tr><tr><td>0.8</td><td>4285.51</td><td>5861.51</td><td>26.89%</td><td>27/27</td><td>5861.51</td><td>0.00%</td><td></td><td>27/27</td><td>5861.51</td><td>0.00%</td></tr><tr><td>avg</td><td colspan="3"></td><td>34.23%</td><td colspan="2">24.6/27</td><td>0.10%</td><td colspan="3">26/27</td><td>0.00%</td></tr><tr><td>avg</td><td></td><td colspan="3"></td><td>35.38%</td><td colspan="2">25.1/27</td><td>0.05%</td><td colspan="3">25.8/27</td><td>0.05%</td></tr><tr><td rowspan="8">Large</td><td rowspan="3"> $g_1$ </td><td>0.4</td><td>160.91</td><td>415.00</td><td>61.23%</td><td>14/24</td><td>415.00</td><td>0.00%</td><td></td><td>20/24</td><td>414.70</td><td>0.07%</td></tr><tr><td>0.6</td><td>203.33</td><td>481.12</td><td>57.74%</td><td>19/24</td><td>480.70</td><td>0.09%</td><td></td><td>23/24</td><td>481.12</td><td>0.00%</td></tr><tr><td>0.8</td><td>236.58</td><td>490.79</td><td>51.80%</td><td>24/24</td><td>490.79</td><td>0.00%</td><td></td><td>24/24</td><td>490.79</td><td>0.00%</td></tr><tr><td>avg</td><td colspan="3"></td><td>56.92%</td><td colspan="2">19/24</td><td>0.03%</td><td></td><td>22.3/24</td><td></td><td>0.02%</td></tr><tr><td rowspan="3"> $g_2$ </td><td>0.4</td><td>8466.70</td><td>21165.20</td><td>60.00%</td><td>12/24</td><td>21077.83</td><td>0.41%</td><td></td><td>20/24</td><td>21165.20</td><td>0.00%</td></tr><tr><td>0.6</td><td>10727.95</td><td>24327.12</td><td>55.90%</td><td>17/24</td><td>24301.91</td><td>0.10%</td><td></td><td>19/24</td><td>24327.12</td><td>0.00%</td></tr><tr><td>0.8</td><td>12603.08</td><td>24814.95</td><td>49.21%</td><td>24/24</td><td>24814.95</td><td>0.00%</td><td></td><td>24/24</td><td>24814.95</td><td>0.00%</td></tr><tr><td>avg</td><td colspan="3"></td><td>55.04%</td><td colspan="2">17.6/24</td><td>0.17%</td><td colspan="3">21/24</td><td>0.00%</td></tr><tr><td>avg</td><td></td><td colspan="3"></td><td>55.98%</td><td colspan="2">18.3/24</td><td>0.10%</td><td colspan="3">21.6/24</td><td>0.01%</td></tr><tr><td></td><td></td><td colspan="3"></td><td>45.68%</td><td colspan="2">21.7/24</td><td>0.08%</td><td colspan="3">23.7/24</td><td>0.03%</td></tr></table>

SOP or HSOP and the percentage improvement of the best solution over the initial solution. The average improvement is calculated as $\frac { z _ { b e s t } { - } z _ { i n i t } } { z _ { b e s t } }$ where $z _ { b e s t }$ is the value of the best known solution and $z _ { i n i t }$ is the value of the initial solution. Then, two blocks of three columns each follow related to MASOP and HSOP. They report, respectively: the number of times the corresponding algorithm found the best solution over the total number of instances in the class, the average solution value and the average gap with respect to the best known solution. The gap with respect to the best known solution is calculated as $\frac { z _ { b e s t } { - } z _ { H } } { z _ { b e s t } }$ where $z _ { H }$ is the value of the solution provided by the algorithm considered.

From Table 3 we can see that, focusing on instances of Set 1, the effect of MIPMove(T ) is more evident on large instances than on small ones. In fact, while MASOP finds the best known value on 118 instances over 144, HSOP finds it on 89 instances only. The average gap has only a slight increase from MASOP to HSOP (from 0.10% to 0.12%) due to the fact that, on instances with profits $g _ { 1 } .$ , HSOP behaves better than MASOP. On small instances instead, the two algorithms have very similar performances, with HSOP performing slightly better than MASOP. Concerning the comparison with the initial solution, the improvement produced by either MASOP or HSOP is remarkable, being 53.96% on average and

**Table 4**

Computing times for MASOP and HSOP.

<table><tr><td></td><td>Size</td><td> $p_g$ </td><td>ω</td><td>HSOP</td><td>MASOP</td></tr><tr><td rowspan="18">Set 1</td><td rowspan="8">Small</td><td rowspan="3"> $g_1$ </td><td>0.4</td><td>2.76</td><td>7.18</td></tr><tr><td>0.6</td><td>3.57</td><td>8.52</td></tr><tr><td>0.8</td><td>4.21</td><td>8.09</td></tr><tr><td>avg</td><td></td><td>3.51</td><td>7.93</td></tr><tr><td rowspan="3"> $g_2$ </td><td>0.4</td><td>2.86</td><td>7.39</td></tr><tr><td>0.6</td><td>3.81</td><td>8.72</td></tr><tr><td>0.8</td><td>4.59</td><td>7.96</td></tr><tr><td>avg</td><td></td><td>3.75</td><td>8.02</td></tr><tr><td>avg</td><td></td><td></td><td>3.63</td><td>7.98</td></tr><tr><td rowspan="8">Large</td><td rowspan="3"> $g_1$ </td><td>0.4</td><td>37.57</td><td>172.46</td></tr><tr><td>0.6</td><td>38.65</td><td>87.23</td></tr><tr><td>0.8</td><td>36.06</td><td>76.95</td></tr><tr><td>avg</td><td></td><td>37.43</td><td>112.21</td></tr><tr><td rowspan="3"> $g_2$ </td><td>0.4</td><td>32.38</td><td>216.72</td></tr><tr><td>0.6</td><td>33.35</td><td>93.88</td></tr><tr><td>0.8</td><td>48.92</td><td>79.26</td></tr><tr><td>avg</td><td></td><td>38.22</td><td>129.95</td></tr><tr><td>avg</td><td></td><td></td><td>37.82</td><td>121.08</td></tr><tr><td>avg</td><td></td><td></td><td></td><td>20.73</td><td>64.53</td></tr><tr><td rowspan="17">Set 2</td><td rowspan="8">Small</td><td rowspan="3"> $g_1$ </td><td>0.4</td><td>3.51</td><td>6.15</td></tr><tr><td>0.6</td><td>5.44</td><td>10.33</td></tr><tr><td>0.8</td><td>7.01</td><td>13.57</td></tr><tr><td>avg</td><td></td><td>5.32</td><td>10.02</td></tr><tr><td rowspan="3"> $g_2$ </td><td>0.4</td><td>3.33</td><td>6.44</td></tr><tr><td>0.6</td><td>5.42</td><td>10.29</td></tr><tr><td>0.8</td><td>6.91</td><td>13.68</td></tr><tr><td>avg</td><td></td><td>5.22</td><td>10.14</td></tr><tr><td rowspan="8">Large</td><td rowspan="3"> $g_1$ </td><td>0.4</td><td>123.93</td><td>201.70</td></tr><tr><td>0.6</td><td>115.96</td><td>140.16</td></tr><tr><td>0.8</td><td>200.37</td><td>253.95</td></tr><tr><td>avg</td><td></td><td>146.75</td><td>198.60</td></tr><tr><td rowspan="3"> $g_2$ </td><td>0.4</td><td>130.84</td><td>271.93</td></tr><tr><td>0.6</td><td>107.55</td><td>191.36</td></tr><tr><td>0.8</td><td>226.59</td><td>287.12</td></tr><tr><td>avg</td><td></td><td>154.99</td><td>250.14</td></tr><tr><td>avg</td><td></td><td></td><td>150.87</td><td>224.37</td></tr><tr><td>avg</td><td></td><td></td><td></td><td>79.08</td><td>121.16</td></tr></table>

69.44% on large instances. Similar considerations can be made on instances of Set 2. Here, on large instances, MASOP finds the best solution on 123 instances over 144, while HSOP finds it on 100 instances. However, the difference in terms of average gap to best known value is larger than for instances of Set 1, being 0.01% for MASOP and 0.10% for HSOP. Considering the improvement with respect to the initial solution, we notice that it is lower than for instances of Set 1 but still 45.98% on average and 55.98% on large instances.

Finally, in Table 4 we report the computational times of MASOP and HSOP. The first three columns of the table are the same as in Table 3. The next two columns report the average computational times for the two algorithms.

Looking at Table 4, we can see that instances of Set 2 takes nearly the double of the time taken by instances of Set 1 for both algorithms. Also, MASOP takes nearly the triple of the time of HSOP on instances of Set 1 while less than the double on instances of Set 2. In any case, computing times of MASOP remain reasonable even for large instances.

## 5. Conclusions

In this paper we introduces the Set Orienteering Problem (SOP) which is a variant of the OP where customers are grouped in clusters and a profit is associated with each cluster. The profit is collected only if at least one vertex belonging to the cluster is visited. The objective is to find the tour that maximizes the collected profit and such that the corresponding duration does not exceed a given threshold. We propose a mathematical formulation and a matheuristic for the SOP. Computational tests on instances with up 1084 vertices show that the matheuristic produces high-quality results in reasonable computing times.

The SOP finds applications in the distribution of mass products where carriers stipulated contracts with customers organized in chains and the contracts are such that the carrier may choose which of the customer in the chain to visit in order to satisfy all the customers in the chain. Thus, this is a way to organize distribution processes which may provide advantages both to carriers, in terms of lower distribution costs, and for the customers, in terms of lower tariffs requested by the carriers.

## References

[Angelelli, E., Archetti, C., & Vindigni, M. (2014). The clustered orienteering problem. European Journal of Operational Research, 238, 404–414.](http://refhub.elsevier.com/S0377-2217%2817%2931020-2/sbref0001)

[Archetti, C., & Speranza, M. (2014). Arc routing problems with profits. In A. Corberàn, & G. Laporte (Eds.), ARC routing: Problems, methods, and applications. In MOS-SIAM series on optimization (pp. 257–284). Philadelphia: SIAM.](http://refhub.elsevier.com/S0377-2217%2817%2931020-2/sbref0002)

[Archetti, C., Speranza, M., & Vigo, D. (2014). Vehicle routing problems with profits. In P. Toth, & D. Vigo (Eds.), Vehicle routing: Problems, methods, and applications. In MOS-SIAM series on optimization: Vol. 18 (pp. 273–298). Philadelphia: SIAM.](http://refhub.elsevier.com/S0377-2217%2817%2931020-2/sbref0003)

[Coutinho, W. P., do Nascimento, R. Q., Pessoa, A. A., & Subramanian, A. (2016). A branch-and-bound algorithm for the close-enough traveling salesman problem. INFORMS Journal on Computing, 28(4), 752–765.](http://refhub.elsevier.com/S0377-2217%2817%2931020-2/sbref0004)

[Fischetti, M., Salazar Gonzàlez, J. J., & Toth, P. (1997). A branch-and-cut algorithm for the symmetric generalized traveling salesman problem. Operations Research, 45(3), 378–394.](http://refhub.elsevier.com/S0377-2217%2817%2931020-2/sbref0005)

[Gavish, B., & Graves, S. (1978). The travelling salesman problem and related problems. Working Paper GR-078-78. Operations Research Center, Massachusetts Institute of Technology.](http://refhub.elsevier.com/S0377-2217%2817%2931020-2/sbref0006)

[Gunawan, A., Lau, H. C., & Vansteenwegen, P. (2016). Orienteering problem: A survey of recent variants, solution approaches and applications. European Journal of Operational Research, 255(2), 315–332.](http://refhub.elsevier.com/S0377-2217%2817%2931020-2/sbref0007)

[Hu, B., & Raidl, G. R. (2008). Effective neighborhood structures for the generalized traveling salesman problem. In J. van Hemert, & C. Cotta (Eds.), Proceedings of the eighth european conference on evolutionary computation in combinatorial optimization (EVOCOP 2008), Naples, Italy (pp. 36–47). Berlin, Heidelberg: Springer Berlin Heidelberg.](http://refhub.elsevier.com/S0377-2217%2817%2931020-2/sbref0008)

[Laporte, G., & Norbert, Y. (1983). Generalized traveling salesman problem through n sets of nodes: An integer programming approach. INFOR, 21(1), 61–75.](http://refhub.elsevier.com/S0377-2217%2817%2931020-2/sbref0009)

[Lin, S., & Kernighan, B. (1973). An effective heuristic algorithm for the traveling salesman problem. Operations Research, 21, 498–516.](http://refhub.elsevier.com/S0377-2217%2817%2931020-2/sbref0010)

[Öncan, T., Altinel, I. K., & Laporte, G. (2009). A comparative analysis of several asymmetric traveling salesman problem formulations. Computers & Operations Research, 36, 637–654.](http://refhub.elsevier.com/S0377-2217%2817%2931020-2/sbref0011)

[Pop, P. C., Matei, O., & Sabo, C. (2010). A new approach for solving the generalized traveling salesman problem. In M. J. Blesa, C. Blum, G. Raidl, A. Roli, & M. Sampels (Eds.), Proceedings of the seventh international workshop on hybrid metaheuristics (HM 2010), Vienna, Austria (pp. 62–72). Berlin, Heidelberg: Springer Berlin Heidelberg.](http://refhub.elsevier.com/S0377-2217%2817%2931020-2/sbref0012)

[Tsiligirides, T. (1984). Heuristic methods applied to orienteering. Journal of the Operational Research Society, 35, 797–809.](http://refhub.elsevier.com/S0377-2217%2817%2931020-2/sbref0013)