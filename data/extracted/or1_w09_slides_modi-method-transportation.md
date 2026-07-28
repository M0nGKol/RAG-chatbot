<!-- page 1 -->
Transportation problem
Modified Distribution (MODI) method / u-v method

1. Solve the transportation problem using MODI method

| | $D_1$ | $D_2$ | $D_3$ | Capacities |
| :--- | :--- | :--- | :--- | :--- |
| $S_1$ | 5 | 1 | 8 | 14 |
| $S_2$ | 9 | 4 | 0 | 13 |
| $S_3$ | 17 | 6 | 7 | 30 |
| Requirements | 31 | 11 | 15 | |

[FIGURE: A transportation cost matrix table showing supplies $S_1, S_2, S_3$ and demands $D_1, D_2, D_3$. It lists the unit transportation costs for each route and the total capacity and requirement constraints.]

Step 1: Checking for balanced rows & columns
$14 + 13 + 30 = 57$ (columns)
$31 + 11 + 15 = 57$ (rows)

Applying North West Corner method

| | $D_1$ | $D_2$ | $D_3$ | Capacities |
| :--- | :--- | :--- | :--- | :--- |
| $S_1$ | (14) 5 | 1 | 8 | 14 0 |
| $S_2$ | 9 | (13) 4 | 0 | 13 0 |
| $S_3$ | 17 | (4) 6 | (11) 7 | (15) 30 26 15 0 |
| Requirements | 31 17 6 0 | 11 0 | 15 0 | 57 57 |

[FIGURE: A transportation tableau showing the initial feasible solution calculated via the North West Corner method. It includes allocated quantities in circles within cells and reflects the exhaustion of supply and demand constraints with crossed-out values.]

---

<!-- page 2 -->
no. of cells allocated = 5
$m+n-1 = 3+3-1 = 5$
Both are same
The solution is nondegenerate

Initial feasible solution $= (14 \times 5) + (13 \times 9) + (4 \times 17) + (11 \times 6) + (15 \times 7)$
$= 70 + 117 + 68 + 66 + 105$
$= 426$

Checking for Optimality using U-V method / Modi method.

$C_{ij} = u_i + v_j \rightarrow$ allocated cells.

[FIGURE: A 3x3 transport cost table with circled costs in specific cells. The table shows occupied cells with allocations (5, 9, 17, 6, 7) and corresponding unit costs (14, 13, 4, 11, 15) to calculate potentials $u_i$ and $v_j$.]

Assume $u_1 = 0$
$C_{11} = u_1 + v_1$
$5 = 0 + v_1 \Rightarrow v_1 = 5$

$C_{21} = u_2 + v_1$
$9 = u_2 + 5 \Rightarrow u_2 = 4$

$C_{31} = u_3 + v_1$
$17 = u_3 + 5 \Rightarrow u_3 = 12$

$C_{32} = u_3 + v_2$
$6 = 12 + v_2 \Rightarrow v_2 = -6$

$C_{33} = u_3 + v_3$
$7 = 12 + v_3 \Rightarrow v_3 = -5$

Allocated cells are $C_{11}, C_{21}, C_{31}, C_{32}, C_{33}$

$u_1 = 0$
$u_2 = 4$
$u_3 = 12$

$v_1 = 5$
$v_2 = -6$
$v_3 = -5$

---

<!-- page 3 -->
Calculating opportunity cost of unallocated cells

[FIGURE: A 3x3 grid showing cost values in specific cells. The grid represents a transportation matrix where the values 1, 8, 4, and 0 are placed in the unallocated cells to calculate their opportunity costs.]

$$\Delta_{ij} = C_{ij} - (u_i + v_j)$$
$$\hookrightarrow \text{for unallocated cells}$$

$$\Delta_{12} = C_{12} - (u_1 + v_2)$$
$$= 1 - (0 + -6) = +7$$

$$\Delta_{13} = C_{13} - (u_1 + v_3)$$
$$= 8 - (0 + -5) = +13$$

$$\Delta_{22} = C_{22} - (u_2 + v_2)$$
$$= 4 - (4 + -6) = +6$$

$$\Delta_{23} = C_{23} - (u_2 + v_3)$$
$$= 0 - (4 + -5) = +1$$

$\Delta_{12}, \Delta_{13}, \Delta_{22}, \Delta_{23}$ all have +ve values.
The initial feasible solution is optimal & unique.

Rules:
1. If $\Delta_{ij}$ has all positive values, the solution is optimum and unique.
2. If $\Delta_{ij}$ has a zero value, the solution is optimum, not unique.
3. If $\Delta_{ij}$ has negative values, the solution is neither optimum, nor unique.

---

<!-- page 4 -->
4

2. Calculate optimum transportation cost using Modi method.

| | $D_1$ | $D_2$ | $D_3$ | Capacities |
| :--- | :--- | :--- | :--- | :--- |
| $S_1$ | 5 | 1 | 8 | 12 |
| $S_2$ | 9 | 4 | 0 | 14 |
| $S_3$ | 17 | 6 | 7 | 4 |
| Requirements | 9 | 10 | 11 | |

$\sum \text{Capacities} = 12 + 14 + 4 = 30$ ] Balanced
$\sum \text{Requirements} = 9 + 10 + 11 = 30$

Solving the above using least cost method:

[FIGURE: A transportation cost matrix showing the initial allocation of goods using the Least Cost Method. It indicates the cost values in each cell, the circled allocated quantities, and the row/column totals, demonstrating the step-by-step assignment process.]

| | $D_1$ | $D_2$ | $D_3$ | Capacities |
| :--- | :--- | :--- | :--- | :--- |
| $S_1$ | 5 (2) | 1 (10) | 8 | 12 |
| $S_2$ | 9 (3) | 4 | 0 (11) | 14 |
| $S_3$ | 17 (4) | 6 | 7 | 4 |
| Requirements | 9 | 10 | 11 | |

Number of cells allocated = 5
$m + n - 1 = 3 + 3 - 1 = 5$
] The solution is non-degenerate

Initial feasible solution $= (2 \times 5) + (1 \times 10) + (9 \times 3) + (0 \times 11) + (17 \times 4)$
$= 10 + 10 + 27 + 0 + 68$
$= 115$

---

<!-- page 5 -->
Checking for optimality using $u-v$ method

Allocated cells $\rightarrow c_{ij} = u_i + v_j$

[FIGURE: A 3x3 table representing a transportation grid. It shows allocated values of 5, 1, 9, 0, and 17 within specific cells, with circled numbers (2, 10, 3, 11, 4) indicating positions or indices of allocated cells.]

Let $u_1 = 0$
$c_{11} = u_1 + v_1$
$5 = 0 + v_1 \Rightarrow v_1 = 5$
$c_{12} = u_1 + v_2$
$1 = 0 + v_2 \Rightarrow v_2 = 1$
$c_{21} = u_2 + v_1$
$9 = u_2 + 5 \Rightarrow u_2 = 4$
$c_{23} = u_2 + v_3$
$0 = 4 + v_3 \Rightarrow v_3 = -4$
$c_{31} = u_3 + v_1$
$17 = u_3 + 5 \Rightarrow u_3 = 12$

$u_1 = 0$  $v_1 = 5$
$u_2 = 4$  $v_2 = 1$
$u_3 = 12$ $v_3 = -4$

Checking opportunity cost of unallocated cells

[FIGURE: A 3x3 grid showing opportunity costs for the unallocated cells. The values 8, 4, 6, and 7 are placed in their respective empty cells to calculate the optimality criterion.]

$\Delta_{ij} = c_{ij} - (u_i + v_j)$
$\Delta_{13} = c_{13} - (u_1 + v_3) = 8 - (0 + -4) = +12$
$\Delta_{22} = c_{22} - (u_2 + v_2) = 4 - (4 + 1) = -1$
$\Delta_{32} = c_{32} - (u_3 + v_2) = 6 - (12 + 1) = -7$
$\Delta_{33} = c_{33} - (u_3 + v_3) = 7 - (12 + -4) = -1$

There is one +ve and three -ve values $\Delta_{22}, \Delta_{32}, \Delta_{33}$
Maximum negative number is $\Delta_{32} = -7$

---

<!-- page 6 -->
6

Putting together values obtained from allocated cells & unallocated cells,

| | | |
| :--- | :--- | :--- |
| (2) 5 | (10) 1 | 8 |
| (3) 9 | 4 | (11) 0 |
| (4) 17 | 6 | 7 |

[FIGURE: This 3x3 table displays numerical values in cells, with some values circled to indicate specific assignments. It represents the state of a transportation problem tableau where allocations or cost-related values are being evaluated.]

From the above cells, the maximum negative values obtained is $-7$, from unallocated $\Delta_{32}$ lies in cell $_{32}$
The $C_{32} = 6$.
$\Delta_{32} \rightarrow C_{32} = 6$

[FIGURE: This table illustrates the modification of a transportation grid by adding or subtracting units along a closed path. It highlights how values change by drawing arrows and plus/minus signs between cells.]

Allocate +ve symbols to $C_{32} + C_{11}$
-ve symbols to $C_{12} + C_{31}$

In the cells with -ve symbols, we have (10) and (4)
Of the two, lesser value is (4)

Select (4) $\left[ \begin{aligned} & \text{In -ve cells, subtract} \\ & \text{In +ve cells, add} \end{aligned} \right]$

(4) - (4) = 0
(10) - (4) = 6
(2) + (4) = 6
(0) + (4) = 4

[FIGURE: This 3x3 table shows the final adjusted allocations for the transportation problem. It reflects the updated values in the grid after applying the adjustments calculated from the previous step.]

---

<!-- page 7 -->
7

[FIGURE: A 3x3 transportation cost matrix with allocations in circles. The rows have total supply constraints of 12, 14, and 4, while the columns have total demand constraints of 9, 10, and 11, totaling 30.]

| | | | Supply |
| :--- | :--- | :--- | :--- |
| (6) 5 | (6) 1 | 8 | 12 |
| (3) 9 | 4 | (11) 0 | 14 |
| 17 | (4) 6 | 7 | 4 |
| **Demand** | (9) (10) (11) | | 30 |

Initial feasible solution $= (6 \times 5) + (6 \times 1) + (3 \times 9) + (11 \times 0) + (4 \times 6)$

$= 30 + 6 + 27 + 0 + 24$

$= 87$

$\left. \begin{aligned} \text{No. of allocated cells} &= 5 \\ m + n - 1 &= 3 + 3 - 1 = 5 \end{aligned} \right]$ the solution is non-degenerate