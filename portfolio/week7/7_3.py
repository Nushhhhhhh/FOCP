# Write a program that manages a list of countries and their capital cities. It should prompt the user to enter the name of a country. If the 
# program already "knows" the name of the capital city, it should display it. Otherwise it should ask the user to enter it. This should carry on 
# until the user terminates the program (how this happens is up to you).

def countries_capitals():
    # dictionary with country as key and and its capital as value
    countries = {
        "wales": "cardiff",
        "england": "london",
        "france": "paris",
        "spain": "madrid",
        "italy": "rome"
        }
    # infinite loop that that runs until the user decides to quit
    while True:
        country = input("Enter a country ('quit' to exit): ")
        if country.lower() == 'quit':
            print("You have sucessfully exited the program.")
            break
        country_lower = country.lower() # converts user input into lower case
        # checks if the user input country exists in the dictionar(countries)
        if country_lower in countries:
            print(f"The capital of {country} is {countries[country_lower]}.")
        else:
            capital = input(f"Enter the capital of {country}: ")
            countries[country_lower] = capital.lower() # add country as key and and capital as value to the dictionary
            print(f"Added country {country} and its capital {capital} to the list.")
countries_capitals()