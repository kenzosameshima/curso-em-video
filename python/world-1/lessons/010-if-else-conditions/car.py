str_car_age = input('How old is your car? ')
car_age = int(str_car_age)

print('new car' if car_age <= 3 else 'old car')

if car_age <= 3:
    print('Your car is new.')
else:
    print('Your car is old.')
