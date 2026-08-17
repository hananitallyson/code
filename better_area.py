height = float(input("\nEnter the height of the room in meters (e.g. 5): "))
length = float(input("Enter the length of the room in meters (e.g. 10): "))
width = float(input("Enter the width of the room in meters (e.g. 12): "))

walls_length = 2 * (length * height)
walls_width = 2 * (width * height)
ceiling = length * width

total_area = ceiling + walls_length + walls_width

print(f"The room has a total area of {total_area:.2f} m².\n")
