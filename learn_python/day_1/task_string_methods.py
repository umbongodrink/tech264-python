
str_with_extra_spaces = " extra spaces at the start and end "
print(len(str_with_extra_spaces))
print(str_with_extra_spaces.strip())

str_with_beg_end_spaces = " Hello World! "
print(len(str_with_beg_end_spaces))
new_str = str_with_beg_end_spaces.strip()
print(len(new_str))


example_text = "here's some text with some words of text"
print(example_text.count("text"))

print(example_text.upper())
print(example_text.lower())

print(example_text.capitalize())

print(example_text.replace(" with", ","))

test_var = "I'm feeling sad"
print(f"\n{test_var.replace("sad", "happy")}")