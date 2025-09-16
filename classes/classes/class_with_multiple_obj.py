class Shapes:
    def __init__(self, l, w, h, r, s, b):
        self.length = l
        self.width = w
        self.height = h
        self.radius = r
        self.side = s
        self.base = b

    def rectangle(self):
        area = self.length* self.width
        print("The area of square is", area)

    def triangle(self):
        area = 0.5 * self.base * self.height
        print("The area of triangle is", area)

    def square(self):
        area = self.side * self.side
        print("The area of square is", area)

    def circle(self):
        area = 3.14 * self.radius**2
        print("The area of circle is", area)

# multiple objects depiction
rec_obj = Shapes(3, 8, 5, 9, 3, 2)
rec_obj.rectangle()

tri_obj = Shapes(9, 7, 4, 6, 3, 4)
tri_obj.triangle()

sq_obj = Shapes(8, 5, 6, 4, 3, 7)
sq_obj.square()

ci_obj = Shapes(9, 7, 5, 4, 3, 14)
ci_obj.circle()
