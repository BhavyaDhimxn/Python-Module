name = "BHAVYA" # this is a collection of characters
for i in name: # i is a variable that takes the value of each character in the string one by one
    print(i) # default row delimiter
print("Loop Completed!")

for i in name: # i is a variable that takes the value of each character in the string one by one
    print(i, end=" ") # end is a parameter that is used to change the default behavior of print function
print("\nLoop Completed!")

names = "Bhavya,Srishti,Bindiya,Asmita,Vikram,Leo"
nameslist = names.split(",") # split() is a method that splits a string into a list based on the delimiter provided

print(nameslist)
for i in nameslist:
    print(i)
print("Loop Completed!")