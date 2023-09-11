# Print 1 .. 100
# print Fizz if divisible by 3
# print Buzz if divisible by 5
# print FizzBuzz if divisible by 3 and 5

for n in range(1, 101):
    if n % 3 == 0:
        print("Fizz", end=" ")
    elif n % 5 == 0:
        print("Buzz", end=" ")
    elif (n % 3 == 0) and (n % 5 == 0):
        print("FizzBuzz", end=" ")
    else:
        print(n, end=" ")

print()
print()

i = 0
while i < 100:
    i += 1
    if i % 3 == 0:
        print("Fizz", end=" ")
    elif i % 5 == 0:
        print("Fuzz", end=" ")
    elif (i % 3 == 0) and (i % 5 == 0):
        print("FizzFuzz", end=" ")
    elif (i % 3 != 0) and (i % 5 != 0):
        print(i, end=" ")
