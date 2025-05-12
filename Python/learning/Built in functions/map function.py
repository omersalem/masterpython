# -------------------------------
# -- Built In Functions => Map --
# -------------------------------
# [1] Map Take A Function + Iterator
# [2] Map Called Map Because It Map The Function On Every Element
# [3] The Function Can Be Pre-Defined Function or Lambda Function
# ---------------------------------------------------------------

# Use Map With Predefined Function

def formatText(text):

  return f"- {text.strip().capitalize()} -" #reuturn the text with - at the start and end and remove the spaces and capitalize the first letter

myTexts = [" OSama ", "AHMED", "  sAYed  "] 

myFormatedData = map(formatText, myTexts) # map the function formatText on every element in the list myTexts

print(myFormatedData) # print the map object the result will be <map object at 0x7f8c6e8b2d90>

for name in list(map(formatText, myTexts)):

  print(name) # print the map object as a list the result will be ['- Osama -', '- Ahmed -', '- Sayed -']

print("#" * 50)

# Use Map With Lambda Function

def formatText(text): 
 
  return f"- {text.strip().capitalize()} -" #reuturn the text with - at the start and end and remove the spaces and capitalize the first letter
# Use Map With Lambda Function

myTexts = [" OSama ", "AHMED", "  sAYed  "]

for name in list(map((lambda text: f"- {text.strip().capitalize()} -"), myTexts)): # map lambda function on every element in the list myTexts


  print(name) # print the map object as a list the result will be ['- Osama -', '- Ahmed -', '- Sayed -']

print("#" * 50)

omersalem=[1, -2, 3, -4, 5, 6, 7, 8, 9, 10]
mylist = list(map(lambda x: f'{abs(x)}', omersalem)) # map the function abs on every element in the list omersalem
for i in mylist:
    print(i,end=' ') # print the map object as a list the result will be ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']