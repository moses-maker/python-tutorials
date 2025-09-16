class Rectangle:
    # class variable
    color = "Red" # attribute (variable)
    # constructor method
    def __init__(self, length, width):
        # length = 67, 
        # self.length= length
        print("Testing constructor method")
        self.length = length
        self.width = width

    def area(self):
        area = self.length * self.width
        print(area)

# Instantiation or object creation
shape = Rectangle(67, 45) # shape is the object created from class Rectangle
# The moment you create an object constructor method is called hence executed

print(shape.color) # attribute referencing
shape.area() # method referencing
