# --------------------------------------------------
# -- Object Oriented Programming => Encapsulation --
# --------------------------------------------------
# Encapsulation
# - Restrict Access To The Data Stored in Attirbutes and Methods
# Public
# - Every Attribute and Method That We Used So Far Is Public
# - Attributes and Methods Can Be Modified and Run From Everywhere
# - Inside Our Outside The Class
# Protected
# - Attributes and Methods Can Be Accessed From Within The Class And Sub Classes
# - Attributes and Methods Prefixed With One Underscore _
# Private
# - Attributes and Methods Can Be Accessed From Within The Class Or Object Only
# - Attributes Cannot Be Modified From Outside The Class
# - Attributes and Methods Prefixed With Two Underscores __
# ---------------------------------------------------------
# - Attributes = Variables = Properties
# -------------------------------------

class Member:

  def __init__(self, name):

    self.name = name  # Public

one = Member("Ahmed")
print(one.name)
one.name = "Sayed"
print(one.name)

class Member:

  def __init__(self, name):

    self._name = name  # Protected by using _ (underscore)
# - This is a convention and not enforced by Python
# - It is a hint to other developers that this attribute is intended for internal use only
# - It is not a strict access control mechanism
# - It is still possible to access and modify this attribute from outside the class
# - But it is not recommended to do so

one = Member("Ahmed")
print(one._name) # Accessing protected attribute from outside the class by using _  but it is not recommended 
# - It is a hint to other developers that this attribute is intended for internal use only
one._name = "Sayed"
print(one._name) # result is Sayed

class Member:

  def __init__(self, name):

    self.__name = name  # Private by using __ (double underscore)
# - This is a strict access control mechanism
# - It is not possible to access or modify this attribute from outside the class
# - It is only accessible from within the class

  def say_hello(self):

    return f"Hello {self.__name}"

one = Member("Ahmed")
# print(one.__name)
print(one.say_hello())
print(one._Member__name) # Accessing private attribute from outside the class by using _ClassName__attribute_name
# - This is not recommended and should be avoided
# - It is only used for debugging purposes
# - It is not a good practice to access private attributes from outside the class