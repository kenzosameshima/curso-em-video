full_name = input("Enter your full name: ").strip()
first_name = full_name.title().split()[0]
last_name = full_name.title().split()[-1]

print(f"Nice to meet you, {first_name}!")
print(f"Your last name is {last_name}, right?")
