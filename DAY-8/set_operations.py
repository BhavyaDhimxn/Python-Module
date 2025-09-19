emp_set = {100, 'Bhavya', 'Dhiman', 'Chandigarh', True, 'CSE', 100, 'Bhavya'}
print("Set:", emp_set)
print("The size of set:", emp_set.__sizeof__())

emp_set.add('Incredible')
print("Set after add:", emp_set)
print("Size of appended set:", emp_set.__sizeof__())

emp_set.remove('Dhiman')
print("Set after remove:", emp_set)
print("Size of set after remove:", emp_set.__sizeof__())

emp_set.discard('NonExistent')
print("Set after discard:", emp_set)
print("Size of set after discard:", emp_set.__sizeof__())

emp_set.update(['NewYork', 42])
print("Set after update:", emp_set)
print("Size of set after update:", emp_set.__sizeof__())

#to get distinct values from a list
emp_list = [100, 'Bhavya', 'Dhiman', 'Chandigarh', True, 'CSE', 100, 'Bhavya']
distinct_emp_set = set(emp_list)
print("Distinct Set from List:", distinct_emp_set)

