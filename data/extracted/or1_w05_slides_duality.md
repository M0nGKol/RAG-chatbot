<!-- page 1 -->
# Linear Programming

## Duality:

The primal is given by
$$\text{Max. } Z = 40x_1 + 35x_2 \text{ subject to}$$
$$2x_1 + 3x_2 \le 60$$
$$4x_1 + 3x_2 \le 96$$
$$x_1, x_2 \ge 0$$
[FIGURE: A vertical text annotation in the left margin indicates that the above defined system is called the PRIMAL problem.]

Find duality.

### Conditions for Duality:
*   For Maximization, all constraints $\le$ RHS
*   Minimization, all constraints $\ge$ RHS

## Dual is given by
$$\text{Minimize. } W = 60y_1 + 96y_2 \text{ subject to}$$
$$2y_1 + 4y_2 \ge 40$$
$$3y_1 + 3y_2 \ge 35$$
$$y_1, y_2 \ge 0$$

---

<!-- page 2 -->
Find the duality of
$$
\text{Min. } Z = 40x_1 + 20x_2 \text{ subject to}
$$
$$
3x_1 + 2x_2 \ge 48
$$
$$
x_1 + 3x_2 \ge 81
$$
$$
2x_1 - x_2 \le 61
$$
$$
x_1, x_2 \ge 0
$$

[FIGURE: A red bracket encompasses the constraint equations of the linear programming problem, labeled as "PRIMAL" with an arrow pointing to the equations, indicating that this set represents the original optimization problem.]

### Conditions for duality
For Minimization, all constraints $\ge$ RHS
The primal can be correctly rewritten as
$$
\text{Min. } Z = 40x_1 + 20x_2 \text{ subject to}
$$
$$
3x_1 + 2x_2 \ge 48
$$
$$
x_1 + 3x_2 \ge 81
$$
$$
-2x_1 + x_2 \ge -61
$$

The dual is given by
$$
\text{Max. } W = 48y_1 + 81y_2 - 61y_3 \text{ subject to}
$$
$$
3y_1 + 1y_2 - 2y_3 \le 40
$$
$$
2y_1 + 3y_2 + 1y_3 \le 20
$$
$$
y_1, y_2, y_3 \ge 0
$$

---

<!-- page 3 -->
Find the duality of
$$\text{Max } Z = x_1 + 2x_2 \text{ subject to}$$
$$2x_1 + 4x_2 \leq 160$$
$$x_1 - x_2 = 30$$
$$x_1 \geq 10$$
$$x_1, x_2 \geq 0$$

In the constraint 2, there is equality sign.
Equality can be $\geq$ or $\leq$.
Since the question is of Maximization type.
As a rule, we use constraints $\leq$ RHS for Maximization.
Here, we have 2 symbols $\geq$ and $\leq$.
We first use $\leq$ (since Maximization problem)
Subsequently we use $\geq$ in the constraint 2 above.

$$\text{Max. } Z = x_1 + 2x_2 \text{ subject to}$$
$$2x_1 + 4x_2 \leq 160$$
$$x_1 - x_2 \leq 30$$
$$x_1 - x_2 \geq 30$$
$$x_1 \geq 10$$
$$x_1, x_2 \geq 0$$

[FIGURE: A boxed note titled "Remember" that outlines the standard forms for maximization problems. It indicates that for a "Max" problem, the right-hand side constraints should use $\leq$ for the first constraint and $\geq$ for the second constraint.]

We rewrite the above equation for
Maximization using symbol $\leq$ for all the constraints

---

<!-- page 4 -->
Max. $Z = 1x_1 + 2x_2$ subject to
$y_1: 2x_1 + 4x_2 \le 160$
$y_2: 1x_1 - 1x_2 \le 30$
$y_3: -1x_1 + 1x_2 \le -30$
$y_4: -1x_1 \le -10$

$x_1, x_2 \ge 0$

For dual, we minimize the function
Min $W = 160y_1 + 30y_2 - 30y_3 - 10y_4$
Subject to

[FIGURE: A red box containing the note "We change symbol to $\ge$ for Min." which explains the conversion process for the dual problem constraints.]

$2y_1 + 1y_2 - 1y_3 - 1y_4 \ge 1$
$4y_1 - 1y_2 + 1y_3 + 0y_4 \ge 2$

$y_1, y_2, y_3, y_4 \ge 0$

Min $W = 160y_1 + (30y_2 - 30y_3) - 10y_4$

Since we split the equal to into 2 parts, we merge the 2 together
Min $W = 160y_1 + 30(y_2 - y_3) - 10y_4$

Let $y_2 - y_3 = y'$ (Replace $y_2 - y_3$ with $y'$)

We rewrite the objective function and the constraints as

---

<!-- page 5 -->
Min $W = 160y_1 + 30y' - 10y_4$ subject to
$2y_1 + y' - y_4 \ge 1$
$4y_1 - y' \ge 2$
$y_1, y_4 \ge 0$
$y'$ is unrestricted $y' \ge 0$ or $y' \le 0$