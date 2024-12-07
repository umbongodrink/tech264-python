import sys
import os

full_name_of_script_and_path = sys.argv[0]
full_path, name_of_file = os.path.split(full_name_of_script_and_path)

print(f"The name of the file is: {name_of_file}")

if len(sys.argv) > 1:
    arguments = sys
    print("You gave me an argument!")
else:
    print("You gave me no argument.")
    print(f"Number of arguments passed: {len(arguments)}")
    print(f"The other arguments are: {arguments}")

## loop through the argument list and print each argument to the screen
if len(sys.argv) > 1:
    arguments = sys.argv[1:]
    for arg in arguments:
        print(arg)

## If there are no elements passed to the script, display an error about this
if len(sys.argv) == 1:
    print("Error: no arguments passed.")
