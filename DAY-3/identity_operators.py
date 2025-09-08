# identity_operators.py

# Define two variables
a = [1, 2, 3]
b = a
c = [1, 2, 3]

# Check identity using 'is' and 'is not'
print("a is b:", a is b)        # True, because b references the same object as a
print("a is c:", a is c)        # False, because c is a different object
print("a is not c:", a is not c)  # True, because a and c are different objects