#we have to find maximum profit from given prices array
import numpy as n
def maxprofit(prices):
    maximum_profit = 0
    bestbuy = prices[0]

    for i in range(1, len(prices)):
        if prices[i] > bestbuy:
            maximum_profit = max(maximum_profit, prices[i] - bestbuy)

        bestbuy = min(bestbuy, prices[i])
    return maximum_profit


prices = n.array(list(map(int, input("Enter the prices separated by space: ").split())))
maximum_profit = maxprofit(prices)
print("Maximum Profit:", maximum_profit)


       