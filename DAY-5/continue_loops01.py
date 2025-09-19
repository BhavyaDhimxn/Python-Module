salary = [1000, 2000, -2500, 3000, 4000, -7000, 5000]

totalSalary = 0

for i in salary:
    if i < 0:
        continue # skip the negative values and continue with the next iteration
    totalSalary += i
    currentTotalSalary = totalSalary
    print("Current Total Salary:", currentTotalSalary)
print("Total Salary:", totalSalary)