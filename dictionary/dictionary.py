# syntax for dictionary with strings only
fish = {"g":"goldfish", "n":"nileperch"}
# display
print(fish)

#use the keys for accessing the value 
t = fish["n"]
print(t)

print(fish["g"])

# mixed dictionary
mixed = {"portable":"laptop", 9:11, 10:"messi"}

# both keys and values can be string or numbers or combined.
print(mixed[9])
print(mixed[10])

# modify value using the key
mixed[9] = "Morata"
print(mixed)

# empty dictionary
dictionary_name = {}


cities = {"counties":{47:"Uasin Gishu", 1:"Mombasa"}, "countries":"kenya"}
print(cities)

print(cities["counties"][47])


