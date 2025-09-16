"""
INDEXING
>Each item in a tuple can be retrieved using index value, 
placed inside square brackets.
>Index usually begins at 0-N

The syntax to retrieve individual item is.

tuple_name[index]
"""

months = ("jan", "feb", "mar", "apr", "may", "jun")

# To retrieve apr
retrieved = months[3]
print(retrieved)

# reverse indexing(-1, -2, -3, -N)
reverse_retrieval = months[-2]
print(reverse_retrieval)

"""
SLICING
This is extracting a chunk of the tuple items.
In slicing, 0:3, the last index is usually ignored i.e. 3
> The syntax: tuple_name[start:stop:step]
"""
colors = ("v", "i", "b", "g", "y", "o", "r")

# start and stop index value
extraction = colors[0:3]
print(extraction)

# start value only
start_value = colors[3:]
print(start_value)

# stop value only
stop_value = colors[:2]
print(stop_value)

# start, stop and step values
start_stop_step = colors[0:5:2]
print(start_stop_step)

#step only
step = colors[::2]
print(step)

# display in reverse
reverse_order = colors[::-1]
print(reverse_order)

# Use the negative indexes
extra = colors[-5:-1]
ec = colors[-6:-3]
print(extra)









