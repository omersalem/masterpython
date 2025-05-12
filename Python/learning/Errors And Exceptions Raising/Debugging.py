# at the beginning we make sure that the debugging is working in vscode by going to file > preferences > search for debug and enable 
# allow breakpoints everywhere

# --------------------
# -- Debugging Code --
# --------------------
"""
so here we put red circle beside the code i want to debug ( brakpoint ) and when i click on it i will see the code in the debug console
and then i press on run and debug in the left panel and i will see the code in the debug console and se the flows of the code
"""

my_list = [1, 2, 3]

my_dictionary = {"Name": "Osama", "Age": 36, "Country": "Egypt"}

for num in my_list:

  print(num)

for key, value in my_dictionary.items():

  print(f"{key} => {value}")

def function_one_one():

  print("Hello From Function One")

function_one_one()