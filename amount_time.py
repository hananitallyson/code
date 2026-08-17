import math

investiment = float(input("\nEnter the amount you will invest (e.g. 100): $"))
amount = float(input("Enter the amount you want to withdraw (e.g. 1500): $"))
fees = float(input("Enter the interest rate as a percentage (e.g. 10%): ").replace("%", ""))

fees = fees / 100

target_time = math.log(amount / investiment) / math.log(1 + fees)
target_time = math.ceil(target_time)

print(f"You will need to wait {target_time} months.\n")
