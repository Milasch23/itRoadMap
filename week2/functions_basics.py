# FUNCTIONS

def salute_function(): 
    print("Hello World")

salute_function() # In this case, you must call the function

def add(parameterA, parameterB): # when you define a function, you set parameters
    return parameterA + parameterB

result = add(6, 5) # When you call the function, you set arguments
print(f"Result: {result}")


# Types of fuction arguments 

# Default arguments - we set a parameter value, and in the function call, the
# argument assumes that value if we don't provide a value.

def fun1(a, b = 10): # b has a default value
    return a + b

result2 = fun1(20)
result3 = fun1(30)

# 
print(f'''Result a: {result2}
Result b: {result3}
''')

# Keyword arguments 
def fun2(thing1, thing2):
    print(thing1, thing2)

# In this one, the order in which we pass the arguments doesn't matter, 
# as long we specify the parameters' names

fun2(thing1 = "Hello", thing2 = "World")
fun2(thing2 = "World", thing1 = "Hello")

# Positional arguments
def fun3(book, year):
    print(f"Book: {book}")
    print(f"Publication year: {year}")

# The values will be asigned based on their order in the function call

fun3("The Wheel of Time", 1990)
fun3(1990, "The Wheel of Time")

# Arbritary arguments
# Allow functions to accept a variable and undefined number of parameters

def sum_all(*args): # you use an asterisk * for positional arguments (collected in a tuple)
    return sum(args)

print(sum_all(12, 5, 3))

def show(**kwargs): # you use a double asterisk ** for keywords (collected in a dictionary)
    for key, valor in kwargs.items():
        print(f"{key}: {valor}")

# Function within functions
def a():
    message = "Hello World"
    def b(): # This one is an inner function
        print(message)
    
    b()

a()

#Annonymous Functions
# Simple-expresion functions that are created using the lambda keyword
# They don't require the def keyword or a return statement

def double_number(x): # normal function
    return x * 2

double_num = lambda x : x * 2

print(double_number(5))
print(double_num(5))    

# Return statement
# Ends a function and sends a value value back to the caller (like double_number())

# Difference between print() and return

def print_multi(a, b):
    print(a * b)

print_multi(4, 6) # This call will show the result, but won't be able to use that result later, because it will have the value None

def return_multi(a, b):
    return a * b

resultA = return_multi(4, 6) # In this case, I'm saving the result in a variable, which I will be able to use later on the code


# Pass by reference and by value
# It's different in Python, because it uses a hybrid mechanism 
# that depends on whether the object being passed is mutable or inmutable

# 1. Inmutable objects (int, str, tuple)
def modify_immutable(x):
    x += 10        # This creates a new integer object (x now points to it)
    print("Inside:", x)

a = 5
modify_immutable(a)
print("Outside:", a)

# Here, a is unchanged because inside the function, x was rebound to a new integer 15. The original a still points to 5

# 2. Mutable objects (list, dict, set)

def func(my_list):
    my_list.append(4) # Mutates the existing list object
    print(f"Inside func: {my_list}")

b = [1, 2, 3]
func(b)
print(f"Outside func: {b}")
# Output:
# Inside func: [1, 2, 3, 4]
# Outside func: [1, 2, 3, 4]


# Recursive functions
# It calls itself to solve a problem

def factorial(n):
    if n == 0:  
        return 1
    else:
        return n * factorial(n - 1) 
      
print(factorial(4))