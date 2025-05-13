
#docstring
"""
Inheritance
Inheritance is a way to form new classes using classes that have already been defined.
The new classes, called ⁡⁢⁣⁣derived classes⁡, take on (or inherit) attributes and behaviors (methods)
 of the pre-existing classes, which are referred to as ⁡⁢⁣⁣base classes⁡.
The derived class can have additional attributes and behaviors of its own.
The derived class can also override or modify the inherited attributes and behaviors.
The main purpose of inheritance is to promote code reusability and establish a hierarchical 
relationship between classes.
""" 
# ------------------------------------------------
# -- Object Oriented Programming => Inheritance --
# ------------------------------------------------
"""
 The Idea: A Son Inherits from His Father
Imagine this:

👨 Father has some properties like name and age, and he knows how to drive.

👦 Son is a child of the father. So, he inherits the name, age, and drive ability from his father. But he also has something new — like toys and the ability to play.

"""
class Father:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print(f"Father {self.name} is {self.age} years old")

    def drive(self):
        print("Father can drive 🚗")

class Son(Father):  # Son inherits from Father
    def __init__(self, name, age, toys):
        super().__init__(name, age)  # Call the constructor of Father so the init method of father will be called
        #so it will print father {self.name} is {self.age} years old
        self.toys = toys # New attribute for Son
        print(f"Son {self.name} is {self.age} years old and has {self.toys} toys 🎮") #after applying father init using super
        # it will print Son {self.name} is {self.age} years old and has {self.toys} toys 🎮





    def play(self): # New method for Son which is not in the father class
        print("Son is playing with his toys 🧸")

ahmed = Son("Ahmed", 10, 5) # Create an instance of Son

ahmed.drive()  # This method is inherited from Father class 
ahmed.play()   # This is a method in Son class so ahmad has both methods of father and son classes

# ------------------------------------------------
class Food:  # Base Class

  def __init__(self, name, price):

    self.name = name

    self.price = price

    print(f"{self.name} Is Created From Base Class")

  def eat(self):

    print("Eat Method From Base Class")

class Apple(Food):  # Derived Class here we wrote Food in the parenthesis to inherit from it

  def __init__(self, name, price, amount): # here we inherited name and price from the base class Food and 
    #added amount as a new attribute

    # Food.__init__(self, name)  # Create Instance From Base Class

    super().__init__(name, price) # Create Instance From Base Class
    # here we used super() to call the constructor of the base class Food and pass the values to it
    # this is the same as Food.__init__(self, name, price)

    self.amount = amount # here we added amount as a new attribute

    print(f"{self.name} Is Created From Derived Class And Price Is {self.price} And Amount Is {self.amount}")

  def get_from_tree(self):

      print("Get From Tree From Derived Class")

# food_one = Food("Pizza")
food_two = Apple("Pizza", 150, 500)
food_two.eat()
food_two.get_from_tree()

print('*'*50)

#⁡⁢⁣⁣important not⁡⁢⁣⁣e⁡⁢⁣⁣:⁡ ⁡⁢⁣⁣if we don't have init consturctor in the son class we don't need to call super().__init__(name, age)⁡
# ⁡⁢⁣⁣because the father class init constructor will be called automatically but if we have init constructor
#  in the son class we⁡ ⁣need to call super().__init__(name, age) to call the constructor of the father class⁡

#example: without using super()__init__()
class Animal:
    def __init__(self):
        print("Animal constructor")

class Dog(Animal):
    def __init__(self):
        print("Dog constructor")

dog1 = Dog()
# the result will be: Dog constructor
# here it will not print "Animal constructor" because we didn't call the constructor of the base class Animal

# now example with using super()__init__()
class Animal:
    def __init__(self):
        print("Animal constructor")

class Dog(Animal):
    def __init__(self):
        super().__init__()
        print("Dog constructor")

dog2 = Dog()

# the result will be: 
# Animal constructor
# Dog constructor

#Why isn’t it executed automatically?

#Because in Python:
#When you write a new constructor (__init__) in the child class, you are overriding 
#the one from the parent class and replacing it with your own.Therefore, Python does not
# automatically call the parent’s constructor. Instead, it gives you full control — 
 #if you want the parent’s constructor to run, you must call it manually using super().__init__().




