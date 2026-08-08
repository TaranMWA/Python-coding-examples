import sqlite3

def delete_student_by_id(student_id):
    conn = sqlite3.connect("student_management.db")
    cursor = conn.cursor()

    try:
        cursor.execute(
            "DELETE FROM students WHERE student_id = ?",
            (student_id,)
        )
        conn.commit()

        cursor.execute("SELECT * FROM students")
        students = cursor.fetchall()

        print(f"Remaining students after deleting ID {student_id}:")
        for student in students:
            print(
                f"ID: {student[0]}, "
                f"Name: {student[1]}, "
                f"Grade: {student[2]}, "
                f"Major: {student[3]}, "
                f"GPA: {student[4]}, "
                f"Enrollment Date: {student[5]}"
            )

    except sqlite3.Error as e:
        print(f"Database error: {e}")
    finally:
        conn.close()

if __name__ == "__main__":
    delete_student_by_id(1002)
