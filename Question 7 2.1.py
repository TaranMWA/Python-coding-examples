Taran={
    "name": "Taran Anderson",
    "student_id": "1025818",
    "total_classes": 55,
    "classes_attended": 55,
    "age": 28
    }

Chris={
    "name": "Christopher Eze",
    "student_id": "1044875",
    "total_classes": 55,
    "classes_attended": 40,
    "age": 34
    }

Maddison={
    "name": "Maddison Connelly",
    "student_id": "1069356",
    "total_classes": 60,
    "classes_attended": 37,
    "age": 20
    }

listOfStudents=[Taran, Chris, Maddison]
perList=[]

for student in listOfStudents:
    percentage= (student["classes_attended"]/student["total_classes"])*100
    print(f"The attendance percentage for {student['name']} is {round(percentage,2)}")
    perList.append(int(percentage))
    
print(max(perList))


      
