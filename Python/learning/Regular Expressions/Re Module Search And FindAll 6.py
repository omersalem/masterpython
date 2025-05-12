# ---------------------------------------------------------
# -- Regular Expressions => Re Module Search And FindAll --
# ---------------------------------------------------------
# search()  => Search A String For A Match And Return A First Match Only
# findall() => Returns A List Of All Matches and Empty List if No Match
# ---------------------------------------------------------------------
# Email Pattern => [A-z0-9\.]+@[A-z0-9]+\.(com|net|org|info)
# ----------------------------------------------------------

import re # Regular Expression Module and it is used to match strings with a specific pattern

my_search = re.search(r"[A-Z]{2}", "OOsamaEElzero") # Search for the first occurrence of two uppercase letters in the string "OOsamaEElzero"
# The pattern [A-Z]{2} means "find two consecutive uppercase letters"
# The search() function returns a match object if a match is found, otherwise it returns None
# the result will be 

print(my_search) # <re.Match object; span=(0, 2), match='OO'>
print(my_search.span()) # (0, 2) indicates the start and end positions of the match in the string
print(my_search.string) # "OOsamaEElzero" is the original string where the match was found
print(my_search.group()) #

is_email = re.search(r"[A-z0-9\.]+@[A-z0-9]+\.(com|net)", "os_123@osama.com")

if is_email:

  print("This is A Valid Email")

  print(is_email.span()) # (0, 12) indicates the start and end positions of the match in the string
  print(is_email.string) # os@osama.com is the original string where the match was found
  print(is_email.group()) # os@osama.com

else:


    print("This is Not A Valid Email")

email_input = input("Please Write Your Email: ") # Get user input for an email address
# The input is expected to be in the format of an email address

search = re.findall(r"[A-z0-9\.]+@[A-z0-9]+\.com|net", email_input) # Find all occurrences of the email pattern in the user input

empty_list = [] # Initialize an empty list to store valid email addresses

if search != []: # Check if the search result is not an empty list

  empty_list.append(search) # Append the found email addresses to the empty list

  print("Email Added") # Print a message indicating that the email has been added

else:

  print("Invalid Email") # Print a message indicating that the email is invalid

for email in empty_list: # Iterate through the list of valid email addresses

  print(email) # Print each valid email address


my_word = "Osama"
my_search = re.search(r'Osa', my_word) # Search for the pattern '0sa' in the string "Osama"
print(my_search) # Print the result of the search
print(my_search.group()) 
print(my_search.string) 
print(my_search.span()) 

my_phone = '09-233-2323'
my_findall = re.findall(r'\d{2}-\d{3}-\d{4}', my_phone) # Find all occurrences of the pattern '09-233-2323' in the string "my_phone"
print(my_findall) # Print the result of the findall
stored_phones = []
if my_findall != []: # Check if the findall result is not an empty list
    stored_phones.append(my_findall) # Append the found phone numbers to the stored_phones list
    print("Phone Number Added") 
    for phone in stored_phones: 
        print(phone) 
else: print("Phone Number Not Added") 
# Print a message indicating that the phone number has been added

