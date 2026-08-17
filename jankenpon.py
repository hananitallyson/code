import random

game_loop = True
player_points = 0
bot_points = 0
tie_points = 0
options = ["rock", "paper", "scissors"]

while game_loop:
    player = ""
    
    print("\n-------- JANKENPON --------\n")

    choice_loop = True
    while choice_loop:
        choice = input("Choose rock (r), paper (p), or scissors (s): ").lower()
        if choice in ["r", "rock"]:
            player = "rock"
            choice_loop = False
        elif choice in ["p", "paper"]:
            player = "paper"
            choice_loop = False
        elif choice in ["s", "scissors"]:
            player = "scissors"
            choice_loop = False
        else:
            print("Invalid choice!")

    bot = random.choice(options)

    print(f"\nPlayer -> [{player}] | Bot -> [{bot}]\n")

    if player == bot:
        print("Tie!")
        tie_points += 1
    elif player == "rock":
        if bot == "paper":
            print("Bot won!")
            bot_points += 1
        else:
            print("Player won!")
            player_points += 1
    elif player == "paper":
        if bot == "rock":
            print("Player won!")
            player_points += 1
        else:
            print("Bot won!")
            bot_points += 1
    else:
        if bot == "rock":
            print("Bot won!")
            bot_points += 1
        else:
            print("Player won!")
            player_points += 1

    print("\n[SCORE]")
    print(f"Player: {player_points} | Bot: {bot_points} | Tie: {tie_points}\n")

    again_loop = True
    while again_loop:
        again = input("Play again? (Y/n): ").upper()
        if again == "N" or again == "EXIT":
            again_loop = False
            game_loop = False
        elif again == "Y" or again == "":
            again_loop = False
            game_loop = True
        else:
            print("Error: invalid option.")
