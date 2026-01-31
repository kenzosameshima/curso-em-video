number = int(input('Type a number (999 to stop) '))
total_sum = 0
count = 0

while number != 999:
    total_sum += number
    count += 1
    number = int(input('Type a number (999 to stop) '))
print(f'You typed {count} numbers and the sum is {total_sum}')
