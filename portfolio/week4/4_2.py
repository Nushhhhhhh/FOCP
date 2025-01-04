# Write a function that has a single string as its parameter, and returns the number of uppercase letters, and the number of lowercase 
# letters in the string. Test the function with a short program.

# fuction adding the total number of uppercaswe and lower case
def count_cases(string):
    upper = sum(1 for char in string if char.isupper())
    lower = sum(1 for char in string if char.islower())
    return upper, lower
# string input
user_string = input("Enter a string: ")
# calls count_cases function with user string as  the argument 
uppercase_count, lowercase_count = count_cases(user_string)
print(f"Total uppercase letters: {uppercase_count}")
print(f"Total lowercase letters: {lowercase_count}")