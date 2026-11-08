'''The stock span is the number of consecutive days 
before and including the current day for 
which the stock price is less than or 
equal to the current day's price.'''

price = list(map(int, input("Enter stock prices: ").split()))
ans = [0] * len(price)
s = []

for i in range(len(price)):
    while len(s) > 0 and price[s[-1]] <= price[i]:
        s.pop()
    if len(s) == 0:
        ans[i] = i + 1
    else:
        ans[i] = i - s[-1]

    s.append(i)

print("Stock Span:", ans)