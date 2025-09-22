def simpleCalculator(a, b, operation):

    if operation == '+':
        result = a + b
    elif operation == '-':
        result = a - b
    elif operation == '*':
        result = a * b
    elif operation == '/':
        if b == 0:
            result = "Error: Division by zero"
        else:
            result = a / b
    else:  
        result = "Error: Invalid operation"

    return result


def inputTaker():
    a = float(input("Enter the first number: "))
    b = float(input("Enter the second number: "))
    operation = input("Enter the operation (+, -, *, /): ")

    return a, b, operation

while True:

    a, b , operation = inputTaker()

    result = simpleCalculator(a, b, operation)

    print(f"The result is: {result}")

    calculate_again = input("Do you want to calculate again? (yes/no): ")
    if calculate_again != 'yes':
        break