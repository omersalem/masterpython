# --------------------------
# -- Iterable vs Iterator --
# --------------------------
# Iterable
# [1] Object Contains Data That Can Be Iterated Upon
# [2] Examples (String, List, Set, Tuple, Dictionary)
# ------------------------------------------
# Iterator
# [1] Object Used To Iterate Over Iterable Using next() Method Return 1 Element At A Time
# [2] You Can Generate Iterator From Iterable When Using iter() Method
# [3] For Loop Already Calls iter() Method on The Iterable Behind The Scene
# [4] Gives "StopIteration" If Theres No Next Element
# -----------------------------------------------------------

myString = "Osama"

myList = [1, 2, 3, 4, 5] #myList is iterable object

for letter in myString:

  print(letter, end=" ") #result is O s a m a

for number in myList:

  print(number, end=" ")

myIterator = iter(myString) # convert myString to iterator object

print(next(myIterator)) # result is O
print(next(myIterator)) # result is s
print(next(myIterator)) # result is a
print(next(myIterator)) # result is m
print(next(myIterator)) # result is a
#print(next(myIterator)) # result is StopIteration error

for letter in iter("Elzero"): # convert "Elzero" to iterator object

  print(letter, end=" ") # result is E l z e r o

print("#" * 40)

mytuple = (1, 2, 3, 4, 5) # mytuple is iterable object
iteratedTuple = iter(mytuple) # convert mytuple to iterator object
print(next(iteratedTuple)) # result is 1
print(next(iteratedTuple)) # result is 2
print(next(iteratedTuple)) # result is 3
print(next(iteratedTuple)) # result is 4
