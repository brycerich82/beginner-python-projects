# Python Quiz Game

questions = (
    "How many elements are in the periodic table?: ",
    "Which animal lays the largest eggs?: ",
    "What is the most abundant gas in Earth's atmosphere?: ",
    "How many bones are in the human body?: ",
    "Which planet in the solar system is the hottest?: ",
)

options = (
    ("A. 116", "B. 117", "C. 118", "D. 119"),
    ("A. Whale", "B. Crocodile", "C. Elephant", "D. Ostrich"),
    ("A. Nitrogen", "B. Oxygen", "C. Carbon-Dioxide", "D. Hydrogen"),
    ("A. 206", "B. 207", "C. 208", "D. 209"),
    ("A. Mercury", "B. Venus", "C. Earth", "D. Mars"),
)

answers = ("C", "D", "A", "A", "B")
guesses = []
score = 0
question_num = 0

for question in questions:
    print("--------------------")
    print(question)
    for option in options[question_num]:
        print(option)
    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print()
        print("CORRECT!")
    else:
        print()
        print("INCORRECT!")
        print(f"{answers[question_num]} is the correct answer.")
    question_num += 1

print()
print()
print()
print("---------------------")
print("       RESULTS       ")
print("---------------------")

print("answers: ", end="")
for answer in answers:
    print(answer, end=" ")
print()

print("guesses: ", end="")
for guess in guesses:
    print(guess, end=" ")
print()

print()

score = float(score / len(questions) * 100)
if 0 <= score < 70:
    print(f"Your grade is {score:.2f}%\nYou got an F!😡")
elif 70 <= score < 75:
    print(f"Your grade is {score:.2f}%\nYou got a D!☹️")
elif 75 <= score < 80:
    print(f"Your grade is {score:.2f}%\nYou got a C!😐")
elif 80 <= score < 90:
    print(f"Your grade is {score:.2f}%\nYou got a B!🙂")
elif 90 <= score <= 100:
    print(f"Your grade is {score:.2f}%\nYou got an A!🤩")
