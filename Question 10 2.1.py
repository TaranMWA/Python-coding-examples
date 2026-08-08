grades={
    "Taran":100,
    "Chris":90,
    "Maddison":85,
    "Saalem":70
    }

while True:
 x=input("Press 1 to add a new student, 2 to remove a student, 3 to update a grade, 4 to view dictionary:")
 if x == "1":
    n=input("Name:").capitalize()
    g=int(input("Grade:"))
    grades.update({n:g})
 elif x == "2":
    n=input("Name:").capitalize()
    del grades[n]
 elif x == "3":
    n=input("Name:").capitalize()
    g=int(input("Updated grade:"))
    grades[n]=g
 elif x == "4":
    print(grades)     
 else:
    print("Invalid option")

