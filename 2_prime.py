num = int(input("Enter a number: "))

if num > 1:
    for i in range(2, num):
        if num % i == 0:
            print(num, "is not a Prime Number")
            break
    else:
        print(num, "is a Prime Number")
else:
    print(num, "is not a Prime Number")

limit = int(input("Enter the limit: "))

print("Prime numbers up to", limit, "are:")

for n in range(2, limit + 1):
    for i in range(2, n):
        if n % i == 0:
            break
    else:
        print(n, end=" ")