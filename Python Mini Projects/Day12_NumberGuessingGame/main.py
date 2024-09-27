import random
import art

print(art.logo)

def number_guess_game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    difficulty_of_game = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
#
    if difficulty_of_game == "easy":
        attempts_left = 10
    else:
        attempts_left = 5

    number_to_guess = random.randint(1, 100)
    print(f"You have {attempts_left} remaining to guess the number.")
    while attempts_left > 0:
        guess_number = int(input("Make a guess: "))

        if guess_number > number_to_guess:
            print("Too high")
            attempts_left -= 1
        elif guess_number < number_to_guess:
            print("Too low.")
            attempts_left -= 1
        else:
            print(f"Congratulations! You guessed the number {number_to_guess}. You win!")
            return

        if attempts_left > 0:
            print(f"You have {attempts_left} attempts remaining")
        else:
            print(f"You have no more attempts left. The number was {number_to_guess}. You lose.")

number_guess_game()