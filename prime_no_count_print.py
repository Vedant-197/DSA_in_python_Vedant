start = int(input("Enter Start Value: "))
end = int(input("Enter End value: "))
count = 0

for n in range(start,end + 1):
    if( n < 2):
        continue
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            break
    else: 
            print(n,end = " ")
            count += 1

print(f"\n Total Prime Numbers Between {start} and {end} : {count}")
