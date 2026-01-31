import datetime

today = datetime.date.today()
current_year = today.year

birth_date = input("Enter your birth date (DD/MM/YYYY): ")
age = current_year - int(birth_date[-4:])

if (today.month, today.day) < (int(birth_date[3:5]), int(birth_date[0:2])):
    age -= 1

if age < 18:
    print(f"\033[32mYou are {age} years old. You still have {18 - age} year(s) left until you need to enlist.\033[0m")
elif age == 18:
    print(f"\033[33mYou are {age} years old. You need to enlist this year.\033[0m")
else:
    print(f"\033[31mYou are {age} years old. You should have enlisted {age - 18} year(s) ago.\033[0m")
