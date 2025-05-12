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
  def __init__(self, first_name, middle_name, last_name, gender):
    """
    Initialize a new instance of the Member class.
    
    Parameters:
    first_name (str): The first name of the member.
    middle_name (str): The middle name of the member.
    last_name (str): The last name of the member.
    gender (str): The gender of the member.
    """
    self.fname = first_name
    self.mname = middle_name
    self.lname = last_name
    self.gender = gender

  def full_name(self): #this is an instance method that takes self as a parameter which points to the current instance
    ## this method returns the full name of the member by concatenating the first name, middle name and last name
    return f"{self.fname} {self.mname} {self.lname}"

  def name_with_title(self): #this is an instance method that takes self as a parameter which points to the current instance
    ## this method returns the name with title based on the gender
    if self.gender == "Male":
      return f"Hello Mr {self.fname}"
    elif self.gender == "Female":
      return f"Hello Miss {self.fname}"
    else:
      return f"Hello {self.fname}"

  def get_all_info(self): #this is an instance method that takes self as a parameter which points to the current instance
    ## this method returns all the information of the member by calling the name_with_title and full_name methods
    ## and concatenating the results
    return f"{self.name_with_title()}, Your Full Name Is: {self.full_name()}"


member_one = Member("Osama", "Mohamed", "Elsayed", "Male")
member_two = Member("Ahmed", "Ali", "Mahmoud", "Male")
member_three = Member("Mona", "Ali", "Mahmoud", "Female")

# print(dir(member_one))

# print(member_one.fname, member_one.mname, member_one.lname)
# print(member_two.fname)
# print(member_three.fname)

# print(member_two.full_name()) 
# print(member_two.name_with_title())

print(member_one.get_all_info()) # the result is : Hello Mr Osama, Your Full Name Is: Osama Mohamed Elsayed