str_kilometers = input('How many kilometers did you drive? ')
str_days = input('For how many days was the car rented? ')

kilometers = float(str_kilometers)
days = int(str_days)

cost_per_km = 0.15
cost_per_day = 60.0

total_cost = (kilometers * cost_per_km) + (days * cost_per_day)
print(f'The total cost of the car rental is: ${total_cost:.2f}')
