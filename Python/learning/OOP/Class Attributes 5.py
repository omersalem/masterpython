# -----------------------------------------------------
# -- Object Oriented Programming => Class Attributes --
# -----------------------------------------------------
# Class Attributes: Attributes Defined Outside The Constructor
# -----------------------------------------------------------

class Member:

  not_allowed_names = ["Hell", "Shit", "Baloot"] # Class Attribute is outside the constructors and 
  # to call it we use the class name not the instance name

  users_num = 0 # Class Attribute is outside the constructors 

  def __init__(self, first_name, middle_name, last_name, gender):

    self.fname = first_name

    self.mname = middle_name

    self.lname = last_name

    self.gender = gender

    Member.users_num += 1  # Member.users_num = Member.users_num + 1

  def full_name(self):

    if self.fname in Member.not_allowed_names: # Check if the first name is in the not_allowed_names list
      ## If it is, raise a ValueError with a custom message

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

  def delete_user(self): # This method deletes the user by decrementing the users_num class attribute

    Member.users_num -= 1  # Member.users_num = Member.users_num -1 

    return f"User {self.fname} Is Deleted." # This message will be printed when the user is deleted


print(Member.users_num)

member_one = Member("Osama", "Mohamed", "Elsayed", "Male")
member_two = Member("Ahmed", "Ali", "Mahmoud", "Male")
member_three = Member("Mona", "Ali", "Mahmoud", "Female")
member_four = Member("Shit", "Hell", "Metal", "DD")

print(Member.users_num) # This will print the number of users created which is class attribute

print(member_four.delete_user()) # This will print the message that the user is deleted

print(Member.users_num) 

print(dir(member_one))

print(member_one.fname, member_one.mname, member_one.lname)
print(member_two.fname)
print(member_three.fname)

print(member_two.full_name())
print(member_two.name_with_title())

print(member_three.get_all_info())

print(dir(Member))