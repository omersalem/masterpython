# ------------------------
# -- Built In Functions --
# ------------------------
# abs() # Return the absolute value of a number (positive value)
# pow() # Return the value of x to the power of y (x^y), with an optional modulus
# min() # Return the smallest of the input values and for letters it will return the first letter in the alphabet
# max()  # Return the largest of the input values and for letters it will return the last letter in the alphabet
# slice() # Return a slice object representing the set of indices specified by range(start, stop[, step])
# ------------------------

# abs()
print(abs(100)) #result will be 100
print(abs(-100)) #result will be 100
print(abs(10.19)) #result will be 10.19
print(abs(-10.19)) #result will be 10.19

print("#" * 50)

# pow(base, exp, mod) => Power mod is optional
print(pow(2, 5))  # 2 * 2 * 2 * 2 * 2
print(pow(2, 5, 10))  # (2 * 2 * 2 * 2 * 2) % 10

print("#" * 50)

# min(item, item , item, or iterator)
myNumbers = (1, 20, -50, -100, 100) #result will be -100
print(min(1, 10, -50, 20, 30)) #result will be -50
print(min("X", "Z", "Osama")) #result will be Osama
print(min(myNumbers)) #result will be -100

print("#" * 50)

# max(item, item , item, or iterator)
myNumbers = (1, 20, -50, -100, 100) #result will be 100
print(max(1, 10, -50, 20, 30)) #result will be 30
print(max("X", "Z", "Osama")) #result will be Z
print(max(myNumbers)) #result will be 100

print("#" * 50)

# slice(start, end, step) step is optional so the result will be from first element (start) to the last element (end-1) and the step 
# is the difference between each element in the list which is 1 by default
a = ["A", "B", "C", "D", "E", "F"] 
print(a[:5]) #result will be ['A', 'B', 'C', 'D', 'E'] 
print(a[slice(5)]) #result will be ['A', 'B', 'C', 'D', 'E']
print(a[slice(2, 5)]) #result will be ['C', 'D', 'E']
print(a[slice(1,4)]) #result will be ['B', 'C', 'D']
print(a[slice(1, 4, 2)]) #result will be ['B', 'D']