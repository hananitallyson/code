import random

def roll(dice_sides):
    dice_roll = random.randint(1, dice_sides)
    return dice_roll

dice = int(input("\nEscolha o dado a ser rolado (d4, d6, d8, d10, d12 ou d20): d"))
dice_result = roll(dice)

print(f"O dado rolado foi o d{dice} e o resultado foi: {dice_result}\n")
