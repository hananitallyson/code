def progression(first_term, number_of_terms, difference):
    if number_of_terms == 1:
        return first_term
    target_number = first_term + (number_of_terms - 1) * difference
    return target_number

numbers = input("\nEnter the first term, the number of terms, and the common difference (e.g. 2 100 3): ")
numbers = numbers.split(" ")

inicial_term = int(numbers[0])
target_term = int(numbers[1])
common_difference = int(numbers[2])

print(f"The target term is equal to {progression(inicial_term, target_term, common_difference)}\n")
