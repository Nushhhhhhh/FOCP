# Write a program that simulates the way in which a user might choose a password. The program should prompt for a new password, and then 
# prompt again. If the two passwords entered are the same the program should say "Password Set" or similar, otherwise it should report 
# an error.

# input password values
password1=input("Create a new password. ")
password2=input("Re-enter your password. ")
# checking if the password is same 
if password1 == password2:
    print("Password Set! Your password has been set sucessfully.")
else:
    print("ERROR: Password is incorrect. Please try again.")

