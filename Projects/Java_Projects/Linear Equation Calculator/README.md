# Linear Equation Calculator

## Overview

The LinEq program is designed to solve a system of linear equations with two unknowns (x and y) using Cramer's Rule. It allows users to input the coefficients of two linear equations and calculates the solutions for x and y.

## How it Works

Suppose we have the following system of linear equations:

1. ax + by = p
2. cx + dy = q

The program takes input for coefficients a, b, p, c, d, and q from the user and calculates the solutions using the following formulas:

- x = (d * p - b * q) / det
- y = (a * q - c * p) / det

Where `det` is the determinant of the coefficient matrix (ad - bc).

## Usage

1. Run the program.
2. Enter the coefficients for the first equation (a, b, and p) when prompted.
3. Enter the coefficients for the second equation (c, d, and q) when prompted.
4. The program will display the equations and the calculated solution for x and y.

## Example

```plaintext
This program solves systems of linear equations.
ax + by = p, cx + dy = q
Enter a, b, and p: 2 4 5
Enter c, d, and q: 3 3 2
The equations are:
2.0 x + 4.0 y = 5.0
and
3.0 x + 3.0 y = 2.0
The solution is (-1.1666666666666667, 1.8333333333333333)
```

## Author

Andrea. A. Venti Fuentes