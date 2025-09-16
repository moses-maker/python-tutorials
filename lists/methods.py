"""
LIST METHODS

a) append(item) 
 listname.append(item)
- adds a single item at the end of a list

b) count()
listname.count(item)
 - counts the number of times the item has occurred in a
 list

c) insert() 
listname.insert(index, item)
- it adds an item at the given index, shifting items to the right.

d) extend()
list.extends(list2)

e) index()
listname.index(item)
- searches for the given item from the start and return its index.

f) remove()
listaname.remove(item)
- remove the item supplied

g) pop()
 listname.pop()
 -It removes the last item of the list
 removed_item = listname.pop(index) removes the value in that index

h) reverse()
listname.reverse()
-It reverses the item in a list.
"""


# append()
countries = [] #empty list
countries.append("Kenya")
countries.append("Uganda")
print(countries)

# count()
letters = ["A", "A", "A", "B", "C", "D"]
print(f" Letter A appears {letters.count("A")} time, in this list {letters}.)

#insert()
fruits = []  # use append method to add fruits to fruits list
fruits.insert(3, "grapes")
print(fruits)

#index()
h = ["a", "b", "c"]  # index - 0+1, 1+1, 2+1
position = fruits.index("mangoes")
print(position+1)

# remove()
fruits.remove("lemon")
print(fruits)

# reverse()
fruits.reverse()
print(fruits)

# pop()- removes the last item by default, 
take = fruits.pop()
print(take)

# pop(item_index) -  removes specific item in bracket.
specific = fruits.pop(1)
print(specific)
"""
Practices Exercise 1
a) Create an empty list called  "fruits_list"
b) add three fruits, [mangoes, banana, apples]
c) remove item called banana in its index replace "pinesapples"
d) reverse the list in that the last item is the first.

Practice exercise 2
1. Create a list to use as your shopping list with 3 items:
 "Milk," "Bread," and "Apples."
 shopping_list = ["Milk", "Bread", "Apples"]
2. Check your list length and print.
print(len(shopping_list))
3. Update "Bread" with "Bananas" and "Eggs".
shopping_list.insert(1, "Banana", "Eggs")
4. Remove the last item from the array and output it into the console
5. Sort the list alphabetically
6. Find and output the index value of Milk.
7.  After Bananas, add Carrots and Lettuce.
8. Create a new list containing Juice and Pop.
9. Combine both lists, adding the new list twice to the end of the first list.
10. Get the last index value of Pop and output it to the console.
11. Your final list should look like this

["Bananas", "Carrots", "Lettuce", "Eggs", "Milk", "Juice", 
"Pop", "Juice", "Pop"]

Practice exercise 3
1. Create an array containing three values: 1, 2, and 3.
2. Nest the original list into a new list three times.
3. Output the value 2 from one of the arrays into the console


"""


