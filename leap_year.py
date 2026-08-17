target_year = int(input("\nEnter the year (e.g. 2026): "))

if target_year % 4 == 0 and target_year % 100 != 0:
    print(f"{target_year} is a leap year.\n")
else:
    print(f"{target_year} isn't a leap year.\n")
