# -------------------------------------------------
# -- Object Oriented Programming => Polymorphism --
# -------------------------------------------------

n1 = 10
n2 = 20

print(n1 + n2) # here we see that + can be used in different ways here is used to sum two numbers

s1 = "Hello"
s2 = "Python"

print(s1 + " " + s2) # here + is used to concatenate two strings

print(len([1, 2, 3, 4, 5, 6])) # here we see that len can return different values depends on the input
print(len("Osama Elzero")) # result is 13
print(len({"Key_One": 1, "Key_Two": 2})) # result is 2

class A:

  def do_something(self):

    print("From Class A")

    raise NotImplementedError("Derived Class Must Implement This Method") # this is an abstract method and
    # it will raise an error if we try to call it without implementing it in the derived class so we need
    # to add this method (line 21) in the derived classes
    
class B(A):

  def do_something(self): # when we use the same name of the method in the derived class
    # it will override the method in the base class

    print("From Class B")

class C(A):

  def do_something(self): # when we use the same name of the method in the derived class
    # it will override the method in the base class

    print("From Class C")

my_instance = B()
my_instance.do_something()