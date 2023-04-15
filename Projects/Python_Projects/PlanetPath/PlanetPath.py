import sys


def walking(distance):
    emissions = distance * 404
    points = round(distance * 10)
    print(f"\nYou just saved {round(emissions, 2)} grams of CO2 emissions by walking {distance} miles with PlanetPath. Keep up the good work for a greener planet!")
    print(
        f"\nYou've earned {points} points for walking {distance} miles with PlanetPath!")

    exit()


def biking(distance):
    emissions = distance * 404
    points = round(distance * 10)
    print(f"\nYou just saved {round(emissions, 2)} grams of CO2 emissions by biking {distance} miles with PlanetPath. Keep up the good work for a greener planet!")
    print(
        f"\nYou've earned {points} points for biking {distance} miles with PlanetPath!")
    exit()


def bus(distance):
    emissions = distance * 209
    points = round(distance * 5)
    print(f"\nYou just saved {round(emissions, 2)} grams of CO2 emissions by using the bus for {distance} miles with PlanetPath. Keep up the good work for a greener planet!")
    print(
        f"\nYou've earned {points} points for using the bus for {distance} miles with PlanetPath!")
    exit()


def ride_share(distance):
    number_of_people = int(
        input("How many people are in the car with you?\n> "))

    emissions = distance * 404
    total_emissions = emissions / number_of_people
    points = round(distance * 3)
    print(f"\nEach passenger saved {round(total_emissions, 2)} grams of CO2 emissions by using ride share for {distance} miles with PlanetPath. Keep up the good work for a greener planet!")
    print(
        f"\nYou've earned {points} points for using ride share for {distance} miles with PlanetPath!")
    exit()


def main():
    print("\nWelcome to PlanetPath")

    while True:
        try:
            # Prompt user to enter distance
            distance = input("\nHow many miles are you travelling? ")
            if distance == 'exit':
                sys.exit()
            distance = float(distance)

            # Display CO2 emissions and points for each transportation option
            print(f"\nCO2 emissions and points for {distance} miles:\n")
            print(
                f"1) Walking: {round(distance * 404, 2)} grams of CO2 emissions, {round(distance * 10)} points")
            print(
                f"2) Biking: {round(distance * 404, 2)} grams of CO2 emissions, {round(distance * 10)} points")
            print(
                f"3) Bus: {round(distance * 209, 2)} grams of CO2 emissions, {round(distance * 5)} points")
            print(
                f"4) Ride share: {round(distance * 404, 2)} grams of CO2 emissions potentially saved by all passengers, {round(distance * 3)} points")

            # Prompt user to choose transportation option
            choice = input("\nPlease choose a transportation option (1-4): ")
            if choice == 'exit':
                sys.exit()
            choice = int(choice)

            # Call appropriate function based on transportation option
            if choice == 1:
                walking(distance)
            elif choice == 2:
                biking(distance)
            elif choice == 3:
                bus(distance)
            elif choice == 4:
                ride_share(distance)
            else:
                print("Invalid choice. Please choose a number from 1-4.")

        except ValueError:
            print("Please enter a valid input or 'exit' to quit the program.")


if (__name__ == "__main__"):
    main()
