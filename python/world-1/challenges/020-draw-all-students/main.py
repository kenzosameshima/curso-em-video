from random import shuffle

student1 = input("Enter the name of the first student: ")
student2 = input("Enter the name of the second student: ")
student3 = input("Enter the name of the third student: ")
student4 = input("Enter the name of the fourth student: ")

students = [student1, student2, student3, student4]
shuffle(students)

print("The order of students is:")
print(students)
