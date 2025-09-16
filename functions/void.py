# Function definition
def hello():
    l = 78
    w = 50
    area = l * w
    print(area)

# Function calling
hello()


def rectangle(l, w):
    area = l * w
    print(area)

rectangle(78, 60)



def circle(r):
    area = 3.14159 * r * r 
    print(area)

def main():
    circle(7) # function call

if __name__ == "__main__":
    main()