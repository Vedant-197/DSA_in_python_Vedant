n = int(input("Enter the Number: "))

def digi_in_num(n):
    while n != 0:
        digit = n % 10
        print(digit)
        n = n // 10

def digi_count(n):
    count = 0
    while n != 0:
        digit = n % 10
        count += 1
        n = n // 10
    print(f"Total Digits are {count}")

def digi_sum(n):
    sum = 0
    while n != 0:
        digit = n % 10
        sum += digit
        n = n // 10
    print(f"Sum of Digits is {sum}")

def digi_mul(n):
    multiply = 1
    while n != 0:
        digit = n % 10
        multiply *= digit
        n = n // 10
    print(f"Multiply of Digits is {multiply}")

digi_in_num(n)
digi_count(n)
digi_sum(n)
digi_mul(n)