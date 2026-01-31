import math

a = float(input('First side: '))
b = float(input('Second side: '))
c = float(input('Third side: '))

if a < b + c and b < a + c and c < a + b:
    print('The segments above CAN FORM A TRIANGLE.')

    if a == b == c:
        side_type = 'EQUILATERAL'
    elif a != b and b != c and a != c:
        side_type = 'SCALENE'
    else:
        side_type = 'ISOSCELES'

    print(f'Side type: {side_type}')

    angle_A = math.degrees(math.acos((b**2 + c**2 - a**2) / (2 * b * c)))
    angle_B = math.degrees(math.acos((a**2 + c**2 - b**2) / (2 * a * c)))
    angle_C = math.degrees(math.acos((a**2 + b**2 - c**2) / (2 * a * b)))

    print('Angles:')
    print(f'A = {angle_A:.2f}°')
    print(f'B = {angle_B:.2f}°')
    print(f'C = {angle_C:.2f}°')

    angles = [angle_A, angle_B, angle_C]

    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    print(f'Area: {area:.2f}')

    eps = 1e-6

    if any(abs(angle - 90) < eps for angle in angles):
        angle_type = 'RIGHT'
    elif any(angle > 90 for angle in angles):
        angle_type = 'OBTUSE'
    else:
        angle_type = 'ACUTE'

    print(f'Angle type: {angle_type}')

else:
    print('The segments above CANNOT FORM A TRIANGLE.')
