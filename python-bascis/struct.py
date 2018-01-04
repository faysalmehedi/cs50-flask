from cs50 import get_string
from student import Student

# Space for Students
students = []

# Prompt for students name and dorms
for i in range(3):
    name = get_string('Name: ')
    dorm = get_string('Dorm: ')
    students.append(Student(name,dorm))
# Print students name and dorm

for student in students:
    print(f"{student.name} lives in {student.dorm}.")