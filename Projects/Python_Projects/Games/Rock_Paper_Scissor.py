import random

user_wins = 0
computer_wins = 0
input_count = 0

options = ["rock", "paper", "scissors"]

while True:
    # .lower() serves so that if the user inputs q or Q it will be the same thing. All inputs will be the same in lower or upper case under the .lower() method.
    user_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower()
    if user_input == "q":
        quit()

    if user_input not in options:
        continue

    input_count += 1

    random_number = random.randint(0, 2)
    # rock: 0, paper: 1, scissors: 2

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
    if computer_guess == "scissors" and user_input == "scissors":
        input_count -= 1
    if computer_guess == "rock" and user_input == "rock":
        input_count -= 1
    if computer_guess == "paper" and user_input == "paper":
        input_count -= 1

    # End the game when 3 turns are played!
    if input_count == 3:
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

print("Goodbye!")
