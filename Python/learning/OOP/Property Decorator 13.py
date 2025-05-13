# --------------------------------------------------------
# -- Object Oriented Programming => @Property Decorator --
# --------------------------------------------------------

class Member:

  def __init__(self, name, age):

    self.name = name

    self.age = age

  def say_hello(self):

    return f"Hello {self.name}"

  @property # Property Decorator changes the method to a property
  # - This allows you to access the method as an attribute
  # - This means you can call the method without parentheses 
  def age_in_days(self):

    return self.age * 365

one = Member("Ahmed", 40)

print(one.name) # Accessing public attribute
print(one.age)
print(one.say_hello())
# print(one.age_in_days()) # accessing the method if we don't use @property

print(one.age_in_days) # Accessing property method as an attribute by using @property wihtout parentheses