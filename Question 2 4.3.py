def calculate_percentage(marks_obtained,total_marks):
    percentage=(marks_obtained/total_marks)*100
    x=(f"Your percentage is {percentage}%")
    return x

print(calculate_percentage(45,60))
print(calculate_percentage(3,40))
print(calculate_percentage(100,750))
print(calculate_percentage(90,180))
