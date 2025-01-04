# Modify your "Times Table" program so that the user enters the number of the table they require. This number should be between 0 and 12
# inclusive.

# input a value for times table
num= int(input("Enter a number between 0 to 12. "))
# checking if the num is between 0 to 12
if num>=0 and num<=12: 
    # looping to display table
    for i in range(13):
        prod=i*num
        print(f"{num}*{i}={prod}")
        i=i+1
else:
    print("The number entered is not between 0 to 12.")