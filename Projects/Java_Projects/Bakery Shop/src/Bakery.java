import java.util.Scanner;

public class Bakery {
    public static void main(String[] args) {
        Scanner keyboard;
        keyboard = new Scanner(System.in);

        double pastries, coffees, sandwiches, loaves;
        pastries = 4.5; // $4.5
        coffees = 3.0; // $3.0
        sandwiches = 6.0; // $6.0
        loaves = 7.0; // $7.0

        int number_of_pastries, number_of_coffees, number_of_sandwiches, number_of_loaves;

        double subtotal_amount, total_tax, total_amount;
        double tax_rate = 0.07; // 7%

        System.out.println("Welcome to Dana's Bakery!");
        System.out.println("Pastries are " + pastries + " dollars each.");
        System.out.println("Coffees are " + coffees + " dollars each.");
        System.out.println("Sandwiches are " + sandwiches + " dollars each.");
        System.out.println("Loaves are " + loaves + " dollars each.");

        System.out.print("How many pastries? ");
        number_of_pastries = keyboard.nextInt();
        subtotal_amount = number_of_pastries * pastries;
        System.out.println("Subtotal is " + (subtotal_amount) + " dollars.");

        System.out.print("How many coffees? ");
        number_of_coffees = keyboard.nextInt();
        subtotal_amount += (number_of_coffees * coffees);
        System.out.println("Subtotal is " + (subtotal_amount) + " dollars.");

        System.out.print("How many sandwiches? ");
        number_of_sandwiches = keyboard.nextInt();
        subtotal_amount += (number_of_sandwiches * sandwiches);
        System.out.println("Subtotal is " + (subtotal_amount) + " dollars.");

        System.out.print("How many loaves? ");
        number_of_loaves = keyboard.nextInt();
        subtotal_amount += (number_of_loaves * loaves);
        System.out.println("Subtotal is " + (subtotal_amount) + " dollars.");

        // Calculate tax amount for all items
        total_tax = (int)(subtotal_amount * tax_rate * 100) / 100.0;
        System.out.println("Tax is " + (total_tax) + " dollars.");

        /*
        - System.out.println(subtotal_amount * tax_rate);
        WE DO NOT USE THIS BECAUSE THE DECIMAL WOULD BE TOO LONG AND UGLY.
        - By using the above total_tax operation the tax is computed, set to integer, and multiplied by 100
        to maintain the 2 decimal values, then it is divided by 100.0 to convert it to a short decimal.
        */

        // Calculate total amount
        total_amount = subtotal_amount + total_tax;
        System.out.println("Total is " + (total_amount) + " dollars.");

        System.out.println("Thank you for coming. See you soon!");
    }
}
