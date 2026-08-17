import random

game_loop = True
player_points = 0
bot_points = 0
tie_points = 0

while game_loop:
    player = random.randint(1, 6)
    bot = random.randint(1, 6)

    print("\n-------- DICE GAME --------\n")
    print(f"Player -> [{player}]")
    print(f"Bot -> [{bot}]")

    if player > bot:
        print("The player won!\n")
        player_points += 1
    elif bot > player:
        print("The bot won!\n")
        bot_points += 1
    else:
        print("Tie!\n")
        tie_points += 1

    print("[SCORE]")
    print(f"Player: {player_points} | Bot: {bot_points} | Tie: {tie_points}")

    again_loop = True
    while again_loop:
        again = input("\nPlay again? (Y/n): ").upper()
        if again == "N" or again == "EXIT":
            again_loop = False
            game_loop = False
        elif again == "Y" or again == "":
            again_loop = False
            game_loop = True
        else:
            print("Error: invalid option.")
