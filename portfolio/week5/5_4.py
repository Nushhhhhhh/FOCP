# Write a program that takes a URL as a command-line argument and reports whether or not there is a working website at that address.

import sys
import requests

def check_website_status(url):
    try:
        # send a get request to the URL
        response = requests.get(url)
        # checks if the status code is 200(OK)
        if response.status_code == 200:
            print(f"Website {url} is reachable and working.")
        else:
            print(f"Website {url} is not working.")
    except requests.exceptions.RequestException as exp:
        # handles exceptions
        print(f"Failed to reach {url}. Error: {exp}")
# checks if more than one url is provided
if len(sys.argv[1:]) != 1:
    print("Please provide only URL as a command-line argument.")
else:
    # gets URL from the command line argument.
    url = sys.argv[1]
    check_website_status(url)