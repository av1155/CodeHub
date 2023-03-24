print("\nAndrea A. Venti Fuentes")  # Student's Full Name
print("aav66@miami.edu")  # Student's Email
print("CSC 115: Python Programming for Everyone")  # Course
print("B.S. in Computer Science\n")  # Student's Major

# The input below records the starting number of organisms.
starting_num_organisms = int(input("Enter the starting number of organisms: "))
# The while loop below validates the input and requests the user to input a new value if the number is negative or zero.
while starting_num_organisms <= 0:
    starting_num_organisms = int(input(
        "Negative values or zero for the starting number of organisms is not allowed. Please re-enter the starting number of organisms: "))
print()

# The input below records the average daily population increase.
daily_population_increase = float(input(
    "Enter the average daily population increase (number will be translated to percent value, for example, 30 means 30%): "))
# The while loop below validates the input and requests the user to input a new value if the numbers are either negative or larger than 100.
while (daily_population_increase < 0) or (daily_population_increase > 100):
    daily_population_increase = float(input(
        "Negative values or values larger than 100 are not allowed. Please re-enter the average daily population increase: "))

# The equation below converts the daily population increase value into a positive multiplication percentage so it can be used later in the program.
# For example, 30 + 100 = 130, dividing 130 by 100 = 1.3
# This number becomes the final percent multiplicator. For example: 1.3 * 2 = 2.6. That is a 30% increase to the original value.
daily_population_increase = ((daily_population_increase + 100) / 100)

print()

# The input below records the number of days that the organisms will be left to multiply for.
days_to_multiply = int(
    input("Enter the number of days the organism will multiply for: "))
# The while loop below validates the input and requests the user to input a new value if the numbers are either negative or larger than 30.
while (days_to_multiply < 0) or (days_to_multiply > 30):
    days_to_multiply = int(input(
        "Negative values or values larger than 30 are not allowed. Please re-enter the number of days the organism will be left to multiply for: "))
print()

# The print statement below prints the table header where the days and the approximate population will be displayed.
print("Day\t Approximate Population")

# The for loop below creates a range from 1 to the number of days that the organism will be left to multiply for.
# A +1 is added so that the range goes from 1 to the exact number, and not one less.
# For example, if the user inputs 3, the range will go from 1 to 3, not 1 to 2.
# The loop will run as many times as the number of days the organism will be left to multiply for.
# The loop will also print the day and the approximate population for each day.
# The population is calculated by multiplying the starting number of organisms by the daily population increase and continuously updating the value of the starting number of organisms.
# The population will be displayed with 5 decimal places for ease of reading and uniformity.

for days in range(1, (days_to_multiply + 1)):
    print(f"{days} \t {starting_num_organisms:.5f}")
    starting_num_organisms *= daily_population_increase

