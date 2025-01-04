# In a long career for Yorkshire, Georey Boycott played 609 matches, batted 1014 times, was not out 162 times, and scored 48426 runs. 
# Write a program to calculate and display Boycott's batting average.

matches = 609 
batted = 1014
notout  = 162
runs = 48426
battingAverage = runs / (batted - notout)
print(f"The batting average of Geoffrey Boycott is {battingAverage}")