name = str(input("Enter your name: ")).strip()

lower = name.lower()

if lower == "pedro" or lower == "maria" or lower == "joão":
    print("Your name is very popular in Brazil!")
elif lower == "kenzo":
    print("What a beautiful name!")
else:
    print("Your name is quite unique!")

print(f"Have a nice day, {name.capitalize()}!")
