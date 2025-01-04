# The Head of Computing at the University of Poppleton is tasked with dividing a group of students into lab groups. A lab group is 24 
# students, since this is the number of PCs in a lab. Write a program that calculates how many groups are needed for the following 
# number of students: 113, 175, 12. Display how many full groups there will be, and how many students will be in the smaller "le over" 
# group.

groupsize = 24
studentno1 = 113
studentno2 = 175
studentno3 = 12
firstgroup = studentno1 // groupsize
secondgroup = studentno2 // groupsize
thirdgroup = studentno3 // groupsize
total_groups = firstgroup + secondgroup + thirdgroup
leftover1 = studentno1 % groupsize
leftover2 = studentno2 % groupsize
leftover3 = studentno3 % groupsize
total_leftover = leftover1 + leftover2 + leftover3
print(f"The total number of groups will be {total_groups} with {total_leftover} leftover students.")