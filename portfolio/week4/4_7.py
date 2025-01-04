# Write a program that reads 6 temperatures (in the same format as before), and displays the maximum, minimum, and mean of the values.
# function to convert Celsius to Fahrenheit

# function calculating maximum minimum and mean temperature
def calculate_maxminmean(fahrenheit):
    max_temp = max(fahrenheit)
    min_temp = min(fahrenheit)
    mean_temp = sum(fahrenheit) / len(fahrenheit)
    return max_temp, min_temp, mean_temp
# creating list 
celsius_temperature = []
fahrenheit_temperature = []
# looping to take 6 temperature 
for i in range(6):
    while True:
        temperature = input(f"Enter temperature {i + 1} in celsius ")
        if temperature[-1:]== "C" or temperature[-1:]== "c":  # slicing to check the last character is c or not
            input_value = float(temperature[:-1]) # slicing to only take numeric value
            celsius_temperature.append(input_value) # adding value to the list
            fahrenheit_conversion = (input_value * 9/5) + 32
            fahrenheit_temperature.append(fahrenheit_conversion)
            break    
        else:
            print("Invalid input. Please enter temperature followed by 'C'.")
# calls function calculatemixminmean() with fahrenheit_temperature as argument
maximum_temperature, minimum_temperature, mean_temperature = calculate_maxminmean(fahrenheit_temperature)
print(f"Celsius Temperature:{celsius_temperature} is equal to Fahrenheit Temperatures:{fahrenheit_temperature} respectively.")
print(f"Maximum Temperature is {maximum_temperature}")
print(f"Minimum Temperature is {minimum_temperature}")
print(f"Mean Temperature is {mean_temperature}")