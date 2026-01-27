city_name = input("Enter the name of a city: ").strip()

if city_name.lower().startswith(('santo', 'são', 'san', 'saint')):
    print("The city name starts with 'Santo' or its variants.")
