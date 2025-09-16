class Mobile:
    # class variable
    phone = "Orange"
    # Function inside a class, it is called a method
    def __init__(self):
        print("This message is from Constructor Method")

    def recieve_message():
        # instance variable
        rv = "i am inside a method"
        print("Recieve message using Mobile", rv)

    def send_message(self):
        print("Send message using Mobile")


# create an object/ instantiation
nokia = Mobile()

# method referencing - to access the methods of a class and display the 
# statement
nokia.recieve_message()
nokia.send_message()

# variable referencing
print(nokia.phone)
