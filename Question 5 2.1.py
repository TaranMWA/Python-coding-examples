Taran={
    "name": "Taran Anderson",
    "student_id": "1025818",
    "grade_level": "Distinction",
    "major": "Python",
    "age": 28
    }

Chris={
    "name": "Christopher Eze",
    "student_id": "1044875",
    "grade_level": "Merit",
    "major": "JavaScript",
    "age": 34
    }

Maddison={
    "name": "Maddison Connelly",
    "student_id": "1069356",
    "grade_level": "Pass",
    "major": "Cisco Networking",
    "age": 20
    }

listOfStudents=[Taran, Chris, Maddison]

total_age = 0
for student in listOfStudents:
    total_age += student["age"]

ave_age = total_age / len(listOfStudents)

print(f"The average age of students is {round(ave_age,2)}")

      
