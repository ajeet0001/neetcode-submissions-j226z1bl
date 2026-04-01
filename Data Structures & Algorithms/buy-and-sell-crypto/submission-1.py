class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        min_price = float('inf')
        for price in prices:
            if price < min_price:
                min_price = price
            profit = price - min_price

            if profit>maxP:
                maxP = profit
        return maxP