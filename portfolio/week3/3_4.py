# Modify your program again so that the chosen password cannot be one of a list of common passwords, defined thus:
# BAD_PASSWORDS = ['password', 'letmein', 'sesame', 'hello', 'justinbieber']

# list of bad password
BAD_PASSWORDS = ['password', 'letmein', 'sesame', 'hello', 'justinbieber']
# input password 
password1=input("Create a new password (8 to 12 character): ")
# check the length of the password
if len(password1)>=8 and len(password1)<= 12:
    # check if the password is in the list
    if password1 not in BAD_PASSWORDS:
        password2=input("Re-enter your password: ")
        #check if both passwords are same
        if password1 == password2:
            print("Password Set! Your password has been set sucessfully.")
        else:
            print("ERROR: Password is incorrect. Please try again.")
    else:
        print("Your password is too common. Choose a stronger password")
else:
    print("Password must be 8 to 12 characters long.")
