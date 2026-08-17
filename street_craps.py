import random

game_loop = True
player_points = 0
bot_points = 0

while game_loop:
    die_one = random.randint(1, 6)
    die_two = random.randint(1, 6)
    sum_of_dices = die_one + die_two

    print("\n-------- STREET CRAPS --------\n")
    print(f"[{die_one}] [{die_two}] = {sum_of_dices}")

    if sum_of_dices == 7 or sum_of_dices == 11:
        print("The player won!\n")
        player_points += 1
    else:
        print("The bot won!\n")
        bot_points += 1

    print("[SCORE]")
    print(f"Player: {player_points} | Bot: {bot_points}")

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
