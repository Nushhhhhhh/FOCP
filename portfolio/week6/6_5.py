# Another way to hide a message is to include the letters that make it up within seemingly random text. The letters of the message might be every 
# fih character, for example. Write and test a function that does such encryption. It should randomly generate an interval (between 2 and 20), space 
# the message out accordingly, and should fill the gaps with random letters. The function should return the encrypted message and the interval used

import random
def encrypt_message():
    message=input("Enter a message: ")
    og_msg= message
    alpha= ["a","i","j","g","f","t","h","v","e","c","t","n","u","b","k","d","l","m","o","q"] # list of random letter
    interval = random.randint(2,20) # picks a random interval between 2 to 20
    fillers="" # empty string
    for i in range(interval):
        letter= random.choice(alpha) # chooses random letter from alpha list
        fillers= fillers+letter
        i= i+1
    message=message.replace(" ",fillers) # replaces space with fillers
    print(f"Original message: {og_msg}")
    print(f"Encrypted message: {message}")    
    print(f"Interval: {interval}") 
encrypt_message()