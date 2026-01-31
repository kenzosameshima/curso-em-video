str_decimal_number = input("Enter a decimal number to convert: ")
str_base = input("Enter the base to convert to (2 for binary, 8 for octal, 16 for hexadecimal): ")

decimal_number = int(str_decimal_number)
base = int(str_base)

digits = "0123456789ABCDEF"

if base in (2, 8, 16):
    if decimal_number == 0:
        converted_number = "0"
    else:
        converted_number = ""
        number = decimal_number

        while number > 0:
            remainder = number % base
            converted_number = digits[remainder] + converted_number
            number //= base

    print(f"The number {decimal_number} in base {base} is: {converted_number}")
else:
    print("Invalid base! Please enter 2, 8, or 16.")
