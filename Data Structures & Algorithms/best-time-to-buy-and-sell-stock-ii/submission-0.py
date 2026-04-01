class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        hold = max(prices)
        sell = 0
        ans = 0
        for num in prices:
            if num < hold:
                hold = num
            elif num>hold:
                sell = num
                p = sell - hold
                ans+=p
                hold = sell
        return ans