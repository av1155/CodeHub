# Main function
def main():

    print("\nAndrea A. Venti Fuentes")

    first_input = get_starting_num_organisms()
    print()
    second_input = get_daily_population_increase()
    print()
    third_input = get_days_to_multiply()
    print()

    print("\nDay\t\t Approximate Population")
    for day in range(1, (third_input + 1)):
        print(f"{day} \t\t {round(first_input, 5)}")
        first_input *= second_input


def get_starting_num_organisms():

    # The input below records the starting number of organisms.
    starting_num_organisms = int(
        input("Enter the starting number of organisms: "))
    # The while loop below validates the input and requests the user to input a new value if the number is negative or zero.
    while starting_num_organisms <= 0:
        starting_num_organisms = int(input(
            "Negative values or zero for the starting number of organisms is not allowed. Please re-enter the starting number of organisms: "))
    return starting_num_organisms


def get_daily_population_increase():

    # The input below records the average daily population increase.
    daily_population_increase = float(input(
        "Enter the average daily population increase (number will be translated to percent value, for example, 30 means 30%): "))
    # The while loop below validates the input and requests the user to input a new value if the numbers are either negative or larger than 100.
    while (daily_population_increase < 0) or (daily_population_increase > 100):
        daily_population_increase = float(input(
            "Negative values or values larger than 100 are not allowed. Please re-enter the average daily population increase: "))

    daily_population_increase = ((daily_population_increase + 100) / 100)

    return daily_population_increase


def get_days_to_multiply():

    # The input below records the number of days that the organisms will be left to multiply for.
    days_to_multiply = int(
        input("Enter the number of days the organism will multiply for: "))
    # The while loop below validates the input and requests the user to input a new value if the numbers are either negative, zero, or larger than 30.
    while (days_to_multiply <= 0) or (days_to_multiply > 30):
        days_to_multiply = int(input(
            "Negative values, zero, or values larger than 30 are not allowed. Please re-enter the number of days the organism will be left to multiply for: "))
    return days_to_multiply


main()  # Very last statement in code
