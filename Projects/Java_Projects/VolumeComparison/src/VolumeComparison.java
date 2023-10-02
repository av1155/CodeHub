import java.util.Scanner;

public class VolumeComparison {
    public static void main(String[] args) {
        Scanner keyboard = new Scanner(System.in); // Initiate and declare scanner

        // The following section outputs a basic prompt, and then the variables `area_of_shape_1` and `area_of_shape_2` store the result from getArea().
        // getArea() is made of a switch statement with the three possible options listed in the prompt. The switch statement then gets the area.
        System.out.println("---- Comparing two 3d shapes ----");
        System.out.print("----------------\nShape 1. Which shape is it? \n1. cylinder, 2. square pyramid, 3. rectlinear: ");
        double area_of_shape_1 = getArea(keyboard, getInt(keyboard));

        System.out.print("Shape 2. Which shape is it? \n1. cylinder, 2. square pyramid, 3. rectlinear: ");
        double area_of_shape_2 = getArea(keyboard, getInt(keyboard));

        // Variables `area_of_shape_1` and `area_of_shape_2` are compared for equality or to determine which one is larger or smaller by:
        // - Comparing the returned values from the previous calls to getArea() to each other.
        // - If the returned value is 0.0 for both variables the program will output "Null Result." to account for failed input from the user.
        if (area_of_shape_1 > area_of_shape_2)
        {
            System.out.println("No.1 has a bigger area.");
        }

        else if (area_of_shape_2 > area_of_shape_1)
        {
            System.out.println("No.2 has a bigger area.");
        }

        else if (area_of_shape_1 == 0.0 && area_of_shape_2 == 0.0)
        {
            System.out.println("Null Result.");
        }

        else
        {
            System.out.println("The areas are identical.");
        }
    }

    // The following method is an input handler that uses a keyboard parameter to let the user input a double number, it is checked and then returned.
    public static double getDouble(Scanner keyboard) {
        double defaultDouble = 10.0; // Sets the default input to 10.0 for later use.
        double inputDouble;

        // If statement that determines if the user typed a double number, then it determines if the number is less than 0.
        // If the number is less than 0 it changes whatever the user typed to 10.0 (defaultDouble).
        // If the user did not type a double number, the program first consumes whatever the user wrote, and then it assigns the variable to the default.
        // The final and corrected double variable is returned for use in the rest of the program.
        if (keyboard.hasNextDouble())
        {
            inputDouble = keyboard.nextDouble();
            if (inputDouble < 0)
            {
                inputDouble = defaultDouble;
            }
        }

        else
        {
            keyboard.nextLine();
            inputDouble = defaultDouble;
        }

        return inputDouble;
    }

    // The following method is an input handler that uses a keyboard parameter to let the user input an integer number, it is checked and then returned.
    public static int getInt(Scanner keyboard) {
        int defaultInteger = 1;
        int inputInteger;

        // If statement that determines if the user typed an integer number, then it determines if the number is less than 0.
        // If the number is less than 0 it changes whatever the user typed to 1 (defaultInteger).
        // If the user did not type an int number, the program first consumes whatever the user wrote, and then it assigns the variable to the default.
        // The final and corrected integer variable is returned for use in the rest of the program.
        if (keyboard.hasNextInt())
        {
            inputInteger = keyboard.nextInt();
            if (inputInteger < 0)
            {
                inputInteger = defaultInteger;
            }
        }

        else
        {
            keyboard.nextLine();
            inputInteger = defaultInteger;
        }

        return inputInteger;
    }

    // The following method uses a mathematical formula to compute the area of a cylinder by using the radius and length values that are provided.
    public static double cylinderArea(double radius, double length) {
        double cylinder_disc_area, cylinder_perimeter, area;

        cylinder_disc_area = Math.PI * Math.pow(radius, 2);
        cylinder_perimeter = 2 * Math.PI * radius;

        area = 2 * cylinder_disc_area + cylinder_perimeter * length; // 2 times the area of the disc plus the cylinder_perimeter times the length.

        return area;
    }

    // The following method uses a mathematical formula to compute the area of a square pyramid by using the side and length values that are provided.
    public static double squarePyramidArea(double side, double length) {
        double square_pyramid_base_area, square_pyramid_triangle_area, semi_perimeter, area;

        square_pyramid_base_area = Math.pow(side, 2);

        semi_perimeter = (length + length + side) / 2.0;
        square_pyramid_triangle_area = Math.sqrt(semi_perimeter * (semi_perimeter - length) * (semi_perimeter - length) * (semi_perimeter - side));

        area = square_pyramid_base_area + (4 * square_pyramid_triangle_area);

        return area;
    }

    // The following method uses a mathematical formula to compute the area of a rectlinear by using the three side length values that are provided.
    public static double rectlinearArea(double side_length_A, double side_length_B, double side_length_C) {
        double area;

        area = 2 * ((side_length_A * side_length_B) + (side_length_A * side_length_C) + (side_length_B * side_length_C));

        return area;
    }

    // The following method is where most of the program depends on:
    // - Receives the choice of the user for which area to compute.
    // - Variables that store the respective argument values for each area method are declared inside each case by calling getDouble().
    // - Prompts for the correct needed values to compute the area depending on the choice of the user.
    // - Stores the value of the area of the desired shape and prints a formatted line with the result.
    // - Returns the area to the main method (where this method is called) be stored in another variable for comparison.
    public static double getArea(Scanner keyboard, int choice) {

        switch (choice) {
            case 1:
                System.out.print("Enter radius and length: ");
                double cylinderRadius = getDouble(keyboard);
                double cylinderLength = getDouble(keyboard);

                double cylinderAreaResult = cylinderArea(cylinderRadius, cylinderLength);
                System.out.printf("The area is %.6f %n%s", cylinderAreaResult, "----------------\n");
                return cylinderAreaResult;

            case 2:
                System.out.print("Enter side and length: ");
                double squarePyramidSide = getDouble(keyboard);
                double squarePyramidLength = getDouble(keyboard);

                double squarePyramidAreaResult = squarePyramidArea(squarePyramidSide, squarePyramidLength);
                System.out.printf("The area is %.6f %n%s", squarePyramidAreaResult, "----------------\n");
                return squarePyramidAreaResult;

            case 3:
                System.out.print("Enter three sides: ");
                double sideLengthA = getDouble(keyboard);
                double sideLengthB = getDouble(keyboard);
                double sideLengthC = getDouble(keyboard);

                double rectlinearAreaResult = rectlinearArea(sideLengthA, sideLengthB, sideLengthC);
                System.out.printf("The area is %.6f %n%s", rectlinearAreaResult, "----------------\n");
                return rectlinearAreaResult;

            // Outputs an error message to the user and returns 0.0 as a default value for an invalid choice.
            default:
                System.out.println("Invalid choice. Please try again.");
                return 0.0;
        }
    }
}
