from random import randint

victories = 0

while True:
    while True:
        user_choice = input("Choose Odds or Evens [O/E]: ").strip().upper()
        if user_choice in ['O', 'E']:
            break
        print("Please choose O or E.")

    computer_choice = 'E' if user_choice == 'O' else 'O'

    while True:
        raw_number = input("Enter a number between 0 and 10: ")
        if raw_number.isdigit():
            user_number = int(raw_number)
            if 0 <= user_number <= 10:
                break
        print("Please enter a valid number between 0 and 10.")

    computer_number = randint(0, 10)

    total = user_number + computer_number

    result = 'E' if total % 2 == 0 else 'O'

    print(f"You chose {user_number} and the computer chose {computer_number}. Total is {total} which is {'Even' if result == 'E' else 'Odd'}.")
    
    if user_choice == result:
        print("\033[32mYou win! Let's play again.\033[0m")
        victories += 1
    else:
        print("\033[31mYou lose! Game over.\033[0m")
        break

print(f"\033[34mYou had {victories} consecutive victories.\033[0m")
