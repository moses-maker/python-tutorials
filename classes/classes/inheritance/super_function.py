class Shapes:
    def __init__(self, length, width, height, radius, base ):
        self.length = length
        self.width = width
        self.height = height
        self.radius = radius
        self.base = base

class Rectangle(Shapes):
    def __init__(self, length, width, height, radius, base, color):
        super().__init__(length, width, height, radius, base)
        self.color = color
    def area(self):
        area = self.length * self.width
        print(area, self.color)
    def volume(self):
        volume = self.length * self.width * self.height
        print(volume, self.color)

class Circle(Shapes):
    def __init__(self, length, width, height, radius, base, color):
        super().__init__(length, width, height, radius, base)
        self.color = color

    def area(self):
        area = 3.14159 * self.radius * self.radius
        print(f"The area of circle is {area} and color {self.color}")

Child_object = Circle(1000, 948, 700, 7, 560, "red")
Child_object.area()
