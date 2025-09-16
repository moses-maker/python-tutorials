class Rectangle:
    # class variable
    color="blue"

    def __init__(self, l, w):
        self.length = l
        self.width = w

    def area(self):
        area = self.length * self.width
        print(f"The rectangle of {color} in color has the area of {area}")
        

    def volume(self):
        #local variable
        height = 70
        volume = self.length * self.width * height
        print(f"The rectangle of {color} in color has the area of {area}m2 and volume is {volume}m3")

# object creation
rectangle_object = Rectangle(45, 23)

# accessing the class variable directly using the object.
print(rectangle_object.color)

# public method
print(rectangle_object.length)
    