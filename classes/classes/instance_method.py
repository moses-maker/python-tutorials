class Rectangle:
    def __init__(self, l, w, h):
        self.length = l
        self.width = w
        self.height = h
    # instance method 1
    def area(self):
        area = self.length * self.width
        return area
    # instance method 2
    def volume(self):
        volume = self.length * self.width * self.height
        return volume

# take user inputs
l = int(input("Enter the length?"))  
w = int(input("Enter the width?"))
h = int(input("Enter the height?"))

# object creation/ class instantiation
shape = Rectangle(l, w, h)

# call the methods attributes inside the class using shape object
print(shape.area())
print(shape.volume())