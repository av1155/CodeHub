import datetime as dt

import requests


def kelvin_to_celsius_and_fahrenheit(kelvin):
    celsius = kelvin - 273.15
    fahrenheit = celsius * (9 / 5) + 32
    return celsius, fahrenheit


def wind_speed_conversion(wind_speed):
    meters_per_second_to_miles_per_hour = wind_speed * 2.237
    meters_per_second_to_kilometers_per_hour = wind_speed * 3.6
    return meters_per_second_to_miles_per_hour, meters_per_second_to_kilometers_per_hour


def main():
    BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"
    API_KEY = open("Weather_App/api_key.txt", "r").read()
    CITY = "Coral Gables"
    URL = BASE_URL + "appid=" + API_KEY + "&q=" + CITY

    response = requests.get(URL).json()

    temp_kelvin = response["main"]["temp"]
    temp_celsius, temp_fahrenheit = kelvin_to_celsius_and_fahrenheit(temp_kelvin)

    feels_like_kelvin = response["main"]["feels_like"]
    feels_like_celsius, feels_like_fahrenheit = kelvin_to_celsius_and_fahrenheit(
        feels_like_kelvin
    )

    wind_speed = response["wind"]["speed"]
    wind_speed_mph, wind_speed_kmh = wind_speed_conversion(wind_speed)

    humidity = response["main"]["humidity"]
    clouds = response["weather"][0]["main"]
    clouds_description = response["weather"][0]["description"]
    sunrise_time = dt.datetime.utcfromtimestamp(
        response["sys"]["sunrise"] + response["timezone"]
    )
    sunset_time = dt.datetime.utcfromtimestamp(
        response["sys"]["sunset"] + response["timezone"]
    )

    print(f"\nWeather in {CITY}:\n")
    print(f"Celsius: {temp_celsius:.2f}°C\t\t | Fahrenheit: {temp_fahrenheit:.2f}°F")
    print(
        f"Feels Like: {feels_like_celsius:.2f}°C\t\t | Feels Like: {feels_like_fahrenheit:.2f}°F"
    )
    print(f"Humidity: {humidity:.0f}%")
    print(f"Weather: {clouds} ({clouds_description})")
    print(
        f"Wind Speed: {wind_speed_kmh:.2f} KM/H\t\t | Wind Speed: {wind_speed_mph:.2f} MP/H"
    )
    print(f"Sunrise: {sunrise_time}")
    print(f"Sunset: {sunset_time}")


if __name__ == "__main__":
    main()
