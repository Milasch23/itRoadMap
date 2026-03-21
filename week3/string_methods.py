import re

# STRING METHODS

# F-Strings 
name = "Cinthia"
age = 27

print(f"Name: {name}, Age: {age}")


# Numerical accuracy and dynamic alignment
pi = 3.14159265359
width = 10
accuracy = 4

print(f"Pi to the nearest digit: {pi:{width}.{accuracy}}")


# Currency format
price = 45189.50

print(f"Price: ${price:,.2f}")


# Self-documentation with =
x = 10
y = [2, 4, 6]

print(f"{x = }, {y = }") # Great for debugging


# !r and !s flags
text = "Hello World!"

print(f"repr: {text!r}")
print(f"str: {text!s}")


# Multi-line F-strings
message = (
    f"Hello, i'm {name}. "
    f"Pi value: {pi:4.3}. "
    f"I'm learning Python"
)

print(message)



# Advanced Essential Methods

# join()
words = ["Hello", "all", "welcome"]
phrase = " ".join(words)
print(phrase)

# More uses
csv_line = ", ".join(["George", "25", "Italy"])
print(csv_line)


# split()
data = "name:surname:age"
parts = data.split(":", maxsplit = 2)
print(parts)



# Alignment and filling

# With String methods
text2 = "Photography"
print(text2.center(23, '*'))
print("48".zfill(6))


# With format specifiers
name2 = "Annabele"
print(f"|{name2:<15}|")
print(f"|{name2:&^14}|")



# Text Transformations

text3 = "world OF warcraft"
print(text3.upper())
print(text3.lower())
print(text3.title())
print(text3.capitalize())
print(text3.swapcase())



# String cleaning
text4 = "    Hello All!    "
print(text4.strip())


# Strip with specific characters
data2 = "$$$Price$$$"
print(data2.strip("$"))


# Replace
print(text4.replace("All", "World"))



# RegEx
text5 = "My phone number is 123-4567-890 and 1234567890 too"

# Find all the numbers
numbers = re.findall(r'\d+', text5)
print(numbers)


# Replace with a pattern
result = re.sub(r'\d{3}-\d{3}-\d{3}', 'XXX-XXX-XXX', text5)
print(result)


# Split by multiple delimiters
data3 = "one,two;three|four"
parts2 = re.split(r'[,;|]', data3)
print(parts2)

