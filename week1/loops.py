# LOOPS
# For Loop

for i in range(5):
    print(i)

list1 = ["Hello", "World", 2026]
for i in list1:
    print(i)

phrase = "Hello World 2026"
for i in phrase:
    print(i)

dicti = {"a": 123,
         "b": 456,
         "c": 789}

for i in dicti:
    print("%s: %d" % (i, dicti[i]))


#While Loop
c = 0
while c <= 3: # 0, 1, 2, 3 <-- That's why we have four 'AbC'
    c += 1 # This is crucial if we don't want an infinite loop
    print("AbC")


# Nested loops
for i in range(1, 5):
    for j in range(i):
        print(i, end=' ')
    print()

rows = int(input("Enter the row size for the pattern: "))
for i in range(rows, 0, -1):
    for j in range(1, i + 1):
        print("A", end = " ")

# Continue Statement = skips the current iteration
for letter in phrase:
    if letter == "e" or letter == "o":
        continue
    print(letter)

print("")

# Break Statement = exits the loop prematurely if a specified condition is met
for letter in phrase:
    if letter == "w" or letter == "W":
        break
    print(letter)

# Pass Statement = iterates over, but doesn't perform any operation
for letter in phrase:
    pass
print(letter)

