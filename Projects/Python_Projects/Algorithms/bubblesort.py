'''
Write a Python program that takes a list of integers as input and sorts the list using the Bubble Sort algorithm. The program should perform the following steps:

1. Define a function called bubble_sort that takes a single parameter, a list of integers.

2. Use a nested loop to iterate over each pair of adjacent elements in the list.

3. For each pair of adjacent elements, if the element on the left is greater than the element on the right, swap the two elements.

4. Repeat step 2 and step 3 until no more swaps are necessary (i.e., the list is sorted).

5. Return the sorted list.

Note: You are not required to implement any error handling or input validation for this program.
'''


def bubble_sort(string_integers):
    # Split the string of integers into a list of strings and convert each string to an integer.
    string_list = string_integers.split()
    # Turn the string_list into integers by using list comprehension method. Turns every element in the string_list into an integer, one by one.
    integer_list = [int(element) for element in string_list]
    # Get the length of the list.
    length = len(integer_list)

    # Perform the bubble sort algorithm.
    for i in range(length - 1):
        # Loop through the list up to the second to last element.
        for j in range(length - 1):
            # Check if the element at the current index is greater than the next element in the list.
            if integer_list[j] > integer_list[j + 1]:
                # If it is bigger, the value of the first index is duplicated in a temporary variable, and the original value remains unchanged.
                temporary_list = integer_list[j]
                # The original value of the first index in the integers list is now replaced with the original value in the second index (the smaller number).
                integer_list[j] = integer_list[j + 1]
                # Because the value of the first index was updated to be the smaller number (`integer_list[j] = integer_list[j + 1]`)... we can now update the value of the second index `[j + 1]` with the value that was stored in the temporary list, which is the larger number.
                integer_list[j + 1] = temporary_list

    # Return the sorted list of integers.
    return integer_list


def main():
    string_integers = input(
        "Type a list of integers in the format: 1 2 3 4\n> ")

    for element in bubble_sort(string_integers):
        print(element, end=" ")

    print("\n")


if (__name__ == "__main__"):
    main()
