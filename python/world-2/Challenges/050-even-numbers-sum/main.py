sum_even = 0
for i in range(0, 6):
    num = int(input('Type a number: '))
    if num % 2 == 0:
        sum_even += num

print(f'The sum of the even numbers typed is {sum_even:,}.')
