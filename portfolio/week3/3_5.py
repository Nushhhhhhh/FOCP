# Modify your program a final time so that it executes until the user successfully chooses a password. That is, if the password chosen 
# fails any of the checks, the program should return to asking for the password the first time.

# list of bad password
BAD_PASSWORDS = ['password', 'letmein', 'sesame', 'hello', 'justinbieber']
while True:
    # input password 
    password1=input("Create a new password (8 to 12 character): ")
    # check the length of the password
    if len(password1)>=8 and len(password1)<= 12:
        # check if the password is in the list
        if password1 not in BAD_PASSWORDS:
            password2=input("Re-enter your password: ")
            # check if both passwords are same
            if password1 == password2:
                print("Password Set! Your password has been set sucessfully.")
                # exit program if the password is set.
                break
            else:
                print("ERROR: Password is incorrect. Please try again.")
        else:
            print("Your password is too common. Choose a stronger password")
    else:
        print("Password must be 8 to 12 characters long.")
