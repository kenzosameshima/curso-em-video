result = 0
numbers = 0

for i in range(3, 501, 6):
    result += i
    numbers += 1

print(f'The sum of all odd multiples of 3 between 1 and 500 is {result} and there are {numbers} numbers in total.')

# could also be:

"""
result = sum(range(3, 501, 6))
numbers = len(range(3, 501, 6))

print(f'The sum of all odd multiples of 3 between 1 and 500 is {result} and there are {numbers} numbers in total.')
"""