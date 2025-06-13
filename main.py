# main.py

from art import logo, vs
from game_data import data
import random
import os


def format_account(account):
    """Format account data for display."""
    name = account["name"]
    description = account["description"]
    country = account["country"]
    return f"{name}, a {description}, from {country}"


def is_guess_correct(guess, a_followers, b_followers):
    """Return True if the guess is correct, otherwise False."""
    return (a_followers > b_followers and guess == "a") or \
           (b_followers > a_followers and guess == "b")


def clear_screen():
    """Clears the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')


def play_game():
    print(logo)
    score = 0
    game_continues = True

    account_b = random.choice(data)

    while game_continues:
        account_a = account_b
        account_b = random.choice(data)

        # Ensure unique accounts
        while account_b == account_a:
            account_b = random.choice(data)

        print(f"Compare A: {format_account(account_a)}")
        print(vs)
        print(f"Against B: {format_account(account_b)}")

        guess = input("Who has more followers? Type 'A' or 'B': ").lower()
        clear_screen()
        print(logo)

        a_followers = account_a["follower_count"]
        b_followers = account_b["follower_count"]

        if is_guess_correct(guess, a_followers, b_followers):
            score += 1
            print(f"✅ You're right! Current score: {score}\n")
        else:
            print(f"❌ Sorry, that's wrong. Final score: {score}")
            game_continues = False


if __name__ == "__main__":
    play_game()
