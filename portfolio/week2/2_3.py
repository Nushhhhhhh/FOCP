# The Head of Computing at the University of Poppleton is tasked with dividing a group of students into lab groups. A lab group is 
# usually 24 students, but this is sometimes varied to create groups of similar size. Write a program that prompts for the number of 
# students and group size, and then displays how many groups will be needed and how many will be left over in a smaller group.

student_num=int(input("Enter the number of student. "))
group_size=int(input("Enter the size of group. "))
no_of_group= student_num//group_size
student_leftover=student_num%group_size
print(f"The number of group that need to be created is {no_of_group} and {student_leftover} are leftover.")