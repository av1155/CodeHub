import java.util.Scanner;

public class ProjectileMotionCalculator {
    public static final double earthG = 9.807; // Earth's gravity constant (g = 9.8 m/s^2)
    public static final double moonG = 1.620; // Moon's gravity constant (g = 1.620 m/s^2)

    public static void main(String[] args) {
        Scanner keyboard = new Scanner(System.in);
        double user_angle, user_speed, user_height, corrected_angle_minimum, corrected_angle_maximum, angle_degrees_to_radians, correctedSpeed, correctedHeight, verticalSpeed, horizontalSpeed;

        message("Distance Calculation");

        System.out.print("Enter angle (degree): ");
        user_angle = keyboard.nextDouble();

        System.out.print("Enter speed (m/s): ");
        user_speed = keyboard.nextDouble();

        System.out.print("Enter height (m): ");
        user_height = keyboard.nextDouble();

        keyboard.close();

        corrected_angle_minimum = Math.min(user_angle, 90);
        corrected_angle_maximum = Math.max(corrected_angle_minimum, 0);
        angle_degrees_to_radians = Math.toRadians(corrected_angle_maximum);

        correctedSpeed = Math.max(user_speed, 0);
        correctedHeight = Math.max(user_height, 0);

        verticalSpeed = Math.sin(angle_degrees_to_radians) * correctedSpeed;
        horizontalSpeed = Math.cos(angle_degrees_to_radians) * correctedSpeed;

        message("On the Earth");
        compute(verticalSpeed, horizontalSpeed, correctedHeight, earthG);
        message("On the Moon");
        compute(verticalSpeed, horizontalSpeed, correctedHeight, moonG);
    }

    public static void compute(double verticalSpeed, double horizontalSpeed, double height, double gravity) {
        double upward_time_t0, upward_distance_h0, downward_distance_h1, downward_time_t1, total_time_t2, horizontal_distance_r;

        myPrint("Height of the cliff", height, "m");
        myPrint("Horizontal speed", horizontalSpeed, "m/s");
        myPrint("Initial vertical speed", verticalSpeed, "m/s");
        myPrint("Gravity", gravity, "m/s^2");

        // upward_time_t0 = duration of the upward movement
        //      upward_time_t0 = v/BallReach.earthG
        upward_time_t0 = verticalSpeed/gravity;

        // upward_distance_h0 = vertical distance the ball goes up from the cliff
        //      upward_distance_h0 = BallReach.earthG * Math.pow((v/BallReach.earthG), 2) - (1/2) * BallReach.earthG * Math.pow(upward_time_t0, 2)
        upward_distance_h0 = gravity * Math.pow((verticalSpeed/gravity), 2) - (1/2.0) * gravity * Math.pow(upward_time_t0, 2);

        // downward_distance_h1 = vertical distance the ball falls (downward_distance_h1 = upward_distance_h0 + h)
        //      downward_distance_h1 = (1/2 * BallReach.earthG) * Math.pow(v, 2) + h
        downward_distance_h1 = upward_distance_h0 + height;

        // downward_time_t1 = duration of the downward movement
        //      downward_time_t1 = Math.sqrt((Math.pow(v, 2)/2 * Math.pow(BallReach.earthG, 2)) + h/BallReach.earthG)
        downward_time_t1 = Math.sqrt((2 * downward_distance_h1)/gravity);

        // total_time_t2 = total duration (total_time_t2 = upward_time_t0 + downward_time_t1)
        //      total_time_t2 = v/BallReach.earthG + Math.sqrt((Math.pow(v, 2)/2 * Math.pow(BallReach.earthG, 2)) + h/BallReach.earthG)
        total_time_t2 = verticalSpeed/gravity + downward_time_t1;

        // horizontal_distance_r = how far the ball reaches (u(upward_time_t0 + downward_time_t1))
        //      horizontal_distance_r = u * (v/BallReach.earthG + Math.sqrt((Math.pow(v, 2)/2 * Math.pow(BallReach.earthG, 2)) + h/BallReach.earthG))
        horizontal_distance_r = horizontalSpeed * (verticalSpeed/gravity + downward_time_t1);

        // OUTPUT
        myPrint("Upward time", upward_time_t0, "s");
        myPrint("Upward distance", upward_distance_h0, "m");
        myPrint("Downward time", downward_time_t1, "s");
        myPrint("Downward distance", downward_distance_h1, "m");
        myPrint("Total time", total_time_t2, "s");
        myPrint("Horizontal distance", horizontal_distance_r, "m");

    }

    public static void message(String message) {
        System.out.printf( "........ %s ........%n", message );
    }

    public static void myPrint(String name, double value, String unit) {
        System.out.printf( "%30s:%14.4f (%s)%n", name, value, unit );
    }
}
