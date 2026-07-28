<!-- page 1 -->
8

Checking optimality of the solution using MODI method / uv method

[FIGURE: A 3x3 grid containing numerical values in each cell, with specific values circled representing allocated quantities. It represents the initial transportation solution for a problem, with the assignment $u_1=0$ indicated to the right.]

| | | |
| :--- | :--- | :--- |
| (6) 5 | (6) 1 | 8 |
| (3) 9 | 4 | (11) 0 |
| 17 | (4) 6 | 7 |

Given in the solution for the problem discussed in the previous chapter.

Consider allocated cells $C_{ij} = u_i + v_j$

$u_1 = 0 \quad v_1 = 5$
$u_2 = 4 \quad v_2 = 1$
$u_3 = 5 \quad v_3 = -4$

$C_{11} = u_1 + v_1$
$5 = 0 + v_1 \Rightarrow v_1 = 5$

$C_{12} = u_1 + v_2$
$1 = 0 + v_2 \Rightarrow v_2 = 1$

$C_{21} = u_2 + v_1$
$9 = u_2 + 5 \Rightarrow u_2 = 4$

$C_{23} = u_2 + v_3$
$0 = 4 + v_3 \Rightarrow v_3 = -4$

$C_{32} = u_3 + v_2$
$6 = u_3 + 1 \Rightarrow u_3 = 5$

---

<!-- page 2 -->
Checking opportunity cost of the unallocated cells
$\Delta_{ij} = c_{ij} - (u_i + v_j)$
$\Delta_{13} = c_{13} - (u_1 + v_3) \Rightarrow 8 - (0 + -4) \Rightarrow +12$
$\Delta_{22} = c_{22} - (u_2 + v_2) \Rightarrow 4 - (4 + 1) \Rightarrow -1$
$\Delta_{31} = c_{31} - (u_3 + v_1) \Rightarrow 17 - (5 + 5) \Rightarrow +7$
$\Delta_{33} = c_{33} - (u_3 + v_3) \Rightarrow 7 - (5 + -4) \Rightarrow +6$

There is only one negative $\Delta_{22} = -1$ in the cell $C_{22}$

[FIGURE: A 3x3 grid showing transport costs in each cell and specific values circled in the top-left and top-middle cells. This figure represents the step of identifying a loop in the transportation problem where cell C22 is selected to enter the basis.]

Assign +ve to this cell $C_{22}$
$C_{22}$ & $C_{11}$ are -ve cells
$C_{12}$ & $C_{21}$ are +ve cells

Consider circled values in all cells,
In the -ve cells, least value is 3

The new cell becomes

[FIGURE: A 3x3 grid showing the updated allocation of units after adjusting the loop. It demonstrates the shift of units between cells to reach a new feasible solution.]

Add to +ve cells, subtract in -ve cells
$6 - 3 = 3$
$3 - 3 = 0$ (null)
$6 + 3 = 9$
$0 + 3 = 3$

Initial feasible solution = $(9 \times 5) + (3 \times 1) + (3 \times 4) + (11 \times 0) + (4 \times 6) = 84$

Allocated cells = 5
$m + n - 1 = 3 + 3 - 1 = 5$
The solution is non-degenerate

---

<!-- page 3 -->
10

Checking for optimality for the allocated cells (using MODI method)

[FIGURE: A 3x3 matrix grid representing a transportation problem table. Cells contain cost values with small circled numbers representing the quantity allocated to specific cells.]

$u_i=0$ Allocated cells $C_{ij} = u_i + v_j$

$C_{11} = u_1 + v_1$
$5 = 0 + v_1 \Rightarrow v_1 = 5$

$C_{12} = u_1 + v_2$
$1 = 0 + v_2 \Rightarrow v_2 = 1$

$C_{22} = u_2 + v_2$
$4 = u_2 + 1 \Rightarrow u_2 = 3$

$C_{23} = u_2 + v_3$
$0 = 3 + v_3 \Rightarrow v_3 = -3$

$C_{32} = u_3 + v_2$
$6 = u_3 + 1 \Rightarrow u_3 = 5$

$u_1 = 0 \quad v_1 = 5$
$u_2 = 3 \quad v_2 = 1$
$u_3 = 5 \quad v_3 = -3$

Checking the unallocated cells
$\Delta_{ij} = C_{ij} - (u_i + v_j)$

$\Delta_{13} = C_{13} - (u_1 + v_3) = 8 - (0 + -3) = +11$
$\Delta_{21} = C_{21} - (u_2 + v_1) = 9 - (3 + 5) = +1$
$\Delta_{31} = C_{31} - (u_3 + v_1) = 17 - (5 + 5) = +7$
$\Delta_{33} = C_{33} - (u_3 + v_3) = 7 - (5 + -3) = +5$

All values are +ve.

Initial feasible solution is the optimal and unique solution.