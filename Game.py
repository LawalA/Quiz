import random
import random

def guess_number_game():
    secret_number = random.randint(1, 100)
    print("Welcome to the Guess the Number game!")
    print("I'm thinking of a number between 1 and 100.")
    
    num_guesses = 0
    while True:
        guess = input("Take a guess: ")
        num_guesses += 1
        
        try:
            guess = int(guess)
        except ValueError:
            print("That's not a valid number. Try again.")
            continue
        
        if guess < secret_number:
            print("Too low. Try again.")
        elif guess > secret_number:
            print("Too high. Try again.")
        else:
            print(f"Congratulations! You guessed the number in {num_guesses} guesses.")
            break

guess_number_game()