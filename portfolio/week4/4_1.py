# Functions are often used to validate input. Write a function that accepts a single integer as a parameter and returns True if the 
# integer is in the range 0 to 100(inclusive), or False otherwise. Write a short program to test the function

# fuction to check if the num is between 1 to 100
def integer_check(num):
    return 0<= num <=100
# user input number
num=int(input("Enter a number. "))
# condition to print if the number ranges from 1 to 100 or not
if integer_check(num):
    print(f"{num} ranges from 1 to 100")
else:
    print(f"{num} doesn't range from 1 to 100")