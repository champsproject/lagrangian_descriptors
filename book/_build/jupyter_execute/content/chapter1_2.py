# Hamiltonian flows and symplectic maps

(sec:Ham2)=
## Hamiltonian flows

A Hamiltonian system with $N$ degrees of freedom is described by the Hamiltonian function $H(\mathbf{q},\mathbf{p},t)$, which depends on the generalized coordinates $\mathbf{q} = (q_1,\ldots,q_N)$, their canonically conjugate momenta $\mathbf{p} = (p_1,\ldots,p_N)$, and time. This scalar function gives rise to a $2N$-dimensional dynamical system by means of Hamilton's equations of motion

```{math}
---
label: eq:hamiltons_eom
---
\dot{q}_i = \frac{\partial H}{\partial p_i} \quad,\quad \dot{p}_i = -\frac{\partial H}{\partial q_i} \;, \quad \text{for} \; i = 1, 2, \ldots, N.
```

where the dot symbol represents the total time derivative, that is,  $\cdot \equiv d/dt$. A state of the system is represented by a point in the $2N$-dimensional _phase space_, Any solution of this system is a trajectory of the form

```{math}
---
label: eq:solution
---
\mathbf{x}(t) = \left(q_1(t), \ldots, q_N(t), p_1(t), \ldots, p_N(t)\right) \,, 
```

starting at the initial condition 

```{math}
---
label: eq:init_condition
---
\mathbf{x}(0) = \mathbf{x}_0 = \left(q_1^0, \ldots, q_N^0, p_1^0, \ldots, p_N^0\right) \, .
```

We will assume that $H$ is sufficiently smooth to guarantee the uniqueness of solutions. If the Hamiltonian is time independent, that is $H(\mathbf{q},\mathbf{p})$, then the resulting dynamical system is autonomous (ref to part 1) and thus the solutions of Eq. {eq}`eq:hamiltons_eom` form a one-parameter family of diffeomorphisms, known as a _Hamiltonian flow_, given by $\{\phi_t\}_{t\in\mathbb{R}}$ so that

```{math}
---
label: eq:flow
---
\phi_s(\mathbf{x}(t))=\mathbf{x}(s+t) \;.
```

The family is a group because it satisfies the properties

* $\phi_0=Id$,
* $\phi_s\circ \phi_t=\phi_{t+s}$,
* $\phi_{-t} \circ \phi_t=\phi_0$.


## Symplectic maps

A linear transformation $C$ is symplectic if it satisfies

```{math}
---
label: eq:symp_cond
---
\begin{equation}
C \mathcal{J} C^T = \mathcal{J} = 
    \begin{pmatrix}
    0_N & I_N \\
    -I_N & 0_N
    \end{pmatrix}
\end{equation}
```

where $\mathcal{J}$ is a 2N $\times$ 2N matrix known as the symplectic matrix, and $I_N$ denotes the $N \times N$ identity matrix. The symplectic transformation $C$ maps the original coordinates $(x_1,\ldots, x_N, p_{x_1}, \ldots, p_{x_N})$ to the coordinates $(q_1, \ldots, q_N, p_1, \ldots, p_N)$ and Hamilton's equations in Eq, {eq}`eq:hamiltons_eom` as follows:

```{math}
\begin{equation}
    \begin{bmatrix}
    q_1 \\
    \vdots \\
    q_N \\
    p_1 \\
    \vdots \\
    q_N
    \end{bmatrix}
    = C
    \begin{bmatrix}
    x_1 \\
    \vdots \\
    x_N \\
    p_{x_1} \\
    \vdots \\
    p_{x_N} 
    \end{bmatrix} 
    \implies
    \begin{bmatrix}
    \dot{q}_1 \\
    \vdots \\
    \dot{q}_N \\ 
    \dot{p}_1 \\
    \vdots \\
    \dot{p}_N
    \end{bmatrix}
    = C
    \begin{bmatrix}
    \dot{x}_1 \\
    \vdots \\
    \dot{x}_N \\
    \dot{p}_{x_1} \\
    \vdots \\
    \dot{p}_{x_N}
    \end{bmatrix}
\end{equation}
```

From {eq}`eq:symp_cond` we find the inverse transformation $C^{-1}=\mathcal{J}C^T\mathcal{J}^{-1}$, such that

```{math}
\begin{equation}
\begin{bmatrix}
\dot{x}_1 \\
\vdots \\
\dot{x}_N \\
\dot{p}_{x_1} \\
\vdots \\
\dot{p}_{x_N} 
\end{bmatrix} 
= C^{-1}
\begin{bmatrix}
\dot{q}_1 \\
\vdots \\
\dot{q}_N \\ 
\dot{p}_1 \\
\vdots \\
\dot{p}_N
\end{bmatrix}
\end{equation}
```

Linear symplectic transformations are $C^\infty$ diffeomorphisms, which means that they have continuous derivatives of all orders and they also have a continuous inverse. This group of transformations is important because they preserve the form of the equations of motion {eq}`eq:hamiltons_eom`, and also phase space structures, such as normally hyperbolic invariant manifolds and their associated stable and unstable invariant manifolds. Furthermore, symplectic transformations preserve the stability of invariant sets and Lyapunov exponents of trajectories.

In Ref {cite}`naik_finding_2019`, we used the symplectic transformation to transform the uncoupled (separable) quadratic normal form to a coupled (non-separable) quadratic normal form Hamiltonian for two and three degrees of freedom systems. 

We can define nonlinear symplectic transformations using the _Poisson bracket_ (see {eq}`eq:poisson`) defined by

```{math}
---
label: eq:poisson
---
\begin{equation}
 \{A, B\} = \langle D A,\mathcal{J} D B \rangle = \sum\limits_{i=1}^{N} \left( \frac{\partial A}{\partial q_i}\frac{\partial B}{\partial p_i} - \frac{\partial A}{\partial p_i} \frac{\partial B}{\partial q_i} \right),
\end{equation}
```

where $D A$ and $D B$ are the gradients of $A$ and $B$, and $\mathcal{J}$ is defined in Eq. {eq}`eq:symp_cond`. For example, the Poisson bracket allows us to rewrite the equations of motion in Eq. {eq}`eq:hamiltons_eom` as

```{math}
---
label: eq:poisson_eqn
---
\begin{equation}
\dot{q}_i = \{q_i, H\} \quad,\quad \dot{p}_i = \{p_i, H\} \; , \quad \text{for } i = 1,\ldots,N
\end{equation}
```

Following {cite}`Wiggins2003`, a  symplectic transformations is a sufficiently smooth diffeomorphism defined on phase space $f:~\mathbb{R}^{2N}\rightarrow \mathbb{R}^{2N}$, such that 


```{math}
---
label: eq:symplectic
---
\begin{equation}
 \langle u, \mathcal{J}v \rangle = \langle u, (Df(x))^T\mathcal{J}Df(x) v \rangle,
\end{equation}
```

for any $x,u,v\in \mathbb{R}^{2N}$.

Under $f$, phase space points $(q,p)$ are transformed into $f(q,p)$ and the Hamiltonian $H(q,p)$ into the new Hamiltonian $G(f(q,p))$, that satisfies $Df(q,p)DH = DG$. The equations of motion {eq}`eq:poisson_eqn` then remain

```{math}
\begin{align*}
 \{(q,p),H\} = \langle D(q,p),\mathcal{J}DH \rangle &= \langle D(q,p),\;(Df(q,p))^T\mathcal{J}Df(q,p)DH \rangle \\
 &= \langle Df(q,p)D(q,p),\;\mathcal{J}Df(q,p)DH \rangle = \{f(q,p), G\}.
\end{align*}
```

For a coordinate free formulation using differential forms see {cite}`Arnold76`.


The flow of an autonomous Hamiltonian system is a symplectic transformation for each $t$. Another common example of a symplectic map is the return map associated with a Poincarè surface of section (See Chapter {ref}`3<sec:LDs>`), to be discussed in the next section. Other well known examples of symplectic maps include the cat map, standard map, and H{\'e}non map.
Symplectic maps arise in many applications in physics and chemistry, for example in celestial mechanics and dynamical astronomy, particle accelerators, plasma, and chemical reactions {cite}`meiss_symplectic_1992` to name but a few.


## Coordinates, ($q, p)$, $(q_i , p_i)$, significance of canonically conjugate pairs

The canonical coordinates $(q, p)$ satisfy the following Poisson bracket relations

```{math}
---
label: eq:pb_canonical
---
\begin{equation}
\{q_i, q_j\} = 0 \quad,\quad \{p_i, p_j\} = 0 \quad,\quad 
\{q_i, p_j\} = \delta_{ij} \; , \quad \text{for } i,j \in \{1,\ldots,N\}
\end{equation}
```

where $\delta_{ij}$ is the Kronecker delta. The pair $(q_i , p_i)$ is referred to as canonically conjugate. The relations above are referred to as the fundamental Poisson bracket equations and are preserved if and only if the coordinates are canonical. Further details on this can be found in the section 9.4 and 9.5 of the textbook {cite}`Goldstein2001`.

An important feature of canonically conjugate pairs lies in their role in defining Poincarè surfaces of section. A surface defined by $q_j = K$ with $\dot{q}_j \geq 0$ or $\dot{q}_j \leq 0$, or $p_j = K$ with $\dot{p}_j \geq 0$ or $\dot{p}_j \leq 0$, admits a symplectic (Poincarè) return map, provided it is a surface of section in the sense of Birkhoff {cite}`Birkhoff27`. Such a surface must be transverse to the flow and all trajectories that cross it must return. Suitably-chosen Poincarè surfaces of section and the associated return maps allow up to study the dynamics in phase space on a lower dimensional surface, for example they facilitate finding periodic orbits of the system as fixed points of the return maps. Note that such surfaces may not exist in every system.



## Phase space slices, phase space transversal slice


The phase space structures that govern the dynamics of a Hamiltonian system with $N$ degrees of freedom are of codimension-$1$ and codimension-$2$ in $2N$-dimensional phase space, in the case of an autonomous system codimension-$1$ and codimension-$2$ in the $2N-1$-dimensional energy surface {cite}`Waalkens08` (refer to hyperbolic section). A Poincarè surface of section is a $(2N - 2)$-dimensional surface, for example one specified by $q_j = K$ with $\dot{q}_j \geq 0$ or $\dot{q}_j \leq 0$,
where $j \in 1, 2, \ldots, N$ and $K$ is constant. For this Poincarè surface of section to be transverse to the flow, we require

```{math}
\begin{equation}
\dot{q}_j = \dfrac{\partial H}{\partial p_j} \neq 0 \, ,
\end{equation}
```

on the entire surface of section.

We note here that the complete $(2N - 2)$-dimensional surface cannot be visualized without projecting onto a $2$ or $3$ dimensional space. Even a three dimensional projection can be difficult to visualize due to the limitation of the viewing medium such as the screen or paper. However, if we consider a two-dimensional slice of the $2N-1$ dimensional energy surface, then the intersection of the slice with a codimension-$1$ or codimension-$2$ object is either one- or zero-dimensional provided they intersect. This follows  the rule 


\begin{equation*}
\text{dimension of intersection = (dimension of surface + dimension of object) - dimension of the space.}
\end{equation*}

Visualising one- or zero-dimensional intersections on a two-dimensional surface makes high-dimensional phase space structures accessible again. This visualization may not give us the whole picture of these structures in high-dimensional phase space but it is useful in order to obtain important dynamical information about these high-dimensional structures, for example to detect the intersections of the invariant manifolds and many others.


## Liouville's Theorem

> This subsection and concepts herein are adapted from <em>Classical Mechanics by Goldstein, 3rd edition</em>.

Suppose some property of the system is denoted by $A = A(\mathbf{x}, t)$, then the total time rate of change of this property along the solutions of an autonomous Hamiltonian system $H$ is 

```{math}
\frac{d A}{d t} = \frac{\partial A}{\partial t} + \sum\limits_{i=1}^{N} \left( \frac{\partial A}{\partial q_i}\dot{q}_i + \frac{\partial A}{\partial p_i} \dot{p}_i \right) = \frac{\partial A}{\partial t} + \sum\limits_{i=1}^{N} \left( \frac{\partial A}{\partial q_i}\frac{\partial H}{\partial p_i} - \frac{\partial A}{\partial p_i} \frac{\partial H}{\partial q_i} \right)
```

Using the definition of the _Poisson bracket_:

```{math}
\begin{equation}
\{A, H\} = \sum\limits_{i=1}^{N} \left( \frac{\partial A}{\partial q_i}\frac{\partial H}{\partial p_i} - \frac{\partial A}{\partial p_i} \frac{\partial H}{\partial q_i} \right)
\end{equation}
```

we can write the time evolution of the property as

```{math}
---
label: eq:property_conserved
---
\begin{equation}
\frac{d A}{d t} = \frac{\partial A}{\partial t} + \{A, H\}
\end{equation}
```

Therefore, if we assume that the Hamiltonian does not depend explicitly on time and use $A = H$ in the above equation, we get

```{math}
---
label: eq:energy_conserved
---
\begin{equation}
\frac{d H}{d t} = 0 + \{H, H\} = 0
\end{equation}
```

which implies that the Hamiltonian, $H$, is a constant of the motion for conservative systems, that is the total energy is fixed. Thus, the states for a specified energy are restricted to the $(2N - 1)$-dimensional surface embedded in the $2N$-dimensional phase space.

We use this set-up to present the mathematical statement of the Liouville's theorem which states: _when a classical ensemble evolves its location and shape in phase space may change but its volume will be conserved_.

A classical ensemble consists of a set of points in phase space, with each point representing a system in a specified state. Let $\rho(\mathbf{x},t)$ be the density of the set of points in a given volume. As each member of ensemble moves through phase space along a trajectory specified by Hamilton's equations of motion, the phase space density evolves in time.

Using Poisson brackets {eq}`eq:property_conserved`, we can express Liouville's theorem as

```{math}
\begin{equation}
\frac{d \rho}{d t} = \frac{\partial \rho}{\partial t} + \{\rho, H\} = 0,
\end{equation}
```

which means that the phase space density $\rho(\mathbf{x}, t)$ is conserved along the solutions of $H$. Consequently when an ensemble evolves, its location and shape in phase space change but its volume is conserved. It also follows that all autonomous Hamiltonian systems are volume preserving due to Liouville's theorem.

## Poincarè recurrence

> This section is adapted from the book <em>Applied Nonlinear Dynamical systems by S. Wiggins </em> (Springer, 2003) and the review article <em>Symplectic maps, variational principles, and transport by J.D. Meiss </em> (Rev. Mod. Phys. 1992).

Hamiltonian systems with a bounded energy surface have a recurrence property discovered by Henri Poincarè (1890). The Poincarè recurrence theorem states that every state of a system will return arbitrarily close to its initial state in finite (potentially very long) time. 

We know from Eq. {eq}`eq:energy_conserved` that autonomous Hamiltonian systems conserve energy and thus for $N$ degrees of freedom system, motion is constrained to a $(2N - 1)$-dimensional energy surface

\begin{equation*}
E = H(q_j, p_j) \;,\quad \text{where } j \in \{1, 2, \ldots, N\}
\end{equation*}

If the energy surface is bounded (compact), then the Poincarè recurrence theorem states that almost all trajectories (all but a set of zero volume) that begin on a Poincarè surface of section will return to it. For a formal statement and proof, see Theorem 7.6.3 in {cite}`Wiggins2003`.

Combining Liouville's theorem and Poincarè recurrence theorem leads to the conclusion, that a set of points of a given volume on a Poincarè surface of section will return to the surface and intersect it in a set of points of equal volume. The return map associated with this surface is therefore volume preserving.


As pointed out by Arnold {cite}`Arnold76`, _"The following prediction is a paradoxical conclusion from the theorems of Poincarè and Liouville: if you open a partition separating a chamber containing gas and a chamber with a vacuum, then after a while the gas molecules will again collect in the first chamber. The resolution of the paradox lies in the fact that"_ a while  may be longer than the duration of the solar system's existence.

# References

```{bibliography} bibliography/chapter1.bib
```