import random

def guessing_game_with_hints():
    print("\n--- Guessing Game with Hints & Scoring ---")
    print("I have selected a random number between 1 and 100.")
    print("Try to guess it! You will get hints and a score based on your attempts.\n")
    
    target_number = random.randint(1, 100)
    attempts = 0
    max_score = 100
    
    while True:
        try:
            guess = int(input("Enter your guess (1-100): "))
        except ValueError:
            print("Please enter a valid integer!")
            continue
            
        attempts += 1
        
        if guess == target_number:
            # Calculate score (subtracting 10 points for each extra attempt)
            score = max(10, max_score - (attempts - 1) * 10)
            print(f"🎉 Congratulations! You guessed the number {target_number} correctly.")
            print(f"Total Attempts: {attempts}")
            print(f"Your Score: {score}/100")
            break
        elif guess < target_number:
            print("📉 Too low! Try a higher number.")
        else:
            print("📈 Too high! Try a lower number.")

if __name__ == "__main__":
    guessing_game_with_hints()