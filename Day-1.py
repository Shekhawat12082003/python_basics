import random

def guess_the_number():
    print("Welcome to the Guess the Number game!")
    print("I'm thinking of a number between 1 and 10.")
    number = random.randint(1, 10)
    attempt = 0
    guess= 0
    number = random.randint(1,10)
    while guess != number:
        guess = int(input("Enter your guess: "))
        attempt += 1
        if guess < number:
            print("Too low! Try again.")
        elif guess > number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You've guessed the number {number} in {attempt} attempts.")
guess_the_number()