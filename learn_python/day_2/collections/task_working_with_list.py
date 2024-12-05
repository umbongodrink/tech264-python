
shopping_list = ["eggs", "bread", "bananas", "biscuits", "milk"]

print(shopping_list)
print(f"The data type of shopping list is: {(type(shopping_list))}")

print(f"The first item on the list is: {shopping_list[0]}")
print(f"The last item on the list is: {shopping_list[-1]}")

shopping_list[1] = "rice"
print(f"The whole shopping list is {shopping_list} and therefore the new second item is {shopping_list[1]}")

shopping_list.append("carrots")
print(len(shopping_list))

shopping_list.extend(["toffee", "coffee"])
# print shopping_list without square brackets
print(*shopping_list, sep=", ")

shopping_list.remove("bananas")
print(shopping_list)

shopping_list.pop()
print(shopping_list)

shopping_list.