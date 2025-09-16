"""
These are function definitions, their implementation will be done on another file.


"""
pi = 22/7

def rectangle(length, width):
    area =  length * width
    return area

def circle(radius):
    area = 3.14159 * radius * radius
    print(area)

def square(side):
    area = side * side
    print(area)

def triangle(base, height):
    area = 0.5 * base * height
    print(area)

def trepezium(a, b, h):
    area = 0.5*(a+b)*h
    print(area)

def cube(s):
    one=s*6
    area = one**2
    print(area)
