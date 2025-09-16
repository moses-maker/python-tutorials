"""
Function with a return value
> This is a function whose last statement has the return keyword and a value
e.g. return value

> You c

"""

# function definition with a return value
def rectangle(length, width):
    area = length * width
    return area


# function call with a return value

"""
one way of calling a function with a return value is to put the function that is
rectangle() inside the built-in print() function call.

Inside the rectangle() function call supply arguments corresponding with the number
of parameters.

arguments - values supplied during function call.
parameters - variables that holds the values you have to supply during function calling.
"""
print(rectangle(70, 60))


"""
Second way of calling a function is by supplying a variable called instance variable
to hold the function call in this case rectangle().

Then put the instance variable in the print() function  call as it s argument.
"""

r = rectangle(78, 50)
print(f"The area of rectangle is {r}")

"""
You can be able to return multiple values to the function call.
e.g return value 1, value 2
In this case you will equal number of instance variable as the return values.

"""
def cube(s):
    # surface area
    area_of_one_side = s * s
    surface_area = area_of_one_side*6

    # volume of a cube
    volume_of_a_cube = s*s*s

    return surface_area, volume_of_a_cube

x, y = cube(8)
print(f"The surface area of cube is {x} and the volume of a cube is {y}")




