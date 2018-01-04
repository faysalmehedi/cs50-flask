from cs50 import get_string
from student import Student
import csv

# Space for Students
students = []

# Prompt for students name and dorms
for i in range(3):
    name = get_string('Name: ')
    dorm = get_string('Dorm: ')
    students.append(Student(name,dorm))
# storing students name and dorm in csv file
with open("students.csv", "w") as file:
    writer = csv.writer(file)
    for student in students:
        writer.writerow((student.name, student.dorm))