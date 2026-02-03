# VARIABLES

x = 10        #
y = 13        # # You create a variable the moment you asign a value to it
z = "Alpha"   #

a = "Alpha"   # You can change the type
b = 1         # anytime you need

c = int(34)   # You can specify the type tho
d = float(40)

print(type(x))  # That's how you can get the data type of a variable
print(type(z))

E = "Toy"  # Variables are case sensitive
e = "Beta"
PI = 3.1416  # If the name is in uppercase, then it's a constant. You must NOT change its value
# Never. Even if Python allows you to do so

###########################################################################################

# DATA TYPES

# Text Type:	str
f = "Fruit"

# Numeric Types:	int, float, complex
g = 56
h = 12, 45
i = 5j

# Sequence Types:	list, tuple, range
j = ["Juice", "Jewel", "Jar"]
k = (34, 1.23, "Koala")
l = list(range(6))

# Mapping Type:	dict
m = {"Key1": 1,
     "Key2": 3,
     "Key3": 6}

# Set Types:	set, frozenset
some_things = {"Roses", "Bread", "Chocolate", "Iron Bar"}
frozenset(some_things)

# Boolean Type:	bool
o = False
p = 6 >= 4

# Binary Types:	bytes, bytearray, memoryview
q = b"Hi"
bytearray(123)
r = memoryview(q)

# None Type:	NoneType
s = None
