# Rock paper scissors game
import random

def play_game():
    choices = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(choices)  # Random choice for the computer
    user_choice = input("Enter your choice (rock, paper, or scissors): ").lower()

    if user_choice not in choices:
        print("Invalid choice. Please choose rock, paper, or scissors.")
        return  # Exit the function if the input is invalid

    print(f"Computer chose: {computer_choice}")
    print(f"You chose: {user_choice}")

    # Determine the winner
    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        print("You have won the game!")
    else:
        print("You have lost the game!")

# Call the function to play the game
play_game()
