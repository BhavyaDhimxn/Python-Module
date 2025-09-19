emp_db = [100, 'Bhavya', 'Dhiman', 'Chandigarh', True, 'CSE']

print(emp_db)
print("Total Length of list:", len(emp_db)) # len() is a method that returns the length of the list

emp_db.append(500106947)
print(emp_db)
print("Total Length of list:", len(emp_db))

emp_db.insert(3, 'Fresher')
print(emp_db)
print("Total Length of list:", len(emp_db))

emp_db.extend(['Cloud Computing', 'DevOps'])
print(emp_db)
print("Total Length of list:", len(emp_db))

emp_db.remove('Dhiman')
print(emp_db)
print("Total Length of list:", len(emp_db))

emp_db.pop() # removes the last element
print(emp_db)
print("Total Length of list:", len(emp_db))

del emp_db[0]
print(emp_db)
print("Total Length of list:", len(emp_db))

