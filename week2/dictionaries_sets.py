# DICTIONARIES
# Ordered collection, changeable. Doesn't allow duplicates

dinosaurs = {
    "T-rex": 2,
    "Triceratops" : 1,
    # "T-rex": 3 <<-- it will take the last key-value, it won't repeat the duplicate 
}
print(dinosaurs)

# Showing items
print(dinosaurs["T-rex"])

# We can store any data type 
cars = {
    "Name": "Nissan Frontier",
    "Type": "Xgear",
    "Year": 2023,
    "Key Words" : ["4x4", "Sport", 2.3, 7]
}

# type = object with the data type 'dict'
print(type(cars))

# Making a dict with the dict() constructor
agenda = dict(name = "John", age = 45, number = 1234455)
print(agenda)



# SETS
"""
Used to store items: 
   - Not duplicated
   - Unordered
   - Mutable
   - Hashing
 """

numbers = {3, 6, 1, 89, 5, 10}
print(numbers)
print(type(numbers))

# Converting other data types into sets
abcList = set(["a", "b", "c", "d"])
print(abcList)

# Adding elements
abcList.add("x")
print(abcList)

# A set cannot have duplicate values
phrase = {"Hello", "World", "Hello"}
print(phrase)

# Set values cannot be changed
# phrase[2] = "!"
print(phrase)

# Storing different data types in a set
dataDif = {"Hello", 67j, 23.5, True}
print(dataDif)

# Frozen Set
fs = frozenset(["Lion", "Giraffe", 12])

# Methods for Sets
letters1 = {"ad", "aa", "ab"}
letters2 = {"af", "ag", "ah", "ai", "aa", "ab"}

letters1.add("ae")

union1 = letters1.union(letters2)
print(union1)

inter1 = letters1.intersection(letters2)
print(inter1)

difference = letters1.difference(letters2)
print(difference)

s = {1, 3, 5}
s.clear()
print(s)


