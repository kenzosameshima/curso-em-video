str_km = input('Enter the travel distance in kilometers: ')
km = float(str_km)

if km <= 200:
    cost = km * 0.50
else:
    cost = km * 0.45

print(f'The total cost of the trip is: ${cost:.2f}')
