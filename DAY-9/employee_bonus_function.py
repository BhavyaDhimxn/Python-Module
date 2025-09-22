def employeeBonus(salary, rating):
    if rating == 3:
        bonus = salary * 0.03
    elif rating == 4:
        bonus = salary * 0.04
    elif rating == 5:
        bonus = salary * 0.05
    else:
        bonus = 0
    return bonus

def inputTaker():
    salary = float(input("Enter the employee's salary: "))
    rating = int(input("Enter the employee's performance rating (1-5): "))
    return salary, rating

while True:
    salary, rating = inputTaker()
    bonus = employeeBonus(salary, rating)
    print(f"The employee's bonus is: {bonus}")

    calculate_again = input("Do you want to calculate again? (yes/no): ")
    if calculate_again != 'yes':
        break
