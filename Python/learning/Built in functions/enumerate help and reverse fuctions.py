# ------------------------
# -- Built In Functions --
# ------------------------
# enumerate() # Return An Iterator With Index + Value
# help() # Return Help For A Function
# reversed() # Return An Iterator With The Reversed Order
# ------------------------

# enumerate(iterable, start=0)

mySkills = ["Html", "Css", "Js", "PHP"]

mySkillsWithCounter = enumerate(mySkills, 20) # Start from 20 default is 0 and it just add no beside the each element in the list

print(type(mySkillsWithCounter)) #result will be <class 'enumerate'>
print(mySkillsWithCounter) #result will be <enumerate object at 0x7f8c6e8b2d90>

for counter, skill in mySkillsWithCounter:

  print(f"{counter} - {skill}") 
  #result will be
  # 20 - Html
  # 21 - Css
  # 22 - Js
  # 23 - PHP

print("#" * 50)

#help() #help(object) # Return Help For A Function

print(help(print)) #result will be Help on built-in function print in module builtins:


print("#" * 50)

# reversed(iterable)

myString = "Elzero"

print(reversed(myString)) #result will be <reversed object at 0x7f8c6e8b2d90>

for letter in reversed(myString):

  print(letter) #result will be   o r e z l E

for s in reversed(mySkills):

  print(s) #result will be  PHP Js Css Html



  