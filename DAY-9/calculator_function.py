def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by 0"
    return a / b

def inputTaker():
    a = float(input("Enter the first number: "))
    b = float(input("Enter the second number: "))
    operation = input("Enter the operation (+, -, *, /): ")

    return a, b, operation

while True:
    a, b , operation = inputTaker()

    if operation == '+':
        result = add(a, b)
    elif operation == '-':
        result = subtract(a, b)
    elif operation == '*':
        result = multiply(a, b)
    elif operation == '/':
        result = divide(a, b)
    else:  
        result = "Error: Invalid operation"

    print(f"The result is: {result}")

    calculate_again = input("Do you want to calculate again? (yes/no): ")
    if calculate_again != 'yes':
        break