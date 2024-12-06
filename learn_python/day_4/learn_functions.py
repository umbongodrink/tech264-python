
# def print_something():
#     print("Something")
# print_something()
#
#
# def print_another_thing(an_argument):
#     print(an_argument)
# print_another_thing("hello")
#
#
# def greet(name):
#     print(f"Hello, my name is {name}")
# greet("Susan")
#
#
# def addition(int1, int2):
#     return int1 + int2
# print(addition(2, 2))
#
#
# def greet(name: str) -> str:
#     return f"Hello {name}"
#
# greet("Mike")

# THIS DOESN'T WORK - WHY?
def division(num1: int=2, num2: int=5) -> float:
    return num1/num2
division(2, 5)


# ===> PYTHON IS NOW STRONGLY STATIC
def division2(n1: int=2, n2: int=2) -> float:
    return n1/n2

a: int = 4
b: int = 6

print(division2(a, b))

