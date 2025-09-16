class Rectangle:
    color = "red"

    def __init__(self, l, w, h):
        self.length = l
        self.width = w
        self.height = h

    @property
    def area(self):
        area = self.length * self.width
        return area
    
    @property
    def volume(self):
        volume = self.length * self.width * self.height
        print(volume)

# object creation/ class instantiation
shape = Rectangle(9, 5, 2)

# call the methods attributes inside the class using shape object
shape.volume
print(shape.area)
print(shape.color)
