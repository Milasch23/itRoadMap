# We define the operation functions
def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b): #This one is different, so we can avoid a zero division
    if b == 0:
        raise ValueError("Error: zero division is not allowed.") 
    return a / b
    
# Menu function
def show_menu():
    print("\n" + "*-"*35)
    print("CLI Calculator")
    print("="*35)
    print("""
          1. Addition
          2. Subtraction
          3. Multiplication
          4. Division
          0. Exit""")
    print("="*35)

# We define a function for the choice. It accepts a message as a parameter.
def ask_num(message):
    while True:
        try:
            return float(input(message))
        except ValueError:
            print("Please, enter a valid number")

# Main function
def main():
    print("Welcome to my CLI Calculator!")

    while True:
        show_menu() #We first call the menu function
        option = input("Choose the math operation: ").strip() #We use the strip function to remove spaces

        # If statement that ends the program if the user types 0
        if option == "0":
            print("See you later!")
            break

        # If statement that validates the choice
        if option not in ["1", "2", "3", "4"]:
            print("Invalid option. Try again.")
            continue
        
        # We call the choice function, and save the results in two different variables
        a = ask_num("Type the first number: ")
        b = ask_num("Type th second number: ")

        try:
            # if - elif statement for operation function calls
            if option == "1":
                result = addition(a, b)
                symbol = "+"

            elif option == "2":
                result = subtraction(a, b)
                symbol = "-"

            elif option == "3":
                result = multiplication(a, b)
                symbol = "*"

            elif option == "4":
                result = division(a, b)
                symbol = "/"

            print(f"\n {a} {symbol} {b} = {result}")
        
        except ValueError as e:
            print(f"\n {e}")

# Finally, we call the main function
if __name__ == "__main__":
    main()