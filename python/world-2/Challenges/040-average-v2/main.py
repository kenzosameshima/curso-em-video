str_grade1 = input("Enter the first grade: ")
str_grade2 = input("Enter the second grade: ")

grade1 = float(str_grade1)
grade2 = float(str_grade2)

average = (grade1 + grade2) / 2

if average < 5.0:
    print(f"Your average is {average:g}. You are \033[31mREPROVED\033[0m.")
elif 5.0 <= average < 7.0:
    print(f"Your average is {average:g}. You are in \033[33mRECOVERY\033[0m.")
else:
    print(f"Your average is {average:g}. You are \033[32mAPPROVED\033[0m.")
