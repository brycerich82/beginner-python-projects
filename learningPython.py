# This is my first Python program

# Strings
# first_name = "Bryce"
# fav_food = "pizza"
# email = "bryce.rich82@gmail.com"

# Integers
# age = 19
# quantity = 5
# num_of_students = 30

# Floats
# price = 9.99
# gpa = 2.73
# distance = 5.5

# Booleans
# is_student = True
# is_wealthy = False


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
# friends = 5
# friends += 1  # adding to a variable
# friends -= 2  # subtracting from a variable
# friends *= 3  # multiplying a variable
# friends /= 4  # dividing a variable (use // for int and not floats)
# friends **= 2  # exponentiating a variable
# remainder = friends % 2
# print(friends)
# print(remainder)

# x = 3.14
# y = 4
# z = 5
# result = round(x)
# result = abs(y)
# result = pow(y, 2)
# result = max(x, y, z)
# result = min(x, y, z)
# print(result)

# num = 7.8
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
# a = float(input("What is the base of the triangle in meters?: "))
# b = float(input("What is the height of the triangle in meters?: "))
# c = math.sqrt(pow(a, 2) + pow(b, 2))
# print(f"The length of the hypotenuse is {round(c, 2)}m")


# if statement = Do some code only IF some condition is True
#       Else do somthing else
# age = int(input("Enter your age: "))

# if age > 99:
#     print("You are too old to sign up.")
# elif age >= 18:
#     print("You are now signed up!")
# elif age < 0:
#     print("You haven't been born yet...")
# else:
#     print("You must be 18+ to sign up.")

# response = input("Would you like food> (Y/N): ")
# if response == "Y":
#     print("Have some food!")
# else:
#     print("No food for you!")

# name = input("Enter your name: ")
# if name == "":
#     print("You did not type in your name!")
# else:
#     print(f"Hello, {name}!")

# for_sale = True
# if for_sale:
#     print("This item is for sale!")
# else:
#     print("This item is not for sale.")

# online = False
# if online:
#     print("The user is online.")
# else:
#     print("The user is offline.")


# Python Calculator
# operator = input("Enter and operator (+ - * /): ")
# num1 = float(input("Enter the first number: "))
# num2 = float(input("Enter the second number: "))

# if operator == "+":
#     result = num1 + num2
#     print(result)
# elif operator == "-":
#     result = num1 - num2
#     print(result)
# elif operator == "*":
#     result = num1 * num2
#     print(result)
# elif operator == "/":
#     result = num1 / num2
#     print(result)
# else:
#     print(f"{operator} is not a valid operator.")


# Python weight converter

# weight = float(input("Enter your weight: "))
# unit = input("Kilograms or pounds? (kg or lbs): ")

# if unit == "kg":
#     weight *= 2.205
#     print(f"Your weight is: {round(weight, 2)}lb(s)")
# elif unit == "lbs":
#     weight /= 2.205
#     print(f"Your weight is: {round(weight, 2)}kg")
# else:
#     print(f"{unit} is not a valid unit of measurement.")


# # Temperature Conversion Program

# temp = float(input("Enter the temperature: "))
# unit1 = input("Is this temperature in Fahrenheit, Celsius, or Kelvin? (F/C/K): ")
# unit2 = input("What unit would you like to convert to?: ")

# if unit1 == "F" and unit2 == "C":
#     temp = (temp - 32) * (5 / 9)
#     print(f"The temperature in Celsius is: {round(temp, 1)}°C.")
# elif unit1 == "F" and unit2 == "K":
#     temp = (temp - 32) * (5 / 9) + 273.15
#     print(f"The temperature in Kelvin is: {round(temp, 1)}°K.")
# elif unit1 == "C" and unit2 == "F":
#     temp = (temp * (9 / 5)) + 32
#     print(f"The temperature in Fahrenheit is: {round(temp, 1)}°F.")
# elif unit1 == "C" and unit2 == "K":
#     temp += 273.15
#     print(f"The temperature in Kelvin is: {round(temp, 1)}°K.")
# elif unit1 == "K" and unit2 == "F":
#     temp = (temp - 273.15) * (9 / 5) + 32
#     print(f"The temperature in Fahrenheit is: {round(temp, 1)}°F.")
# elif unit1 == "K" and unit2 == "C":
#     temp -= 273.15
#     print(f"The temperature in Celsius is: {round(temp, 1)}°C.")
# else:
#     print(f"Either {unit1} or {unit2} is not a valid unit of measurement.")


# Logical Operators = evaulate multiple conditions (or, and, not)
#                     or = at least on must be True
#                     and = both/all must be True
#                     not = inverts the condition (not False, not True)

# temp = 70
# is_raining = False

# if temp > 80 or temp < 40 or is_raining:
#     print("The outdoor event is cancelled.")
# else:
#     print("The outdoor event is still scheduled.")

# temp1 = 85
# is_sunny = True

# if temp1 >= 80 and is_sunny:
#     print("It is HOT outside! 🥵")
#     print("It is sunny. ☀️")
# elif temp1 <= 32 and is_sunny:
#     print("It is COLD outside! 🥶")
#     print("But it is sunny. ☀️")
# elif temp1 < 80 and temp1 > 32 and is_sunny:
#     print("It is WARM outside. 😌")
#     print("And it is sunny. ☀️")

# if temp1 >= 80 and not is_sunny:
#     print("It is HOT outside! 🥵")
#     print("It is CLOUDY. ☁️")
# elif temp1 <= 32 and not is_sunny:
#     print("It is COLD outside! 🥶")
#     print("And it is CLOUDY. ☁️")
# elif temp1 < 80 and temp1 > 32 and is_sunny:
#     print("It is WARM outside. 🌤️")
#     print("And it is CLOUDY. ☁️")


# Conditional Experssions = A one-line shortcut for the if-else statement (ternary operator)
#                           Print or assign one of two values based on a condition
#                           X if condition else Y

# num = -5
# a = 6
# b = 7
# age = 11
# temp = 85
# user_role = "admin"

# # print("Positive" if num > 0 else "Negative")
# # result = "EVEN" if num % 2 == 0 else "ODD"
# max_num = a if a > b else b
# min_num = a if a < b else b
# status = "You are an adult." if age >= 18 else "You are a child."
# weather = "HOT" if temp >= 80 else "COlD"
# access_level = "Full Access" if user_role == "admin" else "Limited Access"
# print(access_level)


# String Methods

# name = input("Enter your full name: ")
# phone_number = input("What is your phone number?: ")

# result = len(name)
# result = name.find(" ")
# result = name.rfind("r")
# name = name.capitalize()
# name = name.upper()
# name = name.lower()
# name = name.title()
# result = name.isdigit()
# result = name.isalpha()
# result = phone_number.count("-")
# phone_number = phone_number.replace("-", " ")

# print(help(str)) for all methods

# Validate user input exercise
# 1. username must be no more than 12 character
# 2. username cannot contain spaces
# 3. username must not contain digits

# user_name = input("Create a username: ")
# if len(user_name) > 12:
#     print("Username can't be more than 12 characters.")
# elif user_name.count(" ") > 0:
#     print("Username cannot contain spaces")
# elif any(c.isdigit() for c in user_name):
#     print("Username can't contain digits")
# else:
#     print(f"Welcome {user_name}!")


# indexing = accessing elements of a sequence using [] (indexing operator)
#            [start : end : step]

# credit_card_num = "1234-5678-9012-3333"
# print(credit_card_num[0])
# print(credit_card_num[0:4])  # you can also just type [:4]
# print(credit_card_num[-4:])  # or print(credit_card_num[-1:-5:-1])
# rev_credit_num = credit_card_num[::-1]
# print(rev_credit_num)


# format specifiers = {:flags} format a value on what flags are inserted

# .(number)f = round to that many decimal places (fixed point)
# :(number) = allocate that many spaces
# :03 = allocate and zero pad that many spaces
# :< = left justify
# :> right justify
# :^ center align
# :+ use a plus sign to indicate positive value
# := = place a sign to leftmost position
# :  = insert a space before positive numbers
# :, = comma separator

# price1 = 3.14159
# price2 = -987.65
# price3 = 12234849820913.3482348929

# print(f"Price 1 is ${price1:.2f}")
# print(f"Price 2 is ${price2:^10}")
# print(
#     f"Price 3 is ${price3:*^+25,.2f}"
# )  # order is fill, align, sign, width, grouping, precision


# while loop = execute some code WHILE some condition remains true

# name = input("Enter your name: ")

# while name == "":
#     name = input("You did not enter your name\nEnter it here: ")

# print(f"Hello, {name}!")

# age = int(input("Enter your age: "))

# while age < 0:
#     print("Age cannot be negative.")
#     age = int(input("Enter your age: "))

# print(f"You are {age} years old!")

# food = input("Enter a food you like (q to quit): ")

# while not food == "q":
#     print(f"You like {food}!")
#     food = input("Enter another food you like (q to quit): ")

# print("bye")

num = float(input("Enter a number between 1 - 10: "))

while num < 1 or num > 10:
    print(f"{num} is not a valid number.")
    num = float(input("Enter a number between 1 - 10: "))

print(f"Your number is {num}!")
