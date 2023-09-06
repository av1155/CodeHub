/*
The goal of this is to write a program, LinEq, to solve a system of linear equations with two unknowns. Suppose we have two linear equations
with two unknowns, x and y, as follows:

ax+by = p
cx+dy = q

Let det denote the determinant ad − bc. The solutions for these equations can be obtained using
Cramer’s Rule as follows:

x = (d∗p−b∗q)/det
y = (a∗q−c∗p)/det
 */

import java.util.Scanner;

public class LinEq {
    public static void main(String[] args) {

        Scanner keyboard;
        keyboard = new Scanner(System.in);

        double a, b, p;
        double c, d, q;

        System.out.println("This program solves systems of linear equations.");
        System.out.println("ax + by = p, cx + dy = q");

        System.out.print("Enter a, b, and p: ");
        a = keyboard.nextDouble();
        b = keyboard.nextDouble();
        p = keyboard.nextDouble();

        System.out.print("Enter c, d, and q: ");
        c = keyboard.nextDouble();
        d = keyboard.nextDouble();
        q = keyboard.nextDouble();

        System.out.println("The equations are:");
        System.out.println(a + " x" + " + " + b + " y" + " = " + p);
        System.out.println("and");
        System.out.println(c + " x" + " + " + d + " y" + " = " + q);

        double det = (a*d - b*c);

        System.out.print("The solution is ");
        System.out.println("(" + ((d * p - b * q)/det) + ", " + ((a * q - c * p)/det) + ")");
    }
}
