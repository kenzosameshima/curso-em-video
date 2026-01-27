from random import randint

random_number = randint(1, 5)
user_guess = input('I have chosen a number between 1 and 5. Can you guess it? ')

if user_guess == str(random_number):
    print('Congratulations! You guessed the number!')
else:
    print(f'Sorry, the number I chose was {random_number}. Better luck next time!')
 