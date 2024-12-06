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