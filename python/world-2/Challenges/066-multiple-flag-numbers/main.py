total_sum = 0
count = 0

while True:
    number = int(input('Type a number (999 to stop) '))
    if number == 999:
        break
    total_sum += number
    count += 1

print(f'You typed {count} numbers and the sum is {total_sum}')
