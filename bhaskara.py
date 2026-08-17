import math

coefficients = input("\nEnter the coefficients of the quadratic equation in order a, b, and c (e.g. 2 3 4): ").split(" ")

a = int(coefficients[0])
b = int(coefficients[1])
c = int(coefficients[2])

delta = b ** 2 - (4 * a * c)

if a == 0:
    print(f"\nThis is not a quadratic equation, since the value of 'a' is zero.\n")
elif delta > 0:
    result_one = -b + math.sqrt(delta) / (2 * a)
    result_two = -b - math.sqrt(delta) / (2 * a)
    print(f"The possible values of X1 and X2, according to the quadratic formula, are: {result_one}, {result_two}.\n")
elif delta == 0:
    result = -b / (2 * a)
    print(f"Delta is equal to zero, so the value of x, according to the quadratic formula, is: {result}")
else:
    print(f"\nDelta is {delta}, in other words, it is less than zero.")
    print("It is not possible to calculate with these values.\n")
