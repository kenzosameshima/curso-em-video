number = int(input("Type a number: "))

if number < 2:
    print(f"{number} is not a prime number.")
elif number == 2:
    print("2 is a prime number.")
elif number % 2 == 0:
    print(f"{number} is not a prime number.")
else:
    for i in range(3, int(number ** 0.5) + 1, 2):
        if number % i == 0:
            print(f"{number} is not a prime number.")
            break
    else:
        print(f"{number} is a prime number.")
