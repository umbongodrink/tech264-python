
# DICTIONARY PASSWORD MANAGER

user_to_passwords = {"Max": "happy",
                     "Tom": "sad",
                     "Alex": "morose"}



username = input("Please enter your username: ")
while username not in user_to_passwords.keys():
    username = input("That username is not valid. Please enter a valid username: ")
password = input("Please enter your password: ")
while password != user_to_passwords[username]:
    password = input("That password is not valid. Please re-enter your password: ")



print("Logged in!")
