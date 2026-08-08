Taran={
    "name": "Taran Anderson",
    "student_id": "1025818",
    "GPA": 4.2,
    "attendance_percentage": 99,
    "age": 28
    }

Chris={
    "name": "Christopher Eze",
    "student_id": "1044875",
    "GPA": 3.6,
    "attendance_percentage": 75,
    "age": 34
    }

Maddison={
    "name": "Maddison Connelly",
    "student_id": "1069356",
    "GPA": 2.6,
    "attendance_percentage": 80,
    "age": 20
    }

listOfStudents=[Taran, Chris, Maddison]

for student in listOfStudents:
    if student.get("GPA") <=3.9:
     print(student["name"])
      

      
