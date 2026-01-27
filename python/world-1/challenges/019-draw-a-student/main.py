from random import choice

student1 = input("Enter the name of the first student: ")
student2 = input("Enter the name of the second student: ")
student3 = input("Enter the name of the third student: ")
student4 = input("Enter the name of the fourth student: ")

students = [student1, student2, student3, student4]
selected_student = choice(students)

print(f"The selected student is: {selected_student}")
