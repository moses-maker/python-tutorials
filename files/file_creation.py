def file_creation():
    # to create a new file we use the "x" mode open()
    file_handler = open("example.txt", "x")
def writing_file():
    while True:
        # write data to a file
        user_name = input("Enter your name?")
        adm = input("Enter admission number?")
        phone = input("Enter phone number?")
        write_data = open("students_registration.txt", "a+")
        write_data.write(user_name + "\n" + adm + "\n" + phone + "\n")
        if user_name or adm or phone == "exit":
            break
def reading_file():
    # we use the read() method to read a file.
    read_file = open("students_registration.txt", "r")
    # reads text in a line in form of a list
    reading = read_file.readlines()
    for line in reading:
        print(line)
def search():
    enter_name = input("Enter name to search?")
    # we use the read() method to read a file.
    read_file = open("students_registration.txt", "r")
    # reads text in a line in form of a list
    reading = read_file.readlines()
    for line in reading:
        if line==enter_name:
            print("Found", line)
print("welcome to registration application \nPlease choose your option")
print("1. Registration\n 2. Read your data \n 3. search")
choice = int(input("Enter your choice here?"))
if choice==1:
    writing_file()
elif choice==2:
    reading_file()
elif choice==3:
    search()















