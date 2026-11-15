while True:
    print("\n===== PYTHON MENU =====")
    print("1. Armstrong Number")
    print("2. Prime Number")
    print("3. Perfect Number")
    print("4. Palindrome")
    print("5. Fibonacci Series")
    print("6. Pattern Printing")
    print("7. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        num = int(input("Enter a number: "))
        total = sum(int(d) ** len(str(num)) for d in str(abs(num)))
        if num >= 0 and total == num:
            print("Armstrong Number")
        else:
            print("Not an Armstrong Number")

    elif choice == 2:
        num = int(input("Enter a number: "))
        if num > 1:
            for i in range(2, num):
                if num % i == 0:
                    print("Not a Prime Number")
                    break
            else:
                print("Prime Number")
        else:
            print("Not a Prime Number")

    elif choice == 3:
        num = int(input("Enter a number: "))
        total = 0
        for i in range(1, num):
            if num % i == 0:
                total += i
        if num > 0 and total == num:
            print("Perfect Number")
        else:
            print("Not a Perfect Number")

    elif choice == 4:
        value = input("Enter a number or string: ")
        if value == value[::-1]:
            print("Palindrome")
        else:
            print("Not a Palindrome")

    elif choice == 5:
        n = int(input("Enter number of terms: "))
        a, b = 0, 1
        for i in range(n):
            print(a, end=" ")
            a, b = b, a + b
        print()

    elif choice == 6:
        n = int(input("Enter rows: "))
        for i in range(1, n + 1):
            print("* " * i)

    elif choice == 7:
        print("Thank you!")
        break

    else:
        print("Invalid choice. Try again.")