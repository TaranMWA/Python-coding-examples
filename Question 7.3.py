student1=int(input("Enter student 1 age:")) #values stored as int as they will be used for mathematical calculations
student2=int(input("Enter student 2 age:"))
student3=int(input("Enter student 3 age:"))
student4=int(input("Enter student 4 age:"))
total=[student1, student2, student3, student4]
numOfStudents=len(total)
age=(sum(total))
ave=age/numOfStudents
print(numOfStudents)
print(age)
print(ave)
