import random

def guess_the_number():
    print("🎯 Welcome to the Guess the Number Game with Difficulty Levels!")
    print("Choose difficulty: Easy (E), Medium (M), Hard (H)")

    while True:
        difficulty = input("Enter E, M, or H: ").strip().upper()
        if difficulty == "E":
            max_number = 10
            max_attempts = 7
            break
        elif difficulty == "M":
            max_number = 50
            max_attempts = 5
            break
        elif difficulty == "H":
            max_number = 100
            max_attempts = 3
            break
        else:
            print("❌ Invalid choice, please enter E, M, or H.")

    secret_number = random.randint(1, max_number)
    attempts = 0

    print(f"I'm thinking of a number between 1 and {max_number}. You have {max_attempts} attempts to guess it.")

    while attempts < max_attempts:
        try:
            guess = int(input(f"Attempt {attempts + 1}/{max_attempts} - Enter your guess: "))
            attempts += 1

            if guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                print(f"🎉 Congratulations! You guessed it in {attempts} attempts.")
                break
        except ValueError:
            print("❌ Please enter a valid number.")
    else:
        print(f"😞 Sorry, you've used all {max_attempts} attempts. The number was {secret_number}.")

guess_the_number()
