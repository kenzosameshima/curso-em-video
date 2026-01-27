str_number = input('Enter a number between 0 and 9999: ')

# string analysis
print('Analyzing the number...')
print('-' * 30, '\n')


str_number = str_number.zfill(4)
thousands = str_number[0]
hundreds = str_number[1]
tens = str_number[2]
ones = str_number[3]

print('Using string indexing:\n')
print(f'The thousands digit is: {thousands}')
print(f'The hundreds digit is: {hundreds}')
print(f'The tens digit is: {tens}')
print(f'The ones digit is: {ones}')

# integer analysis
number = int(str_number)
thousands_int = number // 1000
hundreds_int = (number // 100) % 10
tens_int = (number // 10) % 10
ones_int = number % 10

print('\nUsing integer arithmetic:\n')
print(f'The thousands digit is: {thousands_int}')
print(f'The hundreds digit is: {hundreds_int}')
print(f'The tens digit is: {tens_int}')
print(f'The ones digit is: {ones_int}')
