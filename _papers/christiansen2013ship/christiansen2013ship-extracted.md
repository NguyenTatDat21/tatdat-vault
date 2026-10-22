Invited Review

# Ship routing and scheduling in the new millennium

Marielle Christiansen a,⇑, Kjetil Fagerholt a,b, Bjørn Nygreen a, David Ronen c

<sup>a</sup> Department of Industrial Economics and Technology Management, Norwegian University of Science and Technology, Trondheim, Norway

<sup>b</sup> Norwegian Marine Technology Research Institute (MARINTEK), Trondheim, Norway

c College of Business Administration, University of Missouri-St. Louis, St. Louis, MO, USA

## a r t i c l e i n f o

Article history: Received 22 March 2012 Accepted 1 December 2012 Available online 10 December 2012

Keywords: Maritime transportation Routing Inventory management Liner shipping Tramp shipping

## a b s t r a c t

We review research on ship routing and scheduling and related problems during the new millennium and provide four basic models in this domain. The volume of research in this area about doubles every decade as does the number of research outlets. We have found over a hundred new refereed papers on this topic during the last decade. Problems of wider scope have been addressed as well as more specialized ones. However, complex critical problems remain wide open and provide challenging opportunities for future research.

\- 2013 Elsevier B.V. All rights reserved.

## 1. Introduction

Ocean going ships are the blood vessels of international trade and facilitate the expansion of the global economy. The increasing population, standard of living and industrialization of the Far East are driving the demand for increased ocean shipping capacity, both for importing bulk raw materials and exporting containerized manufactured goods. During the first decade of the new millennium the cargo carrying capacity of oil tankers grew by 60%, that of dry bulk carriers grew by 65%, and containership capacity more than doubled (up 164%, see Table 1). The growth of fleet capacity facilitates the fast expansion of seaborne international trade that has increased by 40% during the same decade (see Table 2). Efficient design and operation of the world fleet increase its productivity and the world’s standard of living. Ship routing and scheduling, the focus of this review, is the major determinant of the fleet productivity.

About every 10 years we have been publishing a survey of research on ship routing and scheduling (and related) problems (see Christiansen et al., 2004; Ronen, 1993, 1983). This paper is the fourth instalment in that series. The purpose of these surveys is to provide a (hopefully) comprehensive source for research published in scientific journals and edited volumes on ship routing and scheduling. Such a source should be useful to researchers and students of this domain. In addition, Christiansen et al. (2007) provided a wider perspective of this domain. The quantity of published research on ship routing and scheduling and related problems has been almost doubling every decade (as discussed later in Section 6). Therefore, in contrast to our earlier reviews, due to space limitations we have to confine our current review to include only work published in English in refereed journals or edited volumes. Thus, excluded from this review are working papers, conference proceedings, theses, dissertations, and technical reports. This review focuses on prescriptive models (those recommending course of action), rather than descriptive models (those describing aggregate behaviour), and, in order to assure overlap with our last review, covers material published in print and online during the years 2002–2011. However, some journals are publishing ahead of time and thus some papers dated 2012 are included here. Material discussed in our earlier reviews is mentioned here only when necessary for completeness of exposition. In addition, we do not cover here specialized problems associated with container line operations, such as: berth scheduling, container stowage, containers management, container yard management, and cargo allocation. Recent reviews are available on some of these topics (e.g. Stahlbock and Voss, 2008). We also do not include here papers regarding operation of non-commercial vessels (e.g. naval vessels).

The fast growth of the containership fleet has been accompanied by a similar growth in research on liner network design and related topics. Therefore we provide wider coverage and present two basic models in this area. Maritime inventory routing (MIR), and, to a lesser extent, Liquefied Natural Gas (LNG) transportation and offshore supply vessels (OSVs) have also attracted increasing attention. More recently, mainly due to the increasing price of bunker fuel, more attention has been devoted to sailing speeds and environmental impact of ships. Thus we review these topics in separate sections.

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">⇑ Corresponding author. Tel.: +47 73593602.</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">E-mail address: [Marielle.Christiansen@iot.ntnu.no](mailto:Marielle.Christiansen@iot.ntnu.no) (M. Christiansen).</span></small>

Table 1

World fleet (beginning-of-year, in million dwt).<sup>a</sup>

| Year | Oil tanker | Dry bulk | General cargo | Container | Other | Total |
| --- | --- | --- | --- | --- | --- | --- |
| 1980 | 339 | 186 | 116 | 11 | 31 | 683 |
| 1985 | 261 | 232 | 106 | 20 | 45 | 664 |
| 1990 | 246 | 235 | 103 | 26 | 49 | 659 |
| 1995 | 268 | 262 | 104 | 44 | 58 | 736 |
| 2000 | 282 | 276 | 101 | 64 | 75 | 798 |
| 2005 | 336 | 321 | 92 | 98 | 49 | 896 |
| 2010 | 450 | 457 | 108 | 169 | 92 | 1276 |

a Cargo carrying vessels over 100 gross tons (source: UNCTAD (2011)).

Table 2

International seaborne trade (millions of tons loaded).

| Year | Oil | Main bulks<sup>a</sup> | Other dry cargo | Total (all cargoes) |
| --- | --- | --- | --- | --- |
| 1980 | 1871 | 796 | 1037 | 3704 |
| 1990 | 1755 | 968 | 1285 | 4008 |
| 2000 | 2163 | 1288 | 2533 | 5984 |
| 2010 | 2752 | 2333 | 3323 | 8408 |

a Iron ore, grain, coal, bauxite/alumina, and phosphate (source: UNCTAD (2011)).

For the novice we have to provide the lay of the land. Ships are usually operated in one of three modes: liner, industrial or tramp. Liner vessels follow a fixed route according to a published schedule, trying to maximize profit, similar to a public bus service. An industrial operator owns the cargo and controls the ships, trying to minimize the cost of delivering the cargoes, similar to a private fleet. In a tramp operation the vessels follow the available cargoes (some of which may be optional), trying to maximize profit, similar to a taxi cab. Ship routing and scheduling decisions in industrial and tramp operations are very similar (except for the optional cargoes in tramp), and therefore they will be discussed together while pointing out the differences. Each one of these operational modes may have niches with special characteristics, such as LNG shipping in industrial/tramp operations, where the number of berths can be very limited (i.e. ship arrivals have to be coordinated) and the cargo is hazardous. For additional background information regarding OR in maritime transportation the reader is referred to Christiansen et al. (2007).

The remainder of this review is organized as follows. In the next section we discuss liner shipping, starting with the strategic issue of network design, then moving to tactical and operational issues. Section 3 is devoted to industrial and tramp shipping, starting with fleet size and composition, moving to cargo routing and scheduling, and then to MIR and LNG. The fourth section focuses on sailing speed, bunkering, and emissions. The fifth one discusses offshore logistics (OSV), lightering, and cargo stowage. Section 6 provides a brief statistical analysis of past research in this domain. Finally we wrap up with concluding remarks.

## 2. Liner shipping

Today, container shipping constitutes the major segment of liner shipping. Combined with the accelerating adoption of shipping containers as the primary mode for shipping general break bulk cargo during the last several decades, liner operators have replaced their general cargo vessels by cellular containerships. Ocean shipping containers were introduced more than half a century ago, but initially their adoption was slow due to the large capital investment required and the transportation infrastructure changes involved. Break bulk cargo (that constitutes the vast majority of packaged goods) used to be carried by multi-deck vessels where each piece (case, bag, drum, etc.) was handled manually numerous times during the shipping process. This labour intensive process resulted in significant cargo damage and provided many opportunities for loss. In addition it resulted in ships spending 50–70% of their route time in ports for cargo handling operations. One should bear in mind that ships are productive only when sailing.

Cargo containerization during recent decades has reduced shipping costs and cargo damage and loss, and improved ship utilization. Container ships spend only 15–30% of their route time in ports for cargo handling operations (the longer the line the lower the percentage of time in port). The cargo carrying capacity of the world containership fleet has more than doubled in each of the last three decades (see Table 1), and the growing fleet has attracted increasing research interest. However, by now containers have achieved close to full market penetration (namely, most of the cargo fit for containerization already is containerized), and future growth will come mainly from trade growth.

Intercontinental container lines (e.g. Asia–Europe, Asia–North America) usually operate in a hub and spoke system with a long main line and regional feeder lines. Containers are transshipped between the main line and the feeder lines at the hub ports. Regional container services (e.g. in the Far East, Mediterranean–Europe) may also include a feeder service. A round trip on a main line may take a few months whereas feeder lines are much shorter. A small minority of containerships are operated in industrial mode to carry special cargo (e.g. refrigerated produce). Kjeldsen (2011) provides a classification of routing and scheduling problems in liner shipping.

Another (minor) segment of liner shipping that expanded remarkably during recent decades is Roll-on Roll-off vessels (RoRo) that are used to transport cars, trucks, trailers and other rolling equipment. These are usually multi-deck vessels where the cargo is driven on and off the vessel through a ramp.

## 2.1. Network design

Liner ships operate mostly along established routes following regular timetables published several months ahead. Although the frequency of sailings may change seasonally, the routes themselves may not change for several years. Therefore the route network design is an important strategic decision. A route in this context is a result of three major decisions: (1) which ports to visit and in what sequence, (2) how often to visit the ports, and (3) the size and speed of the ships to use. In addition, there are many situations where a company, or a group of cooperating companies, have several interconnecting routes. The problem of constructing routes and choosing which routes to serve is usually referred to as the network design problem. In order to be able to solve this problem, the company needs to have a reasonable estimate of the amount of demand it will attract. Thus, in setting up a model for the network design problem, companies usually also model the types of ship to use and how to allocate the estimated demand to the ships. The route network is usually used for several years, while the deployment of the ships (namely, the assignment of ships to routes) might be changed several times a year, as discussed below.

We present here a mathematical model for a liner network design problem that is a slightly simplified version of a model suggested by Agarwal and Ergun (2008). Then we review last decade’s literature on this topic.

In the following model we assume that the shipping company has decided to operate a set of container routes. At the moment the company has a specified set of routes denoted by R of which they want to operate only a profitable subset. The company has decided that all routes should run weekly and that they should restrict the types of ships to a set denoted by V. We also assume that a time resolution of 1 day is sufficient and the set of days in a week is denoted by D. For the elements in the sets, we will use the following indices: r for routes, v for ship types and i and j for days.

In addition o and d represent the origin and destination for particular demand, while p represents an arbitrary port.

In this network design model, we assume that it is reasonable to use a stationary weekly demand. The demanded quantity from o to d available for shipping on day i in every week is $\dot { D } ^ { ( o , d , i ) }$ (however, it may be shipped on a later day). The set of all index triplets $( o , d , i )$ is denoted by W. We need $L _ { v r }$ ships of type v to serve route r with weekly departures, and ship type v has a capacity of $K _ { \nu }$ containers. There might be a shortage in the number of available ships of some of the types, so $N _ { \nu }$ is an upper bound on the number of ships of type v.

Our network model is based on a graph where each port is given a node for each day of the week. The set of all nodes in the graph is denoted by $\mathcal { N }$ and indexed by n (or, more specifically, by $n ( p , i )$ or just $( p , i )$ to include information about port p and day i). The set of arcs in the graph is denoted A and consists of three subsets. Subset (1) consists of all the ship legs between the neighbouring ports for all the defined routes for the different ship types. The length of these legs is pictured as an integer number of days between 1 and 7 in the graph. The real length is the pictured length plus 7 multiplied by a non-negative integer. Subset (2) consists of all port (ground) arcs from day i to day i + 1 in the same port including arcs from day 7 to day 1. Subset (3) consists of artificial arcs from $( d , j )$ for all j back to (o, i) for all $( o , d , i ) \in \mathcal { W }$ . Both ships and containers can flow on the arcs of subsets 1 and 2. The ships must follow their routes, while containers may join or leave the ship routes. There is no real flow on the arcs in subset 3, but in the model the containers flow on the artificial arcs to create circular flows of all containers that are serviced. Independent of subsets, all arcs are indexed by a or by (start node, end node).

The monetary parameters are: $( 1 )   R ^ { ( o , d , i ) }$ is the unit revenue for transporting one container available on day i from port o to port d, $( 2 )   C _ { a } ^ { C }$ is the cost of transporting one container along arc a. In order to keep the model simpler (while not including transshipment costs) we keep this cost independent of the container, ship and port. $( 3 )   C _ { v r } ^ { V }$ is the weekly cost of serving route r with $L _ { v r }$ ships of type v.

To be able to formulate our model, we also need two symbolic variables: The binary variable $x _ { v r }$ is equal to 1 if a ship of type v serves route r, and 0 otherwise. For the sake of simplicity we have restricted the solutions not to have more than 1 weekly departure for each ship type on any route. The variable $y _ { a } ^ { ( o , d , i ) }$ is equal to the number of containers from the demand $D ^ { ( o , d , \bar { i } ) }$ that is transported along arc a. In addition, in order to keep the formulation as simple as possible, we define the following sets: $\mathcal { T } ( n )$ is the set of all arcs that enter $n , \mathcal { O } ( n )$ is the set of all arcs that leave n, and ${ \mathcal { K } } ( a )$ is the set of all routes that use arc a.

The mathematical model for the network design problem can now be stated as follows:

max $\sum \sum R ^ { ( o , d , i ) } y _ { [ n ( d , j ) , i ] } ^ { ( o , d , i ) }$ nðo;iÞ-

$$
- \sum_ {(o, d, i) \in \mathcal {W}} \sum_ {a \in \mathcal {A}} C _ {a} ^ {C} y _ {a} ^ {(o, d, i)} - \sum_ {v \in \mathcal {V}} \sum_ {r \in \mathcal {R}} C _ {v r} ^ {V} x _ {v r},\tag{1}
$$

$$
\text {s.t.} \sum_ {a \in \mathcal {I} (n)} y _ {a} ^ {(o, d, i)} - \sum_ {a \in \mathcal {O} (n)} y _ {a} ^ {(o, d, i)} = 0, \quad (o, d, i) \in \mathcal {W}, n \in \mathcal {N},\tag{2}
$$

$$
\sum_ {(o, d, i) \in \mathcal {W}} y _ {a} ^ {(o, d, i)} - \sum_ {v \in \mathcal {V}} \sum_ {r \in \mathcal {K} (a)} K _ {v} x _ {v r} \leqslant 0, \quad a \in \mathcal {A},
$$

$$
\sum_ {j \in \mathcal {D}} y _ {[ n (d, j), n (o, i) ]} ^ {(o, d, i)} \leqslant D ^ {(o, d, i)}, \quad (o, d, i) \in \mathcal {W},\tag{3}
$$

$$
\sum_ {r \in \mathcal {R}} L _ {v r} x _ {v r} \leqslant N _ {v}, \quad v \in \mathcal {V},\tag{4}
$$

$$
x _ {v r} \in \{0, 1 \}, \quad v \in \mathcal {V}, r \in \mathcal {R},\tag{5}
$$

(6)

$$
y _ {a} ^ {(o, d, i)} \geqslant 0, \quad (o, d, i) \in \mathcal {W}, a \in \mathcal {A}.\tag{7}
$$

The objective function (1) expresses the difference between the revenue earned and total cost of operating the network. Constraints (2) ensure that all containers that arrive in a node also leave the node, while the ships’ container capacities are imposed by constraints (3). Constraints (4) say that the container flow from the destination back to the origin is less than or equal to the demand. Since all container flows are modelled as circular flows this ensures that the quantity transported out of the demand ports is kept at or below the demand. Constraints (5) assure that the availability of ships to use is respected, while constraints (6) and (7) express sign and integrality constraints on the variables.

Our simplification compared to the model by Agarwal and Ergun (2008) is mainly in that we select routes from a given set, while they generate new routes (cycles) when needed by column generation. In solving their model they use Bender’s decomposition.

During recent years we have observed increasing richness in network design models for liner shipping compared to liner models discussed by Christiansen et al. (2007), partly as a consequence of increased computational power. Most of the different network design models published during the last decade can be grouped into the following categories:

(1) Models with a single route or sets of routes without transshipment.

(2) Hub and feeder route models where each feeder port is connected to a single hub port.

(3) Models where some ports are classified as hub ports without any constraints on the number of hub and non-hub ports a route may visit.

(4) Multi route models without any separation of hub and non-hub ports.

A hub port is one where container transshipments may take place, and a feeder port is also known as a spoke. We have chosen to divide our review into these four categories.

## 2.1.1. Models with a single route or sets of routes without transshipment

The simplest type of a shipping line is one where the ships sail just between two ports (a shuttle service). Then there is no network to design. Although we are not reviewing such cases here, we refer to the paper by Boros et al. (2008) that discusses other aspects of liner operations between just two ports.

There are mainly two types of single routes. The route may look circular on a map such that it is natural to visit each port only once on each sailing on the route, or the route may look pendular on a map such that the route goes forth and back between its end ports, and the intermediate ports are visited once or twice on each sailing on the route. In both cases the network design problem consists of determining which ports to visit and the visiting sequence.

Lu (2002) formulates a network design model that on a map looks like a combination of a circular and a pendular route. Some of the ports are forced to be visited several times on the route. This creates a route consisting of several loops. The formulation uses binary variables for choosing which legs to sail and corresponding variables for buffer time on the used legs to let the complete route take exactly an integer number of weeks to sail. Chu et al. (2003) give a mixed integer programming (MIP) formulation for a pendular liner network with weekly departures and an upper bound on the number of weeks to sail the route. They illustrate their model using results from a case with eight ports, some in Asia and some on the US west coast. Ting and Tzeng (2003) use detailed costs and time information to schedule a fixed nine-ports circular line by dynamic programming. Shintani et al. (2007) formulate a model for a pendular line with costs dependent on speed and repositioning of empty containers. They solve their example problem with 20 Asian ports by a genetic algorithm. Chuang et al. (2010) illustrate their fuzzy genetic algorithm by a small five-port example. Their main message is that they manage to construct a good (‘‘optimal’’) liner route for their uncertain demand problem by using fuzzy set theory for the uncertainty part combined with a genetic algorithm for the discrete part. Takano and Arai (2011) describe a problem with focus on repositioning of empty containers. They use a multi route formulation where they generate routes by a genetic algorithm and allocate the cargo to the routes by linear programming. The model and algorithm are demonstrated on a case involving 11 major Asian ports. Sambracos et al. (2004) describe a problem where small containers are transported by coastal freight liners from the Greek mainland to the Greek islands. They use commercial software combined with a list based threshold accepting metaheuristic to find a set of good routes. Fagerholt (2004a) designs short routes for a fleet of ships such that each ship repeats its sailing every week. His model has one common loading depot and many discharging ports. A ship can sail several routes in a week if it has time to complete all the routes sequentially within a week. He solves his model by pre-generating all feasible routes that take less than a week for all ships. The real problem had 15 ports and five ships, while his largest test problem had 40 ports and 20 ships. Sigurd et al. (2005) discuss a problem of designing a set of routes (a network) between several ports on the west coast of Norway and Rotterdam. The network is planned to be serviced by newly built fast RoRo ships (in contrast to most of the papers reviewed which discuss container lines). The different ports need to be visited one or more times each week. The port call day(s) of the week is not important, but it needs to be the same day(s) each week. There are also rules regarding minimal time separation between port calls. This is handled by pre-generation of feasible weekly visit patterns for each customer port. They use column generation with some heuristic shortcuts to solve their model.

Lun and Browne (2009) try to find the best possible ship for each liner route managed by a shipping company. Then they analyse how a company’s results depend on its fleet mix. Since the demand fluctuates over time, it is useful to be able to switch ships between routes. Chen and Zeng (2010) study a network design problem with fluctuating demand. They use MIP models that are heuristically solved by a bi-level genetic algorithm. They use real geography and artificially generated demand in their tests. Meng and Wang (2011d) discuss a problem with fixed routes and several periods with different and uncertain demand. Their concern is how to change the fleet size (and mix) over time. They first formulate a scenario tree that they change to an acyclic graph by a common end node, before they solve their problem by dynamic programming. Their numerical example has three real routes.

## 2.1.2. Hub and feeder route models where each feeder port is connected to a single hub port

Hsu and Hsieh (2005) compare transportation through hubs (with transshipments) to direct transportation from origin to destination. They use more detailed specifications of both transportation and inventory costs than most other authors. After minimizing transportation and inventory costs individually, they try to find Pareto optimal solutions. In the end they get to the logical conclusion that direct transportation gets better and better as the volume between two ports increases. The same authors continue their work in Hsu and Hsieh (2007) where they add formulations of possible direct lines between some ports in different regions to their hub and spoke model.

Karlaftis et al. (2009) enhance the problem description of the small container problem in the Aegean Sea discussed by Sambracos et al. (2004) by adding transportation from the islands to the mainland and incorporating delivery time limits. They incorporate

25 islands in their pickup and delivery problem which they solve heuristically by a genetic algorithm. Takano and Arai (2009) propose a genetic algorithm for designing a hub and spoke network for container transport. Their hub and spoke problem is based on a fixed number of hubs, and each spoke is connected to a single hub. The locations of the hub ports are part of the decision. They test a few different values for the number of hub ports. They use their method on a case with 16 Asian ports in addition to Rotterdam and Los Angeles.

Gelareh et al. (2010) describe a model for hub locations in a hub and spoke network where the demand between two ports depends on the shipping price and the transit time. The authors suggest solving their MIP model by Lagrangian relaxation (LR) to get a decomposed model and then update the multipliers by a sub-gradient method. Meng and Wang (2011e) formulate a model for an intermodal hub and spoke network. Their formulation is solved by a hybrid genetic algorithm where they penalize violating capacity constraints. They illustrate their method with a numerical example from a region north of Singapore, where they use sea, rail and road links.

## 2.1.3. Models where some ports are classified as hub ports

Meng and Wang (2011a) discuss a network design problem with empty container repositioning. Their network has some interesting features upon which we wish to comment. They start with a pre-defined set of liner routes and their main concern is to decide which ones to use. Transshipment is allowed only in some hub ports. Most of the predefined routes visit both several hub ports and several feeder ports. Each feeder port is assigned to exactly one hub port. In order to reduce the number of possible routes for a container between two ports, a container is allowed to be transshipped at most twice between any two ports. Even if two feeder ports are assigned to different hub ports, there might be a direct route between them or there might be a route to the destination port that also visits the hub port assigned to the origin port. In these cases it is possible to ship with no, or just one, transshipment. Their model is solved by commercial software and they present results for 24 test cases.

Gelareh and Pisinger (2011) formulate a network design model for locating hub ports on a circular hub route and choosing the spoke and hub connections. They put an upper bound on how many hub ports a spoke port can be connected to. The model also deploys different ship types on the routes. They solve their model by decomposition following Bender’s principles in order to isolate the integer decisions from the flow decisions.

Reinhardt and Pisinger (2012) discuss a network design and a fleet allocation problem. The sailing frequencies might differ among routes. They also model the transshipment costs more accurately than most other authors in the network design phase. They use two types of routes: Normal single-loop routes and two-loop routes, which they call butterfly routes. For the second type of routes transshipments are allowed in the connecting center port. This results in a more flexible network. They formulate their problem as a MIP and show that commercial software is only able to solve small instances. They relax some of the complicating constraints and re-introduce the violated ones in a branch-and-cut framework. They show that their method works better than standard commercial software.

## 2.1.4. Multi route models without separation of hub and non-hub ports

Agarwal and Ergun (2008) describe a problem that does not partition the ports into hub ports and feeder ports as discussed earlier in this section. The same authors, Agarwal and Ergun (2010), discuss collaboration among two or more liner companies. They first use their former model to find the best overall solution, and then discuss some mechanisms to allocate the transportation work among the companies, including some monetary payments to make all companies better off.

Yan et al. (2009) describe a network design problem based on a practical case from Taiwan. They use a multi commodity flow model on a detailed time–space network (nodes for each hour in the planning period). They assume weekly departure for all lines. Their network has many layers: one for each combination of ship and liner route, and one for each origin–destination pair. They solve their problem by using LR to find lower cost bounds combined with heuristics to make infeasible LR solutions feasible again. By this relaxation, the model decomposes into several smaller (and easier) models. With artificial data they manage to find feasible solutions with objective gaps around one percent.

Imai et al. (2009) compare a single long multi-port route with a hub and spoke network. Container management costs, including repositioning of empty containers, are treated in both cases, and their results show that the multi-port route repositions a lot more containers than the hub and spoke network. They also analyse storage of containers in the ports. Álvarez (2009) points out that the model given by Agarwal and Ergun (2008) does not represent the transshipment cost in a satisfactory manner. He formulates a MIP model with better cost representation. This MIP model provides a linear multi commodity flow problem after fixing all integer variables. This model is solved by an interior point method. Tabu search is used to move between different integer solutions. New feasible routes are generated by column generation. Tests on artificial demand data and real geographical data show that the solution method works reasonably well.

## 2.2. Fleet deployment

Another important planning problem in liner shipping is fleet deployment, which is a tactical planning problem of assigning ships to liner routes. The planning horizon is typically a shipping season or up to 6 months. In this problem we assume that the liner routes to be serviced are defined by the network design stage discussed in Section 2.1. Even though the fleet of owned ships is given, a liner shipping company usually has some flexibility by chartering ships in or out. In case of over-capacity of tonnage, the shipping company may also have the possibility of laying up ships for (parts of) the planning horizon. In the following, we present a mathematical model for fleet deployment inspired by Powell and Perakis (1997) and Gelareh and Meng (2010). Then we review last decade’s literature on this topic.

It is assumed that the shipping company operates a heterogeneous fleet of ships, where the set of ship types is denoted by V. Let $N _ { \nu }$ be the number of available own vessels of type v in the fleet, while $N _ { \nu } ^ { I }$ represents the number of ships available in the market for chartering in. Each ship type has a given cargo carrying capacity $K _ { \nu }$ Further, let $C _ { \nu } ^ { I }$ and $C _ { \nu } ^ { 0 }$ be the cost of chartering in and out a ship of type v for the given planning horizon, respectively, while $C _ { \nu } ^ { L }$ is the daily lay-up cost for a ship of type v.

The set of predefined liner routes is denoted R and indexed by $r .$ Each route has a cumulative demand $D _ { r }$ for the whole planning horizon. A round-trip along a route is called a voyage. There is a service frequency requirement on each route, which can be translated into a required number of voyages to be performed during the planning horizon, $F _ { r } .$ Let $C _ { v r }$ and $T _ { v r }$ be the cost and time for performing a voyage on route r with a ship of type v, respectively, while $\bar { T } ^ { H }$ is the length of the planning horizon.

The following decision variables are defined: $x _ { v r }$ represents the number of voyages that ships of type v perform on route $r ;   n _ { v r }$ is the number of own ships of type v that are assigned to route $r ;$ $n _ { w } ^ { I }$ is the number of ships of type v that are chartered in for the planning horizon and deployed to route $r ; ~ n _ { \nu } ^ { o }$ is the number of own ships of type v that are chartered out for the planning horizon; $d _ { \nu }$ is the number of lay-up days for ships of type v.

The mathematical model for the fleet deployment problem can now be modelled as follows:

$$
\min \sum_ {v \in \mathcal {V}} \sum_ {r \in \mathcal {R}} \left(C _ {v r} x _ {v r} + C _ {v} ^ {I} n _ {v r} ^ {I}\right) + \sum_ {v \in \mathcal {V}} \left(C _ {v} ^ {L} d _ {v} - C _ {v} ^ {O} n _ {v} ^ {O}\right),\tag{8}
$$

$$
\text {s.t.} \sum_ {v \in \mathcal {V}} K _ {v} x _ {v r} \geqslant D _ {r}, \quad r \in \mathcal {R},\tag{9}
$$

$$
\sum_ {v \in \mathcal {V}} x _ {v r} \geqslant F _ {r}, \quad r \in \mathcal {R},\tag{10}
$$

$$
\sum_ {r \in \mathcal {R}} n _ {v r} \leqslant N _ {v}, \quad v \in \mathcal {V},\tag{11}
$$

$$
\sum_ {r \in \mathcal {R}} n _ {v r} ^ {l} \leqslant N _ {v} ^ {l}, \quad v \in \mathcal {V},\tag{12}
$$

$$
n _ {v} ^ {0} \leqslant N _ {v} - \sum_ {r \in \mathcal {R}} n _ {v r}, \quad v \in \mathcal {V},\tag{13}
$$

$$
T _ {v r} \boldsymbol {x} _ {v r} \leqslant T ^ {H} \left(n _ {v r} + n _ {v r} ^ {I}\right), \quad v \in \mathcal {V}, r \in \mathcal {R},\tag{14}
$$

$$
d _ {v} = T ^ {H} N _ {v} + \sum_ {r \in \mathcal {R}} T ^ {H} n _ {v r} ^ {l} - T ^ {H} n _ {v} ^ {0} - \sum_ {r \in \mathcal {R}} T _ {v r} x _ {v r}, \quad v \in \mathcal {V},\tag{15}
$$

(16)

$$
x _ {v r}, n _ {v r}, n _ {v r} ^ {I} \geqslant 0, \text {and integer,} v \in \mathcal {V}, r \in \mathcal {R},\tag{17}
$$

$$
n _ {v} ^ {0}, \quad d _ {v} \geqslant 0, \quad \text {and integer,} v \in \mathcal {V}.
$$

The objective function (8) consists of the sum of the costs for sailing the routes, chartering in ships, and laying up ships, minus the revenue from chartering out ships. Constraints (9) ensure that the demand is satisfied, while the frequency requirement is given by constraints (10). The availability of ships to use from own fleet and chartering-in is given by constraints (11) and (12), respectively. The number of ships that can be chartered out is limited by constraints (13). Constraints (14) ensure that the total time used on each route by each ship type is limited by the number of ships deployed to that route, while constraints (15) calculate the lay-up time. Finally, constraints (16) and (17) impose integer and non-negativity requirements on the variables.

The model above is a simplified version of the one presented by Gelareh and Meng (2010), though with a different notation. There, the authors incorporate speed decisions on sailing legs along each route. They also extend their model to let the service frequency on each liner route be a decision variable, and to handle the possibility of maximal travel time requirement between port pairs (e.g. in case of perishable products). Gelareh and Meng (2010) use a commercial MIP solver to solve the proposed model and test its performance on a number of randomly generated instances. Meng and Wang (2010) extend the model by Gelareh and Meng (2010) and consider uncertainty in container shipment demand. It is assumed that the demand between any two ports follows a normal distribution. The authors impose chance constraints for each liner service route in order to guarantee that the ships assigned to that route can satisfy the demand at least with a given probability. They use a commercial solver on a numerical example to assess the model and analyze the impact of the chance constraints and cargo shipment demand.

Later, Wang et al. (2011) pointed out that the formulation of the maximum number of voyages by Gelareh and Meng (2010) and Meng and Wang (2010) was incorrect and too optimistic for a short-term planning problem. Assume for a given ship type v and route r that $T ^ { H } = 1 2 0 \mathrm { d a y s }$ $T _ { v r }   =   3 5$ days, and $n _ { v r } + n _ { v r } ^ { I } = 3$ . Then, the maximum number of voyages performed is bounded by constraints (14) and (16) as $\begin{array} { r } { x _ { v r } \leqslant \left| \frac { T ^ { H } \left( n _ { v r } + n _ { v r } ^ { I } \right) } { T _ { v r } } \right| = 1 0 . } \end{array}$ . However, Wang et al. (2011) argue that each ship can only make $\begin{array} { r } { \left[ \frac { T ^ { H } } { T _ { v r } } \right] = 3 \; \mathsf { v o y a g e s } , } \end{array}$ which means that the maximum number of voyages on the given route performed by all ships of that type becomes $\begin{array} { r } { \frac { \boldsymbol { T } ^ { H } } { T _ { v r } } \left( \boldsymbol { n } _ { v r } + \boldsymbol { n } _ { v r } ^ { I } \right) = 9 . } \end{array}$ . They also suggest a reformulation of the fleet deployment model that improves the computational efficiency.

Usually, shipping companies plan sequentially, first the container flow and then the fleet deployment. Such a process is also assumed in the fleet deployment studies discussed above, which only implicitly deal with cargo flow management by aggregating the demand for each liner route. Liu et al. (2011) present a joint model for container flow management and fleet deployment. Their model is tested on a small numerical example, and it is argued that jointly considering these two aspects improves the overall solution. Wang and Meng (2012) propose a MIP model that accommodates container transshipment operations in ports. Computational studies on randomly generated networks based on the Asia–Europe– Oceania shipping network of a global liner shipping company show that the proposed model can be solved by commercial software.

Yet another study dealing with fleet deployment is by Zacharioudakis et al. (2011). They include sailing speed as a decision variable and show how their method can be used for what– if analysis for various demand scenarios.

The fleet deployment model and studies discussed above are all for container liner shipping. However, fleet deployment problems may vary among different segments of liner shipping, such as RoRo and container shipping operations. The model above relies on a number of assumptions that may be too restrictive in some cases and does not necessarily cover all important aspects of the problem. The most important limitations are probably (1) that each ship is assigned to only one single route during the whole planning horizon, and (2) that ships are considered as groups (ship types). The latter assumption can be a problem in short-term planning problems as it may result in solutions that are practically infeasible. This is because initial positions and/or ship ongoing voyages may restrict some ships from performing the number of voyages on the route that the model calculates. Fagerholt et al. (2009a) study the fleet deployment problem for a RoRo shipping company. In their model, each ship is modelled individually with a given initial open position and time for when it is available for new assignments. Each voyage on a liner route is also modelled explicitly with a time window in which the voyage must start. They suggest a multi-start local search heuristic to solve the problem. The heuristic, which is embedded in a prototype decision support system, was able to solve a real problem with 55 ships and 150 voyages over 4–6 month planning horizon. Tests indicated that they achieved 2–10% improvements over the shipping company’s solutions from manual planning.

## 2.3. Other liner shipping problems

This section considers liner shipping research that does not belong in the preceding two sections. Most of the studies in liner shipping reviewed above focus on cost minimization for the fleet operator. Álvarez (2012) claims that the level of service experienced by shippers is not properly addressed by such models, despite the fact that liner network design is increasingly driven by the shippers’ requirements. He uses the inventory holding cost, which is a linear function of the cargo’s transit time through the liner shipping network, to represent the shippers’ level of service. Further, he derives mathematical expressions to represent the total transit time for the cargo as a function of service route layout, vessel deployment and speed, cargo flow patterns, and service synchronization or transshipments. It is suggested that the inventory holding costs should be included in liner network design analysis in order to achieve a balance between fleet operating costs and level of service.

Another study that deals with level of service is presented by Meng and Wang (2011b) that consider a single long-haul container service route. Their aim is to determine the optimal operating strategy for the route, namely the optimal combination of service frequency, ships to be deployed to the route, and the sailing speed of the ships. These elements, as well as the interaction among them, clearly have an effect on the level of service. For example, lower service frequency and/or slower sailing speeds result in higher cargo transit times, and hence a poor service to the shipper, and vice versa. Meng and Wang (2011b) develop a mixed integer non-linear programming model for the problem, which they solve by a branch-and-bound method. In yet another study, Wang and Meng (2011) are concerned with level of service by considering transit time of the cargo that is transported. For the situation when the itineraries are given and cargo transshipment is allowed, they formulate a mathematical model for the schedule design and container routing. They propose a genetic local search heuristic for solving the problem, which is tested on the Asia–Europe–Oceania liner shipping services of a global liner company.

Lei et al. (2008) study various degrees of collaboration among container shipping companies. They distinguish between non-collaborative, slot-sharing (partial collaboration) and total-sharing (full collaboration) policies. The non-collaborative policy is the traditional way of operating with no collaboration between shipping companies. The slot-sharing policy assumes that a given percentage of the vessel capacity is exchanged between partner carriers, while in the total-sharing policy it is assumed that the partner carriers operate as one and share their demand and vessel resources. Lei et al. (2008) develop a MIP model and study the effect of the different operational policies using a large number of randomly generated test instances. The study shows that large cost savings can potentially be achieved if the partner carriers are willing to collaborate. Meng and Wang (2011c) develop a container flow simulation model for intermodal freight transportation systems. They mention assessing slot-sharing policies between liner carriers as one application of their model. Another application of their model for liner carriers is to predict revenue and market share when introducing a new liner service route. The simulation model is also reported to have been tested for estimating the impact on container throughput for the port of Singapore after Maersk stopped using that port as their South Asian transshipment hub.

The problem of determining the optimal cycle time (or service frequency) while balancing the business objectives for both the container shipping company and the port is studied by Boros et al. (2008). The port prefers to have short cycle times (or high frequency of service) to mitigate its empty container accumulation and land use problems, while the shipping company may want to have longer cycle times to reduce its costs. Chen et al. (2007) study an idealized container vessel scheduling problem for a fleet of homogeneous vessels used to transport containers between a single origin and a single destination port for a specified planning horizon.

Other important planning problems in liner shipping are the determination of optimal fleet and ship sizes. Lagoudis et al.(2010) presents a model to be used for determining optimal vessel and container fleet size, while Ng and Kee (2008) undertake an investigation in simulating the optimal containership sizes from the perspective of ship operators.

## 3. Industrial and tramp shipping

The mainstay of industrial and tramp shipping are (liquid or dry) bulk cargoes that are shipped in large quantities, such as: crude oil, coal, iron ore, grain, oil products, and chemicals. The main bulk commodities are usually shipped in full shiploads from their loading port to their destination port, whereas the minor ones may require multiple-stop routes. Among industrial (or tramp) cargoes we can also find a variety of semi-bulk commodities, such as cars, industrial equipment, produce (e.g. citrus, bananas, pineapples) and meat, some of which may be containerized.

Earlier research has focused on routing and scheduling of full shiploads, but in more recent papers we can find analysis of the more general case of multi-stop routes, and that is the focus of the model that we present in this section. We start with the strategic decision of fleet size and composition, move to the tactical problem of cargo routing and scheduling, and then discuss the specialized topics of maritime inventory routing (MIR) and Liquefied Natural Gas (LNG).

## 3.1. Fleet size and composition

In fleet size and composition the focus is on how to manage the fleet over time. This includes decisions about how many ships to buy, sell, charter-in, and charter-out, as well as the timing of these activities in order to meet demand. Decisions concerning fleet size and composition determine the ships available for deployment to routes. Hence one must also consider the deployment of the ships when deciding upon the fleet size and composition. This aspect is also emphasized by Hoff et al. (2010) that describe industrial aspects of combined fleet composition and routing in maritime and road-based transportation, and survey the literature in that area. Considering the large amounts of money invested in ships, the long lifetime of a ship (usually 20–30 years), and the large uncertainty involved in shipping, the importance of these decisions is evident. Despite this, very few studies can be found in the research literature that focus primarily on fleet size and composition decisions in industrial and tramp shipping.

One exception is presented by Zeng and Yang (2007) that describe a case study on developing a new ocean shipping system for coal transportation. They present an IP model for determining the optimal fleet and the routing of the vessels. A tabu search heuristic is then proposed for solving the model. Álvarez et al. (2011) extend this to also consider uncertainty in future demand and multiple time periods. They propose a MIP model for the multi-period fleet composition and deployment problem. In order to deal with demand uncertainty, they extend the model into a robust optimization model. This makes it possible to use the model to assist shipping companies with varying degrees of risk tolerance in deciding on the sale, purchase, chartering in and out, lay-up, and scrapping of ships, as well as the deployment of the active ships to contracts and geographic markets. Their model is tested on a realistic case study. We can also mention the work by Fagerholt et al. (2010a), in which a decision support methodology for general strategic planning is presented. A set of different strategic decisions can be evaluated through a simulation that incorporates optimization of the underlying ship routing and scheduling problem. Even though the case study shown in the paper did not include decisions regarding fleet size and composition, the authors argue that this is one alternate application of their methodology. Cheng and Duran (2004) discuss a similar application of their methodology for decision support to crude oil transportation that is based on discrete event simulation and optimal control.

## 3.2. Cargo routing and scheduling

We use the definition from Al-Khayyal and Hwang (2007) and distinguish between cargo routing and inventory routing. We use cargo routing to denote the planning problem of routing a fleet of ships to service a number of specified cargoes that are given as input to the planning process, in contrast to inventory routing where the cargoes are determined by the planning process itself (see Section 3.3). The term scheduling is used when the temporal aspect is brought into routing, i.e. when the time of the various events on a ship’s route is included. Cargo routing and scheduling is an important problem arising in industrial and tramp shipping. A cargo consists of a specified amount of product(s) to be picked up at a specified port, transported, and unloaded at a specified delivery port. There is usually a time window during which the loading of the cargo must start, and there may also be an unloading time window. The operator controls a heterogeneous fleet of ships that are available to transport the cargoes. For various reasons some cargoes may not be compatible with certain ships (e.g. due to loading and/or unloading ports draft limitations). Generally, the ship capacities and the cargo quantities are such that ships can carry multiple cargoes simultaneously. Whereas for major bulk commodities a cargo is usually a full shipload, for minor bulk commodities and chemicals, where the shipments are smaller, the ship capacity may accommodate several cargoes simultaneously. The model that follows reflects this more general case.

A ship operator in industrial shipping must transport all cargoes while minimizing costs, whereas a tramp operator focuses on profit maximization. The tramp operator usually has a set of mandatory contracted cargoes, and will try to increase its revenue by transporting optional spot cargoes. The mandatory cargoes come from long-term agreements between the shipping company and the cargo owners. The challenge for the tramp shipping company is to select spot cargoes and construct routes and schedules that maximize profit. Here, the profit is defined as the income from all transported cargoes minus the variable sailing costs, which mainly consist of fuel and port costs. We focus here on the tramp routing and scheduling problem, as this is the more general case, and it includes most of the characteristics of the corresponding industrial shipping problem. The problem that we discuss here in detail has similarities with the multi-vehicle pickup and delivery problem with time windows described by Desrosiers et al. (1995).

In the mathematical description of the tramp cargo routing and scheduling problem, let each cargo be represented by an index i. Associated with the pickup port of cargo i, there is a node i, and with the corresponding delivery port a node $n + i ,$ where n is the number of cargoes that can be transported during the planning horizon. Different nodes may correspond to the same physical port. Let $\mathcal { N } ^ { P } = \{ 1 , 2 , \ldots , n \}$ be the set of pickup nodes or cargoes, and let $\mathcal{N}^{D}=\left\{n+1,n+2,\cdots\right\}$ ; 2ng be the set of delivery nodes. The set of pickup nodes is partitioned into the sets $\mathcal { N } ^ { C }$ and $\mathcal { N } ^ { 0 }$ , which represent the pickup nodes corresponding to the contracted and optional cargoes, respectively. The set of ships in the fleet is denoted by $\mathcal { V } .$ A network $( \mathcal { N } _ { \nu } , \mathcal { A } _ { \nu } )$ is associated with each ship v. Here, $\mathcal { N } _ { \nu }$ is the set of nodes that can be visited by ship v, including an artificial origin and an artificial destination for ship v, o(v) and $d ( v ) ,$ respectively. Geographically, the origin can be either a port or a point at sea, while the artificial destination will be determined by the solution process and corresponds to the last delivery port for ship v. From these calculations, we can extract the sets $\mathcal { N } _ { \nu } ^ { P } = \dot { \mathcal { N } } ^ { P } \cap \mathcal { N } _ { \nu }$ and $\mathcal { N } _ { \nu } ^ { D } = \mathcal { N } ^ { D } \cap \mathcal { N } _ { \nu }$ consisting of the pickup and delivery nodes that ship v may visit, respectively. The set $\mathcal { A } _ { \nu }$ contains all feasible arcs for ship v, which is a subset of $\mathcal { N } _ { v } \times \mathcal { N } _ { v } .$

Let Q<sub>i</sub> be the quantity of cargo i, while $K _ { \nu }$ represents the capacity of ship v. For each arc, $T _ { i j v }$ is the sum of the calculated sailing time between nodes i and j by ship v and the service time at node i. Let $[ \underline { { T } } _ { i } , \overline { { T } } _ { i } ]$ denote the time window associated with node i, where Ti and $\overline { { T _ { i } } }$ are the earliest and latest time for start of service, respectively. The revenue for transporting cargo i is given by $R _ { i } .$ The transportation cost $C _ { i j v }$ consists of the sum of the sailing costs between nodes i and j and the port costs of node i for ship v.

The binary flow variable $\boldsymbol { \chi } _ { i j v }$ equals one if ship v sails from node i directly to node j, and zero otherwise. The variable $t _ { i \nu }$ represents the time at which service begins at node i, while $l _ { i \nu }$ represents the total load onboard ship v after the service is completed at node i. In order to simplify the model we assume that each ship is empty when leaving its origin and when arriving at the artificial destination, i.e. $l _ { o ( \it { v } ) \it { v } } = l _ { d ( \it { v } ) \it { v } } = 0 .$ In some cases, it might be possible to charter in a vessel from the spot market to transport a single cargo. We introduce a binary variable $y _ { i }$ that is equal to one if cargo i is transported by a spot charter, and zero otherwise, and an associated cost $C _ { i } ^ { S }$ for doing so.

The arc flow formulation of the tramp cargo routing and scheduling problem can now be stated as follows:

$$
\max \sum_ {v \in \mathcal {V}} \sum_ {(i, j) \in A _ {v}} (R _ {i} - C _ {i j v}) x _ {i j v} - \sum_ {i \in \mathcal {N} ^ {\mathcal {C}}} C _ {i} ^ {S} y _ {i},\tag{18}
$$

$$
\text {s.t.} \sum_ {v \in \mathcal {V}} \sum_ {j \in \mathcal {N} _ {v}} x _ {i j v} + y _ {i} = 1, \quad i \in \mathcal {N} ^ {C},\tag{19}
$$

$$
\left| \sum_ {v \in \mathcal {V}} \sum_ {j \in \mathcal {N} _ {v}} x _ {i j v} \leqslant 1, \quad i \in \mathcal {N} ^ {0}, \right|\tag{20}
$$

$$
\sum_ {j \in \mathcal {N} _ {v}} x _ {o (v) j v} = 1, \quad v \in \mathcal {V},\tag{21}
$$

$$
\sum_ {j \in \mathcal {N} _ {v}} x _ {i j v} - \sum_ {j \in \mathcal {N} _ {v}} x _ {j i v} = 0, \quad v \in \mathcal {V}, i \in \mathcal {N} _ {v} \setminus \{o (v), d (v) \},\tag{22}
$$

$$
\sum_ {i \in \mathcal {N} _ {v}} x _ {i d (v) v} = 1, \quad v \in \mathcal {V},\tag{23}
$$

$$
x _ {i j v} (l _ {v} + Q _ {j} - l _ {j}) = 0, \quad \boldsymbol {v} \in \mathcal {V},   j \in \mathcal {N} _ {v} ^ {p}, (i, j) \in \mathcal {A} _ {v},\tag{24}
$$

$$
x _ {i (n + j) \nu} (l _ {\nu} - Q _ {j} - l _ {(n + j) \nu}) = 0, \quad \nu \in \mathcal {V},   j \in \mathcal {N} _ {\nu} ^ {P},
$$

$$
(i, n + j) \in \mathcal {A} _ {v},\tag{25}
$$

$$
0 \leqslant l _ {i v} \leqslant K _ {v}, \quad v \in \mathcal {V}, i \in \mathcal {N} _ {v} ^ {P},\tag{26}
$$

$$
x _ {i j \nu} (t _ {i \nu} + T _ {i j \nu} - t _ {j \nu}) \leqslant 0, \quad \nu \in \mathcal {V}, (i, j) \in \mathcal {A} _ {\nu},\tag{27}
$$

$$
\sum_ {j \in \mathcal {N} _ {v}} x _ {i j v} - \sum_ {j \in \mathcal {N} _ {v}} x _ {(n + i) j v} = 0, \quad v \in \mathcal {V}, i \in \mathcal {N} _ {v} ^ {P},\tag{28}
$$

$$
t _ {i v} + T _ {I (n + i) v} - t _ {(n + i) v} \leqslant 0, \quad v \in \mathcal {V}, i \in \mathcal {N} _ {v} ^ {p},\tag{29}
$$

$$
\underline {{T}} _ {i} \leqslant t _ {i v} \leqslant \overline {{T}} _ {i}, \quad v \in \mathcal {V}, i \in \mathcal {N} _ {v},\tag{30}
$$

$$
y _ {i} \in \{0, 1 \}, \quad i \in \mathcal {N} ^ {c},\tag{31}
$$

$$
x _ {i j v} \in \{0, 1 \}, \quad v \in \mathcal {V}, (i, j) \in A _ {v}.\tag{32}
$$

The objective function (18) maximizes the profit from operating the fleet, while constraints (19) state that all mandatory contract cargoes are transported, either by a ship in the fleet or by a spot charter. The corresponding requirements for the optional spot cargoes are given by constraints (20). Here, we have assumed that spot charters can only be applied to contract cargoes. Constraints (21)– (23) describe the flow on the sailing route used by ship v. Constraints (24) and (25) keep track of the load onboard at each pickup and delivery node, respectively. In constraints (26), it is ensured that the load onboard does not exceed the ship capacity. The lower (upper) bound is only needed in unloading (loading) ports. Constraints (27) describe the compatibility between routes and schedules. Coupling constraints (28) ensure that if ship v visits the pickup node $i ,$ the same ship must also visit the corresponding delivery node n + i. The precedence requirements, forcing pickup node i to be visited before the corresponding delivery node $n + i ,$ are given by constraints (29). The time windows are stated by constraints (30), while constraints (31) and (32) impose binary requirements on the spot charter and flow variables, respectively.

The tramp cargo routing and scheduling problem formulated by (18)–(32) was studied by Brønmo et al. (2007a) that suggest a multi-start local search heuristic to solve the problem. Its performance is compared with a path flow formulation where all feasible ship routes are generated a priori. The study shows that optimal or near-optimal solutions are obtained within reasonable time on eight real life planning problems from four different shipping companies. Korsvik et al. (2010) propose a unified tabu search heuristic, which, in contrast to the heuristic in Brønmo et al. (2007a), allows infeasible solutions with respect to ship capacity and time window constraints during the search. The tabu search heuristic performs better than the heuristic by Brønmo et al. (2007a), especially for large and tightly constrained problems. In a recent paper, Malliappi et al. (2011) present a variable neighbourhood search heuristic for the same problem. Due to the lack of real or benchmark cases from tramp shipping, they modify benchmark problems from land transportation. Their heuristic is compared with their own implementations of the multi-start local search heuristic by Brønmo et al. (2007a) and the unified tabu search heuristic by Korsvik et al. (2010). The results show that the variable neighbourhood search on average has the best performance among the three heuristics.

A tramp routing and scheduling problem for a shipping company engaged in shipping bulk liquid chemicals in the Asia Pacific region is studied by Jetlund and Karimi (2004). They present a MIP formulation of their problem and propose a heuristic decomposition algorithm that obtains the fleet schedule by repeatedly solving the formulation for a single ship. The method is tested on a real problem involving 10 tankers and 79 cargoes, and the results obtained showed a profit increase of 32.7% compared to a manually derived plan. Lin and Liu (2011) also consider a real tramp ship routing and scheduling problem for a shipping company operating seven handy-max dry bulk vessels for transportation of various types of dry cargoes in simple packaging (e.g. steel coils, wood pulp or stone). They suggest a genetic algorithm to solve the problem and show that it outperforms solving a mathematical formulation of the problem by commercial software. Both Jetlund and Karimi (2004) and Lin and Liu (2011) proposed different modelling approaches for their problems than our formulation (18)–(32).

Often, real life problems include aspects that are important but not included in our model formulation (18)–(32). For example, bulk cargoes are frequently shipped on a recurrent basis under long-term contracts. In such cases the exact cargo size is not that important and the ship operator may have some flexibility in the size of the cargo. Normally there is a target cargo size with allowed variability around it (e.g. 20,000 tons ±10%). Then, the problem also includes determining the optimal size of each cargo to transport (within its interval). Such a problem is studied by Brønmo et al. (2007b, 2010) and Korsvik and Fagerholt (2010). These studies show that this flexibility can be utilized to significantly improve the profit (e.g. reducing the size of some cargoes in order to free enough ship capacity to carry additional spot cargoes by the controlled fleet). Brønmo et al. (2007b) give a mathematical formulation of the tramp ship routing and scheduling problem with flexible cargo sizes. They solve a path flow formulation where all feasible ship routes are generated a priori and optimized with respect to the cargo quantities. Eight small to medium size cases from two different shipping companies are solved, of which their solution method is able to find optimal solutions only to six cases. For the larger cases this method becomes intractable due to the exponential increase in the number of feasible ship routes, and hence variables, when the problem size increases. Therefore, Brønmo et al. (2010) suggested a dynamic column generation scheme where ship routes are generated as needed. However, they have to discretize the cargo quantities, which turns the solution method into a heuristic column generation approach. They expanded the set of test problems to 10 cases from the same companies, including the six cases from the initial set. Korsvik and Fagerholt (2010) developed a tabu search algorithm for the same problem, and show that very good solutions are obtained with their method within reasonable time.

Kobayashi and Kubo (2010) study a real-world industrial tanker routing and scheduling problem where the ports are closed for loading or unloading operations during nights. In such a case, when the time windows span several days, they can be converted into multiple time windows. In their problem one also has to consider the allocation of cargoes to multiple compartments onboard the tankers. Kobayashi and Kubo (2010) propose a column generation method on a time–space network to solve the problem. Yet another problem motivated by a real-world application is studied by Li and Pang (2011), and Pang et al. (2011). Their problem does not involve time windows for the cargoes. However, since each terminal/berth can only handle one vessel at a time, they need to assign a time slot to each vessel loading/unloading task so as to avoid time clashes. They propose a heuristic algorithm for the problem using set partitioning formulation and column generation techniques.

Project shipping presents another real-life problem where the allocation (stowage) of cargoes to ship compartments must be considered. Project shipping involves large pieces of equipment that are hard to stow, and cargoes may be related (e.g. must be delivered together). Fagerholt et al. (2011) studied a project shipping problem where they consider cargo coupling constraints (in addition to stowage), which means that some spot cargoes cannot be accepted individually, but rather as sets, namely, if one spot cargo is accepted, one must also accept the other cargo(es) in the set. They propose a tabu search heuristic, which is a modified version of the one presented in Korsvik et al. (2010). A similar problem from project shipping without the stowage constraints, but with synchronization of the delivery of some cargoes, is studied by Andersson et al. (2011b). They propose three alternate solution methods based on path flow formulations and a priori column generation. In one of the solution methods this is combined with a scheme for relaxing the complicating synchronization constraints and reintroducing them dynamically when needed.

In most of the literature on ship routing and scheduling a cargo cannot be transported by more than one ship. By introducing split loads this restriction is removed and a cargo may be split among several ships. This problem was recently studied by Andersson et al. (2011a) and Korsvik et al. (2011). Andersson et al. (2011a) suggest a solution method based on a priori generation of single ship routes and two alternate path flow models that deal with the selection of ship schedules and assignment of cargo quantities to the schedules. Computational results show that the solution method can provide optimal solutions only to realistic problems of small sizes. In order to overcome this limitation Korsvik et al. (2011) proposed a large neighbourhood search heuristic for the same problem, which is able to find optimal solutions to the same instances as Andersson et al. (2011a) within a short time, as well as solving larger problems. Both papers show that utilizing split loads can result in improved utilization of the fleet, and hence significantly increased profit.

Another problem where splitting cargoes can be important is in crude oil tanker routing and scheduling. Hennig et al. (2011) present an extensive mathematical formulation to illustrate various aspects of the problem. One characteristic of the problem is that in contrast to the problem discussed above there are no predefined cargoes. There is rather a quantity requirement for each crude grade that must be picked up at each loading port within some (rather wide) time window. This quantity may be picked up by several tankers. Similarly, there are quantity requirements also for the delivery ports, which can also be satisfied by deliveries from more than one tanker (or more than one source). These pickup and delivery requirements are not paired into cargoes beforehand, which results in a problem with split pickups and split deliveries. Logically, this problem lies between inventory routing, where production and/or consumption rates are specified and is less restricted (see Section 3.3), and ship routing and scheduling (where cargoes are specified). This problem emulates the planning process of oil companies where first comes crude planning, then its shipping. The time windows (weeks, month) correspond to the crude planning time buckets. Hennig et al. (2012) propose a path flow model with a priori route generation for the problem in Hennig et al. (2011), though omitting some of the complicating aspects. They introduce continuous variables to distribute the cargo among the different routes. It is demonstrated that small realistic instances can be solved to optimality.

Fagerholt (2004b) and Fagerholt and Lindstad (2007) present a decision support system (DSS) for ship routing and scheduling, in which the heuristics from Brønmo et al. (2007a), Korsvik et al. (2010, 2011), and Korsvik and Fagerholt (2010) are incorporated in the problem solver. One experience from designing such systems (from Fagerholt (2004b)) is the importance of interaction between the DSS and the user, in contrast to focusing on the optimization algorithm alone. Therefore, Fagerholt et al. (2009b) claim that planners often are interested in a set of high-quality diverse solutions to choose from instead of only one (near-) optimal solution to the model as usually provided by a DSS. Further, ship routes and schedules are generated following a rolling horizon, where schedules are updated when new relevant information appears. Since planners often have made commitments to customers, for example regarding arrival times, the planners are also interested in schedules that are close to the current (baseline) schedule. Fagerholt et al. (2009b) suggest a solution method that includes a persistence penalty function and distance measures to produce such schedules.

Kang et al. (2012) and Jung et al. (2011) present a DSS for a car carrier. In this problem, the objective is to determine the number of cars to allocate to each vessel and the vessel routes, while minimizing the transportation costs. The car production schedule must be considered when planning, and it is assumed that cars that have not been transported during the planning period are carried forward to the next period, though at a penalty cost. A genetic algorithm is proposed to solve the problem.

There are also a few other variants of industrial or tramp cargo routing and scheduling problems studied in the literature. Hwang et al. (2008) deal with a tramp routing and scheduling problem where all cargoes are assumed to be full shiploads, i.e. only one cargo can be onboard the ship at the same time. In contrast to the other studies discussed above, they consider volatility in the shipping market with respect to ship chartering rates and revenues for transporting spot cargoes. They present a set packing model that limits risk using a quadratic variance constraints, which they solve by a branch-and-price-and-cut algorithm. Computational results show that the profit variance can be significantly reduced with a reasonable increase in expected cost.

There are also some studies where speed decisions have been incorporated in the routing and scheduling of ships (e.g. Norstad et al., 2011). These will be discussed in Section 4.

## 3.3. Maritime inventory routing and supply chains

In maritime supply chains, sea transportation constitutes at least one vital link. A classical maritime supply chain starts with extraction of raw materials, transportation of the materials to processing facilities, storage at these facilities, processing the materials, storage of the processed products and finally transportation and storage at a customer’s site. When large volumes are transported over long distances, maritime transportation is the obvious choice. For example, in the petroleum industry maritime transportation is used both upstream and downstream in the supply chain (into and out of refineries). A maritime inventory routing (MIR) problem is defined as a planning problem where an actor has the responsibility for both the inventory management at one or both ends of the maritime transportation legs, and for the ships’ routing and scheduling. In practice, the actor responsible for the coordinated MIR planning can either be the producer, consumer or the shipping company, depending on the type of business. For instance, vertically integrated companies are often responsible for the maritime transportation themselves. Most of this section will be devoted to MIR, but it will also discuss contributions covering a wider scope of maritime supply chains.

The basic MIR problem concerns the transportation of a single product. The product is stored at given loading (production) ports and transported by sea to inventories at unloading (consumption) ports. Inventory storage capacities are defined in all ports and we assume that the production and consumption rates are given in all ports. A heterogeneous fleet of ships is used to transport the product. Each ship has a given capacity and sailing speed. The ships can wait outside a port before entering for (un)loading. A ship can both load and unload at multiple ports in succession. The initial position and load on board each ship is known at the beginning of the planning horizon. The sailing costs, waiting costs and port costs are all ship-dependent. The goal of the MIR problem is to design routes and schedules for the fleet that minimize the costs of delivering the product, and determine the (un)loading quantity at each port visit without exceeding the storage capacities. Depending on the operational context the typical planning horizon may span from 1 week up to several months. Inventory carrying costs are usually not considered because the inventory at both ends of the shipping legs belongs to the same organization.

As discussed in Section 3.2, classical cargo routing is often performed under tight constraints. Each cargo is specified by a given loading and unloading port and the sizes of the cargoes are given with no (or little) flexibility. In addition, there might be tight time windows. In contrast, the MIR problem has no predetermined number of calls at a given port during the planning horizon, neither is the quantity to be (un)loaded at each port call. There is also no predefined pickup and delivery pairing in the MIR problem. Normally, time windows are not given explicitly, but these can be calculated based on the inventory availability. However, these time windows will often become very wide especially towards the end of the planning horizon. The combination of inventory management and ship routing and scheduling makes MIR a very complex problem to solve.

By coordinating these planning challenges it is possible to achieve monetary benefits, flexibility in services and improved robustness. This has resulted in increased attention towards MIR both in the operations research community and the industry. These activities have formed the basis of several surveys in the last decade: Christiansen et al. (2007), Christiansen and Fagerholt (2010), and Andersson et al. (2010b). In the first two surveys a MIR model based on continuous time variables was presented. During the last decade we have also seen several MIR models based on discrete time units. Therefore, we decided to present a basic discrete time MIR model here. Dissimilar to the models presented in the previous surveys, we make the following assumptions in order to present a simple model and focus on the main structure of the model: (1) The (un)loading takes one time period independent of the (un)- loaded quantity, (2) Berth capacities per time period are defined, but no interarrival gap between arrivals in the same port is specified, and (3) A ship waiting cost is introduced.

In the mathematical description of the discrete time MIR problem we use the notation from Section 3.2 and define here only the additional new notation. For the indices, let T , indexed by t, be the set of time periods in the planning horizon. Additional parameters are as follows: The berth capacity (in number of ships at port i in time period t) is given by $B _ { i t \bullet }$ The levels of the inventory (or stock) have to be within a given interval at each port and time period, $[ \underline { { S } } _ { i t } , \overline { { S } } _ { i t } ]$ . The initial inventory level in port i is given by $S _ { i } ^ { 0 } .$ . The production rate $P _ { i t }$ is positive if port i is producing the product in period t, and negative if port i is consuming the product in period t. Further, constant I<sub>i</sub> is equal to 1 if i is a loading port, 1 if i is an unloading port and 0 if i is $o ( v )$ or d(v). In contrast to the definition in Section 3.2, the parameter $T _ { i j v }$ is here the sailing time (in an integer number of time periods) between port i and port j by ship v and does not include the (un)loading time. Finally, let $C _ { \nu } ^ { W }$ be the waiting cost for ship v per time period.

In the mathematical formulation we use the following types of variables: the binary flow variable $x _ { i j v t } , ~ \pmb { \nu } \in \mathcal { V } , ~ ( \pmb { i } , \pmb { j } ) \in \mathcal { A } _ { \nu } , ~ t \in \mathcal { T }$ equals 1, if ship v operates in port i in period t and then sails directly from port i to port j, and 0 otherwise. The binary waiting variable $w _ { i v t } , ~ v \in \mathcal { V } , ~ i \in \mathcal { N } _ { v } , ~ t \in \mathcal { T }$ equals 1, if ship v waits outside port i in period t, and 0 otherwise. Variable $l _ { \nu t } , \nu \in \mathcal { V } , t \in \mathcal { T }$ gives the total load on board ship v at the end of time period t, while variable $q _ { i v t } , \quad v \in \mathcal { V } , \quad i \in \mathcal { N } _ { v } , \quad t \in \mathcal { T }$ represents the quantity (un)loaded at port i by ship v in time period t. Finally, $s _ { i t } , ~ i \in \mathcal { N } , ~ t \in \mathcal { T }$ represents the inventory (or stock) level in port i at the end of time period t. It is assumed that nothing is loaded or unloaded at the artificial origin o(v). The ships may have cargo on board, $L _ { \nu } ^ { 0 } ,$ at the beginning of the planning horizon.

The arc flow formulation of the discrete time maritime inventory routing problem for a single product is as follows:

$$
\min \sum_ {v \in \mathcal {V}} \sum_ {(i j) \in \mathcal {A} _ {v}} \sum_ {t \in \mathcal {T}} C _ {i j v} x _ {i j v t} + \sum_ {v \in \mathcal {V}} \sum_ {i \in \mathcal {N} _ {v}} \sum_ {t \in \mathcal {T}} C _ {v} ^ {W} w _ {i v t},\tag{33}
$$

$$
\text {s.t.} \sum_ {j \in \mathcal {N} _ {v}} \sum_ {t \in \mathcal {T}} x _ {o (v) j v t} = 1, \quad v \in \mathcal {V},\tag{34}
$$

$$
\sum_ {j \in \mathcal {N} _ {v}} x _ {j i v, t - T _ {j i v ^ {- 1}}} + w _ {i v, t - 1} - \sum_ {j \in \mathcal {N} _ {v}} x _ {i j v t} - w _ {i v t} = 0, \quad v \in \mathcal {V},
$$

$$
i \in \mathcal {N} _ {v} \setminus \{\boldsymbol {o} (\boldsymbol {v}), \boldsymbol {d} (\boldsymbol {v}) \}, t \in \mathcal {T},\tag{35}
$$

$$
\sum_ {i \in \mathcal {N} _ {v}} \sum_ {t \in T} x _ {i d (v) v t} = 1, \quad v \in \mathcal {V},\tag{36}
$$

$$
\sum_ {v \in \mathcal {V}} \sum_ {j \in \mathcal {N} _ {v}} x _ {i j v t} \leqslant B _ {i t}, \quad i \in \mathcal {N}, \quad t \in \mathcal {T},\tag{37}
$$

$$
0 \leqslant q _ {i v t} \leqslant \min \left\{K _ {v}, \bar {S} _ {i t} \right\} \sum_ {j \in \mathcal {N} _ {v}} x _ {i j v t}, \quad v \in \mathcal {V},
$$

$$
i \in \mathcal {N} _ {v} \setminus \{\boldsymbol {o} (\boldsymbol {v}), \boldsymbol {d} (\boldsymbol {v}) \}, t \in \mathcal {T},\tag{38}
$$

$$
s _ {i, t - 1} - \sum_ {v \in \mathcal {V}} I _ {i} q _ {i v t} - s _ {i t} + P _ {i t} = 0, \quad i \in \mathcal {N}, t \in \mathcal {T},\tag{39}
$$

$$
\underline {{S}} _ {i t} \leqslant s _ {i t} \leqslant \overline {{S}} _ {i t}, \quad i \in \mathcal {N}, \quad t \in \mathcal {T},\tag{40}
$$

$$
s _ {i 0} = S _ {i} ^ {0}, \quad i \in \mathcal {N},\tag{41}
$$

$$
\left| l _ {v, t - 1} + \sum_ {i \in \mathcal {N} _ {v}} I _ {i} q _ {i v t} - l _ {v t} = 0, \quad v \in \mathcal {V}, t \in \mathcal {T}, \right.\tag{42}
$$

$$
0 \leqslant l _ {v t} \leqslant K _ {v}, \quad v \in \mathcal {V}, t \in \mathcal {T},\tag{43}
$$

$$
l _ {v 0} = L _ {v} ^ {0}, \quad v \in \mathcal {V},\tag{44}
$$

$$
x _ {i j v t} \in \{0, 1 \}, \quad v \in \mathcal {V}, (i, j) \in A _ {v}, t \in \mathcal {T},\tag{45}
$$

$$
w _ {i v t} \in \{0, 1 \}, \quad v \in \mathcal {V}, i \in \mathcal {N} _ {v}, t \in \mathcal {T}.\tag{46}
$$

The objective function (33) minimizes the sailing, port and waiting costs. Constraints (34)–(36) are the flow conservation constraints. Note that the sailing from o(v) starts in period t + 1 in (34), and constraints (35) state that ship v is operating at port i in period t. The berth capacities are given in constraints (37). Constraints (38) ensure that a ship cannot (un)load if it is not operating in a port and defines the upper bound on the quantity (un)loaded. The inventory balances are expressed in constraints (39). Constraints (40) define the upper and lower inventory limits and Eq. (41) state the initial inventory level. The equilibrium of the quantity on board the ship is given in constraints (42)–(44). Finally, the binary requirements on the flow and waiting variables are imposed in constraints (45) and (46), respectively. A variant of model (33)–(46) is presented by Song and Furman (2010). However, their model is more general in the sense that many practical requirements can be incorporated into the model and several of these are discussed there.

Most of the MIR problems reported in the literature are from transportation of liquid bulk products. Particularly, single product

MIR problems are studied for transportation of petroleum products (e.g. Sherali and Al-Yakoob, 2006a,b; Song and Furman, 2010). For example, Furman et al. (2011) present an industrial MIR problem for the transportation of vacuum gas oil. In addition, ammonia is also often considered as a single product for distribution planning purposes, see for instance (Christiansen and Nygreen, 2005). Previously, the focus within MIR was devoted to single-product studies. More recently we have witnessed an increasing attention to multi-product MIR problems, where especially the chemical and petroleum industries have many challenges. Al-Khayyal and Hwang (2007) consider the transportation of petrochemicals, Persson and Göthe-Lundgren (2005) deal with bitumen products, while Li et al. (2010) study different types of chemicals. Further on, we can find multi-product MIR challenges in the cement industry (Christiansen et al., 2011), wheat (Bilgen, 2007; Bilgen and Ozkarahan, 2007), pulp (Bredström et al., 2005; Gunnarsson et al., 2006; Andersson, 2011) and calcium carbonate slurry (Dauzère-Pérès et al., 2007).

The allocation of the various products to the ship’s compartments might be a relevant issue when considering multi-product MIR. Normally, ships have multiple compartments to keep products separated. Both, Al-Khayyal and Hwang (2007) and Li et al. (2010) assume that compartments are dedicated to specific products. This means that it is not permissible to assign a product to a compartment that has been used previously by another product. Christiansen et al. (2011) and Siswanto et al. (2011) relax the problem to consider an assignment of multi-undedicated compartments to products. Most MIR and supply chain studies do not consider the allocation of products to compartments and assume that this problem can be solved by the people responsible for stowage, or as a separate planning problem.

In model (33)–(46), we describe the general MIR case with a network structure consisting of many production and consumption ports. However, some real MIR problems concern inventory constraints at just one of the port types, either in the production ports or the consumption ports. In addition, there might be just one central producer or one central customer. Sherali and Al-Yakoob (2006a) handle the problem of determining the optimal fleet mix and schedules for a problem with a single source and destination, while in Sherali and Al-Yakoob (2006b) they extend the problem to multiple sources and destinations. In contrast to the basic MIR problem, Rakke et al. (2011) present an LNG shipping problem with one central producer with inventory considerations and many customers with no inventory considerations but rather contract requirements. Similarly, the transportation of calcium carbonate slurry products by Dauzère-Pérès et al. (2007) starts at a central producer, but here the inventory is managed at the unloading ports. Several studies present problems with a limited number of loadings or unloadings in succession. Bilgen (2007) and Bilgen and Ozkarahan (2007) define paths with at most two loading ports and one unloading port. In contrast, in the LNG study by Grønhaug and Christiansen (2009) LNG ships are always loaded to capacity but a ship may unload at two regasification terminals in succession.

The nature of the production and consumption rates affects the underlying model. These rates correspond to $P _ { i t }$ in model (33)–(46). If it is assumed that the production and consumption rates are fixed and constant during the planning horizon, then a mathematical model based on continuous time is often used (e.g. Christiansen and Nygreen, 2005; Al-Khayyal and Hwang, 2007; Siswanto et al., 2011). When the production and/or consumption rate is varying during the planning horizon, a discrete time model is applied (e.g. Persson and Göthe-Lundgren, 2005; Sherali and Al-Yakoob, 2006a,b; Bilgen, 2007; Bilgen and Ozkarahan, 2007; Song and Furman, 2010; Andersson, 2011; Furman et al., 2011). Li et al. (2010) formulate a continuous time model, but in addition introduce time slots. These time slots increase the computational efficiency. However, the model assumes constant rates.

The solid growth in demand for and production of Liquefied Natural Gas (LNG) during the last decade has resulted in a significant increase in the LNG shipping fleet capacity. In addition, the size of LNG ships is also increasing. This has resulted in a recent increased focus in the literature on managing and optimizing the LNG supply chain. For transportation purposes natural gas is cooled down and pressurized to reach a liquid state (LNG). This process reduces the volume of the gas by a factor of 610 and facilitates its transportation and storage, but vastly increases the cost of LNG handling facilities and makes them scarce. In most of the studies in the literature, the focus is on inventory management at the liquefaction plants and the regasification terminals, as well as on routing and scheduling the LNG ships. The most general study of the LNG supply chain, including some of its main characteristics, is presented in Andersson et al. (2010a).

The LNG inventory routing problem (LNG-IRP) was presented by Grønhaug and Christiansen (2009). The problem includes decisions concerning the routing and scheduling of the LNG ships as well as the inventory management at both the liquefaction plants and the regasification terminals. The hold of the LNG ships is separated into several cargo tanks. The ships are always loaded to capacity, but it is possible to unload at a destination only some of the tanks. During a voyage some of the LNG evaporates and this gas, called boil-off, is used to fuel the ship. This boil-off effect complicates the model considerably. In addition, the production and consumption of LNG are represented by variables (and not as parameters as in the basic MIR problem). Both an arc flow and a path flow model with pregenerated paths are formulated and solved. The same problem is studied in Grønhaug et al. (2010), but there a branch-and-price method is used to solve the problem.

Fodstad et al. (2010) and Uggen et al. (2011) study a richer version of the LNG-IRP that also includes contract management and trading in a spot market. In addition, the ‘‘fully loaded’’ industry policy is relaxed and the relaxed solution is more profitable in some situations. An arc based formulation is developed and solved by Fodstad et al. (2010), while Uggen et al. (2011) provide a heuristic method based on fix-and-relax time decomposition for the same formulation.

Another planning problem within the LNG business is the Annual Delivery Program (ADP) setup. The ADP for an actor in the LNG supply chain is the complete sailing schedule of the ships in the fleet for the coming year. Rakke et al. (2011) and Stålhane et al. (2012) study the ADP planning problem for one of the world’s largest producers of LNG. The producer is responsible for the LNG inventories at the single liquefaction plant, the loading port with a limited number of berths, and the routing and scheduling of a fleet of LNG ships. In addition, the producer has to fulfill a set of long-term contracts to customers all around the world. The objective is to design an ADP to fulfill the long-term contracts at minimum cost, while maximizing revenue from selling LNG in the spot market. Two types of LNG are produced at the liquefaction plant. The network structure is simple compared to other MIR problems as there is only one liquefaction plant and several regasification terminals. In addition, the ships are always fully loaded and unloaded. This means that the multiple products do not complicate the problem and the boil-off does not need to be considered. However, the length of the planning horizon and the size of the problem make it very difficult to solve. Rakke et al. (2011) formulated a MIP model with voyage variables for each ship, customer contract and time period. The model is incorporated in a rolling horizon heuristic (RHH). Stålhane et al. (2012) solve the same problem by use of a multi-start local search heuristic. The greedy heuristic solution is improved using either a first-descent neighbourhood search, branch-and-bound on a mathematical formulation, or both. A similar MIP-based improvement heuristic is also used to improve the ADPs produced by the RHH. Halvorsen-Weare and Fagerholt (2010) study a similar problem where cargoes with defined time windows are pregenerated for each contract. The problem is decomposed into a routing subproblem and a scheduling master problem where berth, inventory and scheduling decisions are handled. The master problem is solved using branch-and-bound, while the subproblems are solved using either a local search heuristic or branch-and-bound.

LNG shipping presents several additional challenges beyond the coordinated planning of inventories and routes. LNG is a hazardous material and even though the probability for an accident is low, the consequences could be dramatic. Therefore hazmat routing is highly relevant in this context, especially considering the risks when sailing close to coastal towns. Bubbico et al. (2009) present a preliminary risk analysis for LNG tankers approaching a maritime terminal.

Some studies include supply chain activities beyond the MIR problem. For instance, Persson and Göthe-Lundgren (2005) include process scheduling at oil refineries (production ports), while Bilgen (2007) and Bilgen and Ozkarahan (2007) address bulk grain blending. Bredström et al. (2005), Fodstad et al. (2010) and Andersson (2011) extend the supply chain to the customer side.

The literature provides a few maritime supply chain optimization studies that are not focused on inventory considerations. Gunnarsson et al. (2006) consider a combined terminal location and ship routing problem for a pulp producer. The purpose is to supply the customer’s annual demand for pulp products while minimizing the distribution costs. The ship routes go from the pulp mills to terminals and further onto customers by other modes of transportation. Another such study by Liu (2008) concerns the optimal blending and annual distribution of coal fuel from overseas coal sources via ports to domestic power plants.

Many of the studies in the literature formulate a MIP model and use this model in various solution approaches. Arc flow models (such as model (33)–(46)) are used in branch-and-cut approaches (e.g. Song and Furman, 2010; Furman et al., 2011). Song and Furman (2010) solve subproblems that are restricted versions of the original problem, by branch-and-cut. These subproblems are solved iteratively in a large neighbourhood search heuristic. Arc flow models are also solved by metaheuristic-based algorithms as in Dauzère-Pérès et al. (2007). Siswanto et al. (2011) combine an arc flow model with a heuristic. Bredström et al. (2005) developed a hybrid algorithm based on a genetic algorithm and linear programming. Finally, Sherali and Al-Yakoob (2006b) use a rolling horizon heuristic based on an arc flow model. Path flow models, where the path is described by the route and/or schedule, are used in branch-and-price methods (e.g. Persson and Göthe-Lundgren, 2005; Andersson, 2011), rolling horizon heuristics (Rakke et al., 2011) and various fix and relax heuristics (Gunnarsson et al., 2006; Bilgen, 2007). Pure heuristics are also used to solve complicated MIR problems, and Christiansen et al. (2011) developed a construction heuristic that was embedded in a genetic algorithmic framework.

Almost no studies are concerned with the uncertainty in the parameters of the MIR problem. However, both Rakke et al. (2011) and Sherali and Al-Yakoob (2006a,b) introduce penalty functions for deviating from the customer contracts and the storage limits, respectively. Christiansen and Nygreen (2005) introduce soft inventory levels to handle uncertainties in sailing time and time in port, and these levels are transformed into soft time windows.

In recent years, we have seen the beginning of successful implementation stories of decision support systems (DSSs) for MIR. Dauzère-Pérès et al. (2007) report the development of a DSS for Omya Hustadmarmor and Furman et al. (2011) describe a DSS for feedstock routing in the ExxonMobil downstream sector. The LNG model developed by Fodstad et al. (2010) is used by Statoil and GDF SUEZ.

## 4. Sailing speed, bunkering and emissions

Two main trends have brought the issue of bunker fuel management to the forefront in recent years. One is the steep increase in bunker fuel price that accompanied the surge in crude oil price, and the other is the increasing attention to environmental impacts. A vessel may use tons of bunker fuel per day (over 150 tons per day for a large vessel), and at 500–600 USD per ton bunker fuel cost is the majority of the vessel operating expenses. Bunker fuel is a heavy fuel that emits a high amount of air pollutants per ton used, and the amount of emissions is proportional to the quantity of bunker and auxiliary fuel consumed. Thus, reducing the amount of bunker fuel used reduces both costs and emissions.

It is generally accepted from hydrodynamics and confirmed empirically that vessel bunker fuel consumption per time unit is proportional to the third power of the sailing speed (or bunker fuel consumption per unit of distance is proportional to the second power of the sailing speed). However, the exact form of the relationship is vessel-specific and must be derived empirically. There is evidence that the power may be higher than three, and it also depends on the weather and the vessel’s hull condition (see Kontovas and Psaraftis, 2011). For a third power relationship reducing speed by 20% may result in up to 50% reduction of daily bunker fuel consumption and corresponding emissions, or up to 35% reduction in bunker fuel consumption for a given route. On the other hand, sailing speed reduction reduces the amount of cargo a vessel can carry per time period, and may require operating additional vessels in order to meet demand.

There are several additional operational economic issues associated with bunker fuel that were addressed in the OR literature. (1) The total weight carrying capacity of a ship is limited (known as the deadweight of the vessel). It includes cargo, bunker and auxiliary fuel, supplies, stores, etc. If more weight capacity is allocated to revenue generating cargo less bunker fuel can be loaded on the vessel. (2) Bunker fuel prices change over time and the question may be when to buy it. (3) Bunker fuel prices vary from port to port, and one must decide where to buy it. (4) The amount of cargo on a vessel may change from port to port, and thus the amount of bunker fuel that can be loaded at a given port may vary. (5) The later one refuels the less bunker fuel is left on the vessel and more can be loaded. We start here with sailing speed determination, move to bunkering issues, and close with estimation and reduction of emissions.

## 4.1. Sailing speed

On the tramp side, Fagerholt et al. (2010b) minimize vessel fuel consumption on a single route while satisfying port time windows by determining optimal sailing speed for each voyage leg. Norstad et al. (2011) consider a heterogeneous fleet of tramp vessels with a set of mandatory and optional cargoes and associated port time windows. They assign cargoes to vessels and determine the optimal speed for each sailing leg while maximizing profit (income from optional cargoes minus fleet operating costs). It is demonstrated that incorporating sailing speed as a decision variable when planning vessel routes significantly improves fleet utilization and profit. Gatica and Miranda (2010) deal with a heterogeneous fleet of vessels and minimize the cost of serving a set of mandatory single trip cargoes while determining the speed for each trip. Discretizing the port time windows facilitated using a network model.

On the liner side, Notteboom and Vernimmen (2009) provide detailed background information and describe how container lines changed sailing speed and number of vessels deployed in response to increasing bunker fuel cost. Ronen (2011) presents a procedure to determine the optimal average sailing speed and number of containerships for a line with a specified sequence of port calls and given service frequency. Since the service frequency is known it facilitates finding the optimal speed for a heterogeneous set of known vessels. Several papers incorporate sailing speed decisions in fleet deployment models. Gelareh and Meng (2010) allocate vessels to a set of predefined routes, determine service frequency on each route and the corresponding sailing speed necessary to meet specified demand while minimizing fleet operating costs. Meng and Wang (2011b) address a similar problem but focus on a single route. They determine the type and number of containerships for the route, frequency of service, and sailing speed for each leg that minimize average daily operating costs. Meng and Wang (2010) consider a shipping company operating a set of container routes with uncertain demand. A homogeneous set of vessels is assigned to each route and service frequency (i.e. sailing speed) is determined. Another fleet deployment model that determines sailing speed is presented by Zacharioudakis et al. (2011). They use genetic algorithms to assign vessels to predefined routes while determining speed and minimizing costs.

Speed optimization in a somewhat different context is discussed by Álvarez et al. (2010). They evaluate port berth assignment policies to replace the traditional first-come first-served one for arriving vessels, taking into account stochastic aspects in vessel arrival time and port operations. Vessel sailing speed on the inbound leg is adjusted to arrive at its designated berthing time.

## 4.2. Bunkering and refueling

Bebes and Savin (2009) present methodological models for handling vessel refueling decisions. For a single liner on a specified route they minimize refueling costs subject to vessel fuel storage capacity and random fuel prices. For a single vessel in the spot market they select a route that maximizes profit, taking into account cargo revenue and random bunker fuel cost. Kim et al. (2012) look at a single vessel on a single route and try to minimize the bunker fuel related costs and the cost of the ship’s time by determining the sailing speed, the bunkering ports and the associated bunker quantities.

Oh and Karimi (2010) analyze a route of a parcel tanker and determine the optimal speed for each leg of the route and a refueling plan (locations and quantities) that minimize the expected total operating cost of the route (fuel prices are uncertain).

Yao et al. (2012) look at a single shipping line with a homogeneous set of vessels and specified average sailing speed. They determine the bunkering ports, bunker fuel quantities and sailing speed adjustments for each leg that minimize the total bunker fuel related costs. They also consider the potential loss of cargo revenue due to bunker fuel weight.

## 4.3. Emissions

Several papers estimate carbon dioxide $( \mathsf { C O } _ { 2 } )$ emissions of the world fleet and the impact of vessel speed and bunker fuel price (or imposition of tax on bunker fuel) on such emissions. They usually take a bottom-up approach based on optimal sailing speed calculations for fleet segments. Corbett et al. (2009) analyze containership routes whereas Lindstad et al. (2011) base their analysis on the various segments of the world fleet (bulk, container, RoRo and others). Schrooten et al. (2008) estimate emissions from sea-going vessels for the Belgian region. Kontovas and Psaraftis (2011) analyze emission reductions along the container transportation chain taking into account interaction between sailing time and port time. Windeck and Stadtler (2011) propose a model and a heuristic solution algorithm for network design where the focus is on reduction of emissions from fuel consumption while taking into account waves, currents and wind.

## 5. Offshore logistics, lightering and stowage

We have encountered several papers that address other ship routing and scheduling (and associated) problems that do not fall neatly under the former headings. During recent years there has been an increasing research interest in offshore logistics, such as routing and scheduling of offshore supply vessels (OSVs) carrying products between onshore depots and offshore oil and gas installations. OSVs are considered an expensive resource and Aas et al. (2009) discuss their role. Furthermore, they analyze the design of OSVs in order to better support operations. Halvorsen-Weare and Fagerholt (2011) study the problem of designing an optimal fleet of OSVs to charter-in for operation, as well as the fleet’s weekly routes and schedules. The vessels operate in an area where weather conditions can be rough, and wave heights over certain limits reduce the sailing speeds and increase the service times at the offshore installations. Halvorsen-Weare and Fagerholt (2011) suggest and test different strategies for creating more robust OSV fleets and schedules that can better withstand the prevailing weather conditions the vessels may encounter.

Planning the route of a single OSV is an operational problem. In this problem, both pickups and deliveries must be made at the installations, while respecting several practical considerations, such as vessel and platform storage capacities. Aas et al. (2007) consider the problem as a single vessel routing problem with pickups and deliveries extended with capacity restrictions at the customers (offshore installations), and present a mathematical formulation for the problem. They use commercial software to solve the problem. Since they are able to solve only small instances, Gribkovskaia et al. (2008) propose several construction heuristics and a tabu search algorithm that are tested on a large number of instances.

Yet another study from offshore logistics is provided by Shyshou et al. (2010), which consider the problem of sizing a fleet of anchor handling tug supply vessels. They propose a simulation-based decision support tool to evaluate the optimal number of vessels to charter-in for the long-term vs. the number of vessels to charter-in from the spot market while considering uncertainty in weather conditions and future spot rates.

Lin et al. (2003) describe a new formulation for scheduling lightering operations of crude oil tankers outside refinery ports. They introduce sequences of event points and use binary variables to decide whether a ship should start a given task at each event point. Then they use continuous time to keep track of all operations. Their use of continuous time and binary event variables is similar to the way routing models couple start time of service at a node with a binary leg variable representing arrival at the node. They provide lightering schedules for five case studies that are solved by commercial software. Another ‘‘lightering’’ problem is presented by Huang and Karimi (2006). They discuss a problem where large deep-sea chemical tankers transfer their cargo directly to smaller short-sea tankers for regional distribution. They point out that the liquids cannot be stored on shore. This means that there is less operational flexibility compared to other goods, since both ships have to participate in the transfer at the same time. They suggest a MIP model for the problem which is solved by commercial software for a few test cases. For larger problem sizes they propose to heuristically aggregate cargoes with common destinations, and show that this works with small optimality gaps on their test cases.

Stowage of goods is important on all ships, but it is rarely treated in connection with routing. It is usually assumed that it is possible to find a feasible stowage plan for a voyage on a given route. Hvattum et al. (2009) study the problem of allocating liquid bulk cargoes to tanks for a given route. They consider a number of complicating but practical constraints that must be maintained at all stages along the route, such as product – tank compatibility, tank sloshing, hazardous materials rules, and ship stability and strength. A mathematical model and several variations of it are presented. Computational results from solving a large number of randomly generated test instances with different characteristics are reported.

Another stowage problem in maritime transportation is considered by Øvstebø et al. (2011a) that discuss stowage plans for RoRo ships with examples from vehicle transportation. Such ships have several decks with different adjustable heights and each deck is divided into lanes. The authors formulate a MIP model that takes care of the stability of the ship on all legs, and of the fact that it is cheaper to unload vehicles in a last-in-first-out sequence from each lane. They solve their model both with commercial software and a user-written heuristic. The same authors extend their discussion in Øvstebø et al. (2011b) from stowage on a fixed route to a routing problem with stowage constraints. Their routing problem consists of finding a pickup and delivery route for one ship. In addition to visiting a set of mandatory ports there are also some optional ports the ship may visit. Their objective is to maximize the revenue from transporting the optional cars minus the transportation cost and the penalties for not transporting all cars from the mandatory pickup ports. Also here they have a MIP formulation which they solve using commercial software and heuristics. The heuristic for the stowage problem is the same as in the previous paper while they have added a tabu search heuristic for the routing part.

## 6. Statistical analysis and research trends

Over the years we have witnessed large increases in research activity in this domain, combined with shifts in emphasis, as well as the usage of an increasing variety of research outlets. We analyze here developments in the volume of research, the outlets used, and the addressed topics. Improving digital search tools (especially Google Scholar) allowed us to unearth relevant work in minor outlets of which we were not aware in our earlier reviews. The volume of material that we had identified for this review was too large to cover and therefore we had to confine ourselves to papers published in refereed journals and edited volumes. Our earlier reviews were less selective. Thus, in order to facilitate comparisons, we went through the references in our earlier reviews and, for the sake of fair treatment, applied the same criteria. Also, as mentioned earlier, we excluded from this review specialized topics associated with container line operations, an area that has received significant research attention in recent years. Although classification of research papers and outlets requires some expert judgment and may result in minor discrepancies, the trends that we observe are obvious and not affected by such judgement.

We looked first at the development in the number of published papers and their research outlets. Table 3 presents the number of new research papers included in each of our four review papers (each one of the reviews covers about a decade, excluding the initial one). The table presents the top 10 outlets (in terms of cumulative number of papers). We see that the number of new published research papers about doubles every decade. In parallel, the number of research outlets used presents the same growth pattern. The top 10 research outlets are a mix of maritime-focused journals (MPM and MEL), transportation journals (TS and TRE) and general OR journals. Some of these journals have attracted more papers in recent years (EJOR, JORS, TRE, COR, MEL) whereas others have attracted less (OR and NRL).

Table 3

Top 10 outlets for new research papers (number of papers).<sup>a</sup>

| Outlet | Ronen (1983) | Ronen (1993) | Christiansen et al. (2004) | Current review | Total |
| --- | --- | --- | --- | --- | --- |
| Maritime Policy &amp; Management (MPM) | 1 | 8 | 9 | 6 | 24 |
| Transportation Science (TS) | 4 | 7 | 4 | 4 | 19 |
| European J. of Oper. Research (EJOR) | 0 | 3 | 7 | 8 | 18 |
| J. of the Oper. Research Soc. (JORS) | 2 | 3 | 4 | 7 | 16 |
| Operations Research (OR) | 8 | 4 | 1 | 1 | 14 |
| Transportation Research Part E (TRE) | 0 | 1 | 0 | 11 | 12 |
| Naval Research Logistics (NRL) | 4 | 2 | 4 | 0 | 10 |
| Computers &amp; Oper. Research (COR) | 0 | 0 | 0 | 8 | 8 |
| Interfaces | 1 | 2 | 3 | 2 | 8 |
| Maritime Econ. &amp; Logistics (MEL) | 0 | 0 | 1 | 6 | 7 |
| Other outlets | 2 | 8 | 22 | 74 | 106 |
| Number of new papers | 22 | 38 | 55 | 127 | 242 |
| Number of outlets | 8 | 12 | 23 | 48 | 62 |
| Total references in review | 39 | 43 | 78 | 131 | na |

a Published in English in refereed journals and edited volumes (edited volumes are counted as a single outlet).

Topics and publication year (number of papers).

<table><tr><td rowspan="2">Publication year</td><td rowspan="2">Total  $papers^a$  (all modes)</td><td colspan="6">Liners</td><td rowspan="2">General</td></tr><tr><td>Network design</td><td>Size and mix</td><td>Routing and scheduling</td><td>Deployment</td><td>Speed</td><td>Other</td></tr><tr><td>2007-2011</td><td>104</td><td>10</td><td>4</td><td>13</td><td>8</td><td>9</td><td>5</td><td>3</td></tr><tr><td>2002-2006</td><td>26</td><td></td><td></td><td>6</td><td>1</td><td></td><td>1</td><td>3</td></tr><tr><td>1997-2001</td><td>28</td><td></td><td>3</td><td></td><td>3</td><td></td><td></td><td>3</td></tr><tr><td>1992-1996</td><td>11</td><td></td><td></td><td>1</td><td></td><td></td><td>1</td><td>2</td></tr><tr><td rowspan="2"></td><td colspan="8">Industrial and tramp</td></tr><tr><td>Size and mix</td><td>Routing and scheduling</td><td>Speed</td><td>MIR</td><td>LNG</td><td>OSV</td><td>DSS</td><td>Other</td></tr><tr><td>2007-2011</td><td>1</td><td>16</td><td>7</td><td>11</td><td>6</td><td>5</td><td>3</td><td>6</td></tr><tr><td>2002-2006</td><td></td><td>4</td><td></td><td>5</td><td></td><td></td><td>1</td><td>6</td></tr><tr><td>1997-2001</td><td>4</td><td>9</td><td>2</td><td>5</td><td></td><td>1</td><td></td><td>1</td></tr><tr><td>1992-1996</td><td>2</td><td>4</td><td></td><td>1</td><td></td><td></td><td></td><td>1</td></tr></table>

a A paper may address more than one topic.

In order to identify trends in research topics we took the papers referenced in our last two review papers, divided them into 5-year periods, and listed the number of papers by topic (the number of papers in the earlier two reviews is too small and does not provide any additional insight). The results are presented in Table 4. We can see the fast increase in the total number of papers in the last 5 years, combined with increased attention to liners (namely, containerships) during that period, and an increased interest in specialized topics such as: sailing speed, maritime inventory routing (MIR), Liquefied Natural Gas transportation (LNG), and offshore supply vessels operations (OSVs). In our earlier work (Christiansen et al., 2004, 2007) we lamented the lack of research on liner shipping. We are glad to note that, as evidenced by the data in Table 4, this gap has been closing fast in recent years.

We would also like to note that during earlier years the vast majority of research originated in real-life operations, while more recently we see more theoretical models that are less grounded in real operations.

## 7. Concluding remarks

Research on ship routing and scheduling has blossomed during the last decade. Comparing to the former decade its volume has more than doubled, and the same is true for the variety of research outlets. The research seems to be catching up with the increasing world fleet and trade. Problems of wider scope have been addressed, specifically liner network design, maritime inventory routing, and maritime supply chains. In addition, more specialized problems have attracted wider attention, such as LNG shipping, offshore supply vessels operations, optimal sailing speed, and problems specific to Roll-on Roll-off vessels operations. Useful commercial decision support systems for the better defined problems in the industrial shipping mode, those with less uncertainty, have started emerging. These are very encouraging developments.

In spite of all these developments very important challenging complex problems remain to be properly addressed. First and foremost, at least by its potential economic impact, is the liner network design problem. We think that here recent research has just scratched the surface. A major operator of containerships may control hundreds of vessels sailing dozens of routes while serving thousands of origin–destination pairs. The proper network design and allocation of vessels to lines can make or break such an operator. The major obstacles here are demand and operational uncertainties, and the problem size and complexity.

Another important and complex problem, although with somewhat lower economic impact, is combining ship routing and scheduling with port management issues (e.g. berth allocation). This is more practical when the operator that controls the ships also controls the port terminal. These problems and others provide a fertile ground for future high-impact research.

We observe that some of the recent research is addressing problems that are less grounded in real operations but rather focuses more on theoretical contributions. This trend creates a need for benchmark datasets for the different types of problems, like those available in land-based transportation. Such datasets accommodate comparisons among competing solution approaches and would probably attract even more research interest to maritime transportation problems.

Finally, in maritime transportation there is significant uncertainty in sailing and port times as well as in demand, cost of ships and other inputs, and freight rates. So far just a few researchers have explicitly considered such uncertainty. We expect that this will become another area of interest for researchers and the industry in this and future decades.

## Acknowledgements

This research was carried out with financial support from the DESIMAL and DOMinant II projects, partly funded by the Research Council of Norway.

## References

Aas, B., Gribkovskaia, I., Halskau, O., Shlopak, A., 2007. Routing of supply vessels to petroleum installations. International Journal of Physical Distribution & Logistics Management 37 (2), 164–179.

Aas, B., Halskau, O., Wallace, S.W., 2009. The role of supply vessels in offshore logistics. Maritime Economics & Logistics 11 (3), 302–325.

Agarwal, R., Ergun, Ö., 2008. Ship scheduling and network design for cargo routing in liner shipping. Transportation Science 42 (2), 175–196.

Agarwal, R., Ergun, Ö., 2010. Network design and allocation mechanisms for carrier alliances in liner shipping. Operations Research 58 (6), 1726–1742.

Al-Khayyal, F., Hwang, S.-J., 2007. Inventory constrained maritime routing and scheduling for multi-commodity liquid bulk, Part I: Applications and model. European Journal of Operational Research 176, 106–130.

Álvarez, J.F., 2009. Joint routing and deployment of a fleet of container vessels. Maritime Economics & Logistics 11 (2), 186–208.

Álvarez, J.F., 2012. Mathematical expressions for the transit time of merchandise through a liner shipping network. Journal of the Operational Research Society 63, 709–714.

Álvarez, J.F., Longva, T., Engebrethsen, E.S., 2010. A methodology to assess vessel berthing and speed optimization policies. Maritime Economics & Logistics 12 (4), 327–346.

Álvarez, J.F., Tsilingiris, P., Engebrethsen, E., Kakalis, N.M.P., 2011. Robust fleet sizing and deployment for industrial and independent bulk ocean shipping companies. INFOR 49 (2), 93–107.

Andersson, H., 2011. A maritime pulp distribution problem. INFOR 49 (2), 125–138.

Andersson, H., Christiansen, M., Fagerholt, K., 2010a. Transportation planning and inventory management in the LNG supply chain. In: Bjørndal, E., Bjørndal, M., Pardalos, P.M., Rönnqvist, M. (Eds.), Energy, Natural Resources and Environmental Economics. Springer, pp. 427–439.

Andersson, H., Christiansen, M., Fagerholt, K., 2011a. Maritime pickup and delivery problems with split loads. INFOR 49 (2), 79–91.

Andersson, H., Duesund, J.M., Fagerholt, K., 2011b. Ship routing and scheduling with cargo coupling and synchronization constraints. Computers & Industrial Engineering 61, 1107–1116.

Andersson, H., Hoff, A., Christiansen, M., Hasle, G., Løkketangen, A., 2010b. Industrial aspects and literature survey: combined inventory management and routing. Computers & Operations Research 37, 1515–1536.

Bebes, O., Savin, S., 2009. Going bunkers: the joint route selection and refueling problem. Manufacturing & Service Operations Management 11 (4), 694–711.

Bilgen, G., 2007. An interactive fixing variable heuristic for solving a combined blending and distribution planning problem. Numerical Methods and Applications, Lecture Notes in Computer Science 4310, 231–238.

Bilgen, B., Ozkarahan, I., 2007. A mixed-integer linear programming model for bulk grain blending and shipping. International Journal of Production Economics 107, 555–571.

Boros, E., Lei, L., Zaho, Y., Zhong, H., 2008. Scheduling vessels and container-yard operations with conflicting objective. Annals of Operations Research 161 (1), 149–170.

Bredström, D., Carlsson, D., Rönnqvist, M., 2005. A hybrid algorithm for distribution problems. IEEE Intelligent Systems 20, 19–25.

Brønmo, G., Christiansen, M., Fagerholt, K., Nygreen, B., 2007a. A multi-start local search heuristic for ship scheduling – a computational study. Computers & Operations Research 34, 900–917.

Brønmo, G., Christiansen, M., Nygreen, B., 2007b. Ship routing and scheduling with flexible cargo sizes. Journal of the Operational Research Society 58 (9), 1167–1177.

Brønmo, G., Nygreen, B., Lysgaard, J., 2010. Column generation approaches to ship scheduling with flexible cargo sizes. European Journal of Operational Research 200 (1), 139–150.

Bubbico, R., Di Cave, S., Mazzarotta, B., 2009. Preliminary risk analysis for LNG tankers approaching a maritime terminal. Journal of Loss Prevention in the Process Industries 22 (5), 634–638.

Chen, Z.-L., Lei, L., Zhong, H., 2007. Container vessel scheduling with bi-directional flows. Operations Research Letters 35, 186–194.

Chen, C., Zeng, Q., 2010. Designing container shipping network under changing demand and freight rates. Transport 25 (1), 46–57.

Cheng, L., Duran, M.A., 2004. Logistics for world-wide crude oil transportation using discrete event simulation and optimal control. Computers & Chemical Engineering 28, 897–911.

Christiansen, M., Fagerholt, K., 2010. Maritime inventory routing problems. In: Floudas, C.A., Pardalos, P.M. (Eds.), Encyclopedia of Optimization. Springer (1947–1955).

Christiansen, M., Fagerholt, K., Flatberg, T., Haugen, Ø., Kloster, O., Lund, E.H., 2011. Maritime inventory routing with multiple products: a case study from the cement industry. European Journal of Operational Research 208 (1), 86–94.

Christiansen, M., Fagerholt, K., Nygreen, B., Ronen, D., 2007. Maritime transportation. In: Barnhart, C., Laporte, G. (Eds.), Handbooks in Operations Research and Management Science, Transportation, vol. 14. North-Holland, Amsterdam, pp. 189–284.

Christiansen, M., Fagerholt, K., Ronen, D., 2004. Ship routing and scheduling: status and perspectives. Transportation Science 38 (1), 1–18.

Christiansen, M., Nygreen, B., 2005. Robust inventory ship routing by column generation. In: Desaulniers, G., Desrosiers, J., Solomon, M.M. (Eds.), Column Generation. Springer, pp. 197–224.

Chu, C.-W., Kou, T.-C., Shieh, J.-C., 2003. A mixed integer programming model for routing containerships. Journal of Marine Science and Technology 11 (2), 96–103.

Chuang, T.-N., Lin, C.-T., Kung, J.-Y., Lin, M.-D., 2010. Planning the route of container ships: a fuzzy genetic approach. Expert Systems with Applications 37, 2948–2956.

Corbett, J.J., Wang, H., Winebrake, J.J., 2009. The effectiveness and costs of speed reductions on emissions from international shipping. Transportation Research Part D 14, 593–598.

Dauzère-Pérès, S., Nordli, A., Olstad, A., Haugen, K., Koester, U., Myrstad, P.O., Teistklub, P., Reistad, A., 2007. Omya Hustadmarmor optimizes its supply chain for delivering calcium carbonate slurry to European paper manufacturers. Interfaces 37 (1), 39–51.

Desrosiers, J., Dumas, Y., Solomon, M.M., Soumis, F., 1995. Time constrained routing and scheduling. In: Ball, M.O., Magnanti, T.L., Monma, C.L., Nemhauser, G.L. (Eds.), Handbooks in Operations Research and Management Science, Network Routing, vol. 8. North-Holland, Amsterdam, pp. 35–139.

Fagerholt, K., 2004a. Designing optimal routes in a liner shipping problem. Maritime Policy & Management 31 (4), 259–268.

Fagerholt, K., 2004b. A computer-based decision support system for vessel fleet scheduling – experience and future research. Decision Support Systems 37 (1), 35–47.

Fagerholt, K., Christiansen, M., Hvattum, L.M., Johnsen, T.A.V., Vabø, T.J., 2010a. A decision support methodology for strategic planning in maritime transportation. OMEGA 38 (6), 465–474.

Fagerholt, K., Hvattum, L.M., Johnsen, T.A.V., Korsvik, J.E., 2011. Routing and scheduling in project shipping. Annals of Operations Research. http://dx.doi.org/[10.1007/s10479-011-0888-1.](http://dx.doi.org/10.1007/s10479-011-0888-1)

Fagerholt, K., Johnsen, T.A.V., Lindstad, H., 2009a. Fleet deployment in liner shipping: a case study. Maritime Policy & Management 36 (5), 397–409.

Fagerholt, K., Korsvik, J.E., Løkketangen, A., 2009b. Ship routing scheduling with persistence and distance objectives. Innovations in Distribution Logistics, Lecture Notes in Economics and Mathematical Systems 619, 89–107.

Fagerholt, K., Laporte, G., Norstad, I., 2010b. Reducing fuel emissions by optimizing speed on shipping routes. Journal of the Operational Research Society 61 (3), 523–529.

Fagerholt, K., Lindstad, H., 2007. TurboRouter: An interactive optimization-based decision support system for ship routing and scheduling. Maritime Economics & Logistics 9, 214–233.

Fodstad, M., Uggen, K.T., Rømo, F., Lium, A.-G., Stremersch, G., Hecq, S., 2010. LNGScheduler: a rich model for coordinating vessel routing, inventories and trade in the LNG supply chain. Journal of Energy Markets 3, 1–34.

Furman, K.C., Song, J.-H., Kosic, G.R., McDonald, M.M., Warrick, P.H., 2011. Feedstock routing in the ExxonMobil downstream sector. Interfaces 41 (2), 149–163.

Gatica, R.A., Miranda, P.A., 2010. A time based discretization approach for ship routing and scheduling with variable speed. Networks and Spatial Economics 11 (3), 465–485.

Gelareh, S., Meng, Q., 2010. A novel modeling approach for the fleet deployment problem within a short-term planning horizon. Transportation Research Part E 46 (1), 76–89.

Gelareh, S., Nickel, S., Pisinger, D., 2010. Liner shipping hub network design in a competitive environment. Transportation Research Part E 46 (6), 991–1004.

Gelareh, S., Pisinger, D., 2011. Fleet deployment, network design and hub location of liner shipping companies. Transportation Research Part E 47 (6), 947–964.

Gribkovskaia, I., Laporte, G., Shlopak, A., 2008. A tabu search heuristic for a routing problem arising in servicing offshore oil and gas platforms. Journal of the Operational Research Society 59, 1449–1459.

Grønhaug, R., Christiansen, M., 2009. Supply chain optimization for the liquefied natural gas business. Innovations in Distribution Logistics, Lecture Notes in Economics & Mathematical Systems 619, 195–218.

Grønhaug, R., Christiansen, M., Desaulniers, G., Desrosiers, J., 2010. A branch-and-price method for a liquefied natural gas inventory routing problem. Transportation Science 44 (3), 400–415.

Gunnarsson, H., Rönnqvist, M., Carlsson, D., 2006. A combined terminal location and ship routing problem. Journal of the Operational Research Society 57, 923–938.

Halvorsen-Weare, E.E., Fagerholt, K., 2010. Routing and scheduling in a liquefied natural gas shipping problem with inventory and berth constraints. Annals of Operations Research. http://dx.doi.org/[10.1007/s10479-010-0794-y.](http://dx.doi.org/10.1007/s10479-010-0794-y)

Halvorsen-Weare, E.E., Fagerholt, K., 2011. Robust supply vessel planning. Network Optimization, Lecture Notes in Computer Science 6701, 559–574.

Hennig, F., Furman, K.C., Kocis, G.R., Nygreen, B., Song, J., 2011. Crude oil tanker routing and scheduling. INFOR 49 (2), 153–170.

Hennig, F., Nygreen, B., Christiansen, M., Fagerholt, K., Furman, K.C., Song, J., Kocis, G.R., Warrick, P.H., 2012. Maritime crude oil transportation – a split pickup and split delivery problem. European Journal of Operational Research 218 (3), 764–774.

Hoff, A., Andersson, H., Christiansen, M., Hasle, G., Løkketangen, A., 2010. Industrial aspects and literature survey: fleet composition and routing. Computers & Operations Research 37, 2041–2061.

Hsu, C.-I., Hsieh, Y.-P., 2005. Direct versus terminal routing on a maritime hub-and-spoke container network. Journal of Marine Science and Technology 13 (3), 209–217.

Hsu, C.-I., Hsieh, Y.-P., 2007. Routing, ship size and sailing frequency decision making for a maritime hub-and-spoke container network. Mathematical and Computer Modeling 45 (7–8), 899–916.

Huang, C., Karimi, I.A., 2006. Scheduling trans-shipment operations in maritime chemical transportation. Industrial & Engineering Chemistry Research 45, 1955–1973.

Hvattum, L.M., Fagerholt, K., Armentano, V.A., 2009. Tank allocation problems in maritime bulk shipping. Computers & Operations Research 36 (11), 3051–3060.

Hwang, H.-S., Visoldilokpun, S., Rosenberger, J.M., 2008. A branch-and-price-and-cut method for ship scheduling with limited risk. Transportation Science 42 (3), 336–351.

Imai, A., Shintani, K., Papadimitriou, S., 2009. Multi-port vs. hub-and-spoke port calls by containerships. Transportation Research Part E 45, 740–757.

Jetlund, A.S., Karimi, I.A., 2004. Improving the logistics of multi-compartment chemical tankers. Computers and Chemical Engineering 28, 1267–1283.

Jung, J.N., Kang, M.N., Choi, H.R., Kim, H.S., Park, B.J., Park, C.H., 2011. Development of a genetic algorithm for the maritime transportation planning of car carriers. Dynamics in Logistics 6, 481–488.

Kang, M.H., Choi, H.R., Kim, H.S., Park, B.J., 2012. Development of a maritime transportation planning support system for car carriers based on genetic algorithm. Applied Intelligence 36 (3), 585–604.

Karlaftis, M.G., Kepaptsoglou, K., Sambracos, E., 2009. Containership routing with time deadlines and simultaneous deliveries and pick-ups. Transportation Research Part E 45 (1), 210–221.

Kim, H.J., Chang, Y.T., Kim, K.T., Kim, H.J., 2012. An epsilon-optimal algorithm considering greenhouse gas emissions for the management of a ship’s bunker fuel. Transportation Research Part D 17, 97–103.

Kjeldsen, K., 2011. Classification of ship routing and scheduling problems in liner shipping. INFOR 49 (2), 139–152.

Kobayashi, K., Kubo, M., 2010. Optimization of oil tanker schedules by decomposition, column generation, and time-space network techniques. Japan Journal of Industrial and Applied Mathematics 27 (1), 161–173.

Kontovas, K., Psaraftis, H.N., 2011. Reduction of emissions along the maritime intermodal container chain: operational models and policies. Maritime Policy & Management 38 (4), 451–469.

Korsvik, J.E., Fagerholt, K., 2010. A tabu search heuristic for ship routing and scheduling with flexible cargo quantities. Journal of Heuristics 16 (2), 117–137.

Korsvik, J.E., Fagerholt, K., Laporte, G., 2010. A tabu search heuristic for ship routing and scheduling. Journal of the Operational Research Society 61 (4), 594–603.

Korsvik, J.E., Fagerholt, K., Laporte, G., 2011. A large neighbourhood search heuristic for ship routing and scheduling with split loads. Computers & Operations Research 38 (2), 474–483.

Lagoudis, I.N., Litinas, N.A., Fragkos, S.N., tul=0?>Lagoudis et al.(2010. Estimating optimum container and vessel fleet sizes in a cyclic liner service using a holistic approach. International Journal of Shipping and Transport Logistics 2 (1), 4–21.

Lei, L., Fan, C., Boile, M., Theofanis, S., 2008. Collaborative vs. non-collaborative container-vessel scheduling. Transportation Research Part E 44, 504–520.

Li, C.L., Pang, K.W., 2011. An integrated model for ship routing and berth allocation. International Journal of Shipping and Transport Logistics 3 (3), 245–260.

Li, J., Karimi, I.A., Srinivasan, R., 2010. Efficient bulk maritime logistics for the supply and delivery of multiple chemicals. Computers & Chemical Engineering 34 (12), 2118–2128.

Lin, D.-Y., Liu, H.-Y., 2011. Combined ship allocation, routing and freight assignment in tramp shipping. Transportation Research Part E 47, 414–431.

Lin, X., Chajakis, E.D., Floudas, C.A., 2003. Scheduling of tanker lightering via a novel continuous-time optimization framework. Industrial & Engineering Chemistry Research 42, 4441–4451.

Lindstad, H., Asbjørnslett, B.E., Strømman, A.H., 2011. Reductions in greenhouse gas emissions and cost by shipping at lower speed. Energy Policy 39, 3456–3464.

Liu, C.-M., 2008. A blending and inter-modal transportation model for the coal distribution problem. International Journal of Operations Research 5 (2), 107–116.

Liu, X., Ye, H.-Q., Yuan, X.-M., 2011. Tactical planning models for managing container flow and ship deployment. Maritime Policy & Management 38 (5), 487–508.

Lu, H.-A., 2002. Modeling ship’s routing bounded by the cycle time for marine liner. Journal of Marine Science & Technology 10 (1), 61–67.

Lun, Y.H.V., Browne, M., 2009. Fleet mix in container shipping operations. International Journal of Shipping and Transport Logistics 1 (2), 103–118.

Malliappi, F., Bennell, J.A., Potts, C.N., 2011. A variable neighborhood search heuristic for tramp ship scheduling. Computational Logistics, Lecture Notes in Computer Science 6971, 273–285.

Meng, Q., Wang, S., 2011a. Liner shipping service network design with empty container repositioning. Transportation Research Part E 47, 695–708.

Meng, Q., Wang, S., 2011b. Optimal operating strategy for a long-haul liner service route. European Journal of Operational Research 215, 105–114.

Meng, Q., Wang, S., 2011c. An intermodal container flow simulation model and its applications. Transportation Research Record 2224, 35–41.

Meng, Q., Wang, T., 2010. A chance constrained programming model for short-term liner ship planning problems. Maritime Policy & Management 37 (4), 329–346.

Meng, Q., Wang, T., 2011d. A scenario-based dynamic programming model for multi-period liner ship fleet planning. Transportation Research Part E 47, 401–413.

Meng, Q., Wang, X., 2011e. Intermodal hub-and-spoke network design: incorporating multiple stakeholders and multi-type containers. Transportation Research Part B 45 (4), 724–742.

Ng, A.K.Y., Kee, J.K.Y., 2008. The optimal ship sizes of container liner feeder services in Southeast Asia: a ship operator’s perspective. Maritime Policy & Management 35 (4), 353–376.

Norstad, I., Fagerholt, K., Laporte, G., 2011. Tramp ship routing and scheduling with speed optimization. Transportation Research Part C 19, 853–865.

Notteboom, T.E., Vernimmen, B., 2009. The effect of high fuel cost on liner service configuration in container shipping. Journal of Transport Geography 17, 325–337.

Oh, H.C., Karimi, I.A., 2010. Operation planning of multiparcel tankers under fuel price uncertainty. Industrial & Engineering Chemistry Research 49, 6104–6114.

Pang, K.W., Xu, Z., Li, C.L., 2011. Ship routing problem with berthing time clash avoidance constraints. International Journal of Production Economics 131, 752–762.

Persson, J.A., Göthe-Lundgren, M., 2005. Shipment planning at oil refineries using column generation and valid inequalities. European Journal of Operational Research 163, 631–652.

Powell, B.J., Perakis, A.N., 1997. Fleet deployment optimization for liner shipping: an integer programming model. Maritime Policy & Management 24 (2), 183–192.

Rakke, J.G., Stålhane, M., Moe, C.R., Andersson, H., Christiansen, M., Fagerholt, K., Norstad, I., 2011. A rolling horizon heuristic for creating a liquefied natural gas annual delivery program. Transportation Research Part C 19, 896–911.

Reinhardt, L.B., Pisinger, D., 2012. A branch and cut algorithm for the container shipping network design problem. Flexible Services and Manufacturing Journal 24 (3), 349–374.

Ronen, D., 1983. Cargo ships routing and scheduling: survey of models and problems. European Journal of Operational Research 12, 119–126.

Ronen, D., 1993. Ships scheduling: the last decade. European Journal of Operational Research 71 (3), 325–333.

Ronen, D., 2011. The effect of oil price on containership speed and fleet size. Journal of the Operational Research Society 62 (1), 211–216.

Sambracos, E., Paravantis, J.A., Tarantilis, C.D., Kiranoudis, C.T., 2004. Dispatching of small containers via coastal freight liners: the case of the Aegean Sea. European Journal of Operational Research 152, 365–381.

Schrooten, L., De Vlieger, I., Panis, L.I., Styns, K., Torfs, R., 2008. Inventory and forecasting of maritime emissions in the Belgian sea territory, an activity-based emission model. Atmospheric Environment 42 (4), 667–676.

Sherali, H.D., Al-Yakoob, S.M., 2006a. Determining an optimal fleet mix and schedules: Part I – Single source and destination. In: Karlof, J.K. (Ed.), Integer Programming Theory and Practice. CRC Press, Boca-Raton, pp. 137–166.

Sherali, H.D., Al-Yakoob, S.M., 2006b. Determining an optimal fleet mix and schedules: Part II – Multiple sources and destinations, and the option of leasing transshipment depots. In: Karlof, J.K. (Ed.), Integer Programming Theory and Practice. CRC Press, Boca-Raton, pp. 167–194.

Shintani, K., Imai, A., Nishimura, E., Papadimitriou, S., 2007. The container shipping network design problem with empty container repositioning. Transportation Research Part E 43, 39–59.

Shyshou, A., Gribkovskaia, I., Barcelo, J., 2010. A simulation study of the fleet sizing problem arising in offshore anchor handling operations. European Journal of Operational Research 203, 230–240.

Sigurd, M.M., Ulstein, N.L., Nygreen, B., Ryan, D.M., 2005. Ship scheduling with recurring visits and visit separation requirements. In: Desaulniers, G., Desrosiers, J., Solomon, M.M. (Eds.), Column Generation. Springer, US, pp. 225–245 (chapter 8).

Siswanto, N., Essam, D., Sarker, R., 2011. Solving the ship inventory routing and scheduling problem with undedicated compartments. Computers & Industrial Engineering 61 (2), 289–299.

Song, J.-H., Furman, K.C., 2010. A maritime inventory routing problem: practical approach. Computers & Operations Research. http://dx.doi.org/[10.1016/j.cor.2010.10.031.](http://dx.doi.org/10.1016/j.cor.2010.10.031)

Stahlbock, R., Voss, S., 2008. Operations research at container terminals: a literature update. OR Spectrum 30, 1–52.

Stålhane, M., Rakke, J., Moe, C., Andersson, H., Christiansen, M., Fagerholt, K., 2012. A construction and improvement heuristic for a liquefied natural gas inventory routing problem. Computers & Industrial Engineering 62 (1), 245–255.

Takano, K., Arai, M., 2009. A genetic algorithm for the hub-and-spoke problem applied to containerized cargo transport. Journal of Marine Science and Technology 14 (2), 256–274.

Takano, K., Arai, M., 2011. Study on a liner shipping network design considering empty container reposition. Journal of the Japan Society of Naval Architects and Ocean Engineers 13, 175–182.

Ting, S.-C., Tzeng, G.-H., 2003. Ship scheduling and cost analysis for route planning in liner shipping. Maritime Economics & Logistics 5 (4), 378–392.

Uggen, K.T., Fodstad, M., Nørstebø, V.S., 2011. Using and extending fix-and-relax to solve maritime inventory routing problems. TOP. http://dx.doi.org/[10.1007/s11750-011-0174-z.](http://dx.doi.org/10.1007/s11750-011-0174-z)

UNCTAD, 2011. Review of Maritime Transport 2011. New York & Geneva.

Wang, S., Meng, Q., 2011. Schedule design and container routing in liner shipping. Transportation Research Record 2222, 25–33.

Wang, S., Meng, Q., 2012. Liner ship fleet deployment with container transshipment operations. Transportation Research Part E 48 (2), 470–484.

Wang, S., Wang, T., Meng, Q., 2011. A note on liner ship fleet deployment. Flexible Services and Manufacturing Journal 23 (4), 422–430.

Windeck, V., Stadtler, H., 2011. A liner shipping network design – routing and scheduling impacted by environmental influences. Network Optimization, Lecture Notes in Computer Science 6701, 574–576.

Yan, S., Chen, C.-Y., Lin, S.-C., 2009. Ship scheduling and container shipment planning for liners in short-term operations. Journal of Marine Science & Technology 14, 417–435.

Yao, Z., Ng, S.H., Lee, L.H., 2012. A study on bunker fuel management for the shipping liner services. Computers & Operations Research 39 (5), 1160–1172.

Zacharioudakis, P.G., Iordanis, P.G., Lyridis, D.V., Psaraftis, H.N., 2011. Liner shipping cycle cost modeling, fleet deployment optimization and what–if analysis. Maritime Economics & Logistics 13 (3), 278–297.

Zeng, Q., Yang, Z., 2007. Model integrating fleet design and ship routing problems for coal shipping. Computational Science – ICCS 2007, Lecture Notes in Computer Science 4489, 1000–1003.

Øvstebø, B.O., Hvattum, L.M., Fagerholt, K., 2011a. Optimization of stowage plans for RoRo ships. Computers & Operations Research 38, 1425–1434.

Øvstebø, B.O., Hvattum, L.M., Fagerholt, K., 2011b. Routing and scheduling of RoRo ships with stowage constraints. Transportation Research Part C 19 (6), 1225–1242.