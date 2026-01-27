str_salary = input('What is the current salary? $ ')
salary = float(str_salary)
increase_amount = salary * 0.15
new_salary = salary + increase_amount

print(f'The current salary is $ {salary:.2f}. With a 15% increase(${increase_amount:.2f}), the new salary will be $ {new_salary:.2f}.')