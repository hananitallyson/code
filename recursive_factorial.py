def factorial(number):
    if number == 1:
        return number
    return number * factorial(number - 1)

target_number = int(input("\nEnter a number (e.g. 5): "))

print(f"{target_number}! is equal to {factorial(target_number)}.\n")
