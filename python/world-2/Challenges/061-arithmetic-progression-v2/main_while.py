first_term = int(input('Type the first term of the AP: '))
difference = int(input('Type the common difference: '))
total_terms = int(input('How many terms do you want to show? '))

while total_terms > 0:
    print(f'{first_term} → ', end='')
    first_term += difference
    total_terms -= 1
print('END')
