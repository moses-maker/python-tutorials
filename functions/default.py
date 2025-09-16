"""
default parameter is achieved by initializing a
parameter usually the second parameter with value.
leaving the first one.
> in this case, you can supply one or two arguments
"""

def rectangle(l, w=50):
    area = l * w
    print(area)

rectangle(79) # the second argument i.e 50 will be
# used as default.
rectangle(90, 40)
