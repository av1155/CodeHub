decision = input("Do you want to play a game? (y/n) ")

if decision == "y":
    print("You are walking through a parking lot and see a $20 bill on the ground. Do you: ")
    print("1. Pick it up")
    print("2. Leave it")

    choice = input("> ")

    if choice == "1":
        print("You found a lottery ticket underneath of the $20 dollar bill! Do you:")
        print("1. Scratch it off ")
        print("2. Give it to a homeless person")

        choice2 = input("> ")

        if choice2 == "1":
            print("You were one number away from winning 1 million dollars.")
        elif choice2 == "2":
            print("The homeless person was really grateful and gave you a hug. He also won the lottery and gave you half of it!")
        else:
            print("You did not pick a valid option. You lose!")

    elif choice == "2":
        print("You find yourself in an alternate universe where you are now a millionaire, but your family is not with you anymore. Do you:")
        print("1. Find the way to your old universe.")
        print("2. Stay in this alternate universe and dominate the world.")
        print("3. Forget everything and live a simple life in a cave.")

        insanity = input("> ")

        if insanity == "1" or insanity == "2":
            print("The insanity rots your eyes into a pool of muck.")
            print("Good job!")
        else:
            print("Your body survives powered by a mind of jello.")
            print("Good job!")
    else:
        print("You stumble around and fall on a knife and die. Good job!")
else:
    print("You are a coward. Goodbye!")
