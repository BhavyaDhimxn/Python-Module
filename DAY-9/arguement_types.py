# Different Types of Arguments in Python

# 1. Positional Arguments
# These are arguments passed to a function in the correct order.
def greet_positional(name, age):
    print(f"Hello, {name}! You are {age} years old.")

# Example call
greet_positional("Alice", 25)

# 2. Keyword Arguments
# These are arguments passed using the parameter names.
def greet_keyword(name, age):
    print(f"Hello, {name}! You are {age} years old.")

# Example call
greet_keyword(age=30, name="Bob")

# 3. Default Arguments
# These have default values if not provided.
def greet_default(name, age=18):
    print(f"Hello, {name}! You are {age} years old.")

# Example calls
greet_default("Charlie")  # Uses default age
greet_default("David", 40)  # Overrides default age

# 4. Variable-length Arguments (*args)
# Allows a function to accept any number of positional arguments.
def greet_multiple(*names):
    for name in names:
        print(f"Hello, {name}!")

# Example call
greet_multiple("Eve", "Frank", "Grace")

# 5. Keyword Variable-length Arguments (**kwargs)
# Allows a function to accept any number of keyword arguments.
def greet_with_info(**info):
    for key, value in info.items():
        print(f"{key}: {value}")

# Example call
greet_with_info(name="Henry", age=35, city="New York")

# Combined example: Function with all types
def complex_function(name, age, *hobbies, city="Unknown", **extra):
    print(f"Name: {name}, Age: {age}, City: {city}")
    print(f"Hobbies: {', '.join(hobbies)}")
    for key, value in extra.items():
        print(f"{key}: {value}")

# Example call
complex_function("Ivy", 28, "reading", "swimming", city="London", profession="Engineer", favorite_color="Blue")
