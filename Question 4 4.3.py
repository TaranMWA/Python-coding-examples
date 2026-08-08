def classify_progress(overallGradePercentage):
    if overallGradePercentage >= 75:
        return("Distinction")
    elif overallGradePercentage >= 60:
        return("Merit")
    elif overallGradePercentage >= 40:
        return("Pass")
    else:
        return("Fail")

print(classify_progress(67))
print(classify_progress(2))
print(classify_progress(88))
print(classify_progress(41))
print(classify_progress(32))
print(classify_progress(78))
