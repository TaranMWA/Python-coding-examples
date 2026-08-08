Students=["Jason","Sally","Michael","Jamie","Tom","Dick","Harry"]
examResults=[]

for i in Students:
    x=(int(input(f"Enter {i}'s exam result:")))
    examResults.append(x)

highest=max(examResults)
lowest=min(examResults)
print(f"The highest exam result is {highest} and the lowest exam result is {lowest}.")
