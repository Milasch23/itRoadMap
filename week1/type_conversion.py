# Implicit Type Conversion
# Happens automatically
a = 13
b = 14.6
c = 0
c += (a + b)

print(f"a: {type(a)}")
print(f"b: {type(b)}")
print(c)
print(f"c: {type(c)}")

# Explicit Type Conversion (type casting)
d = "14"
print(type(d))

e = int(d)
print(type(e))

# Some examples

# Binary String
f = "101110"
g = int(f, 2)
print(g)

# ASCII, Hexadecimal and Octal
h = "7"
print(ord(h))
print(hex(34))
print(oct(34))

# String to Tuple, Set and List
i = "User information"
print(tuple(i))
print(set(i))
print(list(i))
