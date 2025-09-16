# A tuple can hold mixed values(string/numbers)
countries = ("kenya", 7890, "rwanda", 19.80)
print(countries)
#create a tuple by assigning several values
#on a variable separated by comma
f1 = "ferrari", "redbull", "mercedes", "renault"
y = 344, 567, 908, 554, 343, 567, 547, 786, 444
print(f1)
print(y)

# empty tuple
empty_tuple = ()

# You can have variable representing a tuple inside
#  another tuple
air_force = ("f15", "f22a", "f35a")
fighter_jets = (1988, 2005, 2016, air_force)
print(fighter_jets)

#A comma should be added at the end of  a tuple with 
#one item
singleton = ("hello",)
print(type(singleton))

# when adding one item to an empty tuple put a comma 
#at the end.
list_2 = ["kenya"]
print(singleton)

# operations
tuple_one = (2, 0, 1, 4)
tuple_two = (2, 0, 1, 4)

# add tuples together
joined_tuple = tuple_one + tuple_two
print(joined_tuple)

# multiply a tuple
multiply = tuple_one * 2
print(multiply)

# relational/comparison operators(<, >, <=, >=, !=, ==)
print(tuple_one == tuple_two)

# membership operators( in , not in) can be used on tuples
tuple_items = (1, 9, 8, 8, 10)
print(10 in tuple_items)

# you can use tuple() function to create a tuple.
norse = "vikings"
strings_to_tuples = tuple(norse)
print(strings_to_tuples)

# You can convert a list to a tuple using tuple() function
zeus = ["g", "o", "d", "o", "f", "s", "k", "y"]
list_to_tuple = tuple(zeus)
print(list_to_tuple)

# nested tuple
letters = ("a", "b", "c")
numbers = (1, 2, 3)
nested_tuples = (letters, numbers)
print(nested_tuples)




