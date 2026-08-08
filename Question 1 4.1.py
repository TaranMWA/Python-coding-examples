studentAges=[]
while True:
    name=str(input("Enter student name (or press Enter to stop):"))
    if name =="":
        break
    age=int(input(f"Enter {name}'s age:"))
    studentAges.append(age)
    
x=len(studentAges)
y=sum(studentAges)
print("The total number of students is:",x)
ave=y/x
print("The average age of the students is:",ave)
