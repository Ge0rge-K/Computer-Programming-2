# Name: George Koniaris
# File rps_minus_one.py
# Description: Implements the Rock Paper Scissors Minus One game from Squid Game

import random

def update_score(points):
    global score
    score += points
    print(f"Score updated! Current score: {score}")

def Computer_Action():
    possible_actions = ["rock", "rock", "paper", "paper", "scissors", "scissors"]
    return random.choice(possible_actions)

def User_Action():
    user_action = input("Enter a first choice (rock, paper, scissors): ")
    user_action2 = input("Enter a second choice (rock, paper, scissors): ")
    return user_action, user_action2

def determine_winner(user_action, computer_action):
    if user_action == computer_action:
        print(f"Both players selected {user_action}. It's a tie!")
        update_score(0)
    elif user_action == "rock":
        if computer_action == "scissors":
            print("Rock smashes scissors! You win!")
            update_score(1)
        else:
            print("Paper covers rock! You lose.")
            update_score(-1)
    elif user_action == "paper":
        if computer_action == "rock":
            print("Paper covers rock! You win!")
            update_score(1)
        else:
            print("Scissors cuts paper! You lose.")
            update_score(-1)
    elif user_action == "scissors":
        if computer_action == "paper":
            print("Scissors cuts paper! You win!")
            update_score(1)
        else:
            print("Rock smashes scissors! You lose.")
            update_score(-1)

def main():
    global score
    score = 0  # Reset score at the start of each game
    computer_action = Computer_Action()
    user_action, user_action2 = User_Action()

    print(f"\nYou chose {user_action} and {user_action2}, computer chose {computer_action}.\n")

    print("First choice results:")
    determine_winner(user_action, computer_action)

    print("\nSecond choice results:")
    determine_winner(user_action2, computer_action)

    print(f"Final score: {score}")

while True:
    main()
    play_again = input("Do you want to play again? (Yes/No): ").strip().lower()
    if play_again != "yes":
        print("Bye!")
        break


