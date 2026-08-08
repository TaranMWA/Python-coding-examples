classList=[]
while True:
    action=input("Choose what to do with a name - add/remove/view:")
    if action =="add":
        classList.append(input("name:"))
    elif action == "remove":
        classList.remove(input("name:"))
    elif action == "view":
        print(classList)
    else:
        print("Try again")
