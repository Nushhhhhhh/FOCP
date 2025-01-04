# Write and test a function that takes an integer as its parameter and returns the factors of that integer. (A factor is an integer which can be 
# multiplied by another to yield the original).

def find_factors(num):
        # checks if the user is positive
        if num <= 0:
            print("Please enter a positive integer except zero.")
        # empty list to store factors
        factors=[]
        # loops from 1 to the the number that user inputs
        for i in range(1, num + 1):
            # checks if the i is factor of the number
            if num % i == 0:
                factors.append(i) # adds element to the list
        return factors
number = int(input("Enter a positive integer: "))
factors_of_number=find_factors(number)
# checks if the factors were sucessfully found and then displays the result
if factors_of_number:
     print(f"The factors of {number} are: {factors_of_number}")