str_decimal_number = input("Enter a decimal number to convert: ")
str_base = input("Enter the base to convert to (2 for binary, 8 for octal, 16 for hexadecimal): ")

decimal_number = int(str_decimal_number)
base = int(str_base)

if base == 2:
    converted_number = bin(decimal_number)[2:]
    print(f"The number {decimal_number} in binary is: {converted_number}")
elif base == 8:
    converted_number = oct(decimal_number)[2:]
    print(f"The number {decimal_number} in octal is: {converted_number}")
elif base == 16:
    converted_number = hex(decimal_number)[2:].upper()
    print(f"The number {decimal_number} in hexadecimal is: {converted_number}")
else:
    print("Invalid base! Please enter 2, 8, or 16.")
