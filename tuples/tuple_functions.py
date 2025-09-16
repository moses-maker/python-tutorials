"""
TUPLE FUNCTIONS
> len() - counts number of items in a tuple
> sum() - adds all items in a tuple
> sorted() - arranges according to alphabetical order

TUPLE METHODS
> count() - counts how many times an item appears in a tuple
> index() - display the index position of an item 
"""
years = (1996, 1985, 1981, 1987, 2005, 2005)
#len()
counter = len(years)
print("The tuple has following items ", counter)
# sum()
add_all_years = sum(years)
print(add_all_years)

# sort values
rearrange = sorted(years)
print(rearrange)

#METHODS USED IN TUPLE
# count()
print(years.count(2005))

# index()
print(years.index(1987))

#TUPLE PACKING AND UNPACKING
t = (123, 456, 789)

#tuple unpacking
x, y, z = t
print(x, y, z)

#tuple packing
t = x, y, z
print(t)

# add items to an empty tuple
my_tuple = () 
for f in range(1, 20):
    my_tuple += f,
#display my tuple
print(my_tuple)






