while True:
    while True:
        raw = input("Enter a number to see its multiplication table (negative to exit): ")
        if raw.lstrip('-').isdigit():
            number = int(raw)
            break

    if number < 0:
        break

    for i in range(1, 11):
        print(f"{number} x {i} = {number * i}")
