first_term = int(input('Type the first term of the AP: '))
difference = int(input('Type the common difference: '))
total_terms = int(input('How many terms do you want to show? '))

for i in range(total_terms):
    term = first_term + i * difference
    print(f'{term} → ', end='')
print('END')
