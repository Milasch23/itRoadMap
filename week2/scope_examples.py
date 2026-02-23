# SCOPE
# It means that a variable is only available from inside the region where it was created


# Local Scope
def print_number():
    x = 120
    print(x) 

print_number()
# print(x) <<-- It will cause an error, cause x only exists in the previous function


# Global Scope
def f():
    print(s)

s = "Hello World" # This is a global variable, outside the function, and can be
# used by any part of the program

f()


#Global and Local variables with the same name
# This function has a variable with name same as s.
def salute():
    # print(y) <<-- this will cause an error 
    y = "Hi"
    print(y)

# Global scope
y = "Hello Everyone"
salute()
print(y)

