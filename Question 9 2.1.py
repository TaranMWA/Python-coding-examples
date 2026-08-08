enrol={
    "Taran":["python","maths","art"],
    "Chris":["python","science","english"],
    "Maddison":["history","python","geography"]
    }


x=input("Select student:").capitalize()
if x == "Taran":
    y=input("Add or Remove(a/r)?:")
    if y== "a":
        z=input("Add subject:")
        enrol["Taran"].append(z)
    else:
        z=input("Remove subject:")
        enrol["Taran"].remove(z)
elif x == "Chris":
    y=input("Add or Remove(a/r)?:")
    if y== "a":
        z=input("Add subject:")
        enrol["Chris"].append(z)
    else:
        z=input("Remove subject:")
        enrol["Chris"].remove(z)
elif x == "Maddison":
    y=input("Add or Remove(a/r)?:")
    if y== "a":
        z=input("Add subject:")
        enrol["Maddison"].append(z)
    else:
        z=input("Remove subject:")
        enrol["Maddison"].remove(z)
else:
    print("Student does not exist")


print(enrol)


a = set()
for subjects in enrol.values():
    a.update(subjects)
print(a)
    
