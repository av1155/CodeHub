# Given k numbers which are less than n, return the set of prime number among them
# Note: The task is to write a program to print all Prime numbers in an Interval.
# Definition: A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself.


def prime_numbers_array(range_input):

    # create an empty list to store the prime numbers
    prime_numbers = []

    for number in range(int(range_input)):
        if number > 1:  # all prime numbers are greater than 1
            for i in range(2, number):
                if (number % i) == 0:
                    break
            else:
                prime_numbers.append(number)

    return prime_numbers


def main():
    range_input = input(
        "Enter the range for which the array should follow:\n> ")
    print(*prime_numbers_array(range_input))


if (__name__ == "__main__"):
    main()
