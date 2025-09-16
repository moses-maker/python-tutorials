fruits = ["orange", "orange", "mango", "banana"]

# append() method
fruits.append("apple")

# display full list
print(fruits)

# total number of items in a list
total_times = fruits.count("orange")
print(total_times)

# insert "lemon" as index 2
fruits.insert(2, "lemon")
print(fruits)

# index() gives you the index position of a value
check = fruits.index("banana")
print(check)

# remove()
fruits.remove("orange")
print(fruits)

# pop() method
see_popped_item = fruits.pop()
print(see_popped_item)

# pop(index)
see_specific = fruits.pop(1)
print(see_specific)

# reverse()
fruits.reverse()
print(fruits)


