studentInfo=[]
while True:
    name=str(input("Enter student name (or press Enter to stop):"))
    if name =="":
        break
    ID=str(input("Enter the student's ID:"))
    studentInfo.append((name,ID))
for i in studentInfo:
    print(i)

