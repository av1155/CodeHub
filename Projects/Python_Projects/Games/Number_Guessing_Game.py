import random

user_decision = input(
    "Do you want to play a number guessing game? (y/n): ").lower()
if user_decision != "y" and user_decision != "yes":
    print("\nGoodbye!")
    quit()

while True:
    while True:
        n = random.randint(1, 30)
        counter = 0
        number = int(input("\nGuess a number between 1 and 30: "))
        if (number == n):
            print("\nYou guessed correctly!!! Go you!")
            counter += 1

        while (number < 1) or (number > 30):
            number = int(
                input("\nThat is an invalid number. Please re-enter a number between 1 and 30: "))
            if (number == n):
                print("\nYou guessed correctly!!! Go you!")

        while number != n:
            if (number <= 5) and (n > 5):
                number = int(input("\nToo low! Try again: "))
                counter += 1
            elif (number >= 25) and (n < 25):
                number = int(input("\nWay too high! Try again: "))
                counter += 1
            elif ((n + 5 >= number) and (n - 5 <= number)):
                number = int(input("\nYou are so close! Try again: "))
                counter += 1
            else:
                number = int(input("\nWrong! Try again: "))
                counter += 1
            if (number == n):
                print("\nYou guessed correctly!!! Go you!")
            while (number < 1) or (number > 30):
                number = int(
                    input("\nThat is an invalid number. Please re-enter a number between 1 and 30: "))

        print(f"You took {counter} attempts to guess the number!")

        if number == n:
            break

    play_again = input("\nDo you want to play again? (y/n): ").lower()
    counter = 0
    if play_again != "y" and play_again != "yes":
        print("\nYour loss....")
        break
