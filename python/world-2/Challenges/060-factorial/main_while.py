number = int(input('Type a number to calculate its factorial: '))
factorial = 1
i = number

while i > 0:
    factorial *= i
    i -= 1

print(f'{number}! = {factorial:,}')
