def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    profit = 0
    for i in range(len(prices)):
        for j in range(i + 1, len(prices)):
            if prices[i] >= prices[j]:
                break
            profit = max(profit, (prices[j] - prices[i]))

    return profit


# prices = [7, 6, 4, 3, 1]
prices = [7, 1, 5, 3, 6, 4]

profit = maxProfit(prices)
print(profit)
