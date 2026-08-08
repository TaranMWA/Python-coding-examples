maths=int(input("Enter your score for Maths:"))
english=int(input("Enter your score for English:"))
it=int(input("Enter your score for IT:"))
marks=[maths,english,it]
print(marks)
total=maths+english+it
ave=total/3
print(f"Your total marks equal {total}.")
print(f"Your mark average is {ave}.")
#int are used for marks as the value needs to be a mathematical number to perfrom a calculation, a list is used to store them as mulitple values can be stored inside one list.
