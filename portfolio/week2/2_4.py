# A kindly teacher wishes to distribute a tub of sweets between her pupils. She will first count the sweets and then divide them 
# according to how many pupils attend that day. Write a program that will tell the teacher how many sweets to give to each pupil, and 
# how many she will have left over.

sweets=int(input("Enter the number of sweets "))
pupil=int(input("Enter the number of pupils "))
per_pupil_sweet= sweets//pupil
sweet_leftover=sweets%pupil
print(f"Each pupil will get {per_pupil_sweet} sweet while {sweet_leftover} will be leftover.")