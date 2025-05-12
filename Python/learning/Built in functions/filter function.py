# ----------------------------------
# -- Built In Functions => Filter --
# ----------------------------------
# [1] Filter Take A Function + Iterator
# [2] Filter Run A Function On Every Element
# [3] The Function Can Be Pre-Defined Function or Lambda Function
# [4] Filter Out All Elements For Which The Function Return True
# [5] The Function Need To Return Boolean Value
# ---------------------------------------------------------------

# Example 1

def checkNumber(num):

  return num > 10 # Check if the number is greater than 10
# If the number is greater than 10, return True, else return False

myNumbers = [0, 0, 1, 19, 10, 20, 100, 5, 0]

myResult = filter(checkNumber, myNumbers)   # Filter the numbers that are greater than 10
# The filter function will return an iterator object that contains the numbers that are greater than 10

for number in myResult:

  print(number) # Print the numbers that are greater than 10
# The result will be 19, 20, 100

print("#" * 50)

# Example 2

def checkName(name):

  return name.startswith("O") # Check if the name starts with "O"
# If the name starts with "O", return True, else return False

myTexts = ["Osama", "Omer", "Omar", "Ahmed", "Sayed", "Othman"]

myReturnedData = filter(checkName, myTexts) # Filter the names that start with "O"
# The filter function will return an iterator object that contains the names that start with "O"

for person in myReturnedData:

  print(person) # Print the names that start with "O"
# The result will be Osama, Omer, Omar, Othman

print("#" * 50)

# Example 3

myNames = ["Osama", "Omer", "Omar", "Ahmed", "Sayed", "Othman", "Ameer"]

for p in filter(lambda name: name.startswith("A"), myNames): # Filter the names that start with "A"
  # The filter function will return an iterator object that contains the names that start with "A"

  print(p) # Print the names that start with "A"
# The result will be Ahmed, Ameer

print("#" * 50)
# Example 4
myNumbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
myResult = filter(lambda x: x*2+5 > 10, myNumbers) # Filter the numbers that are greater than 10
for i in myResult:
    print(i) # Print the numbers that are greater than 10
    

    