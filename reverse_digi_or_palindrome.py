n = int(input("Enter the Number: "))

def reverse(n):
    rev_num = 0

    while n != 0:
        digit = n % 10
        rev_num = rev_num * 10 + digit
        n = n // 10

    return rev_num

def is_palindrome(n):
    if n < 0:
        return False

    return reverse(n) == n

print("Reversed Number:", reverse(n))

if is_palindrome(n):
    print(f"{n} is a Palindrome Number")
else:
    print(f"{n} is not a Palindrome Number")
