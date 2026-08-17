list_of_numbers = input("\nEnter three numbers (e.g. 4 8 16): ").split(" ")

a = int(list_of_numbers[0])
b = int(list_of_numbers[1])
c = int(list_of_numbers[2])

if a <= b:
    if b <= c:
        print(f"Ascending Order: {a}, {b}, {c}\n")
    elif a<= c:
        print(f"Ascending Order: {a}, {c}, {b}\n")
    else:
        print(f"Ascending Order: {c}, {a}, {b}\n")
else:
    if a <= c:
        print(f"Ascending Order: {b}, {a}, {c}\n")
    elif b <= c:
        print(f"Ascending Order: {b}, {c}, {a}\n")
    else:
        print(f"Ascending Order: {c}, {b}, {a}\n")
