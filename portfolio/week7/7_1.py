# Write and test a function that takes a string as a parameter and returns a sorted list of all the unique letters used in the string. So, if the 
# string is cheese, the list returned should be ['c', 'e', 'h', 's'].

def unique_sorted_letters(user_string):
    remove_duplictes =set(user_string) # removes duplicate letters from the string
    sorted_letters = sorted(remove_duplictes) # sorts the list alphabetically
    return sorted_letters   
string = input("Enter a string: ")
# calls the function
sorted_letters=unique_sorted_letters(string)
print(f"The unique letters in {string} is: {sorted_letters}")