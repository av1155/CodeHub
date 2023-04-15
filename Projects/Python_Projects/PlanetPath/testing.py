import sys
from geopy.geocoders import Nominatim
from geopy.distance import geodesic


def get_distance(place1, place2):
    # Create a geocoder object
    geolocator = Nominatim(user_agent="my-app")

    # Geocode the place names to get their coordinates
    location1 = geolocator.geocode(place1)
    location2 = geolocator.geocode(place2)

    # Calculate the distance between the two coordinates using geodesic distance
    distance = geodesic((location1.latitude, location1.longitude),
                        (location2.latitude, location2.longitude)).miles

    return distance


def walking(distance):
    emissions = distance * 404
    points = round(distance * 10)
    print(f"\nYou just saved {round(emissions, 2)} grams of CO2 emissions by walking {round(distance, 2)} miles with PlanetPath. Keep up the good work for a greener planet!")
    print(
        f"\nYou've earned {points} points for walking {round(distance, 2)} miles with PlanetPath!")

    exit()


def biking(distance):
    emissions = distance * 404
    points = round(distance * 10)
    print(f"\nYou just saved {round(emissions, 2)} grams of CO2 emissions by biking {round(distance, 2)} miles with PlanetPath. Keep up the good work for a greener planet!")
    print(
        f"\nYou've earned {points} points for biking {round(distance, 2)} miles with PlanetPath!")
    exit()


def bus(distance):
    emissions = distance * 209
    points = round(distance * 5)
    print(f"\nYou just saved {round(emissions, 2)} grams of CO2 emissions by using the bus for {round(distance, 2)} miles with PlanetPath. Keep up the good work for a greener planet!")
    print(
        f"\nYou've earned {points} points for using the bus for {round(distance, 2)} miles with PlanetPath!")
    exit()


def ride_share(distance):
    number_of_people = int(
        input("How many people are in the car with you?\n> "))

    emissions = distance * 404
    total_emissions = emissions / number_of_people
    points = round(distance * 3)
    print(f"\nEach passenger saved {round(total_emissions, 2)} grams of CO2 emissions by using ride share for {round(distance, 2)} miles with PlanetPath. Keep up the good work for a greener planet!")
    print(
        f"\nYou've earned {points} points for using ride share for {round(distance, 2)} miles with PlanetPath!")
    exit()


def main():
    print("\nWelcome to PlanetPath")

    while True:
        try:
            # Prompt user to enter place names
            place1 = input("\nWhat is your starting point? ")
            if place1 == 'exit':
                sys.exit()

            place2 = input("\nWhat is your destination? ")
            if place2 == 'exit':
                sys.exit()

            # Get the distance between the two places
            distance = get_distance(place1, place2)

            # Display CO2 emissions and points for each transportation option
            print(
                f"\nCO2 emissions and points for {round(distance, 2)} miles:\n")
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
