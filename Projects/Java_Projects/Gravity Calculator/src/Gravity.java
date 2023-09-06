import java.util.Scanner;

public class Gravity {
    public static final double g = 9.8;
    public static void main(String[] args) {
        // gt = speed of object at t seconds after its release
        // (1/2) * g * (Math.pow(t, 2)) = distance object has travelled in the t seconds after release
        // g = gravity constant (9.8)

        operations(12.37); // seconds -> predetermined value in code
        operations(59.22); // seconds -> predetermined value in code

        Scanner keyboard; // Variable type declaration

        keyboard = new Scanner(System.in); // created new scanner

        // User input for travel times
        System.out.print("Enter the first travel time (seconds):\n> ");
        double t1 = keyboard.nextDouble();

        System.out.print("Enter the second travel time (seconds):\n> ");
        double t2 = keyboard.nextDouble();

        keyboard.close(); // closed the scanner

        // Calculations based on user input
        operations(t1);
        operations(t2);

    }
    private static void operations(double t) {
        double speed, distance; // declaring variable types

        // Calculate speed and distance
        speed = g * t; // formula for speed
        distance = ((double) 1/2) * g * (Math.pow(t, 2)); // distance object has travelled in the t seconds after release. To get a double instead of an integer after division operation: (1.0/2) or ((double) 1/2)

        // Print the results
        System.out.println("Speed: " + speed);
        System.out.println("Distance: " + distance + " \n");
    }
}
