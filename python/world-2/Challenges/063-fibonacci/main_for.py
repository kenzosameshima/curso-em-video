number = int(input('Type the number of terms for the Fibonacci sequence: '))

t1, t2 = 0, 1

print('Fibonacci Sequence:')

for i in range(1, number + 1):
    print(f'{t1:,}', end=' → ' if i < number else ' → END\n')
    t3 = t1 + t2
    t1 = t2
    t2 = t3
