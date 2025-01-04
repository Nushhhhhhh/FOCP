# Write a program that displays the "Seven Times Table". That is, the result of multiplying 7 by every number from 0 to 12 inclusive.

# loops the code 12 times
for i in range(13):
    prod=i*7
    print(f"{i}*7={prod}")
    i=i+1