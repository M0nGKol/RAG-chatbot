<!-- page 1 -->
A1

# Assignment problem:

A special type of linear programming problem

Objective: To minimize cost/time of completing a job by a number of persons

2 types of assignment problems
* Balanced: No. of rows = No. of columns
* Unbalanced: No. of rows $\neq$ No. of columns

If the problem is unbalanced, use dummy row or dummy column and convert it to balanced assignment problem

Steps:
1. Row reduction, after identifying row minimum
2. Column reduction, after identifying column minimum (this is done to the row reduction table)
3. Zero allocation on rows - Identify cells with only single zero along rows. Select the zero (single zero) along row. Cancel the corresponding columns
4. Zero allocation on columns

---

<!-- page 2 -->
5. Make a note of all the zeros allocated.
6. Replace the allocated zeros with the original values from the given cells in the problem.
7. Add all the original values to give optimum allocation.

Eg: 1. There are four machines operated by 4 operators. Find the optimum assignment cost.

[FIGURE: A 4x4 matrix table labeled "Machines" (columns 1, 2, 3, 4) and "Operators" (rows A, B, C, D) representing cost values for different machine-operator pairings.]

| | 1 | 2 | 3 | 4 |
| :--- | :--- | :--- | :--- | :--- |
| A | 10 | 12 | 19 | 11 |
| B | 5 | 10 | 7 | 8 |
| C | 12 | 14 | 13 | 11 |
| D | 8 | 12 | 11 | 9 |

Let us observe the rows, this is a balanced problem.
The minimum value in row 1 is 10
row 2 is 5
row 3 is 11
row 4 is 8

The above table can be re-written as:

---

<!-- page 3 -->
A3

| | 1 | 2 | 3 | 4 | Row minimum |
|---|---|---|---|---|---|
| A | 10 | 12 | 19 | 11 | 10 |
| B | 5 | 10 | 7 | 8 | 5 |
| C | 12 | 14 | 13 | 11 | 11 |
| D | 8 | 12 | 11 | 9 | 8 |

Row reduction: All rows - Row minimum.
The new matrix will be as follows:

| | 1 | 2 | 3 | 4 |
|---|---|---|---|---|
| A | 0 | 2 | 9 | 1 |
| B | 0 | 5 | 2 | 3 |
| C | 1 | 3 | 2 | 0 |
| D | 0 | 4 | 3 | 1 |

[FIGURE: This is a table showing the result of the row reduction step, where each element has been subtracted by its corresponding row minimum. The table demonstrates the transformed cost matrix after the row reduction process is completed.]

Row reduction

Column reduction:
Identify minimum cells along the columns

| | 1 | 2 | 3 | 4 |
|---|---|---|---|---|
| A | 0 | 2 | 9 | 1 |
| B | 0 | 5 | 2 | 3 |
| C | 1 | 3 | 2 | 0 |
| D | 0 | 4 | 3 | 1 |
| Column minimum | 0 | 2 | 2 | 0 |

[FIGURE: This table identifies the minimum value present in each column of the previously row-reduced matrix. It acts as an intermediate step to perform the column reduction on the matrix.]

All columns - Column minimum.
The matrix after column reduction is given as follows:

---

<!-- page 4 -->
A4

### Column reduction

| | 1 | 2 | 3 | 4 |
| :--- | :--- | :--- | :--- | :--- |
| A | 0 | 0 | 7 | 1 |
| B | 0 | 3 | 0 | 3 |
| C | 1 | 1 | 0 | 0 |
| D | 0 | 2 | 1 | 1 |

Using the above table, zeroes are assigned to each row. There should not be two zeroes.

Identify rows with single zero (for allocation)

Above table reveals that D1 has a single zero.

Allocate D1
Column 1 containing cells gets cancelled

[FIGURE: This grid shows the assignment process for the Hungarian algorithm. Red boxes highlight allocated zeroes at A2, B3, C4, and D1, with red lines striking through the corresponding rows and columns to indicate they are no longer available for assignment.]

Consider rows,
Single zero is in A2 & B3
Allocate A2
Column 2 gets cancelled
Allocate B3
Column 3 gets cancelled

Single zero exists in column 4
Allocate C4, row C gets cancelled

The allocated cells D1, A2, B3 & C4 are replaced with the cost given in problem
The new cell is

---

<!-- page 5 -->
A5

| | 1 | 2 | 3 | 4 |
| :--- | :--- | :--- | :--- | :--- |
| **A** | | 12 | | |
| **B** | | | 7 | |
| **C** | | | | 11 |
| **D** | 8 | | | |

[FIGURE: This is an allocation table representing a 4x4 matrix. It demonstrates the optimal distribution of costs across rows and columns, with specific values assigned to cells (A,2)=12, (B,3)=7, (C,4)=11, and (D,1)=8.]

Optimal cost = $12 + 7 + 11 + 8$
$= 38$

(4 rows, 4 columns)
$\Downarrow$
4 allocations $\checkmark$

---

<!-- page 6 -->
A6

# Assignment problem

## Hungarian method:
This method is used when allocation of zeroes is not possible in any of the given rows.

## Eg: 2 Solve the assignment problem

| | | | |
|---|---|---|---|
| 1 | 4 | 6 | 3 |
| 9 | 7 | 10 | 9 |
| 4 | 5 | 11 | 7 |
| 8 | 7 | 8 | 5 |

[FIGURE: This table represents a 4x4 cost matrix for an assignment problem where values represent task costs across four agents.]

### Applying row reduction

| | | | | Min. Row |
|---|---|---|---|---|
| 1 | 4 | 6 | 3 | 1 |
| 9 | 7 | 10 | 9 | 7 |
| 4 | 5 | 11 | 7 | 4 |
| 8 | 7 | 8 | 5 | 5 |

[FIGURE: This table shows the initial matrix with an additional column on the right indicating the minimum value identified in each respective row.]

### Reduced row

| | | | |
|---|---|---|---|
| 0 | 3 | 5 | 2 |
| 2 | 0 | 3 | 2 |
| 0 | 1 | 7 | 3 |
| 3 | 2 | 3 | 0 |

[FIGURE: This table shows the resulting matrix after subtracting the minimum row values from their respective rows.]

### Applying column reduction

### Reduced column

| | | | |
|---|---|---|---|
| 0 | 3 | 2 | 2 |
| 2 | 0 | 0 | 2 |
| 0 | 1 | 4 | 3 |
| 3 | 2 | 0 | 0 |

[FIGURE: This table shows the matrix after performing column reduction operations on the previous row-reduced matrix to create additional zeroes.]

Applying zero allocation, to solve the above matrix,

---

<!-- page 7 -->
A7

| | | | |
| :---: | :---: | :---: | :---: |
| 0 | 3 | 2 | 2 |
| 2 | 0 | 0 | 2 |
| 0 | 1 | 4 | 3 |
| 3 | 2 | 0 | 0 |

[FIGURE: A 4x4 matrix containing values with some cells highlighted. Lines are drawn horizontally and vertically through specific rows and columns to cover the zeros, demonstrating that only 3 lines are needed to cover the zeros, which is less than the matrix dimension of 4.]

We are able to allocate only 3 rows instead of 4. 1 row/column remains unallocated.

Therefore, inorder to allocate 4 cells, Hungarian method is applied.

Steps in Hungarian method

1. Connect all zeroes using straight lines.
2. Choose the minimum path connecting the lines linking all zeroes (horizontal & vertical lines).
3. Three types of cells are observed:
    * cells lying on the intersecting lines
    * cells lying between intersecting lines
    * cells not lying along the intersecting lines
4. From the cells not lying along the intersecting lines, select the cell with least value.
5. Add this least value cell to the intersections.
6. Subtract this least value cell from the cells not lying at the connecting lines.

---

<!-- page 8 -->
A8

7. Do not interfere with the cells lying between intersecting lines.
8. Prepare a new matrix using the above method and assign values.

[FIGURE: Two 4x4 matrices are shown with vertical and horizontal red lines drawn through certain rows and columns to cross out zeros. The left matrix has 4 lines and is marked with an X, while the right matrix has 3 lines and is marked with a check, indicating the "least connecting lines = 3".]

[FIGURE: A workflow diagram indicating that from the "least connecting lines = 3" step, the user should look at the "cells in the unconnected lines" to find the "least value = 1". This value is then used to adjust the matrix: add 1 to intersection cells, subtract 1 from unconnected cells, and keep other cells as they are.]

| | | | |
|---|---|---|---|
| 0 | 2 | 1 | 1 |
| 3 | 0 | 0 | 1 |
| 0 | 0 | 3 | 2 |
| 4 | 2 | 0 | 0 |

---

<!-- page 9 -->
A9

| | | | |
|---|---|---|---|
| 0 | 2 | 1 | 1 |
| 3 | 0 | 0 | 1 |
| 0 | 0 | 3 | 2 |
| 4 | 2 | 0 | 0 |

4 rows, 4 columns, 4 occupied cells.

[FIGURE: A 4x4 grid containing numerical values. Certain cells containing zeroes are highlighted with red squares to indicate their selection for the optimal assignment.]

Replacing the selected zeroes with the original values given in the problem:

| | | | |
|---|---|---|---|
| 1 | | | |
| | | 10 | |
| | 5 | | |
| | | | 5 |

[FIGURE: A 4x4 grid where most cells are empty. Specific cells are filled with the original values 1, 10, 5, and 5 corresponding to the locations of the zeroes selected in the previous step.]

Optimal Cost
$= 1 + 5 + 10 + 5$
$= 21$