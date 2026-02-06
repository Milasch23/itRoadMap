# # CONDITIONALSs

# # If conditional statement

age = int(input("Please enter your age: "))
if age >= 16:
    print("You can vote.")

# # Short hand version

if age >= 16:
    print("You can vote")


# # If-else conditional statement

number = int(input("Please enter a number: "))
if number % 2 == 0:
    print(f"The number {number} is even.")
else:
    print(f"The number {number} is odd.")

# # Short hand version

grade = 69
result = "Pass" if grade >= 60 else "Fail"
print(f"Result: {result}")


# # elif Statement
wed_anniv = int(input("How long have you been married?: "))
if wed_anniv == 1:
    print("Paper Wedding")
elif wed_anniv == 2:
    print("Cotton Wedding")
elif wed_anniv == 3:
    print("Leather Wedding")
elif wed_anniv < 1:
    print("You must have been married for at least a year!")
else:
    print("Please, wait for future updates!")


# # Nested if-else conditional statement
number2 = float(input("Please, enter a number: "))

if number2 == 0:
    print("It's a Zero")
else:
    if number2 <= -1:
        print("The number entered is less than zero.")
    elif number2 >= 1:
        print("The number entered is greater than zero.")

# # Match case statement

match number2:
    case 1:
        print("It's a one")
    case 2:
        print("It's a two")
    case _:  # _always goes as the last case: is a default case
        print("It's another number")

# # Combine values

day = int(input("Please enter a number from 1 to 7: "))
match day:
    case 1 | 2 | 3 | 4 | 5:
        print("Day of a week")
    case 6 | 7:
        print("Weekend!")
    case _:
        print("¿?")

# Some exercises

# Temperature checker
temperature = float(input("Please enter the current temperature (In Celsius): "))
if temperature < 0:
    print("Freezing")
elif temperature >= 0 and temperature < 15:
    print("Cold")
elif temperature >= 15 and temperature < 25:
    print("Mild")
else:
    print("Hot")

# Leap Year Verifier
is_leap_year = int(input("Please enter the year: "))
if is_leap_year % 4 != 0:
    print(f"{is_leap_year} is not a leap year")
elif is_leap_year % 4 == 0 and is_leap_year % 100 != 0:
    print(f"{is_leap_year} is a leap year")
elif is_leap_year % 4 == 0 and is_leap_year % 100 == 0 and is_leap_year % 400 != 0:
    print(f"{is_leap_year} is not a leap year")
elif is_leap_year % 4 == 0 and is_leap_year % 100 == 0 and is_leap_year % 400 == 0:
    print(f"{is_leap_year} is a leap year")

# Simple calculator
a = float(input("Please, enter a value: "))
b = float(input("Now enter another value: "))
option = int(input("Please enter an option \n" \
"1: Addition \n" \
"2: Substraction \n" \
"3: Multiplication \n" \
"4: Division \n"))

match option:
    case 1:
        result = a + b
        print(f"The result is {result}")
    case 2:
        result = a - b
        print(f"The result is {result}")
    case 3:
        result = a * b
        print(f"The result is {result}")
    case 4:
        result = a / b
        print(f"The result is {result}")
    case _:
        print("Try again")

