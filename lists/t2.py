# variable stores one value
total = 100

#List variable
"""
parts of a list
a) valid identifier
b) assignment operator ( =  messenger)
c) []
d) items


"""
# list is created with [], valid
total = [300, 400, 700, 750]


# empty list creation
crate = []
print(crate)

# list of strings
crate = ["egg one", "egg2", "egg3", "egg4", "egg5", "egg6"]
print(crate)

#list of numbers e.g. integers and floats.
numbers = [45, 21, 78.7, 90.43, 32, 21.6]
print(numbers)

# list of strings, numbers, list and boolean values
mixture = [67, "kenya", 10.5, [4, 5, 6], True, "Good", False]
print(mixture)

# Using index to retrieve an item from list
# items in a list are assigned number starting from - 0 - N
# Items can be reversed indexed -1, -2, -3, -4
eggs_crate = ["e1", "e2", "e3", "e4", "e5", "e6", "e7", "e8", "e9", "e10", "e11", "e12", "e13", "e14"]



# option 2 to display
"""
y = eggs_crate[4]
print(y)

d = eggs_crate[-4]
print(d)
"""
print(eggs_crate[2])

# reverse indexing -1, -2, 
print(eggs_crate[-1])

# replacing broken egg
"""
eggs_crate[-5] = "e1000"
print(eggs_crate)

"""
eggs_crate[4] = "e5"
print(eggs_crate)

# slicing
# list_name[start_index: stop_index: step_value]
"""
To extract multiple values we use indexes 
variable = list_variable[start_index:stop_index:step_index]
-> stop_index is usually disregarded.
h = list_variable[3:10]


"""
chunk = eggs_crate[0:11:2]
print(chunk)

# slicing with start_index only
start_index = eggs_crate[3:]
print(start_index)

# slicing with stop _index only
stop_index = eggs_crate[:10]
print(stop_index)

# slicing with step value, this evaulate the entire list
step_value = eggs_crate[::2]
print(step_value)

# To print list in reverse using negative step
reverse_list_display = eggs_crate[::-1]
print(reverse_list_display)

eggs_crate2 = ["e1", "e2", "e3", "e4", "e5", "e6", "e7", "e8", "e9", "e10", "e11", "e12", "e13", "e14"]

# Negative slicing
right_side_slicing = eggs_crate2[-3:-1]
print(right_side_slicing)

# copy an entire list to new list using full colon
copy_of_entire_list = eggs_crate2[:]
print(copy_of_entire_list)














