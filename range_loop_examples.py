print("\n" + "=" * 50)
print("Range: 0 to 20 (step 2)")
print("=" * 50)
for i in range(0, 20, 2):
    print(i, end=" ")

print("\n")


print("=" * 50)
print("Range: 40 down to 20 (step -2)")
print("=" * 50)
for i in range(40, 19, -2):
    print(i, end=" ")

print("\n")


print("=" * 50)
print("Range: 11 to 30 (step 2)")
print("=" * 50)
for i in range(11, 30, 2):
    print(i, end=" ")

print("\n")


print("=" * 50)
print("Range: 4 to 25 (step 4)")
print("=" * 50)
for i in range(4, 25, 4):
    print(i, end=" ")

print("\n")


print("=" * 50)
print("Range: 10 to 20 (step 5)")
print("=" * 50)
for i in range(10, 20, 5):
    print(i, end=" ")

print("\n")


print("=" * 50)
print("Odd numbers from x down to 1")
print("=" * 50)
x = int(input("Enter x: "))
print("")
for i in range(x, 0, -1):
    if i % 2 == 1:
        print(i, end=" ")

print("\n")


print("=" * 50)
print("Multiples of 7 between a and b (descending)")
print("=" * 50)
a = int(input("Enter a: "))
b = int(input("Enter b: "))
print("")
if a < b:
    for i in range(b, a, -1):
        if i % 7 == 0:
            print(i, end=" ")
else:
    if a > b:
        for i in range(a, b, -1):
            if i % 7 == 0:
                print(i, end=" ")
    else:
        for i in range(a, b, -1):
            if i % 7 == 0:
                print(i, end=" ")

print("\n")
