import random

print("Hi,lets play a game of rock, paper, scissors")

print("Hope you enjoy!")

def main():
    player1 = input("Select Rock, Paper, or Scissors :").lower()
    player2 = random.choice(["Rock", "Paper", "Scissors"]).lower()
    print("Player 2 selected: ", player2)

    if player1 == "rock" and player2 == "paper":
        print("Player 2 Won")
    elif player1 == "paper" and player2 == "scissors":
        print("Player 2 Won")
    elif player1 == "scissors" and player2 == "rock":
        print("Player 2 Won")
    elif player1 == player2:
        print("Tie, lets go again!")
        main()
    else:
        print("You Won!")

    play_again = input("Would you like to play again (yes/no)?").lower()
    if play_again == "yes":
        main()
    else:
        print("Have a good day!")
        exit()

main()
