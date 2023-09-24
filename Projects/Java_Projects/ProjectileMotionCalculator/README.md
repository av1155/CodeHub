# Projectile Motion Calculator

This Java program calculates various parameters related to projectile motion, considering Earth's gravity and optionally the Moon's gravity.

## Features

- Calculates the trajectory and other details of a projectile based on user inputs.
- Provides results for projectile motion on both Earth and the Moon.

## Usage

1. Compile the Java program using a Java compiler.

2. Run the compiled program.

3. Follow the prompts to input the angle, speed, and height of the projectile.

4. The program will calculate and display the results for projectile motion on both Earth and the Moon.

## Code Structure

The code is organized as follows:

- **`ProjectileMotionCalculator`**: Main class containing the entry point for the program and handling user input.
- **`compute`**: Method to calculate various parameters related to projectile motion.
- **`message`**: Method to display messages.
- **`myPrint`**: Method to display formatted output.

## Constants

- `earthG`: Earth's gravity constant (g = 9.8 m/s^2).
- `moonG`: Moon's gravity constant (g = 1.620 m/s^2).

## How it Works

1. The user provides the angle, speed, and height of the projectile.

2. The program calculates the corrected values and converts the angle to radians.

3. It then computes the vertical and horizontal speeds.

4. The program calculates and displays the trajectory and other details of the projectile for both Earth and the Moon.

## Formulas

The calculations are based on the following formulas related to projectile motion:

## Formulas related to projectile motion:

- Upward time (t0): t0 = v / g
- Upward distance (h0): h0 = g * (v / g)^2 - 0.5 * g * t0^2
- Downward distance (h1): h1 = h0 + h
- Downward time (t1): t1 = sqrt((2 * h1) / g)
- Total time (t2): t2 = v / g + t1
- Horizontal distance (r): r = horizontalSpeed * (v / g + t1)
