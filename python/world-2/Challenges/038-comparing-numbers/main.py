str_number1 = input("Enter the first number: ")
str_number2 = input("Enter the second number: ")

number1 = int(str_number1)
number2 = int(str_number2)

if number1 > number2:
    print(f"{number1} > {number2}")
elif number1 < number2:
    print(f"{number1} < {number2}")
else:
    print(f"{number1} = {number2}")
