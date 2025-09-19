emp_tuple = (100, 'Bhavya', 'Dhiman', 'Chandigarh', True, 'CSE')
print("Tuple:", emp_tuple)

emp_list = list(emp_tuple)
print("List:", emp_list)

emp_list.append('Incredible')
print("List after append:", emp_list)
print("Size of appended list:", emp_list.__sizeof__())

emp_tuple = tuple(emp_list)
print("Tuple after converting back from list:", emp_tuple)
print("Size of appended tuple:", emp_tuple.__sizeof__())