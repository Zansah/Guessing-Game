
import random 
import time

diff_level = {
    "easy": {"range": 10, "attempts": 5},
    "medium": {"range": 50, "attempts": 7},
    "hard": {"range": 100, "attempts": 10}
}

def difficulty():
    while True:
        level = input("Choose a difficulty (easy, medium, hard): ").lower()
        if level in diff_level:
            return diff_level[level]
        else:
            print("Please enter a valid choice")

def generate_num(range_val):
    return random.randint(1, range_val)

def get_user_guess():
    while True:
        try:
            guess = int(input("Enter your guess: "))
            return guess
        except ValueError:
            print("Invalid input. Please enter a number.")

def hint(guess, number):
    if guess < number:
        print("Too low!")
    elif guess > number:
        print("Too high!")

def display_score(attempts, max_attempts):
    score = max(0, max_attempts - attempts)
    print(f"Your score: {score}/{max_attempts}")

def play_again():
    choice = input("Do you want to play again? (yes/no): ").lower()
    return choice == 'yes'

def main_game():
    print("Welcome to the Guessing Game!")
    while True:
        settings = difficulty()
        number = generate_num(settings['range'])
        max_attempts = settings['attempts']
        attempts = 0

        while attempts < max_attempts:
            guess = get_user_guess()
            attempts += 1

            if guess == number:
                print("Congratulations! You guessed the correct number!")
                break
            else:
                hint(guess, number)

        display_score(attempts, max_attempts)

        if not play_again():
            break

    print("Adios")


main_game()
