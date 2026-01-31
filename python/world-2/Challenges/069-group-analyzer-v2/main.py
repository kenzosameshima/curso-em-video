i = 0
older_than_18 = 0
total_men = 0
total_under_20_women = 0

while True:
    print(f'--- Registering person {i + 1} ---')

    while True:
        raw = (input('  Age: '))
        if raw.isdigit():
            age = int(raw)
            if 0 <= age <= 120:
                break
        print('Please enter a valid number.')

    while True:
        gender = input('  Gender (M/F): ').strip().upper()
        if gender in ['M', 'F']:
            break
        print('Please type M or F.')

    if age > 18:
        older_than_18 += 1

    if gender == 'M':
        total_men += 1
    elif gender == 'F' and age < 20:
        total_under_20_women += 1

    while True:
        continue_choice = input('Do you want to continue? (Y/N): ').strip().upper()
        if continue_choice in ['Y', 'N']:
            break
        print('Please type Y or N.')
        
    if continue_choice == 'N':
        break

    i += 1

print(f'Total people older than 18: {older_than_18}')
print(f'Total men registered: {total_men}')
print(f'Total women under 20 years old: {total_under_20_women}')
