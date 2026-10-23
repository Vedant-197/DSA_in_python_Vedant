n = int(input("Enter the Number: "))

def is_armstrong(n):
    dupli_n = n
    power = len(str(n))
    total = 0

    while n != 0:
        digit = n % 10
        total += (digit ** power)
        n = n // 10

    return total == dupli_n

if is_armstrong(n):
    print(f"{n} is an Armstrong Number")
else:
    print(f"{n} is not an Armstrong Number")
