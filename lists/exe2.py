#1. Create a list to use as your shopping list with 3 items:
#"Milk," "Bread," and "Apples."
shopping_list = ["Milk", "Bread", "Apples"]
#2. Check your list length and print.
print(len(shopping_list))
#3. Update "Bread" with "Bananas" and "Eggs".
shopping_list[1] = "Bananas"
shopping_list.append("Eggs")
print(shopping_list)
#4. Remove the last item from the array and output it into the console
last_item = shopping_list.pop()
print(last_item)
#5. Sort the list alphabetically
print(shopping_list.sort())
#6. Find and output the index value of Milk.
print(shopping_list.index("Milk"))
#7.  After Bananas, add Carrots and Lettuce.
print(shopping_list)
shopping_list.insert(2, "Carrots")
shopping_list.insert(2, "Lettuce")
print(shopping_list)
#8. Create a new list containing Juice and Pop.
drinks = []
drinks.append("Juice")
drinks.append("Pop")

#9. Combine both lists, adding the new list twice to the end of the first list.
Combined = shopping_list + drinks + drinks
print(Combined)
print(Combined.index("Pop"))
#10. Get the last index value of Pop and output it to the console.
Occur = Combined.count("Pop")
everything = len(Combined) - 1
print(everything)
#11. Your final list should look like this
print(Combined)