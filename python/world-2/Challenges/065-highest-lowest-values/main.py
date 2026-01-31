answer = 'Y'
total = quantity = 0

while answer == 'Y':
    number = int(input('Type a number: '))
    total += number
    quantity += 1

    if quantity == 1:
        highest = lowest = number
    else:
        highest = max(highest, number)
        lowest = min(lowest, number)

    answer = input('Do you want to continue? [Y/N] ').strip().upper()[0]

average = total / quantity
print(f'You typed {quantity} numbers and the average is {average:.2f}')
print(f'The highest value typed was {highest} and the lowest was {lowest}')
