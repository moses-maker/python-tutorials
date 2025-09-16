eggs_crate = ["e1", "e2", "e3", "e4", "e5", "e6", "e7", "e8", "e9", "e10", "e11", "e12", "e13", "e14"]

# extraction
y = eggs_crate[1:7]
print(y)

g = eggs_crate[-5:-1]
print(g)

# step_index
j = eggs_crate[1:10:2]
print(j)

# start_index only
k = eggs_crate[2:]
print(k)

# stop_index only
p = eggs_crate[:10]
print(p)

# step_index only
w = eggs_crate[::3]
print(w)

# copy the entire list
s = eggs_crate[:]
print(s)

# display list in reverse
m = eggs_crate[::-1]
print(m)