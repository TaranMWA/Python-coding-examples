Taran={
    "name": "Taran Anderson",
    "student_id": "1025818",
    "grade_level": "Distinction",
    "major": "Python"
    }

listOfStudents=[Taran]

Chris={
    "name": "Christopher Eze",
    "student_id": "1044875",
    "grade_level": "Merit",
    "major": "JavaScript"
    }
listOfStudents.append(Chris)

x=input("Enter grade level:")
y=x.capitalize()
for student in listOfStudents:
    if student.get("grade_level") == y:
     print(student.get("name"))
      
