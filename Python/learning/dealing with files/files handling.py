# -------------------
# -- File Handling --
# -------------------
# "a" Append  Open File For Appending Values, Create File If Not Exists
# "r" Read    [Default Value] Open File For Read and Give Error If File is Not Exists
# "w" Write   Open File For Writing, Create File If Not Exists
# "x" Create  Create File, Give Error If File Exists
# --------------------------------------------------

import os  # Import the os module for interacting with the operating system

# Main Current Working Directory
print(os.getcwd())  # Print the current working directory

# Directory For The Opened File
print(os.path.dirname(os.path.abspath(__file__)))  # Print the directory of the current script file

# Change Current Working Directory
os.chdir(os.path.dirname(os.path.abspath(__file__)))  # Change the working directory to the script's directory

print(os.getcwd())  # Print the updated current working directory

print(os.path.abspath(__file__))  # Print the absolute path of the current script file

# Open a file in read mode using a raw string path (this will throw an error if the file doesn't exist)
file = open(r"/home/omersalem/Documents/VsCode Projects/Python/learning/dealing with files/osama.txt")  # Open the file at the specified path

# Open another file in read mode (this will also throw an error if the file doesn't exist)
#file = open("D:\Python\Files\osama.txt")  # Open the file at the specified path