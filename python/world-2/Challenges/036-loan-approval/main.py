str_house_value = input("Enter the house value: $ ")
str_salary = input("Enter your monthly salary: $ ")
str_years = input("Enter the number of years to pay off the loan: ")

house_value = float(str_house_value)
salary = float(str_salary)
years = int(str_years)

monthly_payment = house_value / (years * 12)

if monthly_payment > (salary * 0.3):
    print("Loan denied! The monthly payment exceeds 30% of your salary.")
else:
    print("Loan approved! You can afford the monthly payment.")
    print(f"Your monthly payment will be: $ {monthly_payment:.2f}")
