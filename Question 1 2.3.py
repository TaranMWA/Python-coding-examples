import sqlite3

conn = sqlite3.connect("student_management.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    student_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    grade_level TEXT NOT NULL,
    major TEXT NOT NULL,
    gpa REAL NOT NULL,
    enrollment_date TEXT NOT NULL
)
""")

cursor.executemany("""
INSERT INTO students (student_id, name, grade_level, major, gpa, enrollment_date)
VALUES (?, ?, ?, ?, ?, ?)
""", [
    (1001, "Emma", "10", "Computer Science", 3.8, "2024-09-01"),
    (1002, "Liam", "10", "Mathematics", 3.6, "2024-09-02"),
    (1003, "Sophia", "11", "English", 3.9, "2024-09-03")
])

conn.commit()
conn.close()

print("Database 'Student Management' created student sucessfully")
