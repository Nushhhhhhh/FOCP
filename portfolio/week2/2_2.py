#WAP that prompts a user to enter a temperature in Celsius, and then displays the corresponding temperature in Fahrenheit.

ctemp=float(input("Enter temperature in celcius. "))
ftemp=(ctemp*1.8)+32
print(f"{ctemp}C is equivalent to {ftemp}F.")