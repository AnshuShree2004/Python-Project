
import random

print("Welcome to Rock, Paper, Scissors game..")

choices = ('r', 'p', 's')

while True:

    user_choice = input("Rock, paper or scissor? (r/p/s): ").lower()

    if user_choice not in choices:
        print("Invalid choice..")
        continue

    comp_choice = random.choice(choices)

    print("You chose:", user_choice)
    print("Computer chose:", comp_choice)

    if user_choice == comp_choice:
        print("It's a tie..")

    elif (user_choice == 'r' and comp_choice == 's') or \
         (user_choice == 'p' and comp_choice == 'r') or \
         (user_choice == 's' and comp_choice == 'p'):
        print("You won..")

    else:
        print("Computer won..")

    # Ask after one round is completed
    gameToContinue = input("\nWant to continue? (y/n): ").lower()

    if gameToContinue == 'n':
        print("Thanks for playing!")
        break

    elif gameToContinue != 'y':
        print("Invalid input! Enter y or n..")
        break
