str_side1 = input('Enter the length of the first side of the triangle: ')
str_side2 = input('Enter the length of the second side of the triangle: ')
str_side3 = input('Enter the length of the third side of the triangle: ')

side1 = float(str_side1)
side2 = float(str_side2)
side3 = float(str_side3)

if side1 < side2 + side3 and side2 < side1 + side3 and side3 < side1 + side2:
    print('The lengths can form a triangle.')
else:
    print('The lengths cannot form a triangle.')
    