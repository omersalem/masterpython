# ---------------------------------------------------------
# -- Object Oriented Programming => Multiple Inheritance --
# ---------------------------------------------------------

class BaseOne:

  def __init__(self):

    print("Base One")

  def func_one(self):

    print("One")

class BaseTwo:

  def __init__(self):

    print("Base Two")

  def func_two(self):

    print("Two")

class Derived(BaseOne, BaseTwo): # here derived class inherits from both BaseOne and BaseTwo classes
  # and here it will print "Base One" and will not print "Base Two" because the first class in the parenthesis
  #  is the one that will be called first 

  pass

my_var = Derived() # here we created an object from Derived class


print(Derived.mro()) # here we print the method resolution order and it shows that the first class is BaseOne
# and the second class is BaseTwo 

print(my_var.func_one) 
print(my_var.func_two)

my_var.func_one() #my_var has both methods of BaseOne and BaseTwo classes
my_var.func_two()

class Base:

  pass

class DerivedOne(Base):

  pass

class DerivedTwo(DerivedOne): #here DerivedTwo inherits from DerivedOne class which in turn inherits from Base class
  # so derivedTwo class has all the methods and attributes of Base class

  pass