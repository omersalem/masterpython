# -----------------------------------
# --      Exceptions Handling      --
# -- Try | Except | Else | Finally --
# --       Advanced Example        --
# -----------------------------------
"""
this code will try to open a file and read its contentns if the file is not found it will ask the user to enter the file name again
and the user has 5 tries to enter the file name correctly if the file is not found after 5 tries the program will exit 
and print "All Tries Is Done" and if the file is found the program will print the content of the file and close the file afterwards 
"""
the_file = None # Initialize the_file variable

the_tries = 5 # Initialize the_tries variable

while the_tries > 0:  # ⁡⁢⁢⁣Loop While the_tries is greater than 0⁡

  try:  # Try To Open The File

    print("Enter The File Name With Absolute Path To Open") # Print A Message

    print(f"You Have {the_tries} Tries Left") # Print The Number Of Tries Left

    print("Example: D:\Python\Files\yourfile.extension") # Print An Example

    file_name_and_path = input("File Name => : ").strip() # Get The File Name From The User and Remove Any Leading or Trailing Whitespace

    the_file = open(file_name_and_path, 'r') # Open The File

    print(the_file.read()) # Print The Content Of The File

    break # Exit The Loop

  except FileNotFoundError: # If The File Is Not Found

    print("File Not Found Please Be Sure The Name is Valid") # Print A Message.

    the_tries -= 1 # Decrement the_tries

  except: # If Any Other Error

    print("Error Happen") # Print A Message

  finally: # Run This Code No Matter What

    if the_file is not None: # If the_file is not None

      the_file.close() # Close The File

      print("File Closed.") # Print A Message

else:

  print("All Tries Is Done") # Print A Message