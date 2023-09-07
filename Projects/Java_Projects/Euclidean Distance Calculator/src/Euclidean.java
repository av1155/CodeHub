import java.util.InputMismatchException;
import java.util.Scanner;

public class Euclidean {
    public static void main(String[] args) {
        Scanner keyboard; // Declare a Scanner for user input.
        keyboard = new Scanner(System.in); // Create a Scanner instance.

        // Continuous loop until the user chooses to exit.
        while (true) {
            try {
                double x1, y1, z1, x2, y2, z2; // Declare variables for coordinates.

                // Prompt the user to input the first set of coordinates.
                System.out.println("Input the variable values for x1, y1, z1: ");
                x1 = keyboard.nextDouble();
                y1 = keyboard.nextDouble();
                z1 = keyboard.nextDouble();

                // Prompt the user to input the second set of coordinates.
                System.out.println("Input the variable values for x2, y2, z2: ");
                x2 = keyboard.nextDouble();
                y2 = keyboard.nextDouble();
                z2 = keyboard.nextDouble();

                // Calculate and display the Euclidean distance.
                double distance = euclidean(x1, y1, z1, x2, y2, z2);
                System.out.println("\nsqrt((" + x1 + " - " + x2 + ")^2 + (" + y1 + " - " + y2 + ")^2 + (" + z1 + " - " + z2 + ")^2)\n");
                System.out.println("Euclidean distance: " + distance + "\n");

                // Ask the user if they want to calculate another distance.
                System.out.println("Do you want to calculate another distance? (y/n): ");
                String input = keyboard.next();

                // Exit the loop if the user's input is not "y" or "Y."
                if (!input.equalsIgnoreCase("y")) {
                    break;
                }

                // Input error handling for non-numeric input.
            } catch (InputMismatchException e) {
                System.out.println("Invalid input. Please enter valid numeric values.");
                keyboard.nextLine(); // Consume the invalid input to avoid an infinite loop
            }
        }

        keyboard.close(); // Close the Scanner.
    }

    // Calculate the Euclidean distance between two points in 3D space.
    private static double euclidean(double x1, double y1, double z1, double x2, double y2, double z2) {
        return Math.sqrt(Math.pow(x1 - x2, 2) + Math.pow(y1 - y2, 2) + Math.pow(z1 - z2, 2));
    }
}
