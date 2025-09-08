first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
subject = input("Enter your subject: ")
print("Hello {0} {1}! Welcome to {2} class.".format(first_name, last_name, subject)) # Using str.format() method
print(f"Hello {first_name} {last_name}! Welcome to {subject} class.") # Using f-string (formatted string literals)