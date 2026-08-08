subjects=[]
while True:
    name=str(input("Enter subject name (press Enter after last subject):"))
    if name =="":
        break
    score=int(input(f"Enter mark for {name}:"))
    subjects.append(score)
    if score >= 80:
        print(f"Performance for {name}- Excellent") 
    elif score >= 60:
        print(f"Performance for {name}- Good")
    elif score >= 40:
        print(f"Performance for {name}- Average") 
    else:
        print(f"Performance for {name}- Poor")
    
marks=sum(subjects)

if marks >= 150:
    print("Overall performance - Excellent") 
elif marks >= 100:
    print("Overall performance - Good")
elif marks >= 60:
    print("Overall performance - Average") 
else:
    print("Overall performance - Poor")
