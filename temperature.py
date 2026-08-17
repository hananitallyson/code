loop = True

while loop:
    print("\ntype 'exit' to leave\nf: Fahrenheit\nk: Kelvin")
    choice = input("Enter your choice: ")

    if choice == "f":
        num_celsius = float(input("\nEnter the number in Celsius (e.g. 25): "))
        num_fahrenheit = 1.8 * num_celsius + 32
        print(num_celsius, "°C ->", num_fahrenheit, "°F")
    elif choice == "k":
        num_celsius = float(input("\nEnter the number in Celsius (e.g. 25): "))
        num_kelvin = num_celsius + 273.15
        print(num_celsius, "°C ->", num_kelvin, "°K")
    elif choice == "exit":
        print("")
        loop = False

