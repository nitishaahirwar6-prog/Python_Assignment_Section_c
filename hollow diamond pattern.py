def print_hollow_diamond(n):
    if n % 2 == 0:
        print("Please enter an odd number for n.")
        return

    mid = n // 2

    # Upper half (including the middle row)
    for i in range(mid + 1):
        spaces_before = " " * (mid - i)
        if i == 0:
            print(spaces_before + "*")
        else:
            spaces_between = " " * (2 * i - 1)
            print(spaces_before + "*" + spaces_between + "*")

    # Lower half
    for i in range(mid - 1, -1, -1):
        spaces_before = " " * (mid - i)
        if i == 0:
            print(spaces_before + "*")
        else:
            spaces_between = " " * (2 * i - 1)
            print(spaces_before + "*" + spaces_between + "*")

# Taking input from user
n = int(input("Enter an odd number n for Hollow Diamond: "))
print_hollow_diamond(n)