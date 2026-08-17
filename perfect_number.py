loop = True

while loop:
    number = int(input("\nEnter a integer number (e.g. 6): "))
    sum = 0

    for i in range(1, number + 1):
        if number % i == 0:
            sum += i

    if sum == (number * 2):
        print(f"{number} is a perfect number!\n")
    else:
        print(f"{number} isn't a perfect number!\n")

    again_loop = True

    while again_loop:
        again = input("Verify new number? (Y/n): ").upper()
        if again == "Y" or again == "":
            loop = True
            again_loop = False
        elif again == "N" or again == "EXIT":
            loop = False
            again_loop = False
        else:
            print("\nError: invalid option.")

