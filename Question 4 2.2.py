with open("guardian_contacts.txt", "r") as f:
    data = f.read()
    print(data)

def load_guardians(filename="guardian_contacts.txt"):
    guardian_info = {}
    counter = 1

    with open(filename, "r") as f:
        header = f.readline().strip().split("\t")
        for line in f:
            parts = line.strip().split("\t")
            if len(parts) != 4:
                continue

            Student, Name, Phone, Address = parts

            guardian_info[f"Guardian{counter}"] = {
                "Student": Student,
                "Name": Name,
                "Phone": Phone,
                "Address": Address
            }
            counter += 1  

    return guardian_info
print(load_guardians())

def remove_guardian(guardian_info, student_name, filename="guardian_contacts.txt"):
    key_to_remove = None
    for key, info in guardian_info.items():
        if info["Student"] == student_name:
            key_to_remove = key
            break
    
    if key_to_remove:
        del guardian_info[key_to_remove]
        print(f"{student_name}'s guardian removed successfully.")
    else:
        print(f"{student_name}'s guardian not found.")
        return False
    
    
    with open(filename, "w") as f:
        f.write("Student\tName\tPhone\tAddress\n")
        for key, info in guardian_info.items():  
            line = f"{info['Student']}\t{info['Name']}\t{info['Phone']}\t{info['Address']}\n"
            f.write(line)
    
    print(f"{filename} updated.")
    return True


guardian = load_guardians()
remove_guardian(guardian, "Taran")
print(guardian)
