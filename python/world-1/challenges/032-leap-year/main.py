from datetime import date

str_year = input('Enter a year to check if it is a leap year: ')

if str_year.strip() == '':
    year = date.today().year

if str_year.strip() != '':
    year = int(str_year)

if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    if year < date.today().year:
        print(f'The year {year} was a leap year.')
    elif year > date.today().year:
        print(f'The year {year} will be a leap year.')
    else:
        print(f'This year ({year}) is a leap year.')
else:
    if year < date.today().year:
        print(f'The year {year} was not a leap year.')
    elif year > date.today().year:
        print(f'The year {year} will not be a leap year.')
    else:
        print(f'This year ({year}) is not a leap year.')
    