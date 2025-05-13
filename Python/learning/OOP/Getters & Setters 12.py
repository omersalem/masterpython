# ------------------------------------------------------
# -- Object Oriented Programming => Getters & Setters --
# ------------------------------------------------------
from requests import get


# docstring about getters and setters
"""
Getters and Setters are methods that allow you to access and modify the private attributes of a class.
Getters are methods that return the value of a private attribute.
Setters are methods that set the value of a private attribute.
Getters and Setters are used to control access to the private attributes of a class.
They are used to encapsulate the data and provide a way to access and modify the data without directly
accessing the private attributes.
"""
class Member:

  def __init__(self, name):

    self.__name = name  # Private variable

  def say_hello(self):

    return f"Hello {self.__name}" # Method to say hello

  def get_name(self):  # Getter method to get the name

    return self.__name

  def set_name(self, new_name): # Setter method to set the name

    self.__name = new_name # Set the name to the new name passed to the method

one = Member("Ahmed")

one._Member__name = "Sayed" # Accessing private attribute from outside the class by using _ClassName__attribute_name
# - This is not recommended and should be avoided so we use setters and getters instead
print(one._Member__name) # - This is not recommended and should be avoided

print(one.get_name()) # Accessing private attribute using getter method which use method inside
#the class to get the name This is the recommended way to access private attributes
one.set_name('Abbas') # Accessing private attribute using setter method which is inside the class
# - This is the recommended way to modify private attributes
print(one.get_name()) # print the name