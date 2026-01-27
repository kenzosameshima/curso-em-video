str_num = input('Enter a number: ')
num = float(str_num)
integer_part = int(num)
fractional_part = round(num - integer_part, 3)

print(f'The typed number is {num}, its integer part is {integer_part} and its fractional part is {fractional_part}')
