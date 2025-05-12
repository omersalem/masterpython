# ---------------------------------
# -- Modules => Built In Modules --
# ---------------------------------
# [1] Module is A File Contain A Set Of Functions
# [2] You Can Import Module in Your App To Help You
# [3] You Can Import Multiple Modules
# [4] You Can Create Your Own Modules
# [5] Modules Saves Your Time
# --------------------------------------------------

# # Import Main Module
import random # Import Random Module
print(random) # Print The Module Name
print(f"Print Random Float Number {random.random()}") # Print Random Float Number

# Show All Functions Inside Module
print(dir(random)) # Print All Functions Inside Module and also the the location of the all the modules on the system
#<module 'random' from '/usr/lib/python3.12/random.py'> and we can create new modules and save it in the same location

# Import One Or Two Functions From Module
from random import randint, random # import randint and random functions from random module
print(f"Print Random Float {random()}") # Print Random Float Number
print(f"Print Random Integer {randint(100, 900)}") # Print Random Integer Number 

# from random import * # import all functions from random module
from random import sample

mysample = sample(range(0, 100), 5) # Print Random Sample From Range as a List
for i in mysample:
    print(i) # Print Random Sample From Range as a List
#we use sample by doing this  
# from random import sample
# print(sample(range(0, 100), 5)) # Print Random Sample From Range as a List and 5 is the number of elements in the list

