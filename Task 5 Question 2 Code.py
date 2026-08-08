import json #JSON used to store and transfer data, allows data to be kept in a JSON file
import os #Interacts with the operating system on machine

STUDENTS_FILE = "marks.json" #Name of file that will hold the data

MAX_STUDENTS = 10 #Setting maxium number of students, 10 is an interger

SUBJECTS = ["Maths", "Science", "English"] #Subjects to collect marks for

students = []#Starts with empty list so user can add students


def load_students():
    """Load student records from the JSON file if it exists."""
    global students #Use the global students list from outside this function

    if os.path.exists(STUDENTS_FILE): #Check if the file already exists
        try:
            with open(STUDENTS_FILE, "r") as f:#Open the file and read the saved JSON data
                students = json.load(f)
        except:
            students = []#If the reading fails, start with an empty list
    else:
        students = []#If the file does not exist, start with an empty list


def save_students():
    """Save student records to the JSON file."""
    with open(STUDENTS_FILE, "w") as f: #Open the file in write mode so data can be added
        json.dump(students, f, indent=2) #Save the students list as JSON with indentation


def get_valid_mark(subject):
    """Ask the user for a valid mark between 0 and 100."""
    while True:
        mark = input(f"Enter marks for {subject}: ").strip() #Get input from the user and format

        try:
            mark = int(mark)#Convert the input to an integer
            if 0 <= mark <= 100:#Check that the mark is in the valid range
                return mark
            else:
                print("Marks must be between 0 and 100.")
        except ValueError:#Show an error if the input is not a number
            print("Invalid input! Please enter a whole number.")


def calculate_grade(percentage):
    """Calculate the grade based on percentage.""" #If statement to determine grade
    if percentage >= 90:
        return "A"
    elif percentage >= 80:
        return "B"
    elif percentage >= 70:
        return "C"
    elif percentage >= 60:
        return "D"
    else:
        return "F"


def add_student_marks():
    """Add marks for a new student."""
    if len(students) >= MAX_STUDENTS:
        print("Maximum capacity (10 students) reached!")#Stop if the system already has the maximum number of students
        return
    print("Enter Student Details:")
    print("-" * 25)

    student = {} #Create a dictionary to store one student's data

    student["name"] = input("Name: ").strip().title() #Get the student's name and format
    
    if not student["name"]: #Make sure the name is not blank
        print("Student name is required!")
        return

    if any(s["name"].lower() == student["name"].lower() for s in students):
        print("Student already exists!") #Prevent duplicate student names
        return

    student["marks"] = {} #Create a dictionary to store marks for each subject

    for subject in SUBJECTS:
        student["marks"][subject] = get_valid_mark(subject) #Ask for marks in each subject

    total = sum(student["marks"].values()) #Add all marks together

    percentage = total / (len(SUBJECTS) * 100) * 100 #Calculate percentage based on total marks out of 300

    grade = calculate_grade(percentage) #Get the grade from the percentage

    student["total"] = total #Store the calculated results in the student record
    student["percentage"] = round(percentage, 2)#Round to 2 decimal places
    student["grade"] = grade
    students.append(student) #Add the student record to the main list
    save_students() #Save the updated list to the JSON file

    print(f"Marks saved for {student['name']} successfully!")


def display_students():
    """Display all stored student marks."""
    if not students: #Check if there are no records
        print("No student marks recorded yet.")
        return

    print("\nSTUDENT MARKS RECORD")
    print("-" * 80)
    #Print table headings
    print(f"{'Name':<15} {'Maths':<8} {'Science':<8} {'English':<8} {'Total':<8} {'%':<8} {'Grade'}")
    print("-" * 80)
    
    for student in students:#Loop through each student and display their details
        print(f"{student['name']:<15} "
              f"{student['marks']['Maths']:<8} "
              f"{student['marks']['Science']:<8} "
              f"{student['marks']['English']:<8} "
              f"{student['total']:<8} "
              f"{student['percentage']:<8} "
              f"{student['grade']}")

    print("-" * 80)
    print(f"Total students: {len(students)}/{MAX_STUDENTS}")


def display_menu(): #Options for the main menu
    """Show the main menu."""
    print("=" * 50)
    print("      SUBJECT MARKS MANAGEMENT SYSTEM")
    print("=" * 50)
    print("1. Enter Student Marks")
    print("2. Display All Students")
    print("3. View Remaining Slots")
    print("4. Exit")
    print("-" * 50)


def main():
    """Main program loop."""
    load_students() #Load saved student data when the program starts
    while True:#Keep showing the menu until the user exits
        display_menu()
        
        choice = input("Enter your choice (1-4): ").strip()#Get the user choice the if loop displays corressponding action

        if choice == "1":
            add_student_marks()
        elif choice == "2":
            display_students()
        elif choice == "3":
            print(f"\nRemaining slots: {MAX_STUDENTS - len(students)}/{MAX_STUDENTS}")
        elif choice == "4":
            print("\nThank you for using the Subject Marks Management System!")
            break
        else:
            print("Invalid choice! Please enter 1-4.")#Message if an invalid key is pressed

        input("Press Enter to continue...") #User needs to press Enter to go back to menu, does not jump back automatically


if __name__ == "__main__": #Run the program only if this file is executed directly and not imported
    main()
