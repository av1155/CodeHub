'''
Write a Python program that takes a list of integers as input, removes any repeated numbers, and sorts the list using the Bubble Sort algorithm. The program should perform the following steps:

1. Define a function called bubble_sort that takes a single parameter, a list of integers.

2. Use a nested loop to iterate over each pair of adjacent elements in the list.

3. For each pair of adjacent elements, if the element on the left is greater than the element on the right, swap the two elements.

4. Repeat step 2 and step 3 until no more swaps are necessary (i.e., the list is sorted).

5. Return the unique sorted list.

Note: You are not required to implement any error handling or input validation for this program.
'''


def bubble_sort(string_integers):
    string_list = string_integers.split()
    integers_list = [int(element) for element in string_list]

    # Use set() to remove any repeated numbers... it turns the list into all unique values
    unique_set = set(integers_list)
    # Turn the set() back to a list using list()
    unique_list = list(unique_set)

    # Measure the length of the list
    length = len(unique_list)

    # Bubble Sort
    for i in range(length - 1):
        for j in range(length - 1):
            if unique_list[j] > unique_list[j + 1]:
                temporary_list = unique_list[j]
                unique_list[j] = unique_list[j + 1]
                unique_list[j + 1] = temporary_list

    return unique_list


def main():
    string_integers = input(
        "Type a list of integers in the format: 1 2 3 4\n> ")
    for element in bubble_sort(string_integers):
        print(element, end=" ")


if (__name__ == "__main__"):
    main()
