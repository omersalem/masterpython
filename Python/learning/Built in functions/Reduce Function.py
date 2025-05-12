# ----------------------------------
# -- Built In Functions => Reduce --
# ----------------------------------
# [1] Reduce Take A Function + Iterator
# [2] Reduce Run A Function On FIrst and Second Element And Give Result
# [3] Then Run Function On Result And Third Element
# [4] Then Run Function On Rsult And Fourth Element And So On
# [5] Till One ELement is Left And This is The Result of The Reduce
# [6] The Function Can Be Pre-Defined Function or Lambda Function
# ---------------------------------------------------------------

from functools import reduce # Import the reduce function from the functools module

def sumAll(num1, num2): 

  return num1 + num2

numbers = [1, 8, 2, 9, 100]

result = reduce(sumAll, numbers) # Use the reduce function to sum all elements in the list numbers
# The reduce function will take the first two elements in the list and apply the sumAll function on them
# Then it will take the result and the next element in the list and apply the sumAll function on them
# This will continue until there is only one element left in the list
# The result will be the sum of all elements in the list
# The result will be 120

result = reduce(lambda num1, num2: num1 + num2, numbers) # Use the reduce function with a lambda function to sum all elements in the list numbers

print(result) # Print the result of the reduce function
# The result will be 120

# ((((1 + 8) + 2) + 9) + 100)