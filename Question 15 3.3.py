paid=(input("Have you made a recent fee payment? (y/n):"))
if paid =="y":
    print("Cleared")
elif paid=="n":
    print("Payment Due")
else:
    print("unknown")
    
