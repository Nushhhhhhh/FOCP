# Modify your previous program so that the password must be between 8 and 12 characters (inclusive) long.

# input password
password1=input("Create a new password (8 to 12 character): ")
# cheking the length of the password
if len(password1)>=8 and len(password1)<= 12:
    password2=input("Re-enter your password: ")
    # checking if the password is same
    if password1 == password2:
        print("Password Set! Your password has been set sucessfully.")
    else:
        print("ERROR: Password is incorrect. Please try again.")
else:
    print("Password must be 8 to 12 characters long.")
