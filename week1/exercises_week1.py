# # 1 - Temperature Converter (Cº to Fº)
celsius = 12.5
fahrenheit = (celsius * (9/5)) + 32

print(f"Temperature in Celsius: {celsius} Cº \nTemperature in Fahrenheit: {fahrenheit} Fº")
print()
print("x-" * 20)
print()

# # 2 - User Bio
name = "Alan"
age = 32
city = "Oklahoma"
height_in_m = 1.78

print(f"User: {name} \nAge: {age} \nCity: {city} \nHeight(mts): {height_in_m}")
print()
print("x-" * 20)
print()

# # 3 - Age calculator
age = input("Please enter your birth year: ")
years_old = 2026 - int(age)

print(f"You are {years_old} years old")
print()
print("x-" * 20)
print()

# # 4 - Shopping Total
a, b, c = input("Please enter the price of three items (Separated by a space): ").split()
total_price = float(float(a) + float(b) + float(c))
print(f"The total price is {total_price:.2f}")
print()
print("x-" * 20)
print()

# # 5 - Number manipulator
number = input("Please enter a number: ")
res = int(number) + 10 * 3 / 7
print(f"The final result is: {res}")
print()
print("x-" * 20)
print()

# # 6 - Even or Odd
number2 = int(input("Please enter a number (Integer): "))
if number2 % 2 == 0:
    print(f"The number {number2} is even")
else:
    print(f"The number {number2} is odd")
print()
print("x-" * 20)
print()

# # 7 - Grade Calculator
grade = float(input("Please enter the score (Between 0-100): "))
if grade >= 90 and grade <= 100:
    print("Final grade: A")
elif grade >= 80 and grade <= 89.9:
    print("Final grade: B")
elif grade >= 70 and grade <= 79.9:
    print("Final grade: C")
elif grade >= 60 and grade <= 69.9:
    print("Final grade: D")
elif grade >= 0 and grade <= 59.9:
    print("Final grade: F")
elif grade < 0 or grade > 100:
    print("Please enter a valid score")

# 8 - Sum of even numbers
random_number = int(input("Please enter a random number (integer): "))
boxie = 0

for i in range(random_number + 1):
    if i % 2 == 0: 
        boxie += i

print(boxie)

# 9 - FizzBuzz
random_number2 = int(input("Please enter a random integer number: "))
for i in range(random_number2 + 1):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")

# 10 - Palindrome Checker 
# This one was the most chalenging. 
# At first i tried to use a while loop to compare characters from both ends of the string. 
# But then I decided to use string slicing

word = input("Please enter a word: ").lower()

if word == word[::-1]:
    print(f"{word.capitalize()} is a palindrome")
else:
    print(f"{word.capitalize()} is not a palindrome")