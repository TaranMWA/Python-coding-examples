import sqlite3

def get_students_by_grade(grade_level):
    conn = sqlite3.connect("student_management.db")
    cursor = conn.cursor()

    try:
        cursor.execute("""
            SELECT name, gpa
            FROM students
            WHERE grade_level = ?
        """, (grade_level,))
        rows = cursor.fetchall()

        if not rows:
            print(f"No students found in Grade {grade_level}.")
            return

        print(f"Students in Grade {grade_level}:")
        total_gpa = 0
        count = 0

        for name, gpa in rows:
            print(f"Name: {name}, GPA: {gpa}")
            total_gpa += gpa
            count += 1

        average_gpa = total_gpa / count
        print(f"\nAverage GPA for Grade {grade_level}: {average_gpa:.2f}")

    except sqlite3.Error as e:
        print(f"Database error: {e}")
    finally:
        conn.close()

if __name__ == "__main__":
    get_students_by_grade("9")
