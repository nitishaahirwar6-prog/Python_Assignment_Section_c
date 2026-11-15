def print_butterfly(n):
    # Upper half of the butterfly
    for i in range(1, n + 1):
        left_stars = "*" * i
        spaces = " " * (2 * (n - i))
        right_stars = "*" * i
        print(left_stars + spaces + right_stars)

    # Lower half of the butterfly
    for i in range(n, 0, -1):
        left_stars = "*" * i
        spaces = " " * (2 * (n - i))
        right_stars = "*" * i
        print(left_stars + spaces + right_stars)

# Taking input from user
n = int(input("Enter the number n for Butterfly Pattern: "))
print_butterfly(n)