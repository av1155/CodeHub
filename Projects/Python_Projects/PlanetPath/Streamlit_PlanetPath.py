import sys
import streamlit as st
from geopy.geocoders import Nominatim
from geopy.distance import geodesic


def get_distance(place1, place2):
    # Create a geocoder object
    geolocator = Nominatim(user_agent="my-app")

    # Geocode the place names to get their coordinates

    location1 = geolocator.geocode(place1)
    location2 = geolocator.geocode(place2)

    # Calculate the distance between the two coordinates using geodesic distance

    # if location1 is an existing attribute do this

    distance = geodesic((location1.latitude, location1.longitude),
                        (location2.latitude, location2.longitude)).miles

    return distance


def walking(distance):
    emissions = distance * 404
    points = round(distance * 10)
    st.write(
        f"\nYou just saved {round(emissions, 2)} grams of CO2 emissions by walking {round(distance, 2)} miles with PlanetPath. Keep up the good work for a greener planet!")
    st.write(
        f"\nYou've earned {points} points for walking {round(distance, 2)} miles with PlanetPath!")

    exit()


def biking(distance):
    emissions = distance * 404
    points = round(distance * 10)
    st.write(
        f"\nYou just saved {round(emissions, 2)} grams of CO2 emissions by biking {round(distance, 2)} miles with PlanetPath. Keep up the good work for a greener planet!")
    st.write(
        f"\nYou've earned {points} points for biking {round(distance, 2)} miles with PlanetPath!")
    exit()


def bus(distance):
    emissions = distance * 209
    points = round(distance * 5)
    st.write(f"\nYou just saved {round(emissions, 2)} grams of CO2 emissions by using the bus for {round(distance, 2)} miles with PlanetPath. Keep up the good work for a greener planet!")
    st.write(
        f"\nYou've earned {points} points for using the bus for {round(distance, 2)} miles with PlanetPath!")
    exit()


def ride_share(distance):
    number_of_people = st.text_input(
        ("How many people are in the car with you?\n> "))
    number_of_people = int(number_of_people)

    emissions = distance * 404
    total_emissions = emissions / number_of_people
    points = round(distance * 3)
    st.write(
        f"\nEach passenger saved {round(total_emissions, 2)} grams of CO2 emissions by using ride share for {round(distance, 2)} miles with PlanetPath. Keep up the good work for a greener planet!")
    st.write(
        f"\nYou've earned {points} points for using ride share for {round(distance, 2)} miles with PlanetPath!")
    exit()


def main():
    try:
        sys.tracebacklimit = 0  # Turn off traceback error message
        st.set_page_config(
            page_title="PlanetPath",
            page_icon=":earth_africa:",
            layout="wide",
        )
        logo = 'https://green-transfer.fr/wp-content/uploads/2019/08/Green_Leaf_Earth_PNG_Clipart-2978.png'

        st.image(logo, width=365)
        st.title("PlanetPath")

        while True:
            try:
                # Prompt user to enter place names
                place1 = st.text_input("\nWhat is your starting point? ")
                if place1 == 'exit':
                    sys.exit()

                place2 = st.text_input("\nWhat is your destination? ")
                if place2 == 'exit':
                    sys.exit()

                # Get the distance between the two places
                distance = get_distance(place1, place2)

                # Display CO2 emissions and points for each transportation option
                st.write(
                    f"\nCO2 emissions and points for {round(distance, 2)} miles:\n")
                st.write(
                    f"1) Walking: {round(distance * 404, 2)} grams of CO2 emissions, {round(distance * 10)} points")
                st.write(
                    f"2) Biking: {round(distance * 404, 2)} grams of CO2 emissions, {round(distance * 10)} points")
                st.write(
                    f"3) Bus: {round(distance * 209, 2)} grams of CO2 emissions, {round(distance * 5)} points")
                st.write(
                    f"4) Ride share: {round(distance * 404, 2)} grams of CO2 emissions potentially saved by all passengers, {round(distance * 3)} points")

                # Prompt user to choose transportation option
                choice = st.text_input(
                    "\nPlease choose a transportation option (1-4): ")
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
                    st.write("Invalid choice. Please choose a number from 1-4.")

            except ValueError:
                pass
    except:
        pass


if (__name__ == "__main__"):
    main()
