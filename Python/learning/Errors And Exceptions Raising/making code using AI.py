"""
⁡⁢⁢⁢this code will try to open a file and read its contentns if the file is not found it will ask the user to enter the file name again
and the user has 5 tries to enter the file name correctly if the file is not found after 5 tries the program will exit 
and print "All Tries Is Done" and if the file is found the program will print the content of the file and close the file afterwards ⁡
"""


attempts = 5

for attempt in range(attempts):
    try:
        print("Enter the name of the file to open: ")
        print("example: D:\Python\Files\yourfile.extension")
        file_name = input("File Name => : ").strip()

        """ 
        ⁡⁢⁣⁣The with statement in line 22 is used to open the file in a context manager. Its job is to ensure that 
        the file is properly opened and automatically closed after the block of code insidethe with statement 
        is executed, even if an exception occurs.This eliminates the need to explicitly call file.close() and 
        helps prevent resource leaks.⁡
        """
        with open(file_name, 'r') as file: # Open the file in read mode 
       
            print(file.read())
        break  # Exit the loop if the file is successfully opened and read
    except FileNotFoundError:
        print(f"File not found. You have {attempts - attempt - 1} attempts left.")
    except Exception as e:
        print(f"An error occurred: {e}. You have {attempts - attempt - 1} attempts left.")
else:
    print("All attempts are done. Failed to open the file.")
    
