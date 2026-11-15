num = int(input("Enter a number: "))

if num < 0:
    print("Please enter a positive number")
else:
    temp = num
    total = 0
    power = len(str(num))

    while temp > 0:
        digit = temp % 10
        total += digit ** power
        temp //= 10

    if total == num:
        print(num, "is an Armstrong number")
    else:
        print(num, "is not an Armstrong number")