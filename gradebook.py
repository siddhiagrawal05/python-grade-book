#---------------------------------------------------------------------------------------
# GradeBook Analyzer
# Name: Siddhi Agrawal
# Date: novmember 24, 2025
# Project Title: Mini Project – Analysing and Reporting Student Grades
#---------------------------------------------------------------------------------------

import csv

# ------------------ FUNCTIONS ------------------

# Task 3 - Statistical functions
def calculate_average(marks):
    if len(marks) == 0:
        return 0
    return sum(marks.values()) / len(marks)

def calculate_median(marks):
    scores = sorted(marks.values())
    n = len(scores)
    if n == 0:
        return 0
    mid = n // 2
    if n % 2 == 0:
        return (scores[mid - 1] + scores[mid]) / 2
    else:
        return scores[mid]

def max_score(marks):
    if len(marks) == 0:
        return None, 0
    name = max(marks, key=marks.get)
    return name, marks[name]

def min_score(marks):
    if len(marks) == 0:
        return None, 0
    name = min(marks, key=marks.get)
    return name, marks[name]

# Task 4 - Grade assignment
def assign_grades(marks):
    grades = {}
    for name, score in marks.items():
        if score >= 90:
            grade = "A"
        elif score >= 80:
            grade = "B"
        elif score >= 70:
            grade = "C"
        elif score >= 60:
            grade = "D"
        else:
            grade = "F"
        grades[name] = grade
    return grades

def grade_distribution(grades):
    count = {"A":0,"B":0,"C":0,"D":0,"F":0}
    for g in grades.values():
        count[g] += 1
    return count

# ------------------ MAIN PROGRAM LOOP ------------------

while True:

    marks = {}  # dictionary for storing data

    print("\n============================================")
    print(" Welcome to GradeBook Analyzer ")
    print("============================================")
    print("1. Enter data manually")
    print("2. Load data from CSV file")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        # Task 2 - Manual input
        n = int(input("How many students? "))
        for i in range(n):
            name = input(f"Enter name of student {i+1}: ")
            score = float(input(f"Enter marks for {name}: "))
            marks[name] = score

    elif choice == "2":
        # Task 2 - CSV input
        file_name = input("Enter CSV file name (example: data.csv): ")
        try:
            with open(file_name, "r") as file: 
                reader = csv.reader(file)
                for row in reader:
                    marks[row[0]] = float(row[1])
            print("CSV file loaded successfully!")
        except:
            print("Error: File not found!")
            continue

    elif choice == "3":
        print("Thank you for using GradeBook Analyzer!")
        break

    else:
        print("Invalid choice! Try again.")
        continue

    # Task 3 - Analysis
    avg = calculate_average(marks)
    med = calculate_median(marks)
    max_name, max_score = max_score(marks)
    min_name, min_score = min_score(marks)

    print("\n----- Analysis Summary -----")
    print(f"Average Marks : {avg:.2f}")
    print(f"Median Marks  : {med:.2f}")
    print(f"Highest Marks : {max_name} ({max_score})")
    print(f"Lowest Marks  : {min_name} ({min_score})")

    # Task 4 - Grades
    grades = assign_grades(marks)
   
    print("\n----- Grade Distribution -----")
    count = {"A":0,"B":0,"C":0,"D":0,"F":0}
    for g in grades.values():
        count[g] += 1
    print(count)

    # Task 5 - Pass / Fail using list comprehension
    passed = [name for name, score in marks.items() if score >= 40]
    failed = [name for name, score in marks.items() if score < 40]

    print("\nPassed Students:", passed)
    print("Failed Students:", failed)

    # Task 6 - Show result table
    print("\n----------- Result Table -----------")
    print("Name\tMarks\tGrade")
    print("-----------------------------------")
    for name in marks:
        print(f"{name}\t{marks[name]}\t{grades[name]}")
    print("-----------------------------------")

    # Continue loop?
    again = input("\nDo you want to run again? (y/n): ")
    if again.lower() != "y":
        print("Goodbye and all the best!")
        break

# Task 6 : Save Report to File (Manual & CSV)

if choice == "1":
    filename = "manual_grade_report.txt"
elif choice == "2":
    filename = "csv_grade_report.txt"
else:
    filename = "grade_report.txt"  # backup

save = input("\nDo you want to save this report to a file? (yes/no): ").lower()

if save == "yes":
    with open(filename, "a") as file:
        file.write("\n-------------------------------------\n")
        file.write("           GradeBook Report          \n")
        file.write("-------------------------------------\n")
        file.write("Name\tMarks\tGrade\n")
        file.write("-------------------------------------\n")

        for name in marks:
            file.write(f"{name}\t{marks[name]}\t{grades[name]}\n")

        file.write("-------------------------------------\n")
        file.write(f"Average Marks : {round(avg,2)}\n")
        file.write(f"Median Marks  : {round(med,2)}\n")
        file.write(f"Highest Marks : {max_name} ({max_score})\n")
        file.write(f"Lowest Marks  : {min_name} ({min_score})\n")
        file.write("-------------------------------------\n")

        import datetime
        file.write(f"Saved On : {datetime.datetime.now()}\n")
        file.write("-------------------------------------\n")

    print(f"Report saved successfully in '{filename}'")
else:
    print("Report not saved.")
