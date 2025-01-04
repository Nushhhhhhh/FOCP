# Last week you wrote a program that processed a collection of temperature readings entered by the user and displayed the maximum, minimum, and 
# mean. Create a version of that program that takes the values from the command-line instead. Be sure to handle the case where no arguments are 
# provided!

import sys
def calculate_maxminmean(fahrenheit):
    max_temp = max(fahrenheit)
    min_temp = min(fahrenheit)
    mean_temp = sum(fahrenheit) / len(fahrenheit)
    return max_temp, min_temp, mean_temp
if len(sys.argv[1:]) < 2:
    print("Sufficient temperature values were provided.")
else:
    temperatures_celsius = []
# loop over the command-line arguments 
for temperature in sys.argv[1:]:
    temperatures_celsius.append(float(temperature))
# empty list to store temperatures in Fahrenheit.
temperatures_fahrenheit = []
# convert Celsius to Fahrenheit using loop.
for temp in temperatures_celsius:
    fahrenheit_conversion = (temp * 9/5) + 32
    temperatures_fahrenheit.append(fahrenheit_conversion)
maximum_temperature, minimum_temperature, mean_temperature = calculate_maxminmean(temperatures_fahrenheit)
print(f"Celsius Temperature:{temperatures_celsius} is equal to Fahrenheit Temperatures:{temperatures_fahrenheit} respectively.")
print(f"Maximum Temperature is {maximum_temperature}")
print(f"Minimum Temperature is {minimum_temperature}")
print(f"Mean Temperature is {mean_temperature}")
   
    