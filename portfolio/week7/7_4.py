# One approach to analysing some encrypted data where a substitution is suspected is frequency analysis. A count of the dierent symbols in the 
# message can be used to identify the language used, and sometimes some of the letters. In English, the most common letter is "e", and so the 
# symbol representing "e" should appear most in the encrypted text. Write a program that processes a string representing a message and reports the 
# six most common letters, along with the number of times they appear. Case should not matter, so "E" and "e" are considered the same.

def frequency_analysis(message):
    # empty dictionary 
    letter_counts = {}
    # loop through each character in the user input string(message)
    for char in message.lower(): #convers message in to lowercase
        if char.isalpha():  # only count alphabetic characters
            # checks if the character is in the dictionary(letter_count) and adds count of the character
            if char in letter_counts:
                letter_counts[char] += 1
            else:
                letter_counts[char] = 1
    # converts the dictionary to tuple and sort it from most to least frequency
    sorted_letter_count = sorted(letter_counts.items(), key=lambda x: x[1], reverse=True)
    # display six most common letters and their counts
    print("The six most common letters and their counts are:")
    for letter, count in sorted_letter_count[:6]:  # slicing the first 6 elements
        print(f"{letter}: {count}")
message = input("Enter a message ")
frequency_analysis(message)
