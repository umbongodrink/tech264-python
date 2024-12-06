import sys

# check for arguments
# print(sys.argv)
if len(sys.argv) > 1:
    print("You gave me an argument!")
else:
    print("You gave me no argument.")

print(sys.argv[1])