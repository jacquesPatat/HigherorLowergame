from random import randint
from art import logo

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


def check_answer(user_guess, actual_answer, turns):
    """Compares guess to the actual answer and returns updated turns."""
    if user_guess > actual_answer:
        print("Too high.")
        return turns - 1
    elif user_guess < actual_answer:
        print("Too low.")
        return turns - 1
    else:
        print(f"You got it! The answer was {actual_answer}.")
        return turns


def set_difficulty():
    """Prompts the user to choose a difficulty and returns attempts based on it."""
    while True:
        level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
        if level == "easy":
            return EASY_LEVEL_TURNS
        elif level == "hard":
            return HARD_LEVEL_TURNS
        else:
            print("Invalid input. Please type 'easy' or 'hard'.")


def get_valid_guess():
    """Prompts the user for a valid integer guess."""
    while True:
        try:
            return int(input("Make a guess: "))
        except ValueError:
            print("Invalid input. Please enter a number.")


def play_game():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    answer = randint(1, 100)
    # Uncomment for debugging:
    # print(f"[DEBUG] The correct answer is {answer}")

    turns = set_difficulty()
    guess = None

    while guess != answer and turns > 0:
        print(f"\nYou have {turns} attempt(s) remaining.")
        guess = get_valid_guess()
        turns = check_answer(guess, answer, turns)

        if guess != answer and turns > 0:
            print("Guess again.")

    if guess != answer:
        print(f"You've run out of guesses. The correct answer was {answer}. You lose.")


def main():
    while True:
        play_game()
        replay = input("\nWould you like to play again? (yes/no): ").lower()
        if replay not in ["yes", "y"]:
            print("Thanks for playing! Goodbye.")
            break


main()
