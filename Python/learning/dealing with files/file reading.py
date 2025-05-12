# --------------------------------
# -- File Handling => Read File --
# --------------------------------

myFile = open("/home/omersalem/Documents/VsCode Projects/Python/learning/dealing with files/osama.txt", "r")  # Open the file in read mode

print(myFile)  # Print the file object information
print(myFile.name)  # Print the name of the file
print(myFile.mode)  # Print the mode in which the file is opened
print(myFile.encoding)  # Print the file's encoding
print('**' * 20)  # Print a separator line
print(myFile.read())  # Read the entire content of the file
print('**' * 20)  # Print a separator line
print(myFile.read(5))  # Read the next 5 characters from the file

print(myFile.readline(5))  # Read the next 5 characters of the same line and put it in next line
print(myFile.readline())  # Read the next line from the file
print(myFile.readline())  # Read next line from the file

print(myFile.readlines())  # Read all remaining lines as a list
print(myFile.readlines(50))  # Read lines with a maximum of 50 bytes
print(type(myFile.readlines()))  # Print the type of the result from `readlines`

for line in myFile:  # Iterate through each line in the file
  print(line)  # Print the current line
  if line.startswith("08"):  # Check if the line starts with "08"
    break  # Stop the loop if the condition is met



# Reset the file pointer to the beginning of the file
myFile.seek(0)

# Now you can use readline() again
print(myFile.read())

# Close The File
myFile.close()  # Close the file to release system resourcescls