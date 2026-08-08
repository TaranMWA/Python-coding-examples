guardians = {
    "Taran": {
        "Name": "Mike Sal",
        "Phone":"012456",
        "Address":"Trinidad"
        },
    "Chris": {
        "Name": "James Bond",
        "Phone":"00715",
        "Address":"Nigeria"
        },
    "Maddison": {
        "Name": "Harry Potter",
        "Phone":"084512",
        "Address":"Hogwarts"
        },
    }
#with open("guardian_contacts.txt", "x") as f:  
#    f.write("Student\tName\tPhone\tAddress\n")  
#    for student, info in guardians.items():
#        line = f"{student}\t{info['Name']}\t{info['Phone']}\t{info['Address']}\n"
#        f.write(line)

#print("guardian_contacts.txt has been created and populated.")

with open("guardian_contacts.txt", "r") as f:
    data = f.read()
#    print(data)

def update_guardian_phone(guardians, student_name, new_phone, filename="guardian_contacts.txt"):   
    if student_name in guardians:        
        guardians[student_name]["Phone"] = new_phone
    
        with open(filename, "w") as f:
            f.write("Student\tName\tPhone\tAddress\n")
            for student, info in guardians.items():
                line = f"{student}\t{info['Name']}\t{info['Phone']}\t{info['Address']}\n"
                f.write(line)
        
        print(f"Updated {student_name}'s guardian phone to {new_phone}")
        return True
    else:
        print(f"Student '{student_name}' not found.")
        return False

update_guardian_phone(guardians,"Taran", "123456")
with open("guardian_contacts.txt", "r") as f:
    data = f.read()
    print(data)
