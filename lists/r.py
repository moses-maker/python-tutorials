slicing = [34, 56, 32, 78, 54, 90, 43, 90, 71]
# retrieve individual item
print(slicing[3])
# slicing , allows to retrieve more than 1 item
# start index: stop index, step index

# start and stop, stop index is never considered i.e 4
items = slicing[0:4]
print(items)

# start, stop, step
item2 = slicing[0:9:2]
print(item2)