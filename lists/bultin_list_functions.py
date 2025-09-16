years = [2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010]
"""
len() - count number of items in a list
sum() - adds all the items in a list
sorted() - rearrange the list
max() - gets you the largest number in a list
min() - smallest number in a list
"""
print(f"Total items in a list is {len(years)}")

marks = [45, 72, 94, 52]
print(f"The total marks is {sum(marks)}")
print(sorted(marks))
print(max(marks))
print(min(marks))




print(total_years)

sum_of_values = sum(years)
print(sum_of_values)


list_2 = years[::-1]
my = sorted(list_2)
print(my)


maximum_value = max(years)
print(maximum_value)


Minimum_value = min(years)
print(Minimum_value)



test = [56, 89, 34, 21, 89, ["kenya", "uganda", "tanzania"], 100, 300, 150]
# retrieving
r = test[5][1]
print(r)

# add a new list
test[6] = [5000, 4500, 9000, 2000]

# shortcut
h = sum(test[6][1:3], test[6][3])

# short shortcut
k = sum(test[6][1:4])
print(h, k)
# test[][][][]
# replace
test[5][2] = "ethiopia"
print(test[5])

print(test)


k = [
    [7, 6, 2, 1],
    [9, 3, 2, 6],
    [8, 5, 3, 9],
    [2, 8, 3, 9]
]

# first row.
r1v1 = k[0][0]
r1v2 = k[0][1]






g = [
    [8, 4, 3, 3],
    [9, 2, 8, 4],
    [8, 5, 3, 2],
    [9, 3, 2, 8]
]


# multiply the the matrix kg
