from datetime import date

current_year = date.today().year
adults = minors = 0

for i in range(7):
    birth_year = int(input('Enter the year of birth: '))
    age = current_year - birth_year
    if age >= 21:
        print(f'Person {i+1} is an adult.')
        adults += 1
    else:
        print(f'Person {i+1} is a minor.')
        minors += 1
print(f'\nTotal adults: {adults}')
print(f'Total minors: {minors}')
