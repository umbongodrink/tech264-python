
# lists: mutable, ordered, allows duplicate elements
# tuples: immutable, syntax (var,)


# sets: unordered, unindexed, no duplicate elements
# example of a set:
fruits = {"apple", "banana", "cherry"}

fruits.add("orange")
print(fruits)

fruits.remove("banana")
fruits.discard("banana")
print(fruits)

fruits.add("apple")
print(fruits)
# sets contain unique elements, therefore you can't add an item twice

# you can't do this ===> print(fruits[1])
# because sets are unindexed or unordered






