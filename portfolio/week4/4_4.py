# When processing data it is often useful to remove the last character from some input (it is often a newline). Write and test a function 
# that takes a string parameter and returns it with the last character removed. (If the string contains one or fewer characters, return
# it unchanged.)

# fuction to remove last character of the string entered
def remove_last_character(string):
    if len(string) > 1:
        return string[:-1]
    else:
        return string
# user input
user_input = input("Enter a string: ")
# calls the function
remove_char = remove_last_character(user_input)
print(f"Processed string: {remove_char}")