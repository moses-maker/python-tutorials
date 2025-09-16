
# creating file using open() function
file_creation = open("moses.txt", "a+")

# write() method is used to write content to a file
file_creation.write("\nUasin Gishu")

# close() method
file_creation.close()

file = open("C:\\Users\\moses\\Desktop\\pro\\python\\files\\moses.txt", "r")
print(file.read())
