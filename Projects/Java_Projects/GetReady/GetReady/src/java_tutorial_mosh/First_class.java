package java_tutorial_mosh;

public class First_class {
    // `psvm`
    public static void main(String[] args) {
        // `sout` creates `System.out.println();`
        System.out.println("The following is my learning experience by watching the Java tutorial from Mosh");

        // `PrintHelloWorld();` calls the private function `private static void PrintHelloWorld()`... which contains within the curly brackets `System.out.println("HelloWorld);`
        PrintHelloWorld();
    }

    private static void PrintHelloWorld() {
        System.out.println("HelloWorld");
    }

}
