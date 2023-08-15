public class HelloWorld {
    public static void main(String[] args) {
        // Primitive Variables:
        int myInteger = 7;
        System.out.println(myInteger);

        double myDecimal = 21.078;
        System.out.println(myDecimal);

        char myInitial = 'A';
        System.out.println(myInitial);

        // Multiplying integer and decimal:
        System.out.println(myInteger * myDecimal);

        // Storing and then printing the product of myInteger and myDecimal:
        double result = myInteger * myDecimal;
        System.out.println(result);


        // To store strings, use non-primitive type "String":
        String myString = "Hey, my name is Andrea";
        System.out.println(myString);

        // Using . after a variable makes the program suggest many different methods.
//        myString.toUpperCase();
        System.out.println(myString.toUpperCase());
//        myString.length();
        System.out.println(myString.length());

        // Call method burp
        burp();

        // Call method printName
        printNameAndAge("Andrea", 23);

        // Call method favoriteTeam
        System.out.println(favoriteTeam("Real Madrid"));
    }

    private static void burp() {
        System.out.print("Buuuurp");
    }

    private static void printNameAndAge(String name, int number) {
        System.out.print("My name is " + name + " and I am " + number + " years old.");

    }

    // Return a value:
    private static String favoriteTeam(String team) {
        return "My favorite team is " + team;
    }

}