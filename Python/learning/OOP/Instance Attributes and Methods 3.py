# --------------------------------------------------------------------
# -- Object Oriented Programming => Instance Attributes and Methods --
# --------------------------------------------------------------------
# Self: Point To Instance Created From Class
# Instance Attributes: Instance Attributes Defined Inside The Constructor
# -----------------------------------------------------------------------
# Instance Methods: Take Self Parameter Which Point To Instance Created From Class
# Instance Methods Can Have More Than One Parameter Like Any Function
# Instance Methods Can Freely Access Attributes And Methods On The Same Object
# Instance Methods Can Access The Class Itself
# -----------------------------------------------------------

class Member:
  def __init__(self, first_name, middle_name, last_name): #this is called the constructor
    """
    This special method is the constructor of the class.
    It is used to set the initial state of the object by assigning the values of the object's properties.
    That is, when you create a new instance of the class, this method is called and show the attributes of the class
    that you want to fill with values.
    The __init__ method is a special method in Python classes that is called when an object is created from the class.
    """
    
    self.fname = first_name #this is an instance attribute
    self.mname = middle_name #this is an instance attribute
    self.lname = last_name #this is an instance attribute
# self we alway add it at the start of the function to refer to the current instance of the class
# then we add the attributes we want to add to the class such as first name, middle name and last name


member_one = Member("Osama", "Mohamed", "Elsayed") #create an instance of the class Member and we pass the 
#values to the constructor
member_two = Member("Ahmed", "Ali", "Mahmoud") 
member_three = Member("Mona", "Ali", "Mahmoud") 
member_four = Member('ahmad','osama','abeer')

# print(dir(member_one))

print(member_one.fname, member_one.mname, member_one.lname) #here we access the attributes of the class and print them
print(member_two.fname) # the result is : Ahmed
print(member_three.fname) # the result is : Mona

# so we first create a class called Member and then we create constructor inside it which has multiple attributes
# then we create instances of the class Member and pass the values to the constructor for example
# member_one = Member("Osama", "Mohamed", "Elsayed") then we printed the attributes of the class for example
# print(member_one.fname, member_one.mname, member_one.lname) which will print the values we passed to the constructor