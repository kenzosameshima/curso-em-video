full_name = input("Enter your full name: ")
print("Analyzing your name...")
print('-' * 50, '\n')

upper = full_name.upper()
lower = full_name.lower()
count_letters = len(full_name) - full_name.count(' ')
first_name = full_name.title().split()[0]
last_name = full_name.title().split()[-1]
count_letters_first_name = len(first_name)
count_letters_last_name = len(last_name)

print(f"{upper}")
print(f"{lower}")
print(f"Your full name has {count_letters} letters.")
print(f"Your first name is {first_name} and has {count_letters_first_name} letters.")
print(f"Your last name is {last_name} and has {count_letters_last_name} letters.")
