n=int(input("please enter number between 0 and 100:\n"))  # Write the name on a new line
if n>= 0 and n <= 100:
    if n >= 90 and n <= 100:
        print("A+")
        
    elif n >= 80 and n < 90:
        print("A")
    elif n >= 70 and n < 80:
        print("A-")
        
    elif n >= 60 and n < 70:
        print("B")
        

    else:
        print("F")