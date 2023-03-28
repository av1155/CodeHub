import random

# Variables to count for the number of user and computer wins, and another variable to count the number of turns played.
user_wins = 0
computer_wins = 0
input_count = 0

# Rock, paper, scissors is placed inside a list for later use.
options = ["rock", "paper", "scissors"]

user_decision = input(
    "Do you want to play rock, paper, scissors? (y/n): ").lower()
if user_decision != "y" and user_decision != "yes":
    print("\nGoodbye!")
    quit()

while True:
    try:
        number_of_turns = int(input("How many turns do you want to play? "))
        break
    except ValueError:
        print("\nPlease enter a valid number.")

# while True loop for the main section of the game.
while True:
    # .lower() serves so that if the user inputs q or Q it will be the same thing. All inputs will be the same in lower or upper case under the .lower() method.
    user_input = input("Type Rock/Paper/Scissors: ").lower()

    # Input validation: Checks to see if what the user wrote is an option, if not, it will re-run the first prompt asking the user to quit or pick an option.
    if user_input not in options:
        continue

    # Adds one turn to the counter every time the user plays. Because it is placed after "continue" it will not count errors in the input.
    input_count += 1

    # Random function is imported here as a randint list from 0 to 2, and assigned to a variable called random_number. randint counts from 0, to 2, unline range would.
    random_number = random.randint(0, 2)
    # rock: 0, paper: 1, scissors: 2

    # The computer guess is assigned to the random_number variable.
    computer_guess = options[random_number]
    print(f"\nComputer picked {computer_guess}! You picked {user_input}!")

    # User decision
    if user_input == "rock" and computer_guess == "scissors":
        print(f"You won!\n")
        user_wins += 1
    if user_input == "paper" and computer_guess == "rock":
        print(f"You won!\n")
        user_wins += 1
    if user_input == "scissors" and computer_guess == "paper":
        print(f"You won!\n")
        user_wins += 1

    # Computer decision
    if computer_guess == "rock" and user_input == "scissors":
        print(f"You lost!\n")
        computer_wins += 1
    if computer_guess == "paper" and user_input == "rock":
        print(f"You lost!\n")
        computer_wins += 1
    if computer_guess == "scissors" and user_input == "paper":
        print(f"You lost!\n")
        computer_wins += 1

    # Ties reduce input_count
    if computer_guess == user_input:
        print("Tie!\n")
        input_count -= 1

    # End the game when 3 turns are played!
    if input_count == number_of_turns:
        break

# Winner calculation and decision
if user_wins == computer_wins:
    print(
        f"Tie! You got {user_wins} points, and the computer got {computer_wins}")
else:
    if user_wins > computer_wins:
        print(
            f"You won with {user_wins} points! The computer got {computer_wins} points.")
    else:
        print(
            f"You lost! The computer got {computer_wins} points! You got {user_wins} points :(")

print("\nGoodbye!")
