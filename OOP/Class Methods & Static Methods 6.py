# -------------------------------------------------------------------
# -- Object Oriented Programming => Class Methods & Static Methods --
# -------------------------------------------------------------------
# Class Methods:
# - Marked With @classmethod Decorator To Flag It As Class Method
# - It Take Cls Parameter Not Self To Point To The Class not The Instance
# - It Doesn't Require Creation of a Class Instance
# - Used When You Want To Do Something With The Class Itself
# Static Methods:
# - It Takes No Parameters
# - Its Bound To The Class Not Instance
# - Used When Doing Something Doesnt Have Access To Object Or Class But Related To Class
# -----------------------------------------------------------

class Member:

  not_allowed_names = ["Hell", "Shit", "Baloot"] # Class Attribute

  users_num = 0 # Class Attribute

  @classmethod # Class Method decorator
  def show_users_count(cls): # Class Method

    print(f"We Have {cls.users_num} Users In Our System.") # This Method Will Show The Number Of Users In The System

  @staticmethod # Static Method decorator
  def say_hello(): # Static Method

    print("Hello From Static Method")

  def __init__(self, first_name, middle_name, last_name, gender):

    self.fname = first_name

    self.mname = middle_name

    self.lname = last_name

    self.gender = gender

    Member.users_num += 1  # Member.users_num = Member.users_num + 1

  def full_name(self):

    if self.fname in Member.not_allowed_names:

      raise ValueError("Name Not Allowed")

    else:

      return f"{self.fname} {self.mname} {self.lname}"

  def name_with_title(self):

    if self.gender == "Male":

      return f"Hello Mr {self.fname}"

    elif self.gender == "Female":

      return f"Hello Miss {self.fname}"

    else:

      return f"Hello {self.fname}"

  def get_all_info(self):

    return f"{self.name_with_title()}, Your Full Name Is: {self.full_name()}"

  def delete_user(self):

    Member.users_num -= 1  # Member.users_num = Member.users_num -1

    return f"User {self.fname} Is Deleted."

print(Member.users_num)

member_one = Member("Osama", "Mohamed", "Elsayed", "Male")
member_two = Member("Ahmed", "Ali", "Mahmoud", "Male")
member_three = Member("Mona", "Ali", "Mahmoud", "Female")
member_four = Member("Shit", "Hell", "Metal", "DD")

print(Member.users_num)
print(member_four.delete_user())
print(Member.users_num)

print("#" * 50)

Member.show_users_count()

print("#" * 50)

print(member_one.full_name())
print(Member.full_name(member_one)) # here we used the class method to call the instance method

Member.say_hello() # here we used the static method and the result wiil be "Hello From Static Method"
#and here we dont need to create an instance of the class to call the static method
