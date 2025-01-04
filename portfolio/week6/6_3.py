# Write and test a function that determines if a given integer is a prime number. A prime number is an integer greater than 1 that cannot be 
# produced by multiplying two other integers.

def prime_number(num):
    # prime number is greater tha 1
    if num > 1:
        # loops from 2 to num-1
        for i in range(2, num):
            if num % i == 0: # if divisible by any number it is not a prime
                return False
        else:
            return True
    else:
        return False
number = int(input("Enter a positive integer: "))
is_prime_number=prime_number(number)
# checks if the function returned true or false and displays the result
if is_prime_number:
    print(f"{number } is a prime number.")
else:
    print(f"{number } is not a prime number.")