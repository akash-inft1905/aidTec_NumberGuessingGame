import random

def play_game():
    print("Welcome to the Number Guessing Game!")
    name = input("Enter your name: ")
    print(f"Hello, {name}!")
    
    while True:
        number = random.randint(1, 100)
        attempts = 10
        print("\nI'm thinking of a number between 1 and 100. You have 10 attempts to guess it.")

        for attempt in range(1, attempts + 1):
            guess = int(input("Enter your guess: "))

            if guess < number:
                print("Too low!")
            elif guess > number:
                print("Too high!")
            else:
                print(f"\nCongratulations, {name}! You guessed the correct number in {attempt} attempts!")
                break

            if attempt == attempts:
                print(f"\nSorry, {name}! You have used all your attempts. The number was {number}.")
        
        play_again = input("\nDo you want to play again? (yes/no): ")
        if play_again.lower() != "yes":
            break

play_game()
