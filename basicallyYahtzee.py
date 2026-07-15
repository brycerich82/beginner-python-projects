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
