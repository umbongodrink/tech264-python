
# example of a frozen set called "fs"
fs = frozenset([1, 2, 3, 4, 5])
print(fs)

frozen_set = frozenset(["hello", "world"])
# frozen_set.add("!")  # AttributeError: 'frozenset' object has no attribute 'add'

normal_set = {"let's", "learn"}
print(normal_set)

normal_set.add(frozen_set)
print(normal_set)
# if you run the script a few times, you will see that the order of the elements in the set "normal set" will change.
# This is because the order of the elements in a set is not guaranteed to be the same as the order in which they were
# added.


# What makes a frozen set different from a normal set?
# A frozen set is immutable, meaning that once it is created, you cannot change its contents.
# This means that you cannot add, remove, or change elements in a frozen set.
# A normal set, on the other hand, is mutable, meaning that you can add, remove, or change elements in a normal set.
# This makes frozen sets useful in situations where you want to ensure that the contents of a set do not change.


