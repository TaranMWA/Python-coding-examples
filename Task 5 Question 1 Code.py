import json #JSON used to store and transfer data, allows data to be kept in a JSON file
import os #Interacts with the operating system on machine
 
STUDENTS_FILE = "students.json" #Name of file that will hold the data
MAX_STUDENTS = 10 #Setting maxium number of students, 10 is an interger
 
students = [] #Starts with empty list so user can add students
 
 
def load_students():
    """Load students from file if it exists."""
    global students  #Use the global students list from outside this function
    
    if os.path.exists(STUDENTS_FILE): #Check if the file exists first
        try:         
            with open(STUDENTS_FILE, 'r') as f: #Open the file and load JSON data into the students list
                students = json.load(f)
        except:         
            students = [] #If the reading fails, start with an empty list
    else:
        students = []#If file does not exist, start with an empty list
 
 
def save_students():
    """Save students to file.""" 
    with open(STUDENTS_FILE, 'w') as f: #Open the file in write mode so data can be added     
        json.dump(students, f, indent=2) #Save the students list as JSON with indentation
 
 
def display_menu(): # Heading of the main menu
    print("=" * 50)
    print("         STUDENT REGISTRATION SYSTEM")
    print("=" * 50)
    print("1. Add New Student")#Options of the menu
    print("2. View All Students")
    print(f"3. View Remaining Slots ({MAX_STUDENTS - len(students)}/{MAX_STUDENTS})")# Show how many slots are left
    print("4. Remove Student")
    print("5. Exit")
    print("-" * 50)#Bottom of menu
 
 
def add_student():
    """Add a new student if under limit."""
    if len(students) >= MAX_STUDENTS:
        print("Maximum capacity (10 students) reached!")
        return # Cannot add any more than 10 students
 
    print("Enter Student Details:")
    print("-" * 20) # User can enter student details if enough slots
 
    student = {} # Create an empty dictionary for one student
    
    student["name"] = input("Name: ").strip().title() # Get values and format the text
    student["age"] = input("Age: ").strip()
    student["gender"] = input("Gender (M/F): ").strip().upper()
    student["student_id"] = input("Student ID: ").strip().upper()
    student["contact"] = input("Contact Number: ").strip()
 
    if not all([student["name"], student["age"], student["gender"],
                student["student_id"], student["contact"]]):
        print("All fields are required!")# Check that all info has been inputted
        return
 
    if any(s["student_id"] == student["student_id"] for s in students):
        print("Student ID already exists!") # Check if the student ID already exists to avoid duplicates 
        return
 
    students.append(student) # Adds the student to the list
 
    save_students()# Saves updated list to file
 
    print(f"Student '{student['name']}' registered successfully!") # Confirm registered and remaining slots
    print(f"Total students: {len(students)}/{MAX_STUDENTS}")
 
 
def view_students():
    """Display all registered students."""
    
    if not students:
        print("No students registered yet.") #If there are no students
        return
 
    print("REGISTERED STUDENTS:") #Table header
    print("-" * 60)
    print(f"{'ID':<8} {'Name':<12} {'Age':<5} {'Gender':<7} {'Contact'}")
    print("-" * 60)
 
    for i, student in enumerate(students, 1): # Loop through each student and print info
        print(f"{student['student_id']:<8} {student['name']:<12} "
              f"{student['age']:<5} {student['gender']:<7} {student['contact']}")
 
    print(f"Total: {len(students)}/{MAX_STUDENTS} students registered") # Show total number of students


def remove_student():
    """Remove a student by Student ID."""
    if not students: #Message if there are no students to remove
        print("No students to remove.")
        return

    student_id = input("Enter Student ID to remove: ").strip().upper()#Uses student ID to remove and formats the input to match

    for student in students:
        if student["student_id"] == student_id:
            students.remove(student)
            save_students()
            print(f"Student '{student['name']}' removed successfully!")
            print(f"Total students: {len(students)}/{MAX_STUDENTS}")
            return

    print("Student ID not found!")
 
 
def main():
    """Main program loop."""
 
    load_students() # Loads saved students from file when the program starts
 
    while True:
        display_menu()#Keep showing the menu until the user chooses to exit
 
        choice = input("Enter your choice (1-5): ").strip()#Get the user choice the if loop displays corressponding action
        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            print(f"Remaining slots: {MAX_STUDENTS - len(students)}/{MAX_STUDENTS}")
        elif choice == "4":
            remove_student()
        elif choice == "5":
            print("Thank you for using Student Registration System!")
            print("Data saved to 'students.json'")
            break
        else:
            print("Invalid choice! Please enter 1-5.") #Message if an invalid key is pressed
 
        input("Press Enter to continue...")#User needs to press Enter to go back to menu, does not jump back automatically 
 
if __name__ == "__main__": #Run the program only if this file is executed directly and not imported
    main()
