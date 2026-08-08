Students=["Jason","Sally","Michael","Jamie","Tom","Dick","Harry"]
Ages=[]

for i in Students:
    x=(int(input(f"Enter {i}'s age:")))
    Ages.append(x)

l=int((len(Ages)))
s=int((sum(Ages)))
ave=round((s/l),2)

print(f"The average age of the class is {ave}.")
