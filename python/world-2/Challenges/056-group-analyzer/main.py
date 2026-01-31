NUM_PEOPLE = 4

total_under_20_women = 0
total_age = 0
oldest_age = -1
oldest_man = None

for i in range(NUM_PEOPLE):
    print(f'Person {i + 1}:')
    name = input('  Name: ')
    age = int(input('  Age: '))
    gender = input('  Gender (M/F): ').strip().upper()
    print('---')

    total_age += age

    if gender == 'M':
        if age > oldest_age:
            oldest_age = age
            oldest_man = name
    elif gender == 'F' and age < 20:
        total_under_20_women += 1

average_age = total_age / NUM_PEOPLE

if oldest_man is not None:
    print(f'The oldest man is {oldest_man} with {oldest_age} years.')
else:
    print('There are no men in the group.')

print(f'Total women under 20 years old: {total_under_20_women}.')
print(f'Average age of the group: {average_age:.2f}')
