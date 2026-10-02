import random

#a finction to get the computer choice
def get_computer_choice():    
    choices = ["rock", "scissors", "paper"]
    return random.choice(choices)

#a function to get the player choice
def get_player_choice():
    decision = input("Enter your choice (rock, paper, scissors): ").strip().lower()
    if decision != "rock" and decision != "paper" and decision != "scissors":
        print("Invalid choice. Please enter rock, paper, or scissors.")
        get_player_choice()
    else:
        return decision
    
#a function to determine the winner of the game
def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "Tie"
    elif (player_choice == "rock" and computer_choice == "scissors") or \
         (player_choice == "scissors" and computer_choice == "paper") or \
         (player_choice == "paper" and computer_choice == "rock"):
        return "Player wins"
    else:
        return "Computer wins"

#main game loop
want_to_play = True
print("Welcome to Rock, Paper, Scissors!")

#loop to allow the player to play multiple rounds
while want_to_play == True:
    player_wins = 0
    computer_wins = 0
    play_amount = int(input("How many times do you want to play? (must be an odd integer greater than 0) "))
    if (play_amount % 2 == 0) or play_amount <= 0:
        print("Invalid amount, number of rounds must be ODD and more than 0 and an integer.")
        continue
    # Loop through each round of the game, calculating the winner and updating the scores accordingly
    for round_number in range(play_amount):

        player_choice = get_player_choice()
        computer_choice = get_computer_choice()
        result = determine_winner(player_choice, computer_choice)
        print(f"The computer chose {computer_choice}. {result}")
        if result == "Player wins":
            player_wins += 1
        elif result == "Computer wins":
            computer_wins += 1
        else:

            #this was kind of hard, I wanted to make sure that you could get ties indefinitely before a winner is determined
            print("The round is a tie.")
            while(result == "Tie"):
                player_choice = get_player_choice()
                computer_choice = get_computer_choice()
                result = determine_winner(player_choice, computer_choice)
                print(f"The computer chose {computer_choice}. {result}")
                if result == "Player wins":
                    player_wins += 1
                elif result == "Computer wins":
                    computer_wins += 1
                else:
                    print("The round is a tie.")
                    continue

            
        
# Display the final results of the match
    print(f"----------------------- \n Player wins: {player_wins}, Computer wins: {computer_wins}")
    if player_wins > computer_wins:
        print("Player wins the match!")
    elif player_wins < computer_wins:
        print("Computer wins the match!")


# Ask the player if they want to play again
    if input("Do you want to play again? (yes/no): ").lower() == "yes":
        want_to_play = True
    else:
        want_to_play = False

print("Thanks for playing!")

