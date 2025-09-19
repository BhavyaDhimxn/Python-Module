emp_tuple = (100, 'Bhavya', 'Dhiman', 'Chandigarh', True, 'CSE')
print("Original Tuple:", emp_tuple)

emp_tuple = (emp_tuple[0], 'Asmita') + emp_tuple[2:]
print("Tuple after reassignment:", emp_tuple)