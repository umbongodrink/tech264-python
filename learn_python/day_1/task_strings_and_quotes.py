
# bad_string = 'I said Wow!''
# print(bad_string)

## This fails because the string literal is not properly closed.


good_string_1 = "I said Wow!"

good_string_2 = 'I said "Wow!"'
good_string_3 = "I said 'Wow!'"
good_string_4 = "I said \"Wow!\""

#rasheed_method = f"I said "Wow!""

arbitrary_var = '"'
jacks_string = f"I said {arbitrary_var}Wow!{arbitrary_var}"
print(f"Jack's string is: {jacks_string}")

# does this work?
print(f"Kip said: {good_string_4}")


print(good_string_4)


# Q: What is the difference between single quotes and double quotes in Python?
