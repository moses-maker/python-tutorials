"""
ways of entering values in python
a) static input
> in static input values are entered when the program
is not running.
> We use the assignment operator e.g =
    total = 100
b) dynamic input
> In dynamic input values re entered when the 
program is running.
> We use the input() function to enter values.
    variable_name = input("prompt?")

# static
total = 100
print(total)

# dynamic
result = input("Enter value:")
print(result)

"""
# total marks for maths, emglish, kiswahili, science  int(    )
maths = int(input("Enter marks for maths?"))
english = int(input("Enter marks for english?"))
kiswahili = int(input("Enter marks for kiswahili?"))
science = int(input("Enter marks for science?"))

# total marks
total_marks = maths + english + kiswahili + science
print(total_marks)



