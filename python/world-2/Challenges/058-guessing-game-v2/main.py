from random import randint

while True:
    number = randint(0, 10)
    tries = 0
    print('I have selected a number between 0 and 10. Can you guess it?')

    while True:
        guess = int(input('Your guess: '))
        tries += 1

        if guess < number:
            print('\033[1;34mToo low! Try a higher number.\033[m')
            continue

        if guess > number:
            print('\033[1;34mToo high! Try a lower number.\033[m')
            continue
    
        print(f'\033[1;32mCongratulations! You guessed the number {number} in {tries} tries.\033[m')
        break
    
    play_again = input('Do you want to play again? [Y/N]: ').strip().upper()
    if play_again != 'Y':
        print('\033[1;33mThanks for playing! Goodbye!\033[m')
        break
