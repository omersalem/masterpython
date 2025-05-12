# ------------------------
# -- Built In Functions --
# ------------------------
# all() # Check if all elements in an iterable are true
# any() # Check if any element in an iterable is true
# bin() # Convert an integer to its binary representation
# id() # Get the memory address of an object
# iterable should be a list, tuple, set, or any other iterable object

x = [1, 2, 3, 4, []]  # A list containing integers and an empty list

if all(x):  # Checks if all elements in the list are truthy
  print("All Elements Is True")  # Prints if all elements are truthy
else:
  print("Theres At Least One Element Is False")  # Prints if at least one element is falsy

x = [0, 0, []]  # A list containing zeros and an empty list
# 0: The integer 0 is considered falsy in Python.
# 0 (again): The second 0 is also falsy for the same reason.
# []: An empty list is considered falsy in Python because it is empty (has no elements).

if any(x):  # Checks if at least one element in the list is truthy
  print("There's At Least One Element is True")  # Prints if any element is truthy
else:
  print("Theres No Any True Elements")  # Prints if all elements are falsy

print(bin(100))  # Converts the integer 100 to its binary representation and prints it

a = 1  # Assigns the value 1 to variable 'a'
b = 2  # Assigns the value 2 to variable 'b'

print(id(a))  # Prints the memory address of the variable 'a'
print(id(b))  # Prints the memory address of the variable 'b')

