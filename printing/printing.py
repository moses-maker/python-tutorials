# display string
print("Hello world")

# display numbers
print(10)
print(97.98)

# display value stored in a variable
h = 10
print(h)

input()

# 1. formatting
marks = 100
print("The total marks is", marks)
print("The area is ", 43245,"m2")

# 2. f-string
print(f"The total marks is {marks}")
print(f"The area is {43245}m2")

# 3. str.format()
print("The total marks is {}".format(marks))
print("The area is {}m2".format(43245))

l = 60
w = 45
# f-string
print(f"{l}m x {w}m  =  {l * w}m2")
print("{}m x {}m = {}m2".format(l, w, l*w))