# LISTS 
# Are mutable

various_list = [True, 2.5, 123, "Hello", 67j] # Can contain various data types

# Create a list 
flowers = ["Rose", "Sunflower", "Tulip", "Lavender"]
print(flowers)

# Index access
print(flowers[2]) # Result = Tulip

# Modify an element
flowers[3] = "Orchid"
print(flowers)

# Adding elements
flowers.append("Lotus") #at the end
flowers.insert(2, "Daisy") #in position 2
print(flowers)

# Deleting elements
flowers.remove("Rose") #by valor
last = flowers.pop() #by index (the last element by default)


# TUPLES
# Ordered and immutable
# You cannot change elements

various_tuple = (False, 4.4, 654, "World", 11j) # Same as lists

# Create a tuple
numbers = (12, 56, 1, 0, 23, 44)
print(numbers)

w_o_parentheses = 5, 3, 8
print(w_o_parentheses)

single_item = (4,) # <<-- The comma is essential

# Index access 
fruits = ("apple", "cherry", "banana", "grapes")
print(fruits[0:2])

#Unpacking a tuple
(green, red, yellow, purple) = fruits
print(yellow)


