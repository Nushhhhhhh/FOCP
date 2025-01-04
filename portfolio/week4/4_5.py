# Write and test a function that converts a temperature measured in degrees centigrade into the equivalent in fahrenheit, and another 
# that does the reverse conversion. Test both functions. (Google will find you the formulae).

# function to convert Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32
# function to convert Fahrenheit to Celsius
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9
# user defined input
celsius_temperature = float(input("Enter temperature in celcius "))
fahrenheit_temperature = float(input("Enter temperature in fahrenheit "))
# calls the fuction 
fahrenheit_conversion = celsius_to_fahrenheit(celsius_temperature)
celsius_conversion = fahrenheit_to_celsius(fahrenheit_temperature)
print(f"{celsius_temperature} degrees Celsius is equal to {fahrenheit_conversion} degrees Fahrenheit.")
print(f"{fahrenheit_temperature} degrees Fahrenheit is equal to {celsius_conversion} degrees Celsius.")