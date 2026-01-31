number1 = int(input('Type the first number: '))
number2 = int(input('Type the second number: '))
option = 0

while option != 5:
    print('''\nChoose an option:
    [1] Sum
    [2] Multiply
    [3] Find the greater number
    [4] Enter new numbers
    [5] Exit the program
          ''')
    option = int(input('Your choice: '))

    if option == 1:
        result = number1 + number2
        print(f'The sum of {number1} and {number2} is {result}.')
    elif option == 2:
        result = number1 * number2
        print(f'The multiplication of {number1} and {number2} is {result}.')
    elif option == 3:
        if number1 > number2:
            print(f'The greater number between {number1} and {number2} is {number1}.')
        elif number2 > number1:
            print(f'The greater number between {number1} and {number2} is {number2}.')
        else:
            print(f'Both numbers are equal: {number1}.')
    elif option == 4:
        number1 = int(input('Type the first number: '))
        number2 = int(input('Type the second number: '))
    elif option == 5:
        print('Exiting the program. Goodbye!')
        break
