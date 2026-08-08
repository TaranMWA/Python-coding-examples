import sqlite3

def update_liam_gpa():
    conn = sqlite3.connect("student_management.db")
    cursor = conn.cursor()

    try:
        cursor.execute("""
            UPDATE students
            SET gpa = 3.7
            WHERE name = 'Liam'
        """)
        conn.commit()

        cursor.execute("SELECT * FROM students")
        students = cursor.fetchall()

        print("Students in the database after GPA update:")
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
    update_liam_gpa()
