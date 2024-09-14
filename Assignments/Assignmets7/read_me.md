# NUMERICAL ANALYSIS

## Definition: 
Numerical analysis is a branch of mathematics and computer science that focuses on developing and analyzing algorithms for obtaining numerical solutions to mathematical problems. These problems can range from simple equations to complex systems that may not have analytical (exact) solutions.

## The key goals of numerical analysis include:

1. **Approximation:**
   - Finding approximate solutions to problems that cannot be solved exactly.

2. **Error Analysis:**
   - Understanding and minimizing the errors involved in numerical computations.
	   -    **Round-off Error**: Occurs because computers represent numbers with a finite number of digits. For example, the irrational number π is approximated in computers, which leads to small inaccuracies in calculations.
		-  **Truncation Error**: Arises when an infinite process is approximated by a finite one. For example, when using numerical methods to approximate integrals or derivatives, the method stops after a certain number of steps.
		-   **Approximation Error**: Introduced when an exact mathematical expression is replaced by an approximate one, such as using polynomial approximations for complex functions.

3. **Efficiency**:
	- Creating algorithms that are computationally efficient, especially for large-scale problems.

## Methods To Solve Numerical Problems
- Interpolation
- Numerical Integration
1. **Interpolation:**
Interpolation is a numerical method used to estimate unknown values that fall within the range of a discrete set of known data points. Given a set of data points (x1,y1),(x2,y2),…,(xn,yn)(x_1, y_1), (x_2, y_2), \ldots, (x_n, y_n)(x1​,y1​),(x2​,y2​),…,(xn​,yn​), interpolation involves constructing a function that passes through these points, which can then be used to estimate the value of the function at any point within the range of the data.

![Graph](https://www.researchgate.net/profile/Sebastian-Mair-2/publication/344878125/figure/fig1/AS:950726079545344@1603682169265/Illustration-of-different-interpolation-paths-of-points-from-a-high-dimensional-Gaussian.ppm)



**Example**: Consider the table

| Year     | Population |
| -------- | --------   |
| 1940     | 1,32,165   |
| 1950     | 1,51,165   |
| 1960     | 1,79,302   |
| 1970     | 2,03,302   |
| 1980     | 2,26,542   |

**Q.** Whether this data can be used to provide a reasonable estimate of the population say in 1955, 1975.

**_Ans_**: Yes, prediction of this type can be obtained by using function that fits the given data.


### Reference:
[ChatGPT](https://chatgpt.com/c/66e5b628-ec30-8003-948a-a5ec4870c124)

[WIKIPEDIA](https://en.wikipedia.org/wiki/Numerical_analysis)