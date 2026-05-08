class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        curr = float('inf')
        for num in prices:
            if num < curr:
                curr = num
            p = num - curr
            if p>profit:
                profit = p
        return profit