# -----------------------------------------------
# -- File Handling => Write and Append In File --
# -----------------------------------------------
#in write mode each time you write to the file it will be overwritten so the file will only contain the last lines you wrote

# Open the file "osama.txt" in write mode ("w") - this will overwrite the file if it exists and create it if it doesn't
myFile = open("/home/omersalem/Documents/VsCode Projects/Python/learning/dealing with files/omar.txt", "w")
# Write "Hello" followed by a newline to the file
myFile.write("Hello\n")
# Write "Third Line" to the file
myFile.write("Third Line\n")
myFile.write("Second Line\n") 

#--------------------------------------------------------

# Open the file "fun.txt" in write mode ("w") - this will overwrite the file if it exists
myFile = open(r"/home/omersalem/Documents/VsCode Projects/Python/learning/dealing with files/fun.txt", "w")
#here we wrote r before the path to make it a raw string, so we don't have to escape the backslashes because /fun has /f which is
#  a special character in python so we use r to make it a raw string and ignor the special characters
# Write "Elzero Web School" 1000 times, each on a new line
myFile.write("Elzero Web School\n" * 1000)
#-------------------------------------------------------

# Create a list of strings to write to the file
myList = ["Oasma\n", "Ahmed\n", "Sayed\n"]

# Open the file "osama.txt" in write mode ("w") - this will overwrite the file if it exists
myFile = open("/home/omersalem/Documents/VsCode Projects/Python/learning/dealing with files/osama.txt", "w")
# Write all the strings in the list to the file
myFile.writelines(myList) # This will write each string in the list to the file and remove all the previouse contents 
# #-------------------------------------------------------

# Open the file "osama.txt" in append mode ("a") - this will add content to the file without overwriting it
myFile = open("/home/omersalem/Documents/VsCode Projects/Python/learning/dealing with files/osama.txt", "a")
# Append the string "Elzero" to the file

myFile.write("Elzero\n")
myFile.write("omersalem\n")
myFile.write("Ahmed\n\n\n")
myFile.write("Sayed\n")