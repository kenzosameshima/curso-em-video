start = int(input('Start: '))
end = int(input('End: '))
step = int(input('Step: '))

for i in range(start, end + 1, step):
    print(i, end=', ')
print('END')

sum = 0
for i in range(0, 4):
    number = int(input('Enter a value: '))
    sum += number
print(f'The sum of the values is {sum}')
