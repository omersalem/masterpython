# ----------------------------------------------------
# -- Practical => Loop on Many Iterators With Zip() --
# ----------------------------------------------------
# zip() Return A Zip Object Contains All Objects so it merges all objects together
# zip() Length Is The Length of Lowest Object so the loop will stop when the lowest object is finished
# ------------------------------------------------

list1 = [1, 2, 3, 4, 5]
list2 = ["A", "B", "C", "D"] # this list and dict1 are the shortest ones so the loop will stop when these list is finished
tuple1 = ("Man", "Woman", "Girl", "Boy")
dict1 = {"Name": "Osama", "Age": 36, "Country": "Egypt", "Skill": "Python"}

for item1, item2, item3, item4 in zip(list1, list2, tuple1, dict1):

  print("List 1 Item =>", item1) 
  print("List 2 Item =>", item2)
  print("Tuple 1 Item =>", item3)
  print("Dict 1 Key =>", item4, "Value =>", dict1[item4])

ultimateList = zip(list1, list2)
print(ultimateList)
for item in ultimateList:
  print(item) #the result is a tuple of the two lists which is : 
#  (1, 'A')
#  (2, 'B')
#  (3, 'C')
#  (4, 'D') 
# we didnt use the last item in the list1 (5) because the list2 is shorter than the list1


# ------------------------------------------------

list1 = ['a', 'b', 'c', 'd']
list2 = ['e', 'f', 'g', 'h']

list3 = ['i', 'j', 'k', 'l']

mergedlists = zip(list1, list2, list3)
for item1, item2, item3 in mergedlists:
 # print(item1, item2, item3)
  print(f'the list1 item is {item1} and the list2 item is {item2} and the list3 item is {item3}')


    

