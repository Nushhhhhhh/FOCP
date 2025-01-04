# Modify the previous program so that it can process any number of values. The input terminates when the user just pressed "Enter" at the prompt 
# rather than entering a value.

# function calculating maximum, minimum, and mean temperature
def calculate_maxminmean(fahrenheit):
    max_temp = max(fahrenheit)
    min_temp = min(fahrenheit)
    mean_temp = sum(fahrenheit) / len(fahrenheit)
    return max_temp, min_temp, mean_temp
# creating lists for Celsius and Fahrenheit temperatures
celsius_temperature = []
fahrenheit_temperature = []
# looping to take temperatures until the user presses "Enter" without a value
while True:
    temperature = input("Enter temperature in Celsius or press Enter to stop: ")
    # checking if the value is entered or not
    if temperature == "":  # exit the loop if the input is empty
        break
    if temperature[-1:]== "C" or temperature[-1:]== "c":  # slicing to check the last character is c or not
        input_value = float(temperature[:-1]) # slicing to only take numeric value
        celsius_temperature.append(input_value) # adding value to the list
        fahrenheit_conversion = (input_value * 9/5) + 32
        fahrenheit_temperature.append(fahrenheit_conversion) 
    else:
        print("Invalid input. Please enter temperature followed by 'C'.")
# check if any temperature is entered
if celsius_temperature:
    # calls the function calculate_maxminmean() with fahrenheit_temperature as argument
    maximum_temperature, minimum_temperature, mean_temperature = calculate_maxminmean(fahrenheit_temperature)
    print(f"Celsius Temperature:{celsius_temperature} is equal to Fahrenheit Temperatures:{fahrenheit_temperature} respectively.")
    print(f"Maximum Temperature: {maximum_temperature}")
    print(f"Minimum Temperature: {minimum_temperature}")
    print(f"Mean Temperature: {mean_temperature}")
else:
    print("There was no temperature entered.")
