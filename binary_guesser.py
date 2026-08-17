import random

def gen_binary(n):
    number = ""
    for _ in range(n):
        number += str(random.randint(0, 1))
    return number

print("Welcome to Binary Guesser!\n")
game = True
total_bits = 0

while total_bits == 0:
    print("Choose a game mode:\n1 -> 4 bits combination\n2 -> 8 bits combination")
    gamemode = input("\nEnter the mode: ")

    if gamemode == '1':
        total_bits = 4
    elif gamemode == '2':
        total_bits = 8
    else:
        print("\nThe gamemode must be 1 or 2.\nAny other value will result in an ERROR. Please try again!\n")

while game == True:
    binary_to_guess = gen_binary(total_bits)
    print("What decimal number is equivalent to [", binary_to_guess, "]")
    answer_num = int(input("Enter the decimal: "))

    binary_to_decimal = int(binary_to_guess, 2)

    if answer_num == binary_to_decimal:
        print("\nCorrect!\nThe number was", binary_to_decimal,"\n")
        game = True
    else:
        print("\nWrong!\nThe number was", binary_to_decimal, "\n")
        game = False
