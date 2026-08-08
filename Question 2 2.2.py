with open("student_data.txt", "r") as f:
    data = f.read()
    print(data)

def load_students(filename="student_data.txt"):
    students = {}
    counter = 1

    with open(filename, "r") as f:
        header = f.readline().strip().split("\t")
        for line in f:
            parts = line.strip().split("\t")
            if len(parts) != 4:
                continue

            name, student_ID, grade, gpa = parts

            students[f"Student{counter}"] = {
                "name": name,
                "student_ID": student_ID,
                "grade_level": int(grade),
                "gpa": float(gpa)
            }
            counter += 1  

    return students
print(load_students())

def remove_student(students, student_key, filename="student_data.txt"):
    if student_key in students:  
        del students[student_key]
        print(f"{student_key} removed successfully.")
    else:
        print(f"Student {student_key} not found.")
        return False
    
    with open(filename, "w") as f:
        f.write("Name\tID\tGrade\tGPA\n")  
        for key, info in students.items():
            line = f"{info['name']}\t{info['student_ID']}\t{info['grade_level']}\t{info['gpa']}\n"
            f.write(line)
    
    print(f"{filename} updated.")
    return True

students=load_students()
remove_student(students, "Student3")
print(students)
