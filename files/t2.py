registration = open("C:\\Users\\MicroAple\\Desktop\\python\\files\\register.txt", "a")
while True:
    
    names = input("Enter your name for registration?")
    registration.write(names+"\n")
    registration.close()


