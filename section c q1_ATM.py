def atm_simulation():
    balance = 5000.0  # Initial fixed balance[span_1](start_span)[span_1](end_span)
    correct_pin = "1234"  # Fixed PIN for verification[span_2](start_span)[span_2](end_span)
    
    # PIN verification before showing the menu[span_3](start_span)[span_3](end_span)
    entered_pin = input("Enter your 4-digit PIN: ")
    if entered_pin != correct_pin:
        print("Incorrect PIN! Access denied.")
        return

    while True:
        print("\n--- ATM Menu ---")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Change PIN")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == '1':
            print(f"Current Balance: ${balance}")
        elif choice == '2':
            amount = float(input("Enter amount to deposit: "))
            if amount > 0:
                balance += amount
                print(f"Successfully deposited ${amount}. New Balance: ${balance}")
            else:
                print("Invalid deposit amount!")
        elif choice == '3':
            amount = float(input("Enter amount to withdraw: "))
            if amount > balance:
                print("Error: Withdrawal exceeds current balance! Transaction rejected.")[span_4](start_span)[span_4](end_span)
            elif amount <= 0:
                print("Invalid withdrawal amount!")
            else:
                balance -= amount
                print(f"Successfully withdrew ${amount}. New Balance: ${balance}")
        elif choice == '4':
            new_pin = input("Enter new 4-digit PIN: ")
            if len(new_pin) == 4 and new_pin.isdigit():
                correct_pin = new_pin
                print("PIN changed successfully!")
            else:
                print("Invalid PIN format. Must be 4 digits.")
        elif choice == '5':
            print("Thank you for using the ATM. Goodbye!")
            break
        else:
            print("Invalid option! Please choose between 1 and 5.")

if __name__ == "__main__":
    atm_simulation()