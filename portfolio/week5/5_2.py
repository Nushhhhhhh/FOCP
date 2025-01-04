# Write a program that, when run from the command line, reports how many arguments were provided. (Remember that the program name itself is not an 
# argument).

import sys
def count_args():
    # substacting 1 to exclude program name
    num_of_args = len(sys.argv[1:])
    print(f"{num_of_args} arguments were provided.")
count_args()