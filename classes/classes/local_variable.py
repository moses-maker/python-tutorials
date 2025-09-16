class Volume:
    def __init__(self, l, w):
        self.length = l
        self.width = w
    def vol(self, height):
        volume = self.length * self.width * height
        print(volume)

v = Volume(67, 43)
v.vol(86)
