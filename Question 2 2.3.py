import sqlite3

def read_students():
    conn = sqlite3.connect("student_management.db")
    cursor = conn.cursor()

    try:
        cursor.execute("SELECT * FROM students")
        students = cursor.fetchall()
        
        print("Students in the database:")
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
        print(f"Error reading from database: {e}")
    finally:
        conn.close()

if __name__ == "__main__":
    read_students()
