# -----------------------------------
# -- Date and Time => Introduction --
# -----------------------------------

import datetime # import datetime module

# print(dir(datetime)) # print all the attributes and methods of datetime module
# print(dir(datetime.datetime)) # print all the attributes and methods of datetime class

# Print The Current Date and Time
print(datetime.datetime.now()) # Print The Current Date and Time

print("#" * 40)

# Print The Current Year
print(datetime.datetime.now().year) #

# Print The Current Month
print(datetime.datetime.now().month)

# Print The Current Day
print(datetime.datetime.now().day)

print("#" * 40)

# Print Start and End Of Date
print(datetime.datetime.min)
print(datetime.datetime.max)

print("#" * 40)

# print(dir(datetime.datetime.now()))

# Print The Current Time
print(datetime.datetime.now().time())

print("#" * 40)

# Print The Current Time Hour
print(datetime.datetime.now().time().hour)

# Print The Current Time Minute
print(datetime.datetime.now().time().minute)

# Print The Current Time Second
print(datetime.datetime.now().time().second)

print("#" * 40)

# Print Start and End Of Time
print(datetime.time.min)
print(datetime.time.max)

print("#" * 40)

# Print Specific Date
print(datetime.datetime(1982, 10, 25)) # Print Specific Date year, month, day
print(datetime.datetime(1982, 10, 25, 10, 45, 55, 150364)) # Print Specific Date and Time year, month, day, hour, minute, second, microsecond

print("#" * 40)

myBirthDay = datetime.datetime(1982, 10, 25) # My Birthday year, month, day
dateNow = datetime.datetime.now() # Current Date and Time

print(f"My Birthday is {myBirthDay} And ", end="") #My Birthday is 1982-10-25 00:00:00
print(f"Date Now Is {dateNow}")

print(f" I Lived For {dateNow - myBirthDay}") 
print(f" I Lived For {(dateNow - myBirthDay).days} Days.") # show only the days

print('#' * 40)

from datetime import datetime as dt # import datetime class from datetime module as dt alias
from datetime import time as t # import time class from datetime module as t alias

print(dir(dt.now())) # Print all the attributes and methods of datetime class
print(f'{dt.now().hour}-{dt.now().minute}-{dt.now().second}-{dt.now().microsecond}') # Print The Current Date and Time
print(dt.now().hour) # Print The Current Time Hour
mybirth = dt(1987,9,13) # My Birthday year, month, day
print(f'{mybirth.year}-{mybirth.month}-{mybirth.day}') # Print My Birthday