Present=[]
Absent=[]
Students=["Jason","Sally","Michael","Jamie"]
for i in Students:
    x=(input(f"Is {i} present? y/n:"))
    if x=="y":
        Present.append(i)
    else:
        Absent.append(i)
print("Students present:",Present)
print("Students absent:",Absent)
