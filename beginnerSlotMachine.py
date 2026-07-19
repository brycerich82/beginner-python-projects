# Beginner Slot Machine Program

import random
import time


def spin_row() -> list[str]:
    symbols: list[str] = ["🍒"] * 34 + ["🍉"] * 9 + ["🍋"] * 4 + ["🔔"] * 2 + ["⭐️"] * 1

    return [random.choice(symbols) for _ in range(3)]


def print_row(row: list[str]) -> None:
    print()
    print("-------------")
    print(" | ".join(row))
    print("-------------")
    print()


def get_payout(row: str, bet: int) -> int:
    if row[0] == row[1] == row[2]:
        if row[0] == "🍒":
            return bet * 3
        elif row[0] == "🍉":
            return bet * 4
        elif row[0] == "🍋":
            return bet * 5
        elif row[0] == "🔔":
            return bet * 10
        elif row[0] == "⭐️":
            return bet * 20
    return 0


def main():
    balance: int = 100
    print()
    print("*************************")
    print("Welcome to Python Slots!")
    print("Symbols: 🍒 🍉 🍋 🔔 ⭐️")
    print("*************************")

    while balance > 0:
        print(f"Current balance: ${balance}")
        bet: str = input("Place you bet amount: $")
        print()
        if not bet.isdigit():
            print("Please enter a numerical value.")
            continue

        bet: int = int(bet)

        if bet > balance:
            print("Insufficient Funds.")
            continue

        if bet <= 0:
            print("Bet must be greater than 0.")
            continue

        balance -= bet

        row: list[str] = spin_row()
        print("Spinning...\n")
        time.sleep(3)
        print_row(row)

        payout: int = get_payout(row, bet)

        if payout > 0:
            print(f"You won ${payout}!!!")
        else:
            print("Sorry you lost this round.")

        balance += payout

        play_again: str = input("Do you want to spin again? (Y/N): ")
        print()

        if play_again.upper() != "Y":
            break

    print("********************************************")
    print(f"Game Over! Your current balance is ${balance}.")
    print("********************************************")


if __name__ == "__main__":
    main()
