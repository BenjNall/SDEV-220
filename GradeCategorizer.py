# M02 Lab - if...else and while
# Program Name: GradeCategorizer.py
# Author: Ben Nall
# Date 8/24/2024
# Purpose: This program will take input for student names and gpa's and categorize them into either the dean's list, honor roll, or neither.

print("Welcome to the Grade Categorizer!")
print("This program will categorize students into the Dean's List, Honor Roll, or neither based on their GPA.")
print()

# Initialize variables
lastName = ""
firstName = ""
gpa = 0.0
status = ""

#main loop controlled with sentinel value
while (lastName.upper() != "ZZZ"):
    #input
    lastName = input("Please enter the student's Last name or ZZZ to quit: ")
    if lastName.upper() == "ZZZ":
        break
    firstName = input("Please enter the student's First name: ")
    #validates gpa to be between 0 and 4 and a number
    try:
        gpa = float(input("Please enter the student's GPA: "))
        if gpa < 0 or gpa > 4:
            print("Invalid GPA. Please enter a number between 0 and 4.")
            continue
    except ValueError:
        print("Invalid GPA. Please enter a number.")
        continue

    #outputs the student's name and status
    if gpa >= 3.5:
        print(firstName, lastName, "is on the Dean's List.")
        status = "Dean's List"
    elif gpa >= 3.25:
        print(firstName, lastName, "is on the Honor Roll.")
        status = "Honor Roll"
    else: 
        print(firstName, lastName, "is not on the Dean's List or Honor Roll.")
        status = "Neither"