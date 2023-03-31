import random

print("Welcome to the number guessing game!")
print("You have to guess a number between 1 and 30.")
print("You will have 5 attempts to guess the number.")
print("If you guess the number, you win!")
print("If you don't, you lose!")
print("Good luck!\n")

user_decision = input("Do you want to play? (y/n): ").lower()
if user_decision != "y" and user_decision != "yes":
    print("\nGoodbye!")
    quit()

while True:
    print("\nGuess a number between 1 and 30: ")

    def guess_number(counter):
        while counter < 5:
            try:
                number = int(input("> "))
                counter += 1
                if (number < 1) or (number > 30):
                    continue
                elif number == random_number:
                    print(
                        f"\nCongratulations! You guessed the number in {counter} attempts!\n")
                    return True
                elif (random_number - 3 <= number <= random_number + 3):
                    print("\nYou are so close! Try again.")
                elif number > random_number:
                    print(f"\nThe number is lower than {number}. Try again.")
                elif number < random_number:
                    print(f"\nThe number is higher than {number}. Try again.")

            except ValueError:
                print("\nPlease enter a valid number.")

        print(
            f"\nSorry, you ran out of attempts. The number was {random_number} :(\n")
        return False

    random_number = random.randint(1, 30)
    counter = 0
    result = guess_number(counter)

    play_again = input("Do you want to play again? (y/n): ").lower()
    if play_again != "y" and play_again != "yes":
        print("\nThanks for playing!")
        break
