# Computers are commonly used in encryption. A very simple form of encryption (more accurately "obfuscation") would be to remove the spaces from a 
# message and reverse the resulting string. Write, and test, a function that takes a string containing a message and "encrypts" it in this way.

def encrypt(message):
    # remove spaces from the string
    remove_space = message.replace(" ", "")
    # reverse the string
    reverse_message = remove_space[::-1]
    return reverse_message
user_string = input("Enter a message to encrypt: ")
encrypted_message = encrypt(user_string)
print("Encrypted message: ", encrypted_message)
