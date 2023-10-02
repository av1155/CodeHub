# VolumeComparison Java Program

The **VolumeComparison** Java program is a tool for comparing the areas of different 3D shapes. It allows users to input their desired shapes (cylinder, square pyramid, or rectilinear) and computes the respective areas for comparison.

## How to Run

Compile the Java program using a Java compiler and run the compiled program.

```bash
javac VolumeComparison.java
java VolumeComparison
```

Follow the on-screen instructions to select the shapes and input the required parameters for area computation.

## Code Overview

The program is divided into several methods, each responsible for a specific area calculation:

- `cylinderArea`: Computes the area of a cylinder based on the radius and length.
- `squarePyramidArea`: Computes the area of a square pyramid based on the side and length.
- `rectlinearArea`: Computes the area of a rectilinear shape based on three side lengths.
- `getDouble`: Handles user input for a double value, checking for validity and providing a default value if needed.
- `getInt`: Handles user input for an integer value, checking for validity and providing a default value if needed.
- `getArea`: Takes user input for the shape choice and calls the appropriate area calculation method.

The main method orchestrates the user interaction, guiding the user to input their desired shapes and parameters for area computation. It then compares the computed areas and displays the results.

## Example Usage

Here's an example of running the program and comparing areas for a cylinder and a square pyramid:

```bash
---- Comparing two 3d shapes ----
----------------
Shape 1. Which shape is it?
1. cylinder, 2. square pyramid, 3. rectilinear: 1
Enter radius and length: 5 10
The area is 471.238898
----------------
Shape 2. Which shape is it?
1. cylinder, 2. square pyramid, 3. rectilinear: 2
Enter side and length: 7 12
The area is 350.300304
No.1 has a bigger area.
```

## Author

Andrea Arturo Venti Fuentes
