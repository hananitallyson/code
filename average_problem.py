grade = 0
course = 0
sum_of_grades = 0
sum_of_courses = 0

while grade >= 0:
    grade = float(input("Enter the grade: "))
    if grade >= 0:
        sum_of_grades = sum_of_grades + grade
        sum_of_courses = sum_of_courses + 1

final_grade = sum_of_grades / sum_of_courses

if final_grade >= 9.0:
    print(f"{final_grade} is A")
if (final_grade >= 8.0) and (final_grade < 9.0):
    print(f"{final_grade} is B")
if (final_grade >= 7.0) and (final_grade < 8.0):
    print(f"{final_grade} is C")
if (final_grade >= 6.0) and (final_grade < 7.0):
    print(f"{final_grade} is D")
if (final_grade >= 5.0) and (final_grade < 6.0):
    print(f"{final_grade} is F")

