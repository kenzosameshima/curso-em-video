import datetime

today = datetime.date.today()
current_year = today.year

birth_date = input("Enter your birth date (DD/MM/YYYY): ")
age = current_year - int(birth_date[-4:])

if (today.month, today.day) < (int(birth_date[3:5]), int(birth_date[0:2])):
    age -= 1

if age < 12:
    category = "U12"
elif age < 18:
    category = "U18"
elif age < 20:
    category = "U20"
elif age < 23:
    category = "U23"
elif age < 35:
    category = "Senior / Open"
else:
    category = "Master / Veteran"

print(f"You are {age} years old and belong to the '{category}' category.")
