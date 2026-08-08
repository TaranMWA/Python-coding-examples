from datetime import time, datetime

Taran={
    time(7,0):"python",
    time(8,30):"maths",
    time(12,15):"science"
    }

Chris={
    time(7,30):"python",
    time(9,45):"english",
    time(13,0):"art"
    }

Maddison={
    time(10,15):"python",
    time(12,30):"history",
    time(14,0):"geography"
    }

listOfStudents=[Taran, Chris, Maddison]
subjects=[]

for student in listOfStudents:
 for t, activity in student.items():
     x=(f"{t.strftime("%H:%M")} - {activity}")
     print(x)
     subjects.append(x)

y = sorted(subjects, key=lambda s: datetime.strptime(s.split(' - ')[0], '%H:%M'))
print("\nSorted chronologically:")
for item in y:
    print(item)

    

