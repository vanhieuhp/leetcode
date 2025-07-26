def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    if len(prices) == 0:
        return 0

    profit = 0
    min = prices[0]
    for i in range(1, len(prices)):
        if prices[i] < min:
            min = prices[i]
        profit = max(profit, prices[i] - min)
    return profit


# prices = [7, 6, 4, 3, 1]
prices = [7, 1, 5, 3, 6, 4]

profit = maxProfit(prices)
print(profit)
