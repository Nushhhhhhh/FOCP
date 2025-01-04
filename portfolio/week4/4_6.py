# Write a program that takes a centigrade temperature and displays the equivalent in fahrenheit. The input should be a number followed 
# by a letter C. The output should be in the same format.

# function to convert Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    temp=float(celsius[:-1])
    return (temp * 9/5) + 32
# user defined input
celsius_temperature = input("Enter temperature in celcius ")
# condition to check if there is c followed by the temperature
if celsius_temperature[-1:]== "C" or celsius_temperature[-1:]== "c": # slicing to take the last character of the string
    fahrenheit_conversion = celsius_to_fahrenheit(celsius_temperature)
    print(f"{celsius_temperature} degrees Celsius is equal to {fahrenheit_conversion} degrees Fahrenheit.")
else:
    print("Invalid input. Please enter temperature followed by C.")