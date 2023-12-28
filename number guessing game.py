import random

def number_guessing_game():
    print("Try to guess the number from 1 to 100")
    secret_number, max_attempts, attempts = random.randint(1, 100), 10, 0

    while attempts < max_attempts:
        try:
            guess = int(input("Your guess: "))
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue

        attempts += 1
        if guess == secret_number:
            print(f"Congratulations! You guessed the correct number {secret_number} in {attempts} attempts.")
            break
        elif guess < secret_number:
            print("Too low. Try again.")
        else:
            print("Too high. Try again.")

    if attempts == max_attempts:
        print(f"Max attempts exceeded. The correct number was {secret_number}.")

if __name__ == "__main__":
    number_guessing_game()
