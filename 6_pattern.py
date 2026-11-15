n = int(input("Enter number of rows: "))

# Pattern 1: Right-angled Triangle
print("\nRight-angled Triangle:")
for i in range(1, n + 1):
    for j in range(i):
        print("*", end=" ")
    print()

# Pattern 2: Number Pattern
print("\nNumber Pattern:")
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

# Pattern 3: Simple Pyramid
print("\nPyramid Pattern:")
for i in range(1, n + 1):
    print(" " * (n - i) + "* " * i)