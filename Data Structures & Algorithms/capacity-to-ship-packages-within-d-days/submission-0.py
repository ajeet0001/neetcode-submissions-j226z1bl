class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l = max(weights)
        r = sum(weights)
        ans = r
        while l<=r:
            mid = (l+r)//2
            d = 1
            weight = 0
            for w in weights:
                weight += w
                if weight>mid:
                    d += 1
                    weight = w
            if d <= days:
                ans = min(ans,mid)
                r = mid-1
            else:
                l = mid+1
        return ans

