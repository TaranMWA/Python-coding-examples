students = {
    "student1": {
        "name": "Taran Anderson",
        "student_ID":"111",
        "grade_level":10,
        "gpa": 3.8
        },
    "student2": {
        "name": "Chris Eze",
        "student_ID":"112",
        "grade_level": 8,
        "gpa": 4.2
        },
    "student3": {
        "name": "Maddison Connelly",
        "student_ID":"113",
        "grade_level": 7,
        "gpa": 2.6
        },
    }
with open("student_data.txt", "x") as f:
    f.write("Name\tID\tGrade\tGPA\n")
    for student_id, info in students.items():
        line = f"{info['name']}\t{info['student_ID']}\t{info['grade_level']}\t{info['gpa']}\n"
        f.write(line)

print("student_data.txt has been created and populated.")
