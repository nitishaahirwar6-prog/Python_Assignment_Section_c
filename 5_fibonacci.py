# Fibonacci using Loop
n = int(input("Enter number of terms: "))

a, b = 0, 1

print("Fibonacci Series using Loop:")

for i in range(n):
    print(a, end=" ")
    a, b = b, a + b

# Fibonacci using Recursion
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print("\nFibonacci Series using Recursion:")

for i in range(n):
    print(fibonacci(i), end=" ")

