import java.util.Scanner;

public class StringEdit {
    public static void main(String[] args) {
        Scanner keyboard = new Scanner(System.in);

        System.out.print("Enter input: ");
        String userString = keyboard.nextLine().toUpperCase();

        StringBuilder builder = new StringBuilder(userString);
        report(builder);

        boolean terminate = false;
        for (; !terminate ;)
        {
            printInstruction();
            String action = keyboard.next().toUpperCase();

            switch (action.charAt(0))
            {
                case 'I':
                    insert(keyboard, builder);
                    break;

                case 'D':
                    delete(keyboard, builder);
                    break;

                case 'S':
                    substitute(keyboard, builder);
                    break;

                case 'R':
                    System.out.println("-------------------------");
                    System.out.println("0000000000111111111122222");
                    System.out.println("0123456789012345678901234");
                    System.out.println(builder.reverse());
                    System.out.print("-------------------------");
                    break;

                case 'Q':
                    terminate = true;
                    break;

                default:
                    System.out.println("Invalid option. Please try again.");
                    break;
            }
        }
    }

    public static void report(StringBuilder builder)
    {
        System.out.println("-------------------------");
        System.out.println("0000000000111111111122222");
        System.out.println("0123456789012345678901234");
        System.out.println(builder);
        System.out.print("-------------------------");
    }

    public static void printInstruction()
    {
        System.out.print("""
                    \nCommands are:
                    (I)nsert <= 3 symbols
                    (D)elete - range <= 3
                    (S)ubstitute - range <= 3 w. <= 3 symbols
                    (R)everse
                    (Q)uit
                    Enter I/D/S/R/Q:\s""");
    }

    public static int getInteger(Scanner in)
    {
        if (in.hasNextInt()) // if true
        {
            return in.nextInt(); // return the integer
        }

        else
        {
            in.next(); // consume one token from the input
            return -1;
        }
    }

    public static void insert(Scanner in, StringBuilder builder)
    {
        boolean check1 = false; // Initialize check1
        boolean check2 = false; // Initialize check2

        System.out.print("Enter position and symbols: ");

        int position = getInteger(in);
        String symbols = in.next().toUpperCase();

        if (position >= 0 && position <= builder.length())
        {
            check1 = true; // Set check1 to true if condition is met
        }

        if (symbols.length() <= 3)
        {
            check2 = true; // Set check2 to true if condition is met
        }

        System.out.println("-------------------------");
        System.out.println("0000000000111111111122222");
        System.out.println("0123456789012345678901234");
        if (check1 && check2) // Perform builder operation if requirements are met.
        {
            System.out.println(builder.insert(position, symbols));
        }

        else
        {
            System.out.println(builder);
        }
        System.out.print("-------------------------");
    }

    public static void delete(Scanner in, StringBuilder builder)
    {
        boolean check1 = false;
        boolean check2 = false;

        System.out.print("Enter start and end: ");
        int start = getInteger(in);
        int end = getInteger(in);

        if ((start >= 0) && (start <= builder.length()))
        {
            check1 = true;
        }

        if ((end >= start) && (end <= start + 3))
        {
            check2 = true;
        }

        System.out.println("-------------------------");
        System.out.println("0000000000111111111122222");
        System.out.println("0123456789012345678901234");
        if (check1 && check2)
        {
            System.out.println(builder.delete(start, end));
        }

        else
        {
            System.out.println(builder);
        }
        System.out.print("-------------------------");
    }

    public static void substitute(Scanner in, StringBuilder builder)
    {
        boolean check1 = false;
        boolean check2 = false;
        boolean check3 = false;

        System.out.print("Enter start, end, and symbols: ");
        int start = getInteger(in);
        int end = getInteger(in);
        String symbols = in.next().toUpperCase();

        if ((start >= 0) && (start <= builder.length()))
        {
            check1 = true;
        }

        if ((end >= start) && (end <= start + 3))
        {
            check2 = true;
        }

        if (symbols.length() <= 3)
        {
            check3 = true; // Set check3 to true if condition is met
        }

        System.out.println("-------------------------");
        System.out.println("0000000000111111111122222");
        System.out.println("0123456789012345678901234");
        if (check1 && check2 && check3)
        {
            System.out.println(builder.replace(start, end, symbols));
        }

        else
        {
            System.out.println(builder);
        }
        System.out.print("-------------------------");
    }
}
