# -----------------------------------
# --      Exceptions Handling      --
# -- Try | Except | Else | Finally --
# -----------------------------------
# Try     => Test The Code For Errors
# Except  => Handle The Errors If Its Found
# ----------------------------
# Else    => If No Errors Run The Code
# Finally => Run The Code No Matter What
# ------------------------

number = int(input("Write Your Age: "))

print(number)
print(type(number)) 

try:  # Try The Code and Test Errors 

  number = int(input("Write Your Age: "))

  print("Good, This Is Integer From Try")

except:  # Handle The Errors If Its Found

  print("Bad, This is Not Integer")

else:  # If Theres No Errors

  print("Good, This Is Integer From Else") # Run The Code if there is no errors

finally:

  print("Print From Finally Whatever Happens") # Run The Code No Matter What


try:

   #print(10 / 0)
   #print(x)
   print(int("Hello"))

except ZeroDivisionError: #to know the type of error we just run the code and see the error type in the terminal or in the output 

  print("Cant Divide")

except NameError:

  print("Identifier Not Found")

except ValueError: # we tried multiple errors types so any error will match the except will run the print message that belongs to it

  print("Value Error Elzero")

except: #any other error

  print("Error Happens")









                                                               
