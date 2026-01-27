str_celsius = input('Type the temperature in °C: ')
celsius = float(str_celsius)
fahrenheit = (celsius * 9/5) + 32
kelvin = celsius + 273.15

print(f'The temperature of {celsius:.2f}°C is equivalent to {fahrenheit:.2f}°F and {kelvin:.2f}K.')