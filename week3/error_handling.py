import os

# ERROR HANDLING

# Two Handling Error Philosophies

# 1. LBYL - Look Before You Leap
# Check if the file exists before deleting it 

if os.path.exists("file.txt"):
    os.remove("file.txt")
else:
    print("The file doesn't exist.")

# Caution: Race Conditions


# 2. EAFP - Easier to Ask Forgiveness than Permission
# Try the action first, then handle the error

try:
    os.remove("file.txt")
except FileNotFoundError:
    print("The file doesn't exist.")




# try / except / else / finally
try:
    result = 10 / int(input("Enter a number: "))

except ZeroDivisionError:
    print("You can't divide by zero")

except ValueError:
    print("Please, enter a valid number")

else:
    # This runs ONLY if NO exceptions have occurred
    print(f"Result: {result}")

finally:
    # It always runs, regardless of whether an exception occurs or not
    print("Operation complete")




# Handling Multiple Exceptions

# 1. Multiple except blocks
try:
    x = int("Abc")

except TypeError:
    print("Type Error")

except ValueError:
    print("Value Error")


# 2. Catching multiple exceptions in a single except block
def an_operation():
    return 10 / 0

try:
    result2 = an_operation()

except (TypeError, ValueError, ZeroDivisionError) as e:
    print(f"Error: {e}")


# 3. Catch any exceptions (only at the top level)

try:
    result3 = an_operation()

except Exception as e:
    print(f"Unexpected Error: {e}")




# Using raise
def division(a, b):
    if b == 0:
        raise ValueError("You can't divide by zero.")
    return a / b
    

# Re-raise an exception (while preserving the original traceback)
try: 
    result4 = division(10, 0)

except ValueError as e:
    print(f"Catch: {e}")
    raise




# Custom Exceptions

# Simple
class InsufficientFundsError(Exception):
    pass


# Custom with atributes
def __init__(self, host, port, message):
    self.host = host
    self.port = port
    super().__init__(f"Unable to connect to {host}: {port} - {message}")


# Exception hierarchy

class AppError(Exception):
    # Base class for app errors
    pass

class ValidationError(AppError):
    pass

class AuthError(AppError):
    pass


# Using custom exceptions
def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientFundsError(f"You tried to withdraw ${amount}, but there is only ${balance}.")
    return balance - amount

try:
    new_balance = withdraw(100, 200)

except InsufficientFundsError as e:
    print(f"Error: {e}")

