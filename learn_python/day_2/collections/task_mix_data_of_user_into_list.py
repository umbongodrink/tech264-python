
name = "kip"
age = "42"
dob = "11/09/1978"

user_details_list = [name, age, dob]
print(user_details_list)

if type(age) == int:
    print(f"The data type of age is: {(type(age))}")
else:
    print("The data type of age is not an integer")
    age = int(age)
    print(f"The data type of age is now: {(type(age))}, and is value: {age}")

height = float(input("Enter your height: "))
user_details_list.append(height)
print(user_details_list[-1])

