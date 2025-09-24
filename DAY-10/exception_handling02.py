students = ["Alice", "Bob", "Charlie", "David", "Eve"]

def get_student_info(index):
    try:
        student = students[index]
        print(f"Student at index {index}: {student}")
    except (IndexError, ValueError) as e:
        print(f"Error: No student found at index {index}. Please provide a valid index between 0 and {len(students)-1}.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Taking input from user
user_input = int(input("Enter the index of the student you want to access: "))
get_student_info(user_input)
