# Write a function that accepts a positive integer as a parameter and then returns a representation of that number in binary (base 2).

def dec_to_bin(number):
    binary = "" # empty string
    # checking if the user given number is negative
    if number<0:
        print("Please enter a positive integer!")
    # loop to convert decimal number into binary number
    while number > 0:
        remainder=number % 2 #gives remainder
        binary = str(remainder) + binary
        number = number // 2 # division without decimal
    return binary
num = int(input("Enter a positive integer: "))
binary_number=dec_to_bin(num)
# check if valid result is given
if binary_number:
    print("The equivalent binary of the integer is", binary_number)