password=input("please enter your password:\n")  # Write the name on a new line
if password == "admin" or password == "root":
    print("success")
elif "@" in password and len(password) >= 6:
    print("good password but not strong")
else:
    print("rejected password")
