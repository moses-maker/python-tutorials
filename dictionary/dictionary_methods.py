box_office = {"avatar":2009, "titanic":1997, "starwars":2015, "avengers":2012 }
# get() - 
print(box_office.get("avatar"))
# keys()
keys_only = box_office.keys()
print(keys_only)
# values()
values_only = box_office.values()
print(values_only)
# items()
key_value_pairs = box_office.items()
for key, value in key_value_pairs:
    print(f"The movies {key} was produced in {value} ")
print(key_value_pairs)
# update or adds a key:value pairs in a dictionary, at the end
box_office.update({"frozen":2013})
print(box_office)
# convert keys of dictionary to list with list() function
get_keys = box_office.keys()
con = list(get_keys)
print(con)
# remove the last item from dictionary
box_office.pop("avatar")
print(box_office)
# removes item(key:value) pair.
take = box_office.popitem()
print(take)
# removes everything 
box_office.clear()
print(box_office)
# populate an empty dictionary
# list append()
# dictionary update()
countries = {}
countries.update({"Asia":"India"})
countries.update({"Europe":"Germany"})
countries.update({"Africa":"Sudan"})
print(countries)

for key in countries.keys():
    print(key)

for value in countries.values():
    print(value)

for key, value in countries.items():
    print(f"{value} is found in a continent called {key}")

