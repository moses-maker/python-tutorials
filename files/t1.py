# open() function
"""
file_variable = open("filename.txt", "mode")

open() - function to create a file
filename - where the contents will be written.
mode - determine how a file is opened.
"""

#  Creating a file
file_variable = open('C:\\Users\\MicroAple\\Desktop\\python\\files\\intro.txt', "a+")

# writing to a file using write() method.
file_variable.write("Hello"+"\n")
file_variable.write("kenya"+"\n")
file_variable.write("ethiopia"+"\n")

# close the file
file_variable.close()
my_list = []
# open the file for reading.
read_file = open("C:\\Users\\MicroAple\\Desktop\\python\\files\\intro.txt", "r") 
reading = read_file.readlines()

for x in reading:
    print(x)
    my_list.append(x)

print(my_list)





