while True:
    gender = input('Enter your gender [M/F]: ').strip().upper()
    
    if gender in 'MF':
        break
    print('Invalid option! Please enter M or F.')

if gender == 'M':
    print('\033[1;34mYou have selected Male.\033[m')
else:
    print('\033[1;31mYou have selected Female.\033[m')
