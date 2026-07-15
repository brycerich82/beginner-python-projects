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

# num = float(input("Enter a number between 1 - 10: "))

# while num < 1 or num > 10:
#     print(f"{num} is not a valid number.")
#     num = float(input("Enter a number between 1 - 10: "))

# print(f"Your number is {num}!")


# Compound Interest Calculator

# principle = 0
# rate = 0
# time = 0
# contribution = 0

# while True:
#     principle = float(input("Enter the principle value in $: "))
#     if principle < 0:
#         print("Principle can't be negative.")
#     else:
#         break

# while True:
#     contribution = float(
#         input("Enter annual contribution in $ (assume beginning-of-year payments): ")
#     )
#     if contribution < 0:
#         print("Contribution can't be negative.")
#     else:
#         break

# while True:
#     rate = float(input("Enter the expected rate of return in %: "))
#     if rate < 0:
#         print("rate can't be negative.")
#     else:
#         break

# while True:
#     time = int(input("Enter the time in years: "))
#     if time <= 0:
#         print("time can't be less than or equal to zero.")
#     else:
#         break

# if rate == 0:
#     total = principle + contribution * time
# else:
#     total = principle * pow((1 + rate / 100), time) + contribution * (
#         (pow(1 + rate / 100, time) - 1) / (rate / 100)
#     ) * (1 + rate / 100)

# print(f"\nBalance after {time} year(s) would be: ${total:.2f}")


# For Loop = execute a block of code a fixed number of times.
#            You can iterate over a range, string, sequence, etc.

# for x in range(1, 11):
#     print(x)

# for y in reversed(range(1, 11)):
#     print(y)

# print("\nHappy New Year!!!")

# credit_card = "1224-5342-5244-6424"
# for x in credit_card:
#     print(x)

# for x in range(1, 21):
#     if x == 13:
#         continue
#     else:
#         print(x)

# for x in range(1, 21):
#     if x == 13:
#         break
#     else:
#         print(x)


# import time

# my_time = int(input("Enter the time in seconds: "))

# SECONDS_IN_YEAR = 31536000
# SECONDS_IN_WEEK = 604800
# SECONDS_IN_DAY = 86400
# SECONDS_IN_HOUR = 3600
# SECONDS_IN_MINUTE = 60

# for x in range(my_time, 0, -1):
#     years = int(x / SECONDS_IN_YEAR)
#     remaining = x % SECONDS_IN_YEAR
#     weeks = int(remaining / SECONDS_IN_WEEK)
#     remaining = remaining % SECONDS_IN_WEEK
#     days = int(remaining / SECONDS_IN_DAY)
#     remaining = remaining % SECONDS_IN_DAY
#     hours = int(remaining / SECONDS_IN_HOUR)
#     remaining = remaining % SECONDS_IN_HOUR
#     minutes = int(remaining / SECONDS_IN_MINUTE)
#     seconds = remaining % SECONDS_IN_MINUTE
#     print(f"{years:02}:{weeks:02}:{days:02}:{hours:02}:{minutes:02}:{seconds:02}")
#     time.sleep(1)

# print("TIME'S UP!")


# Nested Loop = A loop within another loop (outer, inner)
#               outer loop:
#                   inner loop:

# rows = int(input("Enter the number of rows: "))
# cols = int(input("Enter the number of columns: "))
# symbol = input("Enter a symbol to use: ")

# for x in range(rows):
#     for y in range(cols):
#         print(
#             symbol, end=""
#         )  # in print() you can set end = "" instead of the natural "\n"
#     print()  # this just prints new line


# collection = single "variable" used to store multiple valuse
#   List = [] ordered and changeable. Duplicates OK
#   Set = {} unordered and immutable, but Add/Remove OK. NO duplicates
#   Tuple = () ordered and unchangeable. Duplicates OK. FASTER

# fruits = ["apple", "orange", "banana", "coconut"]
# print(dir(fruits))  # all the things you can do with this list
# print(help(fruits))  # description of attributes and methods
# print(len(fruits))  # how long collection is
# print("apple" in fruits)  # returns True or False

# fruits[1] = "pineapple"  # returns what is in the index, 0 is first index
# fruits.append("grape")  # adds "grape" to end of list
# fruits.remove("apple")  # removes item from list
# fruits.insert("tomato, 2")  # inserts in spot and move everything else down
# fruits.sort()  # puts in alphabetical/numerical order
# fruits.reverse()  # reverse order currently in
# print(fruits.index("apple"))  # gives index of item
# fruits.count("banana")  # tells how many items in list

# print(fruits[:4])

# for fruit in fruits:
#     print(fruit)

# fruits = {"apple", "orange", "banana", "coconut"}
# # print(dir(fruits))  # all the things you can do with this set
# # print(help(fruits))  # description of attributes and methods
# # print(len(fruits))  # how long set is
# # print("apple" in fruits)  # returns True or False
# # cannot index

# fruits.add("strawberry")
# fruits.remove("apple")
# fruits.pop()  # removes random item (if ran multiple times will randomly remove but keep memory of total set)
# fruits.clear()  # poof

# print(fruits)

# for fruit in fruits:
#     print(fruit)

# fruits = ("apple", "orange", "banana", "coconut")
# print(dir(fruits))  # all the things you can do with this tuple
# print(help(fruits))  # description of attributes and methods
# print(len(fruits))  # how long tuple is
# print("apple" in fruits)  # returns True or False

# print(fruits.index("apple"))
# print(fruits.count("coconut"))

# print(fruits)

# for fruit in fruits:
#     print(fruit)


# Shopping Cart Program

# items = []
# prices = []
# total = 0

# while True:
#     item = input("Enter an item to buy (q to quit): ")
#     if item.lower() == "q":
#         break
#     else:
#         price = float(input(f"Enter the price of {item}: $"))
#         items.append(item)
#         prices.append(price)

# print()
# print("----- YOUR CART -----")
# print()

# for item in items:
#     print(item)

# for price in prices:
#     total += price

# print()
# print(f"Your total is: ${total:.2f}")


# 2D collection

# fruits = ["apple", "orange", "banana", "coconut"]
# vegetables = ["celery", "carrots", "potatoes"]
# meats = ["chicken", "fish", "turkey"]

# groceries = [fruits, vegetables, meats]

# print(groceries[0][0])  # prints "apple" (row,cols)

# for collection in groceries:
#     for food in collection:
#         print(food, end=" ")
#     print()

# numpad = ((1, 2, 3), (4, 5, 6), (7, 8, 9), ("*", 0, "#"))

# for row in numpad:
#     for num in row:
#         print(num, end=" ")
#     print()


# # Python Quiz Game

# questions = (
#     "How many elements are in the periodic table?: ",
#     "Which animal lays the largest eggs?: ",
#     "What is the most abundant gas in Earth's atmosphere?: ",
#     "How many bones are in the human body?: ",
#     "Which planet in the solar system is the hottest?: ",
# )

# options = (
#     ("A. 116", "B. 117", "C. 118", "D. 119"),
#     ("A. Whale", "B. Crocodile", "C. Elephant", "D. Ostrich"),
#     ("A. Nitrogen", "B. Oxygen", "C. Carbon-Dioxide", "D. Hydrogen"),
#     ("A. 206", "B. 207", "C. 208", "D. 209"),
#     ("A. Mercury", "B. Venus", "C. Earth", "D. Mars"),
# )

# answers = ("C", "D", "A", "A", "B")
# guesses = []
# score = 0
# question_num = 0

# for question in questions:
#     print("--------------------")
#     print(question)
#     for option in options[question_num]:
#         print(option)
#     guess = input("Enter (A, B, C, D): ").upper()
#     guesses.append(guess)
#     if guess == answers[question_num]:
#         score += 1
#         print()
#         print("CORRECT!")
#     else:
#         print()
#         print("INCORRECT!")
#         print(f"{answers[question_num]} is the correct answer.")
#     question_num += 1

# print()
# print()
# print()
# print("---------------------")
# print("       RESULTS       ")
# print("---------------------")

# print("answers: ", end="")
# for answer in answers:
#     print(answer, end=" ")
# print()

# print("guesses: ", end="")
# for guess in guesses:
#     print(guess, end=" ")
# print()

# print()

# score = float(score / len(questions) * 100)
# if 0 <= score < 70:
#     print(f"Your grade is {score:.2f}%\nYou got an F!😡")
# elif 70 <= score < 75:
#     print(f"Your grade is {score:.2f}%\nYou got a D!☹️")
# elif 75 <= score < 80:
#     print(f"Your grade is {score:.2f}%\nYou got a C!😐")
# elif 80 <= score < 90:
#     print(f"Your grade is {score:.2f}%\nYou got a B!🙂")
# elif 90 <= score <= 100:
#     print(f"Your grade is {score:.2f}%\nYou got an A!🤩")


# dictionary = a collection of {key:value} pairs
#              ordered and changeable. No duplicates

capitals = {
    "USA": "Washington D.C.",
    "India": "New Dehli",
    "China": "Bejing",
    "Russia": "Moscow",
}

# print(dir(capitals)) # attributes and methods
# print(help(capitals)) # descriptions of dir()

# print(capitals.get("USA"))

# if capitals.get("Japan"):
#     print("That capital exists.")
# else:
#     print("That capital doesn't exist.")

# capitals.update({"Germany": "Berlin"})
# capitals.update({"USA": "Atlanta"})
# capitals.pop("China")
# capitals.popitem()  # removes most recent addition to dictionary
# capitals.clear()  # clears dictionary

# keys = capitals.keys()
# for key in capitals.keys():
#     print(key)

# values = capitals.values()
# for value in capitals.values():
#     print(value)

# items = capitals.items()
# for key, value in capitals.items():
#     print(f"{key}: {value}")


# # Consession Stand Program

# menu = {
#     "pizza": 3.00,
#     "nachos": 4.50,
#     "popcorn": 6.00,
#     "fries": 2.50,
#     "chips": 1.00,
#     "pretzel": 3.50,
#     "soda": 3.00,
#     "lemonade": 4.25,
# }

# cart = []
# total = 0

# print("--------- MENU ---------")
# for key, value in menu.items():
#     print(f"{key:10}: ${value:.2f}")
# print("------------------------")

# while True:
#     food = input("Select an item (q to quit): ").lower()
#     if food == "q":
#         break
#     elif menu.get(food) is not None:
#         cart.append(food)

# print()
# print("------- YOUR ORDER -------")
# for food in cart:
#     total += menu.get(food)
#     print(food, end=" | ")


# print()
# print()
# print(f"Your total is: ${total:.2f}")


# # Random Numbers

# import random

# # print(help(random)) # for guidlines

# low = 1
# high = 100
# options = ("rock", "paper", "scissors")
# cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

# # number = random.randint(low, high)
# # float = random.random()
# # option = random.choice(options)
# random.shuffle(cards)

# print(cards)


# # Number Guessing Game

# import random

# low = 1
# high = 100
# answer = random.randint(low, high)
# guesses = 0
# is_running = True

# print()
# print("Python Number Guessing game!")
# print()
# print(f"Select a number between {low} and {high}")

# while is_running:
#     guess = input("Enter your guess: ")
#     if guess.isdigit():
#         guess = int(guess)
#         guesses += 1

#         if guess < low or guess > high:
#             print()
#             print("That number is out of the given range.")
#             print(f"Please select a number between {low} and {high}")
#             print()
#         elif guess < answer:
#             print()
#             print("Too low! Try again!")
#             print()
#         elif guess > answer:
#             print()
#             print("Too high! Try again!")
#             print()
#         else:
#             print()
#             print(f"CORRECT! The answer was {answer}!")
#             print(f"You got the answer in {guesses} tries!")
#             is_running = False

#     else:
#         print()
#         print("That is not a valid guess.")
#         print(f"Please select a number between {low} and {high}")
#         print()


# # Rock Paper Scissors Game

# import random

# options = ("rock", "paper", "scissors")


# print()
# print("Welcome to Rock, Paper, Scissors!")
# print()
# username = input("What is your name?: ").title()
# running = True
# wins_in_row = 0
# loses_in_row = 0
# ties_in_row = 0

# while running:
#     player = None
#     computer = random.choice(options)

#     while player not in options:
#         player = input(f"{username}, enter a choice (rock, paper, scissors): ")
#         print()

#     print(f"{username.title()}: {player}\nComputer: {computer}.")

#     print()
#     if player == computer:
#         print("It's a TIE!")
#         ties_in_row += 1
#         wins_in_row = 0
#         loses_in_row = 0
#         print(f"{username.title()} and computer have {ties_in_row} tie(s) in a row!")
#     elif player == "rock" and computer == "scissors":
#         print("You WIN!")
#         wins_in_row += 1
#         ties_in_row = 0
#         loses_in_row = 0
#         print(f"{username.title()} has {wins_in_row} win(s) in a row!")
#     elif player == "paper" and computer == "rock":
#         print("You WIN!")
#         loses_in_row = 0
#         ties_in_row = 0
#         wins_in_row += 1
#         print(f"{username.title()} has {wins_in_row} win(s) in a row!")
#     elif player == "scissors" and computer == "paper":
#         print("You WIN!")
#         loses_in_row = 0
#         ties_in_row = 0
#         wins_in_row += 1
#         print(f"{username.title()} has {wins_in_row} win(s) in a row!")
#     else:
#         print("You LOSE!")
#         loses_in_row += 1
#         wins_in_row = 0
#         ties_in_row = 0
#         print(f"You have {loses_in_row} loss/es in a row!")

#     if not input("Play again? (y/n): ").lower() == "y":
#         running = False
#     else:
#         print()

# print()
# print("Thanks for playing!")


# Dice Roller Program
import random

# unit code chars to make dice

# print("\u25cf \u250c \u2510 \u2510 \u2502 \u2514 \u2518")

# should look like this:

# ● ┌ ┐ ┐ │ └ ┘

dice_art = {
    1: ("┌─────────┐", "│         │", "│    ●    │", "│         │", "└─────────┘"),
    2: ("┌─────────┐", "│  ●      │", "│         │", "│      ●  │", "└─────────┘"),
    3: ("┌─────────┐", "│  ●      │", "│    ●    │", "│      ●  │", "└─────────┘"),
    4: ("┌─────────┐", "│  ●   ●  │", "│         │", "│  ●   ●  │", "└─────────┘"),
    5: ("┌─────────┐", "│  ●   ●  │", "│    ●    │", "│  ●   ●  │", "└─────────┘"),
    6: ("┌─────────┐", "│  ●   ●  │", "│  ●   ●  │", "│  ●   ●  │", "└─────────┘"),
}

dice = []
total = 0
print()
num_of_dice = int(input("Enter a number of die: "))

for die in range(num_of_dice):
    dice.append(random.randint(1, 6))

# for die in range(num_of_dice):
#     for line in dice_art.get(dice[die]):   #This is for verticle die
#         print(line)

for line in range(5):
    for die in dice:
        print(dice_art.get(die)[line], end="")  # This is for horizontal die
    print()

for die in dice:
    total += die
print()
print(f"The total is: {total}!")
