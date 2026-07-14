# This is my first Python program
import math

# Strings
first_name = "Bryce"
fav_food = "pizza"
email = "bryce.rich82@gmail.com"

# Integers
age = 19
quantity = 5
num_of_students = 30

# Floats
price = 9.99
gpa = 2.73
distance = 5.5

# Booleans
is_student = True
is_wealthy = False


# Type Casting = The conversion of one data type to another
#               int() = converts a data type to an integer
#               float() = converts a data type to a float
#               str() = converts a data type to a string
#              bool() = converts a data type to a boolean
# name = "Bryce Richardson"
# age = 19
# gpa = 2.73
# is_student = True


# input() = a function that promts the user to input data
#         The input() function always returns data as a string
# user_name = input("What is your username?: ")
# user_age = int(input("How old are you?: "))
# user_age += 1


# Exercise 1 = Calculate Area of Rectangle
# length = float(input("What is the length of the rectangle in meters?: "))
# width = float(input("What is the width of the rectangle in meters?: "))
# area = length * width
# print(f"The area of the rectangle is: {area}m²")


# Exercise 2 = Shopping cart program
# item = input("What are you purchasing with us today?: ")
# price = float(input(f"What is the price of {item}?: "))
# quantity = float(input(f"How many {item}s would you like to buy?: "))
# total = price * quantity
# print(f"You are buying {quantity} {item}(s) for a total of ${total}")


# Mad Libs Game
# print("Welcome to Bryce's MADLIBS Game!")
# adj1 = input("Enter an adjective (description): ")
# noun1 = input("Enter a noun (person, place, or thing): ")
# adj2 = input("Enter a second adjective (description): ")
# verb1 = input("Enter a verb ending in 'ing' (an action): ")
# adj3 = input("Enter the last adjective (description): ")
# print(f"Today I went to a(n) {adj1} zoo.")
# print(f"In an exhibit, I saw a(n) {noun1}.")
# print(f"{noun1.title()} was {adj2} and {verb1}!")
# print(f"I was {adj3}!")


# Arithmetic & Math
friends = 5
friends += 1  # adding to a variable
friends -= 2  # subtracting from a variable
friends *= 3  # multiplying a variable
friends /= 4  # dividing a variable (use // for int and not floats)
friends **= 2  # exponentiating a variable
remainder = friends % 2
# print(friends)
# print(remainder)

x = 3.14
y = 4
z = 5
# result = round(x)
# result = abs(y)
# result = pow(y, 2)
# result = max(x, y, z)
# result = min(x, y, z)
# print(result)

num = 7.8
# print(math.pi)
# print(math.e)
# result = math.sqrt(num)
# result = math.ceil(num)
# result = math.floor(num)
# print(result)

# Math Exercise 1 = Calculate circumference of a circle
# radius = float(input("What is the radius of the circle in cm?: "))
# circumference = 2 * math.pi * radius
# print(f"The circumference of the circle is {round(circumference, 2)}cm(s)")

# Math Exercise 2 = Calculate the area of a circle
# r = float(input("What is the radius of the circle in cm?: "))
# area = math.pi * pow(r, 2)
# print(f"The area of the circle is {round(area, 2)}cm²")

# Math Exercise 3 = Calculate the hypotenuse of a triangle
a = float(input("What is the base of the triangle in meters?: "))
b = float(input("What is the height of the triangle in meters?: "))
c = math.sqrt(pow(a, 2) + pow(b, 2))
print(f"The length of the hypotenuse is {round(c, 2)}m")
