# The Setting: Hamiltonian Dynamics on Phase Space

## Configuration Space and Phase space
\label{sec:Ham1}

> The concepts in this section are adapted from the books {cite}`lifshitz1978,wiggins2003applied`.

* __Generalized Coordinates:__ The location of the particles comprising a system are described by a set of coordinates, known in Mechanics as generalized coordinates. The space, i.e. all possible values, described by these coordinates is referred to as {\em configuration space}.

* __Degrees-of-freedom (DoF):__ The number of DoF is the number of independent generalized coordinates required to describe the configuration of the system, i.e. it is the dimension of the configuration space.

* __Momenta:__ In the canonical Hamiltonian framework, each configuration space variable has an associated canonically conjugate variable which are referred to as momentum variables.

* __Phase space:__ The collection of all the configuration and momentum variables is referred to as the phase space of the Hamiltonian dynamical system.

## Hamilton's Equations

Consider an $n$ DoF system described by the scalar function $H(\mathbf{q},\mathbf{p},t)$, known as the Hamiltonian of the system, which smoothly depends on the configuration space coordinates $\mathbf{q} = (q_1,\ldots,q_n) \in \mathbb{R}^{n}$, their canonically conjugate momenta $\mathbf{p} = (p_1,\ldots,p_n) \in \mathbb{R}^{n}$ and time. Hamilton's equations are a set of $2n$ first-order differential equations:

```{math}
---
label: hamiltoneq
---
\begin{cases}
\dot{q}_i = \dfrac{\partial H}{\partial p_i} \\[.4cm]
\dot{p}_i = -\dfrac{\partial H}{\partial q_i} 
\end{cases}
\; , \qquad \; i = 1, 2, \ldots, n,
```

that describe the dynamics of the system, where the dot symbol over a variable denotes the total time derivative, that is $\cdot \equiv d/dt$. When the Hamiltonian function does not depend on time explicitly, the dynamical system it generates by means of Eq. {eq}`hamiltoneq` is said to be __autonomous__.


## Conserved quantities in phase space

> The reader can find more details on Poisson brackets and their properties \\ in many books and lecture notes, see e.g. {cite}`lifshitz1978,arnold1978,giorgilli2002`


Given a Hamiltonian system, a function $A(\mathbf{q}, \mathbf{p},t)$ is called an \textbf{integral of motion}, \textbf{constant of motion} or \textbf{first integral} if it remains constant along a trajectory. Then, its total time derivative is zero along solutions $(\mathbf{q}(t),\mathbf{p}(t))$ of Hamilton's equations, that is

```{math}
:label: integral
    \dfrac{dA}{dt} = \dfrac{\partial A}{\partial t} + \sum\limits_{i = 1}^n \left( \dfrac{\partial A}{\partial q_i} \dfrac{d q_i}{dt} + \dfrac{\partial A}{\partial p_i} \dfrac{d p_i}{dt} \right)  = \dfrac{\partial A}{\partial t} + 
    \sum\limits_{i = 1}^n \left( \dfrac{\partial A}{\partial q_i}\dfrac{\partial H}{\partial p_i}- \dfrac{\partial A}{\partial p_i}  \dfrac{\partial H}{\partial q_i} \right) = 0.
```

The quantity

```{math}
---
label: poisson
---
    \{A,H\} = \sum\limits_{i = 1}^n \left( \dfrac{\partial A}{\partial q_i}\dfrac{\partial H}{\partial p_i}- \dfrac{\partial A}{\partial p_i}  \dfrac{\partial H}{\partial q_i} \right),
```

\noindent
is called the \textit{Poisson bracket} of the functions $A$ and $H$. Therefore, Eq. {eq}`integral` is equivalent to:

\begin{equation}
\dfrac{dA}{dt} = \frac{\partial A}{\partial t} + \{A,H\} = 0. \label{eq:integral2}
\end{equation}

Notice that if the function $A$ does not explicitly depend on time, that is $\partial A / \partial t = 0$, then $A$ is an integral of motion if and only if  $\{A, H\} = 0$. In other words, the Poisson bracket provides us with a useful test to see if a function of the phase space variables and time is conserved or not in a Hamiltonian system. In particular, if the Hamiltonian of the system is time-independent, that is $H = H(\mathbf{q},\mathbf{p})$, then we can deduce that:

\begin{equation}
    \frac{dH}{dt} = \dfrac{\partial H}{\partial t} +  \{ H, H \} = 0 + \sum\limits_{i = 1}^n \left( \dfrac{\partial H}{\partial q_i}\dfrac{\partial H}{\partial p_i}- \dfrac{\partial H}{\partial p_i}  \dfrac{\partial H}{\partial q_i} \right) = 0 \;, 
\end{equation}

which implies that the Hamiltonian itself is a constant of the motion. If the Hamiltonian represents the total energy of the physical system, this property is just the law of conservation of total energy along trajectories of an autonomous Hamiltonian system. The implicit time dependence of the position and momentum coordinates may increase/decrease the kinetic energy at the expense/gain of the potential energy, but the sum of kinetic and potential energy remains constant.

Another example of a quantity that is a constant of the motion is provided by ignorable or cyclic coordinates. A generalized coordinate $q_i$ is said to be \textit{ignorable} or \textit{cyclic} if it does not appear in the expression of the Hamiltonian function. By Hamilton's equations in Eq. {eq}`hamiltoneq`, this implies that

\begin{equation}
    \dot{p}_i = - \dfrac{\partial H}{\partial q_i} = 0
\end{equation}

and therefore the momentum $p_i$ is constant along trajectories, that is, $p_i(t) = p_i^0$.

We introduce next a concept which is important for the study of integrable Hamiltonian systems. Integrable Hamiltonian systems are those that can be solved by quadratures and are characterized by Liouville-Arnold theorem, see {cite}`arnold1978` and the contents in Section \ref{sec:Ham2}. Two constants of the motion $A$ and $B$ are said to be in \textit{involution} if they satisfy

```{math}
---
label: involution
---
\{A,B\} = 0 \;.
```

## Invariant Sets

> The concepts here are adapted from {cite}`wiggins2003applied`.

Invariant sets play a fundamental role in how we understand the nature of phase space dynamics. We will give here a definition for this concept for an autonomous dynamical system in the continuous time setting:

```{math}
---
label: cont_ds
---
\dot{x} = f(x) \;, \quad x \in \mathbb{R}^{n}
```

and also for a map (discrete time dynamics): 

```{math}
---
label: disc_ds
---
x \mapsto g(x) \;, \quad x\in \mathbb{R}^{n}
```

__Definition__
\label{def:invset}
Let $S \subset \mathbb{R}^{n}$ be a set of the phase space of the dynamical system, then


* __Continuous time:__ $S$ is invariant under the flow generated by Eq. {eq}`cont_ds` if for any point $x_{0} \in S$ we have that  $x(t;x_{0}) \in S$ for all $t \in I$, where $x(t;x_{0})$ denotes the solution of Eq. {eq}`cont_ds` with initial condition $x(0) = x_{0}$, and $I$ is the time interval of existence of the solution. 

* __Discrete time:__ $S$ is said to be invariant under the map in Eq. {eq}`disc_ds` if for any $x_{0}\in S$, the orbit (trajectory) associated to that initial condition remains inside the set for all iterates of the map, that is $g^{n}(x_{0})\in S$, for all $n$.


Invariant sets play an important role for the analysis of dynamical systems, as they allow us to break up the dynamics into smaller parts. For example the dynamics in invariant sets can be investigated separately from the rest of the system. As we will show in the following sections, some invariant sets, such as invariant manifolds, naturally divide the phase space of the system into regions of qualitatively distinct dynamical behavior that can be studied independently.


# References

```{bibliography} bibliography/chapter1.bib
```