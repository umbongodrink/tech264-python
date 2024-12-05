
# Variable with a number value
var_number = 10

# Variable with a decimal value
var_decimal = 4.7

# Variable with a string value
var_string = "Sparta Global LMS"

# Q: How is using == different?
# == is used for comparison, = is used for assignment
# == checks if the values of two operands are equal or not
# = assigns the value on the right to the variable on the left


print(var_number)
print(var_decimal)
print(var_string)

print(f"The type of var_number: {type(var_number)}")
print(f"The type of var_decimal: {type(var_decimal)}")
print(f"The type of var_string: {type(var_string)}")


# Q: What does it mean that Python is a strongly typed language?

# In a strongly typed language, the data type of a variable is checked at compile time.
# This means that if a variable is declared as an integer, it cannot be assigned a string value later on.

# It means that each variable has a specific data type, and the type of a variable cannot be changed implicitly.

# While you don't need to explicitly declare the data type of a variable when you define it (like in statically typed
# languages like C++ or Java), Python infers the type at runtime based on the value assigned to it


# Q: Why is strong typing important?
# - Error prevention: It helps catch potential type errors early in the development process.
# - Code readability: It makes code more readable and understandable.
# - Performance optimization: The interpreter can optimize code based on the known types of variable

## STRONGLY VS WEAKLY TYPED LANGUAGE:
# Python needs explicit casting of data types to perform operations on variables of different types.
# Will not do implicit casting of data types.

## DYNAMICALLY VS STATICALLY TYPED LANGUAGE:
# I don't need to define a data type of a variable when I define it.


# Q: What is a dynamically typed language?
# A dynamically typed language is a programming language where the data type of a variable is determined at runtime
# rather than at compile time. This means that you don't need to explicitly declare the data type of a variable when
# you define it, and the type of a variable can change during the execution of the program.
# e.g.

var_x = 10  # x is an integer
var_x = "Hello"  # x is now a string


# Q: what is a statically typed language?
# A statically typed language is a programming language where the data type of a variable is determined at compile time.
# This means that you need to explicitly declare the data type of a variable when you define it, and the type of a
# variable cannot change during the execution of the program.

# e.g. in C++
# int x = 10; // x is an integer
# x = "Hello"; // This would result in a compilation error as x is declared as an integer


x = 10
y = x

print(f"\n")
print(f"The id of x is: {id(x)}")
print(f"The id of y is: {id(y)}")
# x and y are the same because they are pointing to the same memory location.

# if I now change the value of x, y will be different. This is because x and y are pointing to different memory
# locations. This is called shallow copy.

print(f"\n")
x = 20
print(f"x is: {x}, and its id is: {id(x)}")
print(f"y is: {y}, and its id is: {id(y)}")

# an ID is an object, and has an address in memory.


## Q: What is the difference between shallow copy and deep copy?
# A shallow copy creates a new object and inserts references to the original object's elements.
# A deep copy creates a new object and inserts copies of the original object's elements.


# INPUT:
# print(input("Enter your name: "))

# print(name, age, dob = input("Enter your name, age, and date of birth: ").split(", "))
name = input("Enter your name: ")
print(f"Hi {name}!")