#dynamic entry
year = int(input("Enter the year:"))


if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(year, "is  a Leap Year. ")
        else:
            print(year, "is not a Leap Year")
    else:
        print(year, "is a Leap Year")
else:
    print(year, "is not a Leap Year")


"""
ask a user to enter a number. The program should be capable of evaluating the value
user has entered as either "even" number or "odd" number.

hints
modulus(%) and equal to(==) 
if varaible % 4 == 0:
    statement

"""


