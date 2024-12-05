

user_prompt = True

while user_prompt:
    age = input("What is your age? ")
    if age.isdigit() and 0 < int(age) <= 117:
        user_prompt = False
    else:
        age = input("Please enter your age as a digit: ")
        #print(f"age is {age} and type {type(age)}")
        if age.isdigit() and 0 < int(age) <= 117:
            user_prompt = False



print(f"Your age is {age}")


