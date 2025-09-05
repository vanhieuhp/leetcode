from typing import List

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        cash, hold = 0, -prices[0]

        for price in prices[1:]:
            cash = max(cash, hold + price - fee)
            hold = max(hold, cash - price)
        
        return cash


prices = [1,3,2,8,4,9]
fee = 2

res = Solution().maxProfit(prices, fee)
print(res)