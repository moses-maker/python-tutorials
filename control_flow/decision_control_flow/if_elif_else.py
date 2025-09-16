# dynamic input
mathematics = int(input("Enter marks for mathematics?"))
english = int(input("Enter average_marks for english?"))
kiswahili = int(input("Enter marks for kiswahili?"))
science = int(input("Enter marks for science?"))

total_average_marks = mathematics + english + kiswahili + science

average_marks = total_average_marks/4    # 40

if average_marks>20 and average_marks<30:  # 20, 30
    print("Average grade is D-")

elif average_marks>=30 and average_marks<=40: # 30, 40
    print("Average grade is D")

elif average_marks>=40 and average_marks<=50: # 40, 50
    print("Average grade is D+")

elif average_marks>50 and average_marks<60:
    print("Average grade is C")

elif average_marks>60 and average_marks<70:
    print("Average grade is is B")

elif average_marks>70 and average_marks<80:
    print("Average grade is B+")

elif average_marks>80 and average_marks<=100:
    print("Average grade is A")

else:
    print("Try again")