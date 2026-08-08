name=str(input("Enter your name:")) #string as this is text to be read
completed=int(input("Enter units completed:"))#int as this is a numerical amount and may change
unit1=str(input("Enter first unit:"))
unit2=str(input("Enter second unit:"))
unit3=str(input("Enter third unit:"))
units=[unit1, unit2, unit3]#list so that mulitple values can be added to one variable name
totalUnits=len(units)
grade1=int(input("Enter grade for "+unit1+":"))
grade2=int(input("Enter grade for "+unit2+":"))
grade3=int(input("Enter grade for "+unit3+":"))
grades=[grade1, grade2, grade3]
totalGrade=sum(grades)
ave=float(totalGrade/totalUnits)#decimal number for more accurate percentage
sentence=(f"Your name is {name}, you have completed {completed} units, which are {unit1}, {unit2} and {unit3}. Your average overall grade percentage is {ave}%.")
print(sentence)
