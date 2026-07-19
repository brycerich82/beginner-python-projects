# Hangman in Python
import random

from hangmanWord import words

hangman_art: dict[int, tuple[str, ...]] = {
    0: ("   ", "   ", "   "),
    1: (" o ", "   ", "   "),
    2: (" o ", " | ", "   "),
    3: (" o ", "/| ", "   "),
    4: (" o ", "/|\\  ", "   "),
    5: (" o ", "/|\\", "/  "),
    6: (" o ", "/|\\", "/ \\"),
}


def display_man(wrong_guesses: int) -> None:
    print("----------")
    for line in hangman_art[wrong_guesses]:
        print(line)
    print("----------")


def display_hint(hint: list[str]) -> None:
    print()
    print(" ".join(hint))
    print()


def display_answer(answer: str) -> None:
    print(" ".join(answer))


def main() -> None:
    answer: str = random.choice(words)
    hint: list[str] = ["_"] * len(answer)
    wrong_guesses: int = 0
    guessed_letters: set[str] = set()
    is_running: bool = True

    while is_running:
        display_man(wrong_guesses)
        display_hint(hint)
        guess: str = input("Enter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input.\nPlease enter 1 letter.")
            continue

        if guess in guessed_letters:
            print()
            print(f"{guess} is already guessed.")
            print()
            continue

        guessed_letters.add(guess)

        if guess in answer:
            for i in range(len(answer)):
                if answer[i] == guess:
                    hint[i] = guess
        else:
            wrong_guesses += 1

        if "_" not in hint:
            display_man(wrong_guesses)
            display_answer(answer)
            print("YOU WIN!")
            is_running = False
        elif wrong_guesses >= len(hangman_art) - 1:
            display_man(wrong_guesses)
            display_answer(answer)
            print("YOU LOSE!")
            is_running = False


if __name__ == "__main__":
    main()
