# ----------------
# -- Generators --
# ----------------
# [1] Generator is a Function With "yield" Keyword Instead of "return"
# [2] It Support Iteration and Return Generator Iterator By Calling "yield"
# [3] Generator Function Can Have one or More "yield"
# [4] By Using next() It Resume From Where It Called "yield" Not From Begining
# [5] When Called, Its Not Start Automatically, Its Only Give You The Control
# -----------------------------------------------------------------

def myGenerator(): # Generator Function
  yield 1 # First Yield
  yield 2 
  yield 3
  yield 4 #fourth Yield

myGen = myGenerator() # myGen is a generator object

print(next(myGen), end=" ") # Call The First Yield
print("Hello From Python") # Print Hello From Python
print(next(myGen), end=" ") # Call The Second Yield

for number in myGen: 
  print(number) # here it will print the third and fourth yield because the first and second yield are already called


print("#" * 40)

def myGenerator2(x,y): # Generator Function
    yield x+y # First Yield
    yield x-y 
    yield x*y
    yield x/y #fourth Yield

a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))
myGen2 = myGenerator2(a,b)
print(f'the summation is {next(myGen2)}') # Call The First Yield
print(f'the subtraction is {next(myGen2)}') # Call The Second Yield
print(f'the multiplication is {next(myGen2)}') # Call The Third Yield
print(f'the division is {next(myGen2)}') # Call The Fourth Yield
