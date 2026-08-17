import random

count = 0

while count not in range(6, 16):
    count = int(input("\nEnter the range number (6~15): "))

print("\nYour betting slip has been generated!")

chosen_numbers = []
numbers = list(range(1, 60))

for _ in range(count):
    picked_number = random.choice(numbers)
    chosen_numbers.append(picked_number)
    numbers.remove(picked_number)

print(f"Numbers: {chosen_numbers}\n")

