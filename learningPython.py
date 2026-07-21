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

# capitals = {
#     "USA": "Washington D.C.",
#     "India": "New Dehli",
#     "China": "Bejing",
#     "Russia": "Moscow",
# }

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


# # Dice Roller Program
# import random

# # unit code chars to make dice

# # print("\u25cf \u250c \u2510 \u2510 \u2502 \u2514 \u2518")

# # should look like this:

# # ● ┌ ┐ ┐ │ └ ┘

# dice_art = {
#     1: ("┌─────────┐", "│         │", "│    ●    │", "│         │", "└─────────┘"),
#     2: ("┌─────────┐", "│  ●      │", "│         │", "│      ●  │", "└─────────┘"),
#     3: ("┌─────────┐", "│  ●      │", "│    ●    │", "│      ●  │", "└─────────┘"),
#     4: ("┌─────────┐", "│  ●   ●  │", "│         │", "│  ●   ●  │", "└─────────┘"),
#     5: ("┌─────────┐", "│  ●   ●  │", "│    ●    │", "│  ●   ●  │", "└─────────┘"),
#     6: ("┌─────────┐", "│  ●   ●  │", "│  ●   ●  │", "│  ●   ●  │", "└─────────┘"),
# }

# dice = []
# total = 0
# print()
# num_of_dice = int(input("Enter a number of die: "))

# for die in range(num_of_dice):
#     dice.append(random.randint(1, 6))

# # for die in range(num_of_dice):
# #     for line in dice_art.get(dice[die]):   #This is for verticle die
# #         print(line)

# for line in range(5):
#     for die in dice:
#         print(dice_art.get(die)[line], end="")  # This is for horizontal die
#     print()

# for die in dice:
#     total += die
# print()
# print(f"The total is: {total}!")


# Function: str = "A block of resusable code."
#                 place () after the function name to invoke it


# def happy_birthday(name: str, age: int) -> None:
#     print("Happy birthday to you!")
#     print("Happy birthday to you!")
#     print(f"Happy birthday dear {name}!")
#     print(f"You are {age} years old!\n")


# happy_birthday("Bryce", 19)
# happy_birthday("Addie", 51)
# happy_birthday("Raheem", 52)


# def display_invoice(username: str, amount: float, due_date: str) -> None:
#     print(f"Hello {username}.")
#     print(f"Your bill of ${amount:.2f} is due: {due_date}")


# display_invoice("JoeSchmo", 100.01, "1/10")

# return = statement used to end a function
#          and send a result back to the caller


# def add(x: float, y: float) -> float:
#     z = x + y
#     return z


# def subtract(x: float, y: float) -> float:
#     z = x - y
#     return z


# def multiply(x: float, y: float) -> float:
#     z = x * y
#     return z


# def divide(x: float, y: float) -> float:
#     z = x / y
#     return z


# print(multiply(4, 7))


# def create_name(f_name: str, l_name: str) -> str:
#     fullname: str = f"{f_name.capitalize()} {l_name.capitalize()}"
#     return fullname


# print(create_name("Bryce", "Richardson"))


# default argument = A default value for certain parameters
#                    default is used when that argument is omitted
#                    make your functions more flexible, reduces num of arguments
#                    1. positional, 2. DEFAULT, 3. keyword 4. arbitrary


# def net_priceATL(
#     list_price: float, discount: float = 0, tax: float = 8.9
# ) -> str:  # because of f"${x,y,z:.2f}"
#     return f"${list_price * (1 - discount / 100) * (1 + tax / 100):.2f}"


# print(net_priceATL(500))
# print(net_priceATL(500, 20))


# def count(end: int, start: int = 1) -> None:
#     for x in range(start, end + 1):
#         print(x)
#         time.sleep(1)
#     print("DONE!")


# count(10, 5)


# keyword argument = an argument preceeded by an identifier
#                    helps with readability
#                    order of arguments does not matter
#                    1. positional, 2. DEFAULT, 3. keyword 4. arbitrary


# def greet(greeting: str, title: str, first: str, last: str) -> None:
#     print(
#         f"{greeting.capitalize()}, {title.capitalize()} {first.capitalize()} {last.capitalize()},"
#     )


# greet(
#     greeting="Good day", title="Dr.", first="Michael", last="Scott"
# )  # You can mix and match

# print(
#     "1", "2", "3", "4", "5", sep="-"
# )  # sep is another keyword argument like end in print()


# def get_phone(country: int, area: int, first_3: int, last_4: int) -> str:
#     return f"+{country}({area})-{first_3}-{last_4}"


# phone_num = get_phone(1, 678, 735, 9686)
# print(phone_num)


# *args    = allows you to pass multipl non-key arguments
# **kwargs = allows you to pass multiple keyword arguments
#            * unppacking operator
#            1. positional, 2. DEFAULT, 3. keyword 4. arbitrary


# def add(*args: int) -> int:
#     total = 0

#     for arg in args:
#         total += arg
#     return total


# print(add(1, 2))


# def display_name(*names: str) -> list[str]:
#     list_name: list[str] = [name.title() for name in names]
#     return list_name


# print(
#     display_name(
#         "Bryce Richardson",
#         "brielle richardson",
#         "addie Richardson",
#         "Raheem richardson",
#     )
# )


# def print_address(**kwargs: str | int) -> None:
#     for value in kwargs.values():
#         print(value)


# print_address(street="4000 Paulette Drive", city="Monroe", state="Georgia", zip=30656)


# def shipping_lable(*args: str, **kwargs: str | int) -> None:
#     for arg in args:
#         print(arg, end=" ")
#     print()
#     for value in kwargs.values():
#         print(value, end=" ")
#     print()
#     print(
#         f"{kwargs.get('street')}\n{kwargs.get('city')} {kwargs.get('state')} {kwargs.get('zip')}"
#     )


# shipping_lable(
#     "Rev.",
#     "Dr.",
#     "Martin",
#     "Luther",
#     "King",
#     "Jr.",
#     street="4000 Paulette Drive",
#     city="Monroe",
#     state="Georgia",
#     zip=30656,
# )


# Iterable = object / collection that can return its elements one at a time,
#            allowing it to be iterated over in a loop

# numbers: list[int] = [1, 2, 3, 4, 5]

# for number in numbers:
#     print(number, end=" - ")

# numbers: tuple[int, ...] = (1, 2, 3, 4, 5)

# for number in numbers:
#     print(number)

# fruits: set[str] = {"apple", "orange", "banana", "coconut"}

# for fruit in fruits:
#     print(fruit)

# name: str = "Bryce Richardson"

# for char in name:
#     print(char, end="")

# my_dict: dict[str, int] = {"A": 1, "B": 2, "C": 3}

# for key in my_dict:
#     print(key)

# for value in my_dict.values():
#     print(value)

# for key, value in my_dict.items():
#     print(key, value)  # or you can use an f""


# Mmbership Operators = used to test whether a value or variable is found in a sequence
#                       (string, list, tuple, set, dictionary)
#                       1. in
#                       2. not in

# word: str = "APPLE"

# letter: str = input("Guess a letter in the secret word: ")

# if letter.upper() in word:
#     print(f"There is a/n {letter.upper()}.")
# else:
#     print(f"{letter.upper()} was not found.")

# if letter.upper() not in word:
#     print(f"{letter.upper()} was not found.")
# else:
#     print(f"There is a/n {letter.upper()}.")

# students: set[str] = {"Spongebob", "Patrick", "Sandy"}

# student: str = input("Enter the name of a student: ")

# if student in students:
#     print(f"{students} is a student.")
# else:
#     print(f"{student} is not a student.")

# if student not in students:
#     print(f"{students} is not a student.")
# else:
#     print(f"{students} is a student.")

# grades: dict[str, str] = {
#     "Sandy": "A",
#     "Squidward": "B",
#     "Spongebob": "C",
#     "Patrick": "D",
# }

# student: str = input("Enter the name of a student: ")

# if student in grades:
#     print(f"{student}'s grade is {grades[student]}.")
# else:
#     print(f"{student} was not found.")

# email: str = "bryce.rich82@gmail.com"

# if "@" in email and "." in email:
#     print("Valid email.")
# else:
#     print("Invalid email.")


# List comprehension = A concise way too create lists in Python
#                      Compact and easier to read than traditional loops
#                      [expression for value in iterable if condition]

# doubles: list[int] = []

# for x in range(1, 11):
#     doubles.append(x * 2)   # This is the bad way

# print(doubles)

# doubles: list[int] = [x * 2 for x in range(1, 11)]

# doubles_set: set[int] = {x * 2 for x in range(1, 11)}

# doubles_dict: dict[int, int] = {x: x * 2 for x in range(1, 11)}

# doubles_tuple: tuple[int, ...] = tuple(x for x in range(1, 11))

# fruits: list[str] = ["apple", "orange", "banana", "coconut"]
# fruits_upper: list[str] = [fruit.upper() for fruit in fruits]

# print(fruits_upper)

# numbers = [1, -2, 3, -4, 5, -6, -7, 8]

# pos_nums: list[int] = [num for num in numbers if num >= 0]
# negative_nums: list[int] = [num for num in numbers if num < 0]
# even_nums: list[int] = [num for num in numbers if num % 2 == 0]
# odd_nums: list[int] = [num for num in numbers if num % 2 == 1]

# print(odd_nums)

# grades: list[int] = [85, 42, 79, 90, 56, 61, 30]
# passing_grades: list[int] = [grade for grade in grades if grade >= 60]

# print(passing_grades)


# Match-case statements (switch) = An alternative to using many elif statements
#                                  Execute some code if a value matches a case
#                                  Benefits: cleaner and syntax is more readable


# def day_of_week(day: int) -> str:
#     if day == 1:
#         return "It is Sunday"
#     elif day == 2:
#         return "It is Monday"
#     elif day == 3:
#         return "It is Tuesday"
#     elif day == 4:
#         return "It is Wednesday"  # Really bad and ugly
#     elif day == 5:
#         return "It is Thursday"
#     elif day == 6:
#         return "It is Friday"
#     elif day == 7:
#         return "It is Saturday"
#     else:
#         return "Not a valid day"


# print(day_of_week(1))


# def is_weekend(day: int) -> bool | str:
#     match day:
#         case "Sunday":
#             return True
#         case "Monday":
#             return False
#         case "Tuesday":
#             return False
#         case "Wednesday":
#             return False  # Really bad and ugly but better
#         case "Thursday":
#             return False
#         case "Friday":
#             return False
#         case "Saturday":
#             return True
#         case _:
#             return "Not a valid day"


# print(day_of_week(1))


# def is_weekend(day: int) -> bool | str:
#     match day:
#         case "Saturday" | "Sunday":
#             return True
#         case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday":  # Best
#             return False
#         case _:
#             return "Not a valid day"


# print(is_weekend(1))


# module = a file containing code you want to include in your program
#          use import to include a module (built in or your own)
#          useful to break up a large program reusable seperate files

# help("math")

# import math

# print(math.pi)

# import math as m

# print(m.pi)

# from math import pi

# print(pi)

# import moduleLearn

# # result: float = moduleLearn.pi
# # result: int = moduleLearn.square(3)
# # result: int = moduleLearn.cube(3)
# # result: float = moduleLearn.circumference(3)
# result: float = moduleLearn.area_of_circle(3)

# print(result)


# variable scope = where a variable is visible and accessible
# scope resolution = (LEGB) Local -> Enclosed -> Global -> Built-in (That is the order of operations)


# def func1() -> None:
#     a = 1
#     print(a)

#                                   #These are local examples
# def func2() -> None:
#     b = 2
#     print(b)


# func1()
# func2()


# def func1() -> None:
#     x = 1
#     print(x)
#                                           #These are enclosed examples
#     def func2() -> None:
#         x = 2
#         print(x)

#     func2()  # if ran, this prints 2


# func1()

#                                                #These are enclosed examples
# def func1() -> None:
#     x = 1
#     print(x)

#     def func2() -> None:

#         print(x)

#     func2()  # if ran, this prints 1


# func1()


# def func1() -> None:
#     print(x)


# #                                   #These are global examples
# def func2() -> None:
#     print(x)


# x = 3
# func1()
# func2()

# from math import e

# # def func1() -> None:
# #     print(e) #                   This prints 2.7...


# # func1()


# def func1() -> None:
#     print(e)  #                      This prints 3 (global comes before built-in)


# e = 3

# func1()


# if __name__ == '__main__': (this script can be imported OR run standalone)
#                            Functions and classes in this module can be reused
#                            without the main block of code executing

# ex. library = Import library for functionality
#               When running library directly, display a help page


# Banking Program


# def show_balance(balance) -> None:
#     print(f"Your balance is ${balance:.2f}.")


# def deposit() -> float:
#     amount = float(input("Enter an amount to be deposited: $"))

#     if amount < 0:
#         print("That is not a valid amount.\nPlease try again.")
#         return 0
#     else:
#         return amount


# def withdraw(balance) -> float:
#     amount = float(input("Enter an amount to be withdrawn: $"))

#     if amount > balance:
#         print("Insufficient funds.\nPlease try again.")
#         return 0
#     elif amount < 0:
#         print("Amount must be greater than 0.")
#         return 0
#     else:
#         return amount


# def main() -> None:
#     balance: float = 0
#     is_running = True

#     while is_running:
#         print()
#         print("--------- Rich. Bank ----------")
#         print()
#         print("1.Show Balance")
#         print("2.Deposit")
#         print("3.Withdraw")
#         print("4.Exit")
#         print()

#         choice = input("Enter your choice (1-4): ")
#         print()

#         if choice == "1":
#             show_balance(balance)
#         elif choice == "2":
#             balance += deposit()
#             print(f"\nYour new balance is ${balance:.2f}.")
#         elif choice == "3":
#             balance -= withdraw(balance)
#             print(f"\nYour new balance is ${balance:.2f}.")
#         elif choice == "4":
#             print(f"\nYour account balance is: ${balance:.2f}.")
#             is_running = False
#         else:
#             print("That is not a valid choice.\nPlease try again.\n")

#     print()
#     print("Thank you. Have a nice day!")


# if __name__ == "__main__":
#     main()


# # Beginner Slot Machine Program
# import random
# import time


# def spin_row() -> list[str]:
#     symbols: list[str] = ["🍒"] * 34 + ["🍉"] * 9 + ["🍋"] * 4 + ["🔔"] * 2 + ["⭐️"] * 1

#     return [random.choice(symbols) for _ in range(3)]


# def print_row(row: list[str]) -> None:
#     print()
#     print("-------------")
#     print(" | ".join(row))
#     print("-------------")
#     print()


# def get_payout(row: str, bet: int) -> int:
#     if row[0] == row[1] == row[2]:
#         if row[0] == "🍒":
#             return bet * 3
#         elif row[0] == "🍉":
#             return bet * 4
#         elif row[0] == "🍋":
#             return bet * 5
#         elif row[0] == "🔔":
#             return bet * 10
#         elif row[0] == "⭐️":
#             return bet * 20
#     return 0


# def main():
#     balance: int = 100
#     print()
#     print("*************************")
#     print("Welcome to Python Slots!")
#     print("Symbols: 🍒 🍉 🍋 🔔 ⭐️")
#     print("*************************")

#     while balance > 0:
#         print(f"Current balance: ${balance}")
#         bet: str = input("Place you bet amount: $")
#         print()
#         if not bet.isdigit():
#             print("Please enter a numerical value.")
#             continue

#         bet: int = int(bet)

#         if bet > balance:
#             print("Insufficient Funds.")
#             continue

#         if bet <= 0:
#             print("Bet must be greater than 0.")
#             continue

#         balance -= bet

#         row: list[str] = spin_row()
#         print("Spinning...\n")
#         time.sleep(3)
#         print_row(row)

#         payout: int = get_payout(row, bet)

#         if payout > 0:
#             print(f"You won ${payout}!!!")
#         else:
#             print("Sorry you lost this round.")

#         balance += payout

#         play_again: str = input("Do you want to spin again? (Y/N): ")
#         print()

#         if play_again.upper() != "Y":
#             break

#     print("********************************************")
#     print(f"Game Over! Your current balance is ${balance}.")
#     print("********************************************")


# if __name__ == "__main__":
#     main()


# # Substitution Cipher Encryption Program

# import random
# import string

# chars: list[str] = list(" " + string.punctuation + string.digits + string.ascii_letters)
# key: list[str] = chars.copy()

# random.shuffle(key)

# # print(f"chars: {chars}")
# # print(f"key: {key}")

# # ENCRYPT
# plain_text: str = input("Enter a message to encrypt: ")
# cipher_text: str = ""
# print()

# for letter in plain_text:
#     index: int = chars.index(letter)
#     cipher_text += key[index]

# print(f"Original message : {plain_text}")
# print(f"Encrypted Message: {cipher_text}")
# print()

# # DECRYPT
# cypher_text: str = input("Enter a message to decrypt: ")
# plain_text_text: str = ""
# print()

# for letter in cipher_text:
#     rev_index: int = key.index(letter)
#     plain_text_text += chars[rev_index]

# print(f"Encrypted Message: {cipher_text}")
# print(f"Original message : {plain_text}")


# Hangman in Python
# import random

# from hangmanWord import words

# hangman_art: dict[int, tuple[str, ...]] = {
#     0: ("   ", "   ", "   "),
#     1: (" o ", "   ", "   "),
#     2: (" o ", " | ", "   "),
#     3: (" o ", "/| ", "   "),
#     4: (" o ", "/|\\  ", "   "),
#     5: (" o ", "/|\\", "/  "),
#     6: (" o ", "/|\\", "/ \\"),
# }


# def display_man(wrong_guesses: int) -> None:
#     print("----------")
#     for line in hangman_art[wrong_guesses]:
#         print(line)
#     print("----------")


# def display_hint(hint: list[str]) -> None:
#     print()
#     print(" ".join(hint))
#     print()


# def display_answer(answer: str) -> None:
#     print(" ".join(answer))


# def main() -> None:
#     answer: str = random.choice(words)
#     hint: list[str] = ["_"] * len(answer)
#     wrong_guesses: int = 0
#     guessed_letters: set[str] = set()
#     is_running: bool = True

#     while is_running:
#         display_man(wrong_guesses)
#         display_hint(hint)
#         guess: str = input("Enter a letter: ").lower()

#         if len(guess) != 1 or not guess.isalpha():
#             print("Invalid input.\nPlease enter 1 letter.")
#             continue

#         if guess in guessed_letters:
#             print()
#             print(f"{guess} is already guessed.")
#             print()
#             continue

#         guessed_letters.add(guess)

#         if guess in answer:
#             for i in range(len(answer)):
#                 if answer[i] == guess:
#                     hint[i] = guess
#         else:
#             wrong_guesses += 1

#         if "_" not in hint:
#             display_man(wrong_guesses)
#             display_answer(answer)
#             print("YOU WIN!")
#             is_running = False
#         elif wrong_guesses >= len(hangman_art) - 1:
#             display_man(wrong_guesses)
#             display_answer(answer)
#             print("YOU LOSE!")
#             is_running = False


# if __name__ == "__main__":
#     main()


# object = A "bundle" of related attributes (variables) and methods (functions)
#          Ex. phone, cup, book
#          You need a "class" to create many objects

# class = (blueprint) used to design the structure and layout of an object


# class Car:
#     def __init__(self, model: str, year: int, color: str, for_sale: bool):
#         self.model: str = model
#         self.year: int = year
#         self.color: str = color
#         self.for_sale: bool = for_sale

# from car import Car

# car1 = Car("Mazda 6", 2018, "white", False)
# car2 = Car("Porsche", 2027, "black", True)
# car3 = Car("Demon 170", 2026, "purple", False)

# # print(car3.model)
# # print(car3.year)
# # print(car3.color)
# # print(car3.for_sale)

# # car1.drive()
# # car2.drive()
# # car3.drive()

# # car1.stop()
# # car2.stop()
# # car3.stop()

# car1.describe()
# car2.describe()
# car3.describe()


# calss variables = Shared among all instances of a class
#                   Defined outside the constuctor
#                   Allow you to share data among all objects created from that class


# class Student:
#     class_year = 2029
#     num_students = 0

#     def __init__(self, name: str, age: int):
#         self.name: str = name
#         self.age: int = age
#         Student.num_students += 1


# student1 = Student("Spongebob", 30)
# student2 = Student("Patrick", 35)
# student3 = Student("Squidward", 35)
# student4 = Student("Sandy", 27)

# print(student1.name)
# print(student1.age)

# print(student2.name)
# print(student2.age)

# print(student1.class_year)
# print(student2.class_year)

# print(Student.class_year)  # This better to find class year

# print(Student.num_students)

# print(
#     f"My graduating class of {Student.class_year} has {Student.num_students} students:"
# )
# print(student1.name)
# print(student2.name)
# print(student3.name)
# print(student4.name)


# Inheritance = Allows a class to inherit attributes and methods from another class
#               Helps with code reusability and extensibility
#               class Child(parent)


# class Animal:
#     def __init__(self, name: str) -> None:
#         self.name: str = name
#         self.is_alive: bool = True

#     def eat(self) -> None:
#         print(f"{self.name} is eating.")

#     def sleep(self) -> None:
#         print(f"{self.name} is sleeping.")


# class Dog(Animal):
#     def speak(self) -> None:
#         print("WOOF!")


# class Cat(Animal):
#     def speak(self) -> None:
#         print("MEOW!")


# class Mouse(Animal):
#     def speak(self) -> None:
#         print("SQUEAK!")


# dog = Dog("Scooby")
# cat = Cat("Garfield")
# mouse = Mouse("Micky")

# print(dog.name)
# print(dog.is_alive)
# dog.eat()
# dog.sleep()
# dog.speak()
# print()

# print(cat.name)
# print(cat.is_alive)
# cat.eat()
# cat.sleep()
# cat.speak()
# print()

# print(mouse.name)
# print(mouse.is_alive)
# mouse.eat()
# mouse.sleep()
# mouse.speak()


# multiple inheritance = inherit from more than one parent class
#                        C(A, B)

# multilevel inheritance = inherit from a parent which inherits from another parent
#                          C(B) <- B(A) <- A


# class Animal:
#     def __init__(self, name: str):
#         self.name = name

#     def eat(self) -> None:
#         print(f"{self.name} is eating.")

#     def sleep(self) -> None:
#         print(f"{self.name} is sleeping.")


# class Prey(Animal):
#     def flee(self) -> None:
#         print(f"{self.name} is fleeing.")


# class Predator(Animal):
#     def hunt(self) -> None:
#         print(f"{self.name} is hunting.")


# class Rabbit(Prey):
#     pass


# class Hawk(Predator):
#     pass


# class Fish(Prey, Predator):
#     pass


# rabbit = Rabbit("Bugs")
# hawk = Hawk("Tony")
# fish = Fish("Nemo")

# rabbit.flee()
# print()

# hawk.hunt()
# print()

# fish.flee()
# fish.hunt()

# rabbit.eat()
# rabbit.sleep()
# print()

# fish.eat()
# fish.sleep()
# print()

# hawk.eat()
# hawk.sleep()


# super() = Function used in a childe class to call methods from a parent class (superclass).
#           Allows you to extend the functionality of the inherited methods


# class Shape:
#     def __init__(self, color: str, is_filled: bool) -> None:
#         self.color: str = color
#         self.is_filled: bool = is_filled

#     def describe(self) -> None:
#         print(f"It is {self.color} and {'filled' if self.is_filled else 'not filled'}.")


# class Circle(Shape):
#     def __init__(self, color: str, is_filled: bool, radius: int) -> None:
#         super().__init__(color, is_filled)
#         self.radius: int = radius

#     def describe(self) -> None:
#         super().describe()
#         print(f"It is a circle with an area of {3.14 * self.radius**2}cm²")


# class Square(Shape):
#     def __init__(self, color: str, is_filled: bool, width: int) -> None:
#         super().__init__(color, is_filled)
#         self.width: int = width

#     def describe(self) -> None:
#         super().describe()
#         print(f"It is a square with an area of {self.width**2}cm²")


# class Triangle(Shape):
#     def __init__(self, color: str, is_filled: bool, width: int, height: int) -> None:
#         super().__init__(color, is_filled)
#         self.width: int = width
#         self.height: int = height

#     def describe(self) -> None:
#         super().describe()
#         print(f"It is a triangle with an area of {0.5 * self.width * self.height}cm²")


# circle = Circle(color="red", is_filled=True, radius=5)
# square = Square(color="blue", is_filled=False, width=6)
# triangle = Triangle(color="yellow", is_filled=True, width=7, height=8)

# print(circle.color)
# print(circle.is_filled)
# print(f"{circle.radius}cm")
# circle.describe()
# print()

# print(square.color)
# print(square.is_filled)
# print(f"{square.width}cm")
# square.describe()
# print()

# print(triangle.color)
# print(triangle.is_filled)
# print(f"{triangle.width}cm")
# print(f"{triangle.height}cm")
# triangle.describe()
# print()


# Polymorphism = Greek word that means to "have many forms or faces"
#                Poly = many
#                Morphe = form

#                TWO WAYS TO ACHIEVE POLYMORPHISM
#                1. Inheritance = An object could be treated of the same tyoe as a parent class
#                2. "Duck typing" = Object must have necesarry attributes/methods

# from abc import abstractmethod


# class Shape:
#     @abstractmethod
#     def area(self) -> float:
#         pass


# class Circle(Shape):
#     def __init__(self, radius: float) -> None:
#         self.radius = radius

#     def area(self) -> float:
#         return 3.14 * self.radius**2


# class Square(Shape):
#     def __init__(self, width: float) -> None:
#         self.width = width

#     def area(self) -> float:
#         return self.width**2


# class Triangle(Shape):
#     def __init__(self, width, height) -> None:
#         self.width = width
#         self.height = height

#     def area(self) -> float:
#         return 0.5 * self.width * self.height


# class Pizza(Circle):
#     def __init__(self, topping, radius) -> None:
#         super().__init__(radius)
#         self.topping = topping


# shapes: list[Shape] = [Circle(4), Square(5), Triangle(6, 7), Pizza("pepperoni", 15)]

# for shape in shapes:
#     print(f"{shape.area()}cm²")


# Duck typing = another way to achieve polymorphism besides Inheritance
#               Object must have the minimum necessary attributes/methods
#               "If it looks like a duck and quacks like a duck, it must be a duck."


# class Animal:
#     alive = True


# class Dog(Animal):
#     def speak(self) -> None:
#         print("Woof!")


# class Cat(Animal):
#     def speak(self) -> None:
#         print("Meow!")


# class Car:
#     alive = False

#     def speak(self) -> None:
#         print("HONK!")


# animals: list[object] = [Dog(), Cat(), Car()]

# for animal in animals:
#     animal.speak()
#     print(animal.alive)


# Static methods = a method that belog to a class rather than any object from that class (instance)
#                  Usually use for general utility functions

# Instance methods = best for operations on instances of the class (objects)
# Static methods = best for utility functions that do not need access to class data


# class Employee:
#     def __init__(self, name: str, position: str) -> None:
#         self.name: str = name
#         self.position: str = position

#     def get_info(self) -> str:
#         return f"{self.name} = {self.position}"

#     @staticmethod  # general utility method, not reliant on objects created in that class
#     def is_valid_position(position) -> bool:
#         valid_positions: list[str] = ["Manager", "Cashier", "Cook", "Janitor"]
#         return position in valid_positions


# employee1 = Employee("Eugene", "Manager")
# employee2 = Employee("Squidward", "Cashier")
# employee3 = Employee("Spongebob", "Cook")


# print(Employee.is_valid_position("Rocket Scientist"))
# print(employee1.get_info())
# print(employee2.get_info())
# print(employee3.get_info())


# Class method = allows operations related to the class itself
#                Take (cls) as the first parameter, which represents the class itself.


# class Student:
#     count: int = 0

#     total_gpa: float = 0

#     def __init__(self, name: str, gpa: float):
#         self.name: str = name
#         self.gpa: float = gpa
#         Student.count += 1
#         Student.total_gpa += gpa

#     # INSTANCE METHOD
#     def get_info(self) -> str:
#         return f"{self.name} {self.gpa}"

#     @classmethod
#     def get_count(cls) -> str:
#         return f"Total number of students: {cls.count}"

#     @classmethod
#     def get_average_gpa(cls) -> str | float:
#         if cls.count == 0:
#             return 0
#         else:
#             return f"The average student gpa: {cls.total_gpa / cls.count:.2f}"


# student1 = Student("Spongebob", 3.2)
# student2 = Student("Patrick", 2.0)
# student3 = Student("Sandy", 4.0)


# print(Student.get_count())
# print(Student.get_average_gpa())


# Magice methods = Dunder methods (double-underscore) __init__, __str__, __eq__
#                  They are automatically called by many of Python's built-in operations.
#                  They allow developers to define or customize the behavior of objects


# class Book:
#     def __init__(self, title: str, author: str, num_pages: int):
#         self.title = title
#         self.author = author
#         self.num_pages = num_pages

#     def __str__(self) -> str:
#         return f"'{self.title}' by {self.author}"

#     def __eq__(self, other) -> bool:
#         return self.title == other.title and self.author == other.author

#     def __lt__(self, other) -> bool:
#         return self.num_pages < other.num_pages

#     def __gt__(self, other) -> bool:
#         return self.num_pages > other.num_pages

#     def __add__(self, other) -> str:
#         return f"{self.num_pages + other.num_pages} pages"

#     def __contains__(self, keyword):
#         return keyword in self.title or keyword in self.author

#     def __getitem__(self, key) -> str | int:
#         if key == "title":
#             return self.title
#         elif key == "author":
#             return self.author
#         elif key == "num_pages":
#             return self.num_pages
#         raise KeyError(key)


# book1 = Book("The Hobbit", "J.R.R. Tolkien", 310)
# book2 = Book("Harry Potter and The Philosopher's Stone", "J.K. Rowling", 223)
# book3 = Book("The Lion, the Witch, and the Wardrobe", "C.S. Lewis", 172)


# print(book3)
# print(book1 == book2)
# print(book2 < book3)
# print(book2 > book3)
# print(book2 + book3)
# print("Lion" in book3)
# print(book1["title"])
# print(book2["author"])
# print(book3["num_pages"])
# print(book1["hi"])

# @property = Decorator used to define a method as a property (it can be accessed like an attribute)
#             Benefit: add additional logic when read, write, or delete attributes
#             Gives you getter, setter, and deleter method


# class Rectangle:
#     def __init__(self, width: float, height: float):
#         self._width: float = width
#         self._height: float = height

#     @property
#     def width(self) -> str:
#         return f"{self._width:.1f}cm"

#     @property
#     def height(self) -> str:
#         return f"{self._height:.1f}cm"

#     @width.setter
#     def width(self, new_width: int):
#         if new_width > 0:
#             self._width = new_width
#         else:
#             print("Width must be greater than 0")

#     @height.setter
#     def height(self, new_height: int):
#         if new_height > 0:
#             self._height = new_height
#         else:
#             print("Height must be greater than 0")

#     @width.deleter
#     def width(self):
#         del self._width
#         print("Width has been deleted.")

#     @height.deleter
#     def height(self):
#         del self._height
#         print("Height has been deleted.")


# rectangle = Rectangle(3, 4)

# rectangle.width = 5
# rectangle.height = 6

# del rectangle.width
# del rectangle.height

# print(rectangle.width)
# print(rectangle.height)


# Decorator = a function that extends the behavior of another function
#             w/o modifying the base function
#             Pass the base function as an argument to the decorator

#             @add_sprinkles
#             get_ice_cream("vanilla")


# def add_sprinkles(func):
#     def wrapper(
#         *args, **kwargs
#     ):  # need wrapper() because if @ is applied, it will call the functions even if you did not call them
#         print("*You add sprinkles 🎊* ")
#         func(*args, **kwargs)

#     return wrapper


# def add_fudge(func):
#     def wrapper(*args, **kwargs):
#         print("*You add fudge 🍫*")
#         func(*args, **kwargs)

#     return wrapper


# @add_sprinkles
# @add_fudge
# def get_ice_cream(flavor: str) -> None:
#     print(f"Here is your {flavor} ice cream 🍦")


# get_ice_cream("vanilla")
