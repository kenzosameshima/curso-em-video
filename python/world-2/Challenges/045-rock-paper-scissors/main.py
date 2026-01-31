from random import choice

print("Welcome to Rock, Paper, Scissors!")
user_choice = input("Enter rock, paper, or scissors: ").lower().strip()

rock_paper_scissors = ["rock", "paper", "scissors"]
computer_choice = choice(rock_paper_scissors)

if user_choice not in rock_paper_scissors:
    print("Invalid choice! Please choose rock, paper, or scissors.")
else:
    print(f"Computer chose: {computer_choice}")
    
    if user_choice == computer_choice:
        print("\033[33mIt's a tie!\033[0m")
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        print("\033[32mYou win!\033[0m")
    else:
        print("\033[31mComputer wins!\033[0m")
