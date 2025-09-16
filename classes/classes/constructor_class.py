class Rectangle:
    def __init__(self, l, w, h):
        # instance variables, variables created inside a method.
        self.length = l
        self.width = w
        self.height = h

    def area(self):
        rectangle_area = self.length * self.width
        return rectangle_area
    
    def volume(self, color):
        rectangle_volume = self.length * self.width * self.height
        return color, rectangle_volume
    

a = 90
b = 60
c = 40

rec = Rectangle(a, b, c)
rec.area()

# inputting argument values dynamically using input() function
l = int(input("Enter the length?"))
w = int(input("Enter the width?"))
h = int(input("Enter the height?"))

# created an object
rectangle_object = Rectangle(l, w, h)
instance_variable_area = rectangle_object.area()
print("The area of a rectangle is ", instance_variable_area)
color, instance_variable_volume = rectangle_object.volume("red")
print("The color of rectangle is ", color, "and the volume of a rectangle is ", instance_variable_volume)



"""
def main():
    # inputting argument values dynamically using input() function
    l = int(input("Enter the length?"))
    w = int(input("Enter the width?"))
    h = int(input("Enter the height?"))

    # created an object
    rectangle_object = Rectangle(l, w, h)

    instance_variable_area = rectangle_object.area()
    print("The area of a rectangle is ", instance_variable_area)

    color, instance_variable_volume = rectangle_object.volume("red")
    print("The color of rectangle is ", color, "and the volume of a rectangle is ", instance_variable_volume)

if __name__ == "__main__":
    main()

"""
