names=[]
while True:
    name=str(input("Add student name to list (or press Enter to finish):"))
    if name =="":
        break
    names.append(name)
search=input("Search student name:")
while True:
    print("This name exists" if search in names else "This name does not exist")
    x=input("Search again?(y/n):")
    if x == "y":
        search=input("Search student name:")
    else:
        break
