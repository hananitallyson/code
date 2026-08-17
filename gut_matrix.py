print("\n-------- GUT MATRIX --------")

loop = True
while loop:
    gravity = int(input("\nWhat are the effects? (1/2/3/4/5): "))
    urgency = int(input("Can this wait? (1/2/3/4/5): "))
    tendency = int(input("Will this get worst? (1/2/3/4/5): "))

    gut_score = gravity * urgency * tendency
    print(f"\nGUT Score: {gut_score}/125")

    again_loop = True
    while again_loop:
            again = input("\nCalculate the GUT score again? (Y/n): ").upper()
            if again == "N" or again == "EXIT":
                again_loop = False
                loop = False
            elif again == "Y" or again == "":
                again_loop = False
                loop = True
            else:
                print("Error: invalid option.")
