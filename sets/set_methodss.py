"""
SET METHODS
"""
# set_name.add() insert a new item to the set at the end
countries = {"kenya", "uganda", "tanzania", "ethiopia"}
countries.add("sudan")
print(countries)

# set_name.difference(other_set)
# The difference() method returns a new set with items in the set set_name
# that are not in the others sets.
c1 = {"kenya", "uganda", "tanzania", "ethiopia"}
c2 = {"fiji", "argentina", "uganda", "tanzania"}
differences = c1.difference(c2)
print(differences)

#set_name.intersection(others)- The intersection() method returns a new 
# set with items common to the set set_name and all others sets.
c3 = {"kenya", "uganda", "tanzania", "ethiopia"}
c4 = c2 = {"fiji", "agentina", "uganda", "tanzania"}
common_in_both = c3.intersection(c4)
print("Common characters in both", common_in_both)


# set_name.discard() - The discard() method removes an item from the set
# set_name if it is present.
c5 = {"kenya", "uganda", "tanzania", "ethiopia"}
c5.discard("uganda")
print(c5)

# set_name.clear() - The clear() method removes all the items from the set 
# set_name.
c6 = {"kenya", "uganda", "tanzania", "ethiopia"}
c6.clear()
print(c6)


# The isdisjoint() method returns True if the set set_name has no items in
#  common with other set. Sets are disjoint if and only if their 
# intersection is the empty set.
c7 = {"kenya", "uganda", "tanzania", "ethiopia"}
c8  = {"fiji", "agentina"}
unique_item = c7.isdisjoint(c8)
print(unique_item)

# The issubset() method returns True if every item in the set
# set_name is in other set.
c9 = {"kenya", "uganda", "tanzania", "ethiopia"}
c10 = c2 = {"fiji", "agentina"}
those_not_in_set_1 = c9.issubset(c10)
print(those_not_in_set_1)

# The issuperset() method returns True if every element in
# other set is in the set set_name.
c11 = {"kenya", "uganda", "tanzania", "ethiopia"}
c12 = c2 = {"tanzania", "ethiopia"}
confirm = c11.issuperset(c12)
print(confirm)

# The method pop() removes and returns an arbitrary item
# from the set set_name. It raises KeyError if the set is empty.
c11 = {"kenya", "uganda", "tanzania", "ethiopia"}
my = c11.pop()
print(my)

# The method remove() removes an item from the set
# set_name. It raises KeyError if the item is not contained
# in the set.
c12 = {"kenya", "uganda", "tanzania", "ethiopia"}
c12.remove("uganda")
print(c12)

# The method union() returns a new set with items from
# the set set_name and all others sets.
c13 = {"kenya", "uganda", "tanzania", "ethiopia"}
c14  = {"fiji", "agentina"}
my_union = c13.union(c14)
print(my_union)

# The method symmetric_difference() returns a new set with
# items in either the set or other but not both
c15 = {"kenya", "uganda", "tanzania", "ethiopia"}
c16  = {"fiji", "agentina", "tanzania"}
unique_in_both = c15.symmetric_difference(c16)
print(unique_in_both)

# Update the set set_name by adding items from all others sets.
c17 = {"fiji", "agentina", "tanzania"}
c18 = {"kenya", "uganda", "tanzania", "ethiopia"}
c17.update(c18)
print(c17)


"""
Exercise: 
a) Find unique characters between these words ( "egg", "immune")
b) Find unique charcters that are both in these words ("feed", "vacuum")
c) Remove the last item from the set that you will create on this string ("goddesship")

"""