# ----------------------------------------------------------------
# -- Object Oriented Programming => ABCs => Abstract Base Class --
# ----------------------------------------------------------------
# - Class Called Abstract Class If it Has One or More Abstract Methods
# - abc module in Python Provides Infrastructure for Defining Custom Abstract Base Classes.
# - By Adding @absttractmethod Decorator on The Methods
# - ABCMeta Class Is a Metaclass Used For Defining Abstract Base Class
# --------------------------------------------------------------------
"""
inside abstract base class we can define abstract methods with on value we just write pass but 
if we inherit from the abstract base class we have to write all the abstract methods of the base class in
the derived class otherwise we will get an error """
# ---------------------------------------------------------


from abc import ABCMeta, abstractmethod # here we import the ABCMeta and abstractmethod from abc module
# - ABCMeta is a metaclass for defining abstract base classes in Python.
# - abstractmethod is a decorator that marks a method as abstract

class Programming(metaclass=ABCMeta): 

  @abstractmethod # we add this decorator to the method to make it abstract
  def has_oop(self): # abstract method and should be added to all derived classes

    pass # this word return None

  @abstractmethod
  def has_name(self): # abstract method and should be added to all derived classes

    pass # this word return None

class Python(Programming):

  def has_oop(self): # we wrote the abstract method of the base class 

    return "Yes"

class Pascal(Programming):

  def has_oop(self):

    return "No"

  def has_name(self):

    return "Pascal"

one = Pascal()

print(one.has_oop())
print(one.has_name())

one = Python() 
print(one.has_oop()) # ⁡⁢⁣⁣here we have error because in Python class we did'nt add all the abstract
# methods of the base class so we need to add the has_name method in the Python class⁡