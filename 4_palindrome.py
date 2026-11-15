# Palindrome Number
num = int(input("Enter a number: "))

temp = num
reverse = 0

while temp > 0:
    digit = temp % 10
    reverse = reverse * 10 + digit
    temp //= 10

if num >= 0 and num == reverse:
    print(num, "is a Palindrome Number")
else:
    print(num, "is not a Palindrome Number")


# Palindrome String
text = input("Enter a string: ")

if text == text[::-1]:
    print(text, "is a Palindrome String")
else:
    print(text, "is not a Palindrome String")