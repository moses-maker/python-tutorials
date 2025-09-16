f = open("file_methods.txt", "w")
total = 100
f.write("good")


# To read a file you have to open in in read mode
f = open("file_methods.txt", "r")    # insta = open()

# 2 is the size or total number of characters
print(f.read(3))

# seek() - placing your cursor at 
#r.seek(5)
#r.seek(0, 1)
#print(r.tell())

# read()
#print(f"The file will be read from position 5 - {r.read()}")









