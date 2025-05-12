# -------------------------
# -- Decorators => Intro --
# -------------------------
# [1] Sometimes Called Meta Programming
# [2] Everything in Python is Object Even Functions
# [3] Decorator Take A Function and Add Some Functionality and Return It
# [4] Decorator Wrap Other Function and Enhance Their Behaviour
# [5] Decorator is Higher Order Function (Function Accept Function As Parameter)
# ----------------------------------------------------------------------
from termcolor import colored as c # we can import the function directly as c alias 
from pyfiglet import figlet_format as f # we can import the function directly as f alias




def myDecorator(func):  # Decorator

  def nestedFunc():  # Any Name Its Just For Decoration

    print("Before")  # Message From Decorator

    func()  # Execute Function

    print("After")  # Message From Decorator

  return nestedFunc  # Return All Data

@myDecorator  #when we use this it will apply the decorator on the function bellow 

def sayHello():

  print("Hello From Say Hello Function")

@myDecorator

def sayHowAreYou():

  print("Hello From Say How Are You Function")

# afterDecoration = myDecorator(sayHello) # this is the same as @myDecorator before the function so we dont need to use it again

# afterDecoration() #if we used @myDecorator we dont need to use this line

sayHello()

print("#" * 50)

sayHowAreYou()

print("#" * 50)

def mynewdecorator(omer):  # Decorator

  def nestedFunc():  # Any Name Its Just For Decoration

    print(c(f("omersalem"), color="red")) # we used  termcolor and pyfiglet packages to print the text in colored format
    

    omer()  # Execute Function

    print(c(f("Welcome"), color="red")) # we used  termcolor and pyfiglet packages to print the text in colored format

  return nestedFunc  # Return All Data

@mynewdecorator  #when we use this it will apply the decorator on the function bellow
def sayhello2():
  print("Hello From Say Hello Function")

sayhello2()


