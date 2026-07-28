<!-- page 1 -->
# Operations Research
– Linear Programming –

16th June 2026
dr. ing. ir. Satish Kumar Damodar MBA, Dip.TD, IBP, CSSC

---

<!-- page 2 -->
Linear programming model
Used for optimum allocation of scarce or limited resources to competing products
Used for solving broad range of problems arising in business, government, industry, hospitals, production, finance,
marketing, research and development and personnel management for decision making.
Useful in allocation of available resources that are limited.
Determines optimal product mix (a combination of products, which gives maximum profit), transportation schedules,
assignment problem and many more.

---

<!-- page 3 -->
Product mix problem (Example)
A company manufactures two products X and Y, which require, the following resources.
The resources are the capacities machine M1, M2, and M3.
The available capacities are 50, 25, and 15 hours respectively in the planning period.
Product X requires 1 hour of machine M2 and 1 hour of machine M3.
Product Y requires 2 hours of machine M1, 2 hours of machine M2 and 1 hour of machine M3.
The profit contribution of products X and Y are $5 and $4 respectively.

---

<!-- page 4 -->
Product mix problem (Example)
Products X and Y are competing variables
X and Y should not exceed available capacities
Both companies can stop the production of both x and y or can manufacture any amount of x and y 
It cannot manufacture negative quantities of x and y

---

<!-- page 5 -->
Properties of linear programming model
(a) Linear relationship among variables and constraints.
b) The model must have an objective function.
(c) The model must have structural constraints.
(d) The model must have non-negativity constraint.
Linear relationship = Consistent, proportional relationship that can be graphically represented by a straight line

---

<!-- page 6 -->
Basic assumptions of Linear Programming 
1. The decision is certain (i.e., deterministic conditions) regarding all aspects of the situation;
i.e., availability of resources, profit contribution of the products, technology, courses of action and their 
consequences etc.
2. The relationship between variables in the problem and the resources available 
i.e., constraints of the problem exhibits linearity.
Here the term linearity implies proportionality and additivity.
This assumption simplifies the model.
3. The technology used is fixed.
Fixed technology refers to the fact that the production requirements are fixed during the planning period 
and will not change in the period.

---

<!-- page 7 -->
4. It is assumed that the profit contribution of a product remains constant, irrespective of level of production
and sales.
5.  The decision variables are continuous.
The companies manufacture products in fractional units.
For example, company manufactures 2.5 vehicles, 3.2 barrels of oil etc. This
is referred to as the assumption of divisibility.
6. It is assumed that only one decision is required during the planning period.
This condition reveals that the linear programming model is a static model, which implies that linear 
programming problem is a single stage decision problem.
(Note: Dynamic Programming problem is a multistage decision problem).
7.  All variables are restricted to non-negative values (i.e., their numerical value will be ≥0).
Basic assumptions of Linear Programming

---

<!-- page 8 -->
Terms used
Linear programming is a method of obtaining an optimal solution or program (say, product mix in a production 
problem), when resources are limited resources and there are competing candidates to consume the limited resources 
in certain proportion.
The term linear implies the condition of proportionality and additivity.
Program is referred as a course of action covering a specified period of time, say planning period.
The manager has to find out the best course of action in the interest of the organization.
This best course of action is termed as optimal course of action or optimal solution to the problem.
A program is optimal, when it maximizes or minimizes some measure or criterion of effectiveness, such as profit, 
sales or costs.

---

<!-- page 9 -->
Terms used
Programing refers to a systematic procedure by which a particular program or plan of action is designed.
Programming consists of a series of instructions and computational rules for solving a problem that can be
worked out manually or can fed into the computer.
In solving linear programing problem, a systematic method known as Simplex method is used.
The activity here refers to number of products or any items that utilization available resources in a certain required 
proportion.
The available resources may be of any nature, such as money, land, machine hours, and man-hours or materials. 
These are limited in availability and are desired by the activities / products for consumption.

---

<!-- page 10 -->
Mathematical expression of a problem
where aij, bm    &  cn
are constants and
xj is decision variable and should be positive
≥is generally used for minimization
≤is used for maximization
values on Right Hand Side

---

<!-- page 11 -->
Steps in formulating Linear Programing problem
1. Identify the unknown decision variables to be determined and assign 
symbols to them.
2. Identify all restrictions or constraints in the problem and express them as a linear
equation or inequalities of decision variables.
3. Identify objective and represent it as a linear function of decision variables

---

<!-- page 12 -->
Maximization problem (Example 1)
A retail store stocks two types of shirts A and B in a storage box.
During a week the store can sell a maximum of 400 shirts of type A; and a maximum of 300 shirts of type B. 
The storage capacity, however, is limited to a maximum of 600 of both types combined.
Type A shirt fetches a profit of $ 2 per unit and type B a profit of $ 5 per unit.
How many of each type the store should stock per week to maximize the total profit? 
Formulate a mathematical model of the problem.

---

<!-- page 13 -->
Solution (Example 1)
Shirts A and B are problem variables.
Let the store stock ‘a’ units of A and ‘b’ units of B.
As the profit contribution of A and B are $2 and $5 respectively,
The objective function is: Maximize Z = 2a + 5b subjected to condition (s.t.)
Structural constraints are, stores can sell 400 units of shirt A; and 300 units of shirt B and storage capacity of both
put together is 600 units.
The model will be:

---

<!-- page 14 -->
Maximization problem (Example 2)
A ship has three cargo holds, forward, aft and center.
The capacity limits of the ship are:
The following cargoes are offered, the ship owners may accept all or 
any part of each commodity:
Weight
(Tons)
Volume
(Cubic meter)
Forward
2000
100,000
Centre
3000
135,000
Aft
1500
30,000
Total
6500
265,000
In order to preserve the trim of the ship the weight in each hold must be proportional to the capacity in tons.
How should the cargo be distributed so as to maximize profit?
Formulate this as linear programming problem

---

<!-- page 15 -->
A = 6000 tons 
Volume/ton = 60m3
1 ton has a volume of 60m3 
1 ton = 60 m3
1/60 ton = 1 m3
For 6000 tons, volume =1/60 * 6000 m3= 100 m3
B = 4000 tons
Volume/ton = 50m3
1 ton has a volume of 50 m3
1 ton = 50m3
1/50 ton = 1m3
For 4000 tons, volume = 1/50 * 4000 m3 = 80 m3
C = 2000 tons
Volume/ton = 25m3
1 ton has a volume of 25 m3
1 ton = 25m3
1/25 ton = 1m3
For 2000 tons, volume = 1/25 * 2000 m3 = 80 m3
Standardizing 
tonnage into volume
among the 3 commodities A, B & C

---

<!-- page 16 -->
Commodities are A, B & C with respective units a, b & c 
s.t.
The objective is to maximize profits
Then, Objective function is: Maximize Z = 60a + 80b + 50c
Constraints: Weight (Tonnage) and Volume (Cubic meter)
Weight constraint: 6000a + 4000b +2000c ≤6500
The tonnage of commodity is 6000 and each ton occupies 60 cubic meters, 
hence there are 100 cubic meters capacity is available for A
Volume constraint: 100a +80b + 80c ≤2,65,000
Maximise Z = 60a+80b+50c s.t. 
6000a + 4000b + 2000c ≤6,500
100a + 80b + 80c ≤2,65,000 and
a, b, c ≥0

---

<!-- page 17 -->
Minimization problem (Example 1)
A doctor examines a patient and find out that and he is deficient in two vitamins- vitamin A and vitamin D. 
The doctor prescribes tonic X and tonic Y, containing vitamin A, and vitamin D in certain proportion.
Also advises the patient to consume at least 40 units of vitamin A and 50 units of vitamin D everyday.
The cost of tonics X and Y and the proportion of vitamin A and D that present in X and Y are given in the table below.
Formulate linear program to minimize the cost of tonics

---

<!-- page 18 -->
Solution
Let patient purchase x units of X and y units of Y.
Objective function: Minimize Z = 5x + 3y
Inequality for vitamin A is 2x + 4y ≥ 40
(at least 40 units of A)
(Here at least word indicates that the patient can consume more than 40 units but not less than 40 units of vitamin A 
daily).
Similarly the inequality for vitamin D is 3x + 2y ≥50 (At least 50 units of B)
For non-negativity constraint the patient cannot consume negative units. 
Hence both x and y must be ≥0
Model:
Minimize Z = 5x + 3y s.t. 
2x + 4y ≥40
3x + 2y ≥50 and 
Both x and y are ≥0.

---

<!-- page 19 -->
Methods for solving linear programing problem
The Graphical Method:
When there are two decision variables in the problem.
The graphical method solves only two variable problems.
1. The Systematic Trial and Error method:
In this method, values are given to variables until optimal solution is achieved. 
This method is time consuming and laborious, and not discussed.
2. The Vector method:
In this method each decision variable is considered as a vector and principles of vector algebra is used to obtain 
optimal solution.
This method is also time consuming, and not discussed.

---

<!-- page 20 -->
Methods for solving linear programing problem
3. The Simplex method:
When there are more than two decision variables, simplex method is used to solve the
problem. It is systematic program.
Problem with two variables is solved using both graphical and simplex method, to understand 
relationship between the two variables.

---

<!-- page 21 -->
Graphical method
Inequalities (structural constraints) are equations and cannot be represented graphically
Only two variable problems are considered, because straight lines are represented in two-dimensional plane
(X- axis and Y-axis).
Nonnegativity constraints (decision variables) must have positive values always, and the solution to the problem 
lies in FIRST QUADRANT of the graph.
Some times the value of variables may fall in other quadrants.
In such cases, the line joining the values of the variables must be extended to the first quadrant.

---

<!-- page 22 -->
Graphical problem 1
A company manufactures two products, X and Y by using three machines A, B, and C. Machine A has 4 hours of 
capacity available during the coming week. The available capacity of machines B and C during the coming week is 24
hours and 35 hours respectively. One unit of product X requires one hour of Machine A, 3 hours of machine B and
10 hours of machine C. One unit of product Y requires 1 hour, 8 hour and 7 hours of machine A, B and C
respectively. When one unit of X is sold in the market, it yields a profit of $ 5 per unit and that of Y is $ 7 per unit. 
Solve the problem by using graphical method to find the optimal product mix

---

<!-- page 23 -->
Solution
Let the company manufactures x units of X and y units of Y.
The L.P. model is:
Maximize Z = 5x + 7y s.t. (subject to) 
1x + 1y ≤4
3x + 8y ≤24
10x + 7y ≤35 and 
Both x and y are ≥0.
As we cannot draw graph for inequalities, consider them as equations. 
Let us take machine A. and find the boundary conditions.
If x = 0, machine A can manufacture 4/1 = 4 units of y.
Similarly, if y = 0, machine A can manufacture 4/1 = 4 units of x.
P0Q represents capacity of machine A
Machine A
1x + 1 y =4

---

<!-- page 24 -->
Solution
Consider machine B
When x = 0 , y = 24/8 = 3 and when y = 0 x = 24/3 = 8
R0S represents capacity of machine B
Consider machine C
When x = 0, y = 35/10 = 3.5 and when y = 0, x = 35 / 7 = 5
T0U represents capacity of machine C
Machine B
Machine C
10x + 7y =35
3x + 8y =24

---

<!-- page 25 -->
# Solution

[FIGURE: The left graph illustrates the production constraint boundary for two machines, A and B, showing lines intersecting at point M. The right graph depicts the expanded production constraint boundary when machine C is added, resulting in a new, outer boundary profile formed by segments of individual machine constraints.]

* Machines A & B
* Machines A, B & C combined

---

<!-- page 26 -->
Solution
The combined graphs of machines A and B meets at M
The three machines A, B and C represents a polygon R0UVW
For maximization problem, we select coordinates that gives maximum
value For minimization problem, we select coordinates that gives
minimum value
The coordinates are
R = (0, 3), O = (0, 0), U = (3.5, 0), V = (2.5, 1.5) and W = (1.6, 2.4).
Substituting these values in objective function 5x +7y we get 
Z(0, 3) = 5 × 0 + 7 × 3 = $ 21.00, at point R
Z (0, 0) = 5 × 0 + 7 × 0 = $ 00.00, at point O
Z(3.5, 0) = 5 × 3.5 + 7 × 0 = $ 17.5 at point U
Z (2.5, 1.5) = 5 × 2.5 + 7 × 1.5 = $ 23.00 at point V
Z (1.6, 2.4) = 5 × 1.6 + 7 × 2.4 = $ 24.80 at point W is the optimal solution (Z Maximization)
Machines A, B & C combined

---

<!-- page 27 -->
Graphical problem 2
A company produces two types of items P and Q that require gold and silver.
Each unit of type P requires 4g silver and 1g gold while that of type Q requires 1g silver and 3g gold. 
The company produces 8g silver and 9g gold.
If each unit of type P brings a profit of $44 and that of type Q brings a profit of $55, determine the number of units of 
each type that the company should produce to maximize the profit.
What is the maximum profit?

---

<!-- page 28 -->
Solution
Let x be the quantity of type P to be produced and y be the quantity of type Q to be produced.
Maximize Z = 44x + 55y subject to the constraints: 
4x + y ≤8
x + 3y ≤9
and x ≥0, y ≥0.

---

<!-- page 29 -->
Solution
Plotting graphs for equations 4x + y = 8, 
For the line 4x + y = 8
x + 3y = 9 , x = 0 , y = 0
For the line x + 3y = 9
x
0
2
y
8
0
x
0
9
y
3
0

---

<!-- page 30 -->
Solution
Maximum Z = 44x + 55y
From the graph, the points are 
Z (0, 0) = 44 (0) + 55 (0) = 0
Z (2, 0) = 44 (2) + 55 (0) = 88
Z (15/11, 28/11) = 44 (15/11) + 55 (28/11) = 200 
Z (0, 3) = 44 (0) + 55 (3) = 165
The value of Z is maximum at C (15/11 , 28/11) and 
optimum solution is Max. Z = 200 when x = 15/11 and
y = 28/11
The value of x and y at point C on graph is 
obtained by solving both equations
4x + y = 8 
x + 3y = 9
0 + 11y = 28
y = 28/11
Substituting the value of y in the equation, 
we get x = 15/11
C = (15/11, 28/11)

---

<!-- page 31 -->
Assignment 1 
1. Maximize Z = 6X + 3Y subjects to the constraints 2X + 5Y ≤ 120, 4X + 2Y ≤80, X ≥0 , Y ≥0.
2. Maximize Z = 3x1 + 2x2 subjects to the constraints x1 –x2 ≤ 1, x1+x2≥3, x1≥ 0 , x2 ≥0
3. Maximize Z = x1 + x2 subjects to the constraints x1+x2 ≤1, -3x1+x2≥3, x1≥ 0 , x2 ≥0
4. A company manufactures two products X and Y, each of which requires three types of processing. 
The length of time for processing each unit and the profit per unit are given in the following table:
How many units of each product should the company manufacture per day in order to maximize profit?

---

<!-- page 32 -->
Expressing LPP in Canonical form
(a) Objective function should be of maximization form.
If it is given in minimization form, it should be converted into maximization form.
(b) All the constraints should be of “ ≤ ” type, except for non- negative restrictions. 
Inequality of “ ≥” type, if any, should be changed to an inequality of the “ ≤” type    
(b) All variables should be non-negative.
If a given variable is unrestricted in sign (i.e., positive, negative or zero), it can be written as a difference
of two non-negative variables.
Suppose x is unrestricted in sign, then x can be written as x= 𝑥′ - 𝑥′′ where 𝑥′ ≥0, 𝑥′′ ≥0.

---

<!-- page 33 -->
Expressing LPP in Canonical form
Minimize Z = 2𝑥1 + 𝑥2 + 4𝑥3 Subject to constraints:
-2𝑥1 + 4𝑥2 ≤4
𝑥1 + 2𝑥2 + 𝑥3 ≥5 
2𝑥1 + 3𝑥3 ≤2
𝑥1, 𝑥2 ≥ 0 and 𝑥3 is unrestricted in sign (x3 > 0, x3 < 0)
Here, the objective function is of the minimization form. 
We rewrite the maximization form as:
Minimize Z = 2𝑥+ 𝑥+ 4𝑥
1
2
3
We have to maximize -Z = -2𝑥1 - 𝑥2 - 4𝑥3. 
The problem becomes,
1
2
3
Maximize 𝑍′= -2𝑥- 𝑥- 4𝑥. where 𝑍′ = -Z
The second constraints is of the type “ ≥”.
Convert it into type “ ≤”, we multiply the inequality by
-1 and write - 𝑥1 - 2𝑥2 - 𝑥3 ≤-5
Other constraints are already in the desired form. But
𝑥3 is unrestricted in sign.
So, we write 𝑥3 = 𝑥3′ −𝑥3′′ , 
where 𝑥3′ ≥0, 𝑥3′′ ≥0
The canonical form of the given problem is
Maximize 𝑍′= -2𝑥1 - 𝑥2 – 4(𝑥3′ −𝑥3′′), where 𝑍′ = -Z 
Subject to the constraints:
-2𝑥1 + 4𝑥2 ≤4
1
2
3
3
-𝑥- 2𝑥– (𝑥′ −𝑥′′) ≤-5
2𝑥1 + 3(𝑥3′ −𝑥3′′) ≤2
𝑥1 ≥0, 𝑥2 ≥0, 𝑥3′ ≥0, 𝑥3′′ ≥0

---

<!-- page 34 -->
Expressing LPP in Standard form
1) The objective function should be in the maximization form.
2) The right-side element of each constraint should be non- negative. 
If it is negative, we multiply the inequality by -1.
3) All constraints should be expressed in the form of equations, except for the non- negative restrictions
4) Augmenting a slack or surplus variables to the function and balance it by adding the slack variables to the
objective function

---

<!-- page 35 -->
Expressing LPP in Standard form
A slack variable is added to the left side of each of 
the first and third inequalities.
The second inequality is of the type “more than or 
equal to (≥) ”.
So, a surplus variable is to be subtracted from the left 
side of this inequality.
Thus, a standard form of the given LPP is
Maximize Z’ = -2𝑥1 - 𝑥2 - 4𝑥3 + 0S1 + 0S2 + 0S3 , 
where Z’ = -Z subject to constraints:
-2𝑥1 + 4𝑥2 + 𝑠1 = 4
-𝑥1 - 2𝑥2 - 𝑥3 - 𝑠2 = -5 
2𝑥1 + 3𝑥3 + 𝑠3 = -2
𝑥1 ≥0 , 𝑥2 ≥0 , 𝑥3 ≥0 , 𝑠1 ≥0 , 𝑠2 ≥0 , 𝑠3 ≥0
Minimize Z = 2𝑥1 + 𝑥2 + 4𝑥3 Subject to the constraints:
-2𝑥1 + 4𝑥2 ≤4
𝑥1 + 2𝑥2 + 𝑥3 ≥5 
2𝑥1 + 3𝑥3 ≤-2
𝑥1 ≥0, 𝑥2 ≥0 and 𝑥3 ≥0
Here, the objective function is of the minimization form. 
We rewrite it in the maximization form as follows: 
Minimize Z = 2𝑥1 + 𝑥2 + 4𝑥3
We have to maximize -Z = -2𝑥1 - 𝑥2 - 4𝑥3. 
The problem becomes,
Maximize 𝑍′= -2𝑥1 - 𝑥2 - 4𝑥3. where 𝑍′ = -Z 
The inequalities are to be converted to equations.
The first and third inequalities are of the type “less than 
or equal to (≤)”.

---

<!-- page 36 -->
# Canonical form & Standard form

| Feature | Canonical Form | Standard Form |
| :--- | :--- | :--- |
| Objective Function | Usually Maximization | Can be Maximization or Minimization |
| Constraints | All are Inequalities (typically $\leq$) | All are strict Equalities ($=$) |
| Variables | All decision variables must be $\geq 0$ | All variables (including slack/surplus) must be $\geq 0$ |
| Right-Hand Side ($b$) | Can be positive or negative | Must be non-negative ($b \geq 0$) |
| Primary Use Case | Duality theory and economic interpretation | Inputting into the Simplex Algorithm |

[FIGURE: This table compares the properties of Canonical and Standard forms in linear programming. It highlights differences in objective functions, constraint types, variable requirements, sign of the right-hand side, and their respective primary applications.]

---

<!-- page 37 -->
Problem
A machine tool company conducts a job-training at a ratio of one for every ten trainees.
The training lasts for one month.
From past experience it has been found that out of 10 trainees hired, only seven complete the program successfully. 
(The unsuccessful trainees are released). Trained machinists are also needed for machining.
The company's requirement for the next three months is as follows: January: 100 machinists, February: 150 
machinists and March: 200 machinists. In addition, the company requires 250 trained machinists by April.
There are 130 trained machinists available at the beginning of the year. Pay roll cost per month is: Each
trainee $ 400 per month.
Each trained machinist (machining or teaching): $ 700 p.m.
Trained machinist who is idle: $ 500 p.m. (Labour union forbids ousting trained machinists). Build linear program
for produce the minimum cost hiring and training schedule and meet the company’s requirement.

---

<!-- page 38 -->
Solution
There are three options for trained machinists as per the data given.
(i) A trained machinist can work on machine,
(ii) he can teach or
(iii) he can remain idle.
It is given that the number of trained machinists available for machining is fixed.
The unknown decision variables are the number of machinists goes for teaching and those who remain idle for each 
month.
Let,
‘a’ be the trained machinists teaching in the month of January. 
‘b’ be the trained machinists idle in the month of January.
‘c’ be the trained machinists for teaching in the month of February. 
‘d’ be the trained machinists remain idle in February.
‘e’ be the trained machinists for teaching in March.
‘f ’ be the trained machinists remain idle in the month of March.

---

<!-- page 39 -->
Solution
The constraints can be formulated by the rule that the number of machinists employed (machining + teaching + idle)
= Number of trained machinists available at the beginning of the month.
For January 100 + 1a + 1b ≥130
For February, 150 + 1c + 1d = 130 + 7a
(Here 7a indicates that the number of machinist trained is 10 × a = 10a. 
But only 7 of them are successfully completed the training i.e. 7a).
For the month of March, 200 + 1e + 1f ≥130 + 7a +7c
The requirement of trained machinists in the month of April is 250, the constraints for this will be 
130 + 7a + 7c + 7e ≥250 and
The objective function is
Minimize Z = 400 (10a + 10c + 10e) + 700 (1a +1c + 1e) + 500 (1b + 1d +1f) and 
the nonnegativity constraint is a, b, c, d, e, f ≥0.

---

<!-- page 40 -->
Solution
The model is:
Minimize Z = 400 (10a + 10c + 10e) + 700 (1a +1c + 1e) + 500 (1b + 1d + 1f) s.t.
100 + 1a + 1b ≥130
150 + 1c + 1d ≥130 + 7a
200 + 1e + 1f ≥130 + 7a + 7c
130 + 7a + 7c + 7e ≥250 and 
a, b, c, d, e, f all ≥0.

---

<!-- page 41 -->
# Thank You!

www.kit.edu.kh