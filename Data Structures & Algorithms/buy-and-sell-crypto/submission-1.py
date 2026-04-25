class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        L = 0
        maxProfit = 0

        for R in range(len(prices)):
            profit = prices[R] - prices[L]

            if profit < 0:
                L = R

            maxProfit = max(profit, maxProfit)

        return maxProfit