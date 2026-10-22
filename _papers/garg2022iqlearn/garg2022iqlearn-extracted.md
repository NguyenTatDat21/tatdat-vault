# IQ-Learn: Inverse soft-Q Learning for Imitation

**Divyansh Garg**<sup>1</sup> **Shuvam Chakraborty**<sup>1</sup> **Chris Cundy**<sup>1</sup> **Jiaming Song**<sup>1</sup> **Matthieu Geist**<sup>2</sup> **Stefano Ermon**<sup>1</sup> 1 Stanford University 2 Google Research, Brain Team {divgarg, shuvamc, cundy, tsong, ermon}@stanford.edu

## Abstract

In many sequential decision-making problems (e.g., robotics control, game playing, sequential prediction), human or expert data is available containing useful information about the task. However, imitation learning (IL) from a small amount of expert data can be challenging in high-dimensional environments with complex dynamics. Behavioral cloning is a simple method that is widely used due to its simplicity of implementation and stable convergence but doesn’t utilize any information involving the environment’s dynamics. Many existing methods that exploit dynamics information are difficult to train in practice due to an adversarial optimization process over reward and policy approximators or biased, high variance gradient estimators. We introduce a method for dynamics-aware IL which avoids adversarial training by learning a single Q-function, implicitly representing both reward and policy. On standard benchmarks, the implicitly learned rewards show a high positive correlation with the ground-truth rewards, illustrating our method can also be used for inverse reinforcement learning (IRL). Our method, Inverse soft-Q learning (IQ-Learn) obtains state-of-the-art results in offline and online imitation learning settings, significantly outperforming existing methods both in the number of required environment interactions and scalability in high-dimensional spaces, often by more than **3x**<sup>1</sup>.

## 1 Introduction

Imitation of an expert has long been recognized as a powerful approach for sequential decisionmaking [29, 1], with applications as diverse as healthcare [39], autonomous driving [41], and playing complex strategic games [8]. In the imitation learning (IL) setting, we are given a set of expert trajectories, with the goal of learning a policy which induces behavior similar to the expert’s. The learner has no access to the reward, and no explicit knowledge of the dynamics.

The simple behavioural cloning [34] approach simply maximizes the probability of the expert’s actions under the learned policy, approaching the IL problem as a supervised learning problem. While this can work well in simple environments and with large quantities of data, it ignores the sequential nature of the decision-making problem, and small errors can quickly compound when the learned policy departs from the states observed under the expert. A natural way of introducing the environment dynamics is by framing the IL problem as an Inverse RL (IRL) problem, aiming to learn a reward function under which the expert’s trajectory is optimal, and from which the learned imitation policy can be trained [1]. This framing has inspired several approaches which use rewards either explicitly or implicitly to incorporate dynamics while learning an imitation policy [17, 10, 33, 22]. However, these dynamics-aware methods are typically hard to put into practice due to unstable learning which can be sensitive to hyperparameter choice or minor implementation details [21].

In this work, we introduce a dynamics-aware imitation learning method which has stable, non-adversarial training, allowing us to achieve state-of-the-art performance on imitation learning benchmarks. Our key insight is that much of the difficulty with previous IL methods arises from the IRL-motivated representation of the IL problem as a min-max problem over reward and policy [17, 1].

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280"><sup>1</sup>Our implementation is available at [https://github.com/Div99/IQ-Learn](https://github.com/Div99/IQ-Learn).</span></small>

Table 1: A comparison of various algorithms for imitation learning. “Convergence Guarantees” refers to if a proof is given that the algorithm converges to the correct policy with sufficient data. We consider an algorithm “directly optimized” if it consists of an optimization algorithm (such as gradient descent) applied to the parameters of a single function

<table><tr><td colspan="2">Method</td><td>Reference</td><td>Dynamics Aware</td><td>Non-Adversarial Training</td><td>Convergence Guarantees</td><td>Non-restrictive Reward</td><td>Direct Optimization</td></tr><tr><td rowspan="6">Online</td><td>Max Margin IRL</td><td>[29, 1]</td><td>✓</td><td>✓</td><td>✓</td><td>×</td><td>×</td></tr><tr><td>Max Entropy IRL</td><td>[43]</td><td>✓</td><td>✓</td><td>✓</td><td>×</td><td>×</td></tr><tr><td>GAIL/AIRL</td><td>[17, 10]</td><td>✓</td><td>×</td><td>✓</td><td>✓</td><td>×</td></tr><tr><td>ASAF</td><td>[4]</td><td>✓</td><td>✓</td><td>✓</td><td>×</td><td>✓</td></tr><tr><td>SQIL</td><td>[33]</td><td>✓</td><td>✓</td><td>×</td><td>×</td><td>✓</td></tr><tr><td>Ours (Online)</td><td>-</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td></tr><tr><td rowspan="8">Offline</td><td>Max Margin IRL</td><td>[24, 20]</td><td>✓</td><td>✓</td><td>✓</td><td>×</td><td>×</td></tr><tr><td>Max Likelihood IRL</td><td>[18]</td><td>✓</td><td>✓</td><td>✓</td><td>×</td><td>×</td></tr><tr><td>Max Entropy IRL</td><td>[16]</td><td>✓</td><td>✓</td><td>✓</td><td>×</td><td>×</td></tr><tr><td>ValueDICE</td><td>[22]</td><td>✓</td><td>×</td><td>×</td><td>×</td><td>×</td></tr><tr><td>Behavioral Cloning</td><td>[34]</td><td>×</td><td>✓</td><td>✓</td><td>×</td><td>✓</td></tr><tr><td>Regularized BC</td><td>[30]</td><td>✓</td><td>✓</td><td>✓</td><td>×</td><td>✓</td></tr><tr><td>EDM</td><td>[19]</td><td>✓</td><td>✓</td><td>×</td><td>✓</td><td>✓</td></tr><tr><td>Ours (Offline)</td><td>-</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td></tr></table>

This introduces a requirement to separately model the reward and policy, and train these two functions jointly, often in an adversarial fashion. Drawing on connections between RL and energy-based models [13, 14], we propose learning a single model for the Q-value. The Q-value then implicitly defines both a reward and policy function. This turns a difficult min-max problem over policy and reward functions into a simpler minimization problem over a single function, the Q-value. Since our problem has a one-to-one correspondence with the min-max problem studied in adversarial IL [17], we maintain the generality and guarantees of these previous approaches, resulting in a meaningful reward that may be used for inverse reinforcement learning. Furthermore, our method may be used to minimize a variety of statistical divergences between the expert and learned policy. We show that we recover several previously-described approaches as special cases of particular divergences, such as the regularized behavioural cloning of [30], and the conservative Q-learning of [23].

In our experiments, we find that our method is performant even with very sparse data - surpassing prior methods using one expert demonstration in the completely offline setting - and can scale to complex image-based tasks like Atari reaching expert performance. Moreover, our learnt rewards are highly predictive of the original environment rewards. Finally, our method is robust to distribution shifts in the environment showing great generalization performance to never seen goals and an ability to act as a meta-learner.

Concretely, our contributions are as follows:

• We present a modified Q-learning update rule for imitation learning that can be implemented on top of soft-Q learning or soft actor-critic (SAC) algorithms in fewer than **15** lines of code.

• We introduce a simple framework to minimize a wide range of statistical distances: Integral Probability Metrics (IPMs) and f-divergences, between the expert and learned distributions.

• We empirically show state-of-art results in a variety of imitation learning settings: online and offline IL. On the complex Atari suite, we outperform prior methods by **3-7x** while requiring **3x** less environment steps.

• We characterize our learnt rewards and show a high positive correlation with the ground-truth rewards, justifying the use of our method for Inverse Reinforcement Learning.

## 2 Background

**Preliminaries** We consider environments represented as a Markov decision process $( \mathrm { M D P } ) ,$ which is defined by a tuple $( \mathcal { S } , \mathcal { A } , p _ { 0 } , \mathcal { P } , r , \gamma )$ . S, A represent state and action spaces, $p _ { 0 }$ and $\mathcal { P } ( s ^ { \prime } | s , a )$

represent the initial state distribution and the dynamics, $r ( s , a ) \in \mathcal { R }$ represents the reward function, and $\gamma \in ( 0 , 1 )$ represents the discount factor. $\mathbb{R}^{\mathcal{S} \times \mathcal{A}} = \{ x : \mathcal{S} \times \mathcal{A} \to \mathbb{R} \}$ will denote the set of all functions in the state-action space and R will denote the extended real numbers $\mathbb { R } \cup \{ \infty \}$ . Sections 3 and 4 will work with finite state and action spaces $\mathcal { S }$ and $\mathcal { A } ,$ but our algorithms and experiments later in the paper use continuous environments. Π is the set of all stationary stochastic policies that take actions in $\mathcal { A }$ given states in $\mathcal { S } .$ We work in the γ-discounted infinite horizon setting, and we will use an expectation with respect to a policy $\pi \in$ Π to denote an expectation with respect to the trajectory it generates: $\textstyle \mathbb { E } _ { \pi } [ r ( s , a ) ] { \triangleq } \mathbb { E } [ \sum _ { t = 0 } ^ { \infty } \gamma ^ { t } r ( s _ { t } , a _ { t } ) ]$ , where $s _ { 0 } \sim p _ { 0 } ,   a _ { t } \sim \pi ( \cdot | s _ { t } )$ , and $s _ { t + 1 } \sim \mathcal { P } ( \cdot | s _ { t } , a _ { t } )$ for $t \geq 0$ . For a policy π ∈ Π, we define its occupancy measure $\rho _ { \pi } : \mathcal { S } \times \mathcal { A } \to \mathbb { R }$ as $\begin{array} { r } { \left( \rho _ { \pi } ( s , a ) \stackrel { \cdot } { = } ( 1 - \gamma ) \pi ( a | s ) \sum _ { t = 0 } ^ { \infty ^ { * } } \gamma ^ { t } \dot { P } \left( s _ { t } = s | \pi \right) \right. } \end{array}$ We refer to the expert policy as $\pi _ { E }$ and its occupancy measure as $\rho _ { E }$ . In practice, $\pi _ { E }$ is unknown and we have access to a sampled dataset of demonstrations D. For brevity, we refer to $\rho _ { \pi }$ as $\rho$ for a learnt policy in the paper.

**Soft** $Q .$ **-functions** For a reward $r \in \mathcal { R }$ and $\pi \in \mathrm { ~ \Pi ~ }$ , the soft Bellman operator $\mathcal { B } _ { r } ^ { \pi } \quad :$ $\mathbb { R } ^ { \mathcal { S } \times \mathcal { A } ^ { \bullet } } \rightarrow \mathbb { R } ^ { \mathcal { S } \times \mathcal { A } }$ is defined as $\begin{array} { r } { ( \mathcal { B } _ { r } ^ { \pi } Q ) ( s , a ) = r ( s , a )   +   \gamma \mathbb { E } _ { s ^ { \prime } \sim \mathcal { P } ( s , a ) } V ^ { \pi } ( s ^ { \prime } ) } \end{array}$ with $V ^ { \pi } ( s ) ^ { \dot { } } =$ $\mathbb { E } _ { a \sim \pi ( \cdot | s ) } \left[ Q ( s , a ) - \operatorname { l o g } \pi ( a | s ) \right]$ . The soft Bellman operator is contractive [13] and defines a unique soft Q-function for r, given as the fixed point solution $Q = \mathcal { B } _ { r } ^ { \pi } Q$ with $Q \in \Omega$

**Max Entropy Reinforcement Learning** For a given reward function $r \in \mathcal { R }$ , maximum entropy RL [14, 5] aims to learn a policy that maximizes the expected cumulative discounted reward along with the entropy in each state: ma $\operatorname { a x } _ { \pi \in \Pi } \mathbb { E } _ { \rho _ { \pi } } [ r ( s , a ) ] + H ( \pi )$ , where $H ( \pi ) \triangleq \mathbb { E } _ { \rho _ { \pi } } [ - \operatorname { l o g } \pi ( a | s ) ]$ is the discounted causal entropy of the policy π. The optimal policy satisfies [42, 5]:

$$
\pi^ {*} (a | s) = \frac {1}{Z _ {s}} \exp \left(Q ^ {*} (s, a)\right),\tag{1}
$$

where $Z _ { s }$ is the normalization factor given as $\textstyle \sum _ { a ^ { \prime } } \exp \left( Q ^ { * } \left( s , a ^ { \prime } \right) \right)$ and $Q ^ { * }$ is the optimal soft $Q _ { 1 }$ function.

$Q ^ { * }$ satisfies the soft-Bellman equation:

$$
Q ^ {*} (s, a) = \left(\mathcal {B} ^ {*} Q ^ {*}\right) (s, a) := r (s, a) + \gamma \mathbb {E} _ {s ^ {\prime} \sim \mathcal {P} (\cdot | s, a)} \left[ \log \sum_ {a ^ {\prime}} \exp \left(Q ^ {*} \left(s ^ {\prime}, a ^ {\prime}\right)\right) \right].\tag{2}
$$

In continuous action spaces, $Z _ { s }$ becomes computationally intractable and soft actor-critic methods like SAC [13] can be used to learn an explicit policy.

**Max Entropy Inverse Reinforcement Learning** Given demonstrations sampled using the policy $\pi _ { E } ,$ maximum entropy Inverse RL aims to recover the reward function in a family of functions $\dot { \mathcal { R } } \subset \mathbb { R } ^ { \mathcal { S } \times \mathcal { A } }$ that rationalizes the expert behavior by solving the optimization problem: $\operatorname { m a x } _ { r \in \mathcal { R } } \operatorname { m i n } _ { \pi \in \Pi } \mathbb { E } _ { \rho _ { E } } [ r ( s , a ) ] - ( \mathbb { E } _ { \rho _ { \pi } } [ r ( s , a ) ] + H ( \pi ) )$ , where the expected reward of $\pi _ { E }$ is empirically approximated using a dataset ${ \mathcal { D } } .$ It looks for a reward function that assigns high reward to the expert policy and low reward to other ones, while searching for the best policy for the reward function in an inner loop.

The Inverse RL objective can be generalized in terms of its occupancy measure, and with a convex reward regularizer $\psi : \mathbb { R } ^ { \mathcal { S } \times \mathcal { A } } \rightarrow \overline { { \mathbb { R } } }   [ 1 7 ]$

$$
\max _ {r \in \mathcal {R}} \min _ {\pi \in \Pi} L (\pi , r) = \mathbb {E} _ {\rho_ {E}} [ r (s, a) ] - \mathbb {E} _ {\rho_ {\pi}} [ r (s, a) ] - H (\pi) - \psi (r).\tag{3}
$$

In general, for a non-restrictive set of reward functions $\mathcal { R } = \mathbb { R } ^ { \mathcal { S } \times \mathcal { A } }$ , we can exchange the max-min resulting in an objective that minimizes the statistical distance parameterized by $\psi ,$ , between the expert and the policy [17]

$$
\min _ {\pi \in \Pi} \max _ {r \in \mathcal {R}} L (\pi , r) = \min _ {\pi \in \Pi} d _ {\psi} (\rho_ {\pi}, \rho_ {E}) - H (\pi),\tag{4}
$$

with $d _ { \psi } \triangleq \psi ^ { * } ( \rho _ { E } - \rho _ { \pi } )$ , where $\psi ^ { * }$ is the convex conjugate of $\psi .$ .

## 3 Inverse soft Q-learning (IQ-Learn) Framework

A naive solution to the nested min-max IRL problem in (Eq. 3) involves (1) an outer loop learning rewards and (2) executing RL in an inner loop to find an optimal policy for them. However, we know that this optimal policy can be obtained solely in terms of the soft $Q _ { 1 }$ -function $( \mathrm { E q . ~ 1 } )$ . Interestingly, as we will show later, the rewards can also be represented in terms of only $Q \; ( \mathrm { E q . } \; 2 ) .$ Together, these observations suggest it might be possible to directly solve the IRL problem by optimizing only over the $Q -$ function, thus reducing the nested min-max problem to a single minimization problem over $Q .$

To motivate the search of an imitation learning algorithm that depends only on the $Q \cdot$ function, we characterize the space of Q-functions and policies obtained using Inverse $\dot{\mathrm{RL}}$ . We will study $\pi \in \Pi$ $r \in \mathcal { R }$ and Q-functions $Q \in \Omega$ , with fully general classes $\mathcal { R } = \tilde { \Omega } = \mathbb { R } ^ { \mathcal { S } \times \mathcal { A } }$ . The full policy class Π is convex, compact with $\pi _ { E } \in \Pi$

We start with the analysis developed in [17]:

**Proposition 3.1.** The regularized IRL objective $L ( \pi , r )$ given by $E q . ~ 3$ is convex in the occupancy measure of the policy $( \rho _ { \pi } )$ and concave in the reward function $( r ) ,$ and for a strongly convex regularizer ψ has a unique saddle point $( \pi ^ { * } , r ^ { * } )$ .

To characterize the Q-functions obtained using Inverse RL it is useful to transform the IRL problem over rewards to a problem over Q-functions.

Define the inverse soft Bellman operator $\mathcal { T } ^ { \pi } : \mathbb { R } ^ { \mathcal { S } \times \mathcal { A } } \rightarrow \mathbb { R } ^ { \mathcal { S } \times \mathcal { A } }$ as

$$
(\mathcal {T} ^ {\pi} Q) (s, a) = Q (s, a) - \gamma \mathbb {E} _ {s ^ {\prime} \sim \mathcal {P} (\cdot | s, a)} V ^ {\pi} (s ^ {\prime}).
$$

with $\begin{aligned} { V ^ { \pi } ( s ) = \mathbb { E } _ { a \sim \pi ( \cdot | s ) } \left[ Q ( s , a ) - \operatorname { l o g } \pi ( a | s ) \right] } \\ \end{aligned}$ as defined before. Then, $\mathcal { T } ^ { \pi }$ inverts the soft Bellman operator $\mathcal { B } ^ { \pi }$ to map from $Q _ { 1 }$ -functions to rewards. We can get a one-to-one correspondence between r and $Q ;$

**Lemma 3.2.** For a fixed policy $\pi ,$ the inverse soft Bellman operator $\mathcal { T } ^ { \pi }$ is bijective, and for any $r \in \mathcal { R } ,   Q = ( \mathcal { T } ^ { \pi } ) ^ { - \check { 1 } } r$ is the unique fixed point of the Bellman operator $\mathcal { B } _ { r } ^ { \pi }$

The proof of this lemma is in Appendix $\mathbf { A } . 2 .$ For a policy $\pi ,$ we are justified in changing between rewards and the corresponding soft-Q functions using $\mathcal { T } ^ { \pi }$ . Thus, we can freely transform functions from the reward-policy space, $\bar { \Pi } \times \mathcal { R }$ , to the Q-policy space, $\Pi \times \Omega ,$ giving us the following lemma:

**Lemma 3.3.** Let $L ( \pi , r ) = \mathbb { E } _ { \rho _ { E } } [ r ( s , a ) ] - \mathbb { E } _ { \rho _ { \pi } } [ r ( s , a ) ] - H ( \pi ) - \psi ( r )$ and

$\mathcal { J } ( \pi , Q ) = \mathbb { E } _ { \rho _ { E } } [ ( \widetilde { \mathcal { T } ^ { \pi } Q } ) ( s , a ) ] - \mathbb { E } _ { \rho _ { \pi } } [ ( \widetilde { \mathcal { T } ^ { \pi } Q } ) ( \widetilde { s } , a ) ] - \widetilde { H } ( \pi ) - \widetilde { \psi } ( \mathcal { T } ^ { \pi } \widetilde { Q } )$ , then for all policies $\pi \in \Pi$

$$
L (\pi , r) = \mathcal {J} (\pi , (\mathcal {T} ^ {\pi}) ^ {- 1} r)   \forall r \in \mathcal {R}, \text {and} \mathcal {J} (\pi , Q) = L (\pi , \mathcal {T} ^ {\pi} Q)   \forall Q \in \Omega .
$$

The proof follows directly from Lemma 3.2. These lemmas allow us to adapt the Inverse RL objective $L ( \pi , r )$ to learning Q through $\mathcal { J } ( \pi , Q )$ , i.e., working in the Q-policy space.

We can simplify the new objective $\mathcal { J } ( \pi , Q )$ by working with initial states $s _ { 0 }$ sampled from the initial state distribution $p _ { 0 } ( s )$ (Lemma $\mathrm { A } . 2$ in Appendix) as follows:

$$
\mathcal {J} (\pi , Q) = \mathbb {E} _ {(s, a) \sim \rho_ {E}} [ Q (s, a) - \gamma \mathbb {E} _ {s ^ {\prime} \sim \mathcal {P} (\cdot | s, a)} V ^ {\pi} (s ^ {\prime}) ] - (1 - \gamma) \mathbb {E} _ {s _ {0} \sim p _ {0}} [ V ^ {\pi} (s _ {0}) ] - \psi (\mathcal {T} ^ {\pi} Q),\tag{5}
$$

where again $\begin{aligned}V^{\pi}(s) = \mathbb{E}_{a \sim \pi(\cdot | s)} \left[ Q(s, a) - \log \pi(a | s) \right]\end{aligned}$

We are now ready to study $\mathcal { J } ( \pi , Q )$ , the Inverse RL problem in the Q-policy space. As the regularizer $\psi$ depends on both $Q$ and $\pi ,$ a general analysis over all functions in $\mathbb { R } ^ { \mathcal { S } \times \mathcal { A } }$ becomes too difficult. We restrict ourselves to regularizers induced by a convex function $g : \mathbb { R } \rightarrow \overline { { \mathbb { R } } }$ such that

$$
\psi_ {g} (r) = \mathbb {E} _ {\rho_ {E}} [ g (r (s, a)) ].\tag{6}
$$

This allows us to simplify our analysis to the set of all real functions while retaining generality<sup>2</sup>. We further motivate this choice in Section 4.

**Proposition 3.4.** In the Q-policy space, there exists a unique saddle point $( \pi ^ { * } , Q ^ { * } )$ that optimizes $\mathcal { I }$ i.e. $Q ^ { * } =$ argma $\mathbf { x } _ { Q \in \Omega }$ min<sub>π</sub>∈Π $\mathcal { J } ( \pi , Q )$ and $\pi ^ { * } = \operatorname { a r g m i n } _ { \pi \in \Pi }$ max<sub>Q</sub>∈Ω $\mathcal { J } ( \pi , Q )$ . Furthermore, $\pi ^ { * }$ and $r ^ { * } = { \mathcal { T } ^ { \pi } } ^ { * } Q ^ { * }$ are the solution to the Inverse RL objective $L ( \pi , r )$

Thus we have, maxQ∈Ω minπ∈Π $\mathcal { J } ( \pi , Q )   =   \operatorname * { m a x } _ { r \in \mathcal { R } }$ minπ∈Π $L ( \pi , r )$ . And the maxima $Q ^ { * }$ is simply the optimal soft Q-function for the reward $r ^ { * }$

This tells $\mathbf { u } \mathbf { s } ,$ even after transforming to Q-functions we have retained the saddle point property of the original IRL objective and optimizing $\mathcal { J } ( \pi , Q )$ recovers this saddle point. In the $Q -  policy$ space, we can get an additional property:

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280"><sup>2</sup>Averaging over the expert occupancy allows ψ to adjust to arbitrary experts and accommodate multimodality.</span></small>

**Proposition 3.5.** For a fixed $Q ,$ argmin ${ } _ { \cdot \pi \in \Pi } \; { \mathcal { J } } ( \pi , Q )$ is simply the solution to max entropy RL with rewards $r = \mathcal { T } ^ { \pi } Q$ . Thus, using $E q . \; I ,$ , the argmin policy satisfies

$$
\pi_ {Q} (a | s) = \frac {1}{Z _ {s}} \exp (Q (s, a)),
$$

with normalization factor $\begin{array} { r } { Z _ { s } = \sum _ { a } \exp Q ( s , a ) } \end{array}$ . Thus, the policy minima for a given $Q$ describes a manifold in the Q-policy space $( F i g u r e ~ I )$

Proposition 3.4 and 3.5 tell us that if we know $Q ,$ then the inner optimization problem in terms of policy is trivial, and obtained in a closed form! Thus, we can recover an objective that only requires learning Q:

$$
\max _ {Q \in \Omega} \min _ {\pi \in \Pi} \mathcal {J} (\pi , Q) = \max _ {Q \in \Omega} \mathcal {J} (\pi_ {Q}, Q)\tag{7}
$$

Lastly, we have:

**Proposition 3.6.** Let $\mathcal { J } ^ { * } ( Q ) = \mathcal { J } \left( \pi _ { Q } , Q \right)$ . Then the new objective $\mathcal { T } ^ { * }$ is concave in $Q .$ .

Thus, this new optimization objective is well-behaved and has a unique maxima $Q ^ { * }$ that gives the required saddle point as $( \pi _ { Q ^ { * } } , Q ^ { * } )$

In Appendix C we expand on our analysis and characterize the behavior for different choices of regularizer $\psi ,$ while giving proofs of all our propositions. Figure 1 summarizes the properties for the IRL objective: there exists an optimal policy manifold depending on $Q ,$ allowing optimization along it (using $\mathcal { T } ^ { * } )$ to con-

![](images/page_4_chart_9.jpg)

![](images/page_4_chart_10.jpg)

Figure 1: Properties of IRL objective in reward-policy space and Q-policy space.

verge to the saddle point. We further present analysis of IL methods that learn Q-functions like SQIL [33] and ValueDICE [22] and find subtle fallacies affecting their learning.

Note that although the same analysis holds in the reward-policy space, the optimal policy manifold depends on Q, which isn’t trivially known unlike when we work directly in the Q-policy space.

## 4 Approach

In this section, we develop our inverse soft-Q learning (IQ-Learn) algorithm, such that it recovers the optimal soft Q-function for an MDP from a given expert distribution. We start by learning energy-based models for the policy similar to soft Q-learning and later learn an explicit policy similar to actor-critic methods.

## 4.1 General Inverse RL Objective

For designing a practical algorithm using regularizers of the form $\psi _ { g }$ (from Eq. 6), we define $g$ using a concave function $\phi : \mathcal { R } _ { \psi } \rightarrow \mathbb { R }$ , such that $g ( x ) = { \left\{ \begin{array} { l l } { x - \phi ( x ) } & { { \mathrm { ~ i f ~ } } x \in { \mathcal { R } } _ { \psi } } \\ { + \infty } & { { \mathrm { ~ o t h e r w i s e ~ } } } \end{array} \right. }$ with the rewards constrained in $R _ { \psi }$

For this choice of ψ, the Inverse RL objective $L ( \pi , r )$ takes the form of Eq. 4 with a distance measure:

$$
d _ {\psi} (\rho , \rho_ {E}) = \max _ {r \in \mathcal {R} _ {\psi}} \mathbb {E} _ {\rho_ {E}} [ \phi (r (s, a)) ] - \mathbb {E} _ {\rho} [ r (s, a) ],\tag{8}
$$

This forms a general learning objective that allows the use of a wide-range of statistical distances including Integral Probability Metrics (IPMs) and f-divergences (see Appendix B).<sup>3</sup>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">R.</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280"><sup>3</sup>We recover IPMs when using identity φ and restricted reward family</span></small>

## 4.2 Choice of Statistical Distances

While choosing a practical regularizer, it can be useful to obtain certain properties on the reward functions we recover. Some (natural) nice properties are: having rewards bounded in a range, learning smooth functions or enforcing a norm-penalty.

In fact, we find these properties correspond to the Total Variation distance, the Wasserstein-1 distance and the $\chi ^ { 2 }$ -divergence respectively. The regularizers and the induced statistical distances are summarized in Table $2 ;$

Table 2: Enforced reward property, corresponding regularizer ψ and statistical distance $( R _ { \operatorname* { m a x } } , K , \alpha \in \mathbb { R } ^ { + } )$

| Reward Property | ψ | d<sub>ψ</sub> |
| --- | --- | --- |
| Bound range | ψ = 0 if \|r\| ≤ R<sub>max</sub> and +∞ otherwise | 2R<sub>max</sub> · TV(ρ,ρ<sub>E</sub>) |
| Smoothness | ψ = 0 if krk<sub>Lip</sub> ≤ K and +∞ otherwise | K · W<sub>1</sub>(ρ,ρ<sub>E</sub>) |
| L2 Penalization | ψ(r) = αr<sup>2</sup> | 41α · χ2(ρ,ρE) |

We find that these choices of regularizers<sup>4</sup> work very well in our experiments. In Appendix B, we further give a table for the well known f-divergences, the corresponding $\phi$ and the learnt reward estimators, along with a result ablation on using different divergences. Compared to $\chi ^ { 2 }$ , we find other f-divergences like Jensen-Shannon result in similar performances but are not as readily interpretable.

## 4.3 Inverse soft-Q update (Discrete control)

Optimization along the optimal policy manifold gives the concave objective (Prop 3.6):

$$
\max _ {Q \in \Omega} \mathcal {J} ^ {*} (Q) = \mathbb {E} _ {\rho_ {E}} [ \phi (Q (s, a) - \gamma \mathbb {E} _ {s ^ {\prime} \sim \mathcal {P} (\cdot | s, a)} V ^ {*} (s ^ {\prime})) ] - (1 - \gamma) \mathbb {E} _ {\rho_ {0}} [ V ^ {*} (s _ {0}) ],\tag{9}
$$

with $\begin{array} { r } { V ^ { * } ( s ) = \log \sum _ { a } \exp Q ( s , a ) } \end{array}$

For each $Q ,$ we get a corresponding reward $\begin{array} { r } { r ( s , a ) = Q ( s , a )   -   \gamma \mathbb { E } _ { s ^ { \prime } \sim \mathcal { P } ( \cdot | s , a ) } [ \log \sum _ { a ^ { \prime } } \exp Q \left( s ^ { \prime } , a ^ { \prime } \right) ] } \end{array}$ This correspondence is unique (Lemma C.3 in Appendix), and every update step can be seen as finding a better reward for IRL.

Note that estimating $V ^ { * } ( s )$ exactly is only possible in discrete action spaces. Our objective forms a variant of soft-Q learning: to learn the optimal Q-function given an expert distribution.

## 4.4 Inverse soft actor-critic update (Continuous control)

In continuous action spaces, it might not be possible to exactly obtain the optimal policy $\pi _ { Q }$ , which forms an energy-based model of the Q-function, and we use an explicit policy π to approximate $\pi _ { Q }$

For any policy π, we have a objective (from Eq. 5):

$$
\mathcal {J} (\pi , Q) = \mathbb {E} _ {\rho_ {E}} [ \phi (Q - \gamma \mathbb {E} _ {s ^ {\prime} \sim \mathcal {P} (\cdot | s, a)} V ^ {\pi} (s ^ {\prime})) ] - (1 - \gamma) \mathbb {E} _ {\rho_ {0}} [ V ^ {\pi} (s _ {0}) ].\tag{10}
$$

For a fixed $Q ,$ soft actor-critic (SAC) update: ma $\operatorname { x } \mathbb { E } _ { s \sim \mathcal { D } , a \sim \pi ( \cdot | s ) } [ Q ( s , a ) - \operatorname { l o g } \pi ( a | s ) ]$ , brings π π closer to $\pi _ { Q }$ while always minimizing Eq. 10 (Lemma $\mathrm { A } . 3$ in Appendix). Here $\mathcal { D }$ is the distribution of previously sampled states, or a replay buffer.

Thus, we obtain the modified actor-critic update rule to learn $Q _ { 1 }$ functions from the expert distribution:

1. For a fixed $\pi ,$ optimize Q by maximizing $\mathcal { J } ( \pi , Q )$

2. For a fixed Q, apply SAC update to optimize π towards $\pi _ { Q }$

This differs from ValueDICE [22], where the actor is updated adverserially and the objective may not always converge (Appendix C).

## 5 Practical Algorithm

Algorithm 1 shows our Q-learning and actor-critic variants, with differences with conventional RL algorithms in red (we optimize $- \check { \mathcal { T } }$ to use gradient descent). We can implement our algorithm IQ Learn in **15** lines of code on top of standard implementations of (soft) DQN [14] for discrete control or soft actor-critic (SAC) [13] for continuous control, with a change on the objective for the Q-function. Default hyperparameters from [14, 13] work well, except for tuning the entropy regularization. Target networks were helpful for continuous control. We elaborate details in Appendix D.

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280"><sup>4</sup>The additional scalar terms scale the entropy regularization strength and can be ignored in practice.</span></small>

## 5.1 Training methodology

Corollary A.1.1 states $\begin{aligned} { \begin{array} { l l } { \mathbb { E } _ { ( s , a ) \sim \mu } [ V ^ { \pi } ( s ) - \gamma \mathbb { E } _ { s ^ { \prime } \sim \mathcal { P } ( \cdot | s , a ) } V ^ { \pi } ( s ^ { \prime } ) ] = } & { ( 1 - \gamma ) \mathbb { E } _ { s \sim p _ { 0 } } [ V ^ { \pi } ( s ) ] } \\ \end{array} } \\ \end{aligned}$ , where $\mu$ is any policy’s occupancy. We use this to stabilize training instead of using Eq. 9 directly.

**Online**: Instead of directly estimating $\mathbb { E } _ { p _ { 0 } } [ V ^ { \pi } ( s _ { 0 } ) ]$ in our algorithm, we can sample $( s , a , s ^ { \tilde { \prime } } )$ from a replay buffer and get a single-sample estimate $\widetilde { \mathbb { E } _ { ( s , a , s ^ { \prime } ) \sim \mathrm { r e p l a y } } [ V ^ { \pi } ( s ) - \gamma V ^ { \pi } ( s ^ { \prime } ) ] }$ This removes the issue where we are only optimizing Q in the inital states resulting in overfitting of $V ^ { \pi } ( s _ { 0 } )$ , and improves the stability for convergence in our experiments. We find sampling half from the policy buffer and half from the expert distribution gives the best performances. Note that this is makes our learning online, requiring environment interactions.

**Offline**: Although $\mathbb { E } _ { p _ { 0 } } [ V ^ { \pi } ( s _ { 0 } ) ]$

<div class="docvortex-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Algorithm 1 Inverse soft Q-Learning (both variants)
Initialize Q-function $Q_{\theta}$, and optionally a policy $\pi_{\phi}$
for step $t$ in $\{1...N\}$ do
    Train Q-function using objective from Equation 9:
        $\theta_{t+1} \leftarrow \theta_t - \alpha_Q \nabla_{\theta}[-\mathcal{J}(\theta)]$
        (Use $V^*$ for Q-learning and $V^{\pi_{\phi}}$ for actor-critic)
    (only with actor-critic) Improve policy $\pi_{\phi}$ with SAC style actor update:
        $\phi_{t+1} \leftarrow \phi_t + \alpha_\pi \nabla_{\phi} \mathbb{E}_{s \sim \mathcal{D}, a \sim \pi_{\phi}(\cdot|s)}[Q(s, a) - \log \pi_{\phi}(a|s)]$
end for
</div>

<div class="docvortex-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Algorithm 2 Recover policy and reward
Given trained Q-function $Q_{\theta}$, and optionally a trained policy $\pi_{\phi}$
Recover policy $\pi$:
    (Q-learning) $\pi := \frac{1}{Z} \exp Q_{\theta}$
    (actor-critic) $\pi := \pi_{\phi}$
For state s, action a and $s' \sim \mathcal{P}(\cdot | \mathbf{s}, \mathbf{a})$
Recover reward $r(\mathbf{s}, \mathbf{a}, \mathbf{s}') = Q_{\theta}(\mathbf{s}, \mathbf{a}) - \gamma V^{\pi}(\mathbf{s}')$
</div>

serve an overfitting issue. Instead of requiring policy samples we use only expert samples to estimate $\mathbb { E } _ { ( s , a , s ^ { \prime } ) \sim \mathsf { e x p e r t } } [ \bar { V ^ { \pi } ( s ) } - \gamma V ^ { \pi } ( s ^ { \prime } ) ]$ to sufficiently approximate the term. This methodology gives us state-of-art results for offline IL.

## 5.2 Recovering rewards

Instead of the conventional reward function $r ( s , a )$ on state and action pairs, our algorithm allows recovering rewards for each transition $( s , a , s ^ { \prime } )$ using the learnt Q-values as follows:

$$
r (s, a, s ^ {\prime}) = Q (s, a) - \gamma V ^ {\pi} \left(s ^ {\prime}\right)\tag{11}
$$

Now, $\begin{aligned} { \mathbb { E } _ { s ^ { \prime } \sim \mathcal { P } ( \cdot | s , a ) } [ Q ( s , a ) - \gamma V ^ { \pi } \left( s ^ { \prime } \right) ] = } & { { } ~ Q ( s , a ) - \gamma \mathbb { E } _ { s ^ { \prime } \sim \mathcal { P } ( \cdot | s , a ) } [ V ^ { \pi } \left( s ^ { \prime } \right) ] = \mathcal { T } ^ { \pi } Q ( s , a ) } \\ \end{aligned}$ . This is just the reward function $r ( s , a )$ we want. So by marginalizing over next-states, our expression correctly recovers the reward over state-actions. Thus, Eq. 11 gives the reward over transitions.

Our rewards require $s ^ { \prime }$ which can be sampled from the environment, or by using a dynamics model.

## 5.3 Implementation of Statistical Distances

Implementing TV and $W _ { 1 }$ distances is fairly trivial and we give details in Appendix B. For the $\chi ^ { 2 } .$ **-divergence**, we note that it corresponds to $\begin{array} { r } { \phi ( x ) = x - \frac { 1 } { 4 \alpha } \tilde { x ^ { 2 } } } \end{array}$ . On substituting in Eq. 9, we get

$$
\max _ {Q \in \Omega} \mathbb {E} _ {\rho_ {E}} [ (Q (s, a) - \gamma \mathbb {E} _ {s ^ {\prime} \sim \mathcal {P} (\cdot | s, a)} V ^ {*} (s ^ {\prime})) ] - (1 - \gamma) \mathbb {E} _ {p _ {0}} [ V ^ {*} (s _ {0}) ] - \frac {1}{4 \alpha} \mathbb {E} _ {\rho_ {E}} [ (Q (s, a) - \gamma \mathbb {E} _ {s ^ {\prime} \sim \mathcal {P} (\cdot | s, a)} V ^ {*} (s ^ {\prime})) ^ {2} ]
$$

In a fully offline setting, this can be further simplified as (using the offline methodology in Sec 5.1):

$$
\min _ {Q \in \Omega} - \mathbb {E} _ {\rho_ {E}} [ (Q (s, a) - V ^ {*} (s)) ] + \frac {1}{4 \alpha} \mathbb {E} _ {\rho_ {E}} [ (Q (s, a) - \gamma \mathbb {E} _ {s ^ {\prime} \sim \mathcal {P} (\cdot | s, a)} V ^ {*} (s ^ {\prime})) ^ {2} ]\tag{12}
$$

This is interestingly the same as the $Q _ { 1 }$ -learning objective in CQL [23], a state-of-art method for offline RL (using 0 rewards), and shares similarities with regularized behavior cloning [33].<sup>5</sup>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280"><sup>5</sup>The simplification to get Eq. (12) is not applicable in the online IL setting where our method differs.</span></small>

## 5.4 Learning state-only reward functions

Previous works like AIRL [10] propose learning rewards that are only function of the state, and claim that these form of reward functions generalize between different MDPs. We find our method can predict state-only rewards by using the policy and expert state-marginals with a modification to Eq. 9:

$$
\max _ {Q \in \Omega} \mathcal {J} ^ {*} (Q) = \mathbb {E} _ {s \sim \rho_ {E} (s)} \left[ \mathbb {E} _ {a \sim \pi (\cdot | s)} \left[ \phi \left(Q (s, a) - \gamma \mathbb {E} _ {s ^ {\prime} \sim \mathcal {P} (\cdot | s, a)} V ^ {*} \left(s ^ {\prime}\right)\right) \right] \right] - (1 - \gamma) \mathbb {E} _ {p _ {0}} \left[ V ^ {*} \left(s _ {0}\right) \right],
$$

with π being here a stop gradient of $\pi _ { Q }$ . Interestingly, our objective no longer depends on the the expert actions $\pi _ { E }$ and can be used for IL using only observations. For the sake of brevity, we expand on this in Appendix $\mathrm { A . 1 }$

## 6 Related Work

**Classical IL**: Imitation learning has a long history, with early works using supervised learning to match a policy’s actions to those of the expert [15, 35]. A significant advance was made with the formulation of IL as the composition of RL and IRL [29, 1, 43], recovering the expert’s policy by inferring the expert’s reward function, then finding the policy which maximizes reward under this reward function. These early approaches required a hand-designed featurization of the MDP, limiting their applicability to complex MDPs. In this setting, early approaches [9, 31] noted a formal equivalence between IRL and IL using an inverse Bellman operator similar to our own.

**Online IL**: More recent work aims to leverage the power of modern machine learning approaches to learn good featurizations and extend IL to complex settings. Recent work generally falls into one of two settings: online or offline. In the online setting, the IL algorithm is able to interact with the environment to obtain dynamics information. GAIL [17] takes the nested RL/IRL formulation of earlier work , optimizing over all reward functions with a convex regularizer. This results in the objective in Eq. (3), with a max-min adversarial problem similar to a GAN [11]. A variety of further work has built on this adversarial approach [21, 10, 3]. A separate line of work aims to simplify the problem in Eq. (3) by using a fixed r or π. In SQIL [33], r is chosen to be the 1-0 indicator on the expert demonstrations, while ASAF [4] takes the GAN approach and uses a discriminator (with role similar to r) of fixed form, consisting of a ratio of expert and learner densities. AdRIL [38] is a recent extension of SQIL, additionally assigning decaying negative reward to previous policy rollouts.

**Offline IL**: In the offline setting, the learner has no access to the environment. The simple behavioural cloning (BC) [34] approach is offline, but doesn’t use any dynamics information. ValueDICE [22] is a dynamics-aware offline approach with an objective somewhat similar to ours, motivated from minimization of a variational representation of the KL-divergence between expert and learner policies. ValueDICE requires adversarial optimization to learn the policy and Q-functions, with a biased gradient estimator for training. We show a way to recover a unbiased gradient estimate for the KL-divergence in Appendix C. The O-NAIL algorithm [2] builds on ValueDICE and combines with a SAC update to obtain a method that is similar to our algorithm described in section 4.4, with the specific choice of reverse KL-divergence as the relevant statistical distance. The EDM method [19] incorporates dynamics via learning an explicit energy based model for the expert state occupancy, although some theoretical details have been called into question (see [37] for details). The recent AVRIL approach [6] uses a variational method to solve a probabilistic formulation of IL, finding a posterior distribution over r and π. Illustrating the potential benefits of alternative distances for IL, the PWIL [7] algorithm gives a non-adversarial procedure to minimize the Wasserstein distance between expert and learned occupancies. The approach is specific to the primal form of the W<sub>1</sub>-distance, while our method (when used with the Wasserstein distance) targets the dual form.

## 7 Experiments

## 7.1 Experimental Setup

We compare IQ-Learn $( \mathrm { { ` I Q } ^ { \mathrm { { ' } ^ { \prime } } } } )$ to prior works on a diverse collection of RL tasks and environments - ranging from low-dimensional control tasks: CartPole, Acrobot, LunarLander - to more challenging continuous control MuJoCo tasks: HalfCheetah, Hopper, Walker and Ant. Furthermore, we test on the visually challenging Atari Suite with high-dimensional image inputs. We compare on offline IL - with no access to the the environment while training, and online IL - with environment access. We show results on $W _ { 1 }$ and $\chi ^ { 2 }$ as our statistical distances, as we found them more effective than TV distance. In all cases, we train until convergence and average over multiple seeds. Hyperparameter settings and training details are detailed in Appendix D.

## 7.2 Benchmarks

**Offline IL** We compare to the state-of-art IL methods EDM and AVRIL, following the same experimental setting as [6]. Furthermore, we compare with ValueDICE which also learns Q-functions, albeit with drawbacks such as adversarial optimization. We also experimented with SQIL, but found that it was not competitive in the offline setting. Finally, we utilize BC as an additional IL baseline.

**Online IL** We use MuJoCo and Atari environments and compare against state-of-art online IL methods: ValueDICE, SQIL and GAIL. We only show results on $\chi ^ { 2 }$ as $W _ { 1 }$ was harder to stabilize on complex environments<sup>6</sup>. Using target updates stabilizes the Q-learning on MuJoCo. For brevity, further online IL results are shown in Appendix D.

## 7.3 Results

![](images/page_8_chart_5.jpg)

![](images/page_8_chart_6.jpg)

![](images/page_8_chart_7.jpg)

Figure 2: Offline IL results. We plot the average environment returns vs the number of expert trajectories.

**Offline IL** We present results on the three offline control tasks in Figure 2. On all tasks, IQ strongly outperforms prior works we compare to in performance and sample efficiency. Using just one expert trajectory, we achieve expert performance on Acrobot and reach near expert on Cartpole.

**Mujoco Control** We present our results on the MuJoCo tasks using a single expert demo in Table 3. IQ achieves expert-level performance in all the tasks while outperforming prior methods like ValueDICE and GAIL. We did not find SQIL competitive in this setting, and skip it for brevity.

Table 3: Mujoco Results. We show our performance on MuJoCo control tasks using a single expert trajectory.

| Task | GAIL | DAC | ValueDICE | IQ (Ours) | Expert |
| --- | --- | --- | --- | --- | --- |
| Hopper Half-Cheetah Walker Ant Humanoid | 3252.53080.04013.72299.1232.6 | 3305.14080.64107.91437.5380.5 | 3312.13835.63842.61806.3644.5 | 3546.45076.65134.04362.95227.1 | 3532.75098.35274.54700.05312.8 |

**Atari** We present our results on Atari using 20 expert demos in Figure 3. We reach expert performance on Space Invaders while being near expert on Pong and Breakout. Compared to prior methods like SQIL, IQ obtains **3-7x** normalized score<sup>7</sup>and converges in ∼300k steps, being **3x** faster compared to Q-learning based RL methods that take more than 1M steps to converge. Other popular methods like GAIL and ValueDICE perform near random even with 1M env steps.

## 7.4 Recovered Rewards

IQ has the added benefit of recovering rewards and can be used for IRL. On Hopper task, our learned rewards have a Pearson correlation of **0.99** with the true rewards. In Figure 4, we visualize our recovered rewards in a simple grid environment. We elaborate details in Appendix D.

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">1</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">6χ2and W can be used together to still have a convex regularization and is more stable.</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280"><sup>7</sup>Normalized rewards are obtained by setting random behavior to 0 and expert one to 1.</span></small>

![](images/page_9_chart_0.jpg)

Figure 4: Reward Visualization. We use a discrete GridWorld environment with 5 possible actions: up, down, left, right, stay. Agent starts in a random state. (With 30 expert demos)

## 7.5 Robustness to Distribution Shifts

We find IQ to be robust to distribution shifts between the expert and policy occupanices, and detail experiments with shift in the initial state distributions as well as goal distributions in Appendix F. Overall we find that IQ shows good generalization performance to never seen before goals, and the capability to act as a meta-learner for IL.

## 8 Discussion and Outlook

We present a new principled framework for learning soft-Q functions for IL and recovering the optimal policy and the reward, building on past works in IRL [43]. Our algorithm IQ-Learn outperforms prior methods with very sparse expert data and scales to complex image-based environments. We also recover rewards highly correlated with actual rewards. It has applications in autonomous driving and complex decision-making, but proper considerations need to be taken into account to ensure safety and reduce uncertainty, before any deployment. Finally, human or expert data can have errors that can propagate. A limitation of our method is that our recovered rewards depend on the environment dynamics, preventing trivial use on reward transfer settings. One direction of future work could be to learn a reward model from the trained soft-Q model to make the rewards explicit.

## 9 Acknowledgements

We thank Kuno Kim and John Schulman for helpful discussions. We also thank Ian Goodfellow as some initial motivations for this work were developed under an internship with him.

## 10 Funding Transparency

This research was supported in part by NSF (#1651565, #1522054, #1733686), ONR (N00014-19-1-2145), AFOSR (FA9550-19-1-0024) and FLI.

## References

[1] Pieter Abbeel and Andrew Y Ng. Apprenticeship learning via inverse reinforcement learning. International conference on Machine learning (ICML), 2004. 1, 2, 8

[2] Oleg Arenz and Gerhard Neumann. Non-adversarial imitation learning and its connections to adversarial methods. arXiv preprint arXiv:2008.03525, 2020. 8

[3] Nir Baram, Oron Anschel, and Shie Mannor. Model-based adversarial imitation learning. stat, 1050:7, 2016. 8

[4] Paul Barde, Julien Roy, Wonseok Jeon, Joelle Pineau, Christopher Pal, and Derek Nowrouzezahrai. Adversarial soft advantage fitting: Imitation learning without policy optimization. Advances in neural information processing systems (NeurIPS), 2020. 2, 8

[5] M. Bloem and N. Bambos. Infinite time horizon maximum causal entropy inverse reinforcement learning. 53rd IEEE Conference on Decision and Control, pages 4911–4916, 2014. 3

[6] Alex J. Chan and Mihaela van der Schaar. Scalable bayesian inverse reinforcement learning, 2021. 8, 9, 24

[7] Robert Dadashi, Léonard Hussenot, Matthieu Geist, and Olivier Pietquin. Primal wasserstein imitation learning. In ICLR 2021-Ninth International Conference on Learning Representations, 2021. 8

[8] G Alphastar DeepMind. Mastering the real-time strategy game starcraft ii, 2019. 1

[9] Krishnamurthy Dvijotham and Emanuel Todorov. Inverse optimal control with linearly-solvable mdps. In ICML, 2010. 8

[10] Justin Fu, Katie Luo, and Sergey Levine. Learning robust rewards with adverserial inverse reinforcement learning. In International Conference on Learning Representations, 2018. URL [https://openreview.net/forum?id=rkHywl-A-](https://openreview.net/forum?id=rkHywl-A-). 1, 2, 8

[11] Ian J Goodfellow, Jean Pouget-Abadie, Mehdi Mirza, Bing Xu, David Warde-Farley, Sherjil Ozair, Aaron C Courville, and Yoshua Bengio. Generative adversarial nets. In NIPS, 2014. 8

[12] Ishaan Gulrajani, Faruk Ahmed, Martín Arjovsky, Vincent Dumoulin, and Aaron C. Courville. Improved training of wasserstein gans. In NIPS, 2017. 17

[13] T. Haarnoja, Aurick Zhou, P. Abbeel, and S. Levine. Soft actor-critic: Off-policy maximum entropy deep reinforcement learning with a stochastic actor. In ICML, 2018. 2, 3, 7, 16, 25

[14] Tuomas Haarnoja, Haoran Tang, Pieter Abbeel, and Sergey Levine. Reinforcement learning with deep energy-based policies. 2017. 2, 3, 6, 7, 18

[15] G HAYES. A robot controller using learning by imitation. In Proc. 2nd Int. Symposium on Intelligent Robotic Systems, LIFTA-IMAG, Grenoble, France, 1994. 8

[16] Michael Herman, Tobias Gindele, Jörg Wagner, Felix Schmitt, and Wolfram Burgard. Inverse reinforcement learning with simultaneous estimation of rewards and dynamics. International conference on artificial intelligence and statistics (AISTATS), 2016. 2

[17] Jonathan Ho and S. Ermon. Generative adversarial imitation learning. In NIPS, 2016. 1, 2, 3, 4, 8, 15

[18] Vinamra Jain, Prashant Doshi, and Bikramjit Banerjee. Model-free irl using maximum likelihood estimation. AAAI Conference on Artificial Intelligence (AAAI), 2019. 2

[19] Daniel Jarrett, Ioana Bica, and Mihaela van der Schaar. Strictly batch imitation learning by energy-based distribution matching. Advances in neural information processing systems (NeurIPS), 2020. 2, 8, 24

[20] Edouard Klein, Matthieu Geist, and Olivier Pietquin. Batch, off-policy and model-free apprenticeship learning. European Workshop on Reinforcement Learning (EWRL), 2011. 2

[21] Ilya Kostrikov, Kumar Krishna Agrawal, Debidatta Dwibedi, Sergey Levine, and Jonathan Tompson. Discriminator-actor-critic: Addressing sample inefficiency and reward bias in adversarial imitation learning. In International Conference on Learning Representations, 2018. 1, 8

[22] Ilya Kostrikov, Ofir Nachum, and Jonathan Tompson. Imitation learning via off-policy distribution matching. In International Conference on Learning Representations, 2020. URL [https://openreview.net/forum?id=Hyg-JC4FDr](https://openreview.net/forum?id=Hyg-JC4FDr). 1, 2, 5, 6, 8, 22

[23] Aviral Kumar, Aurick Zhou, George Tucker, and Sergey Levine. Conservative q-learning for offline reinforcement learning. 2020. URL [https://arxiv.org/abs/2006.04779](https://arxiv.org/abs/2006.04779). 2, 7

[24] Donghun Lee, Srivatsan Srinivasan, and Finale Doshi-Velez. Truly batch apprenticeship learning with deep successor features. International Joint Conference on Artificial Intelligence (IJCAI), 2019. 2

[25] Mario Lucic, Karol Kurach, Marcin Michalski, S. Gelly, and O. Bousquet. Are gans created equal? a large-scale study. In NeurIPS, 2018. 17

[26] Takeru Miyato, Toshiki Kataoka, Masanori Koyama, and Y. Yoshida. Spectral normalization for generative adversarial networks. ArXiv, abs/1802.05957, 2018. 17

[27] V. Mnih, K. Kavukcuoglu, D. Silver, A. Graves, Ioannis Antonoglou, Daan Wierstra, and Martin A. Riedmiller. Playing atari with deep reinforcement learning. ArXiv, abs/1312.5602, 2013. 24, 25

[28] Ofir Nachum, Yinlam Chow, B. Dai, and L. Li. Dualdice: Efficient estimation of off-policy stationary distribution corrections. 2019. 15

[29] Andrew Y Ng, Stuart J Russell, et al. Algorithms for inverse reinforcement learning. International conference on Machine learning (ICML), 2000. 1, 2, 8

[30] Bilal Piot, Matthieu Geist, and Olivier Pietquin. Boosted and reward-regularized classification for apprenticeship learning. International conference on Autonomous agents and multi-agent systems (AAMAS), 2014. 2

[31] Bilal Piot, Matthieu Geist, and Olivier Pietquin. Bridging the gap between imitation learning and inverse reinforcement learning. IEEE transactions on neural networks and learning systems, 28(8):1814–1826, 2016. 8

[32] Antonin Raffin. Rl baselines3 zoo. [https://github.com/DLR-RM/rl-baselines3-zoo](https://github.com/DLR-RM/rl-baselines3-zoo),2020. 24

[33] Siddharth Reddy, A. Dragan, and S. Levine. Sqil: Imitation learning via reinforcement learning with sparse rewards. arXiv: Learning, 2020. 1, 2, 5, 7, 8, 22, 29

[34] Stéphane Ross and Drew Bagnell. Efficient reductions for imitation learning. International conference on artificial intelligence and statistics (AISTATS), 2010. 1, 2, 8, 27, 28

[35] Claude Sammut, Scott Hurst, Dana Kedzier, and Donald Michie. Learning to fly. In Proceedings of the Ninth Conference on Machine Learning, pages 385–393. Elsevier, 1992. 8

[36] Maurice Sion. On general minimax theorems. Pacific Journal of Mathematics, 8(1):171 – 176, 1958. doi: pjm/1103040253. URL [https://doi.org/](https://doi.org/).

[37] Gokul Swamy, Sanjiban Choudhury, J. Andrew Bagnell, and Zhiwei Steven Wu. A Critique of Strictly Batch Imitation Learning. arXiv:2110.02063 [cs], October 2021. 8

[38] Gokul Swamy, Sanjiban Choudhury, Zhiwei Steven Wu, and J Andrew Bagnell. Of moments and matching: Trade-offs and treatments in imitation learning. arXiv preprint arXiv:2103.03236, 2021. 8

[39] Lu Wang, Wenchao Yu, Xiaofeng He, Wei Cheng, Martin Renqiang Ren, Wei Wang, Bo Zong, Haifeng Chen, and Hongyuan Zha. Adversarial cooperative imitation learning for dynamic treatment regimes. In Proceedings of The Web Conference 2020, pages 1785–1795, 2020. 1

[40] Lantao Yu, Tianhe Yu, Chelsea Finn, and Stefano Ermon. Meta-inverse reinforcement learning with probabilistic context variables. In NeurIPS, 2019. 29

[41] Jinyun Zhou, Rui Wang, Xu Liu, Yifei Jiang, Shu Jiang, Jiaming Tao, Jinghao Miao, and Shiyu Song. Exploring imitation learning for autonomous driving with feedback synthesizer and differentiable rasterization. arXiv preprint arXiv:2103.01882, 2021. 1

[42] Brian D Ziebart. Modeling purposeful adaptive behavior with the principle of maximum causal entropy. 2010. 3

[43] Brian D. Ziebart, Andrew L. Maas, J. Bagnell, and A. Dey. Maximum entropy inverse reinforcement learning. In AAAI, 2008. 2, 8, 10, 26

![](images/page_13_image_1.jpg)

Figure 5: State Rewards Visualization. We visualize the state-only rewards recovered on a continuous control point maze task. The agent (white circle) has to reach the goal (red star) avoiding the barrier on right.

## A.1 Learning with state-only rewards

For a policy $\pi   \in   \Pi .$ , we define its state-marginal occupancy measure $\rho _ { \pi }   :   \mathcal { S }   \to   \mathbb { R }$ as $\rho _ { \pi } ( s )   =$ $\begin{array} { r } { \left( 1 - \gamma \right) \sum _ { t = 0 } ^ { \infty } \gamma ^ { t } P \left( s _ { t } = s | \pi \right) } \end{array}$

Suppose we are interested in learning rewards that are functions of only the states, then the Inverse-RL objective $L$ from Eq. 3 becomes a function of the state-marginal occupancies:

$$
\max _ {r \in \mathcal {R} _ {\psi}} \min _ {\pi \in \Pi} L _ {s} (\pi , r) = \mathbb {E} _ {s \sim \rho_ {E} (s)} [ \phi (r (s)) ] - \mathbb {E} _ {s \sim \rho (s)} [ r (s) ] - H (\pi).\tag{13}
$$

Now, we can parameterize the rewards $r ( s )$ using state-only value-functions $V ( s )$ and remove the dependency on $Q ( s , a )$ . Then $V ( s )$ can be learnt similar to learning $Q ( s , a )$ in the main paper, but $Q ( s , a )$ remains unknown and the optimal policy cannot be obtained simply as an energy-based model of $Q$

Instead, we develop a new objective that can learn $Q$ while recovering state-only rewards below.

We expand the original objective L using the expert occupancy:

$$
L (\pi , r) = \mathbb {E} _ {s \sim \rho_ {E} (s)} \mathbb {E} _ {a \sim \pi_ {E} (\cdot | s)} \left[ \phi (r (s, a)) - \frac {\rho (s) \pi (a | s)}{\rho_ {E} (s) \pi_ {E} (a | s)} r (s, a)) \right] - H (\pi).
$$

We see that the action dependency comes in the equation from the fact that we have $\pi / \pi _ { E }$ inside.

Now, we propose to fix the expression to make it independent of actions by replacing the expert policy $\pi _ { E }$ with the policy π. The new objective becomes:

$$
L ^ {\prime} (\pi , r) = \mathbb {E} _ {s \sim \rho_ {E} (s)} \mathbb {E} _ {a \sim \pi (\cdot | s)} \left[ \phi (r (s, a)) - \frac {\rho (s)}{\rho_ {E} (s)} r (s, a) \right] - H (\pi).
$$

Then for a fixed policy $\pi ,$ while maximizing over r the constraint we have is that each reward component $r ( s , a ) \in R _ { \psi }$ . In a state $s , r ( s , a )$ that maximizes the objective will take the same value independent of the action<sup>8</sup>. Thus, the expectation over actions can be removed and this recovers Eq. 13.

Writing the new objective using Q-functions, we get the modification to Eq. 9:

$$
\max _ {Q \in \Omega} \mathcal {J} ^ {*} (Q) = \mathbb {E} _ {s \sim \rho_ {E} (s)} [ \mathbb {E} _ {a \sim \pi (\cdot | s)} [ \phi (Q (s, a) - \gamma \mathbb {E} _ {s ^ {\prime} \sim P (s, a)} V ^ {*} (s ^ {\prime})) ] ] - (1 - \gamma) \mathbb {E} _ {p _ {0}} [ V ^ {*} (s _ {0}) ],\tag{14}
$$

with π set to stop $\mathrm { \_ g r a d } ( \pi _ { Q } )$ to prevent passing gradients through it.

This new objective does not depend on the the expert actions $\pi _ { E }$ and can be used for IL using only observations (ILO). We visualize state-only rewards recovered on a 2D point mass navigation task in Fig 5. Notice that the rewards are not directional and are high on all sides of the target point, indicating they are not dependent on the action. We present additional results in Appendix D and a theoretical guarantee in Appendix C.4.

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280"><sup>8</sup>The objective and the reward constraints remain same along each action dimension and a symmetry argument holds.</span></small>

## A.2 Proofs for Section 3 and Section 4

**Proof for Lemma 3.2.** Let $P ^ { \pi }$ be the (stochastic) transition matrix for the MDP corresponding to a policy π, such that for any $\begin{aligned} { \underset {} { x \in \mathbb { R } ^ { \mathcal { S } \times \mathcal { A } } , P ^ { \pi } x ( s , a ) } { \overset { } { = } } \mathbb { E } _ { s ^ { \prime } \sim \mathcal { P } ( \cdot | s , a ) , a ^ { \prime } \sim \pi ( \cdot | s ^ { \prime } ) } \left[ x ( s ^ { \prime } , a ^ { \prime } ) \right] } \\ \end{aligned}$

Let $r   =   \mathcal { T } ^ { \pi } Q$ for any $Q   \in   \mathbb { R } ^ { \mathcal { S } \times \mathcal { A } }$ . We expand $\mathcal { T } ^ { \pi }$ in vector form over $\mathcal { S } \times \mathcal { A }$ using $P ^ { \pi }$ . Then $\pmb { r }   =   \pmb { Q }   -   \gamma P ^ { \pi } ( \pmb { Q }   -   \log \pi )$ . Here, $( I - \gamma \bar { P } ^ { \pi } )$ is invertible as $\| \gamma P ^ { \pi } \|   <   1$ , for $\gamma < 1$ , and the corresponding Neumann series converges. Thus $\boldsymbol { Q } = \left( I - \gamma P ^ { \pi } \right) ^ { - 1 } \left( \boldsymbol { r } - \log \pi \right) + \log \pi$ . So we see that for any $\tilde { r \in \mathbb { R } ^ { \mathcal { S } \times \mathcal { A } } }$ , there exists a unique preimage $Q \in \mathbb { R } ^ { \mathcal { S } \dot { \times } \mathcal { A } }$ proving that $\mathcal { T } ^ { \pi }$ is a bijection.

Furthermore, on rearranging the vector form, we have $\pmb { Q } = \pmb { r } + \gamma P ^ { \pi } ( \pmb { Q } - \log \pmb { \pi } )$ . This is just the vector expansion of the soft-bellmann operator $\mathcal { B } _ { r } ^ { \pi }$ , which has a unique contraction $Q$ for a given r. Thus, $\stackrel { \cdot } { Q } \stackrel { \cdot } { = } ( \mathcal { T } ^ { \pi } ) ^ { - 1 } r = \mathcal { B } _ { r } ^ { \pi } Q$ for any $r \dot { \in } \mathbb { R } ^ { \mathcal { S } \times \mathcal { A } }$

**Lemma A.1.** Let the initial state distribution be $p _ { 0 } ( s )$ , then for a policy π and $V ^ { \pi }$ defined as before, we have

$$
\mathbb {E} _ {(s, a) \sim \rho_ {\pi}} [ V ^ {\pi} (s) - \gamma \mathbb {E} _ {s ^ {\prime} \sim \mathcal {P} (\cdot | s, a)} V ^ {\pi} (s ^ {\prime}) ] = (1 - \gamma) \mathbb {E} _ {s \sim p _ {0}} [ V ^ {\pi} (s) ].
$$

Proof. We expand the discounted stationary distribution $\rho$ over state-actions and show the series forms a telescopic sum. Let $p _ { t } ^ { \pi } ( s )$ be the marginal state distribution at time t for a policy π. Then,

$$
\begin{array}{r l} & {\mathbb {E} _ {(s, a) \sim \rho_ {\pi}} [ V ^ {\pi} (s) - \gamma \mathbb {E} _ {s ^ {\prime} \sim \mathcal {P} (\cdot | s, a)} V ^ {\pi} (s ^ {\prime}) ]} \\ & {= (1 - \gamma) \sum_ {t = 0} ^ {\infty} \gamma^ {t} \mathbb {E} _ {s \sim p _ {t} ^ {\pi}, a \sim \pi (s)} [ V ^ {\pi} (s) - \gamma \mathbb {E} _ {s ^ {\prime} \sim \mathcal {P} (\cdot | s, a)} V ^ {\pi} (s ^ {\prime}) ]} \\ & {= (1 - \gamma) \sum_ {t = 0} ^ {\infty} \gamma^ {t} \mathbb {E} _ {s \sim p _ {t} ^ {\pi}} [ V ^ {\pi} (s) ] - (1 - \gamma) \sum_ {t = 0} ^ {\infty} \gamma^ {t + 1} \mathbb {E} _ {s \sim p _ {t + 1} ^ {\pi}} [ V ^ {\pi} (s) ]} \\ & {= (1 - \gamma) \mathbb {E} _ {s \sim p _ {0}} [ V ^ {\pi} (s) ].} \end{array}
$$

**Corollary A.1.1.** In fact, for any valid occupancy measure $\mu$ over state-actions and $V ^ { \pi }$ , it holds that

$$
\mathbb {E} _ {(s, a) \sim \mu} [ V ^ {\pi} (s) - \gamma \mathbb {E} _ {s ^ {\prime} \sim \mathcal {P} (\cdot | s, a)} V ^ {\pi} (s ^ {\prime}) ] = (1 - \gamma) \mathbb {E} _ {s \sim \mathcal {P} _ {0}} [ V ^ {\pi} (s) ].
$$

Proof. This relies on the fact that $V ^ { \pi } ( s )$ is a function of only state and doesn’t depend on the action. First, for any valid occupancy measure $\mu ,$ there exists a corresponding unique policy $\beta ^ { \mu } ( a | s )$ s.t. $\beta ^ { \mu }$ generates $\mu$ [17].

Let $p _ { t } ^ { \mu } ( s )$ be the marginal state distribution at timestep t for the policy $\beta ^ { \mu }$ . Then,

$$
\begin{array}{r l} & {\mathbb {E} _ {(s, a) \sim \mu} [ V ^ {\pi} (s) - \gamma \mathbb {E} _ {s ^ {\prime} \sim \mathcal {P} (\cdot | s, a)} V ^ {\pi} (s ^ {\prime}) ]} \\ & {= (1 - \gamma) \sum_ {t = 0} ^ {\infty} \gamma^ {t} \mathbb {E} _ {s \sim p _ {t} ^ {\mu}, a \sim \beta^ {\mu} (s)} [ V ^ {\pi} (s) - \gamma \mathbb {E} _ {s ^ {\prime} \sim \mathcal {P} (\cdot | s, a)} V ^ {\pi} (s ^ {\prime}) ]} \\ & {= (1 - \gamma) \sum_ {t = 0} ^ {\infty} \gamma^ {t} \mathbb {E} _ {s \sim p _ {t} ^ {\mu}} [ V ^ {\pi} (s) ] - (1 - \gamma) \sum_ {t = 0} ^ {\infty} \gamma^ {t + 1} \mathbb {E} _ {s \sim p _ {t + 1} ^ {\mu}} [ V ^ {\pi} (s ^ {\prime}) ]} \\ & {= (1 - \gamma) \mathbb {E} _ {s \sim p _ {0} ^ {\mu}} [ V ^ {\pi} (s) ].} \end{array}
$$

Now $p _ { 0 } ^ { \mu }$ is just the initial state distribution $p _ { 0 }$ which is independent of the policy, thus giving our result.

**Lemma A.2.** $\begin{array} { r } { \mathbb { E } _ { \rho _ { \pi } } [ ( \mathcal { T } ^ { \pi } Q ) ( s , a ) ] + H ( \pi )   =   ( 1 - \gamma ) \mathbb { E } _ { p _ { 0 } } [ V ^ { \pi } ( s _ { 0 } ) ] } \end{array}$ , where $p _ { 0 } ( s )$ is the initial state distribution.

Proof. We can show this forms a telescopic series as in [28] using lemma $\mathrm { A . 1 }$ to depend only on the initial state distribution:

$$
\begin{array}{r l} \mathbb {E} _ {\rho_ {\pi}} [ Q (s, a) - \gamma \mathbb {E} _ {s ^ {\prime} \sim \mathcal {P} (\cdot | s, a)} V ^ {\pi} (s ^ {\prime}) ] + H (\pi) & = \mathbb {E} _ {\rho_ {\pi}} [ Q (s, a) - \gamma \mathbb {E} _ {s ^ {\prime} \sim \mathcal {P} (\cdot | s, a)} V ^ {\pi} (s ^ {\prime}) + H (\pi (a | s) ] \\ & = \mathbb {E} _ {\rho_ {\pi}} [ Q (s, a) - \log \pi (a | s) - \gamma \mathbb {E} _ {s ^ {\prime} \sim \mathcal {P} (\cdot | s, a)} V ^ {\pi} (s ^ {\prime}) ] \\ & = \mathbb {E} _ {\rho_ {\pi}} [ V ^ {\pi} (s) - \gamma \mathbb {E} _ {s ^ {\prime} \sim \mathcal {P} (\cdot | s, a)} V ^ {\pi} (s ^ {\prime}) ] \\ & = (1 - \gamma) \mathbb {E} _ {p _ {0}} [ V ^ {\pi} (s) ]. \end{array}
$$

This makes sense as the LHS and RHS both represent the max entropy RL objective, that is to maximize the cumulative sum of rewards or the expected value with respect to a policy for the initial state. □

**Lemma A.3.** SAC actor update decreases the objective $\mathcal { J } ( \pi , Q )$ for the actor-critic update in main paper, wrt π for a fixed $Q .$

Proof.

$$
V ^ {\pi} (s) = \mathbb {E} _ {a \sim \pi} [ Q (s, a) - \log \pi (a | s) ] = - D _ {K L} \left(\pi (\cdot | s) \| \frac {1}{Z _ {s}} \exp (Q (s, \cdot)\right) + \log (Z _ {s}),
$$

where $Z _ { s }$ is the normalizing factor $\textstyle \sum _ { a } \exp Q ( s , a )$

Now, for a policy $\pi ^ { \prime }$ the the SAC actor update rule [13] is arg min $\textstyle D _ { K L } \left( \pi ^ { \prime } \| \frac { 1 } { Z } \operatorname { e x p } ( Q ) \right)$

Thu ${ \bf l } { \bf S } ,$ if π is the policy obtained on applying the SAC actor update to $\pi ^ { \prime } ,$ , we have $V ^ { \pi } ( s ) > V ^ { \pi ^ { \prime } } ( s )$ . So, as long as φ in $\mathcal { T }$ is a monotonically non-decreasing function, this implies $\mathcal { J } ( \pi , Q ) \stackrel { \frown } { < } \mathcal { J } ( \pi ^ { \prime } , \dot { Q } )$ □

## B Appendix B

**Integral Probability Metric (IPM)** An IPM parameterized by $\mathcal { F }$ between two distributions $P$ and Q is defined as

$$
\left| \gamma_ {\mathcal {F}} (P, Q) := \sup _ {f \in \mathcal {F}} \left| \mathbb {E} _ {P} f (X) - \mathbb {E} _ {Q} f (X) \right| \right..\tag{15}
$$

Suppose $\mathcal { F }$ is such that $f \in { \mathcal { F } } \Rightarrow - f \in { \mathcal { F } }$ . Then,

$$
\gamma_ {\mathcal {F}} (P, Q) = \sup _ {f \in \mathcal {F}} | \mathbb {E} _ {P} f - \mathbb {E} _ {Q} f | = \sup _ {f \in \mathcal {F}} \mathbb {E} _ {P} f - \mathbb {E} _ {Q} f.\tag{16}
$$

Some IPMs that satisfy this symmetry are: Dudley metric, Wasserstein metric, total variation distance, Maximum Mean Discrepancy (MMD).

We can see that for $\phi = \mathcal { I } , R _ { \psi } = \mathcal { F }$ , Eq. 8 reduces to Eq. 16.

f**-divergence** The f-divergence between two distributions $P$ and $Q$ is defined using the convex conjugate $f ^ { * }$ as

$$
D _ {f} (P \| Q) = \mathbb {E} _ {Q} \left[ f \left(\frac {P}{Q}\right) \right] = \sup _ {g: \mathcal {X} \to \mathbb {R}} \mathbb {E} _ {P} [ g (X) ] - \mathbb {E} _ {Q} \left[ f ^ {*} (g (X)) \right].\tag{17}
$$

Interpreting $g = - r$

$$
D _ {f} (P \| Q) = \sup _ {r: \mathcal {X} \to \mathbb {R}} \mathbb {E} _ {P} [ - r (X) ] - \mathbb {E} _ {Q} \left[ f ^ {*} (- r (X)) \right]\tag{18}
$$

$$
= \sup _ {r: \mathcal {X} \to \mathbb {R}} \mathbb {E} _ {Q} \left[ - f ^ {*} (- r) \right] - \mathbb {E} _ {P} [ r ].\tag{19}
$$

Thus, for $\phi ( x ) = - f ^ { * } ( - x ) , R _ { \psi } = \mathbb { R } ^ { \mathcal { S } \times \mathcal { A } } ,$ , Eq. 8 reduces to Eq. 18.

Table 4: List of divergence functions, convex conjugates, φ and optimal reward estimators

<table><tbody><tr><td>Divergence</td><td>f(t)</td><td>f<sup>∗</sup>(u)</td><td>φ(x)</td><td>r</td></tr><tr><td rowspan="9">Forward KL Reverse KL Squared Hellinger Pearson χ<sup>2</sup>Total variation Jensen-Shannon</td><td rowspan="9">-log t tlog t (√t - 1)<sup>2</sup> (t - 1)<sup>2</sup> 12|t - 1| -(t + 1)log(t+21) + tlog t</td><td rowspan="5">-1 - log(-u) e(u-1)u</td><td rowspan="5">1 + log x -e-(x+1)x</td><td rowspan="9">ρρE -(1 + log ρρE ) qρρE - 12(1 - ρρE ) 12 sign(1 - ρρE ) log 12(1 + ρρE )</td></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr><td rowspan="4">1-u u + u42 u -log (2 - e<sup>u</sup>)</td><td rowspan="4">1+x x - x42 x log (2 - e-<sup>x</sup>)</td></tr><tr></tr><tr></tr><tr></tr></tbody></table>

## B.1 Implementation of Statistical Distances

**Total Variation** Total variation gives a constraint on reward functions: $\begin{array} { r } { | r | \leq \frac { 1 } { 2 } } \end{array}$

As $\begin{array} { r } { Q _ { t ^ { \prime } } = \sum _ { t = t ^ { \prime } } ^ { \infty } \gamma ^ { t } r ( s _ { t } , a _ { t } ) + \gamma ^ { t } H ( a _ { t } | s _ { t } ) } \end{array}$ , we obtain a constraint on $Q ;$

$$
| Q | \leq \frac {1}{1 - \gamma} (R _ {m a x} + \log | A |) = \frac {1}{1 - \gamma} (\frac {1}{2} + \log | A |)
$$

This can be easily enforced by bounding $Q$ to this range using a tanh activation.

$W _ { 1 }$ **Distance** For Wasserstein-1 distance, we use gradient penalty [12] to enforce the Lipschitz constraint, although other techniques like spectral normalization [26] can also be utilized.

$\chi ^ { 2 } \mathbf { - d i v e r g e n c e } \quad \chi ^ { 2 }$ **-divergence** corresponds to an f-divergence with a choice of $f(x) = (x - 1)^{2}$ We generalize this to a choice of $f(x) = \alpha(x - 1)^{2}$ with $\alpha > 0 ,$ which scales the original divergence by a constant factor of α.

Then $\begin{array} { r } { \phi ( x ) = - f ^ { * } ( - x ) = x - \frac { 1 } { 4 \alpha } x ^ { 2 } } \end{array}$ . It corresponds to using a (strong) convex reward regularizer $\begin{array} { r } { \psi ( r ) = \frac { 1 } { 4 \alpha } r ^ { 2 } } \end{array}$

## B.2 Effect of different Divergences

![](images/page_16_chart_9.jpg)

Figure 6: Divergence ablation. We show environment returns for different divergences on LunarLander.

We test IQ-Learn with different divergences: Jensen-Shannon (JS), Hellinger, KL and $\chi ^ { 2 }$ divergence. We use the LunarLander environment with our offline IL experimental settings and a single expert trajectory. All experiments are repeated over 10 seeds. We show a box-plot of the environment returns for different divergences and find that JS, Hellinger and $\chi ^ { 2 }$ divergence perform similarly, consistent with the findings on different type of GANs [25]. Here, KL-divergence performs worse and is suboptimal compared to the other divergences.

## C Appendix C

In this section, we expand over our analysis in Section 3 and present proof of properties over the Q-policy space: Propositions 3.4, 3.5, 3.6 in main paper.

For simplicity, we define a concave function $\phi : \mathbb { R } \to \mathbb { R } \cup \{ - \infty \}$ such that $g$ is given as $g ( x )   : =   x   -   \phi ( x )$ , same as in Section 4 of the main paper. We are interested in regularizers $\psi$ induced by $g ,$ such that

$$
\psi_ {g} (r) = \mathbb {E} _ {\rho_ {E}} [ g (r (s, a)) ].\tag{20}
$$

We simplify the IRL objective (from Eq. 5):

$$
\begin{array}{r l} \mathcal {J} (\pi , Q) & = \mathbb {E} _ {\rho_ {E}} [ \mathcal {T} ^ {\pi} Q ] - (1 - \gamma) \mathbb {E} _ {p _ {0}} [ V ^ {\pi} (s _ {0}) ] - \psi (\mathcal {T} ^ {\pi} Q) \\ & = \mathbb {E} _ {\rho_ {E}} [ \mathcal {T} ^ {\pi} Q ] - (1 - \gamma) \mathbb {E} _ {\rho_ {0}} [ V ^ {\pi} (s _ {0}) ] - \mathbb {E} _ {\rho_ {E}} [ \mathcal {T} ^ {\pi} Q - \phi (\mathcal {T} ^ {\pi} Q) ] \\ & = \mathbb {E} _ {\rho_ {E}} [ \phi (Q - \gamma \mathbb {E} _ {s ^ {\prime} \sim \mathcal {P} (\cdot | s, a)} V ^ {\pi} (s ^ {\prime})) ] - (1 - \gamma) \mathbb {E} _ {\rho_ {0}} [ V ^ {\pi} (s _ {0}) ]. \end{array}
$$

**Lemma C.1.** $\mathcal { J } ( \pi , \cdot )$ is concave for all $\pi \in \Pi$

Proof. Let $Q _ { 1 } , Q _ { 2 } \in \Omega$ and suppose $\lambda \in [ 0 , 1 ]$ . We rely on the fact that the regularized IRL objective $L ( \pi , \cdot )$ is concave for all $\pi .$ Note that $r = \mathcal { T } ^ { \pi } Q$ is an affine transform of $Q ,$ given in vector form as $\boldsymbol{r}-\log \boldsymbol{\pi}=\left(I-P^{\pi}\right) \boldsymbol{Q}.$ Thus, $\begin{array} { r l } { \mathcal { T } ^ { \pi } ( \lambda Q _ { 1 } + ( 1 - \lambda ) Q _ { 2 } ) = \lambda \mathcal { T } ^ { \pi } Q _ { 1 } + ( 1 - \lambda ) \mathcal { T } ^ { \pi } Q _ { 2 } } \\ \end{array}$

$$
\begin{array}{r l} \mathcal {J} (\pi , \lambda Q _ {1} + (1 - \lambda) Q _ {2}) & = L (\pi , \mathcal {T} ^ {\pi} (\lambda Q _ {1} + (1 - \lambda) Q _ {2})) \\ & = L (\pi , \lambda \mathcal {T} ^ {\pi} Q _ {1} + (1 - \lambda) \mathcal {T} ^ {\pi} Q _ {2}) \\ & \geq \lambda L (\pi , \mathcal {T} ^ {\pi} Q _ {1}) + (1 - \lambda) L (\pi , \mathcal {T} ^ {\pi} Q _ {2}) \\ & = \lambda \mathcal {J} (\pi , Q _ {1}) + (1 - \lambda) \mathcal {J} (\pi , Q _ {2}). \end{array}
$$

Thus, $\mathcal { J } ( \pi , \cdot )$ is concave.

For building up our analysis, we will first prove the saddle point properties of $\mathcal { J } ( \pi , Q )$ by adding a monotonicity assumption on φ that it is a non-decreasing function. We then generalize the proof to show that these properties hold for any concave $\phi$ in Section C.1.

**Lemma C.2.** For $\psi _ { g }$ corresponding to a non-decreasing $\phi , \mathcal { I } ( \cdot , Q )$ has a unique minima $\pi _ { Q } =$ $\textstyle { \frac { 1 } { Z _ { s } } } \exp ( Q )$ with normalizing factor $\begin{array} { r } { Z _ { s } = \sum _ { a } \exp Q ( s , a ) } \end{array}$

Proof. We have,

$$
V ^ {\pi} (s) = \mathbb {E} _ {a \sim \pi} [ Q (s, a) - \log \pi (a | s) ] = - D _ {K L} \left(\pi (\cdot | s) \| \frac {1}{Z _ {s}} \exp (Q (s, \cdot)\right) + \log (Z _ {s}).
$$

For a fixed $Q ,$ the KL divergence is strictly convex in π with minima at $\pi _ { Q }$ , implying $V ^ { \pi } ( s )$ is strictly concave in $\pi$ . Similarly, $\begin{aligned} { r   =   } & { { } \hat { \mathcal { T } ^ { \pi } Q }   =   Q   -   \gamma \mathbb { E } _ { s ^ { \prime } \sim \mathcal { P } ( \cdot | s , a ) } V ^ { \pi } ( s ^ { \prime } ) } \\ \end{aligned}$ is strictly convex in $\pi$ with minima at $\pi _ { Q }$ . Now, as $\phi$ is a non-decreasing function, $\mathbb { E } _ { \rho _ { E } } [ \phi ( \mathcal { T } ^ { \pi } Q ) ]$ will be minimum at $\pi _ { Q }$ and will be always non-decreasing as we pull away. Similarly the second term of $\mathcal { T }$ , given as $- \check { ( } 1 - \gamma ) \mathbb { E } _ { \rho _ { 0 } } [ V ^ { \pi } ( s _ { 0 } \check { ) } ]$ is convex with a minima at $\pi _ { Q }$ . Thus $\mathcal { J } ( \pi , \dot { Q } ) > \mathcal { J } ( \pi _ { Q } , Q )$ , for any $\pi \neq \pi _ { Q }$ This is sufficient to establish that $J ( \cdot , Q )$ has a unique minima at $\pi _ { Q }$

**Lemma C.3.** Define $\mathcal { T } ^ { * } : \mathbb { R } ^ { \mathcal { S } \times \mathcal { A } } \rightarrow \mathbb { R } ^ { \mathcal { S } \times \mathcal { A } }$ such that

$$
(\mathcal {T} ^ {*} Q) (s, a) = Q (s, a) - \gamma \mathbb {E} _ {s ^ {\prime} \sim \mathcal {P} (\cdot | s, a)} [ \log \sum_ {a ^ {\prime}} \exp Q (s ^ {\prime}, a ^ {\prime}) ].
$$

Then $\mathcal { T } ^ { * }$ is bijective.

Proof. For $r = \mathcal { T } ^ { * } Q$ , we have $\begin{array} { r } { Q ( s , a )   =   r ( s , a )   +   \gamma \mathbb { E } _ { s ^ { \prime } \sim \mathcal { P } ( \cdot | s , a ) } [ \log \sum _ { a ^ { \prime } } \exp Q \left( s ^ { \prime } , a ^ { \prime } \right) ] } \end{array}$ . This is just the soft Bellman equation $( \mathrm { E q . } ~ 2 )$ , for which a unique contraction $\overline { { Q ^ { * } } }$ exists satisfying it [14]. Thus for any $r ,$ we have a unique preimage $Q ^ { * }$ such that $r = \mathcal { T } ^ { * } Q ^ { * }$ . Hence, $\mathcal { T } ^ { * }$ is a bijection.

**Lemma C.4.** We have that ${ \mathcal { T } } ^ { * } Q = { \mathcal { T } } ^ { \pi _ { Q } } Q .$ . Moreover, for $Q \in \mathbb { R } ^ { \mathcal { S } \times \mathcal { A } }$ , let $r = \mathcal { T } ^ { * } Q$ . Then, the optimal (soft) policy with respect to r satisfies $\pi _ { r } ^ { * } = \pi _ { Q } .$ . This notably implies that

$$
\pi_ {Q} = \underset {\pi} {\operatorname{argmax}} \mathbb {E} _ {s, a \sim \rho_ {\pi}} [ (\mathcal {T} ^ {*} Q) (s, a) - \ln \pi (a | s) ].\tag{21}
$$

Proof. The first holds is true by basic properties of the Legendre-Fenchel transform [? , Appx. A]. Here, $Q$ is the fixed point of the optimal Bellman operator $\mathcal { B } ^ { * }$ for reward r, so π<sub>Q</sub> is the optimal policy. □

**Lemma C.5.** We have that a unique saddle point exists for $\mathcal { J } ( \pi , Q )$ implying minmax $\mathcal { J } ( \pi , Q ) =$ π∈ΠQ∈Ω max min $\mathcal { J } ( \pi , Q )$ Q∈Ωπ∈Π

Let $( \pi ^ { * } , r ^ { * } )$ be the unique saddle point for $L$ We will first solve for the min-max of $\mathcal { T }$ .

$\mathrm { A s } \; r = \mathcal { T } ^ { \pi } Q$ is an affine transform of $Q$ for a fixed $\pi ,$ we have

$$
\pi^ {*} = \underset {\pi \in \Pi} {\operatorname{argmin}} \max _ {r \in \mathcal {R}} L (\pi , r) = \underset {\pi \in \Pi} {\operatorname{argmin}} \max _ {Q \in \Omega} L (\pi , \mathcal {T} ^ {\pi} Q) = \underset {\pi \in \Pi} {\operatorname{argmin}} \max _ {Q \in \Omega} \mathcal {J} (\pi , Q)
$$

Thus, argmin $\iota _ { \pi } \operatorname* { m a x } _ { Q } \mathcal { J }$ coincides with the first coordinate of the saddle point for $L .$ Now, we can relate the second coordinates.

For $r ^ { * } = \operatorname { a r g m a x } _ { r } L ( \pi ^ { * } , r )$ , as $L$ satisfies the minimax theorem, we necessarily have that

$$
\underline {{\pi^ {*} = \underset {\pi} {\operatorname{argmin}} L (\pi , r ^ {*})}}.
$$

So, as $\begin{aligned} { L ( \pi , r ^ { * } ) = \mathbb { E } _ { s , a \sim \rho _ { E } } [ \phi ( r ^ { * } ( s , a ) ) ] - \mathbb { E } _ { s , a \sim \rho _ { \pi } } [ r ^ { * } ( s , a ) - \operatorname { l n } \pi ( a | s ) ] } \\ \end{aligned}$ , this means that $\pi ^ { * }$ is the optimal policy for $r ^ { * }$ . Write $Q ^ { * }   =   ( \mathcal { T } ^ { * } ) ^ { - 1 } r ^ { * }$ the associated optimal Q-function, we have that $\pi ^ { * } = \pi _ { Q ^ { * } }$ . So, using the affine transformation property, we have

$$
\begin{array}{r l} r ^ {*} & = \underset {r} {\operatorname{argmax}} L (\pi^ {*}, r) \\ & = \mathcal {T} ^ {\pi^ {*}} \left(\underset {Q} {\operatorname{argmax}} L (\pi^ {*}, \mathcal {T} ^ {\pi^ {*}} Q)\right) \\ & = \mathcal {T} ^ {\pi_ {Q ^ {*}}} \left(\underset {Q} {\operatorname{argmax}} L (\pi_ {Q ^ {*}}, \mathcal {T} ^ {\pi_ {Q ^ {*}}} Q)\right) \\ & = \mathcal {T} ^ {\pi_ {Q ^ {*}}} \left(Q ^ {\dagger}\right). \end{array}
$$

where $Q ^ { \dagger } : = \operatorname { a r g m a x } _ { Q } L ( \pi _ { Q ^ { * } } , \mathcal { T } ^ { \pi _ { Q ^ { * } } } Q )$

$\mathrm { A s } \; r ^ { * } = \mathcal { T } ^ { * } Q ^ { * }$ by definition of $Q ^ { * }$ , we have $\mathcal { T } ^ { * } Q ^ { * } = \mathcal { T } ^ { \pi _ { Q ^ { * } } } Q ^ { \dagger }$ . We also know that $\mathcal { T } ^ { * } Q = \mathcal { T } ^ { \pi _ { Q } } Q$ so $\mathcal { T } ^ { * } Q ^ { * } = \widetilde { \mathcal { T } ^ { \pi _ { Q ^ { * } } } Q ^ { * } } = \mathcal { T } ^ { \pi _ { Q ^ { * } } } Q ^ { \dagger }$ . Composing with $( \mathcal { T } ^ { \pi _ { Q ^ { * } } } ) ^ { - \hat { 1 } }$ we obtain $Q ^ { \dagger } = Q ^ { * }$

Overall, with $( \pi ^ { * } , r ^ { * } )$ the unique saddle point of $L ,$ having defined $Q ^ { * } = ( \mathcal { T } ^ { * } ) ^ { - 1 } r ^ { * }$ , we have shown

$$
\min _ {\pi \in \Pi} \max _ {Q \in \Omega} \mathcal {J} (\pi , Q) = \mathcal {J} (\pi^ {*}, Q ^ {*}),
$$

and $\pi ^ { * } = \pi _ { Q ^ { * } }$

Now, we show the same holds for the max-min of $\mathcal { I } .$ . We can relate $Q ^ { * * } : = \operatorname { a r g m a x } _ { Q } \operatorname { m i n } _ { \pi } \mathcal { J } ( \pi , Q )$ and $\pi _ { Q ^ { * * } }$ to the saddle point of $L ( \pi , r )$ . We have

$$
\begin{array}{l l} \underset {\pi} {\min} \mathcal {J} (\pi , Q) = \underset {\pi} {\min} L (\pi , \mathcal {T} ^ {\pi} Q) & \text {by def. of} \mathcal {J} \\ = L (\pi_ {Q}, \mathcal {T} ^ {\pi_ {Q}} Q) & \text {by Lemma C.2} \\ = L (\pi_ {Q}, \mathcal {T} ^ {*} Q) & \text {by Lemma C.4} \\ = \mathbb {E} _ {\rho_ {E}} [ \phi (\mathcal {T} ^ {*} Q) ] - \mathbb {E} _ {\rho_ {\pi_ {Q}}} [ (\mathcal {T} ^ {*} Q) - \ln \pi_ {Q} ] & \text {by def. of} L \\ = \underset {\pi} {\min} \mathbb {E} _ {\rho_ {E}} [ \phi (\mathcal {T} ^ {*} Q) ] - \mathbb {E} _ {\rho_ {\pi}} [ (\mathcal {T} ^ {*} Q) - \ln \pi ] & \text {by Lemma C.4} \\ = \underset {\pi} {\min} L (\pi , \mathcal {T} ^ {*} Q). \end{array}
$$

We therefore have that,

$$
Q ^ {* *} = \underset {Q} {\operatorname{argmax}} \underset {\pi} {\min} \mathcal {J} (\pi , Q) = \underset {Q} {\operatorname{argmax}} \underset {\pi} {\min} L (\pi , \mathcal {T} ^ {*} Q).
$$

Recalling that $( \pi ^ { * } , r ^ { * } )$ is the saddle point of $L ,$ we have $r ^ { * } = \mathcal { T } ^ { * } Q ^ { * * }$ as $\mathcal { T } ^ { * }$ is bijective. However, by definition $\vec { Q ^ { * } } = ( \vec { \mathcal { T } } ^ { * } ) ^ { - 1 } r ^ { * }$ , which readily implies that $Q ^ { * * } = Q ^ { * }$

We have just shown that

$$
\max _ {Q \in \Omega} \min _ {\pi \in \Pi} \mathcal {J} (\pi , Q) = \mathcal {J} (\pi_ {Q ^ {*}}, Q ^ {*}) = \mathcal {J} (\pi^ {*}, Q ^ {*}) = \min _ {\pi \in \Pi} \max _ {Q \in \Omega} \mathcal {J} (\pi , Q).
$$

Therefore, the saddle point of $L$ uniquely corresponds to the saddle point $( \pi ^ { * } , Q ^ { * } )$ of $\mathcal { T }$ , given as $( \pi ^ { * } , r ^ { * } )$ for $r ^ { * } = \mathcal { T } ^ { \pi ^ { * } } Q ^ { * }$

This forms the proof for Proposition 3.4, 3.5

**Proof for Proposition 3.6** We have,

$$
\mathcal {J} ^ {*} (Q) = \mathbb {E} _ {\rho_ {E}} [ \phi (Q (s, a) - \gamma \mathbb {E} _ {s ^ {\prime} \sim \mathcal {P} (\cdot , s, a)} V ^ {*} (s ^ {\prime})) ] - (1 - \gamma) \mathbb {E} _ {p _ {0}} [ V ^ {*} (s _ {0}) ].
$$

As log-sum-exp is convex, $\begin{array} { r } { V ^ { * } ( s ) = \log \sum _ { a } \exp Q ( s , a ) } \end{array}$ is convex in $\mathbf { Q } .$ Then concavity follows from the fact that the first term, $\phi ( Q ( s , a ) - \overline { { \gamma \mathbb { E } } } _ { s ^ { \prime } \sim \mathcal { P } ( \cdot | s , a ) } V ^ { * } ( s ^ { \prime } ) )$ is concave, as it is a concave function composed with a non-decreasing concave function.

## C.1 Generalization

![](images/page_19_image_1.jpg)

Figure 7: Feasibility region in Q-policy space.

In the above section, we made a monotonicity assumption on φ in Lemma C.2. We show that we can relax this assumption and the saddle point properties still hold, although J is not so well-behaved everywhere anymore.

For a fixed $\pi ,$ the optimizer of the concave problem, maxr $L ( \pi , r ) = \mathbb { E } _ { \rho _ { E } } [ \phi ( r ( s , a ) ) ] - \mathbb { E } _ { \rho } [ r ( s , a ) ] -$ $H ( \pi )$ satisfies<sup>9</sup>:

$$
\phi^ {\prime} (r) \rho_ {E} - \rho = 0.
$$

Thus, $\phi ^ { \prime } ( r ( s , a ) ) = \rho ( s , a ) / \rho _ { E } ( s , a ) \in [ 0 , \infty )$ . This tells us that there exists a set of rewards $\mathcal { R } _ { \phi }$ such that φ is non-decreasing on this set. For a concave $\phi , \mathcal { R } _ { \phi }$ is just the convex set of reals that are on the left of its maxima.

**Lemma C.6.** Define a convex **feasibility region** on the Q-policy space:

$$
\mathcal {F} _ {\phi} = \{(\pi , Q): r = \mathcal {T} ^ {\pi} Q \in \mathcal {S} \times \mathcal {A} \rightarrow \mathcal {R} _ {\phi} \}.
$$

Then, for a given π, any optimal $Q = \operatorname { a r g m a x } _ { Q ^ { \prime } } \mathcal { J } ( \pi , Q ^ { \prime } )$ has to lie in ${ \mathcal { F } } _ { \phi } .$

Proof. If $Q$ is optimal, then $\mathcal { T } ^ { \pi } Q$ maximizes $L ( \cdot , r )$ , and so it’s corresponding r is optimal. For a fixed π, and any $( s , a ) \in \mathcal { S } \times \mathcal { A } ,$ the optimal reward has to satisfy $\bar { \phi ^ { \prime } ( r ( s , a ) ) } = \bar { \rho ( s , a ) } / \rho _ { E } ( s , a )$ Thus, each component of the reward vector lies in $\mathcal { R } _ { \phi }$ . This tells us $[ \mathcal { T } ^ { \pi } \hat { Q } ]$ lies in the required region. □

We get two properties in the feasibility region $\mathcal { F } _ { \phi } ;$

1. argmax<sub>Q</sub> ${ } _ { 2 }   \mathcal { I } ( \cdot , Q )$ lies in ${ \mathcal { F } } _ { \phi } ,$ ,

2. $\phi$ is non-decreasing, so lemma C.2 holds in this region.

We just need one last lemma to prove the existence of a unique saddle point:

**Lemma C.7.** A saddle point exists only at the intersection of two curves: argmax<sub>Q</sub> $\mathcal { J } ( \cdot , Q )$ and argmin ${ } _ { \pi }   \mathcal { I } ( \pi , \cdot )$

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">b: ρ/ρE ∈ ∂φ(r)</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">9<sub>A</sub> concave function may not be differentiable everywhere and in general, we get a condition on the subdifferential of φ: ρ/ρE ∈ φ(r).</span></small>

Proof. We parameterize the curves $f ( \pi ) = \operatorname { a r g m a x } _ { Q } { \mathcal { J } } ( \pi , Q )$ and $g ( Q ) = \operatorname { a r g m i n } _ { \pi } { \mathcal { J } } ( \pi , Q )$ . A saddle point has to satisfy minmax $\mathcal { J } ( \pi , Q ) = \operatorname* { m a x } _ { Q } \operatorname* { m i n } _ { \pi }$ n $\mathcal { J } ( \pi , Q )$ . This implies, min $\mathcal { J } ( \pi , f ( \pi ) ) =$ π Q π max $\mathcal { J } ( g ( Q ) , Q )$ . This equation can only be satisfied when both the curves intersect. Q

Therefore, any saddle point lies at the intersection of the Q-maxima and policy minima curves.

We have established that within the feasibility region ${ \mathcal { F } } _ { \phi } ,$ , lemma C.1 and C.2 hold. Thus, there exists a single saddle point in this region. Furthermore, argmax $\iota _ { Q }   \mathcal { I } ( \cdot , Q )$ lies in $\mathcal { F } _ { \phi }$ so lemma C.4 tells us there cannot exist any other saddle points outside $\widetilde { \mathcal { F } _ { \phi } }$

This completes our proof of the existence of a unique saddle point of $\mathcal { T }$ for any concave $\phi .$

We summarize these properties in Fig 7.

## C.2 Convergence Guarantee

![](images/page_20_image_6.jpg)

Figure 8: Policy learning. Comparison of SAC vs adverserial policy update outside the feasibility region.

For any $\phi ,$ our soft actor-critic (SAC) policy update (Sec 4.4) minimizes the KL divergence between the current policy $\pi$ and $\pi _ { Q } ,$ , always pointing towards the the policy minima manifold whereas adversarial policy update relying on the local gradient can diverge away from it (outside the feasibility region). This has the effect, that with sufficient steps, learning with SAC updates is guaranteed to converge to the saddle point, but no such guarantee exists with adversarial policy updates.

## C.3 Effect of various divergences

In the Q-policy space, the policy minima manifold $\pi _ { Q }$ is an energy-based model of $Q ,$ and doesn’t depend on the choice of regularizer $\psi .$

Whereas, the $Q _ { 1 }$ -maxima manifold is dependent on the choice of regularizer. As the saddle point is formed by the intersection of these two curves (Lemma C.4), we can study how different divergences will affect the saddle point which solves the regularized-IRL problem.

We have that for a choice of $\phi ,$ the $Q _ { 1 }$ -maxima manifold is given by the condition:

$$
\phi^ {\prime} (r) \rho_ {E} - \rho = 0.
$$

Thus on the maxima manifold, $r   =   ( \phi ^ { \prime } ) ^ { - 1 } ( \rho / \rho _ { E } )$ . We visualize this in the Fig. 9, we see that different statistical distances correspond to different saddle points. The overall effect is that that at the saddle point $\pi ^ { * }$ remains close to $\pi _ { E }$ , but may not be exactly equal as the regularization constrains the policy class.

In general, $\pi ^ { * }$ is the solution to the (transcendental) equation:

$$
\phi^ {\prime} (\mathcal {T} ^ {\pi} Q) \rho_ {E} - \rho_ {Q} = 0,\tag{22}
$$

where $\rho _ { Q }$ is the occupancy measure corresponding to $\pi _ { Q } = { \textstyle \frac { 1 } { Z } } \exp Q$

![](images/page_21_chart_0.jpg)

Figure 9: Saddle points. Effect of regularizer ψ on the saddle point. (not to scale)

For f-divergences, this can be simplified as

$$
\mathcal {T} ^ {\pi} Q = - f ^ {\prime} \left(\frac {\rho_ {Q}}{\rho_ {E}}\right).\tag{23}
$$

For an IPM parametrized by $\mathcal { F } , \phi ^ { \prime } ( x ) = 0$ and the equation will be maximized on the boundary of ${ \mathcal { F } } ,$ without a closed form equation.

Now, SQIL [33] uses the reward of the form 1 − 0 dependent on sampling from the expert or policy distributions. This condition corresponds to a maxima manifold in this space, such that instead of the reward being a function of the ratio density of the expert and the policy, it is stochastically dependent on the sampling. Thus, instead of being fixed, the manifold will shift stochastically with the sampling. This has the corresponding effect of shifting the saddle point and can result in numerical instabilities near convergence, as a unique convegence point does not exist for the SQIL style update.

Similary, we can analyze ValueDICE [22]. ValueDICE mimimizes the Reverse-KL divergence between the expert and policy using the Donsker-Varadhan (DV) variational form of Reverse-KL. This corresponds to the maxima manifold with rewards satisfying $r = \log ( \rho _ { E } / \rho )$ , but suffers from two issues: 1) biased gradient estimates, and 2) adversarial policy updates.

We have already shown how adverserial policy updates are not optimal, we will now focus on fixing the biasing issue with the Reverse-KL distance.

First, the DV representation is given as:

$$
K L (\rho , \rho_ {E}) = \max _ {r \in \mathcal {R}} \log \mathbb {E} _ {\rho_ {E}} [ e ^ {- r (s, a)} ] - \mathbb {E} _ {\rho} [ r (s, a) ]
$$

This corresponds to a $\phi ( x )   =   \log \mathbb { E } _ { \rho _ { E } } [ e ^ { - x } ]$ , even though its outside the class of $\psi$ we study, it satisfies all the previous properties we developed (Lemma C.1 - C.4).

Now, to unbias the Reverse-KL representation, we propose using the f-divergence representation, with $f ( t )   =   t \log t   -   t   +   1$ . Then the f-divergence for this choice of $f$ is just the Reverse-KL divergence, but it’s variational form is:

$$
\max _ {r \in \mathcal {R}} \mathbb {E} _ {\rho_ {E}} [ - e ^ {- r (s, a)} ] - \mathbb {E} _ {\rho} [ r (s, a) ] - 1
$$

and corresponds to $\phi ( x ) = - e ^ { - x }$ with rewards $r = \log ( \rho _ { E } / \rho )$

Thus, we can obtain the same $Q _ { 1 }$ -maxima manifold to minimize the Reverse-KL distance as ValueDICE by using this new representation, while avoiding the biasing issue.

**Effect of different forms of Reverse-KL** We test IQ-Learn with different variational representations of Reverse-KL: Donsker-Varadhan (DV), Original KL (KL), ours Modified KL (KL-fix).

We use the LunarLander environment with our offline IL experimental settings and a single expert trajectory. All experiments are repeated over 10 seeds. We show a box-plot of the environment returns for different variational forms and find that our proposed form (KL-fix) and the DV representation perform similarly. The original f-divergence form of KL remains problematic, performing noticeably worse, which may be due to an issue with its corresponding Q-maxima manifold. Compared to DV, our proposed KL variation representation has the advantage of giving unbiased gradient estimates and can be more stable.

![](images/page_22_chart_1.jpg)

Figure 10: Reverse-KL ablation. We show environment returns for different variational forms of Reverse-KL on LunarLander.

## C.4 A theoretical guarantee for A.1

Motivated by learning a state-dependent reward function, Section A.1 proposes an alternative objective function for learning Q. Here, we provide a form of monotonic improvement guarantee for an idealized version of the objective in Eq. 14.

Before this, lets introduce some notations that will be useful, as we’ll now work with both state and state-action occupancy measures. Let write $\mu \in \Delta _ { \mathcal { S } \times \mathcal { A } }$ an occupancy measure on state-actions, $\rho \in \Delta _ { \mathcal { S } }$ an occupancy measure on states. For $\rho \in \Delta _ { \mathcal { S } }$ and $\pi \in \Delta _ { \mathcal { A } } ^ { \mathcal { S } }$ , write $\rho \pi \in \Delta _ { \mathcal { S } \times \mathcal { A } }$ defined as $( \rho \pi ) ( s , a ) = \rho _ { \pi } ( s ) \pi ( a | s )$ . Now, let recall Eq. 14:

$$
\mathcal {J} ^ {*} (Q) = \mathbb {E} _ {s \sim \rho_ {E}} [ \mathbb {E} _ {a \sim \text {stop\_grad} (\pi_ {Q}) (\cdot | s)} [ \phi ((\mathcal {T} ^ {*} Q) (s, a)) ] ] - (1 - \gamma) \mathbb {E} _ {s \sim \rho_ {0}} [ \log \sum_ {a} \exp Q (s, a) ].\tag{24}
$$

Now, we’ll consider a more conservative version of this objective function. For a given policy $\pi _ { k } ,$ define

$$
\mathcal {J} _ {k} ^ {*} (Q) = \mathbb {E} _ {s \sim \rho_ {E}} [ \mathbb {E} _ {a \sim \pi_ {k} (\cdot | s)} [ \phi ((\mathcal {T} ^ {*} Q) (s, a)) ] ] - (1 - \gamma) \mathbb {E} _ {s \sim \rho_ {0}} [ \log \sum_ {a} \exp Q (s, a) ].
$$

Now, for any initial $Q _ { 0 } ,$ define for $k \geq 0$

$$
\begin{array}{l} \left\{ \begin{array}{l} \pi_ {k} = \pi_ {Q _ {k}} = \operatorname{softmax} (Q _ {k}) \\ Q _ {k + 1} = \operatorname{argmax} _ {Q} \mathcal {J} _ {k} ^ {*} (Q) \end{array} \right.. \end{array}\tag{25}
$$

Eq. (24) can be see as an optimistic version of Eq. (25), in the sense that instead of optimizing to the end each subproblem, we update $\pi _ { k }$ at each gradient step. It is Eq. (25) that we’ll analyse. Before that, we need some assumption: φ is concave and non-decreasing. Write $f$ the convex conjugate of $- \phi ( - x )$ (that is $f ^ { * } ( x ) = \dot { - } \phi ( - \dot { x } ) )$ , f satisfies $f ( 1 ) = 0$

In other words, we restrict ourselves to (a subclass of) f-divergences, but it should be possible to adapt the analysis to other cases (eg, IPMs). The core result is the following.

**Theorem C.8.** Under the previous assumption, the sequence of policies $( \pi _ { k } ) _ { k \geq 0 }$ produced by Eq. (25) satisfies a monotonic improvement guarantee, in the sense that for any $k \geq { \bar { 0 } } ,$ we have

$$
D _ {f} (\rho_ {\pi_ {k + 1}} | | \rho_ {E}) - H (\pi_ {k + 1}) \leq D _ {f} (\rho_ {\pi_ {k}} | | \rho_ {E}) - H (\pi_ {k}).\tag{26}
$$

Proof. Define for $k \geq 0$

$$
\begin{array}{c} L _ {k} (\pi , r) = \mathbb {E} _ {s \sim \rho_ {E}} [ \mathbb {E} _ {a \sim \pi_ {k} (\cdot | s)} [ \phi (r (s, a)) ] ] - \mathbb {E} _ {s, a \sim \rho_ {\pi}} [ r (s, a) - \ln \pi (a | s) ] \\ \text {and} \mathcal {J} _ {k} (\pi , Q) = L _ {k} (\pi , \mathcal {T} ^ {\pi} Q). \end{array}
$$

We have that

$$
\left| \begin{array}{c c} \mathcal {J} _ {k} ^ {*} (Q) = \underset {\pi} {\operatorname{argmin}} \mathcal {J} _ {k} (\pi , Q) & \text {(minimized for} Q _ {k + 1}) \\ \text {and} \pi_ {Q _ {k + 1}} = \underset {\pi} {\operatorname{argmin}} \underset {r} {\max} L _ {k} (\pi , r) \\ = \underset {\pi} {\operatorname{argmin}} D _ {f} (\mu_ {\pi} | | \rho_ {E} \pi_ {k}) - H (\pi) & \text {(by def. of} L _ {k}). \end{array} \right|
$$

This implies that

$$
D _ {f} (\mu_ {\pi_ {k + 1}} | | \rho_ {E} \pi_ {k}) - H (\pi_ {k + 1}) \leq D _ {f} (\mu_ {\pi_ {k}} | | \rho_ {E} \pi_ {k}) - H (\pi_ {k}).
$$

We’ll work both sides of this bound. For the r.h.s., we have that

$$
\begin{array}{r l} D _ {f} (\mu_ {\pi_ {k}} | | \rho_ {E} \pi_ {k}) & = \sum_ {s, a} \rho_ {E} (s) \pi_ {k} (a | s) f \left(\frac {\rho_ {\pi_ {k}} (s) \pi_ {k} (a | s)}{\rho_ {E} (s) \pi_ {k} (a | s)}\right) \\ & = \sum_ {s} \rho_ {E} (s) \sum_ {a} \pi_ {k} (a | s) f \left(\frac {\rho_ {\pi_ {k}} (s)}{\rho_ {E} (s)}\right) \\ & = \sum_ {s} \rho_ {E} (s) f \left(\frac {\rho_ {\pi_ {k}} (s)}{\rho_ {E} (s)}\right) \\ & = D _ {f} (\rho_ {\pi_ {k}} | | \rho_ {E}). \end{array}
$$

For the l.h.s., we have

$$
\begin{array}{l} D _ {f} (\mu_ {\pi_ {k + 1}} | | \rho_ {E} \pi_ {k}) = \sum_ {s} \rho_ {E} (s) \sum_ {a} \pi_ {k} (a | s) f \left(\frac {\rho_ {\pi_ {k + 1}} (s) \pi_ {k + 1} (a | s)}{\rho_ {E} (s) \pi_ {k} (a | s)}\right) \\ \quad \geq \sum_ {s} \rho_ {E} (s) f \left(\sum_ {a} \pi_ {k} (a | s) \frac {\rho_ {\pi_ {k + 1}} (s) \pi_ {k + 1} (a | s)}{\rho_ {E} (s) \pi_ {k} (a | s)}\right) \quad \text {(by Jensen)} \\ \quad = \sum_ {s} \rho_ {E} (s) f \left(\frac {\rho_ {\pi_ {k + 1}} (s)}{\rho_ {E} (s)}\right) \\ \quad = D _ {f} (\rho_ {\pi_ {k + 1}} | | \rho_ {E}). \end{array}
$$

Putting things together, we get

$$
\begin{array}{r l} D _ {f} (\rho_ {\pi_ {k + 1}} | | \rho_ {E}) - H (\pi_ {k + 1}) & \leq D _ {f} (\mu_ {\pi_ {k + 1}} | | \rho_ {E} \pi_ {k}) - H (\pi_ {k + 1}) \\ & \leq D _ {f} (\mu_ {\pi_ {k}} | | \rho_ {E} \pi_ {k}) - H (\pi_ {k}) \\ & = D _ {f} (\rho_ {\pi_ {k}} | | \rho_ {E}) - H (\pi_ {k}), \end{array}
$$

and thus the stated result.

## D Appendix D

## D.1 Implementation Details

For reproducibility, we release all our expert demonstrations, either trained from scratch or obtained using Stable Baslines3 Zoo [32]. We also release an efficient expert data generation and data-loading pipeline, that can work with pre-trained Stable Baselines3 models, or arbitary pytorch RL agents. We hope this will make benchmarking for IL easier and help with standardization. Our code is available at [https://github.com/Div99/IQ-Learn](https://github.com/Div99/IQ-Learn).

## D.1.1 Offline Setup

We mimic prior works’ settings [19, 6] to make our results directly comparable for offline IL.

**Expert Demonstrations** We obtain expert demonstrations by training a DQN [27] agent from scratch for all the environments tested. Our trajectories were then sub-sampled for every 20th step in Acrobot and CartPole, and every 5th step in LunarLander.

**Training Setup** We test with (1,3,7,10,15) expert trajectories uniformly sampled from a pool of 1000 expert demonstrations. Each algorithm is trained until convergence and tested by performing 300 live rollouts in the simulated environment and recording the average episode rewards. We repeat this over 10 seeds, consequently with different initializations and seen trajectories.

**Implementation** All methods use neural networks with the same architecture of 2 hidden layers of 64 units each connected by exponential linear unit (ELU) activation functions.

We use the original public code implementations of EDM, AVRIL and ValueDICE. Note, ValueDICE is adapted to discrete environments using an actor with Gumbel-softmax distribution output.

**Hyperparameters** We use batch size 32 and Q-network learning rate 1e−4 with entropy coefficient 0.01. We found learning rate of $1 e - 4$ worked best for IQ-Learn on discrete environments. We also found entropy coefficient values $[ 1 e - 2 , 1 e - 3 ]$ to be optimal depending on the environment. Here, we don’t use target updates as we found them to give no visible improvement and slow down the training.

## D.1.2 Online Setup

**Expert Demonstrations** For Mujoco environments, we generate expert demonstrations from scratch using a Pytorch implementation of SAC. For Atari, we generate demonstrations using pre-trained DQN agents from Stable Baselines3 Zoo. For both, we generate a pool of 30 expert demonstrations and sample trajectories uniformly. For Mujoco results, we sample 1 expert demo and for Atari we sample 20 expert demos without any subsampling.

**Implementation** For Mujoco, with all methods we use critic and actor networks with an MLP architecture with 2 hidden layers and 256 hidden units, keeping settings similar to original SAC [13]. For Atari, with all methods we use a single convolution neural network same as the original DQN architecture [27]. For IQ-Learn in continuous environments, for SAC policy updates we sample states from both policy and expert distributions. We regularize policy states in addition to expert states to improve the stability of learning Q-values. We use soft target updates and find them helpful for stabilizing the training.

For BC and $\mathbf { G A I L } ,$ we use the stable-baselines implementations. For SQIL, we use original public code for Atari environments. For ValueDICE, we use the open-sourced official code.

**Hyperparameters** For SAC style learning, we use default settings of critic learning rate $3 e - 4$ and policy learning rate values $[ 3 e - \dot { 4 } , 3 e - 5 ]$ . We found $3 e - 5$ to work well in complex environments and remain stable, although 3e − 4 can be better with simpler environments (like Half-Cheetah). We use a fixed batch size of 256 and found entropy coefficient 0.01 to work well. We use soft target updates with the default SAC smoothing constant $\tau = 0 . 0 5$ . For DQN-style learning on Atari, we use Q-network learning rate 1e − 4 with entropy coefficient 1e − 4 and batch size 64. We found entropy coefficient values $[ \bar { 1 } e - 3 , 1 e - 4 ]$ to work well. We didn’t find noticeable improvements with using target updates on Atari (with the exception of Space Invaders, where they stabilize the training).

## D.2 Additional Results

**Mujoco** We show additional results on Mujoco obtained using 10 expert trajectories in Table 5. We find IQ-Learn gets state-of-art performance in all environments and reaches expert-level rewards.

Table 5: Mujoco Results. We show our performance on MuJoCo control tasks using 10 expert trajectories.

| Task | Random | BC | GAIL | ValueDICE | IQ (Ours) | Expert |
| --- | --- | --- | --- | --- | --- | --- |
| Hopper | 14 ± 8 | 1345 ± 422 | 3322 ± 510 | 3399 ± 651 | 3529 ± 15 | 3533 ± 39 |
| Half-Cheetah | -282 ± 80 | 2701 ± 950 | 4280 ± 1002 | 4840 ± 132 | 5154 ± 82 | 5098 ± 62 |
| Walker | 1 ± 5 | 3730 ± 1440 | 4417 ± 420 | 4384 ± 345 | 5212 ± 85 | 5274 ± 53 |
| Ant | -70 ± 111 | 2272 ± 472 | 3997 ± 312 | 4507 ± 265 | 4683 ± 67 | 4700 ± 80 |
| Humanoid | 123 ± 35 | 2057 ± 843 | 372 ± 51 | 2001 ± 524 | 5288 ± 73 | 5313 ± 210 |

**Atari Suite.** We show detailed performance of IQ-Learn on Atari Suite environments using 20 expert demonstrations in Table 6.

Table 6: Results on Atari Suite. We show our results on Atari Suite tasks using 20 expert demonstrations.

| Env | IQ (Ours) | Expert |
| --- | --- | --- |
| Pong | 19 ± 2 | 21 ± 0 |
| Breakout | 320 ± 72 | 376 ± 34 |
| Space Invaders | 807 ± 102 | 823 ± 272 |
| BeamRider | 3025 ± 845 | 4295 ± 1173 |
| Seaquest | 2349 ± 342 | 2393 ± 291 |
| Qbert | 12940 ± 2026 | 11496 ± 1988 |

**Reward Correlations.** We show the Pearson correlation coefficient of our learnt rewards with environment rewards in Table 7.

Table 7: Reward Correlations. We show pearson correlations between our learnt reward and the env rewards.

| Env | Reward correlation |
| --- | --- |
| Cartpole | 0.99 |
| LunarLander | 0.92 |
| Hopper | 0.99 |
| Half-Cheetah | 0.86 |
| Pong | 0.67 |

**Do we overfit?** Compared to ValueDICE, we don’t observe overfitting using IQ-Learn with the number of update steps. We show a comparision on Half-Cheetah environment using one expert trajectory in Fig 11. ValueDICE begins to overfit around 100k update steps, whereas IQ-Learn converges to expert rewards and remains stable.

![](images/page_25_chart_6.jpg)

Figure 11: Half-Cheetah overfitting comparision

## D.3 Recovering Rewards

We show visualizations of our reward correlations on the Hopper environment using 10 expert demonstrations in Fig 12. We obtain a Pearson correlation of 0.99 of our recovered episode rewards compared with the original environment rewards, showing that our rewards are almost linear with the actual rewards, and thus can be used for Inverse RL. Note, that to recover rewards with IQ-Learn, we need to sample the current state and the next state.

![](images/page_25_chart_10.jpg)

We perform similar comparisons on GAIL and SQIL, obtaining Pearson coefficients of 0.90 and 0.72 respectively.

Figure 12: Hopper correlations

In the main paper, we also show recovered rewards on a simple grid environment by using sampling based Q-learning with a simple Q-network having two hidden layers. In the section below, we further compare IQ-Learn on a tabular setting.

**Tabular Inverse RL** To further validate IQ-Learn as a method for IRL and show we recover correct rewards, we directly compare with the classical Max Entropy IRL [43] method on a tabular Grid world setting, by using an open-source implementation<sup>10</sup>. We implement IQ-Learning as a modification to tabular value iteration. The classical method requires repeated backward and forward passes, to calculate soft-values and action probabilities for a given reward and optimize the rewards respectively. IQ-Learn skips the expensive backward pass and directly optimizes the rewards. We show comparision in Fig 13, where we find our method recovers very similar rewards while being more than 3x faster.

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">10<a href="https://github.com/yrlu/irl-imitation"><sub>https</sub>://github.com/yrlu/irl-imitation</a></span></small>

![](images/page_26_chart_0.jpg)

Figure 13: Tabular Grid Rewards. We recover similar rewards as Max entropy IRL (Ziebert et al.) while avoiding an expensive backward pass.

## D.4 Imitation learning with Observations

We show results for IQ-Learn trained with using only expert observations in Table 8. We test on CartPole, LunarLander and Hopper environments with 1 and 10 expert demonstrations using online IL settings without any subsampling of trajectories. We find that with one expert demonstration, we get below expert-level rewards, and

Table 8: Results on ILO. We show evironment returns using 1 and 10 expert demonstrations.

| Env | 1 demo | 10 demos |
| --- | --- | --- |
| CartPole LunarLander Hopper | 254205072±±±15300425 | 3424826505±±±265591 |

as expected, our performance suffers compared to with using expert actions. We find using 10 demonstrations is enough to reach expert-level performance in these simple environments.

Target updates are helpful in stabilizing the training in this setting.

## E Appendix E

## E.1 Dynamics-Aware Imitation Learning and the Loop MDP

In this section we illustrate the importance of dynamics-awareness in imitation learning with a toy MDP based on the Loop MDP from [34]. The MDP is shown in Fig 14. The MDP has a fixed length of 100 steps. The key problem for dynamics-unaware algorithms, such as behavioural cloning, is the behaviour in state $s _ { 2 }$ . If we happen to use an expert trajectory where the expert never visits state $s _ { 2 }$ then the learned policy will not necessarily have the right behaviour in state $s _ { 2 }$ . This is because the objective for behavioural cloning is to match the action probabilities in the expert states, and $s _ { 2 }$ is not in the expert states visited. However, the dynamics-aware methods are able to deduce that taking action $a _ { 1 }$ in state $s _ { 2 }$ will return the imitator to state $s _ { 1 }$ . Although this $\mathrm { M D P }$ is simple, it illustrates a general advantage of dynamics-aware methods which will hold in many situations. In particular, it will hold for environments where the expert may keep very close to an optimal trajectory, yet it is possible to recover back to that trajectory if a small mistake is made, such as in autonomous lane-keeping in a car.

![](images/page_27_image_0.jpg)

Figure 14: A variant of the Loop MDP from [34]. Taking actions labelled in green gives 1 reward, while actions in black give reward $0 .$ The MDP is stochastic for action $a _ { 1 }$ in state $s _ { 0 }$ , which with probability $p$ leads to state $s _ { 2 } ,$ and with probability $1 - p$ leads to state $s _ { 1 }$

To substantiate this illustrative case, we implemented this MDP and evaluated a few methods. We use a single expert trajectory which goes from $s _ { 0 }$ to $s _ { 1 }$ , never going to state $s _ { 2 }$ . We set $p = 0 . 5$ for this experiment. The results are in Table $^ { 9 , }$ averaged over five random seeds. They are as we expect, with the dynamics-aware methods able to convincingly master the environment and find the optimal policy, while the behavioural cloning approach achieves around 50 reward. This is because it learns the wrong behaviour in state $s _ { 2 }$ so gets zero reward in that state in the 50% of the time that taking action $a _ { 1 }$ results in a transition to state $s _ { 2 }$

Table 9: Results of imitation learning algorithms on the Loop MDP described above. We observe that the dynamics-unaware behavioural cloning baseline performs much worse than the other dynamicsaware methods.

| Method | Episode Reward |
| --- | --- |
| Behavioural Cloning | 54 ± 5 |
| SQIL | 100 ± 0 |
| IQ (Online, $\chi^{2}$) | 100 ± 0 |

## E.2 Ablation on Gamma

The dynamics are encoded in our learning objective by the discount factor $\gamma ,$ and setting it to zero removes dynamic-awareness in IQ-Learn.

To show how dynamics help with learning, we do an ablation on γ with IQ-Learn. We use the offline IL settings for CartPole environment with one expert trajectory.

![](images/page_27_chart_8.jpg)

Figure 15: Ablation on Gamma

We set $\gamma$ to 0.99 and 0. The results are visualized in Fig 15, we can see that without the dynamics the training is not stable and there is a strong decay in the rewards obtained by the IL agent from the environment. Whereas, when using dynamics, we see that the training is stable and properly converges.

## F Appendix F

## F.1 Generalization over distribution shift

We show our method can be robust to distribution shifts between the expert and policy and perform additional experiments over two different settings: 1) Initial distribution shift using a modified LunarLander env motivated by [33] and 2) Goal distribution shift using DeepMind Control Suite.

## F.1.1 Initial distribution shift

We experiment with initial shift distribution in the LunarLander-v2 environment similar to [33]. The agent is typically initialized in a small zone at the middle top of the screen. Instead, we modify the environment to initialize the agent near the top-left corner of the screen. We use experts from the unmodified environment, and test whether the agent can still learn to land the lunar lander while recovering from the initial distribution shift.

**Offline Case**: We find in the offline case that the agent cannot learn to recover from the occupancy shift. The lander typically tends to fly off the frame and shows random behavior. This is expected as IQ-learn is not aware of the shift of initial distributions between the agent and the expert, and can’t explore the environment to correct the initial state shift to match the occupancy distributions.

**Online Case**: In the online case, we find that the agent can sufficiently explore the environment, and learns a behavior of first horizontally moving the lander from the top left to the top center and then successfully imitating the original expert trajectory, receiving an avg. episode reward of 250 with 10 expert demos.

An extra consideration here is in Eq. 9, where we originally only apply reward regularization to the expert states, but we find applying regularization to both expert and policy states to be beneficial in this case. As it enforces the learning of an implicit reward function that can generalize outside the expert distribution to more arbitrary policy states.

## F.1.2 Goal Distribution Shift

We experiment with the reacher\_easy task in DeepMind Control Suite. We choose the reacher environment as it is a multi-task environment, where the goal given by the target position changes in every episode randomly. Such environments have been found to be very difficult to solve using IRL [40] as a large number of expert demos are needed to fully cover the goal distributions, and usually require meta-IRL methods to figure the right task context for a given expert demonstration like PEMIRL [40].

We test with different number of expert demonstrations: (1, 5, 10, 20) each with different target positions on the offline and online settings. The average expert performance is ∼ 990 in this case and we report averaged results over 100 episodes with different targets.

**Offline Case**: In the offline setting, a single demonstration is typically not enough to learn a generalized reward function and leads to a reward that overfits to a particular target position. We quantify the results in Table 10, with the observation that imitation learning performance improves with the number of expert demos. This can be justified, as more experts with different targets allow learning a reward function that is better generalizable.

Table 10: **Offline**. We show evironment returns vs number of experts on reacher\_easy for offline case.

| Num Experts | Rewards |
| --- | --- |
| 1 | 105.4 |
| 5 | 120.1 |
| 10 | 210.6 |
| 20 | 325.0 |

**Online Case**: In the online setting, our method is able to explore the environment over different episodes and can learn to correct the behavior leading to better performance. In particular, given a sufficient number of expert demos, it can learn to associate what expert behavior to imitate given a particular target and learns a more reward function generalizable over multiple goals. We show quantitative results in Table 11.

BC and GAIL on reacher\_easy even with 50 experts obtain mean rewards of 325.2 and 440.1 respectively, which is equivalent to what we see using our method with just 5 expert demos! It is surprising to us that our method can learn a reward to figure out what goal state to reach, acting as a **meta-learner** even when not engineered specifically to do so.

Table 11: **Online**. We show evironment returns vs number of experts on reacher\_easy for online case.

| Num Experts | Rewards |
| --- | --- |
| 1 | 271.3 |
| 5 | 485.1 |
| 10 | 545.0 |
| 20 | 734.9 |
| 50 | 926.1 |