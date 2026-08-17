print("\n------------------------------------")

start = int(input("\nEnter the start of the range (e.g. 2): "))
end = int(input("Enter the end of the range (e.g. 12): "))
step = int(input("Enter the step of the range (e.g., 3): "))

print("\n--------------- loop ---------------")

for i in range(start, end, step):
    print(f"Value of i: {i}")

print("------------- end loop -------------\n")
