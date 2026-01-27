str_salary = input('Enter your current salary: ')
salary = float(str_salary)

if salary <= 1250:
    new_salary = salary * 1.15
    print(f'Your new salary after a 15% increase is: ${new_salary:.2f}')
else:
    new_salary = salary * 1.10
    print(f'Your new salary after a 10% increase is: ${new_salary:.2f}')
    