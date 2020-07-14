# The Setting: Hamiltonian Dynamics on Phase Space

\section{Configuration Space and Phase space}
\label{sec:Ham1}
\fbox{%
\begin{minipage}{\linewidth}
\begin{center}
The concepts in this section are adapted from the books \cite{lifshitz1978,wiggins2003applied}.  
\end{center}

\end{minipage}
} 

\bigskip

\begin{description}

\item[\underline{\textbf{Generalized Coordinates:}}] The location of the particles comprising a system are described by a set of coordinates, known in Mechanics as generalized coordinates. The space, i.e. all possible values, described by these coordinates is referred to as {\em configuration space}.

\item[\underline{\textbf{Degrees-of-freedom (DoF):}}] The number of DoF is the number of independent generalized coordinates required to describe the configuration of the system, i.e. it is the dimension of the configuration space.

\item[\underline{\textbf{Momenta:}}] In the canonical Hamiltonian framework, each configuration space variable has an associated canonically conjugate variable which are referred to as momentum variables.

\item[\underline{\textbf{Phase space:}}] The collection of all the configuration and momentum variables is referred to as the phase space of the Hamiltonian dynamical system. 

\end{description}


\section{Hamilton's Equations}

Consider an $n$ DoF system described by the scalar function $H(\mathbf{q},\mathbf{p},t)$, known as the Hamiltonian of the system, which smoothly depends on the configuration space coordinates $\mathbf{q} = (q_1,\ldots,q_n) \in \mathbb{R}^{n}$, their canonically conjugate momenta $\mathbf{p} = (p_1,\ldots,p_n) \in \mathbb{R}^{n}$ and time. Hamilton's equations are a set of $2n$ first-order differential equations:
\begin{equation}
\begin{cases}
\dot{q}_i = \dfrac{\partial H}{\partial p_i} \\[.4cm]
\dot{p}_i = -\dfrac{\partial H}{\partial q_i} 
\end{cases}
\; , \qquad \; i = 1, 2, \ldots, n,
\label{eq:hamiltoneq}
\end{equation}
that describe the dynamics of the system, where the dot symbol over a variable denotes the total time derivative, that is $\cdot \equiv d/dt$. When the Hamiltonian function does not depend on time explicitly, the dynamical system it generates by means of Eq. \eqref{eq:hamiltoneq} is said to be \emph{autonomous}.




\section{Conserved quantities in phase space}

\fbox{%
\begin{minipage}{\linewidth}
\begin{center}
The reader can find more details on Poisson brackets and their properties \\ in many books and lecture notes, see e.g. \cite{lifshitz1978,arnold1978,giorgilli2002}. 
\end{center}

\end{minipage}
} 

\bigskip

Given a Hamiltonian system, a function $A(\mathbf{q}, \mathbf{p},t)$ is called an \textbf{integral of motion}, \textbf{constant of motion} or \textbf{first integral} if it remains constant along a trajectory. Then, its total time derivative is zero along solutions $(\mathbf{q}(t),\mathbf{p}(t))$ of Hamilton's equations, that is

\begin{equation}
    \dfrac{dA}{dt} = \dfrac{\partial A}{\partial t} + \sum\limits_{i = 1}^n \left( \dfrac{\partial A}{\partial q_i} \dfrac{d q_i}{dt} + \dfrac{\partial A}{\partial p_i} \dfrac{d p_i}{dt} \right)  = \dfrac{\partial A}{\partial t} + 
    \sum\limits_{i = 1}^n \left( \dfrac{\partial A}{\partial q_i}\dfrac{\partial H}{\partial p_i}- \dfrac{\partial A}{\partial p_i}  \dfrac{\partial H}{\partial q_i} \right) = 0.
    \label{eq:integral}
\end{equation}

\noindent
The quantity

\begin{equation}
    \{A,H\} = \sum\limits_{i = 1}^n \left( \dfrac{\partial A}{\partial q_i}\dfrac{\partial H}{\partial p_i}- \dfrac{\partial A}{\partial p_i}  \dfrac{\partial H}{\partial q_i} \right),
    \label{eq:poisson}
\end{equation}

\noindent
is called the \textit{Poisson bracket} of the functions $A$ and $H$. Therefore, Eq. \eqref{eq:integral} is equivalent to:
\begin{equation}
\dfrac{dA}{dt} = \frac{\partial A}{\partial t} + \{A,H\} = 0. \label{eq:integral2}
\end{equation}
Notice that if the function $A$ does not explicitly depend on time, that is $\partial A / \partial t = 0$, then $A$ is an integral of motion if and only if  $\{A, H\} = 0$. In other words, the Poisson bracket provides us with a useful test to see if a function of the phase space variables and time is conserved or not in a Hamiltonian system. In particular, if the Hamiltonian of the system is time-independent, that is $H = H(\mathbf{q},\mathbf{p})$, then we can deduce that:
\begin{equation}
    \frac{dH}{dt} = \dfrac{\partial H}{\partial t} +  \{ H, H \} = 0 + \sum\limits_{i = 1}^n \left( \dfrac{\partial H}{\partial q_i}\dfrac{\partial H}{\partial p_i}- \dfrac{\partial H}{\partial p_i}  \dfrac{\partial H}{\partial q_i} \right) = 0 \;, 
\end{equation}
which implies that the Hamiltonian itself is a constant of the motion. If the Hamiltonian represents the total energy of the physical system, this property is just the law of conservation of total energy along trajectories of an autonomous Hamiltonian system. The implicit time dependence of the position and momentum coordinates may increase/decrease the kinetic energy at the expense/gain of the potential energy, but the sum of kinetic and potential energy remains constant.

Another example of a quantity that is a constant of the motion is provided by ignorable or cyclic coordinates. A generalized coordinate $q_i$ is said to be \textit{ignorable} or \textit{cyclic} if it does not appear in the expression of the Hamiltonian function. By Hamilton's equations in Eq. \eqref{eq:hamiltoneq}, this implies that
\begin{equation}
    \dot{p}_i = - \dfrac{\partial H}{\partial q_i} = 0
\end{equation}
and therefore the momentum $p_i$ is constant along trajectories, that is, $p_i(t) = p_i^0$.

We introduce next a concept which is important for the study of integrable Hamiltonian systems. Integrable Hamiltonian systems are those that can be solved by quadratures and are characterized by Liouville-Arnold theorem, see \cite{arnold1978} and the contents in Section \ref{sec:Ham2}. Two constants of the motion $A$ and $B$ are said to be in \textit{involution} if they satisfy
\begin{equation}
    \{A,B\} = 0 \;.
    \label{eq:involution}
\end{equation}



\section{Invariant Sets}
\fbox{%
\begin{minipage}{\linewidth}
\begin{center}
The concepts here are adapted from \cite{wiggins2003applied}.
\end{center}
\end{minipage}
} 

\bigskip

Invariant sets play a fundamental role in how we understand the nature of phase space dynamics. We will give here a definition for this concept for an autonomous dynamical system in the continuous time setting:
\begin{equation}
    \dot{x} = f(x) \;, \quad x \in \mathbb{R}^{n}
    \label{eq:cont_ds}
\end{equation}
and also for a map (discrete time dynamics): 
\begin{equation}
    x \mapsto g(x) \;, \quad x\in \mathbb{R}^{n}
    \label{eq:disc_ds}
\end{equation}

\begin{definition} 
\label{def:invset}
Let $S \subset \mathbb{R}^{n}$ be a set of the phase space of the dynamical system, then

\begin{itemize}

\item \underline{\textbf{Continuous time:}} $S$ is invariant under the flow generated by Eq. \eqref{eq:cont_ds} if for any point $x_{0} \in S$ we have that  $x(t;x_{0}) \in S$ for all $t \in I$, where $x(t;x_{0})$ denotes the solution of Eq. \eqref{eq:cont_ds} with initial condition $x(0) = x_{0}$, and $I$ is the time interval of existence of the solution. 

\item \underline{\textbf{Discrete time:}} $S$ is said to be invariant under the map in Eq. \eqref{eq:disc_ds} if for any $x_{0}\in S$, the orbit (trajectory) associated to that initial condition remains inside the set for all iterates of the map, that is $g^{n}(x_{0})\in S$, for all $n$.

\end{itemize}
\end{definition}

Invariant sets play an important role for the analysis of dynamical systems, as they allow us to break up the dynamics into smaller parts. For example the dynamics in invariant sets can be investigated separately from the rest of the system. As we will show in the following sections, some invariant sets, such as invariant manifolds, naturally divide the phase space of the system into regions of qualitatively distinct dynamical behavior that can be studied independently.




\section{Hamiltonian flows and symplectic maps}
\label{sec:ham2}

\subsection{Hamiltonian flows}

A Hamiltonian system with $N$ degrees of freedom is described by the Hamiltonian function $H(\mathbf{q},\mathbf{p},t)$, which depends on the generalized coordinates $\mathbf{q} = (q_1,\ldots,q_N)$, their canonically conjugate momenta $\mathbf{p} = (p_1,\ldots,p_N)$, and time. This scalar function gives rise to a $2N$-dimensional dynamical system by means of Hamilton's equations of motion
\begin{equation}
\dot{q}_i = \frac{\partial H}{\partial p_i} \quad,\quad \dot{p}_i = -\frac{\partial H}{\partial q_i} \;, \quad \text{for} \; i = 1, 2, \ldots, N. \label{eqn:hamiltons_eom}
\end{equation}
where the dot symbol represents the total time derivative, that is,  $\cdot \equiv d/dt$. A state of the system is represented by a point in the $2N$-dimensional \emph{phase space}, Any solution of this system is a trajectory of the form
\begin{equation}
\mathbf{x}(t) = \left(q_1(t), \ldots, q_N(t), p_1(t), \ldots, p_N(t)\right) \,, 
\label{eqn:solution}
\end{equation}
starting at the initial condition 
\begin{equation}
\mathbf{x}(0) = \mathbf{x}_0 = \left(q_1^0, \ldots, q_N^0, p_1^0, \ldots, p_N^0\right) \, . \label{eqn:init_condition}
\end{equation}

We will assume that $H$ is sufficiently smooth to guarantee the uniqueness of solutions. If the Hamiltonian is time independent, that is $H(\mathbf{q},\mathbf{p})$, then the resulting dynamical system is autonomous (ref to part 1) and thus the solutions of Eq. \eqref{eqn:hamiltons_eom} form a one-parameter family of diffeomorphisms, known as a \emph{Hamiltonian flow}, given by $\{\phi_t\}_{t\in\mathbb{R}}$ so that
\begin{equation}
\phi_s(\mathbf{x}(t))=\mathbf{x}(s+t) \;. \label{eqn:flow}
\end{equation}
The family is a group because it satisfies the properties
\begin{itemize}
 \item $\phi_0=Id$,
 \item $\phi_s\circ \phi_t=\phi_{t+s}$,
 \item $\phi_{-t} \circ \phi_t=\phi_0$.
\end{itemize}
 

\subsection{Symplectic maps}
A linear transformation $C$ is symplectic if it satisfies
%
\begin{equation}
C \mathcal{J} C^T = \mathcal{J} = \begin{pmatrix}
0_N & I_N \\
-I_N & 0_N
\end{pmatrix}
\label{eqn:symp_cond}
\end{equation}
%
where $\mathcal{J}$ is a 2N $\times$ 2N matrix known as the symplectic matrix, and $I_N$ denotes the $N \times N$ identity matrix. The symplectic transformation $C$ maps the original coordinates $(x_1,\ldots, x_N, p_{x_1}, \ldots, p_{x_N})$ to the coordinates $(q_1, \ldots, q_N, p_1, \ldots, p_N)$ and Hamilton's equations in Eq, \eqref{eqn:hamiltons_eom} as follows:
%
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
\end{bmatrix}.
\end{equation}

From \eqref{eqn:symp_cond} we find the inverse transformation $C^{-1}=\mathcal{J}C^T\mathcal{J}^{-1}$, such that

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
\end{bmatrix}.
\end{equation}

Linear symplectic transformations are $C^\infty$ diffeomorphisms, which means that they have continuous derivatives of all orders and they also have a continuous inverse. This group of transformations is important because they preserve the form of the equations of motion \eqref{eqn:hamiltons_eom}, and also phase space structures, such as normally hyperbolic invariant manifolds and their associated stable and unstable invariant manifolds. Furthermore, symplectic transformations preserve the stability of invariant sets and Lyapunov exponents of trajectories.

In Ref~\cite{naik_finding_2019}, we used the symplectic transformation to transform the uncoupled (separable) quadratic normal form to a coupled (non-separable) quadratic normal form Hamiltonian for two and three degrees of freedom systems. 



We can define nonlinear symplectic transformations using the \emph{Poisson bracket} (see \eqref{eq:poisson}) defined by
\begin{equation}
 \{A, B\} = \langle D A,\mathcal{J} D B \rangle = \sum\limits_{i=1}^{N} \left( \frac{\partial A}{\partial q_i}\frac{\partial B}{\partial p_i} - \frac{\partial A}{\partial p_i} \frac{\partial B}{\partial q_i} \right),
\label{eqn:poisson}
\end{equation}
where $D A$ and $D B$ are the gradients of $A$ and $B$, and $\mathcal{J}$ is defined in Eq. \eqref{eqn:symp_cond}. For example, the Poisson bracket allows us to rewrite the equations of motion in Eq. \eqref{eqn:hamiltons_eom} as
\begin{equation}
\dot{q}_i = \{q_i, H\} \quad,\quad \dot{p}_i = \{p_i, H\} \; , \quad \text{for } i = 1,\ldots,N
 \label{eqn:poisson_eqn}
\end{equation}
Following \cite{Wiggins2003}, a  symplectic transformations is a sufficiently smooth diffeomorphism defined on phase space $f:~\mathbb{R}^{2N}\rightarrow \mathbb{R}^{2N}$, such that 
\begin{equation}
 \langle u, \mathcal{J}v \rangle = \langle u, (Df(x))^T\mathcal{J}Df(x) v \rangle,
\label{eqn:symplectic}
\end{equation}
for any $x,u,v\in \mathbb{R}^{2N}$.
Under $f$, phase space points $(q,p)$ are transformed into $f(q,p)$ and the Hamiltonian $H(q,p)$ into the new Hamiltonian $G(f(q,p))$, that satisfies $Df(q,p)DH = DG$. The equations of motion \eqref{eqn:poisson_eqn} then remain
\begin{align*}
 \{(q,p),H\} = \langle D(q,p),\mathcal{J}DH \rangle &= \langle D(q,p),\;(Df(q,p))^T\mathcal{J}Df(q,p)DH \rangle \\
 &= \langle Df(q,p)D(q,p),\;\mathcal{J}Df(q,p)DH \rangle = \{f(q,p), G\}.
\end{align*}
For a coordinate free formulation using differential forms see \cite{Arnold76}.


The flow of an autonomous Hamiltonian system is a symplectic transformation for each $t$. Another common example of a symplectic map is the return map associated with a Poincar\'e surface of section ({\bf refer to LD chapter}), to be discussed in the next section. Other well known examples of symplectic maps include the cat map, standard map, and H{\'e}non map.
Symplectic maps arise in many applications in physics and chemistry, for example in celestial mechanics and dynamical astronomy, particle accelerators, plasma, and chemical reactions \cite{meiss_symplectic_1992} to name but a few.


\section{Coordinates, ($q, p)$, $(q_i , p_i)$, significance of canonically conjugate pairs}

The canonical coordinates $(q, p)$ satisfy the following Poisson bracket relations
\begin{equation}
\{q_i, q_j\} = 0 \quad,\quad \{p_i, p_j\} = 0 \quad,\quad 
\{q_i, p_j\} = \delta_{ij} \; , \quad \text{for } i,j \in \{1,\ldots,N\}
\label{eqn:pb_canonical}
\end{equation}
where $\delta_{ij}$ is the Kronecker delta. The pair $(q_i , p_i)$ is referred to as canonically conjugate. The relations above are referred to as the fundamental Poisson bracket equations and are preserved if and only if the coordinates are canonical. Further details on this can be found in the section 9.4 and 9.5 of the textbook~\cite{Goldstein2001}.

An important feature of canonically conjugate pairs lies in their role in defining Poincar\'e surfaces of section. A surface defined by $q_j = K$ with $\dot{q}_j \geq 0$ or $\dot{q}_j \leq 0$, or $p_j = K$ with $\dot{p}_j \geq 0$ or $\dot{p}_j \leq 0$, admits a symplectic (Poincar\'e) return map, provided it is a surface of section in the sense of Birkhoff \cite[Chapter 5]{Birkhoff27}. Such a surface must be transverse to the flow and all trajectories that cross it must return. Suitably-chosen Poincar\'e surfaces of section and the associated return maps allow up to study the dynamics in phase space on a lower dimensional surface, for example they facilitate finding periodic orbits of the system as fixed points of the return maps. Note that such surfaces may not exist in every system.




\section{Phase space slices, phase space transversal slice}


The phase space structures that govern the dynamics of a Hamiltonian system with $N$ degrees of freedom are of codimension-$1$ and codimension-$2$ in $2N$-dimensional phase space, in the case of an autonomous system codimension-$1$ and codimension-$2$ in the $2N-1$-dimensional energy surface \cite{Waalkens08} (refer to hyperbolic section). A Poincar\'e surface of section is a $(2N - 2)$-dimensional surface, for example one specified by $q_j = K$ with $\dot{q}_j \geq 0$ or $\dot{q}_j \leq 0$,
where $j \in 1, 2, \ldots, N$ and $K$ is constant. For this Poincar\'e surface of section to be transverse to the flow, we require
\begin{equation}
\dot{q}_j = \dfrac{\partial H}{\partial p_j} \neq 0 \, ,
\end{equation}
on the entire surface of section.

We note here that the complete $(2N - 2)$-dimensional surface cannot be visualized without projecting onto a $2$ or $3$ dimensional space. Even a three dimensional projection can be difficult to visualize due to the limitation of the viewing medium such as the screen or paper. However, if we consider a two-dimensional slice of the $2N-1$ dimensional energy surface, then the intersection of the slice with a codimension-$1$ or codimension-$2$ object is either one- or zero-dimensional provided they intersect. This follows  the rule 
$$\text{dimension of intersection = (dimension of surface + dimension of object) - dimension of the space.}$$
Visualising one- or zero-dimensional intersections on a two-dimensional surface makes high-dimensional phase space structures accessible again. This visualization may not give us the whole picture of these structures in high-dimensional phase space but it is useful in order to obtain important dynamical information about these high-dimensional structures, for example to detect the intersections of the invariant manifolds and many others.


\section{Liouville's Theorem}

\fbox{%
\begin{minipage}{\linewidth}
This subsection and concepts herein are adapted from \emph{Classical Mechanics by Goldstein, 3rd edition}.
\end{minipage}
}

Suppose some property of the system is denoted by $A = A(\mathbf{x}, t)$, then the total time rate of change of this property along the solutions of an autonomous Hamiltonian system $H$ is 
\begin{equation}
\frac{d A}{d t} = \frac{\partial A}{\partial t} + \sum\limits_{i=1}^{N} \left( \frac{\partial A}{\partial q_i}\dot{q}_i + \frac{\partial A}{\partial p_i} \dot{p}_i \right) = \frac{\partial A}{\partial t} + \sum\limits_{i=1}^{N} \left( \frac{\partial A}{\partial q_i}\frac{\partial H}{\partial p_i} - \frac{\partial A}{\partial p_i} \frac{\partial H}{\partial q_i} \right)
\end{equation}
Using the definition of the \emph{Poisson bracket}:
\begin{equation}
\{A, H\} = \sum\limits_{i=1}^{N} \left( \frac{\partial A}{\partial q_i}\frac{\partial H}{\partial p_i} - \frac{\partial A}{\partial p_i} \frac{\partial H}{\partial q_i} \right)
\end{equation}
we can write the time evolution of the property as
\begin{equation}
\frac{d A}{d t} = \frac{\partial A}{\partial t} + \{A, H\}
\label{eqn:property_conserved}
\end{equation}
Therefore, if we assume that the Hamiltonian does not depend explicitly on time and use $A = H$ in the above equation, we get
\begin{equation}
\frac{d H}{d t} = 0 + \{H, H\} = 0
\label{eqn:energy_conserved}
\end{equation}
which implies that the Hamiltonian, $H$, is a constant of the motion for conservative systems, that is the total energy is fixed. Thus, the states for a specified energy are restricted to the $(2N - 1)$-dimensional surface embedded in the $2N$-dimensional phase space.

We use this set-up to present the mathematical statement of the Liouville's theorem which states: \emph{when a classical ensemble evolves its location and shape in phase space may change but its volume will be conserved}.

A classical ensemble consists of a set of points in phase space, with each point representing a system in a specified state. Let $\rho(\mathbf{x},t)$ be the density of the set of points in a given volume. As each member of ensemble moves through phase space along a trajectory specified by Hamilton's equations of motion, the phase space density evolves in time.



Using Poisson brackets \eqref{eqn:property_conserved}, we can express Liouville's theorem as
\begin{equation}
\frac{d \rho}{d t} = \frac{\partial \rho}{\partial t} + \{\rho, H\} = 0,
\end{equation}
which means that the phase space density $\rho(\mathbf{x}, t)$ is conserved along the solutions of $H$. Consequently when an ensemble evolves, its location and shape in phase space change but its volume is conserved. It also follows that all autonomous Hamiltonian systems are volume preserving due to Liouville's theorem.



\section{Poincar\'e recurrence}

\fbox{%
\begin{minipage}{\linewidth}
This section is adapted from the book \emph{Applied Nonlinear Dynamical systems by S. Wiggins (Springer, 2003)} and the review article \emph{Symplectic maps, variational principles, and transport by J.D. Meiss (Rev. Mod. Phys. 1992)}.
\end{minipage}
}

\vspace{.5cm}

Hamiltonian systems with a bounded energy surface have a recurrence property discovered by Henri Poincar\'e (1890). The Poincar\'e recurrence theorem states that every state of a system will return arbitrarily close to its initial state in finite (potentially very long) time. 

We know from Eq. \eqref{eqn:energy_conserved} that autonomous Hamiltonian systems conserve energy and thus for $N$ degrees of freedom system, motion is constrained to a $(2N - 1)$-dimensional energy surface
$$ E = H(q_j, p_j) \;,\quad \text{where } j \in \{1, 2, \ldots, N\} $$
If the energy surface is bounded (compact), then the Poincar\'e recurrence theorem states that almost all trajectories (all but a set of zero volume) that begin on a Poincar\'e surface of section will return to it. For a formal statement and proof, see Theorem 7.6.3 in \cite{Wiggins2003}.

Combining Liouville's theorem and Poincar\'e recurrence theorem leads to the conclusion, that a set of points of a given volume on a Poincar\'e surface of section will return to the surface and intersect it in a set of points of equal volume. The return map associated with this surface is therefore volume preserving.


As pointed out by Arnold \cite[p. 71]{Arnold76}, ``The following prediction is a paradoxical conclusion from the theorems of Poincar\'e and Liouville: if you open a partition separating a chamber containing gas and a chamber with a vacuum, then after a while the gas molecules will again collect in the first chamber. The resolution of the paradox lies in the fact that ``a while  may be longer than the duration of the solar system's existence''. 

