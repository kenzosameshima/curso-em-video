str_grade1 = input('Enter the first grade: ')
str_grade2 = input('Enter the second grade: ')

grade1 = float(str_grade1)
grade2 = float(str_grade2)

average = (grade1 + grade2) / 2
print(f'Your average grade is {average:.2f}')

if average < 7:
    print('You are reproved, study more!')
else:
    print('You are approved, congratulations!')
