# -----------------------------------
# -- Modules => Create Your Module --
# -----------------------------------
#so here we created a module called elzero.py and we will use it in this file and this module
#  is in /home/omersalem/Documents/VsCode Projects/Python/learning/Modules so we add this location to the path so python can find it

import sys
sys.path.append(r"/home/omersalem/Documents/VsCode Projects/Python/learning/Modules") # Add Your Module Path so Python Can Find It so if you have a module in the same location as this file you can import it
print(sys.path)

import elzero # Import elzero Module
print(dir(elzero)) # Print All Functions Inside elzero Module

elzero.sayhello("Ahmed") # Print Hello Ahmed
elzero.sayhello("Osama") # Print Hello Osama
elzero.sayhello("Mohamed") # Print Hello Mohamed

elzero.sayHowAreYou("Ahmed") # Print How Are You Ahmed
elzero.sayHowAreYou("Osama") # Print How Are You Osama
elzero.sayHowAreYou("Mohamed") # Print How Are You Mohamed

# Alias

import elzero as ee # Import elzero module and give it an alias ee

ee.sayHello("Ahmed") # Print Hello Ahmed
ee.sayHello("Osama")
ee.sayHello("Mohamed")

ee.sayHowAreYou("Ahmed")
ee.sayHowAreYou("Osama")
ee.sayHowAreYou("Mohamed")

from elzero import sayHello # Import sayHello function from elzero module

sayHello("Osama") # Print Hello Osama

from elzero import sayHello as ss # Import sayHello function from elzero module and give it an alias ss

ss("Osama") # Print Hello Osama