
# tuples are non-mutable whereas lists are (changeable)

# immutability means you cannot change something

# Other immutable data types:
mutable_data_types = ["int", "float", "string", "tuples", "frozen sets", "boolean", "bytes"]

# good use for tuple = any time you want a list that you can't change.
## 1. returning multiple values from a function
## 2. storing heterogenous data
## 3. using tuples as dictionary keys
## 4. ensuring data integrity
## 5. tuple unpacking


essentials = ("bread", "eggs", "milk")
print(essentials)
print(essentials.count("bread"))

essential_item1 = input("What is an essential item you would take? ")
essential_item2 = input("What is an essential item you would take? ")
essential_item3 = input("What is an essential item you would take? ")

essentials_tuple = (essential_item1, essential_item2, essential_item3)

print("Here are your items as a tuple: ", essentials_tuple)
print("")
print("I lied. You can take one more item.")
essential_item4 = input("What is an essential item you would take? ")

# add another item to the tuple
essentials_tuple = essentials_tuple + (essential_item4,)
print("Here are your items as a tuple (with the 4th item added): ", essentials_tuple)


