import random 

def computer_choice():
    return random.choice(["rock",'paper',"scissors"])

def get_result(player,computer):
    if player == computer :
        print("Match tie ")
    elif (
        (player == "rock" and computer == "scissors") or
        (player == "scissors" and computer == "paper") or
        (player == "paper" and computer == "rock")
    ):
        print("You win")
    else :
        print("You lose")

def play_choice():
    print("Welcome to Rock, Paper, Scissors!")

    while True:
        choice = input("\nChoose rock, paper, or scissors (or 'exit' to quit): ").lower()

        if choice == "exit":
            print("Thanks ")
            break
        if choice not in ["rock",'paper',"scissors"]:
            print("invalid choice")
            continue 
        computer = computer_choice()
        print(f"Computer choice: {computer}")
        get_result(choice, computer)

play_choice()
        


    