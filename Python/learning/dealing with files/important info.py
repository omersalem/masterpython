# -------------------------------------
# -- File Handling => Important Info --
# -------------------------------------

import os  # Import the os module to interact with the operating system

# Open the file "ahmad.txt" in append mode ("a") and create it if it doesn't exist
myFile = open("/home/omersalem/Documents/VsCode Projects/Python/learning/dealing with files/ahmad.txt", "a")
myFile.write("Hello\n")  # Write "Hello" followed by a newline to the file
myFile.write("Second Line\n")  # Write "Second Line" followed by a newline to the file
# Truncate the file to the first 5 bytes, removing any content beyond that
myFile.truncate(5) #this will remove all the content after the 5th character and keep the first 5 characters

# Open the file "osama.txt" in append mode ("a")
myFile = open("/home/omersalem/Documents/VsCode Projects/Python/learning/dealing with files/omar.txt", "a")
# Print the current file pointer position (in bytes) from the start of the file
print(myFile.tell())
myFile.seek(0)  # Move the file pointer to the beginning of the file
myFile.write("Hell\n")  # Write "Hello" followed by a newline to the file but it will be added to the end of 
#the file because we are in append mode and the words are written in the end of the file always
myFile.write("Second Line\n")  # Write "Second Line" followed by a newline to the file

# Open the file "osama.txt" in read mode ("r")
myFile = open("/home/omersalem/Documents/VsCode Projects/Python/learning/dealing with files/omar.txt", "r")
# Move the file pointer to the 11th byte in the file
myFile.seek(11)
# Read the content of the file starting from the current pointer position and print it
print(myFile.read())

# Remove (delete) the file "osama.txt" from the filesystem
os.remove("/home/omersalem/Documents/VsCode Projects/Python/learning/dealing with files/omar.txt")

myFile = open("/home/omersalem/Documents/VsCode Projects/Python/learning/dealing with files/ali.txt", "w")
myFile.write("Hello\n"*50)  # Write "Hello" followed by a newline to the file
myFile.seek(200)
myFile.write("omar\n"*10)  # Write "Hello" followed by a newline to the file