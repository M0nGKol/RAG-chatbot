<!-- page 1 -->
Operations Research

Linear Programming II

Transportation Model

Deals with special class of linear programming problem in which the objective is to transport a homogenous commodity from various facilities/origins to different destinations or markets at a minimum total cost.

Properties:
(i) It has an objective function
(ii) It has structural constraints
(iii) It has a non-negativity constraint
(iv) The relationship between variables and constraints are linear

Expression of transportation problem:

| | 1 | 2 | 3 | ... | n | SUPPLY |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **1** | $x_{11} | c_{11}$ | $x_{12} | c_{12}$ | $x_{13} | c_{13}$ | ... | $x_{1n} | c_{1n}$ | $a_1$ |
| **2** | $x_{21} | c_{21}$ | $x_{22} | c_{22}$ | $x_{23} | c_{23}$ | ... | $x_{2n} | c_{2n}$ | $a_2$ |
| **3** | $x_{31} | c_{31}$ | $x_{32} | c_{32}$ | $x_{33} | c_{33}$ | ... | $x_{3n} | c_{3n}$ | $a_3$ |
| **m** | $x_{m1} | c_{n1}$ | $x_{m2} | c_{n2}$ | $x_{m3} | c_{n3}$ | ... | $x_{mn} | c_{mn}$ | $a_m$ |
| **DEMAND** | $b_1$ | $b_2$ | $b_3$ | | $b_n$ | |

[FIGURE: A grid representing the transportation problem structure with origins (sources) on the vertical axis and destinations on the horizontal axis. Cells contain variables $x_{ij}$ representing quantities and coefficients $c_{ij}$ representing costs, while the final row and column denote supply $a_i$ and demand $b_j$ respectively.]

---

<!-- page 2 -->
$T_2$

Where $c_{ij}$ is the cost of transporting 1 unit of the product from $i^{th}$ origin to $j^{th}$ destination

$x_{ij}$ is the quantity transported from $i^{th}$ origin to $j^{th}$ destination

Objective:
To transport various quantities of goods from various origin to different destinations such that the cost of transportation is minimum.

### Transportation problem

[FIGURE: A tree diagram categorizing the Transportation Problem into "Balanced" and "Unbalanced" types. The Balanced branch notes that Demand = Supply ($\sum a_i = \sum b_j$), while the Unbalanced branch splits into Demand > Supply (requiring a dummy row with cost = 0) and Demand < Supply (requiring a dummy column with cost = 0).]

*   **Balanced**
    *   Demand = Supply
    *   $\sum a_i = \sum b_j$
*   **Unbalanced**
    *   **Demand > Supply**
        *   $\sum b_j > \sum a_i$
        *   Add a dummy row
        *   cost = 0
    *   **Demand < Supply**
        *   $\sum b_j < \sum a_i$
        *   Add a dummy column
        *   cost = 0

---

<!-- page 3 -->
$T_3$

Represented as $m \times n$ matrix
* Sources (origin) along rows
* Destination along columns

Solutions: 5 types

* Feasible solution: A set of non-negative allocations that satisfy the rim restrictions (necessary and sufficient conditions $\to$ total supply = total demand)
* Basic feasible solution: A feasible solution that contains no more than $m+n-1$ non-negative allocations
* Non-degenerate basic feasible solution: A basic feasible solution containing $m+n-1$ non-negative allocations and these are in independent positions.
* Degenerate basic feasible solution: A basic feasible solution where the total number of non-negative allocation is less than $m+n-1$
* Optimal solution: A feasible solution that minimizes transportation cost or maximizes profit

---

<!-- page 4 -->
T4

Methods:
* Feasible solution (Initial basic feasible solution)
    * North west corner method
    * Least cost method (Matrix minima)
    * Row minima method
    * Column minima method
    * Vogel's approximation method

Optimal solution:
* Modified distribution method
    * (non negative allocation = $m+n-1$)

---

<!-- page 5 -->
T5

### Problem 1
Solve the transportation problem consisting of demand and supply given in table below using North west corner method.

| | $D_1$ | $D_2$ | $D_3$ | Supply |
| :--- | :--- | :--- | :--- | :--- |
| $S_1$ | 4 | 8 | 8 | 76 |
| $S_2$ | 16 | 24 | 16 | 82 |
| $S_3$ | 8 | 16 | 24 | 77 |
| **Demand** | 72 | 102 | 41 | |

Total supply $= 76 + 82 + 77 = 235$
Total demand $= 72 + 102 + 41 = 215$
Supply > Demand
Unbalanced

Supply 235
Demand $215 + 20$ Add a dummy column

| | $D_1$ | $D_2$ | $D_3$ | Dummy | Supply |
| :--- | :--- | :--- | :--- | :--- | :--- |
| $S_1$ | 4 | 8 | 8 | 0 | 76 |
| $S_2$ | 16 | 24 | 16 | 0 | 82 |
| $S_3$ | 8 | 16 | 24 | 0 | 77 |
| **Demand** | 72 | 102 | 41 | 20 | |

We start with North west corner starting from $S_1 D_1$ (Here 4)
$\left. \begin{array}{l} \text{the demand is } 72 \\ \text{supply is } 76 \end{array} \right]$ Lowest is 72

---

<!-- page 6 -->
$T_6$

| | $D_1$ | $D_2$ | $D_3$ | Dummy | Supply |
| :--- | :--- | :--- | :--- | :--- | :--- |
| $S_1$ | 72 / 4 | 4 / 8 | 8 | 0 | 76 / 0 |
| $S_2$ | 16 | 82 / 24 | 16 | 0 | 82 / 0 |
| $S_3$ | 8 | 16 / 16 | 41 / 24 | 20 / 0 | 77 / 0 |
| Demand | 72 / 0 | 102 / 98 / 16 | 41 | 20 | |

[FIGURE: This is a transportation problem matrix (tableau) showing supply and demand constraints. It displays assigned quantities (top-left of each cell) and unit costs (bottom-right of each cell) for three supply nodes $S_1, S_2, S_3$ and four demand nodes.]

We write 72 in the cost (on top of 4) and cancel the column which becomes 0. The zero column gets cancelled.
$\begin{matrix} 76 \\ -72 \\ \hline 4 \end{matrix}$ (To balance)

Consider $S_1 D_2$, 8 is the value in $S_1 D_2$
Corresponding demand is 102, supply is 4. Minimum is 4. 4 goes inside cost.
$\begin{matrix} 102 \\ -4 \\ \hline 98 \end{matrix}$

The row becomes zero once 4 goes inside and the row gets cancelled.

Consider North west $S_2 D_2$, value is 24.
Corresponding demand is 98, supply is 82. Lowest is 82. 82 goes inside & supply becomes 0.
$\begin{matrix} 98 \\ -82 \\ \hline 16 \end{matrix}$

The row containing 0 supply is cancelled.

The next North west is $S_3 D_2$ which is 16.
Corresponding demand = 16, Supply = 77. Lowest is 16. 16 goes inside.

---

<!-- page 7 -->
$D_2$ becomes zero and supply becomes 61.
$\begin{array}{r}77 \\ -16 \\ \hline 61\end{array}$

Cancel the column containing 0.

The next North west is $S_3 D_3$ with 24

Corresponding supply = 61 | lowest is 41
Demand = 41 | 41 goes inside
$\begin{array}{r}61 \\ -41 \\ \hline 20\end{array}$

The supply becomes 20 and $D_3$ becomes 0.

Column $D_3$ is cancelled.

The next North west is $S_3$ Dummy which is 0

Corresponding row (supply) = 20 | Demand = supply
Demand = 20 | 20 goes inside
and demand &
supply becomes 0.
$\begin{array}{r}20 \\ -20 \\ \hline 0\end{array}$ $\begin{array}{r}20 \\ -20 \\ \hline 0\end{array}$

Minimum transportation cost is given by
$$(4 \times 72) + (8 \times 4) + (24 \times 82) + (16 \times 16)$$
$$+ (24 \times 41) + (0 \times 20)$$

$= \underline{3528}$

Number of allocated cells = 6
$= m + n - 1 = (4 + 3 - 1)$

These are non negative and independent (not closed path)
$\therefore$ The solution is non-degenerate.

4 columns
3 rows
$7 - 1 = 6$

---

<!-- page 8 -->
Problem 2:
Solve the transportation problem using least cost method (matrix minimum method)

| | $D_1$ | $D_2$ | $D_3$ | $D_4$ | Supply |
| :--- | :--- | :--- | :--- | :--- | :--- |
| $S_1$ | 6 | 4 | 1 | 5 | 14 |
| $S_2$ | 8 | 9 | 2 | 7 | 16 |
| $S_3$ | 4 | 3 | 6 | 2 | 5 |
| Demand | 6 | 10 | 15 | 4 | |

To balance the demand and supply
Total demand = $6 + 10 + 15 + 4 = 35$
Total supply = $14 + 16 + 5 = 35$

Demand = supply

For least cost method, among the $S_1, S_2, S_3$ and $D_1, D_2, D_3$ find the lowest number
Here, the row/column with lowest number is $S_1 D_3$
Which is 1

start the operation with this number
Leat value = 1, Corresponding demand = 15, Supply = 14 | lowest is 14

[FIGURE: A subtraction calculation showing 15 minus 14 equals 1, indicating that after allocating the supply of 14, the demand for column D3 is reduced from 15 to 1.]

When supply becomes 0, Row gets cancelled
14 goes inside
Supply becomes 0
Demand becomes 1

---

<!-- page 9 -->
| | $D_1$ | $D_2$ | $D_3$ | $D_4$ | Supply |
| :--- | :---: | :---: | :---: | :---: | :---: |
| $S_1$ | 6 | 4 | 1 | 5 | 140 |
| $S_2$ | 8 | 9 | 2 | 7 | 16 15 0 |
| $S_3$ | 4 | 3 | 6 | 2 | 05 1 0 |
| Demand | 10 | 10 0 | 15 10 | 4 0 | 35 |

[FIGURE: A transportation tableau grid showing supply values in rows and demand values in columns. Certain cells are marked with allocations, and some values have been crossed out to reflect updated supply and demand calculations.]

The next least number is 2.
2 repeats at $S_2 D_3$ and $S_3 D_4$. Choose any one.

Choose $S_2 D_3$ with least value 2.
Corresponding Supply = 16
Demand = 1
Lowest is 1. 1 goes inside & demand becomes 0.

The row becomes 15 and column $D_3$ becomes 0.
$D_3$ column gets cancelled.

$$\begin{array}{r} 16 \\ -1 \\ \hline 15 \end{array}$$

The next least value is 2 at $S_3 D_4$.
Corresponding Supply = 5
Demand = 4
Lowest is 4. 4 goes in & $D_4$ becomes 0.

$D_4$ gets cancelled.
$$\begin{array}{r} 5 \\ -4 \\ \hline 1 \end{array}$$
Supply becomes 1.

---

<!-- page 10 -->
T10

The next least value is at $S_3 D_2$ which is 3
Corresponding supply = 1 | lowest is 1
demand = 10 | 1 goes in &
Supply becomes 0
The supply row gets [ILLEGIBLE] cancelled.
The demand becomes 9
[FIGURE: A subtraction calculation showing 10 - 1 = 9, with an arrow indicating the update of the demand value.]

The next least value is at $S_2 D_1$ which is 8
Corresponding demand = 6 | lowest is 6
supply = 15 | 6 goes in
$D_1$ becomes 0
Supply becomes $15 - 6 = 9$

The only value available is 9 at $S_2 D_2$
The corresponding supply = 9 | Both are equal
Demand = 9 | Both goes in and
becomes 0
Supply becomes 0
Demand becomes 0
Supply and demand
gets cancelled.

Allocated cells are : $(1 \times 14) + (6 \times 6) + (9 \times 9) + (2 \times 1)$
$+ (3 \times 1) + (2 \times 4)$

Total Minimum Cost = 156

---

<!-- page 11 -->
Problem 3:
Find the initial feasible solution using Vogel's approximation method

| | $D_1$ | $D_2$ | $D_3$ | $D_4$ | Supply |
| :--- | :---: | :---: | :---: | :---: | :---: |
| $O_1$ | 11 | 13 | 17 | 14 | 250 |
| $O_2$ | 16 | 18 | 14 | 10 | 300 |
| $O_3$ | 21 | 24 | 13 | 10 | 400 |
| Demand | 200 | 225 | 275 | 250 | 950 |

Step 1: Total supply = $250 + 300 + 400 = 950$
Total demand = $200 + 225 + 275 + 250 = 950$
Total supply = Total demand (Balanced)

Step 2: Identify second minimum among demand and supply in each row and column

Row 1: 
The first minimum = 11 ($O_1, D_1$)
Second minimum = 13 ($O_1, D_2$)
Penalty = $13 - 11 = 2$
(calculate difference || penalty)

Row 2: 
First minimum = 10
Second minimum = 14
Penalty = $14 - 10 = 4$

Row 3: 
First minimum = 10
Second minimum = 13
Penalty = $13 - 10 = 3$

Note:
First minimum = least minimum value

---

<!-- page 12 -->
| | $D_1$ | $D_2$ | $D_3$ | $D_4$ | Supply | $P_1$ | $P_2$ | $P_3$ | $P_4$ | $P_5$ |
|---|---|---|---|---|---|---|---|---|---|---|
| $O_1$ | 11 | 13 | 17 | 14 | 250 | 2 | 1 | - | - | - |
| $O_2$ | 16 | 18 | 14 | 10 | 300 | 4 | 4 | 4 | 4 | - |
| $O_3$ | 21 | 24 | 13 | 10 | 400 | 3 | 3 | 3 | 3 | 3 |
| Demand | 200 | 225 | 275 | 250 | | | | | | |

[FIGURE: A table showing Row-wise penalties for a transportation problem with three origins ($O_1, O_2, O_3$) and four destinations ($D_1, D_2, D_3, D_4$). It displays the cost matrix along with supply/demand constraints and calculated penalties across multiple iterations.]

| Column wise penalty | $D_1$ | $D_2$ | $D_3$ | $D_4$ |
|---|---|---|---|---|
| $P_1$ | 5↑ | 5 | 1 | 0 |
| $P_2$ | - | 5↑ | 1 | 0 |
| $P_3$ | - | 6↑ | 1 | 0 |
| $P_4$ | - | - | 1 | 0 |
| $P_5$ | - | - | 13↑ | 10 |

[FIGURE: A table showing Column-wise penalties for the same transportation problem. It tracks the penalties for each column across five iterative steps ($P_1$ to $P_5$) to determine optimal allocation.]

| | $D_1$ | $D_2$ | $D_3$ | $D_4$ | Supply |
|---|---|---|---|---|---|
| $O_1$ | [200] 11 | [50] 13 | 17 | 14 | 250→50→0 |
| $O_2$ | 16 | [175] 18 | 14 | [125] 10 | 300→125→0 |
| $O_3$ | 21 | 24 | [275] 13 | [125] 10 | 400→125→0 |
| Demand | 200→0 | 225→175→0 | 275→0 | 250→125→0 | |

[FIGURE: The final allocation table for the transportation problem with crossed-out values indicating the exhaustion of supply and demand. The boxed values represent the units allocated to each origin-destination pair to satisfy the constraints.]

---

<!-- page 13 -->
$T_{13}$

Column 1: 
First minimum = 11
Second minimum = 16
Penalty = $16 - 11 = 5$

Column 2: 
First minimum = 13
Second minimum = 18
Penalty = $18 - 13 = 5$

Column 3: 
First minimum = 13
Second minimum = 14
Penalty = $14 - 13 = 1$

Column 4: 
First minimum = 10
Second minimum = 10
Penalty = $10 - 10 = 0$

Step 3:
Of all the penalties given in $P_1$, the maximum penalty = 5 (in $D_1$ and $D_2$) choose any one of the two [among $\underline{5}, \underline{5}, 1, 0, 3, 4, 2$]

Choose the row/column corresponding to maximum penalty

Step 4:
Select the least number and solve the demand and supply problem (using least cost method)

Step 5:
After cancelling column/row, proceed with $P_2$ (Penalty 2) from Row 1

---

<!-- page 14 -->
Calculating penalty 2: $T_{14}$

*   Select first row,
    *   First minimum $= 13$
    *   Second minimum $= 14$
    *   Penalty $= 14 - 13 = 1$
*   Row 2:
    *   First minimum $= 10$
    *   Second minimum $= 14$
    *   Penalty $= 14 - 10 = 4$
*   Row 3:
    *   First minimum $= 10$
    *   Second minimum $= 13$
    *   Penalty $= 13 - 10 = 3$
*   Column 1: cancelled
*   Column 2:
    *   First minimum $= 13$
    *   Second minimum $= 18$
    *   Penalty $= 18 - 13 = 5$
*   Column 3:
    *   First minimum $= 13$
    *   Second minimum $= 14$
    *   Penalty $= 14 - 13 = 1$
*   Column 4:
    *   First minimum $= 10$
    *   Second minimum $= 10$
    *   Penalty $= 10 - 10 = 0$

Of all the penalties in $P_2$, the maximum is 5 at $D_2$. This corresponds to column $D_2$.

---

<!-- page 15 -->
In column $D_2$, minimum value is 13.
Undertaking least cost method,
Delete Row 1 since the value of $O_1$ is zero.
(Row 1 gets cancelled)

Consider row 2,
First minimum = 10
Second minimum = 14
Penalty = $14 - 10 = 4$

Consider row 3,
First minimum = 10
Second minimum = 13
Penalty = $13 - 10 = 3$

Consider Column 1, $D_1$, cancelled.

Consider Column 2, $D_2$,
First minimum = 18
Second minimum = 24
Penalty = $24 - 18 = 6$

Consider Column 3, $D_3$,
First minimum = 13
Second minimum = 14
Penalty = $14 - 13 = 1$

Consider Column 4, $D_4$,
First minimum = 10
Second minimum = 10
Penalty = $10 - 10 = 0$

Of Penalty $P_3$, the maximum penalty is 6.
This corresponds to Column $D_2$.

---

<!-- page 16 -->
In the column $D_2$, we have two values 18 and 24 (after cancellation of Row 1)
Of these, 18 is lowest
Undertaking least cost method, we get $D_2$ zero
$D_2$ gets cancelled
Now we have Columns $D_3$ and $D_4$ & Rows $O_2$ & $O_3$

Consider row 2,
First minimum = 10
Second minimum = 14
Penalty = $14 - 10 = 4$

Consider row 3,
First minimum = 10
Second minimum = 13
Penalty = $13 - 10 = 3$

Consider Column $D_1$ & $D_2$ are cancelled

Consider Column $D_3$,
First minimum = 13
Second minimum = 14
Penalty = $14 - 13 = 1$

Consider Column $D_4$,
First minimum = 10
Second minimum = 10
Penalty = $10 - 10 = 0$

Consider Penalty 4 ($P_4$), the maximum value = 4
This corresponds to second row $O_2$
Rows $R_1$ and Columns $D_1$ & $D_2$ are cancelled

---

<!-- page 17 -->
The minimum value corresponding to row $O_2$ in Penalty 4 is 10 (at $O_2 D_4$)

Consider $D_4 O_2$, Minimum value is 10
Undertaking least cost method
Row 2 ($O_2$ gets cancelled)

Now we have row 3, calculating penalty,
$13 - 10 = 3$

Column $D_3$ and $D_4$ only are available
Of these penalty, penalty for $D_3$ is 13
penalty for $D_4$ is 10

Among $P_5$, highest penalty value is 13 at $D_3$
We select column $D_3$ and undertake least cost method
$D_3$ becomes zero and $D_3$ gets cancelled

Now we have $O_3 D_4$ with value 10

Allocated cells = 6
$(m+n-1)$
The allocations are independent
The solution is non-degenerate
Transportation cost $= (11 \times 200) + (13 \times 50) + (18 \times 175) + (10 \times 125) + 13(275) + 10(125)$
$= 12075$