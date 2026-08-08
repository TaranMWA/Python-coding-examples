def attendance_status(numDaysPresent,totalTeachDays):
    x=int((numDaysPresent/totalTeachDays)*100)

    if x >= 95:
        return("Excellent")
    elif x >=90:
        return("Good")
    else:
        return("Concern")

print(attendance_status(35,50))
print(attendance_status(50,50))
print(attendance_status(44,50))
print(attendance_status(10,50))
print(attendance_status(47,50))

