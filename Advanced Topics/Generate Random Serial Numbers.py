# --------------------------------------------------------
# -- Advanced_Lessons => Generate Random Serial Numbers --
# --------------------------------------------------------

import string # import string module and use it bring in string
 
import random # import random module

print(string.digits) # 0-9
print(string.hexdigits) # 0-9, a-f, A-F
print(string.ascii_letters) # a-z, A-Z
print(string.ascii_lowercase) # a-z
print(string.ascii_uppercase) # A-Z

def make_serial(count): # function to generate a random serial number

  all_chars = string.ascii_letters + string.digits
  # print(all_chars) # 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'

  chars_count = len(all_chars)
  # print(chars_count)

  serial_list = [] # create an empty list to hold the serial number characters

  while count > 0: # while loop to generate characters until count reaches 0

    random_number = random.randint(0, chars_count - 1) # generate a random number
    # between 0 and chars_count - 1

    random_character = all_chars[random_number]

    serial_list.append(random_character)

    count -= 1  # count = count - 1

  print("".join(serial_list)) # join the list into a string and print it

make_serial(10)