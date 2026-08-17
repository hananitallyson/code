fibonacci_position = int(input("\nEnter the desired Fibonacci position (e.g. 6): "))

current_number = 0
next_number = 1

for index in range(1, fibonacci_position):
    fibonacci_number = current_number + next_number
    current_number = next_number
    next_number = fibonacci_number

print(f"The number at position {fibonacci_position} in the Fibonacci sequence is {current_number}.\n")
