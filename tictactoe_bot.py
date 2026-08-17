import random


def render_board(gameboard):
    print()
    for i in range(3):
        for j in range(3):
            print(gameboard[i][j], end=" ")
        print()


def check_winner(gameboard):
    win = False

    if (
        (gameboard[0][0] == gameboard[0][1])
        and (gameboard[0][1] == gameboard[0][2])
        and (gameboard[0][2] != "*")
    ):
        win = True

    elif (
        (gameboard[1][0] == gameboard[1][1])
        and (gameboard[1][1] == gameboard[1][2])
        and (gameboard[1][2] != "*")
    ):
        win = True

    elif (
        (gameboard[2][0] == gameboard[2][1])
        and (gameboard[2][1] == gameboard[2][2])
        and (gameboard[2][2] != "*")
    ):
        win = True

    elif (
        (gameboard[0][0] == gameboard[1][0])
        and (gameboard[1][0] == gameboard[2][0])
        and (gameboard[2][0] != "*")
    ):
        win = True

    elif (
        (gameboard[0][1] == gameboard[1][1])
        and (gameboard[1][1] == gameboard[2][1])
        and (gameboard[2][1] != "*")
    ):
        win = True

    elif (
        (gameboard[0][2] == gameboard[1][2])
        and (gameboard[1][2] == gameboard[2][2])
        and (gameboard[2][2] != "*")
    ):
        win = True

    elif (
        (gameboard[0][0] == gameboard[1][1])
        and (gameboard[1][1] == gameboard[2][2])
        and (gameboard[2][2] != "*")
    ):
        win = True

    elif (
        (gameboard[0][2] == gameboard[1][1])
        and (gameboard[1][1] == gameboard[2][0])
        and (gameboard[2][0] != "*")
    ):
        win = True

    return win


gameboard = [["*", "*", "*"], ["*", "*", "*"], ["*", "*", "*"]]

print("\n[ TIC TAC TOE ]")

turns = 0
win = False
bot_options = [0, 1, 2, 3, 5, 6, 7, 8]

gameboard[1][1] = "0"
render_board(gameboard)

while turns < 10 and not win:
    print("\n(Players X's turn)")
    position = int(input("Enter the position: ")) - 1
    row = position // 3
    column = position % 3
    gameboard[row][column] = "X"
    turns += 1
    bot_options.remove(position)
    win = check_winner(gameboard)
    render_board(gameboard)

    if not win:
        print("\n(Players 0's turn)")
        position = random.choice(bot_options)
        row = position // 3
        column = position % 3
        gameboard[row][column] = "0"
        turns += 1
        bot_options.remove(position)
        win = check_winner(gameboard)
        render_board(gameboard)

print()

