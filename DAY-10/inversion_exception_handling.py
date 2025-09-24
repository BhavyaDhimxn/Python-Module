def inversion(n):
    return 1 / n

try: # Start of the try block to catch exceptions
    number = int(input("Enter your number: "))
    result = inversion(number)
    print(f"The inversion of {number} is {result}")

except ZeroDivisionError as e: # Handles division by zero error
    print("Error: Division by zero is not allowed.")
    print(f"Error Details: {e}")

except ValueError as e: # Handles invalid input that cannot be converted to integer
    print("Error: Invalid input. Please enter a valid integer.")
    print(f"Error Details: {e}")

except Exception as e: # Catch-all for any other exceptions
    print("An unexpected error occurred.")
    print(f"Error Details: {e}")

else: # This block executes if no exceptions were raised
    print("Inversion calculated successfully.")

finally: # This block always executes
    print("Execution completed.")    