a = int(input("Enter First Element: "))
b = int(input("Enter Second Element: "))

def gcd(a,b):
    while(a > 0 and b > 0):
        if (a > b) :
            a = a % b
        else:
            b = b % a
    if b == 0: 
        return a
    else:
        return b

def lcm(a,b):
    gcd_result = gcd(a,b)
    return (a * b)//gcd_result

print(" ")

gcd(a,b)
print(f"The HCF or GCD is {gcd(a,b)}")

lcm(a,b)
print(f"LCM of {a} and {b} is {lcm(a,b)}")