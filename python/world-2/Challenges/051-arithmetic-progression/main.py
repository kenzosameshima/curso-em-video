str_number = input('Type a number: ')
str_difference = input('Type the common difference: ')
number = int(str_number)
difference = int(str_difference)

print(f'The first 10 terms, besides a0, of the arithmetic progression are:')
for i in range(0, 11):
    term = number + i * difference
    print(term, end=' → ')
print('\nEND')
