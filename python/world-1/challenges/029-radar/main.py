str_car_speed = input('What is the speed of the car (in km/h)? ')
car_speed = float(str_car_speed)

if car_speed > 80:
    print('You have been fined for exceeding the speed limit of 80 km/h.')
    fine = (car_speed - 80) * 7
    print(f'Your fine is: ${fine:.2f}')
else:
    print('You are within the speed limit. Drive safely!')
