import random

number = random.randint(1, 100)
attempts = 7

print("Welcome to Number Guessing Game!")
print("Guess a number between 1 and 100")
print("You have 7 attempts.")

for i in range(attempts):
    guess = int(input("Enter your guess: "))

    if guess == number:
        print("Congratulations! You guessed correctly.")
        break
    elif guess < number:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")

else:
    print("Sorry! You have used all attempts.")
    print("The correct number was:", number)