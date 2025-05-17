import json

def print_students(students):
    """Prints the names of students in a list."""
    for student in students:
        print(student)

with open('student.json') as f:
    students = json.load(f)
print_students(students)

students.append({
    "F_Name": "Rachel",
    "L_Name": "Lane",
    "Student_ID": 123456,
    "Email": "Rlane@my365.bellevue.edu"
})
print("\nUpdated Student list:")
print_students(students)

with open('student.json', 'w') as f:
    json.dump(students, f, indent=4)

    print("\nThe student.json file has been updated.")
