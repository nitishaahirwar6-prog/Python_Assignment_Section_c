num = int(input("Enter a number: "))

total = 0

for i in range(1, num):
    if num % i == 0:
        total += i

if total == num and num > 0:
    print(num, "is a Perfect Number")
else:
    print(num, "is not a Perfect Number")

limit = int(input("Enter the limit: "))

print("Perfect numbers up to", limit, "are:")

for n in range(1, limit + 1):
    sum_divisors = 0

    for i in range(1, n):
        if n % i == 0:
            sum_divisors += i

    if sum_divisors == n:
        print(n, end=" ")