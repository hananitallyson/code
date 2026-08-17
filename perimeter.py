length = float(input("Enter the length of one of the sides in meters (e.g. 15): "))
width = float(input("Enter the width of one of the sides in meters (e.g. 30): "))

perimeter = (2 * length) + (2 * width)
total_of_wires = 5 * perimeter

print(f"The total number of meters of wire needed is {total_of_wires:.2f} m.\n")
