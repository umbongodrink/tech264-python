## Tasks 1 & 2

def print_something(name):
    print(f"Hello {name}")

# Task 3
def greet(name: str):
    print("Hello, my name is", name )

# Task 4
def addition(int1, int2):
    return int1 + int2

# Task 5
def default_addition(int1 = 2, int2 = 2):
    return int1 + int2

# Task 6
def print_every_number(num_tuple):
    print(type(num_tuple))
    for n in num_tuple:
        print(n)

# Task 7


if __name__ == '__main__':
    # Tasks 1 & 2
    # my_name = input("What is your name? ")
    # print_something(my_name)

    # Task 3
    # greet("Susan")

    # Task 4
    # print(addition(2, 2))

    # Task 5
    # print(default_addition(4, 4))
    # The answer is 8, because the arguments are default and optional

    # Task 6
    # print_every_number((1, 2, 2, 3, 3, , 4, 5, 5))

    # Task 7
    greet(24601)