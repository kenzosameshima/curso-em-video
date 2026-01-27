str_meters = input("Enter a distance in meters: ")
meters = float(str_meters)

kilometers = meters / 1000
hectometers = meters / 100
decameters = meters / 10
print(f'Kilometers: {kilometers} km, Hectometers: {hectometers} hm, Decameters: {decameters} dam')

decimeters = meters * 10
centimeters = meters * 100
millimeters = meters * 1000
print(f'Decimeters: {decimeters} dm, Centimeters: {centimeters} cm, Millimeters: {millimeters} mm')