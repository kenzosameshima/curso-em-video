var = input('Type something: ')

print(f"Is it printable? {var.isprintable()}")
print(f"Is it only space(s)? {var.isspace()}")

print(f"Is it ASCII? {var.isascii()}")

print(f"Is it identifier? {var.isidentifier()}")

print(f"Is it alphabetic? {var.isalpha()}")
print(f"Is it alphanumeric? {var.isalnum()}")

print(f"Is it decimal? {var.isdecimal()}")
print(f"Is it digit? {var.isdigit()}")
print(f"Is it numeric? {var.isnumeric()}")

print(f"Is it lowercase? {var.islower()}")
print(f"Is it uppercase? {var.isupper()}")
print(f"Is it titlecase? {var.istitle()}")
