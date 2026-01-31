str_weight = input('Weight (kg): ').strip().replace(',', '.')
str_height = input('Height (m): ').strip().replace(',', '.')

weight = float(str_weight)
height = float(str_height)
bmi = weight / (height ** 2)

if bmi < 18.5:
    category = '\033[31mUNDERWEIGHT\033[m'
elif bmi < 25:
    category = '\033[32mNORMAL WEIGHT\033[m'
elif bmi < 30:
    category = '\033[33mOVERWEIGHT\033[m'
elif bmi < 35:
    category = '\033[31mOBESITY I (LOW-RISK)\033[m'
elif bmi < 40:
    category = '\033[31mOBESITY II (MODERATE-RISK)\033[m'
else:
    category = '\033[31mOBESITY III (HIGH-RISK/SEVERE/MORBID)\033[m'

print(f'BMI: {bmi:.2f} - Category: {category}')
