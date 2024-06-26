import random

def get_computer_choice():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

def get_player_choice():
    while True:
        choice = input("Enter your choice (rock, paper, scissors): ").lower()
        if choice in ["rock", "paper", "scissors"]:
            return choice
        else:
            print("Invalid choice, try again.")

def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "tie"
    elif (player_choice == "rock" and computer_choice == "scissors") or \
         (player_choice == "scissors" and computer_choice == "paper") or \
         (player_choice == "paper" and computer_choice == "rock"):
        return "user"
    else:
        return "computer"

def display_result(player_choice, computer_choice, winner):
    print(f"\nYou chose {player_choice}, computer chose {computer_choice}.")
    if winner == "tie":
        print("It's a tie!")
    elif winner == "user":
        print("You win!")
    else:
        print("Computer wins!")

def main():
    player_score = 0
    computer_score = 0

    print("Welcome to Rock, Paper, Scissors!")
    
    while True:
        player_choice = get_player_choice()
        computer_choice = get_computer_choice()
        winner = determine_winner(player_choice, computer_choice)
        
        display_result(player_choice, computer_choice, winner)
        
        if winner == "player":
            player_score += 1
        elif winner == "computer":
            computer_score += 1
        
        print(f"\nScore - You: {player_score}, Computer: {computer_score}")
        
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            break
    
    print("Thanks for playing the game!")

if __name__ == "__main__":
    main()
