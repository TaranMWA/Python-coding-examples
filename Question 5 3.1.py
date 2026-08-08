Students=["Jason","Sally","Michael","Jamie","Tom","Dick","Harry"]
Payment=[]

for i in Students:
    x=(int(input(f"Total fee amount paid by {i} in £:")))
    Payment.append(x)


s=float((sum(Payment)))
print(f"Total amount paid by all students is £{s}.")



