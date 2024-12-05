
student1 = {"name": "susan",
            "stream": "tech",
            "completed_lessons": 4,
            "completed_lessons_names": ["variables", "data_types", "set_up"]
            }


# a dictionary is a collection of key-value pairs, keys are unique

print(student1)

print(f"The dictionary 'student1' is of class {type(student1)}")

print(student1["stream"])

print(type(student1["completed_lessons_names"]))

print(student1["completed_lessons_names"][0])

student1["completed_lessons"] = 3
print(student1)

student1["completed_lessons_names"].remove("data_types")
print(student1)

# print a list of student1's keys without it saying "dict_keys"
print(list(student1.keys()))