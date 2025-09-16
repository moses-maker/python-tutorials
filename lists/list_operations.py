"""
List operations
> In python list can b econcatinated using +
>You can use membership operators on alist 
    a) in
    b) not in
"""
# + to concatinate two lists
list1 = [1, 2, 3, 4]
list2 = [5, 6, 7, 8]
combined_list = list1+list2
print(combined_list)

# * to multiply a list
multi = list1 * 3
print(multi)

# evaluate two lists
print(list1 == list2)

# membership operator on list
print(1 in list1)
print(2 not in list1)

for g in list1:
    if g == 1:
        print("Found")


sentence = "Kenya"
# list() function
string_to_list = list(sentence)
print(string_to_list)



