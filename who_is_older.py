person_one = input("\nEnter the first person name and age (e.g. Gabi 19): ").split(" ")
person_two = input("Enter the second person name and age (e.g. Hanani 21): ").split(" ")

person_one_name = person_one[0]
person_one_age = int(person_one[1])
person_two_name = person_two[0]
person_two_age = int(person_two[1])

if person_one_age > person_two_age:
    print(f"{person_one_name} is older than {person_two_name}.")
    print(f"The age difference is {person_one_age - person_two_age} years.\n")
elif person_one_age < person_two_age:
    print(f"{person_two_name} is older than {person_one_name}.")
    print(f"The age difference is {person_two_age - person_one_age} years.\n")
else:
    print(f"{person_one_name} is the same age as {person_two_name}\n")

