def round_to(number):
    if number == 0:
        return 0
    integer_part = 0
    if number % 2 < 1:
        integer_part = 2 * (number // 2)
    elif number % 2 > 1:
        integer_part = 2 * (number // 2) + 1
    decimal_part = number - integer_part
    if decimal_part < 0.5:
        return integer_part
    else:
        return integer_part + 1

float_number = float(input("\nEnter a float number (e.g., 10.5): "))
target_number = round_to(float_number)

print(f"The number {float_number} was rounded to {target_number}.\n")
