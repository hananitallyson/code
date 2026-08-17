import random

game_loop = True
player_points = 0
bot_one_points = 0
bot_two_points = 0
tie_points = 0

while game_loop:
    player = random.randint(0, 1)
    bot_one = random.randint(0, 1)
    bot_two = random.randint(0, 1)

    print("\n-------- ZERO-ONE --------\n")
    print(f"Player -> {player}\nBot 1  -> {bot_one}\nBot 2  -> {bot_two}\n")

    if player != bot_one and player != bot_two:
        print("Player won!")
        player_points += 1
    elif player != bot_one and player == bot_two:
        print("Bot 1 won!")
        bot_one_points += 1
    elif player == bot_one and player != bot_two:
        print("Bot 2 won!")
        bot_two_points += 1
    else:
        print("Tie!")
        tie_points += 1

    print("\n[SCORE]")
    print(
        f"Player: {player_points} | Bot 1: {bot_one_points} | Bot 2: {bot_two_points} | Ties: {tie_points}"
    )

    if player_points == 5:
        print("\nThe player won 5 times. Game over!\n")
        game_loop = False
    elif bot_one_points == 5:
        print("\nThe bot 1 won 5 times. Game over!\n")
        game_loop = False
    elif bot_two_points == 5:
        print("\nThe bot 2 won 5 times. Game over!\n")
        game_loop = False
    else:
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
