"""
void function
> This is a function definition that has print() function
as the last statement in the function definition block.
"""

def rectangle(length, width):
    area_of_rectangle = length * width
    #This is void function as the last statement is print() function call
    print(area_of_rectangle)

l = 50
w = 45
rectangle(l, w)

def hello():
    print("Hello world")

hello()


