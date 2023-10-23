import random
#This line imports the random module, which is used to generate a random choice for the computer.
def get_player_choice():
    while True:
        player = input("Enter your choice (rock, paper, scissors): ").lower()
        if player in ["rock", "paper", "scissors"]:
            return player
        else:
            print("Invalid input. Please choose from rock, paper, or scissors.")
#this fuction allows player to enter their choice using while loop from rock,paper and scissors
def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])
#this function generates a random choice from computer
def determine_winner(player, computer):
    outcomes = {
        ("rock", "paper"): "Computer wins",
        ("paper", "rock"): "Player wins",
        ("scissors", "paper"): "Player wins",
        ("paper", "scissors"): "Computer wins",
        ("rock", "scissors"): "Player wins",
        ("scissors", "rock"): "Computer wins",
    }
    if player == computer:
        return "Tie"
    return outcomes.get((player, computer), "Invalid input")
# all the possible cases from player and the system
def main():
    player = get_player_choice()
    computer = get_computer_choice()
    result = determine_winner(player, computer)
    
    print(f"Player chose {player}")
    print(f"Computer chose {computer}")
    print(result)
#this function determines the winner
if __name__ == "__main__":
    main()
