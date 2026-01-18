# STUDENT RESULT MANAGEMENT SYSTEM

## Student Information

Name: Omeh Chukwuebuka Anthony
Course: SEN201
Matric No: 24/15596
Department: Computer Science

## Project Description

This project is a simple console-based application that calculates a student’s average score and grade based on three course scores.

## Features

1. Accepts student name and scores

2. Calculates average score

3. Assigns grade automatically

4. Displays student result

# Technology Used

Python

# How to Run the Project

Clone the repository

Run the file student_result.py

Enter student details when prompted

## SDLC Model Used

Waterfall Model:

Requirement Analysis

System Design

Implementation

Testing

## SDLC 

## ✅ PROJECT TITLE

Student Result Management System (Console-Based)

A simple system that allows a user to input student details and calculate the average score and grade.

This project is simple, academic, and perfect for SEN assignments.

## ✅ 1. SOFTWARE DEVELOPMENT LIFE CYCLE (SDLC)

We will use the Waterfall Model, which is commonly taught.

# 1️⃣ Requirement Analysis

At this stage, the problem is identified and requirements are gathered.

Functional Requirements

The system should accept:

Student name

Three course scores

The system should:

Calculate the average score

Display the student’s grade

Non-Functional Requirements

The program should be easy to use

The program should run on a command-line interface

The program should produce accurate results

# 2️⃣ System Design

This stage defines how the system will work.

Design Components

Input:

Student name

Scores

Process:

Calculate average

Determine grade

Output:

Student details

Average score

Grade

Algorithm (Design Logic)

Start

Input student name and scores

Calculate average

Assign grade based on average

Display results

End

⚠️ Note: Names like average, score, grade used here will also appear in the code.

# 3️⃣ Implementation

This is where the system is coded.

Programming Language

Python (simple and acceptable)

Implementation Code
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

# 4️⃣ Testing

This stage checks if the system works correctly.

Test Cases

Input valid scores → correct average and grade

Input low scores → correct failure grade

Input high scores → correct distinction grade

The system was tested using different score values and produced correct results.

# 5️⃣ Deployment

The project is deployed by:

Saving the program as student_result.py

Uploading it to a GitHub repository

# 6️⃣ Maintenance

Future improvements may include:

Adding more courses

Saving results to a file
....

Creating a graphical interface

Deployment

Maintenance
