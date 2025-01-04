# Modify the "Times Table" again so that the user still enters the number of the table, but if this number is negative the table is 
# printed backwards. So entering "-7" would produce the Seven Times Table starting at "12 times" down to "0 times".

# input a number for times table 
num= int(input("Enter a number. "))
# check if the value is positve or negative 
if num>=0: 
    # looping to display table
    for i in range(13):
        prod=i*num
        print(f"{num}*{i}={prod}")
        i=i+1
else:
    # looping the table from opposite as the value is in negative
    for i in range(12,-1,-1):
        prod=i*num
        print(f"{num}*{i}={prod}")

