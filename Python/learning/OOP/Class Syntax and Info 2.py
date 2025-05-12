# ----------------------------------------------------------
# -- Object Oriented Programming => Class Syntax and Info --
# ----------------------------------------------------------
# [01] Class is The Blueprint Or Construtor Of The Object
# [02] Class Instantiate Means Create Instance of A Class
# [03] Instance => Object Created From Class And Have Their Methods and Attributes
# [04] Class Defined With Keyword class
# [05] Class Name Written With PascalCase [UpperCamelCase] Style
# [06] Class May Contains Methods and Attributes
# [07] When Creating Object Python Look For The Built In __init__ Method
# [08] __init__ Method Called Every Time You Create Object From Class
# [09] __init__ Method Is Initialize The Data For The Object
# [10] Any Method With Two Underscore in The Start and End Called Dunder or Magic Method
# [11] self Refer To The Current Instance Created From The Class And Must Be First Param
# [12] self Can Be Named Anything
# [13] In Python You Dont Need To Call new() Keyword To Create Object
# -------------------------------------------------------------------

# Syntax
# class Name:
#     Constructor => Do Instantiation [ Create Instance From A Class ]
#     Each Instance Is Separate Object
#     def __init__(self, other_data) 
#         Body Of Function


class Member:

  def __init__(self):

    print("A New Member Has Been Added")

member_one = Member() # the result is : A New Member Has Been Added
member_two = Member() # the result is : A New Member Has Been Added
member_three = Member() # the result is : A New Member Has Been Added

print(member_one.__class__) # the result is : <class '__main__.Member'>

my_dictionary = { #here we cant make operations on the dictionary itself so we create a class for it to make operations on it
  'name': "Osama",
  'age': 36,
  'monthly_salary': 5000,
  'yearly_salary': ''  # Something
}
print('*' * 50)
class Name: # the name of the class is Name
    def __init__(self, other_data): #refers to the current instance of the class.
        # It allows you to access the instance's attributes and methods.
        print(f"Object created with data: {other_data}") #inside the __init__ method,
        #you define what happens when an object is created (e.g., setting attributes or printing a message).

obj = Name("Hello")

# When obj = Name("Hello") is executed:
# The __init__ method is called automatically.
# It prints: Object created with data: Hello.