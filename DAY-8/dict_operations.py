emp_db = {'Name': 'Bhavya', 'Surname': 'Dhiman', 'City': 'Chandigarh', 'Is_Employed': True, 'Department': 'CSE'}
print("Original Dictionary:", emp_db)
print("Type of emp_db:", type(emp_db))
print("Lenth of dictionary:", len(emp_db))

print("Keys:", emp_db.keys()) # Accessing all keys
print("Values:", emp_db.values()) # Accessing all values

print("Employee Name:", emp_db.get('Name')) # Accessing value using get() method
print("Employee Surname:", emp_db['Name']) # Accessing value using key

emp_db['Salary'] = 500106947 # Adding new key-value pair
print("Dictionary after add operation:", emp_db)

emp_db['Name'] = 'Asmita' # Modifying existing key-value pair
print("Dictionary after modify operation:", emp_db)

emp_db.pop('Is_Employed') # Removing key-value pair using pop() method
print("Dictionary after pop operation:", emp_db)

emp_db.popitem() # Removing last inserted key-value pair using popitem() method
print("Dictionary after popitem operation:", emp_db)
