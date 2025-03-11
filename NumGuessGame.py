import random

class NumberGuessingGame:
    def __init__(self, lower=1, upper=100):
        self.lower = lower
        self.upper = upper
        self.number = random.randint(self.lower, self.upper)
        self.guesses = 0

    def guess(self, user_guess):
        self.guesses += 1
        if user_guess < self.number:
            return "Too low!"
        elif user_guess > self.number:
            return "Too high!"
        else:
            return "Correct!"

def play_game():
    game = NumberGuessingGame()
    print(f"Guess the number between {game.lower} and {game.upper}")
    while True:
        try:
            user_input = int(input("Enter your guess: "))
            result = game.guess(user_input)
            print(result)
            if result == "Correct!":
                print(f"You guessed it in {game.guesses} tries.")
                break
        except ValueError:
            print("Please enter a valid integer.")

if __name__ == "__main__":
    play_game()
