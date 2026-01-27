str_num1 = input('Enter the first number: ')
str_num2 = input('Enter the second number: ')
str_num3 = input('Enter the third number: ')

num1 = float(str_num1)
num2 = float(str_num2)
num3 = float(str_num3)

highest = num1
if num2 > highest:
    highest = num2
if num3 > highest:
    highest = num3

lowest = num1
if num2 < lowest:
    lowest = num2
if num3 < lowest:
    lowest = num3

if num1 == num2 and num1 == num3:
    print('All values entered are equal.')

print(f'The highest value entered is: {highest:g}')
print(f'The lowest value entered is: {lowest:g}')
