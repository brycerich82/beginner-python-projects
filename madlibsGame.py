# Mad Libs Game

print("\nWelcome to Bryce's MADLIBS Game!")
user_name = str(input("What is your name?: "))
print(f"\nNice to meet you {user_name.title()}! Let's get started:")

adj1 = input("To start, let's pick an adjective (description): ")
noun1 = input(
    "\nNice! Ok, now we need a subject.\nEnter a noun (person, place, or thing): "
)
adj2 = input(
    "\nMain character energy lowk 😂\nNow enter a second adjective (description): "
)
verb1 = input(
    "\nClassy, let's see what buddy's up to!\nEnter a verb ending in 'ing' (an action): "
)
adj3 = input(
    "\nPutting it all together now...describe yourself reacting to this situation.\nEnter the last adjective (description): "
)

print("\nLet's see just how crazy this story is!")
print(f"\nToday I went to a(n) {adj1.title()} Zoo.")
print(f"In an exhibit, I saw a(n) {noun1}.")
print(f"{noun1.title()} was {adj2.lower()} and {verb1.lower()}!")
print(f"I was {adj3.lower()}!")
print(
    f"\nThank you for playing Bryce's Madlibs Game, {user_name}!\nHave a blessed one, and come back soon!😊"
)
