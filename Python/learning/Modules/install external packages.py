#packages contains list of modules that are not built in and we need to install them
# # to install packages we use pip install package_name
# the package is a folder that contains multiple modules and the module is a file that contains multiple functions
# ------------------------------------------
# -- Modules => Install External Packages --
# ------------------------------------------
# [1] Module vs Package
# [2] External Packages Downloaded From The Internet
# [3] You Can Install Packages With Python Package Manager PIP
# [4] PIP Install the Package and Its Dependencies
# [5] Modules List "https://docs.python.org/3/py-modindex.html"
# [6] Packages and Modules Directory "https://pypi.org/"
# [7] PIP Manual "https://pip.pypa.io/en/stable/reference/pip_install/"
# [8] check if pip is installed by running pip --version
# [9] check if pip is installed by running python3 -m pip --version
# [10] to install pip on windows run the command curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
# [11] to install pip on linux run command sudo apt install python3-pip
# [11] to update packages on linux run sudo apt update
# [11] to upgrade pip on linux run sudo apt install --upgrade python3-pip
# [12] to install external packages on linux run sudo apt install python3-<package_name>
# [12] to install multiple external packages on linux run sudo apt install python3-<package_name1> python3-<package_name2>
# [12] to install multiple external packages on linux with version run sudo apt install python3-<package_name1>=<version> python3-<package_name2>=<version>
# [13] to install external packages on windows run the command pip install <package_name>
# ---------------------------------------------------------------------

import termcolor #after installing the package from terminal we can import it
import pyfiglet

print(dir(pyfiglet))
print(pyfiglet.figlet_format("Elzero"))
print(termcolor.colored("Elzero", color="yellow"))

print(termcolor.colored(pyfiglet.figlet_format("Elzero"), color="yellow"))

print('*' * 50)
from termcolor import colored as c # we can import the function directly as c alias 
from pyfiglet import figlet_format as f # we can import the function directly as f alias
print(c(f("Elzero"), color="red")) # we used  termcolor and pyfiglet packages to print the text in colored format


