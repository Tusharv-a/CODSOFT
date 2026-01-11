import random

def get_computer_choice():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

def get_player_choice():
    while True:
        choice = input("Enter the choice(rock, paper or scissors):").lower()
        if choice in["rock", "paper", "scissor"]:
            return choice
        print("invaild choice. please enter 'rock', 'paper', or 'scissors'.")

def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "It is tie"
    elif(player_choice =="rock" and computer_choice =="scissors")or\
        (player_choice =="paper" and computer_choice =="rock")or\
        (player_choice =="scissors" and computer_choice =="paper"):
        return "you win!"
    else:
        return "computer win!"

def play_game():
    print("welcome to rock, paper or scissors game")
    while True:
        player_choice = get_player_choice()
        computer_choice = get_computer_choice()
        print(f"\n you chose: {player_choice}")
        print(f"Computer chose: {computer_choice}")
        result = determine_winner(player_choice, computer_choice)
        print(result)

        play_again = input("\nDo you want to play again?(yes/no):").lower()
        if play_again != "yes":
            print("thanks for playing")
            break

if __name__ == "__main__":
    play_game()
