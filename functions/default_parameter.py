# default parameter
def rectangle(length, width=40):
    area = length * width
    print(area)

rectangle(60)
rectangle(70, 35)


# keyword argument
def volume(length, width=40, height=70):
    volume = length * width * height
    print(volume)

volume(100)
volume(100, 65)
volume(120, 85, 50)
