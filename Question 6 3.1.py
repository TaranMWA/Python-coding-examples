subjects=[]
while True:
    subjectName=str(input("Name of subject you would like to enrol into (press Enter after final subject):"))
    if subjectName =="":
        break
    subjects.append(subjectName)
print(f"You have enrolled into the following subjects:{subjects}" )
