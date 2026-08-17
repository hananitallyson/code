import datetime

date_of_birth = input("\nEnter your date of birth (e.g. 04/07/2006): ").split("/")

day_of_birth = int(date_of_birth[0])
month_of_birth = int(date_of_birth[1])
year_of_birth = int(date_of_birth[2])

current_date = datetime.date.today()

this_year_age = current_date.year - year_of_birth

if current_date.month == month_of_birth and current_date.day < day_of_birth or current_date.month < month_of_birth:
    print(f"Since it hasn't been your birthday yet, your age is {this_year_age - 1}.\n")
elif current_date.day == day_of_birth and current_date.month == month_of_birth:
    print(f"Happy Birthday! Today is {current_date.day}/{current_date.month:02}, your birthday, and your age is {this_year_age}.\n")
else:
    print(f"Since your birthday has already passed, your age is {this_year_age}.\n")
