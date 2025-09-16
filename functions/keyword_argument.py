# keyword argument
def fruits(variety, color='yellow', quantity=10, price=10.00):
    print(variety, color, quantity, price)
    print(variety, color)
    print(variety, quantity, price)
    print(color, quantity, price)


# calling
fruits("banana")
fruits("apple", quantity=200, price=50.95)