# Student Result Management System

name = input("Enter student name: ")

score1 = int(input("Enter score 1: "))
score2 = int(input("Enter score 2: "))
score3 = int(input("Enter score 3: "))

average = (score1 + score2 + score3) / 3

if average >= 70:
    grade = "A"
elif average >= 60:
    grade = "B"
elif average >= 50:
    grade = "C"
else:
    grade = "F"

print("\nStudent Name:", name)
print("Average Score:", average)
print("Grade:", grade)

