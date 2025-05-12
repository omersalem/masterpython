# ----------------------------------------
# -- Decorators => Practical Speed Test --
# ----------------------------------------

from time import time # Import Time Function

def myDecorator(func):  # Decorator

  def nestedFunc(*numbers):  # Any Name Its Just For Decoration 

    for number in numbers:

      if number < 0:

        print("Beware One Of The Numbers Is Less Than Zero")

    func(*numbers)  # Execute Function here we use * so it can take any number of parameters

  return nestedFunc  # Return All Data

@myDecorator

def calculate(n1, n2, n3, n4): 

  print(n1 + n2 + n3 + n4)

calculate(-5, 90, 50, 150)

def speedTest(func): #another decorator to test the speed of the function and always put any name between () 

  def wrapper(): #nested function so if we have parameters in the function we put the same parameters in the wrapper function (nested function)

    start = time() # Get Start Time
    # The time function will return the current time in seconds 

    func()

    end = time() # Get End Time
    # The time function will return the current time in seconds

    print(f"Function Running Time Is: {end - start}")

  return wrapper

@speedTest

def bigLoop():

  for number in range(1, 20000):

    print(number)

bigLoop()


print("#" * 50)

#we wwill make decorator to count the numbers of letters in the string

def countLetters(func):
  def countstring(a):
    count=0
    for i in a:
        if i==" ":
            continue
        else:
            count+=1

    print(f"the number of letters in the string is {count}")
    func(a)
  return countstring


    
@countLetters 

def printletters(a):
    print(a)

printletters("hello   world")

