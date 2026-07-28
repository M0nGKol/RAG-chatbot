<!-- page 1 -->
Operations Research
Linear Programming Models
Simplex method

Eg: 2: Maximize $Z = 23a + 32b$ subject to
$10a + 6b \le 2500$
$5a + 10b \le 2000$
$1a + 2b \le 500$

Standardizing the above equation
Max $Z = 23a + 32b - 0s_1 - 0s_2 - 0s_3$
Max $Z - 23a - 32b + 0s_1 + 0s_2 + 0s_3 = 0$
$10a + 6b + 1s_1 + 0s_2 + 0s_3 = 2500$
$5a + 10b + 0s_1 + 1s_2 + 0s_3 = 2000$
$1a + 2b + 0s_1 + 0s_2 + 1s_3 = 500$

Table 1 :
[FIGURE: A simplex tableau showing the coefficients of variables a, b, s1, s2, and s3 along with the RHS and ratio columns. The column for 'b' and row R3 are circled in red to identify the key column and key row.]

| | | Coefficients | | | | | RHS | RHS key column |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| | $Z$ | $a$ | $b$ | $s_1$ | $s_2$ | $s_3$ | | |
| $R_1$ | | -23 | -32 | 0 | 0 | 0 | 0 | $\frac{0}{-32} = 0$ |
| $R_2$ | $s_1$ | 10 | 6 | 1 | 0 | 0 | 2500 | $\frac{2500}{6} = 416.67$ |
| $R_3$ | $s_2$ | 5 | 10 | 0 | 1 | 0 | 2000 | $\frac{2000}{10} = 200$ |
| $R_4$ | $s_3$ | 1 | 2 | 0 | 0 | 1 | 500 | $\frac{500}{2} = 250$ |

The smallest positive ratio is 200
Key row is $R_3$ and key element is 10

---

<!-- page 2 -->
$R_1 + R_3 (32) \quad -32 + 32 = 0 \quad [\text{key column}]$
$-23 + \frac{1}{2}(32) = -23 + 16 = -7$
$0 + 0(32) = 0 + 0 = 0$
$0 + \frac{1}{10}(32) = \frac{32}{10}$
$0 + 0(32) = 0$
$0 + 200(32) = 6400$

Consider $R_4$, $R_4 \rightarrow R_4 - R_3(2)$
$2 - 2 = 0 \quad [\text{key column}]$
$1 - \frac{1}{2}(2) = 1 - 1 = 0$
$0 - 0(2) = 0$
$0 - \frac{1}{10}(2) = -\frac{1}{5}$
$1 - 0(2) = 1 - 0 = 1$
$500 - 200(2) = 100$

In the Table 2, the Row $R_1$ has negative number
The maximum negative value is $-7$
The column corresponding to $-7$ will be key column
Circle the key column

Divide the RHS by key column
The minimum value is $185.75$ which is $R_2$
The key row becomes $R_2$
Circle the key Row $R_2$

---

<!-- page 3 -->
3

Table 2:

| | Basic Variable | Coefficients | | | | | RHS | RHS / Key Column |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| | | $a$ | $b$ | $s_1$ | $s_2$ | $s_3$ | | |
| $R_1$ | $z$ | $-7$ | $0$ | $0$ | $32/10$ | $0$ | $6400$ | $6400 / -7 = -914.28$ |
| $R_2$ | $s_1$ | $7^*$ | $0$ | $1$ | $-3/5$ | $0$ | $1300$ | $1300 / 7 = 185.71$ |
| | | $1$ | $0$ | $1/7$ | $-3/35$ | $0$ | $1300/7$ | |
| $R_3$ | $s_2$ | $1/2$ | $1^*$ | $0$ | $1/10$ | $0$ | $200$ | $200 / (1/2) = 400$ |
| $R_4$ | $s_3$ | $0$ | $0$ | $0$ | $-1/5$ | $1$ | $100$ | $100 / 0 = \infty$ |

[FIGURE: This table presents a simplex tableau used in linear programming optimization. It shows the current state of variables $a, b, s_1, s_2, s_3$ with specific cells marked with an asterisk to denote the pivot element and row selection.]

We divide $R_3$ by $10$ to get key element $1$
$\therefore R_3 \rightarrow R_3 (\frac{1}{10})$ [Table 2 above]

We have to make the key columns at $R_2, R_1, R_4$ zero.

Consider $R_2 \rightarrow R_2 - R_1(6)$ [Table 1]
$6 - 1(6) = 0$ [Key column]
$10 - \frac{1}{2}(6) = 10 - 3 = 7$
$1 - 0(6) = 1 - 0 = 1$
$0 - \frac{1}{10}(6) = -\frac{3}{5}$
$0 - 0(6) = 0 - 0 = 0$
$2500 - 200(6) = 2500 - 1200 = 1300$

Similarly, we make the key column at $R_1$ zero
$R_1 \rightarrow R_1 + 32 R_3$

---

<!-- page 4 -->
4

In the Table 2, the key element is $7$.
To make key element $1$, divide the $R_2$ by $7$.

$R_2 \to R_2 (\frac{1}{7})$

$7(\frac{1}{7}) = 1$ [key element]

$0(\frac{1}{7}) = 0$

$1(\frac{1}{7}) = \frac{1}{7}$

$-\frac{3}{5}(\frac{1}{7}) = -\frac{3}{35}$

$0(\frac{1}{7}) = 0$

$1300(\frac{1}{7}) = \frac{1300}{7}$

Table 3:

| | Base Variable | a | b | $s_1$ | $s_2$ | $s_3$ | RHS |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| $R_1$ | $Z$ | 0 | 0 | 1 | $13/5$ | 0 | 7700 |
| $R_2$ | a | $1^*$ | 0 | $1/7$ | $-3/35$ | 0 | $1300/7$ |
| $R_3$ | $s_2$ | 0 | 1 | $-1/14$ | $1/7$ | 0 | $750/7$ |
| $R_4$ | $s_3$ | 0 | 0 | 0 | $-1/5$ | 1 | 100 |

[FIGURE: This is a simplex method tableau representing the state of a linear programming problem after a pivot operation. It identifies the basic variables for each row and lists the coefficients for variables a, b, s1, s2, and s3, with the right-hand side (RHS) values for the current system of equations.]

---

<!-- page 5 -->
Consider Row $R_1$, we need to make the key column zero.

$R_1 \to R_1 + R_2(7) \quad -7 + 1(7) = 0$ [key column at $R_1$]

$0 + 0(7) = 0 + 0 = 0$

$0 + \frac{1}{7}(7) = 0 + 1 = 1$

$\frac{32}{10} + \frac{-3}{35}(7) = \frac{16}{5} - \frac{3}{5} = \frac{16-3}{5} = \frac{13}{5}$

$0 + 0(7) = 0 + 0 = 0$

$6400 + \frac{1300}{7}(7) = 7700$

Consider Row $R_3$, we need to make the key column at $R_3$ zero.

$R_3 \to R_3 - R_2(\frac{1}{2})$

$\frac{1}{2} - 1(\frac{1}{2}) = 0$ [key column]

$1 - 0(\frac{1}{2}) = 1 - 0 = 1$

$0 - \frac{1}{7}(\frac{1}{2}) = -\frac{1}{14}$

$\frac{1}{10} - (\frac{-3}{35})(\frac{1}{2}) = \frac{1}{10} + \frac{3}{70} = \frac{70+30}{700} = \frac{1}{7}$

$0 - 0(\frac{1}{2}) = 0 - 0 = 0$

$200 - \frac{1300}{7}(\frac{1}{2}) = 200 - \frac{650}{7} = \frac{750}{7}$

---

<!-- page 6 -->
6

Coming to Row $R_4$, we notice that the key column is already zero.
$\therefore$ We leave the $R_4$ as it is

Consider Row $R_1$, it is observed that the $R_1$ is positive.
We replace the slack $s_1$ on key row by the corresponding coefficient in key column $s_1$ is replaced by with a

The final value is
$$Z = 7700$$
$$a = \frac{1300}{7} = 185.71$$
$$b = ? \text{ (unknown)}$$

From the objective function, $Z = 23a + 32b$
$$\therefore 7700 = 23(185.71) + 32b$$
$$7700 = 4271.33 + 32b$$
$$32b = 7700 - 4271.33$$
$$32b = 3428.67$$
$$b = \frac{3428.67}{32} = 107.14$$

$\therefore$ The answer is
$$Z = 7700$$
$$a = 185.71$$
$$b = 107.14$$