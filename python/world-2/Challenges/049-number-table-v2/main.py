str_number = input('Type a number: ')
number = int(str_number)

print(f'Table of {number}:')
print('-' * 20)
for i in range(1, 11):
    print(f'{number:>2} x {i:<2} = {number * i}')
print('-' * 20)
