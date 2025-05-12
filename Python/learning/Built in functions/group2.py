# ------------------------
# -- Built In Functions --
# ------------------------
# sum() # Sum all elements in an iterable, optionally adding a starting value
# round() # Round a number to the nearest integer or to a specified number of decimal places
# range() # Generate a sequence of numbers from start to end with an optional step
# print() # Print to the console with optional separators and end characters
# ------------------------

# sum(iterable, start)
a = [1, 10, 19, 40]
print(sum(a)) # sum all elements in the list result will be 70
print(sum(a, 40)) # sum all elements in the list and add 40 to the result result will be 110 known

# round(number, numofdigits)
print(round(150.501)) # round to the nearest integer result will be 151
print(round(150.554, 2)) # round to 2 decimal places result will be 150.55

# range(start, end, step) start is not important if you want to start from 0,
#  end is the last number in the range and step is the difference between each number in the range and the default is 1
print(list(range(0))) # empty list starting from 0 ending at 0 step 1 result will be []
print(list(range(5))) # starting from 0 ending at 5 step 1 result will be [0, 1, 2, 3, 4]
print(list(range(5, 10))) # starting from 5 ending at 10 step 1 result will be [5, 6, 7, 8, 9]
print(list(range(10))) # starting from 0 ending at 10 step 1 result will be [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list(range(0, 20, 2))) # starting from 0 ending at 20 step 2 result will be [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

# print()
print("Hello @ Osama @ How @ Are @ You")
print("Hello", "Osama", "How", "Are", "You", sep=" | ") # print with separator result will be Hello | Osama | How | Are | You

print("First Line", end=" ") # print with end result will be First Line Second Line
print("Second Line") 
print("Third Line")

omar=list(range(0, 20, 2)) # starting from 0 ending at 20 step 2 result will be [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
print(omar) # print the list result will be [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]