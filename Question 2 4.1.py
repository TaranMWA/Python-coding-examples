import math
marksAvailable=[]
marksObtained=[]

x=int(input("How many assessments have you completed?:"))

for i in range(x):
      y=int(input(f"Score for assessment {i+1}:"))
      marksObtained.append(y)
      z=int(input(f"Marks available for assessment {i+1}:"))
      marksAvailable.append(z)
      percent=(y/z)*100
      print(f"Percentage for assessment {i+1} is: {math.floor(percent)}%")

totalMarks=sum(marksObtained)
totalAvailable=sum(marksAvailable)
percentage=(totalMarks/totalAvailable)*100
a=(f"Total percentage across all assessments is {math.floor(percentage)}%")

print(a)

