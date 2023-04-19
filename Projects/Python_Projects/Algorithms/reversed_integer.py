# Given an integer, return the integer with reversed digits.
# Note: The integer could be either positive or negative.

# 123 -> 321
# -123 -> -321

def reversed_integer(string_input):
    if string_input[0] == "-":
        return int("-" + string_input[:0:-1])
    else:
        return int(string_input[::-1])


def main():
    string_input = input("Type a number (negative or positive):\n> ")
    print(reversed_integer(string_input))


if (__name__ == "__main__"):
    main()
