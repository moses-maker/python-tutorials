with open("filename.txt", "a+") as file_handler:
    file_handler.write("hello world")
    file_handler.close()

with open("C:\\Users\\moses\\Desktop\\pro\\python\\files\\filename.txt", "r") as file:
    print(file.read())


