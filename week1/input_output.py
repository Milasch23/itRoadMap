name = input("Please, enter your name: ")
print(f"Hello, {name}")
# The function 'input' always returns a String
# If we need a different type of data, we have to convert it

age = int(input("Now, enter your age: "))
height = input("Enter your height: ")

print(type(age))
print(type(height))  # type() to determine the data type of a variable

# printing multiple variables
print(name, age, height)

# Taking multiple inputs
# split() always returns a String
a, b, c = input("Enter two values: ").split()
print(a)
print(b)
print(c)
