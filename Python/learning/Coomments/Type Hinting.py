# ------------------
# -- Type Hinting --
# ------------------
# type hinting => help us to avoid errors in our code by telling python what type of data we are working with 
#so you can just add specific data type such as int or str or list or boolean .... etc
def say_hello(name) -> str: # -> str means that the function returns a string

  print(f"Hello {name}")

say_hello("Ahmed")

def calculate(n1, n2) -> str: #example for type hinting

  print(n1 + n2)

calculate(10, 40)