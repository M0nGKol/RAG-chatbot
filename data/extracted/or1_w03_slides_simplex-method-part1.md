<!-- page 1 -->
(1)

# Operations Research

## Linear Programming Models
### Simplex method

In simplex method, the problem is always maximization type.
The constants are "$\le$".

Eg. 1: Maximize $Z = x_1 + 4x_2$ subject to
$$2x_1 + x_2 \le 3$$
$$3x_1 + 5x_2 \le 9$$
$$x_1 + 3x_2 \le 5 \quad \text{and} \quad x_1, x_2 \ge 0$$

Objective function: Max. $Z = x_1 + 4x_2$ s.t.

Constraints:
$$2x_1 + x_2 \le 3$$
$$3x_1 + 5x_2 \le 9$$
$$x_1 + 3x_2 \le 5$$

There are three constraints, we will introduce three slack variables in the above equation, $(s_1, s_2, s_3)$.

Step 1: Standard form of equation is
$$Max. Z = x_1 + 4x_2 + 0s_1 + 0s_2 + 0s_3$$
Taking the variables in the objective function to the left side, we get

---

<!-- page 2 -->
$Max \ z - x_1 - 4x_2 + 0S_1 + 0S_2 + 0S_3 = 0$

$2x_1 + x_2 + 1S_1 + 0S_2 + 0S_3 = 3$

$3x_1 + 5x_2 + 0S_1 + 1S_2 + 0S_3 = 9$

$x_1 + 3x_2 + 0S_1 + 0S_2 + 1S_3 = 5$

$x_1, x_2, S_1, S_2, S_3 \geq 0$

Table 1

| | Basic variable | $x_1$ | $x_2$ | $S_1$ | $S_2$ | $S_3$ | RHS | RHS key column |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| $R_1$ | $z$ | -1 | -4 | 0 | 0 | 0 | 0 | $\frac{0}{-4} = 0$ |
| $R_2$ | $S_1$ | 2 | 1 | 1 | 0 | 0 | 3 | $\frac{3}{1} = 3$ |
| $R_3$ | $S_2$ | 3 | 5 | 0 | 1 | 0 | 9 | $\frac{9}{5} = 1.8$ |
| $R_4$ | $S_3$ | 1 | 3 | 0 | 0 | 1 | 5 | $\frac{5}{3} = 1.67$ |

[FIGURE: A simplex tableau showing the initial iteration. The $x_2$ column is circled as the key column, and the $R_4$ row is circled to indicate the pivot row identified by the smallest positive ratio.]

Consider coefficients on the top row (Table 1)
Identify the coefficient that is more negative
-4 is more negative than -1
Circle the column containing the more -ve number, -4. This column is called key column

Divide the RHS by key column, we get
$\frac{0}{-4} = 0$
$\frac{3}{1} = 3$
$\frac{9}{5} = 1.8$
$\frac{5}{3} = 1.67$

Of these, the smallest positive ratio is 1.67
We select this row

---

<!-- page 3 -->
The row containing smallest positive ratio is called key row. Here the smallest positive ratio is $5/3$.

The intersection of key row and key column is called key element.

In this problem, the key element is $3$.

Now, we have to make key element $1$. This is possible by dividing the entire row by $3$.

Table 2:

| | Basic variable | Coefficient of | | | | | RHS |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| | | $x_1$ | $x_2$ | $S_1$ | $S_2$ | $S_3$ | |
| $R_1$ | $Z$ | $-1$ | $-4$ | $0$ | $0$ | $0$ | $0$ |
| $R_2$ | $S_1$ | $2$ | $1$ | $1$ | $0$ | $0$ | $3$ |
| $R_3$ | $S_2$ | $3$ | $5$ | $0$ | $1$ | $0$ | $9$ |
| $R_4$ | $S_3$ | $1/3$ | $1$ | $0$ | $0$ | $1/3$ | $5/3$ |

[FIGURE: This table shows a simplex tableau for a linear programming problem. A red oval highlights the second column (the key column) and the fourth row (the key row), indicating that the element at their intersection is the key element being processed.]

With the help of key element, convert the rows above and below key element to zero.

With the help of $R_4$, make $R_3$ zero

$R_3 \to R_3 - 5R_4$

$5 - 5(1) = 5 - 5 = 0$

$3 - 5(\frac{1}{3}) = 3 - \frac{5}{3} = \frac{9-5}{3} = \frac{4}{3}$

$0 - 5(0) = 0 - 0 = 0$

$1 - 5(0) = 1 - 0 = 1$

$0 - 5(\frac{1}{3}) = -\frac{5}{3}$

$9 - 5(\frac{5}{3}) = 9 - \frac{25}{3} = \frac{27-25}{3} = \frac{2}{3}$

---

<!-- page 4 -->
With the help of $R_4$, make $R_2$ zero.
$$R_2 \to R_2 - R_4$$
$$2 - \frac{1}{3} = \frac{6-1}{3} = \frac{5}{3}$$
$$1 - 1 = 0$$
$$1 - 0 = 1$$
$$0 - 0 = 0$$
$$1 - \frac{1}{3} = -\frac{1}{3}$$
$$3 - \frac{5}{3} = \frac{9-5}{3} = \frac{4}{3}$$

With the help of $R_4$, make $R_1$ zero.
$$R_1 \to R_1 + 4R_4$$
$$-4 + 4(1) = -4 + 4 = 0$$
$$-1 + 4\left(\frac{1}{3}\right) = -1 + \frac{4}{3} = \frac{4}{3} - 1 = \frac{1}{3}$$
$$0 + 4(0) = 0 + 0 = 0$$
$$0 + 4(0) = 0 + 0 = 0$$
$$0 + 4\left(\frac{1}{3}\right) = \frac{4}{3}$$
$$0 + 4\left(\frac{5}{3}\right) = \frac{20}{3}$$

Table 3:

| | Basic variable | Coefficient of | | | | | RHS |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| | | $x_1$ | $x_2$ | $S_1$ | $S_2$ | $S_3$ | |
| $R_1$ | $Z$ | $1/3$ | $0$ | $0$ | $0$ | $4/3$ | $20/3$ |
| $R_2$ | $S_1$ | $5/3$ | $0$ | $1$ | $0$ | $-1/3$ | $4/3$ |
| $R_3$ | $S_2$ | $4/3$ | $0$ | $0$ | $1$ | $-5/3$ | $2/3$ |
| $R_4$ | $S_3$ | $1/3$ | $(1)^*$ | $0$ | $0$ | $1/3$ | $5/3$ |

[FIGURE: A Simplex method tableau showing the coefficients of variables in rows $R_1$ through $R_4$. An arrow points from the table to the text indicating that $x_2$ replaces $S_3$ in the basis.]

There is no negative term in Row 1 ($R_1$)
we have value $Z = \frac{20}{3}$

---

<!-- page 5 -->
In Table 2, consider key element 3, $S_3$ is the at the key row and $x_2$ is at the key column.
$S_3$ will leave and $x_2$ will enter replacing $S_3$

[FIGURE: A simplex tableau showing basic variables $Z, S_1, S_2, x_2$ with their coefficients for variables $x_1, x_2, S_1, S_2, S_3$ and the RHS values. A loop and arrow indicate the pivot operation involving $S_3$ and $x_2$.]

| | Basic Variable | Coefficients of | | | | | RHS |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| $R_1$ | $Z$ | $x_1$ | $x_2$ | $S_1$ | $S_2$ | $S_3$ | $20/3$ |
| | | $1/3$ | $0$ | $0$ | $0$ | $4/3$ | |
| $R_2$ | $S_1$ | $5/3$ | $0$ | $1$ | $0$ | $-1/3$ | $4/3$ |
| $R_3$ | $S_2$ | $4/3$ | $0$ | $0$ | $1$ | $-5/3$ | $2/3$ |
| $R_4$ | $x_2$ | $1/3$ | $1$ | $0$ | $0$ | $1/3$ | $5/3$ |

From the above $x_2 = 5/3$ Max $Z = 20/3$
$x_1 = ?$

$\text{Max } Z = x_1 + 4x_2$
$\frac{20}{3} = x_1 + 4\left(\frac{5}{3}\right)$
$\frac{20}{3} = x_1 + \frac{20}{3}$
$x_1 = \frac{20}{3} - \frac{20}{3} = 0$
$\therefore x_1 = 0$

The solution is $Z_{max} = \frac{20}{3}$, $x_1 = 0$, $x_2 = \frac{5}{3}$