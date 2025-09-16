class Shapes:
    model= "toyota"

    def __init__(self, l, w, r):
        print("Constructor method")
        self.length = l
        self.width = w
        self.radius = r

    def rectangle(self, c):
        s = "red"
        print("Rectangle shape")
        print(c, s)

    def circle(self, c):
        print("Circle shape")
        print(c)
# first object 1
l = 60
w = 30
h = 100
my_shape = Shapes(l, w, h)
shape4 = my_shape
my_shape.rectangle("blue")

# second object 2
shape2 = Shapes(657, 53, 533)
shape2.circle("red")