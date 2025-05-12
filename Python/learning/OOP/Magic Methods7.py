# --------------------------------------------------
# -- Object Oriented Programming => Magic Methods --
# --------------------------------------------------
# Everything in Python is An Object
# __init__  Called Automatically When Instantiating Class
# self.__class__ The class to which a class instance belongs
# __str__   Gives a Human-Readable Output of the Object
# __len__   Returns the Length of the Container
#           Called When We Use the Built-in len() Function on the Object
# ------------------------------------------------------

class Skill:

  def __init__(self):

    self.skills = ["Html", "Css", "Js"]

  def __str__(self): #

    return f"This is My Skills => {self.skills}" # 

  def __len__(self):

    return len(self.skills)

profile = Skill() 
print(profile)
print(len(profile))

profile.skills.append("PHP") # Add "PHP" To The List
profile.skills.append("MySQL") # Add "MySQL" To The List

print(len(profile)) # Print The Length of the List which is 5

print(profile.__class__) # Print The Class of the Object which is Skill
my_string = "Osama" # String is an Object of Class str
print(type(my_string)) # Print The Type of the Object which is str
print(my_string.__class__) # Print The Class of the Object which is str 
print(dir(str)) # Print All The Methods of the Class str
print(str.upper(my_string)) # Print The Uppercase of the String