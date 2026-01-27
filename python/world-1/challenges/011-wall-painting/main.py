str_length = input('Enter the length of the wall in meters: ')
str_height = input('Enter the height of the wall in meters: ')

length = float(str_length)
height = float(str_height)
area = length * height

# paint = 2m² per liter
paint_needed = area / 2

print(f'To paint a wall with {area:.2f}m², you will need {paint_needed:.2f} liters of paint.')
