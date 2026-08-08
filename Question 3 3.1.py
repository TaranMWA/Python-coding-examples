Students=["Jason","Sally","Michael","Jamie","Tom","Dick","Harry"]
Marks=[]

for i in Students:
    x=(int(input(f"Enter {i}'s mark:")))
    Marks.append(x)

l=int((len(Marks)))
s=int((sum(Marks)))
ave=round((s/l),2)

print(f"The average mark for the class is {ave}.")
