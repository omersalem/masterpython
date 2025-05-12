# -----------------------------------
# -- Errors And Exceptions Raising --
# -----------------------------------
# [1] Exceptions Is A Runtime Error Reporting Mechanism
# [2] Exception Gives You The Message To Understand The Problem
# [3] Traceback Gives You The Line To Look For The Code in This Line
# [4] Exceptions Have Types (SyntaxError, IndexError, KeyError, Etc...)
# [5] Exceptions List https://docs.python.org/3/library/exceptions.html
# [6] raise Keyword Used To Raise Your Own Exceptions
# -----------------------------------------------------------------

x = -10

if x < 0:

  raise Exception(f"The Number {x} Is Less Than Zero")

  print("This Will Not Print Because The Error") # this will not be printed because the error is raised

else:

  print(f"{x} Is Good Number and Ok")

print('Print Message After If Condition')

y = 10

if type(y) != int:

  raise ValueError("Only Numbers Allowed")

print('Print Message After If Condition') #this will be printed because the error is not raised

print('#' * 50)

z='osama'

if type(z) != int:
  
  raise TypeError("Only Numbers Allowed")

print('#' * 50)

e=0

if e==0:
  raise ZeroDivisionError ("Can't divide by zero")                  
f= 10/e
print("f =", f) 

print('#' * 50)




