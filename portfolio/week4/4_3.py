# Modify your "greetings" program so that the first letter of the name entered is always in uppercase with the rest in lowercase. This 
# should happen even if the user entered their name dierently. So if the user entered arthur, ARTHUR, or even arTHur the name should be 
# displayed as Arthur

# function to format the name
def format_name(name):
    return name.capitalize() # capitalize the first letter of the name and all other subsequent numbers are lowercased
# get user input
name = input("Enter your name: ")
if name=="":
	print("Hello, stranger!")
else:
    print(f"Hello, {format_name(name)}!")