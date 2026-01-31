number = int(input('Type the number of terms for the Fibonacci sequence: '))

t1, t2 = 0, 1
i = 1

print('Fibonacci Sequence:')

while i <= number:
    print(f'{t1:,}', end=' → ' if i < number else ' → END\n')
    t3 = t1 + t2
    t1 = t2
    t2 = t3
    i += 1