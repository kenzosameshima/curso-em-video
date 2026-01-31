first_term = int(input('Type the first term of the AP: '))
difference = int(input('Type the common difference: '))
initial_terms = int(input('How many terms do you want to show initially? '))

total_terms = 0
current_term = first_term
i = 1

while i <= initial_terms:
    print(f'{current_term} → ', end='')
    current_term += difference
    total_terms += 1
    i += 1

print('PAUSE')

more_terms = int(input('How many more terms do you want to show? '))

while more_terms != 0:
    i = 1
    while i <= more_terms:
        print(f'{current_term} → ', end='')
        current_term += difference
        total_terms += 1
        i += 1

    print('PAUSE')
    more_terms = int(input('How many more terms do you want to show? '))

print(f'Total terms shown: {total_terms}')
print('END')
