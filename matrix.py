matrix = [[11, 22, 33], [44, 55, 66], [77, 88, 99]]

row_length = len(matrix)
columns_length = len(matrix[0])

print("\nNOMINAL MATRIX ------------------")
for row in range(row_length):
    print(f"ROW({row}):")
    for column in range(columns_length):
        print(f"({row},{column}) <- [{matrix[row][column]}]", end=" | ")
        print(
            f"K: {row} * {columns_length} + {column} -> {row * columns_length + column}"
        )
    print(" ")

print("TRANSPOSED MATRIX ---------------")
for row in range(row_length):
    print(f"COLUMN({row}):")
    for column in range(columns_length):
        print(f"({column},{row}) <- [{matrix[column][row]}]", end=" | ")
        print(
            f"K: {column} * {columns_length} + {row} -> {column * columns_length + row}"
        )
    print(" ")

