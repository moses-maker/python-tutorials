# if statement
"""
if condition:
    statements/block

#dynamic entry
marks = int(input("Enter your marks?"))

# if statement
if total>50: # is total > 50 ?    (True or False)-
    print("Great job")

# if ...else statement
if total>50:  #True
    print("Pass")

else:# false
    print("you have failed your marks is", total)
"""

# if ...elif  ...else
#Enter marks eng, kisw, sci, math, social_studies, cre
print("welcome to school grading system")
english = int(input("Enter marks for english after question mark?"))
kiswahili = int(input("Enter marks for kiswahili after question mark?"))
science = int(input("Enter marks for science after question mark?"))
social_studies = int(input("Enter marks for social studies after question mark?"))
cre = int(input("Enter marks for cre after question mark?"))

total_marks = english + kiswahili + science + social_studies + cre

print("Hello!, your total marks is", total_marks)

average_marks = total_marks / 6

print("Hello!, your average marks is", average_marks)

if average_marks > 46 and average_marks<=49:
    print("Based on your average marks, your grade is { D }")

elif average_marks > 50 and average_marks<=54:
    print("Based on your average marks, your grade is { C }")

elif average_marks > 54 and average_marks<=59:
    print("Based on your average marks, your grade is { C+ }")

elif average_marks > 60 and average_marks<=64:
    print("Based on your average marks, your grade is { B- }")

elif average_marks > 64 and average_marks<=69:
    print("Based on your average marks, your grade is { B }")

elif average_marks > 69 and average_marks<=74:
    print("Based on your average marks, your grade is { B+ }")

elif average_marks > 74 and average_marks<=79:
    print("Based on your average marks, your grade is { A- }")

elif average_marks > 79 and average_marks<=100:
    print("Based on your average marks, your grade is { A }")

else:
    print("Please enter your marks carefully")




