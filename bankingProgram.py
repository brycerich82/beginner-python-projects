def show_balance(balance) -> None:
    print(f"Your balance is ${balance:.2f}.")


def deposit() -> float:
    amount = float(input("Enter an amount to be deposited: $"))

    if amount < 0:
        print("That is not a valid amount.\nPlease try again.")
        return 0
    else:
        return amount


def withdraw(balance) -> float:
    amount = float(input("Enter an amount to be withdrawn: $"))

    if amount > balance:
        print("Insufficient funds.\nPlease try again.")
        return 0
    elif amount < 0:
        print("Amount must be greater than 0.")
        return 0
    else:
        return amount


def main() -> None:
    balance: float = 0
    is_running = True

    while is_running:
        print()
        print("--------- Rich. Bank ----------")
        print()
        print("1.Show Balance")
        print("2.Deposit")
        print("3.Withdraw")
        print("4.Exit")
        print()

        choice = input("Enter your choice (1-4): ")
        print()

        if choice == "1":
            show_balance(balance)
        elif choice == "2":
            balance += deposit()
            print(f"\nYour new balance is ${balance:.2f}.")
        elif choice == "3":
            balance -= withdraw(balance)
            print(f"\nYour new balance is ${balance:.2f}.")
        elif choice == "4":
            print(f"\nYour account balance is: ${balance:.2f}.")
            is_running = False
        else:
            print("That is not a valid choice.\nPlease try again.\n")

    print()
    print("Thank you. Have a nice day!")


if __name__ == "__main__":
    main()
