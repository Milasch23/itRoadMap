def modulus(a, b):
    if b == 0:
        raise ValueError("Error: zero division is not allowed.") 
    return a % b

def exponentiation(a, b):
    return a ** b

def floor_div(a, b):
    if b == 0:
        raise ValueError("Error: zero division is not allowed.") 
    return a // b

