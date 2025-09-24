def validAge(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    elif age > 120:
        raise ValueError("Age seems unrealistic")
    else:
        return True

try:
    user_age = int(input("Enter your age: "))
    if validAge(user_age):
        print(f"Your age is {user_age}")

except ValueError as ve:
    print(f"Invalid age input: {ve}")
    
