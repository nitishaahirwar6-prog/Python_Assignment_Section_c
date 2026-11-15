import random

def reverse_guessing_game():
    print("\n--- Reverse Guessing Game ---")
    print("Think of a number between 1 and 100, and I will try to guess it!")
    print("Type 'high' if my guess is too high, 'low' if it's too low, and 'correct' if I got it right.\n")
    
    low = 1
    high = 100
    attempts = 0
    
    while low <= high:
        # Computer guesses the midpoint
        guess = (low + high) // 2
        attempts += 1
        
        print(f"My guess is: {guess}")
        feedback = input("Enter feedback ('high', 'low', 'correct'): ").strip().lower()
        
        if feedback == 'correct':
            print(f"Yay! I guessed your number {guess} in {attempts} attempts!")
            break
        elif feedback == 'high':
            high = guess - 1
        elif feedback == 'low':
            low = guess + 1
        else:
            print("Invalid feedback! Please type exactly 'high', 'low', or 'correct'.")
            attempts -= 1  # Don't count invalid attempts

if __name__ == "__main__":
    reverse_guessing_game()