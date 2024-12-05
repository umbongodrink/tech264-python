
list_data = [1, 2, 3, 4, 5]

embedded_lists = [[1,2,3], [4,5,6]]

dict_data = {1: {"name": "Bronson", "money": "$0.05"},
             2: {"name": "Masha", "money": "$3.66"},
             3: {"name": "Roscoe", "money": "$1.14"}}

# 1. Loop through a list
print("Question 1:")
print("Using List Comprehension")
print([num * 2 for num in list_data])
# OR
print("\nOR")
for num in list_data:
    print(num * 2)

print("\nQuestion 2:")
# 2. Loop through the "embedded_lists" list
for data in embedded_lists:
    print(data)

print("\nQuestion 3:")
# 3. Loop through the lists embedded inside a list
for data in embedded_lists:
    print(data)
    for number in data:
        print(number)

print("\nQuestion 4:")
# 4. Loop through a dictionary
for key in dict_data.keys():
    print(key)

print("\nQuestion 5:")
# 5. Loop through a dictionary and print its values
for value in dict_data.values():
    print(value)

print("\nQuestion 6:")
# 6. Loop to print the values of the dictionary items inside a dictionary
for value in dict_data.values():
    for individual_value in value.values():
        print(individual_value)

print("\nQuestion 7:")
# 7. Loop to print specific values of the dictionary items inside a dictionary
for value in dict_data.values():
    for k, v in value.items():
        if k == "money":
            print(v)


print("\nQuestion 8:")
# 8. Loop through a list with a nested statement
for number in list_data:
    if number < 3:
        print("less than 3")
    elif number == 3:
        print("I found thee")
    else:
        print("greater than 3")


