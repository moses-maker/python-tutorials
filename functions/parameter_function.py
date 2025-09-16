# parameter function

"""
parameter - variables that holds values you supply as argument.
argument - it is a value you supply during function call.

"""

def rectangle(length, width):
    area = length * width
    print(area)
    # return area

# a) pass by value - supplying argument values directly to the function call
rectangle(78, 20)

# b) pass by reference - supply variable that store value to function call 
# static input
length = 45
width = 30
rectangle(length, width)

# c) pass by reference - (dynamic input)
l = int(input("Enter length:"))
w = int(input("Enter width:"))
rectangle(l , w)






