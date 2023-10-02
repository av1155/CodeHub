# StringEdit Java Program

The **StringEdit** Java program demonstrates string manipulation by allowing users to insert, delete, substitute, and reverse parts of a given string. It interacts with the user through the console, providing a simple yet effective interface to modify the input string.

## Features

- **Insertion**: Insert symbols at a specified position in the string (up to 3 symbols).
- **Deletion**: Delete a range of symbols in the string (up to 3 symbols in a specified range).
- **Substitution**: Substitute symbols in a specified range of the string (up to 3 symbols and a range of up to 3).
- **Reversal**: Reverse the input string.
- **Quit**: Exit the program.

## How to Run

Compile the Java program using a Java compiler and run the compiled program.

```bash
javac StringEdit.java
java StringEdit
```

Follow the on-screen instructions to manipulate the input string using the provided commands.

## Example

Suppose we start with the input string examplestring. Here's a brief example of using the program:

```bash
Enter input: examplestring
-------------------------
0000000000111111111122222
0123456789012345678901234
EXAMPLESTRING
-------------------------
Commands are:
(I)nsert <= 3 symbols
(D)elete - range <= 3
(S)ubstitute - range <= 3 w. <= 3 symbols
(R)everse
(Q)uit
Enter I/D/S/R/Q: I
Enter position and symbols: 5 ABC
-------------------------
0000000000111111111122222
0123456789012345678901234
EXAMPABCLESTRING
-------------------------
```

## Note

This program showcases fundamental string manipulation techniques and provides a foundation for building more complex applications in Java.

## Author

Andrea Arturo Venti Fuentes
