number = int(input("\nEnter a integer number (e.g 20): "))

print(f"\nThe divisors of {number} are:")
for i in range(1, number + 1):
    if number % i == 0:
        print(i, end=" ")
print("\n")

